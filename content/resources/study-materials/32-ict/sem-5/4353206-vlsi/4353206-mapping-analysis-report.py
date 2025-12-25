#!/usr/bin/env python3
"""
Mapping Analysis Report for VLSI Technology (4353206)
Analyzes current question bank and provides recommendations for improved mapping
"""

import json
import re
from collections import defaultdict, Counter

def analyze_question_bank():
    """Analyze the generated question bank for mapping accuracy"""
    
    # Load the question bank
    with open('4353206-question-bank-final.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    
    print("=== VLSI Technology (4353206) Question Bank Analysis ===\n")
    print(f"Total Questions: {len(questions)}")
    
    # Analyze by language
    english_qs = [q for q in questions if q['language'] == 'english']
    gujarati_qs = [q for q in questions if q['language'] == 'gujarati']
    
    print(f"English Questions: {len(english_qs)}")
    print(f"Gujarati Questions: {len(gujarati_qs)}")
    
    # Analyze confidence scores
    confidence_analysis = {
        'high': [q for q in questions if q['confidence_score'] >= 0.7],
        'medium': [q for q in questions if 0.3 <= q['confidence_score'] < 0.7],
        'low': [q for q in questions if q['confidence_score'] < 0.3]
    }
    
    print(f"\n=== Confidence Score Analysis ===")
    print(f"High Confidence (>=0.7): {len(confidence_analysis['high'])}")
    print(f"Medium Confidence (0.3-0.7): {len(confidence_analysis['medium'])}")
    print(f"Low Confidence (<0.3): {len(confidence_analysis['low'])}")
    
    # Analyze unit distribution
    unit_dist = defaultdict(list)
    for q in questions:
        unit_dist[q['unit']].append(q)
    
    print(f"\n=== Unit Distribution ===")
    for unit in sorted(unit_dist.keys()):
        unit_questions = unit_dist[unit]
        english_count = len([q for q in unit_questions if q['language'] == 'english'])
        gujarati_count = len([q for q in unit_questions if q['language'] == 'gujarati'])
        print(f"Unit {unit}: {len(unit_questions)} total ({english_count} EN, {gujarati_count} GU)")
    
    # Analyze keywords
    print(f"\n=== Most Common Keywords ===")
    all_keywords = []
    for q in questions:
        all_keywords.extend(q['keywords'])
    
    keyword_counts = Counter(all_keywords)
    for keyword, count in keyword_counts.most_common(20):
        print(f"{keyword}: {count}")
    
    # Sample questions by unit for manual verification
    print(f"\n=== Sample Questions by Unit ===")
    for unit in ['1', '2', '3', '4', '5']:
        unit_questions = unit_dist.get(unit, [])
        if unit_questions:
            print(f"\nUnit {unit} samples:")
            for i, q in enumerate(unit_questions[:3]):  # Show first 3
                print(f"  {i+1}. [{q['marks']}m] {q['text'][:80]}...")
                print(f"     Keywords: {', '.join(q['keywords'][:5])}")
                print(f"     Confidence: {q['confidence_score']:.2f}")
    
    # Identify problematic mappings
    print(f"\n=== Mapping Issues Analysis ===")
    
    # Questions mapped to all units (likely wrong)
    all_unit_mapped = [q for q in questions if len(q['mapped_units']) == 5]
    print(f"Questions mapped to all 5 units: {len(all_unit_mapped)}")
    
    # High confidence but multiple units
    multi_unit_high_conf = [q for q in questions if len(q['mapped_units']) > 2 and q['confidence_score'] > 0.5]
    print(f"High confidence but mapped to >2 units: {len(multi_unit_high_conf)}")
    
    # Low confidence questions
    low_conf_questions = [q for q in questions if q['confidence_score'] < 0.3]
    print(f"Low confidence questions needing review: {len(low_conf_questions)}")
    
    # Analyze by question type
    print(f"\n=== Question Type Distribution ===")
    type_dist = defaultdict(int)
    for q in questions:
        type_dist[q['question_type']] += 1
    
    for qtype, count in sorted(type_dist.items()):
        print(f"{qtype}: {count}")
    
    return data

def manual_unit_mapping():
    """Provide manual mapping suggestions based on question content analysis"""
    
    # Define more specific unit patterns based on syllabus
    unit_patterns = {
        "1": {
            "keywords": ["vlsi", "design methodology", "design flow", "hierarchy", "regularity", 
                        "modularity", "fpga", "asic", "gate array", "standard cell", "y-chart", 
                        "full custom", "semi custom", "top-down", "bottom-up"],
            "concepts": ["design styles", "vlsi design", "chip design", "design constraints"]
        },
        "2": {
            "keywords": ["mosfet", "mos transistor", "energy band", "structure", "external bias",
                        "channel formation", "current voltage", "scaling", "threshold voltage",
                        "depletion", "inversion", "accumulation", "gradual channel"],
            "concepts": ["transistor", "bias", "scaling", "characteristics"]
        },
        "3": {
            "keywords": ["inverter", "vtc", "voltage transfer", "noise margin", "resistive load",
                        "enhancement load", "depletion load", "cmos inverter", "switching",
                        "static power", "dynamic power"],
            "concepts": ["inverter", "vtc", "noise margin", "load"]
        },
        "4": {
            "keywords": ["cmos logic", "nand", "nor", "aoi", "oai", "transmission gate",
                        "sr latch", "d latch", "flip flop", "sequential", "combinational",
                        "logic gates", "boolean"],
            "concepts": ["logic gates", "latch", "flip flop", "cmos circuits"]
        },
        "5": {
            "keywords": ["verilog", "hdl", "behavioral", "data flow", "gate level", "module",
                        "always", "assign", "case", "testbench", "simulation", "synthesis",
                        "counter", "decoder", "encoder", "multiplexer", "adder"],
            "concepts": ["verilog", "hdl", "programming", "modeling", "simulation"]
        }
    }
    
    print("\n=== Manual Unit Mapping Guidelines ===")
    for unit, data in unit_patterns.items():
        print(f"\nUnit {unit}:")
        print(f"  Key concepts: {', '.join(data['concepts'])}")
        print(f"  Keywords: {', '.join(data['keywords'][:10])}")

if __name__ == "__main__":
    data = analyze_question_bank()
    manual_unit_mapping()
    
    print(f"\n=== Recommendations ===")
    print("1. Improve keyword mappings with more specific terms")
    print("2. Adjust confidence thresholds")
    print("3. Add manual review for ambiguous questions")
    print("4. Implement better unit-specific scoring")
    print("5. Consider question context beyond just keywords")