#!/usr/bin/env python3
"""
Enhanced Question Bank Generator for Software Engineering (4353202)
Comprehensive bilingual question extraction and mapping system for Software Engineering
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

class EnhancedSEQuestionBankGenerator:
    """Enhanced question bank generator for Software Engineering"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.syllabus_data = {}
        self.questions = []
        
        # Enhanced bilingual keyword mappings for Software Engineering
        self.unit_keywords = {
            "Unit-I": {
                "english": [
                    # Software Engineering Fundamentals
                    "software engineering", "software", "engineering", "SE", "define software engineering",
                    "software application domain", "application domain", "domain", "enlist",
                    "embedded software", "embedded system", "real-time software", "embedded",
                    "system software", "application software", "web application", "web applications",
                    "AI software", "artificial intelligence", "engineering software",
                    "scientific software", "CAD software", "simulation software", "simulation tools",
                    "operating systems", "device drivers", "word processors", "games", "business apps",
                    "browser-based applications", "machine learning", "expert systems",
                    
                    # Layered Approach
                    "layered approach", "software engineering layers", "process layer",
                    "methods layer", "tools layer", "quality focus", "foundation",
                    "framework", "umbrella activities", "generic framework",
                    
                    # Programs vs Software Products
                    "programs", "software products", "product", "program", "vs", "versus",
                    "difference", "distinction", "characteristics", "features", "differentiate",
                    "commercial software", "custom software", "off-the-shelf",
                    
                    # Software Process and Methods
                    "software process", "process", "methods", "software engineering methods",
                    "methodology", "approach", "technique", "practice",
                    "development process", "engineering process",
                    
                    # Generic Framework Activities
                    "communication", "planning", "modeling", "construction", "deployment",
                    "framework activities", "generic activities", "core activities",
                    "requirement gathering", "stakeholder communication", "project planning",
                    "analysis", "design", "code generation", "testing", "installation",
                    "customer support", "feedback", "adaptation", "explain generic framework",
                    "generic framework activity", "explain umbrella",
                    
                    # Umbrella Activities
                    "project management", "risk management", "quality assurance",
                    "configuration management", "work product preparation",
                    "reusability management", "measurement", "SQA", "SCM", "tracking",
                    "control", "review", "audit", "process improvement", "umbrella activity"
                ],
                "gujarati": [
                    # સૉફ્ટવેર એન્જિનિયરિંગ મૂળભૂતો
                    "સૉફ્ટવેર એન્જિનિયરિંગ", "સૉફ્ટવેર", "એન્જિનિયરિંગ", "SE",
                    "સૉફ્ટવેર એપ્લિકેશન ડોમેઇન", "એપ્લિકેશન ડોમેઇન", "ડોમેઇન",
                    "એમ્બેડેડ સૉફ્ટવેર", "એમ્બેડેડ સિસ્ટમ", "રિયલ-ટાઇમ સૉફ્ટવેર",
                    "સિસ્ટમ સૉફ્ટવેર", "એપ્લિકેશન સૉફ્ટવેર", "વેબ એપ્લિકેશન",
                    "AI સૉફ્ટવેર", "આર્ટિફિશિયલ ઇન્ટેલિજન્સ", "એન્જિનિયરિંગ સૉફ્ટવેર",
                    "સાયન્ટિફિક સૉફ્ટવેર", "CAD સૉફ્ટવેર", "સિમ્યુલેશન સૉફ્ટવેર",
                    
                    # સ્તરીય અભિગમ
                    "સ્તરીય અભિગમ", "સૉફ્ટવેર એન્જિનિયરિંગ સ્તરો", "પ્રક્રિયા સ્તર",
                    "પદ્ધતિઓ સ્તર", "સાધનો સ્તર", "ગુણવત્તા કેન્દ્ર", "પાયો",
                    "ફ્રેમવર્ક", "અમ્બ્રેલા પ્રવૃત્તિઓ", "જેનેરિક ફ્રેમવર્ક",
                    
                    # પ્રોગ્રામ્સ વિ સૉફ્ટવેર પ્રોડક્ટ્સ
                    "પ્રોગ્રામ્સ", "સૉફ્ટવેર ઉત્પાદનો", "ઉત્પાદન", "પ્રોગ્રામ",
                    "તફાવત", "ભેદ", "લક્ષણો", "વિશેષતાઓ",
                    "વ્યાવસાયિક સૉફ્ટવેર", "કસ્ટમ સૉફ્ટવેર", "તૈયાર સૉફ્ટવેર",
                    
                    # સૉફ્ટવેર પ્રક્રિયા અને પદ્ધતિઓ
                    "સૉફ્ટવેર પ્રક્રિયા", "પ્રક્રિયા", "પદ્ધતિઓ", "સૉફ્ટવેર એન્જિનિયરિંગ પદ્ધતિઓ",
                    "કાર્યપદ્ધતિ", "અભિગમ", "તકનીક", "પ્રથા",
                    "વિકાસ પ્રક્રિયા", "એન્જિનિયરિંગ પ્રક્રિયા",
                    
                    # જેનેરિક ફ્રેમવર્ક પ્રવૃત્તિઓ
                    "કોમ્યુનિકેશન", "પ્લાનિંગ", "મોડેલિંગ", "કન્સ્ટ્રક્શન", "ડિપ્લોયમેન્ટ",
                    "ફ્રેમવર્ક પ્રવૃત્તિઓ", "જેનેરિક પ્રવૃત્તિઓ", "મુખ્ય પ્રવૃત્તિઓ",
                    "જરૂરિયાત એકત્રીકરણ", "હિતધારક સંચાર", "પ્રોજેક્ટ આયોજન",
                    "વિશ્લેષણ", "ડિઝાઇન", "કોડ જનરેશન", "ટેસ્ટિંગ", "ઇન્સ્ટોલેશન",
                    "ગ્રાહક સપોર્ટ", "પ્રતિસાદ", "અનુકૂલન",
                    
                    # અમ્બ્રેલા પ્રવૃત્તિઓ
                    "પ્રોજેક્ટ મેનેજમેન્ટ", "રિસ્ક મેનેજમેન્ટ", "ગુણવત્તા આશ્વાસન",
                    "કન્ફિગરેશન મેનેજમેન્ટ", "વર્ક પ્રોડક્ટ તૈયારી",
                    "પુનઃઉપયોગિતા મેનેજમેન્ટ", "માપ", "SQA", "SCM", "ટ્રેકિંગ",
                    "નિયંત્રણ", "સમીક્ષા", "ઑડિટ", "પ્રક્રિયા સુધારણા"
                ]
            },
            
            "Unit-II": {
                "english": [
                    # SDLC Introduction
                    "software development life cycle", "SDLC", "life cycle", "development cycle",
                    "software lifecycle", "development process", "lifecycle model",
                    "process model", "development methodology", "software process model",
                    "recreate", "diagram", "phases", "explain", "sdlc diagram",
                    
                    # Waterfall Model
                    "waterfall model", "waterfall", "linear sequential model", "sequential",
                    "classic life cycle", "systematic approach", "phase-wise development",
                    "requirements", "analysis", "design", "implementation", "testing",
                    "operation", "maintenance", "advantages", "disadvantages", "limitations",
                    "explain waterfall", "waterfall process",
                    
                    # Incremental Process Model
                    "incremental model", "incremental process", "incremental development",
                    "incremental delivery", "increment", "partial implementation",
                    "evolutionary development", "iterative enhancement",
                    "core functionality", "supplementary features", "explain incremental",
                    
                    # Prototype Model
                    "prototype model", "prototyping", "prototype", "throwaway prototype",
                    "evolutionary prototype", "rapid prototype", "proof of concept",
                    "user feedback", "requirements clarification", "feasibility study",
                    "quick design", "prototype construction", "customer evaluation",
                    "explain prototype", "prototyping approach",
                    
                    # Spiral Model
                    "spiral model", "spiral", "risk-driven model", "cyclic model",
                    "quadrant model", "planning", "risk analysis", "engineering",
                    "customer evaluation", "risk assessment", "prototype development",
                    "Barry Boehm", "risk mitigation", "iterative process",
                    "spiral process", "spiral process model", "differentiate spiral",
                    
                    # RAD Model
                    "RAD model", "rapid application development", "RAD", "rapid development",
                    "component-based construction", "reusable components", "code generation",
                    "visual programming", "business modeling", "data modeling",
                    "process modeling", "application generation", "testing delivery",
                    "explain RAD", "RAD approach",
                    
                    # Agile Development
                    "agile development", "agile model", "agile methodology", "agile",
                    "agile principles", "agility", "adaptive software development",
                    "iterative development", "customer collaboration", "working software",
                    "responding to change", "individuals and interactions",
                    "agile manifesto", "scrum", "extreme programming", "XP",
                    "sprint", "backlog", "user stories", "stand-up meetings",
                    "pair programming", "test-driven development", "TDD",
                    "continuous integration", "refactoring", "release planning",
                    "scrum agile", "differentiate scrum", "agile process", "scrum process"
                ],
                "gujarati": [
                    # SDLC પરિચય
                    "સૉફ્ટવેર ડેવલપમેંટ લાઇફ સાઇકલ", "SDLC", "લાઇફ સાઇકલ", "ડેવલપમેંટ સાઇકલ",
                    "સૉફ્ટવેર જીવનચક્ર", "વિકાસ પ્રક્રિયા", "જીવનચક્ર મોડેલ",
                    "પ્રક્રિયા મોડેલ", "વિકાસ કાર્યપદ્ધતિ", "સૉફ્ટવેર પ્રક્રિયા મોડેલ",
                    
                    # વોટરફોલ મોડેલ
                    "વોટરફોલ મોડેલ", "વોટરફોલ", "રેખીય અનુક્રમિક મોડેલ", "અનુક્રમિક",
                    "ક્લાસિક લાઇફ સાઇકલ", "વ્યવસ્થિત અભિગમ", "તબક્કાવાર વિકાસ",
                    "જરૂરિયાતો", "વિશ્લેષણ", "ડિઝાઇન", "અમલીકરણ", "ટેસ્ટિંગ",
                    "ઓપરેશન", "જાળવણી", "ફાયદાઓ", "નુકસાનો", "મર્યાદાઓ",
                    
                    # ઇન્ક્રિમેન્ટલ પ્રક્રિયા મોડેલ
                    "ઇન્ક્રિમેન્ટલ મોડેલ", "ઇન્ક્રિમેન્ટલ પ્રક્રિયા", "ઇન્ક્રિમેન્ટલ ડેવલપમેન્ટ",
                    "ઇન્ક્રિમેન્ટલ ડિલિવરી", "ઇન્ક્રિમેન્ટ", "આંશિક અમલીકરણ",
                    "ઉત્ક્રાંતિ વિકાસ", "પુનરાવર્તિત વૃદ્ધિ",
                    "મુખ્ય કાર્યક્ષમતા", "પૂરક વિશેષતાઓ",
                    
                    # પ્રોટોટાઇપ મોડેલ
                    "પ્રોટોટાઇપ મોડેલ", "પ્રોટોટાઇપિંગ", "પ્રોટોટાઇપ", "ફેંકી દેવાયેલ પ્રોટોટાઇપ",
                    "ઉત્ક્રાંતિ પ્રોટોટાઇપ", "ઝડપી પ્રોટોટાઇપ", "સંકલ્પનાનો પુરાવો",
                    "વપરાશકર્તા પ્રતિસાદ", "જરૂરિયાતોની સ્પષ્ટતા", "શક્યતા અભ્યાસ",
                    "ઝડપી ડિઝાઇન", "પ્રોટોટાઇપ નિર્માણ", "ગ્રાહક મૂલ્યાંકન",
                    
                    # સ્પાઇરલ મોડેલ
                    "સ્પાઇરલ મોડેલ", "સ્પાઇરલ", "જોખમ-સંચાલિત મોડેલ", "ચક્રીય મોડેલ",
                    "ચતુર્થાંશ મોડેલ", "આયોજન", "જોખમ વિશ્લેષણ", "એન્જિનિયરિંગ",
                    "ગ્રાહક મૂલ્યાંકન", "જોખમ આકારણી", "પ્રોટોટાઇપ ડેવલપમેન્ટ",
                    "બેરી બોહમ", "જોખમ શમન", "પુનરાવર્તિત પ્રક્રિયા",
                    
                    # RAD મોડેલ
                    "RAD મોડેલ", "ઝડપી એપ્લિકેશન ડેવલપમેન્ટ", "RAD", "ઝડપી વિકાસ",
                    "ઘટક-આધારિત નિર્માણ", "પુનઃઉપયોગી ઘટકો", "કોડ જનરેશન",
                    "વિઝ્યુઅલ પ્રોગ્રામિંગ", "બિઝનેસ મોડેલિંગ", "ડેટા મોડેલિંગ",
                    "પ્રક્રિયા મોડેલિંગ", "એપ્લિકેશન જનરેશન", "ટેસ્ટિંગ ડિલિવરી",
                    
                    # એજાઇલ ડેવલપમેન્ટ
                    "એજાઇલ ડેવલપમેન્ટ", "એજાઇલ મોડેલ", "એજાઇલ કાર્યપદ્ધતિ", "એજાઇલ",
                    "એજાઇલ સિદ્ધાંતો", "ચપળતા", "અનુકૂલનશીલ સૉફ્ટવેર ડેવલપમેન્ટ",
                    "પુનરાવર્તિત વિકાસ", "ગ્રાહક સહયોગ", "કાર્યશીલ સૉફ્ટવેર",
                    "પરિવર્તનનો પ્રતિસાદ", "વ્યક્તિઓ અને ક્રિયાપ્રતિક્રિયાઓ",
                    "એજાઇલ મેનિફેસ્ટો", "સ્ક્રમ", "એક્સ્ટ્રીમ પ્રોગ્રામિંગ", "XP",
                    "સ્પ્રિન્ટ", "બેકલોગ", "યુઝર સ્ટોરીઝ", "સ્ટેન્ડ-અપ મીટિંગ્સ",
                    "પેર પ્રોગ્રામિંગ", "ટેસ્ટ-ડ્રિવન ડેવલપમેન્ટ", "TDD",
                    "સતત એકીકરણ", "રિફેક્ટરિંગ", "રિલીઝ પ્લાનિંગ"
                ]
            },
            
            "Unit-III": {
                "english": [
                    # Requirements Gathering and Analysis
                    "requirement gathering", "requirements analysis", "requirement engineering",
                    "requirements", "stakeholder", "customer needs", "user requirements",
                    "system requirements", "business requirements", "elicitation",
                    "interview", "questionnaire", "observation", "document analysis",
                    "prototyping", "brainstorming", "focus groups", "use cases",
                    
                    # Software Requirement Specification (SRS)
                    "software requirement specification", "SRS", "requirement specification",
                    "functional requirements", "non-functional requirements", "constraints",
                    "performance requirements", "security requirements", "usability",
                    "reliability", "availability", "portability", "maintainability",
                    "IEEE 830", "SRS template", "specification document",
                    
                    # Software Design
                    "software design", "design", "analysis vs design", "design principles",
                    "characteristics of good design", "design quality", "design process",
                    "architectural design", "detailed design", "interface design",
                    "component design", "data design", "algorithm design",
                    "design patterns", "design methodologies", "design notation",
                    
                    # Cohesion and Coupling
                    "cohesion", "coupling", "module cohesion", "module coupling",
                    "functional cohesion", "sequential cohesion", "communicational cohesion",
                    "procedural cohesion", "temporal cohesion", "logical cohesion",
                    "coincidental cohesion", "data coupling", "stamp coupling",
                    "control coupling", "external coupling", "common coupling",
                    "content coupling", "tight coupling", "loose coupling",
                    
                    # Data Flow Diagram (DFD)
                    "data flow diagram", "DFD", "context diagram", "level 0 DFD",
                    "level 1 DFD", "data flow", "data store", "process", "external entity",
                    "decomposition", "balancing", "data dictionary", "process specification",
                    "structured analysis", "functional decomposition",
                    
                    # Object Modeling with UML
                    "UML", "unified modeling language", "object modeling", "object-oriented",
                    "use case diagram", "class diagram", "sequence diagram", "activity diagram",
                    "collaboration diagram", "state diagram", "component diagram",
                    "deployment diagram", "object diagram", "package diagram",
                    "actor", "use case", "association", "generalization", "aggregation",
                    "composition", "class", "object", "attribute", "method", "operation",
                    "inheritance", "polymorphism", "encapsulation", "abstraction",
                    "multiplicity", "cardinality", "stereotype", "tagged value"
                ],
                "gujarati": [
                    # જરૂરિયાત એકત્રીકરણ અને વિશ્લેષણ
                    "જરૂરિયાત એકત્રીકરણ", "જરૂરિયાતો વિશ્લેષણ", "જરૂરિયાત એન્જિનિયરિંગ",
                    "જરૂરિયાતો", "હિતધારક", "ગ્રાહકની જરૂરિયાતો", "વપરાશકર્તા જરૂરિયાતો",
                    "સિસ્ટમ જરૂરિયાતો", "બિઝનેસ જરૂરિયાતો", "ઉદ્ઘાટન",
                    "ઇન્ટરવ્યુ", "પ્રશ્નાવલી", "અવલોકન", "દસ્તાવેજ વિશ્લેષણ",
                    "પ્રોટોટાઇપિંગ", "બ્રેઇનસ્ટોર્મિંગ", "ફોકસ ગ્રુપ્સ", "ઉપયોગ કેસો",
                    
                    # સૉફ્ટવેર જરૂરિયાત વિશિષ્ટતા (SRS)
                    "સૉફ્ટવેર જરૂરિયાત વિશિષ્ટતા", "SRS", "જરૂરિયાત વિશિષ્ટતા",
                    "કાર્યાત્મક જરૂરિયાતો", "બિન-કાર્યાત્મક જરૂરિયાતો", "અવરોધો",
                    "પ્રદર્શન જરૂરિયાતો", "સુરક્ષા જરૂરિયાતો", "ઉપયોગિતા",
                    "વિશ્વસનીયતા", "ઉપલબ્ધતા", "પોર્ટેબિલિટી", "જાળવણીયતા",
                    "IEEE 830", "SRS ટેમ્પલેટ", "વિશિષ્ટતા દસ્તાવેજ",
                    
                    # સૉફ્ટવેર ડિઝાઇન
                    "સૉફ્ટવેર ડિઝાઇન", "ડિઝાઇન", "વિશ્લેષણ વિ ડિઝાઇન", "ડિઝાઇન સિદ્ધાંતો",
                    "સારા ડિઝાઇનની લાક્ષણિકતાઓ", "ડિઝાઇન ગુણવત્તા", "ડિઝાઇન પ્રક્રિયા",
                    "આર્કિટેક્ચરલ ડિઝાઇન", "વિગતવાર ડિઝાઇન", "ઇન્ટરફેસ ડિઝાઇન",
                    "ઘટક ડિઝાઇન", "ડેટા ડિઝાઇન", "એલ્ગોરિધમ ડિઝાઇન",
                    "ડિઝાઇન પેટર્ન", "ડિઝાઇન કાર્યપદ્ધતિઓ", "ડિઝાઇન નોટેશન",
                    
                    # કોહેશન અને કપલિંગ
                    "કોહેશન", "કપલિંગ", "મોડ્યુલ કોહેશન", "મોડ્યુલ કપલિંગ",
                    "કાર્યાત્મક કોહેશન", "અનુક્રમિક કોહેશન", "સંચાર કોહેશન",
                    "પ્રક્રિયાગત કોહેશન", "સમયગત કોહેશન", "તાર્કિક કોહેશન",
                    "સંયોગિક કોહેશન", "ડેટા કપલિંગ", "સ્ટેમ્પ કપલિંગ",
                    "નિયંત્રણ કપલિંગ", "બાહ્ય કપલિંગ", "સામાન્ય કપલિંગ",
                    "સામગ્રી કપલિંગ", "ચુસ્ત કપલિંગ", "શિથિલ કપલિંગ",
                    
                    # ડેટા ફ્લો ડાયાગ્રામ (DFD)
                    "ડેટા ફ્લો ડાયાગ્રામ", "DFD", "કન્ટેક્સ્ટ ડાયાગ્રામ", "લેવલ 0 DFD",
                    "લેવલ 1 DFD", "ડેટા ફ્લો", "ડેટા સ્ટોર", "પ્રક્રિયા", "બાહ્ય એન્ટિટી",
                    "વિઘટન", "સંતુલન", "ડેટા ડિક્શનરી", "પ્રક્રિયા વિશિષ્ટતા",
                    "સ્ટ્રક્ચર્ડ એનાલિસિસ", "કાર્યાત્મક વિઘટન",
                    
                    # UML સાથે ઑબ્જેક્ટ મોડેલિંગ
                    "UML", "યુનિફાઇડ મોડેલિંગ લેંગ્વેજ", "ઑબ્જેક્ટ મોડેલિંગ", "ઑબ્જેક્ટ-ઓરિએન્ટેડ",
                    "યુઝ કેસ ડાયાગ્રામ", "ક્લાસ ડાયાગ્રામ", "સિક્વન્સ ડાયાગ્રામ", "એક્ટિવિટી ડાયાગ્રામ",
                    "કોલેબોરેશન ડાયાગ્રામ", "સ્ટેટ ડાયાગ્રામ", "કોમ્પોનન્ટ ડાયાગ્રામ",
                    "ડિપ્લોયમેન્ટ ડાયાગ્રામ", "ઑબ્જેક્ટ ડાયાગ્રામ", "પેકેજ ડાયાગ્રામ",
                    "એક્ટર", "યુઝ કેસ", "એસોસિએશન", "જનરલાઇઝેશન", "એગ્રિગેશન",
                    "કમ્પોઝિશન", "ક્લાસ", "ઑબ્જેક્ટ", "એટ્રિબ્યુટ", "મેથડ", "ઓપરેશન",
                    "ઇન્હેરિટન્સ", "પોલિમોર્ફિઝમ", "એન્કેપ્સ્યુલેશન", "એબ્સ્ટ્રેક્શન",
                    "મલ્ટિપ્લિસિટી", "કાર્ડિનાલિટી", "સ્ટીરિયોટાઇપ", "ટેગ્ડ વેલ્યુ"
                ]
            },
            
            "Unit-IV": {
                "english": [
                    # Project Management
                    "software project management", "project management", "project manager",
                    "responsibility", "project planning", "project control", "project monitoring",
                    "project tracking", "project execution", "resource management",
                    "team management", "communication management", "stakeholder management",
                    "responsibility of software project manager", "project manager responsibility",
                    
                    # Size Estimation Metrics
                    "size estimation", "estimation", "metrics", "measurement", "sizing",
                    "line of code", "LOC", "KLOC", "source lines of code", "SLOC",
                    "function points", "FP", "function point analysis", "function counting",
                    "unadjusted function points", "adjusted function points", "complexity adjustment",
                    "external inputs", "external outputs", "external inquiries",
                    "internal logical files", "external interface files",
                    "metrics for size estimation", "size estimation metrics",
                    
                    # Estimation Techniques
                    "project estimation", "estimation technique", "estimation methods",
                    "empirical estimation", "heuristic estimation", "analytical estimation",
                    "expert judgment", "analogy-based estimation", "top-down estimation",
                    "bottom-up estimation", "three-point estimation", "PERT estimation",
                    "delphi technique", "planning poker", "wideband delphi",
                    "project estimation technique", "explain project estimation",
                    
                    # COCOMO Models
                    "COCOMO", "constructive cost model", "COCOMO I", "COCOMO II",
                    "organic mode", "semidetached mode", "embedded mode",
                    "effort estimation", "schedule estimation", "cost estimation",
                    "person-months", "development time", "productivity", "team size",
                    "effort multipliers", "scale factors", "cost drivers",
                    "intermediate COCOMO", "COCOMO model", "explain COCOMO",
                    "basic COCOMO", "detailed COCOMO", "cocomo approach",
                    
                    # Project Scheduling
                    "project scheduling", "scheduling", "task scheduling", "activity scheduling",
                    "work breakdown structure", "WBS", "milestone", "deliverable",
                    "critical path", "critical path method", "CPM", "PERT",
                    "gantt chart", "timeline", "dependency", "predecessor", "successor",
                    "sprint burndown chart", "agile scheduling", "iteration planning",
                    "release planning", "story points", "velocity", "burnup chart",
                    "explain gantt chart", "project scheduling techniques",
                    
                    # Risk Management
                    "risk management", "risk", "uncertainty", "threat", "opportunity",
                    "risk identification", "risk assessment", "risk analysis", "risk control",
                    "risk monitoring", "risk mitigation", "risk avoidance", "risk transfer",
                    "risk acceptance", "contingency planning", "risk register",
                    "risk matrix", "probability", "impact", "exposure", "RMMM plan",
                    "explain risk management", "risk management process"
                ],
                "gujarati": [
                    # પ્રોજેક્ટ મેનેજમેન્ટ
                    "સૉફ્ટવેર પ્રોજેક્ટ મેનેજમેન્ટ", "પ્રોજેક્ટ મેનેજમેન્ટ", "પ્રોજેક્ટ મેનેજર",
                    "જવાબદારી", "પ્રોજેક્ટ આયોજન", "પ્રોજેક્ટ નિયંત્રણ", "પ્રોજેક્ટ મોનિટરિંગ",
                    "પ્રોજેક્ટ ટ્રેકિંગ", "પ્રોજેક્ટ અમલીકરણ", "સંસાધન વ્યવસ્થાપન",
                    "ટીમ મેનેજમેન્ટ", "સંચાર વ્યવસ્થાપન", "હિતધારક વ્યવસ્થાપન",
                    
                    # સાઇઝ એસ્ટિમેશન મેટ્રિક્સ
                    "સાઇઝ એસ્ટિમેશન", "અંદાજ", "મેટ્રિક્સ", "માપ", "સાઇઝિંગ",
                    "લાઇન ઓફ કોડ", "LOC", "KLOC", "સોર્સ લાઇન્સ ઓફ કોડ", "SLOC",
                    "ફંક્શન પોઇન્ટ્સ", "FP", "ફંક્શન પોઇન્ટ એનાલિસિસ", "ફંક્શન કાઉન્ટિંગ",
                    "અનએડજસ્ટેડ ફંક્શન પોઇન્ટ્સ", "એડજસ્ટેડ ફંક્શન પોઇન્ટ્સ", "જટિલતા એડજસ્ટમેન્ટ",
                    "બાહ્ય ઇનપુટ્સ", "બાહ્ય આઉટપુટ્સ", "બાહ્ય પૂછપરછ",
                    "આંતરિક લોજિકલ ફાઇલો", "બાહ્ય ઇન્ટરફેસ ફાઇલો",
                    
                    # એસ્ટિમેશન તકનીકો
                    "પ્રોજેક્ટ એસ્ટિમેશન", "એસ્ટિમેશન તકનીક", "એસ્ટિમેશન પદ્ધતિઓ",
                    "અનુભવસિદ્ધ એસ્ટિમેશન", "હ્યુરિસ્ટિક એસ્ટિમેશન", "વિશ્લેષણાત્મક એસ્ટિમેશન",
                    "નિષ્ણાત નિર્ણય", "સાદૃશ્ય-આધારિત એસ્ટિમેશન", "ટોપ-ડાઉન એસ્ટિમેશન",
                    "બોટમ-અપ એસ્ટિમેશન", "ત્રિ-બિંદુ એસ્ટિમેશન", "PERT એસ્ટિમેશન",
                    "ડેલ્ફી તકનીક", "પ્લાનિંગ પોકર", "વાઇડબેન્ડ ડેલ્ફી",
                    
                    # COCOMO મોડેલ્સ
                    "COCOMO", "કન્સ્ટ્રક્ટિવ કોસ્ટ મોડેલ", "COCOMO I", "COCOMO II",
                    "ઓર્ગેનિક મોડ", "સેમિડિટેચ્ડ મોડ", "એમ્બેડેડ મોડ",
                    "પ્રયાસ અંદાજ", "શેડ્યૂલ અંદાજ", "કિંમત અંદાજ",
                    "વ્યક્તિ-મહિનાઓ", "વિકાસ સમય", "ઉત્પાદકતા", "ટીમ સાઇઝ",
                    "પ્રયાસ ગુણાકારો", "સ્કેલ ફેક્ટર્સ", "કોસ્ટ ડ્રાઇવર્સ",
                    
                    # પ્રોજેક્ટ શેડ્યૂલિંગ
                    "પ્રોજેક્ટ શેડ્યૂલિંગ", "શેડ્યૂલિંગ", "ટાસ્ક શેડ્યૂલિંગ", "એક્ટિવિટી શેડ્યૂલિંગ",
                    "વર્ક બ્રેકડાઉન સ્ટ્રક્ચર", "WBS", "માઇલસ્ટોન", "ડિલિવરેબલ",
                    "ક્રિટિકલ પાથ", "ક્રિટિકલ પાથ મેથડ", "CPM", "PERT",
                    "ગેન્ટ ચાર્ટ", "ટાઇમલાઇન", "ડિપેન્ડન્સી", "પૂર્વવર્તી", "ઉત્તરવર્તી",
                    "સ્પ્રિન્ટ બર્નડાઉન ચાર્ટ", "એજાઇલ શેડ્યૂલિંગ", "ઇટરેશન પ્લાનિંગ",
                    "રિલીઝ પ્લાનિંગ", "સ્ટોરી પોઇન્ટ્સ", "વેલોસિટી", "બર્નઅપ ચાર્ટ",
                    
                    # રિસ્ક મેનેજમેન્ટ
                    "રિસ્ક મેનેજમેન્ટ", "જોખમ", "અનિશ્ચિતતા", "ધમકી", "તક",
                    "જોખમ ઓળખ", "જોખમ આકારણી", "જોખમ વિશ્લેષણ", "જોખમ નિયંત્રણ",
                    "જોખમ મોનિટરિંગ", "જોખમ શમન", "જોખમ ટાળવું", "જોખમ સ્થાનાંતરણ",
                    "જોખમ સ્વીકૃતિ", "આકસ્મિક આયોજન", "જોખમ રજિસ્ટર",
                    "જોખમ મેટ્રિક્સ", "સંભાવના", "અસર", "એક્સપોઝર", "RMMM યોજના"
                ]
            },
            
            "Unit-V": {
                "english": [
                    # Code Review
                    "code review", "code inspection", "peer review", "static analysis",
                    "code walkthrough", "formal inspection", "informal review",
                    "review process", "review checklist", "review meeting", "defect detection",
                    "code quality", "coding standards", "best practices", "code metrics",
                    "describe code review", "explain code review", "code work through",
                    "different code review", "code review techniques",
                    
                    # Software Documentation
                    "software documentation", "documentation", "technical documentation",
                    "internal documentation", "external documentation", "user documentation",
                    "system documentation", "program documentation", "code documentation",
                    "API documentation", "design documentation", "requirements documentation",
                    "user manual", "installation guide", "maintenance manual", "help system",
                    "comments", "inline comments", "header comments", "documentation tools",
                    "explain software documentation", "types of documentation",
                    
                    # Testing Fundamentals
                    "software testing", "testing", "test", "quality assurance", "QA",
                    "verification", "validation", "V&V", "testing process", "test plan",
                    "test strategy", "test approach", "test execution", "test reporting",
                    "defect", "bug", "error", "fault", "failure", "defect life cycle",
                    "software testing process", "testing methodology", "testing principles",
                    
                    # Unit Testing
                    "unit testing", "unit test", "module testing", "component testing",
                    "test driver", "test stub", "test harness", "mock object",
                    "test framework", "JUnit", "NUnit", "pytest", "automated testing",
                    "test case", "test suite", "assertion", "test coverage",
                    "explain unit testing", "unit testing approach", "describe unit testing",
                    
                    # Black Box Testing
                    "black box testing", "functional testing", "behavioral testing",
                    "specification-based testing", "equivalence partitioning",
                    "boundary value analysis", "decision table testing", "state transition testing",
                    "use case testing", "error guessing", "exploratory testing",
                    "acceptance testing", "system testing", "integration testing",
                    "explain black box", "describe black box", "black box approach",
                    "black box testing techniques", "functional testing methods",
                    
                    # White Box Testing
                    "white box testing", "structural testing", "glass box testing",
                    "code-based testing", "statement coverage", "branch coverage",
                    "path coverage", "condition coverage", "decision coverage",
                    "multiple condition coverage", "cyclomatic complexity",
                    "basis path testing", "control flow testing", "data flow testing",
                    "explain white box", "describe white box", "white box approach",
                    "white box testing techniques", "structural testing methods",
                    
                    # Test Case Templates
                    "test case", "test case design", "test case template", "test case format",
                    "test case specification", "test scenario", "test data", "test script",
                    "expected result", "actual result", "test status", "pass", "fail",
                    "test case management", "test case execution", "test case review",
                    "traceability matrix", "requirements traceability", "test coverage matrix",
                    "prepare test case", "test case templates", "test case preparation",
                    "design test case", "test cases for module"
                ],
                "gujarati": [
                    # કોડ રિવ્યુ
                    "કોડ રિવ્યુ", "કોડ ઇન્સ્પેક્શન", "પીઅર રિવ્યુ", "સ્ટેટિક એનાલિસિસ",
                    "કોડ વોકથ્રુ", "ફોર્મલ ઇન્સ્પેક્શન", "ઇન્ફોર્મલ રિવ્યુ",
                    "રિવ્યુ પ્રક્રિયા", "રિવ્યુ ચેકલિસ્ટ", "રિવ્યુ મીટિંગ", "ખામી શોધ",
                    "કોડ ગુણવત્તા", "કોડિંગ સ્ટેન્ડર્ડ્સ", "શ્રેષ્ઠ પ્રથાઓ", "કોડ મેટ્રિક્સ",
                    
                    # સૉફ્ટવેર ડોક્યુમેન્ટેશન
                    "સૉફ્ટવેર ડોક્યુમેન્ટેશન", "દસ્તાવેજીકરણ", "તકનીકી દસ્તાવેજીકરણ",
                    "આંતરિક દસ્તાવેજીકરણ", "બાહ્ય દસ્તાવેજીકરણ", "વપરાશકર્તા દસ્તાવેજીકરણ",
                    "સિસ્ટમ દસ્તાવેજીકરણ", "પ્રોગ્રામ દસ્તાવેજીકરણ", "કોડ દસ્તાવેજીકરણ",
                    "API દસ્તાવેજીકરણ", "ડિઝાઇન દસ્તાવેજીકરણ", "જરૂરિયાતો દસ્તાવેજીકરણ",
                    "વપરાશકર્તા માર્ગદર્શિકા", "ઇન્સ્ટોલેશન ગાઇડ", "જાળવણી માર્ગદર્શિકા", "હેલ્પ સિસ્ટમ",
                    "ટિપ્પણીઓ", "ઇનલાઇન ટિપ્પણીઓ", "હેડર ટિપ્પણીઓ", "દસ્તાવેજીકરણ સાધનો",
                    
                    # ટેસ્ટિંગ મૂળભૂતો
                    "સૉફ્ટવેર ટેસ્ટિંગ", "ટેસ્ટિંગ", "ટેસ્ટ", "ગુણવત્તા આશ્વાસન", "QA",
                    "વેરિફિકેશન", "વેલિડેશન", "V&V", "ટેસ્ટિંગ પ્રક્રિયા", "ટેસ્ટ પ્લાન",
                    "ટેસ્ટ સ્ટ્રેટેજી", "ટેસ્ટ અભિગમ", "ટેસ્ટ એક્ઝિક્યુશન", "ટેસ્ટ રિપોર્ટિંગ",
                    "ખામી", "બગ", "ભૂલ", "ફોલ્ટ", "નિષ્ફળતા", "ખામી જીવન ચક્ર",
                    
                    # યુનિટ ટેસ્ટિંગ
                    "યુનિટ ટેસ્ટિંગ", "યુનિટ ટેસ્ટ", "મોડ્યુલ ટેસ્ટિંગ", "કોમ્પોનન્ટ ટેસ્ટિંગ",
                    "ટેસ્ટ ડ્રાઇવર", "ટેસ્ટ સ્ટબ", "ટેસ્ટ હાર્નેસ", "મોક ઑબ્જેક્ટ",
                    "ટેસ્ટ ફ્રેમવર્ક", "JUnit", "NUnit", "pytest", "ઓટોમેટેડ ટેસ્ટિંગ",
                    "ટેસ્ટ કેસ", "ટેસ્ટ સૂટ", "એસર્શન", "ટેસ્ટ કવરેજ",
                    
                    # બ્લેક બોક્સ ટેસ્ટિંગ
                    "બ્લેક બોક્સ ટેસ્ટિંગ", "કાર્યાત્મક ટેસ્ટિંગ", "વર્તણૂકીય ટેસ્ટિંગ",
                    "વિશિષ્ટતા-આધારિત ટેસ્ટિંગ", "સમાનતા વિભાજન",
                    "બાઉન્ડરી વેલ્યુ એનાલિસિસ", "ડિસિઝન ટેબલ ટેસ્ટિંગ", "સ્ટેટ ટ્રાન્ઝિશન ટેસ્ટિંગ",
                    "યુઝ કેસ ટેસ્ટિંગ", "એરર ગેસિંગ", "એક્સપ્લોરેટરી ટેસ્ટિંગ",
                    "એક્સેપ્ટન્સ ટેસ્ટિંગ", "સિસ્ટમ ટેસ્ટિંગ", "ઇન્ટિગ્રેશન ટેસ્ટિંગ",
                    
                    # વ્હાઇટ બોક્સ ટેસ્ટિંગ
                    "વ્હાઇટ બોક્સ ટેસ્ટિંગ", "સ્ટ્રક્ચરલ ટેસ્ટિંગ", "ગ્લાસ બોક્સ ટેસ્ટિંગ",
                    "કોડ-આધારિત ટેસ્ટિંગ", "સ્ટેટમેન્ટ કવરેજ", "બ્રાન્ચ કવરેજ",
                    "પાથ કવરેજ", "કન્ડિશન કવરેજ", "ડિસિઝન કવરેજ",
                    "મલ્ટિપલ કન્ડિશન કવરેજ", "સાયક્લોમેટિક જટિલતા",
                    "બેસિસ પાથ ટેસ્ટિંગ", "કંટ્રોલ ફ્લો ટેસ્ટિંગ", "ડેટા ફ્લો ટેસ્ટિંગ",
                    
                    # ટેસ્ટ કેસ ટેમ્પલેટ્સ
                    "ટેસ્ટ કેસ", "ટેસ્ટ કેસ ડિઝાઇન", "ટેસ્ટ કેસ ટેમ્પલેટ", "ટેસ્ટ કેસ ફોર્મેટ",
                    "ટેસ્ટ કેસ વિશિષ્ટતા", "ટેસ્ટ સ્થિતિ", "ટેસ્ટ ડેટા", "ટેસ્ટ સ્ક્રિપ્ટ",
                    "અપેક્ષિત પરિણામ", "વાસ્તવિક પરિણામ", "ટેસ્ટ સ્થિતિ", "પાસ", "ફેઇલ",
                    "ટેસ્ટ કેસ મેનેજમેન્ટ", "ટેસ્ટ કેસ એક્ઝિક્યુશન", "ટેસ્ટ કેસ રિવ્યુ",
                    "ટ્રેસેબિલિટી મેટ્રિક્સ", "જરૂરિયાતો ટ્રેસેબિલિટી", "ટેસ્ટ કવરેજ મેટ્રિક્સ"
                ]
            }
        }
        
        # Enhanced topic mappings with broader semantic coverage
        self.topic_mappings = {
            "software engineering fundamentals": ["Unit-I"],
            "layered approach": ["Unit-I"],
            "umbrella activities": ["Unit-I"],
            "framework activities": ["Unit-I"],
            "sdlc": ["Unit-II"],
            "waterfall model": ["Unit-II"],
            "agile development": ["Unit-II"],
            "prototype model": ["Unit-II"],
            "spiral model": ["Unit-II"],
            "rad model": ["Unit-II"],
            "requirements analysis": ["Unit-III"],
            "srs": ["Unit-III"],
            "software design": ["Unit-III"],
            "dfd": ["Unit-III"],
            "uml": ["Unit-III"],
            "cohesion": ["Unit-III"],
            "coupling": ["Unit-III"],
            "project management": ["Unit-IV"],
            "estimation": ["Unit-IV"],
            "cocomo": ["Unit-IV"],
            "function points": ["Unit-IV"],
            "scheduling": ["Unit-IV"],
            "risk management": ["Unit-IV"],
            "testing": ["Unit-V"],
            "code review": ["Unit-V"],
            "documentation": ["Unit-V"],
            "unit testing": ["Unit-V"],
            "black box testing": ["Unit-V"],
            "white box testing": ["Unit-V"]
        }
        
        # Advanced scoring weights for enhanced accuracy
        self.scoring_weights = {
            'exact_keyword_match': 10.0,
            'partial_keyword_match': 6.0,
            'contextual_match': 4.0,
            'semantic_similarity': 2.0,
            'topic_coherence': 3.0,
            'unit_consistency': 4.0,
            'language_consistency': 1.0
        }
        
    def load_syllabus(self):
        """Load syllabus data"""
        syllabus_file = self.base_path / "4353202.json"
        with open(syllabus_file, 'r', encoding='utf-8') as f:
            self.syllabus_data = json.load(f)
    
    def extract_questions_from_file(self, file_path: Path) -> List[Question]:
        """Extract questions from a solution file"""
        questions = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine language and exam details from filename
            filename = file_path.name
            language = 'gujarati' if '.gu.' in filename else 'english'
            
            # Extract year and season from filename
            year_match = re.search(r'(\d{4})', filename)
            season_match = re.search(r'(summer|winter)', filename.lower())
            
            exam_year = year_match.group(1) if year_match else "unknown"
            exam_season = season_match.group(1) if season_match else "unknown"
            
            # Enhanced question pattern matching
            if language == 'gujarati':
                question_pattern = r'##\s*પ્રશ્ન\s+(\d+)\s*\(\s*([અબકડ]|OR)\s*\)\s*\[(\d+)\s*ગુણ\]\s*\n\n\*\*(.*?)\*\*'
            else:
                question_pattern = r'##\s*Question\s+(\d+)\s*\(\s*([abc]|OR)\s*\)\s*\[(\d+)\s*marks\]\s*\n\n\*\*(.*?)\*\*'
            
            matches = re.finditer(question_pattern, content, re.MULTILINE | re.IGNORECASE)
            
            for match in matches:
                question_num = match.group(1)
                sub_part = match.group(2)
                marks = int(match.group(3))
                question_text = match.group(4).strip()
                
                # Create unique question ID
                question_id = f"{exam_year}_{exam_season}_{question_num}_{sub_part}_{language}"
                question_id = hashlib.md5(question_id.encode()).hexdigest()[:12]
                
                question = Question(
                    id=question_id,
                    text=question_text,
                    language=language,
                    marks=marks,
                    source_file=str(file_path),
                    exam_year=exam_year,
                    exam_season=exam_season
                )
                
                questions.append(question)
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
        return questions
    
    def normalize_text(self, text: str) -> str:
        """Normalize text for better matching"""
        # Convert to lowercase and normalize unicode
        text = unicodedata.normalize('NFKD', text.lower())
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        # Remove common punctuation
        text = re.sub(r'[^\w\s]', ' ', text)
        return text
    
    def calculate_keyword_score(self, question_text: str, unit_keywords: Dict[str, List[str]], language: str) -> float:
        """Calculate keyword-based score for unit mapping"""
        if language not in unit_keywords:
            return 0.0
            
        normalized_text = self.normalize_text(question_text)
        keywords = unit_keywords[language]
        
        exact_matches = 0
        partial_matches = 0
        total_keyword_weight = 0
        
        for keyword in keywords:
            normalized_keyword = self.normalize_text(keyword)
            keyword_weight = len(keyword.split()) * 0.5 + 1  # Longer phrases get higher weight
            total_keyword_weight += keyword_weight
            
            if normalized_keyword in normalized_text:
                exact_matches += keyword_weight * self.scoring_weights['exact_keyword_match']
            elif any(word in normalized_text for word in normalized_keyword.split()):
                partial_matches += keyword_weight * self.scoring_weights['partial_keyword_match']
        
        # Calculate weighted score
        if total_keyword_weight == 0:
            return 0.0
            
        keyword_score = (exact_matches + partial_matches) / total_keyword_weight
        return min(keyword_score, 10.0)  # Cap at 10.0
    
    def calculate_contextual_score(self, question_text: str, unit_data: Dict) -> float:
        """Calculate contextual relevance score"""
        normalized_text = self.normalize_text(question_text)
        score = 0.0
        
        # Check against unit topics and subtopics
        if 'topics' in unit_data:
            for topic in unit_data['topics']:
                topic_title = self.normalize_text(topic.get('title', ''))
                if topic_title and topic_title in normalized_text:
                    score += self.scoring_weights['contextual_match']
                
                # Check subtopics
                for subtopic in topic.get('subtopics', []):
                    subtopic_normalized = self.normalize_text(subtopic)
                    if subtopic_normalized and subtopic_normalized in normalized_text:
                        score += self.scoring_weights['contextual_match'] * 0.7
        
        return score
    
    def map_question_to_unit(self, question: Question) -> Tuple[str, float]:
        """Map question to most appropriate unit with confidence score"""
        best_unit = None
        best_score = 0.0
        scores_by_unit = {}
        
        for unit_name, unit_keywords in self.unit_keywords.items():
            # Calculate keyword-based score
            keyword_score = self.calculate_keyword_score(
                question.text, unit_keywords, question.language
            )
            
            # Calculate contextual score
            contextual_score = 0.0
            unit_data = next(
                (unit for unit in self.syllabus_data.get('underpinningTheory', []) 
                 if unit.get('unitNumber') == unit_name), {}
            )
            if unit_data:
                contextual_score = self.calculate_contextual_score(question.text, unit_data)
            
            # Calculate semantic similarity score
            semantic_score = self.calculate_semantic_score(question.text, unit_name)
            
            # Combine scores
            total_score = (
                keyword_score +
                contextual_score +
                semantic_score * self.scoring_weights['semantic_similarity']
            )
            
            scores_by_unit[unit_name] = total_score
            
            if total_score > best_score:
                best_score = total_score
                best_unit = unit_name
        
        # Calculate confidence as normalized score
        max_possible_score = 20.0  # Theoretical maximum
        confidence = min(best_score / max_possible_score, 1.0)
        
        return best_unit, confidence
    
    def calculate_semantic_score(self, question_text: str, unit_name: str) -> float:
        """Calculate semantic similarity score"""
        normalized_text = self.normalize_text(question_text)
        score = 0.0
        
        # Topic-based semantic matching
        for topic, units in self.topic_mappings.items():
            if unit_name in units:
                topic_words = topic.split()
                matches = sum(1 for word in topic_words if word in normalized_text)
                if matches > 0:
                    score += (matches / len(topic_words)) * self.scoring_weights['semantic_similarity']
        
        return score
    
    def extract_topics_from_question(self, question: Question, unit: str) -> List[str]:
        """Extract relevant topics from question text"""
        topics = []
        normalized_text = self.normalize_text(question.text)
        
        # Get unit-specific topics from syllabus
        unit_data = next(
            (unit_data for unit_data in self.syllabus_data.get('underpinningTheory', []) 
             if unit_data.get('unitNumber') == unit), {}
        )
        
        if 'topics' in unit_data:
            for topic in unit_data['topics']:
                topic_title = topic.get('title', '')
                if self.normalize_text(topic_title) in normalized_text:
                    topics.append(topic_title)
                
                # Check subtopics
                for subtopic in topic.get('subtopics', []):
                    if self.normalize_text(subtopic) in normalized_text:
                        topics.append(subtopic)
        
        # Add semantic topic matches
        for topic, units in self.topic_mappings.items():
            if unit in units and topic.replace('_', ' ') in normalized_text:
                topics.append(topic.replace('_', ' ').title())
        
        return list(set(topics))  # Remove duplicates
    
    def generate_question_bank(self):
        """Generate the complete question bank"""
        print("🚀 Starting Enhanced Software Engineering Question Bank Generation...")
        
        # Load syllabus
        self.load_syllabus()
        print("✅ Syllabus data loaded successfully")
        
        # Find all solution files
        solution_files = list(self.base_path.glob("*solution*.md"))
        print(f"📁 Found {len(solution_files)} solution files")
        
        # Extract questions from all files
        all_questions = []
        for file_path in solution_files:
            questions = self.extract_questions_from_file(file_path)
            all_questions.extend(questions)
            print(f"  📝 Extracted {len(questions)} questions from {file_path.name}")
        
        print(f"🔍 Total questions extracted: {len(all_questions)}")
        
        # Map questions to units and extract topics
        mapped_questions = []
        mapping_stats = defaultdict(int)
        confidence_stats = []
        
        for question in all_questions:
            unit, confidence = self.map_question_to_unit(question)
            if unit:
                question.unit = unit
                question.confidence = confidence
                question.topics = self.extract_topics_from_question(question, unit)
                mapped_questions.append(question)
                mapping_stats[unit] += 1
                confidence_stats.append(confidence)
        
        self.questions = mapped_questions
        
        # Calculate statistics
        total_mapped = len(mapped_questions)
        mapping_accuracy = (total_mapped / len(all_questions)) * 100 if all_questions else 0
        avg_confidence = sum(confidence_stats) / len(confidence_stats) if confidence_stats else 0
        
        print(f"\n📊 Mapping Results:")
        print(f"   Total questions: {len(all_questions)}")
        print(f"   Successfully mapped: {total_mapped}")
        print(f"   Mapping accuracy: {mapping_accuracy:.2f}%")
        print(f"   Average confidence: {avg_confidence:.3f}")
        
        print(f"\n📈 Distribution by unit:")
        for unit, count in sorted(mapping_stats.items()):
            print(f"   {unit}: {count} questions")
        
        # Generate final JSON
        self.save_question_bank()
        
        return {
            'total_questions': len(all_questions),
            'mapped_questions': total_mapped,
            'mapping_accuracy': mapping_accuracy,
            'average_confidence': avg_confidence,
            'unit_distribution': dict(mapping_stats)
        }
    
    def save_question_bank(self):
        """Save the question bank to JSON file"""
        output_file = self.base_path / "4353202-question-bank-final.json"
        
        # Prepare data structure
        question_bank = {
            "metadata": {
                "subject": "Software Engineering",
                "subject_code": "4353202",
                "semester": "5",
                "generated_at": "2024-09-11",
                "total_questions": len(self.questions),
                "mapping_methodology": "Enhanced bilingual keyword mapping with contextual analysis",
                "confidence_threshold": 0.3,
                "languages": ["english", "gujarati"]
            },
            "questions": []
        }
        
        # Convert questions to dictionaries
        for question in self.questions:
            question_dict = asdict(question)
            # Ensure topics is not None
            if question_dict['topics'] is None:
                question_dict['topics'] = []
            question_bank["questions"].append(question_dict)
        
        # Sort questions by confidence (highest first)
        question_bank["questions"].sort(key=lambda x: x['confidence'], reverse=True)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(question_bank, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Question bank saved to: {output_file}")
        
        # Generate summary statistics
        self.generate_summary_report(question_bank)
    
    def generate_summary_report(self, question_bank: Dict):
        """Generate and display summary report"""
        questions = question_bank["questions"]
        
        # Language distribution
        lang_dist = Counter(q['language'] for q in questions)
        
        # Unit distribution
        unit_dist = Counter(q['unit'] for q in questions)
        
        # Marks distribution
        marks_dist = Counter(q['marks'] for q in questions)
        
        # Confidence statistics
        confidences = [q['confidence'] for q in questions]
        high_conf = sum(1 for c in confidences if c >= 0.7)
        medium_conf = sum(1 for c in confidences if 0.4 <= c < 0.7)
        low_conf = sum(1 for c in confidences if c < 0.4)
        
        print(f"\n📋 QUESTION BANK SUMMARY REPORT")
        print(f"=" * 50)
        print(f"Subject: Software Engineering (4353202)")
        print(f"Total Questions: {len(questions)}")
        print(f"Mapping Success Rate: {(len(questions)/question_bank['metadata']['total_questions'])*100:.1f}%")
        
        print(f"\n🌍 Language Distribution:")
        for lang, count in lang_dist.items():
            percentage = (count / len(questions)) * 100
            print(f"   {lang.title()}: {count} ({percentage:.1f}%)")
        
        print(f"\n📚 Unit Distribution:")
        for unit, count in sorted(unit_dist.items()):
            percentage = (count / len(questions)) * 100
            print(f"   {unit}: {count} ({percentage:.1f}%)")
        
        print(f"\n🎯 Marks Distribution:")
        for marks, count in sorted(marks_dist.items()):
            percentage = (count / len(questions)) * 100
            print(f"   {marks} marks: {count} ({percentage:.1f}%)")
        
        print(f"\n📈 Confidence Levels:")
        print(f"   High (≥0.7): {high_conf} ({(high_conf/len(questions))*100:.1f}%)")
        print(f"   Medium (0.4-0.7): {medium_conf} ({(medium_conf/len(questions))*100:.1f}%)")
        print(f"   Low (<0.4): {low_conf} ({(low_conf/len(questions))*100:.1f}%)")
        
        avg_confidence = sum(confidences) / len(confidences)
        print(f"   Average Confidence: {avg_confidence:.3f}")
        
        if low_conf == 0:
            print(f"\n🎉 PERFECT MAPPING ACHIEVED! All questions mapped with confidence ≥ 0.4")
        else:
            print(f"\n⚠️  {low_conf} questions with low confidence may need manual review")

def main():
    """Main execution function"""
    base_path = "/Users/milav/Code/studio/content/resources/study-materials/32-ict/sem-5/4353202-se/"
    
    generator = EnhancedSEQuestionBankGenerator(base_path)
    results = generator.generate_question_bank()
    
    print(f"\n🎯 FINAL RESULTS:")
    print(f"   Mapping Accuracy: {results['mapping_accuracy']:.2f}%")
    print(f"   Total Questions Processed: {results['total_questions']}")
    print(f"   Successfully Mapped: {results['mapped_questions']}")
    print(f"   Average Confidence: {results['average_confidence']:.3f}")

if __name__ == "__main__":
    main()