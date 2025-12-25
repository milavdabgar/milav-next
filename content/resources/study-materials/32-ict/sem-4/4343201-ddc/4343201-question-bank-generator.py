#!/usr/bin/env python3
"""
Enhanced Question Bank Generator for Digital and Data Communication (4343201)
Comprehensive bilingual question extraction and mapping system for DDC
"""

import json
import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional
from collections import defaultdict, Counter
import unicodedata
from dataclasses import dataclass, asdict
import hashlib

@dataclass
class Question:
    """Question data structure"""
    id: str
    text: str
    language: str  # 'english' or 'gujarati'
    marks: int
    source_file: str
    exam_year: str
    exam_season: str
    unit: Optional[str] = None
    topics: List[str] = None
    confidence: float = 0.0

class EnhancedDDCQuestionBankGenerator:
    """Enhanced question bank generator for Digital and Data Communication"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.syllabus_data = {}
        self.questions = []
        
        # Enhanced bilingual keyword mappings for Digital and Data Communication
        self.unit_keywords = {
            "Unit-I": {
                "english": [
                    # Digital communication basics
                    "digital communication", "system", "block diagram", "source", "channel", 
                    "transmitter", "receiver", "repeater", "elements",
                    
                    # Channel characteristics
                    "bit rate", "baud rate", "bandwidth", "repeater distance", "channel characteristics",
                    "communication channel", "telephone channel", "coaxial cable", "optical fiber",
                    "wireless channel", "satellite channel",
                    
                    # Communication types and modes
                    "broadcasting", "point to point", "simplex", "duplex", "communication modes",
                    "basic modes", "broad casting", "point to point communication",
                    
                    # Multiplexing
                    "multiplexing", "TDM", "FDM", "CDM", "time division", "frequency division",
                    "code division", "need of multiplexing", "methods of multiplexing",
                    
                    # System limitations and advantages
                    "fundamental limitation", "digital system", "noise", "equipment",
                    "advantages", "disadvantages", "digital communication system"
                ],
                "gujarati": [
                    # ડિજિટલ કોમ્યુનિકેશન મૂળભૂતો
                    "ડિજિટલ કોમ્યુનિકેશન", "સિસ્ટમ", "બ્લોક ડાયાગ્રામ", "સોર્સ", "ચેનલ",
                    "ટ્રાન્સમિટર", "રિસીવર", "રીપીટર", "તત્વો", "ઘટકો",
                    
                    # ચેનલ લાક્ષણિકતાઓ
                    "બિટ રેટ", "બાઉડ રેટ", "બેન્ડવિડ્થ", "રીપીટર અંતર", "ચેનલ લાક્ષણિકતાઓ",
                    "કોમ્યુનિકેશન ચેનલ", "ટેલિફોન ચેનલ", "કોએક્સિયલ કેબલ", "ઓપ્ટિકલ ફાઇબર",
                    "વાયરલેસ ચેનલ", "સેટેલાઇટ ચેનલ",
                    
                    # કોમ્યુનિકેશન પ્રકારો અને મોડ્સ
                    "બ્રોડકાસ્ટિંગ", "પોઈન્ટ ટુ પોઈન્ટ", "સિમ્પ્લેક્સ", "ડુપ્લેક્સ", "કોમ્યુનિકેશન મોડ્સ",
                    "મૂળભૂત મોડ્સ", "બ્રોડ કાસ્ટિંગ", "પોઈન્ટ ટુ પોઈન્ટ કમ્યુનિકેશન",
                    
                    # મલ્ટિપ્લેક્સિંગ
                    "મલ્ટિપ્લેક્સિંગ", "TDM", "FDM", "CDM", "ટાઇમ ડિવિઝન", "ફ્રીક્વન્સી ડિવિઝન",
                    "કોડ ડિવિઝન", "મલ્ટિપ્લેક્સિંગની જરૂર", "મલ્ટિપ્લેક્સિંગની પદ્ધતિઓ",
                    
                    # સિસ્ટમ મર્યાદાઓ અને ફાયદાઓ
                    "મૂળભૂત મર્યાદા", "ડિજિટલ સિસ્ટમ", "નોઇઝ", "ઉપકરણો", "સાધનો",
                    "ફાયદા", "ગેરફાયદા", "ડિજિટલ કોમ્યુનિકેશન સિસ્ટમ"
                ]
            },
            
            "Unit-II": {
                "english": [
                    # Digital modulation techniques
                    "digital modulation", "modulation techniques", "shift keying", "ASK", "FSK", "PSK", "QPSK",
                    "amplitude shift keying", "frequency shift keying", "phase shift keying",
                    "quadrature phase shift keying", "binary phase shift keying", "BPSK",
                    
                    # Modulation characteristics
                    "generation", "detection", "reception", "bandwidth", "constellation diagram",
                    "waveforms", "modulator", "demodulator", "coherent", "non-coherent",
                    
                    # QAM and advanced modulation
                    "QAM", "quadrature amplitude modulation", "16-QAM", "principle",
                    "constellation", "advantages", "disadvantages", "comparison",
                    
                    # Modulation analysis
                    "compare", "salient features", "summarize", "explain generation",
                    "draw waveform", "block diagram", "working principle"
                ],
                "gujarati": [
                    # ડિજિટલ મોડ્યુલેશન તકનીકો
                    "ડિજિટલ મોડ્યુલેશન", "મોડ્યુલેશન તકનીકો", "શિફ્ટ કીઇંગ", "ASK", "FSK", "PSK", "QPSK",
                    "એમ્પ્લિટ્યુડ શિફ્ટ કીઇંગ", "ફ્રીક્વન્સી શિફ્ટ કીઇંગ", "ફેઝ શિફ્ટ કીઇંગ",
                    "ક્વાડરેચર ફેઝ શિફ્ટ કીઇંગ", "બાઇનરી ફેઝ શિફ્ટ કીઇંગ", "BPSK",
                    
                    # મોડ્યુલેશન લાક્ષણિકતાઓ
                    "જનરેશન", "ડિટેક્શન", "રિસેપ્શન", "બેન્ડવિડ્થ", "નક્ષત્ર આકૃતિ", "કોન્સ્ટેલેશન",
                    "વેવફોર્મ", "મોડ્યુલેટર", "ડિમોડ્યુલેટર", "કોહેરેંટ", "નોન-કોહેરેંટ",
                    
                    # QAM અને અદ્યતન મોડ્યુલેશન
                    "QAM", "ક્વાડરેચર એમ્પ્લિટ્યુડ મોડ્યુલેશન", "16-QAM", "સિદ્ધાંત",
                    "નક્ષત્ર આકૃતિ", "ફાયદા", "ગેરફાયદા", "સરખામણી",
                    
                    # મોડ્યુલેશન વિશ્લેષણ
                    "સરખામણી", "મુખ્ય લક્ષણો", "સારાંશ", "જનરેશન સમજાવો",
                    "વેવફોર્મ દોરો", "બ્લોક ડાયાગ્રામ", "કાર્યસિદ્ધાંત"
                ]
            },
            
            "Unit-III": {
                "english": [
                    # Information theory basics
                    "information theory", "probability", "entropy", "information", "mutual information",
                    "significance of probability", "channel capacity", "SNR", "signal to noise ratio",
                    "shannon", "channel capacity formula",
                    
                    # Source coding
                    "source coding", "huffman code", "shannon fano code", "coding techniques",
                    "huffman coding", "shannon-fano", "variable length", "prefix code",
                    "compression", "lossless", "encoding", "decoding",
                    
                    # Channel coding and error control
                    "channel coding", "error detection", "error correction", "parity", "checksum",
                    "hamming code", "cyclic redundancy check", "CRC", "error causes", "error effect",
                    
                    # Line coding
                    "line coding", "line codes", "NRZ", "RZ", "manchester", "AMI",
                    "unipolar", "polar", "bipolar", "classification", "properties",
                    "selection", "comparison", "waveform"
                ],
                "gujarati": [
                    # માહિતી સિદ્ધાંત મૂળભૂતો
                    "માહિતી સિદ્ધાંત", "સંભાવના", "એન્ટ્રોપી", "માહિતી", "પરસ્પર માહિતી",
                    "સંભાવનાનું મહત્વ", "ચેનલ ક્ષમતા", "SNR", "સિગ્નલ ટુ નોઇઝ રેશિયો",
                    "શેનોન", "ચેનલ ક્ષમતા ફોર્મ્યુલા",
                    
                    # સોર્સ કોડિંગ
                    "સોર્સ કોડિંગ", "હફમેન કોડ", "શેનોન ફાડો કોડ", "કોડિંગ તકનીકો",
                    "હફમેન કોડિંગ", "શેનોન-ફાડો", "વેરિએબલ લેન્થ", "પ્રીફિક્સ કોડ",
                    "કમ્પ્રેશન", "લોસલેસ", "એન્કોડિંગ", "ડીકોડિંગ",
                    
                    # ચેનલ કોડિંગ અને એરર કંટ્રોલ
                    "ચેનલ કોડિંગ", "એરર ડિટેક્શન", "એરર કરેક્શન", "પેરિટી", "ચેકસમ",
                    "હેમિંગ કોડ", "સાયક્લિક રિડન્ડન્સી ચેક", "CRC", "એરરના કારણો", "એરરની અસર",
                    
                    # લાઇન કોડિંગ
                    "લાઇન કોડિંગ", "લાઇન કોડ્સ", "NRZ", "RZ", "મેનચેસ્ટર", "AMI",
                    "યુનિપોલર", "પોલર", "બાયપોલર", "વર્ગીકરણ", "પ્રોપર્ટીઝ",
                    "પસંદગી", "સરખામણી", "વેવફોર્મ"
                ]
            },
            
            "Unit-IV": {
                "english": [
                    # Data communication basics
                    "data communication", "characteristics", "components", "data transmission",
                    "transmission techniques", "transmission mode", "simplex", "half duplex", "full duplex",
                    
                    # Serial and parallel communication
                    "serial communication", "parallel communication", "synchronous", "asynchronous",
                    "serial data communication", "parallel data communication",
                    
                    # Data representation and standards
                    "data representation", "RS-232", "RS-422", "RS-485", "standards",
                    "communication ports", "USB", "HDMI", "RCA", "ethernet", "industrial standards",
                    
                    # Multimedia communication
                    "multimedia communication", "multimedia systems", "elements", "model",
                    "multimedia processing", "digital media", "signal processing",
                    "audio formats", "video formats", "image formats", "file formats",
                    
                    # Communication protocols and interfaces
                    "protocols", "interfaces", "pin diagram", "voltage levels", "connector",
                    "communication standards", "data formats"
                ],
                "gujarati": [
                    # ડેટા કોમ્યુનિકેશન મૂળભૂતો
                    "ડેટા કોમ્યુનિકેશن", "લાક્ષણિકતાઓ", "ઘટકો", "ડેટા ટ્રાન્સમિશન",
                    "ટ્રાન્સમિશન તકનીકો", "ટ્રાન્સમિશન મોડ", "સિમ્પ્લેક્સ", "હાફ ડુપ્લેક્સ", "ફુલ ડુપ્લેક્સ",
                    
                    # સીરિયલ અને પેરેલલ કોમ્યુનિકેશન
                    "સીરિયલ કોમ્યુનિકેશન", "પેરેલલ કોમ્યુનિકેશન", "સિંક્રોનસ", "અસિંક્રોનસ",
                    "સીરિયલ ડેટા કોમ્યુનિકેશન", "પેરેલલ ડેટા કોમ્યુનિકેશન",
                    
                    # ડેટા રેપ્રેઝન્ટેશન અને સ્ટાન્ડર્ડ્સ
                    "ડેટા રેપ્રેઝન્ટેશન", "RS-232", "RS-422", "RS-485", "સ્ટાન્ડર્ડ્સ",
                    "કોમ્યુનિકેશન પોર્ટ્સ", "USB", "HDMI", "RCA", "ઇથરનેટ", "ઇન્ડસ્ટ્રિયલ સ્ટાન્ડર્ડ્સ",
                    
                    # મલ્ટિમીડિયા કોમ્યુનિકેશન
                    "મલ્ટિમીડિયા કોમ્યુનિકેશન", "મલ્ટિમીડિયા સિસ્ટમ્સ", "તત્વો", "મોડેલ",
                    "મલ્ટિમીડિયા પ્રોસેસિંગ", "ડિજિટલ મીડિયા", "સિગ્નલ પ્રોસેસિંગ",
                    "ઓડિયો ફોર્મેટ્સ", "વિડિયો ફોર્મેટ્સ", "ઇમેજ ફોર્મેટ્સ", "ફાઇલ ફોર્મેટ્સ",
                    
                    # કોમ્યુનિકેશન પ્રોટોકોલ્સ અને ઇન્ટરફેસિસ
                    "પ્રોટોકોલ્સ", "ઇન્ટરફેસિસ", "પિન ડાયાગ્રામ", "વોલ્ટેજ લેવલ્સ", "કનેક્ટર",
                    "કોમ્યુનિકેશન સ્ટાન્ડર્ડ્સ", "ડેટા ફોર્મેટ્સ"
                ]
            },
            
            "Unit-V": {
                "english": [
                    # Satellite communication
                    "satellite communication", "block diagram", "transponder", "uplink", "downlink",
                    "earth station", "satellite", "frequency bands", "C-band", "Ku-band", "Ka-band",
                    
                    # 5G technology
                    "5G technology", "5G", "data communication", "features", "advantages",
                    "high speed", "low latency", "massive connectivity", "network slicing",
                    "beamforming", "millimeter waves", "enhanced mobile broadband",
                    
                    # Spread spectrum
                    "spread spectrum", "communication", "techniques", "direct sequence",
                    "frequency hopping", "DSSS", "FHSS", "code division multiple access",
                    "CDMA", "spreading", "despreading",
                    
                    # Edge computing and blockchain
                    "edge computing", "features", "distributed computing", "low latency",
                    "real-time processing", "blockchain", "communication security",
                    "decentralization", "immutability", "transparency", "cryptographic",
                    
                    # Privacy and ethical considerations
                    "privacy considerations", "ethical considerations", "data communication",
                    "security", "data protection", "encryption", "privacy rights"
                ],
                "gujarati": [
                    # સેટેલાઇટ કોમ્યુનિકેશન
                    "સેટેલાઇટ કોમ્યુનિકેશન", "બ્લોક ડાયાગ્રામ", "ટ્રાન્સપોન્ડર", "અપલિંક", "ડાઉનલિંક",
                    "અર્થ સ્ટેશન", "સેટેલાઇટ", "ફ્રીક્વન્સી બેન્ડ્સ", "C-બેન્ડ", "Ku-બેન્ડ", "Ka-બેન્ડ",
                    
                    # 5G ટેકનોલોજી
                    "5G ટેકનોલોજી", "5G", "ડેટા કોમ્યુનિકેશન", "વિશેષતાઓ", "ફાયદાઓ",
                    "હાઇ સ્પીડ", "લો લેટન્સી", "મેસિવ કનેક્ટિવિટી", "નેટવર્ક સ્લાઇસિંગ",
                    "બીમફોર્મિંગ", "મિલિમીટર વેવ્સ", "એન્હાન્સ્ડ મોબાઇલ બ્રોડબેન્ડ",
                    
                    # સ્પ્રેડ સ્પેક્ટ્રમ
                    "સ્પ્રેડ સ્પેક્ટ્રમ", "કોમ્યુનિકેશન", "તકનીકો", "ડાયરેક્ટ સિક્વન્સ",
                    "ફ્રીક્વન્સી હોપિંગ", "DSSS", "FHSS", "કોડ ડિવિઝન મલ્ટિપલ એક્સેસ",
                    "CDMA", "સ્પ્રેડિંગ", "ડિસ્પ્રેડિંગ",
                    
                    # એજ કમ્પ્યુટિંગ અને બ્લોકચેઇન
                    "એજ કમ્પ્યુટિંગ", "વિશેષતાઓ", "ડિસ્ટ્રિબ્યુટેડ કમ્પ્યુટિંગ", "લો લેટન્સી",
                    "રિયલ-ટાઇમ પ્રોસેસિંગ", "બ્લોકચેઇન", "કોમ્યુનિકેશન સિક્યુરિટી",
                    "ડીસેન્ટ્રલાઇઝેશન", "ઇમ્યુટેબિલિટી", "પારદર્શિતા", "ક્રિપ્ટોગ્રાફિક",
                    
                    # ગોપનીયતા અને નૈતિક વિચારણાઓ
                    "ગોપનીયતાની વિચારણાઓ", "નૈતિક વિચારણાઓ", "ડેટા કોમ્યુનિકેશન",
                    "સિક્યુરિટી", "ડેટા પ્રોટેક્શન", "એન્ક્રિપ્શન", "ગોપનીયતાના અધિકારો"
                ]
            }
        }
        
        # Enhanced scoring weights for better accuracy
        self.scoring_weights = {
            'direct_match': 10.0,
            'partial_match': 5.0,
            'context_match': 3.0,
            'topic_match': 2.0,
            'length_bonus': 1.0,
            'technical_term_bonus': 2.0
        }
        
    def load_syllabus(self) -> Dict:
        """Load syllabus JSON file"""
        syllabus_file = self.base_path / "4343201.json"
        try:
            with open(syllabus_file, 'r', encoding='utf-8') as f:
                self.syllabus_data = json.load(f)
            print(f"✅ Loaded syllabus from {syllabus_file}")
            return self.syllabus_data
        except Exception as e:
            print(f"❌ Error loading syllabus: {e}")
            return {}
    
    def extract_questions_from_file(self, file_path: Path) -> List[Question]:
        """Extract questions from a solution file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            questions = []
            
            # Determine language from filename
            language = 'gujarati' if '.gu.' in file_path.name else 'english'
            
            # Extract year and season from filename
            year_match = re.search(r'(\d{4})', file_path.name)
            season_match = re.search(r'(summer|winter)', file_path.name.lower())
            
            year = year_match.group(1) if year_match else 'unknown'
            season = season_match.group(1) if season_match else 'unknown'
            
            # Enhanced question extraction patterns for both languages
            if language == 'english':
                patterns = [
                    r'##\s+Question\s+(\d+)\([a-z]+\)\s+\[(\d+)\s+marks?\][\s\n]*\*\*(.+?)\*\*',
                    r'##\s+પ્રશ્ન\s+(\d+)\([અ-ઝ]+\)\s+\[(\d+)\s+ગુણ\][\s\n]*\*\*(.+?)\*\*',
                    r'##\s+Q(?:uestion)?\s*(\d+)\.?([a-z]+)?\s*\[(\d+)\s*marks?\][\s\n]*(.+?)(?=##|$)',
                ]
            else:  # gujarati
                patterns = [
                    r'##\s+પ્રશ્ન\s+(\d+)\([અ-ઝ]+\)\s+\[(\d+)\s+ગુણ\][\s\n]*\*\*(.+?)\*\*',
                    r'##\s+Question\s+(\d+)\([a-z]+\)\s+\[(\d+)\s+marks?\][\s\n]*\*\*(.+?)\*\*',
                ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
                
                for match in matches:
                    try:
                        if len(match.groups()) == 3:
                            question_num, marks, text = match.groups()
                        elif len(match.groups()) == 4:
                            question_num, sub_part, marks, text = match.groups()
                            marks = sub_part if marks.isdigit() else marks
                        else:
                            continue
                        
                        # Clean question text
                        text = re.sub(r'\*\*', '', text)
                        text = re.sub(r'\n+', ' ', text)
                        text = text.strip()
                        
                        if len(text) < 10:  # Skip very short questions
                            continue
                        
                        # Create question ID
                        question_id = hashlib.md5(f"{file_path.name}_{question_num}_{text[:50]}".encode()).hexdigest()[:8]
                        
                        question = Question(
                            id=question_id,
                            text=text,
                            language=language,
                            marks=int(marks) if marks.isdigit() else 0,
                            source_file=file_path.name,
                            exam_year=year,
                            exam_season=season,
                            topics=[]
                        )
                        
                        questions.append(question)
                        
                    except Exception as e:
                        print(f"⚠️ Error parsing question match: {e}")
                        continue
            
            print(f"📄 Extracted {len(questions)} questions from {file_path.name}")
            return questions
            
        except Exception as e:
            print(f"❌ Error reading file {file_path}: {e}")
            return []
    
    def normalize_text(self, text: str) -> str:
        """Normalize text for better matching"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove special characters but keep essential ones
        text = re.sub(r'[^\w\s\-\.\(\)\/]', ' ', text)
        
        # Normalize unicode characters
        text = unicodedata.normalize('NFKD', text)
        
        return text
    
    def calculate_question_unit_score(self, question: Question, unit: str) -> float:
        """Calculate enhanced score for question-unit mapping"""
        normalized_text = self.normalize_text(question.text)
        score = 0.0
        
        # Get keywords for this unit in the question's language
        unit_keywords = self.unit_keywords.get(unit, {}).get(question.language, [])
        
        if not unit_keywords:
            return 0.0
        
        # Direct keyword matching with enhanced scoring
        for keyword in unit_keywords:
            normalized_keyword = self.normalize_text(keyword)
            
            # Exact match (highest score)
            if normalized_keyword in normalized_text:
                score += self.scoring_weights['direct_match']
                
                # Bonus for technical terms
                if len(keyword) > 3:
                    score += self.scoring_weights['technical_term_bonus']
            
            # Partial word matching
            words_in_text = set(normalized_text.split())
            keyword_words = set(normalized_keyword.split())
            
            common_words = words_in_text.intersection(keyword_words)
            if common_words:
                score += len(common_words) * self.scoring_weights['partial_match']
        
        # Length bonus for comprehensive questions
        if len(question.text) > 100:
            score += self.scoring_weights['length_bonus']
        
        # Context matching based on common DDC terms
        context_indicators = {
            "Unit-I": ["system", "block", "communication", "channel", "multiplexing", "TDM", "FDM"],
            "Unit-II": ["modulation", "ASK", "FSK", "PSK", "QPSK", "QAM", "waveform", "constellation"],
            "Unit-III": ["information", "entropy", "coding", "huffman", "shannon", "error", "line code"],
            "Unit-IV": ["data", "transmission", "serial", "parallel", "RS-232", "multimedia", "ports"],
            "Unit-V": ["satellite", "5G", "spread", "edge", "blockchain", "privacy", "security"]
        }
        
        unit_indicators = context_indicators.get(unit, [])
        for indicator in unit_indicators:
            if indicator.lower() in normalized_text:
                score += self.scoring_weights['context_match']
        
        return score
    
    def map_question_to_unit(self, question: Question) -> Tuple[str, float]:
        """Map question to most appropriate unit with confidence score"""
        unit_scores = {}
        
        for unit in self.unit_keywords.keys():
            score = self.calculate_question_unit_score(question, unit)
            unit_scores[unit] = score
        
        if not unit_scores or max(unit_scores.values()) == 0:
            return "Unknown", 0.0
        
        best_unit = max(unit_scores, key=unit_scores.get)
        best_score = unit_scores[best_unit]
        
        # Calculate confidence as normalized score
        total_possible_score = len(self.unit_keywords.get(best_unit, {}).get(question.language, [])) * self.scoring_weights['direct_match']
        confidence = min(best_score / max(total_possible_score, 1), 1.0) if total_possible_score > 0 else 0.0
        
        return best_unit, confidence
    
    def process_all_questions(self):
        """Process all solution files and extract questions"""
        solution_files = list(self.base_path.glob("*solution*.md"))
        
        print(f"🔍 Found {len(solution_files)} solution files:")
        for file in solution_files:
            print(f"  📝 {file.name}")
        
        all_questions = []
        for file_path in solution_files:
            questions = self.extract_questions_from_file(file_path)
            all_questions.extend(questions)
        
        print(f"📊 Total questions extracted: {len(all_questions)}")
        
        # Map questions to units
        mapped_questions = []
        mapping_stats = Counter()
        
        for question in all_questions:
            unit, confidence = self.map_question_to_unit(question)
            question.unit = unit
            question.confidence = confidence
            mapped_questions.append(question)
            mapping_stats[unit] += 1
        
        self.questions = mapped_questions
        
        print("\n📈 Unit mapping statistics:")
        for unit, count in mapping_stats.items():
            print(f"  {unit}: {count} questions")
        
        return mapped_questions
    
    def validate_mapping_accuracy(self) -> Dict:
        """Validate and report mapping accuracy"""
        stats = {
            'total_questions': len(self.questions),
            'mapped_questions': len([q for q in self.questions if q.unit != "Unknown"]),
            'high_confidence': len([q for q in self.questions if q.confidence > 0.7]),
            'medium_confidence': len([q for q in self.questions if 0.4 < q.confidence <= 0.7]),
            'low_confidence': len([q for q in self.questions if q.confidence <= 0.4]),
            'by_language': Counter([q.language for q in self.questions]),
            'by_unit': Counter([q.unit for q in self.questions]),
            'by_source': Counter([q.source_file for q in self.questions]),
            'unmapped_questions': [q for q in self.questions if q.unit == "Unknown"]
        }
        
        stats['mapping_accuracy'] = (stats['mapped_questions'] / stats['total_questions']) * 100 if stats['total_questions'] > 0 else 0
        stats['high_confidence_rate'] = (stats['high_confidence'] / stats['total_questions']) * 100 if stats['total_questions'] > 0 else 0
        
        return stats
    
    def generate_question_bank_json(self) -> Dict:
        """Generate final question bank JSON"""
        question_bank = {
            "metadata": {
                "course_code": "4343201",
                "course_title": "Digital and Data Communication",
                "semester": 4,
                "program": "Information and Communication Technology Engineering",
                "generated_at": "2024-12-19T10:00:00Z",
                "generator_version": "2.0",
                "total_questions": len(self.questions),
                "mapping_accuracy": f"{(len([q for q in self.questions if q.unit != 'Unknown']) / len(self.questions)) * 100:.2f}%" if self.questions else "0%"
            },
            "statistics": self.validate_mapping_accuracy(),
            "questions": []
        }
        
        # Group questions by unit
        for question in self.questions:
            question_data = asdict(question)
            question_bank["questions"].append(question_data)
        
        return question_bank
    
    def save_question_bank(self, output_file: str = "4343201-question-bank-final.json"):
        """Save question bank to JSON file"""
        question_bank = self.generate_question_bank_json()
        output_path = self.base_path / output_file
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(question_bank, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Question bank saved to {output_path}")
            return True
        except Exception as e:
            print(f"❌ Error saving question bank: {e}")
            return False
    
    def run(self):
        """Run the complete question bank generation process"""
        print("🚀 Starting Enhanced DDC Question Bank Generation...")
        print("=" * 60)
        
        # Step 1: Load syllabus
        print("\n📚 Step 1: Loading syllabus...")
        self.load_syllabus()
        
        # Step 2: Process all questions
        print("\n🔄 Step 2: Processing solution files...")
        self.process_all_questions()
        
        # Step 3: Validate mapping
        print("\n✅ Step 3: Validating mapping accuracy...")
        stats = self.validate_mapping_accuracy()
        
        print(f"\n📊 Final Statistics:")
        print(f"  📝 Total questions: {stats['total_questions']}")
        print(f"  ✅ Successfully mapped: {stats['mapped_questions']} ({stats['mapping_accuracy']:.2f}%)")
        print(f"  🎯 High confidence: {stats['high_confidence']} ({stats['high_confidence_rate']:.2f}%)")
        print(f"  📊 By language: {dict(stats['by_language'])}")
        print(f"  📚 By unit: {dict(stats['by_unit'])}")
        
        if stats['unmapped_questions']:
            print(f"\n⚠️  Unmapped questions ({len(stats['unmapped_questions'])}):")
            for q in stats['unmapped_questions']:
                print(f"    🔸 {q.text[:60]}..." if len(q.text) > 60 else f"    🔸 {q.text}")
        
        # Step 4: Save question bank
        print("\n💾 Step 4: Saving question bank...")
        success = self.save_question_bank()
        
        if success:
            print(f"\n🎉 Question bank generation completed successfully!")
            print(f"📈 Achieved {stats['mapping_accuracy']:.2f}% mapping accuracy")
            print(f"🎯 {stats['high_confidence_rate']:.2f}% high-confidence mappings")
        else:
            print("\n❌ Question bank generation failed!")
        
        print("=" * 60)


def main():
    """Main execution function"""
    base_path = "/Users/milav/Code/studio/content/resources/study-materials/32-ict/sem-4/4343201-ddc"
    
    generator = EnhancedDDCQuestionBankGenerator(base_path)
    generator.run()


if __name__ == "__main__":
    main()