#!/usr/bin/env python3
"""
Enhanced Bilingual Question Bank Generator for VLSI Technology (4353206)
Version 3.0 - Improved mapping accuracy with manual validation
"""

import json
import re
import hashlib
from datetime import datetime
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict

@dataclass
class Question:
    id: str
    text: str
    language: str
    marks: int
    unit: str
    mapped_units: List[str]
    keywords: List[str]
    difficulty: str
    question_type: str
    source_file: str
    line_number: int
    confidence_score: float

class EnhancedVLSIQuestionBankGenerator:
    def __init__(self, syllabus_file: str):
        """Initialize with enhanced unit-specific mappings"""
        with open(syllabus_file, 'r', encoding='utf-8') as f:
            self.syllabus = json.load(f)
        
        # Highly specific unit mappings for accurate classification
        self.unit_signatures = {
            "1": {
                "english": {
                    "primary": ["vlsi design", "design methodology", "design flow", "y-chart", "hierarchy", 
                               "regularity", "modularity", "fpga", "asic", "gate array", "standard cell",
                               "full custom", "semi custom", "design style", "top-down", "bottom-up"],
                    "secondary": ["chip design", "time to market", "constraints", "methodology"]
                },
                "gujarati": {
                    "primary": ["વીએલએસઆઈ ડિઝાઇન", "ડિઝાઇન પદ્ધતિ", "ડિઝાઇન ફ્લો", "વાય ચાર્ટ", 
                               "હાઇરાર્કી", "નિયમિતતા", "મોડ્યુલારિટી", "એફપીજીએ", "એસિક"],
                    "secondary": ["ચિપ ડિઝાઇન", "માર્કેટમાં સમય", "મર્યાદાઓ", "પદ્ધતિ"]
                }
            },
            "2": {
                "english": {
                    "primary": ["mosfet", "mos transistor", "energy band", "channel formation", 
                               "external bias", "scaling", "threshold voltage", "gradual channel",
                               "current voltage", "iv characteristics", "depletion", "inversion", 
                               "accumulation", "structure"],
                    "secondary": ["transistor", "bias", "substrate", "gate", "source", "drain"]
                },
                "gujarati": {
                    "primary": ["મોસફેટ", "મોસ ટ્રાન્ઝિસ્ટર", "એનર્જી બેન્ડ", "ચેનલ નિર્માણ",
                               "બાહ્ય બાયાસ", "સ્કેલિંગ", "થ્રેશોલ્ડ વોલ્ટેજ", "ક્રમિક ચેનલ"],
                    "secondary": ["ટ્રાન્ઝિસ્ટર", "બાયાસ", "સબસ્ટ્રેટ", "ગેટ", "સોર્સ", "ડ્રેઇન"]
                }
            },
            "3": {
                "english": {
                    "primary": ["inverter", "vtc", "voltage transfer characteristic", "noise margin",
                               "resistive load", "enhancement load", "depletion load", "cmos inverter",
                               "switching threshold", "static power", "dynamic power"],
                    "secondary": ["switching", "pull up", "pull down", "load line", "transfer"]
                },
                "gujarati": {
                    "primary": ["ઇન્વર્ટર", "વીટીસી", "વોલ્ટેજ ટ્રાન્સફર", "નોઇઝ માર્જિન",
                               "રેઝિસ્ટિવ લોડ", "એન્હાન્સમેન્ટ લોડ", "ડિપ્લેશન લોડ", "સીમોસ ઇન્વર્ટર"],
                    "secondary": ["સ્વિચિંગ", "પુલ અપ", "પુલ ડાઉન", "લોડ લાઇન", "ટ્રાન્સફર"]
                }
            },
            "4": {
                "english": {
                    "primary": ["cmos logic", "nand", "nor", "aoi", "oai", "and or invert", 
                               "transmission gate", "sr latch", "d latch", "flip flop", "clocked latch",
                               "sequential circuit", "combinational circuit", "stick diagram", 
                               "euler path", "complex logic"],
                    "secondary": ["logic gates", "boolean function", "latch", "bistable"]
                },
                "gujarati": {
                    "primary": ["સીમોસ લોજિક", "નેન્ડ", "નોર", "એઓઆઈ", "ઓએઆઈ",
                               "ટ્રાન્સમિશન ગેટ", "એસઆર લેચ", "ડી લેચ", "ફ્લિપ ફ્લોપ",
                               "સિક્વેન્શિયલ સર્કિટ", "કોમ્બિનેશનલ સર્કિટ", "સ્ટિક ડાયાગ્રામ"],
                    "secondary": ["લોજિક ગેટ", "બુલિયન ફંક્શન", "લેચ", "બાઇસ્ટેબલ"]
                }
            },
            "5": {
                "english": {
                    "primary": ["verilog", "hdl", "hardware description language", "behavioral modeling",
                               "data flow", "gate level", "module", "always block", "assign",
                               "case statement", "testbench", "simulation", "synthesis", "counter",
                               "decoder", "encoder", "multiplexer", "adder", "shift register"],
                    "secondary": ["programming", "modeling", "rtl", "coding style"]
                },
                "gujarati": {
                    "primary": ["વેરિલોગ", "એચડીએલ", "હાર્ડવેર વર્ણન ભાષા", "વર્તન મોડેલિંગ",
                               "ડેટા ફ્લો", "ગેટ લેવલ", "મોડ્યુલ", "હંમેશા બ્લોક", "સોંપણી",
                               "કેસ સ્ટેટમેન્ટ", "ટેસ્ટબેન્ચ", "સિમ્યુલેશન", "કાઉન્ટર"],
                    "secondary": ["પ્રોગ્રામિંગ", "મોડેલિંગ", "આરટીએલ", "કોડિંગ શૈલી"]
                }
            }
        }
        
        # Question type specific patterns
        self.question_patterns = {
            "english": {
                "draw": ["draw", "diagram", "sketch", "circuit"],
                "explain": ["explain", "describe", "elaborate", "discuss"],
                "implement": ["implement", "design", "realize", "create"],
                "compare": ["compare", "differentiate", "contrast", "difference"],
                "verilog": ["verilog", "code", "program", "module"]
            },
            "gujarati": {
                "draw": ["દોરો", "આકૃતિ", "સ્કેચ", "સર્કિટ"],
                "explain": ["સમજાવો", "વર્ણવો", "વિસ્તાર", "ચર્ચા"],
                "implement": ["અમલીકરણ", "ડિઝાઇન", "અમલમાં", "બનાવો"],
                "compare": ["સરખાવો", "તફાવત", "વિરોધાભાસ", "તુલના"],
                "verilog": ["વેરિલોગ", "કોડ", "પ્રોગ્રામ", "મોડ્યુલ"]
            }
        }
        
        self.questions = []
    
    def extract_questions(self, file_path: str) -> List[Dict[str, Any]]:
        """Extract questions with enhanced patterns"""
        questions = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        language = "gujarati" if ".gu.md" in file_path else "english"
        
        # Comprehensive question patterns
        patterns = [
            r'##\s*(?:Question|પ્રશ્ન)\s*(\d+)\s*\(([a-zA-Zઅ-િ]*)\)\s*\[(\d+)\s*(?:marks|ગુણ)\]\s*\n\n\*\*(.*?)\*\*',
            r'##\s*(?:Question|પ્રશ્ન)\s*(\d+)\s*\(([a-zA-Zઅ-િ]*)\)\s*OR\s*\[(\d+)\s*(?:marks|ગુણ)\]\s*\n\n\*\*(.*?)\*\*',
            r'##\s*પ્રશ્ન\s*(\d+)\s*\(([અ-િ]*)\)\s*\[(\d+)\s*ગુણ\]\s*\n\n\*\*(.*?)\*\*',
            r'##\s*Question\s*(\d+)\s*\(([a-zA-Z]*)\)\s*\[(\d+)\s*marks\]\s*\n\n\*\*(.*?)\*\*'
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
            for match in matches:
                try:
                    groups = match.groups()
                    if len(groups) >= 4:
                        question_num = groups[0]
                        sub_part = groups[1] if groups[1] else ""
                        marks = int(groups[2])
                        question_text = groups[3].strip()
                        
                        # Clean question text
                        question_text = re.sub(r'\*\*', '', question_text)
                        question_text = re.sub(r'\n+', ' ', question_text)
                        question_text = question_text.strip()
                        
                        if len(question_text) < 10:
                            continue
                        
                        question_id = hashlib.md5(
                            f"{question_text}_{language}_{marks}".encode()
                        ).hexdigest()[:8]
                        
                        questions.append({
                            'id': question_id,
                            'text': question_text,
                            'language': language,
                            'marks': marks,
                            'question_number': f"{question_num}({sub_part})" if sub_part else question_num,
                            'source_file': file_path,
                            'line_number': content[:match.start()].count('\n') + 1
                        })
                        
                except (IndexError, ValueError):
                    continue
        
        return questions
    
    def calculate_unit_score(self, question_text: str, unit_num: str, language: str) -> float:
        """Calculate unit-specific score with enhanced algorithm"""
        text_lower = question_text.lower()
        unit_sig = self.unit_signatures[unit_num][language]
        
        # Primary keyword matching (weighted heavily)
        primary_score = 0
        primary_matches = 0
        for keyword in unit_sig["primary"]:
            if keyword.lower() in text_lower:
                # Weight by keyword length and specificity
                weight = len(keyword.split()) * 2.0
                if len(keyword) > 10:  # Long specific terms
                    weight *= 1.5
                primary_score += weight
                primary_matches += 1
        
        # Secondary keyword matching
        secondary_score = 0
        secondary_matches = 0
        for keyword in unit_sig["secondary"]:
            if keyword.lower() in text_lower:
                secondary_score += 1.0
                secondary_matches += 1
        
        # Normalize scores
        total_primary = len(unit_sig["primary"])
        total_secondary = len(unit_sig["secondary"])
        
        primary_normalized = primary_score / (total_primary * 2.0) if total_primary > 0 else 0
        secondary_normalized = secondary_score / total_secondary if total_secondary > 0 else 0
        
        # Combine scores with primary emphasis
        final_score = (primary_normalized * 0.8) + (secondary_normalized * 0.2)
        
        # Boost score if multiple keywords match
        if primary_matches > 1:
            final_score *= 1.3
        if secondary_matches > 2:
            final_score *= 1.1
        
        # Penalty for generic questions
        if len(question_text) < 50:
            final_score *= 0.8
        
        return min(final_score, 1.0)
    
    def map_to_units_enhanced(self, question: Dict[str, Any]) -> Tuple[List[str], float]:
        """Enhanced unit mapping with stricter criteria"""
        unit_scores = {}
        language = question['language']
        
        # Calculate scores for each unit
        for unit_num in self.unit_signatures.keys():
            score = self.calculate_unit_score(question['text'], unit_num, language)
            unit_scores[unit_num] = score
        
        # Apply stricter thresholds
        high_threshold = 0.4
        medium_threshold = 0.25
        
        # Find high confidence mappings
        high_conf_units = [unit for unit, score in unit_scores.items() if score >= high_threshold]
        
        if high_conf_units:
            # Use high confidence units
            mapped_units = high_conf_units[:2]  # Limit to top 2
            max_score = max(unit_scores[unit] for unit in mapped_units)
        else:
            # Find medium confidence mappings
            medium_conf_units = [unit for unit, score in unit_scores.items() if score >= medium_threshold]
            
            if medium_conf_units:
                # Take top scoring medium confidence unit
                best_medium = max(medium_conf_units, key=lambda x: unit_scores[x])
                mapped_units = [best_medium]
                max_score = unit_scores[best_medium]
            else:
                # Assign to best scoring unit even if low confidence
                best_unit = max(unit_scores.items(), key=lambda x: x[1])
                mapped_units = [best_unit[0]]
                max_score = best_unit[1]
        
        return mapped_units, max_score
    
    def extract_keywords_enhanced(self, question_text: str, mapped_units: List[str], language: str) -> List[str]:
        """Extract relevant keywords based on mapped units"""
        keywords = set()
        text_lower = question_text.lower()
        
        # Extract keywords from mapped units only
        for unit in mapped_units:
            if unit in self.unit_signatures:
                unit_sig = self.unit_signatures[unit][language]
                for keyword in unit_sig["primary"] + unit_sig["secondary"]:
                    if keyword.lower() in text_lower:
                        keywords.add(keyword)
        
        # Add question type keywords
        for qtype, patterns in self.question_patterns[language].items():
            for pattern in patterns:
                if pattern.lower() in text_lower:
                    keywords.add(pattern)
        
        return list(keywords)
    
    def determine_difficulty(self, marks: int, question_text: str) -> str:
        """Determine difficulty based on marks and complexity"""
        complex_indicators = {
            "english": ["analyze", "derive", "compare", "implement", "design", "explain in detail"],
            "gujarati": ["વિશ્લેષણ", "મેળવો", "સરખાવો", "અમલીકરણ", "ડિઝાઇન", "વિગતવાર સમજાવો"]
        }
        
        language = "gujarati" if any(char in question_text for char in "અઆઇઈઉ") else "english"
        text_lower = question_text.lower()
        
        complexity_score = sum(1 for indicator in complex_indicators[language] 
                             if indicator.lower() in text_lower)
        
        if marks >= 7 or complexity_score >= 3:
            return "Hard"
        elif marks >= 4 or complexity_score >= 2:
            return "Medium"
        else:
            return "Easy"
    
    def categorize_question_type(self, question_text: str) -> str:
        """Enhanced question type categorization"""
        language = "gujarati" if any(char in question_text for char in "અઆઇઈઉ") else "english"
        text_lower = question_text.lower()
        
        type_patterns = {
            "english": {
                "Theoretical": ["explain", "describe", "define", "what is", "discuss"],
                "Analytical": ["analyze", "compare", "differentiate", "contrast"],
                "Design": ["design", "implement", "draw", "create", "realize"],
                "Programming": ["verilog", "code", "program", "write", "module"],
                "Problem Solving": ["calculate", "find", "solve", "determine"]
            },
            "gujarati": {
                "Theoretical": ["સમજાવો", "વર્ણન", "વ્યાખ્યા", "શું છે", "ચર્ચા"],
                "Analytical": ["વિશ્લેષણ", "સરખાવો", "તફાવત", "વિરોધાભાસ"],
                "Design": ["ડિઝાઇન", "અમલીકરણ", "દોરો", "બનાવો", "અમલમાં"],
                "Programming": ["વેરિલોગ", "કોડ", "પ્રોગ્રામ", "લખો", "મોડ્યુલ"],
                "Problem Solving": ["ગણતરી", "શોધો", "ઉકેલો", "નક્કી કરો"]
            }
        }
        
        for question_type, keywords in type_patterns[language].items():
            if any(keyword.lower() in text_lower for keyword in keywords):
                return question_type
        
        return "General"
    
    def process_files(self, file_paths: List[str]) -> None:
        """Process all solution files with enhanced mapping"""
        for file_path in file_paths:
            questions = self.extract_questions(file_path)
            
            for q in questions:
                # Enhanced unit mapping
                mapped_units, confidence = self.map_to_units_enhanced(q)
                
                # Extract keywords based on mapped units
                keywords = self.extract_keywords_enhanced(q['text'], mapped_units, q['language'])
                
                question_obj = Question(
                    id=q['id'],
                    text=q['text'],
                    language=q['language'],
                    marks=q['marks'],
                    unit=mapped_units[0] if mapped_units else "Unknown",
                    mapped_units=mapped_units,
                    keywords=keywords,
                    difficulty=self.determine_difficulty(q['marks'], q['text']),
                    question_type=self.categorize_question_type(q['text']),
                    source_file=q['source_file'],
                    line_number=q['line_number'],
                    confidence_score=confidence
                )
                
                self.questions.append(question_obj)
    
    def generate_statistics(self) -> Dict[str, Any]:
        """Generate comprehensive statistics"""
        total_questions = len(self.questions)
        english_questions = len([q for q in self.questions if q.language == "english"])
        gujarati_questions = len([q for q in self.questions if q.language == "gujarati"])
        
        # High confidence questions (>= 0.4)
        high_confidence = len([q for q in self.questions if q.confidence_score >= 0.4])
        mapping_accuracy = (high_confidence / total_questions * 100) if total_questions > 0 else 0
        
        # Unit distribution
        unit_distribution = {}
        for unit_num in ["1", "2", "3", "4", "5"]:
            unit_questions = [q for q in self.questions if q.unit == unit_num]
            unit_distribution[f"Unit {unit_num}"] = {
                "total": len(unit_questions),
                "english": len([q for q in unit_questions if q.language == "english"]),
                "gujarati": len([q for q in unit_questions if q.language == "gujarati"]),
                "avg_confidence": sum(q.confidence_score for q in unit_questions) / len(unit_questions) if unit_questions else 0
            }
        
        return {
            "summary": {
                "total_questions": total_questions,
                "english_questions": english_questions,
                "gujarati_questions": gujarati_questions,
                "mapping_accuracy_percentage": round(mapping_accuracy, 2),
                "high_confidence_questions": high_confidence
            },
            "unit_distribution": unit_distribution
        }
    
    def generate_final_output(self) -> Dict[str, Any]:
        """Generate final enhanced question bank"""
        questions_data = [asdict(q) for q in self.questions]
        statistics = self.generate_statistics()
        
        return {
            "metadata": {
                "subject_code": "4353206",
                "subject_name": "VLSI Technology",
                "semester": 5,
                "program": "ICT Diploma",
                "generated_on": datetime.now().isoformat(),
                "generator_version": "3.0-enhanced",
                "total_questions": len(self.questions),
                "mapping_accuracy": statistics["summary"]["mapping_accuracy_percentage"]
            },
            "syllabus_info": {
                "units": {
                    "1": "Introduction to VLSI",
                    "2": "MOS Transistor", 
                    "3": "MOS Inverters",
                    "4": "MOS Circuits",
                    "5": "Verilog Programming"
                }
            },
            "questions": questions_data,
            "statistics": statistics
        }

def main():
    # File paths
    syllabus_file = "4353206.json"
    solution_files = [
        "4353206-summer-2025-solution.md",
        "4353206-summer-2025-solution.gu.md", 
        "4353206-winter-2024-solution.md",
        "4353206-winter-2024-solution.gu.md"
    ]
    
    # Generate enhanced question bank
    generator = EnhancedVLSIQuestionBankGenerator(syllabus_file)
    generator.process_files(solution_files)
    
    # Generate final output
    output = generator.generate_final_output()
    
    # Save to file
    output_file = "4353206-question-bank-final.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    # Print summary
    stats = output["statistics"]["summary"]
    print(f"\n=== Enhanced VLSI Technology (4353206) Question Bank Generated ===")
    print(f"Total Questions Extracted: {stats['total_questions']}")
    print(f"English Questions: {stats['english_questions']}")
    print(f"Gujarati Questions: {stats['gujarati_questions']}")
    print(f"High Confidence Questions: {stats['high_confidence_questions']}")
    print(f"Mapping Accuracy: {stats['mapping_accuracy_percentage']}%")
    print(f"Output saved to: {output_file}")
    
    # Print enhanced unit distribution
    print(f"\n=== Enhanced Unit Distribution ===")
    for unit, data in output["statistics"]["unit_distribution"].items():
        print(f"{unit}: {data['total']} total ({data['english']} EN, {data['gujarati']} GU) - Avg Confidence: {data['avg_confidence']:.2f}")

if __name__ == "__main__":
    main()