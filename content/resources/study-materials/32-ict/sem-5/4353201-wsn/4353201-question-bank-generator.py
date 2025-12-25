#!/usr/bin/env python3
"""
Enhanced Question Bank Generator for Wireless Sensor Networks and IoT (4353201)
Comprehensive bilingual question extraction and mapping system for WSN
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

class EnhancedWSNQuestionBankGenerator:
    """Enhanced question bank generator for Wireless Sensor Networks and IoT"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.syllabus_data = {}
        self.questions = []
        
        # Enhanced bilingual keyword mappings for WSN and IoT
        self.unit_keywords = {
            "Unit-I": {
                "english": [
                    # WSN Fundamentals
                    "wireless sensor network", "WSN", "sensor network", "wireless network",
                    "sensor node", "sensor nodes", "sensing", "distributed sensing",
                    "autonomous sensor", "spatially distributed", "monitoring",
                    
                    # Single-Node Architecture
                    "single node", "node architecture", "sensor node architecture",
                    "sensor node design", "hardware components", "node components",
                    
                    # Hardware Components
                    "sensing subsystem", "processor subsystem", "communication subsystem",
                    "power subsystem", "sensing unit", "processing unit", "communication unit",
                    "power unit", "hardware", "components", "subsystem",
                    "ADC", "analog to digital converter", "transceiver", "antenna",
                    "microcontroller", "microprocessor", "memory", "battery",
                    
                    # Specific Hardware 
                    "IMote", "XYZ node", "Hog throb", "prototypes", "node prototypes",
                    "communication interfaces", "sensing interfaces",
                    
                    # Energy and Power
                    "energy consumption", "power consumption", "battery life",
                    "energy efficiency", "power management", "energy harvesting",
                    "power optimization", "sleep mode", "active mode",
                    
                    # Operating Systems
                    "operating system", "execution environment", "embedded OS",
                    "TinyOS", "Contiki", "RIOT", "real time operating system",
                    
                    # Network Architecture
                    "network architecture", "sensor network scenarios", "topology",
                    "network topology", "star topology", "mesh topology", "tree topology",
                    "cluster topology", "hierarchical topology",
                    
                    # Optimization and Design
                    "optimization goals", "figures of merit", "design principles",
                    "network lifetime", "coverage", "connectivity", "scalability",
                    "cost effectiveness", "data quality", "reliability",
                    
                    # Challenges and Constraints
                    "challenges", "constraints", "unique challenges", "limitations",
                    "resource constraints", "energy constraints", "bandwidth constraints",
                    "computational constraints", "memory constraints",
                    
                    # Applications
                    "applications", "environmental monitoring", "habitat monitoring",
                    "military surveillance", "health monitoring", "smart agriculture",
                    "industrial monitoring", "home automation", "structural monitoring"
                ],
                "gujarati": [
                    # WSN મૂળભૂતો
                    "વાયરલેસ સેન્સર નેટવર્ક", "WSN", "સેન્સર નેટવર્ક", "વાયરલેસ નેટવર્ક",
                    "સેન્સર નોડ", "સેન્સર નોડ્સ", "સેન્સિંગ", "વિતરિત સેન્સિંગ",
                    "સ્વાયત્ત સેન્સર", "અવકાશીય રીતે વિતરિત", "નિરીક્ષણ",
                    
                    # સિંગલ-નોડ આર્કિટેક્ચર
                    "સિંગલ નોડ", "નોડ આર્કિટેક્ચર", "સેન્સર નોડ આર્કિટેક્ચર",
                    "સેન્સર નોડ ડિઝાઇન", "હાર્ડવેર ઘટકો", "નોડ ઘટકો",
                    
                    # હાર્ડવેર ઘટકો
                    "સેન્સિંગ સબસિસ્ટમ", "પ્રોસેસર સબસિસ્ટમ", "કમ્યુનિકેશન સબસિસ્ટમ",
                    "પાવર સબસિસ્ટમ", "સેન્સિંગ યુનિટ", "પ્રોસેસિંગ યુનિટ", "કમ્યુનિકેશન યુનિટ",
                    "પાવર યુનિટ", "હાર્ડવેર", "ઘટકો", "સબસિસ્ટમ",
                    "ADC", "એનાલોગ ટુ ડિજિટલ કન્વર્ટર", "ટ્રાન્સીવર", "એન્ટેના",
                    "માઇક્રોકંટ્રોલર", "માઇક્રોપ્રોસેસર", "મેમોરી", "બેટરી",
                    
                    # વિશિષ્ટ હાર્ડવેર
                    "IMote", "XYZ નોડ", "Hog throb", "પ્રોટોટાઇપ્સ", "નોડ પ્રોટોટાઇપ્સ",
                    "કમ્યુનિકેશન ઇન્ટરફેસ", "સેન્સિંગ ઇન્ટરફેસ",
                    
                    # એનર્જી અને પાવર
                    "એનર્જી વપરાશ", "પાવર વપરાશ", "બેટરી લાઇફ",
                    "એનર્જી એફિશિયન્સી", "પાવર મેનેજમેન્ટ", "એનર્જી હાર્વેસ્ટિંગ",
                    "પાવર ઓપ્ટિમાઇઝેશન", "સ્લીપ મોડ", "એક્ટિવ મોડ",
                    
                    # ઓપરેટિંગ સિસ્ટમ્સ
                    "ઓપરેટિંગ સિસ્ટમ", "એક્ઝિક્યુશન એન્વાયરનમેન્ટ", "એમ્બેડેડ OS",
                    "TinyOS", "Contiki", "RIOT", "રીઅલ ટાઇમ ઓપરેટિંગ સિસ્ટમ",
                    
                    # નેટવર્ક આર્કિટેક્ચર
                    "નેટવર્ક આર્કિટેક્ચર", "સેન્સર નેટવર્ક દૃશ્યો", "ટોપોલોજી",
                    "નેટવર્ક ટોપોલોજી", "સ્ટાર ટોપોલોજી", "મેશ ટોપોલોજી", "ટ્રી ટોપોલોજી",
                    "ક્લસ્ટર ટોપોલોજી", "હાઇરાર્કિકલ ટોપોલોજી",
                    
                    # ઓપ્ટિમાઇઝેશન અને ડિઝાઇન
                    "ઓપ્ટિમાઇઝેશન ગોલ્સ", "ફિગર્સ ઓફ મેરિટ", "ડિઝાઇન સિદ્ધાંતો",
                    "નેટવર્ક લાઇફટાઇમ", "કવરેજ", "કનેક્ટિવિટી", "સ્કેલેબિલિટી",
                    "કોસ્ટ ઇફેક્ટિવનેસ", "ડેટા ક્વોલિટી", "વિશ્વસનીયતા",
                    
                    # પડકારો અને મર્યાદાઓ
                    "પડકારો", "મર્યાદાઓ", "અનન્ય પડકારો", "લિમિટેશન્સ",
                    "રિસોર્સ મર્યાદાઓ", "એનર્જી મર્યાદાઓ", "બેન્ડવિડ્થ મર્યાદાઓ",
                    "કોમ્પ્યુટેશનલ મર્યાદાઓ", "મેમોરી મર્યાદાઓ",
                    
                    # એપ્લિકેશન્સ
                    "એપ્લિકેશન્સ", "પર્યાવરણીય મોનિટરિંગ", "હેબિટેટ મોનિટરિંગ",
                    "મિલિટરી સર્વેલન્સ", "આરોગ્ય મોનિટરિંગ", "સ્માર્ટ એગ્રિકલ્ચર",
                    "ઇન્ડસ્ટ્રિયલ મોનિટરિંગ", "હોમ ઓટોમેશન", "સ્ટ્રક્ચરલ મોનિટરિંગ"
                ]
            },
            
            "Unit-II": {
                "english": [
                    # Physical Layer
                    "physical layer", "transceiver design", "radio frequency", "RF",
                    "modulation", "demodulation", "signal processing", "antenna design",
                    "transmission power", "receiver sensitivity", "frequency band",
                    "ISM band", "2.4 GHz", "915 MHz", "433 MHz",
                    
                    # MAC Protocols
                    "MAC protocol", "medium access control", "MAC layer", "channel access",
                    "collision avoidance", "collision detection", "CSMA", "TDMA", "FDMA",
                    "contention based", "schedule based", "classification of MAC",
                    
                    # Low Duty Cycle Protocols
                    "low duty cycle", "S-MAC", "T-MAC", "B-MAC", "X-MAC", "RI-MAC",
                    "IEEE 802.15.4", "ZigBee", "wakeup", "sleep scheduling",
                    "duty cycling", "energy efficient MAC", "listen period",
                    
                    # Schedule-based Protocols
                    "LEACH", "SMACS", "TRAMA", "HEED", "PEGASIS", "TEEN", "APTEEN",
                    "cluster head", "clustering", "hierarchical routing", "round",
                    "setup phase", "steady state", "data aggregation",
                    
                    # Address and Name Management
                    "address management", "name management", "addressing scheme",
                    "MAC address", "network address", "node identification",
                    "address assignment", "address allocation", "unique identifier",
                    
                    # MAC Address Assignment
                    "MAC address assignment", "static assignment", "dynamic assignment",
                    "local assignment", "global assignment", "address conflict",
                    "address resolution", "duplicate address detection",
                    
                    # Routing Protocols
                    "routing protocol", "routing algorithm", "energy efficient routing",
                    "geographic routing", "location based routing", "hierarchical routing",
                    "flat routing", "proactive routing", "reactive routing", "hybrid routing",
                    
                    # Energy-Efficient Routing
                    "SPIN", "Directed Diffusion", "Rumor Routing", "GEAR", "GPSR",
                    "minimum energy", "maximum lifetime", "energy aware",
                    "power efficient", "load balancing", "energy consumption model",
                    
                    # Geographic and Hierarchical Routing
                    "geographic routing", "position based", "location service", "GPS",
                    "coordinate system", "greedy forwarding", "face routing",
                    "hierarchical networks", "clustering algorithm", "cluster formation",
                    "inter-cluster", "intra-cluster", "cluster maintenance",
                    
                    # Quality of Service
                    "quality of service", "QoS", "real time", "delay", "throughput",
                    "reliability", "packet loss", "jitter", "bandwidth",
                    "end to end delay", "network performance", "service differentiation"
                ],
                "gujarati": [
                    # ફિઝિકલ લેયર
                    "ફિઝિકલ લેયર", "ટ્રાન્સીવર ડિઝાઇન", "રેડિયો ફ્રીક્વન્સી", "RF",
                    "મોડ્યુલેશન", "ડિમોડ્યુલેશન", "સિગ્નલ પ્રોસેસિંગ", "એન્ટેના ડિઝાઇન",
                    "ટ્રાન્સમિશન પાવર", "રીસીવર સેન્સિટિવિટી", "ફ્રીક્વન્સી બેન્ડ",
                    "ISM બેન્ડ", "2.4 GHz", "915 MHz", "433 MHz",
                    
                    # MAC પ્રોટોકોલ્સ
                    "MAC પ્રોટોકોલ", "મીડિયમ એક્સેસ કંટ્રોલ", "MAC લેયર", "ચેનલ એક્સેસ",
                    "કોલિઝન એવોઇડન્સ", "કોલિઝન ડિટેક્શન", "CSMA", "TDMA", "FDMA",
                    "કન્ટેન્શન આધારિત", "શેડ્યુલ આધારિત", "MAC નું વર્ગીકરણ",
                    
                    # લો ડ્યુટી સાયકલ પ્રોટોકોલ્સ
                    "લો ડ્યુટી સાયકલ", "S-MAC", "T-MAC", "B-MAC", "X-MAC", "RI-MAC",
                    "IEEE 802.15.4", "ZigBee", "વેકઅપ", "સ્લીપ શેડ્યુલિંગ",
                    "ડ્યુટી સાયકલિંગ", "એનર્જી એફિશિયન્ટ MAC", "લિસન પીરિયડ",
                    
                    # શેડ્યુલ-આધારિત પ્રોટોકોલ્સ
                    "LEACH", "SMACS", "TRAMA", "HEED", "PEGASIS", "TEEN", "APTEEN",
                    "ક્લસ્ટર હેડ", "ક્લસ્ટરિંગ", "હાઇરાર્કિકલ રાઉટિંગ", "રાઉન્ડ",
                    "સેટઅપ ફેઝ", "સ્ટેડી સ્ટેટ", "ડેટા એગ્રિગેશન",
                    
                    # એડ્રેસ અને નેમ મેનેજમેન્ટ
                    "એડ્રેસ મેનેજમેન્ટ", "નેમ મેનેજમેન્ટ", "એડ્રેસિંગ સ્કીમ",
                    "MAC એડ્રેસ", "નેટવર્ક એડ્રેસ", "નોડ આઇડેન્ટિફિકેશન",
                    "એડ્રેસ અસાઇનમેન્ટ", "એડ્રેસ એલોકેશન", "યુનિક આઇડેન્ટિફાયર",
                    
                    # MAC એડ્રેસ અસાઇનમેન્ટ
                    "MAC એડ્રેસ અસાઇનમેન્ટ", "સ્ટેટિક અસાઇનમેન્ટ", "ડાયનેમિક અસાઇનમેન્ટ",
                    "લોકલ અસાઇનમેન્ટ", "ગ્લોબલ અસાઇનમેન્ટ", "એડ્રેસ કન્ફ્લિક્ટ",
                    "એડ્રેસ રેઝોલ્યુશન", "ડુપ્લિકેટ એડ્રેસ ડિટેક્શન",
                    
                    # રાઉટિંગ પ્રોટોકોલ્સ
                    "રાઉટિંગ પ્રોટોકોલ", "રાઉટિંગ અલ્ગોરિધમ", "એનર્જી એફિશિયન્ટ રાઉટિંગ",
                    "જિયોગ્રાફિક રાઉટિંગ", "લોકેશન આધારિત રાઉટિંગ", "હાઇરાર્કિકલ રાઉટિંગ",
                    "ફ્લેટ રાઉટિંગ", "પ્રોએક્ટિવ રાઉટિંગ", "રીએક્ટિવ રાઉટિંગ", "હાઇબ્રિડ રાઉટિંગ",
                    
                    # એનર્જી-એફિશિયન્ટ રાઉટિંગ
                    "SPIN", "ડાયરેક્ટેડ ડિફ્યુઝન", "રુમર રાઉટિંગ", "GEAR", "GPSR",
                    "મિનિમમ એનર્જી", "મેક્સિમમ લાઇફટાઇમ", "એનર્જી અવેર",
                    "પાવર એફિશિયન્ટ", "લોડ બેલેન્સિંગ", "એનર્જી કન્ઝમ્પશન મોડેલ",
                    
                    # જિયોગ્રાફિક અને હાઇરાર્કિકલ રાઉટિંગ
                    "જિયોગ્રાફિક રાઉટિંગ", "પોઝિશન આધારિત", "લોકેશન સર્વિસ", "GPS",
                    "કોઓર્ડિનેટ સિસ્ટમ", "ગ્રીડી ફોરવર્ડિંગ", "ફેસ રાઉટિંગ",
                    "હાઇરાર્કિકલ નેટવર્ક્સ", "ક્લસ્ટરિંગ અલ્ગોરિધમ", "ક્લસ્ટર ફોર્મેશન",
                    "ઇન્ટર-ક્લસ્ટર", "ઇન્ટ્રા-ક્લસ્ટર", "ક્લસ્ટર મેઇન્ટેનન્સ",
                    
                    # ક્વોલિટી ઓફ સર્વિસ
                    "ક્વોલિટી ઓફ સર્વિસ", "QoS", "રીઅલ ટાઇમ", "ડેલે", "થ્રુપુટ",
                    "રિલાયેબિલિટી", "પેકેટ લોસ", "જિટર", "બેન્ડવિડ્થ",
                    "એન્ડ ટુ એન્ડ ડેલે", "નેટવર્ક પરફોર્મન્સ", "સર્વિસ ડિફરન્શિએશન"
                ]
            },
            
            "Unit-III": {
                "english": [
                    # IoT Conceptual Framework
                    "internet of things", "IoT", "conceptual framework", "IoT framework",
                    "connected devices", "smart devices", "embedded systems", "cyber physical systems",
                    "ubiquitous computing", "pervasive computing", "ambient intelligence",
                    
                    # IoT Architectural View
                    "IoT architecture", "architectural view", "IoT layers", "IoT stack",
                    "three layer architecture", "four layer architecture", "five layer architecture",
                    "perception layer", "network layer", "middleware layer", "application layer",
                    "business layer", "sensing layer", "connectivity layer", "data processing layer",
                    
                    # Technology Behind IoT
                    "IoT technology", "enabling technologies", "RFID", "NFC", "Bluetooth",
                    "WiFi", "ZigBee", "Z-Wave", "LoRa", "SigFox", "cellular", "satellite",
                    "wireless communication", "wired communication", "6LoWPAN", "IPv6",
                    
                    # Sources of IoT
                    "IoT sources", "data sources", "sensor data", "actuator data",
                    "environmental data", "location data", "user data", "device data",
                    "contextual data", "real time data", "streaming data",
                    
                    # M2M Communication
                    "machine to machine", "M2M", "M2M communication", "device communication",
                    "automated communication", "autonomous communication", "direct communication",
                    "protocol", "communication protocol", "messaging", "data exchange",
                    
                    # Modified OSI Model
                    "modified OSI", "IoT OSI model", "M2M OSI model", "protocol stack",
                    "layered architecture", "communication layers", "network protocols",
                    "application protocols", "transport protocols", "network protocols",
                    
                    # Major Components
                    "IoT components", "major components", "sensors", "actuators", "gateways",
                    "cloud platform", "analytics", "user interface", "mobile app",
                    "web application", "dashboard", "data storage", "database",
                    
                    # Development Boards
                    "development boards", "IoT boards", "Arduino", "Raspberry Pi", "NodeMCU",
                    "ESP8266", "ESP32", "BeagleBone", "Intel Edison", "ARM mbed",
                    "microcontroller", "single board computer", "prototyping platform",
                    
                    # IoT Applications
                    "IoT applications", "smart home", "smart city", "smart agriculture",
                    "industrial IoT", "IIoT", "healthcare IoT", "wearable devices",
                    "smart grid", "smart transportation", "environmental monitoring",
                    "asset tracking", "supply chain", "retail", "connected car"
                ],
                "gujarati": [
                    # IoT કોન્સેપ્ચ્યુઅલ ફ્રેમવર્ક
                    "ઇન્ટરનેટ ઓફ થિંગ્સ", "IoT", "કોન્સેપ્ચ્યુઅલ ફ્રેમવર્ક", "IoT ફ્રેમવર્ક",
                    "કનેક્ટેડ ડિવાઇસિસ", "સ્માર્ટ ડિવાઇસિસ", "એમ્બેડેડ સિસ્ટમ્સ", "સાયબર ફિઝિકલ સિસ્ટમ્સ",
                    "યુબિક્વિટસ કોમ્પ્યુટિંગ", "પર્વેસિવ કોમ્પ્યુટિંગ", "એમ્બિયન્ટ ઇન્ટેલિજન્સ",
                    
                    # IoT આર્કિટેક્ચરલ વ્યુ
                    "IoT આર્કિટેક્ચર", "આર્કિટેક્ચરલ વ્યુ", "IoT લેયર્સ", "IoT સ્ટેક",
                    "ત્રણ લેયર આર્કિટેક્ચર", "ચાર લેયર આર્કિટેક્ચર", "પાંચ લેયર આર્કિટેક્ચર",
                    "પરસેપ્શન લેયર", "નેટવર્ક લેયર", "મિડલવેર લેયર", "એપ્લિકેશન લેયર",
                    "બિઝનેસ લેયર", "સેન્સિંગ લેયર", "કનેક્ટિવિટી લેયર", "ડેટા પ્રોસેસિંગ લેયર",
                    
                    # IoT પાછળની ટેકનોલોજી
                    "IoT ટેકનોલોજી", "એનેબલિંગ ટેકનોલોજીઝ", "RFID", "NFC", "બ્લુટૂથ",
                    "WiFi", "ZigBee", "Z-Wave", "LoRa", "SigFox", "સેલ્યુલર", "સેટેલાઇટ",
                    "વાયરલેસ કોમ્યુનિકેશન", "વાયર્ડ કોમ્યુનિકેશન", "6LoWPAN", "IPv6",
                    
                    # IoT ના સ્રોતો
                    "IoT સ્રોતો", "ડેટા સ્રોતો", "સેન્સર ડેટા", "એક્ચ્યુએટર ડેટા",
                    "પર્યાવરણીય ડેટા", "લોકેશન ડેટા", "યુઝર ડેટા", "ડિવાઇસ ડેટા",
                    "કોન્ટેક્સ્ચ્યુઅલ ડેટા", "રીઅલ ટાઇમ ડેટા", "સ્ટ્રીમિંગ ડેટા",
                    
                    # M2M કોમ્યુનિકેશન
                    "મશીન ટુ મશીન", "M2M", "M2M કોમ્યુનિકેશન", "ડિવાઇસ કોમ્યુનિકેશન",
                    "ઓટોમેટેડ કોમ્યુનિકેશન", "ઓટોનોમસ કોમ્યુનિકેશન", "ડાયરેક્ટ કોમ્યુનિકેશન",
                    "પ્રોટોકોલ", "કોમ્યુનિકેશન પ્રોટોકોલ", "મેસેજિંગ", "ડેટા એક્સચેન્જ",
                    
                    # મોડિફાઇડ OSI મોડેલ
                    "મોડિફાઇડ OSI", "IoT OSI મોડેલ", "M2M OSI મોડેલ", "પ્રોટોકોલ સ્ટેક",
                    "લેયર્ડ આર્કિટેક્ચર", "કોમ્યુનિકેશન લેયર્સ", "નેટવર્ક પ્રોટોકોલ્સ",
                    "એપ્લિકેશન પ્રોટોકોલ્સ", "ટ્રાન્સપોર્ટ પ્રોટોકોલ્સ", "નેટવર્ક પ્રોટોકોલ્સ",
                    
                    # મુખ્ય ઘટકો
                    "IoT ઘટકો", "મુખ્ય ઘટકો", "સેન્સર્સ", "એક્ચ્યુએટર્સ", "ગેટવેઝ",
                    "ક્લાઉડ પ્લેટફોર્મ", "એનાલિટિક્સ", "યુઝર ઇન્ટરફેસ", "મોબાઇલ એપ",
                    "વેબ એપ્લિકેશન", "ડેશબોર્ડ", "ડેટા સ્ટોરેજ", "ડેટાબેઝ",
                    
                    # ડેવલપમેન્ટ બોર્ડ્સ
                    "ડેવલપમેન્ટ બોર્ડ્સ", "IoT બોર્ડ્સ", "આર્ડુઇનો", "રાસ્પબેરી પાઇ", "NodeMCU",
                    "ESP8266", "ESP32", "BeagleBone", "Intel Edison", "ARM mbed",
                    "માઇક્રોકંટ્રોલર", "સિંગલ બોર્ડ કોમ્પ્યુટર", "પ્રોટોટાઇપિંગ પ્લેટફોર્મ",
                    
                    # IoT એપ્લિકેશન્સ
                    "IoT એપ્લિકેશન્સ", "સ્માર્ટ હોમ", "સ્માર્ટ સિટી", "સ્માર્ટ એગ્રિકલ્ચર",
                    "ઇન્ડસ્ટ્રિયલ IoT", "IIoT", "હેલ્થકેર IoT", "વેરેબલ ડિવાઇસિસ",
                    "સ્માર્ટ ગ્રિડ", "સ્માર્ટ ટ્રાન્સપોર્ટેશન", "એન્વાયરનમેન્ટલ મોનિટરિંગ",
                    "એસેટ ટ્રેકિંગ", "સપ્લાય ચેઇન", "રિટેલ", "કનેક્ટેડ કાર"
                ]
            },
            
            "Unit-IV": {
                "english": [
                    # Types of Sensors and Actuators
                    "sensors", "actuators", "temperature sensor", "humidity sensor", "pressure sensor",
                    "light sensor", "motion sensor", "proximity sensor", "gas sensor", "pH sensor",
                    "accelerometer", "gyroscope", "magnetometer", "GPS", "camera", "microphone",
                    "servo motor", "stepper motor", "relay", "LED", "buzzer", "speaker",
                    "solenoid", "valve", "pump", "heater", "cooler", "fan",
                    
                    # IoT Components and Implementation
                    "IoT components", "implementation", "microcontroller", "development board",
                    "communication module", "power management", "sensor interfacing",
                    "actuator control", "GPIO", "PWM", "ADC", "DAC", "I2C", "SPI", "UART",
                    
                    # IoT Protocols
                    "IoT protocols", "communication protocols", "network protocols",
                    
                    # Link Layer Protocols
                    "link layer protocols", "Ethernet", "WiFi", "Bluetooth", "ZigBee",
                    "Z-Wave", "6LoWPAN", "LoRa", "SigFox", "NB-IoT", "LTE-M",
                    
                    # Network/Internet Layer Protocols
                    "network layer protocols", "internet layer protocols", "IPv4", "IPv6",
                    "ICMPv6", "RPL", "routing protocol", "mesh networking",
                    
                    # Transport Layer Protocols
                    "transport layer protocols", "TCP", "UDP", "SCTP", "QUIC",
                    "reliable transport", "unreliable transport", "connection oriented",
                    "connectionless", "flow control", "congestion control",
                    
                    # Application Layer Protocols
                    "application layer protocols", "HTTP", "HTTPS", "FTP", "CoAP",
                    "MQTT", "XMPP", "AMQP", "DDS", "WebSocket", "REST", "SOAP",
                    "constrained application protocol", "message queuing", "publish subscribe",
                    
                    # IoT Security
                    "IoT security", "security issues", "security challenges", "vulnerabilities",
                    "authentication", "authorization", "encryption", "data integrity",
                    "privacy", "secure communication", "key management", "certificate management",
                    "device security", "network security", "application security", "data security",
                    
                    # Prototyping and Software Design
                    "prototyping", "software design", "IoT applications", "development environment",
                    "IDE", "programming languages", "embedded programming", "cloud integration",
                    "API development", "web services", "mobile app development",
                    
                    # NodeMCU and Raspberry Pi
                    "NodeMCU", "Raspberry Pi", "block diagram", "pin configuration",
                    "ESP8266", "ESP32", "GPIO pins", "power supply", "WiFi module",
                    "Bluetooth module", "analog pins", "digital pins", "PWM pins",
                    
                    # Cloud Integration and Device Control
                    "sensor data", "cloud transmission", "cloud platform", "data upload",
                    "device control", "remote control", "mobile application", "web application",
                    "cloud services", "AWS IoT", "Google Cloud IoT", "Azure IoT",
                    "ThingSpeak", "Blynk", "Firebase", "real time database"
                ],
                "gujarati": [
                    # સેન્સર્સ અને એક્ચ્યુએટર્સના પ્રકારો
                    "સેન્સર્સ", "એક્ચ્યુએટર્સ", "ટેમ્પરેચર સેન્સર", "હ્યુમિડિટી સેન્સર", "પ્રેશર સેન્સર",
                    "લાઇટ સેન્સર", "મોશન સેન્સર", "પ્રોક્સિમિટી સેન્સર", "ગેસ સેન્સર", "pH સેન્સર",
                    "એક્સેલેરોમીટર", "જાયરોસ્કોપ", "મેગ્નેટોમીટર", "GPS", "કેમેરા", "માઇક્રોફોન",
                    "સર્વો મોટર", "સ્ટેપર મોટર", "રિલે", "LED", "બઝર", "સ્પીકર",
                    "સોલેનોઇડ", "વાલ્વ", "પંપ", "હીટર", "કૂલર", "ફેન",
                    
                    # IoT ઘટકો અને અમલીકરણ
                    "IoT ઘટકો", "અમલીકરણ", "માઇક્રોકંટ્રોલર", "ડેવલપમેન્ટ બોર્ડ",
                    "કોમ્યુનિકેશન મોડ્યુલ", "પાવર મેનેજમેન્ટ", "સેન્સર ઇન્ટરફેસિંગ",
                    "એક્ચ્યુએટર કંટ્રોલ", "GPIO", "PWM", "ADC", "DAC", "I2C", "SPI", "UART",
                    
                    # IoT પ્રોટોકોલ્સ
                    "IoT પ્રોટોકોલ્સ", "કોમ્યુનિકેશન પ્રોટોકોલ્સ", "નેટવર્ક પ્રોટોકોલ્સ",
                    
                    # લિંક લેયર પ્રોટોકોલ્સ
                    "લિંક લેયર પ્રોટોકોલ્સ", "ઇથરનેટ", "WiFi", "બ્લુટૂથ", "ZigBee",
                    "Z-Wave", "6LoWPAN", "LoRa", "SigFox", "NB-IoT", "LTE-M",
                    
                    # નેટવર્ક/ઇન્ટરનેટ લેયર પ્રોટોકોલ્સ
                    "નેટવર્ક લેયર પ્રોટોકોલ્સ", "ઇન્ટરનેટ લેયર પ્રોટોકોલ્સ", "IPv4", "IPv6",
                    "ICMPv6", "RPL", "રાઉટિંગ પ્રોટોકોલ", "મેશ નેટવર્કિંગ",
                    
                    # ટ્રાન્સપોર્ટ લેયર પ્રોટોકોલ્સ
                    "ટ્રાન્સપોર્ટ લેયર પ્રોટોકોલ્સ", "TCP", "UDP", "SCTP", "QUIC",
                    "રિલાયેબલ ટ્રાન્સપોર્ટ", "અનરિલાયેબલ ટ્રાન્સપોર્ટ", "કનેક્શન ઓરિએન્ટેડ",
                    "કનેક્શનલેસ", "ફ્લો કંટ્રોલ", "કન્જેસ્ચન કંટ્રોલ",
                    
                    # એપ્લિકેશન લેયર પ્રોટોકોલ્સ
                    "એપ્લિકેશન લેયર પ્રોટોકોલ્સ", "HTTP", "HTTPS", "FTP", "CoAP",
                    "MQTT", "XMPP", "AMQP", "DDS", "WebSocket", "REST", "SOAP",
                    "કન્સ્ટ્રેઇન્ડ એપ્લિકેશન પ્રોટોકોલ", "મેસેજ ક્યુઇંગ", "પબ્લિશ સબ્સ્ક્રાઇબ",
                    
                    # IoT સિક્યુરિટી
                    "IoT સિક્યુરિટી", "સિક્યુરિટી ઇશ્યુઝ", "સિક્યુરિટી પડકારો", "વલ્નરેબિલિટીઝ",
                    "ઓથેન્ટિકેશન", "ઓથોરાઇઝેશન", "એન્ક્રિપ્શન", "ડેટા ઇન્ટેગ્રિટી",
                    "પ્રાઇવેસી", "સિક્યોર કોમ્યુનિકેશન", "કી મેનેજમેન્ટ", "સર્ટિફિકેટ મેનેજમેન્ટ",
                    "ડિવાઇસ સિક્યુરિટી", "નેટવર્ક સિક્યુરિટી", "એપ્લિકેશન સિક્યુરિટી", "ડેટા સિક્યુરિટી",
                    
                    # પ્રોટોટાઇપિંગ અને સોફ્ટવેર ડિઝાઇન
                    "પ્રોટોટાઇપિંગ", "સોફ્ટવેર ડિઝાઇન", "IoT એપ્લિકેશન્સ", "ડેવલપમેન્ટ એન્વાયરનમેન્ટ",
                    "IDE", "પ્રોગ્રામિંગ લેંગ્વેજિસ", "એમ્બેડેડ પ્રોગ્રામિંગ", "ક્લાઉડ ઇન્ટિગ્રેશન",
                    "API ડેવલપમેન્ટ", "વેબ સર્વિસિસ", "મોબાઇલ એપ ડેવલપમેન્ટ",
                    
                    # NodeMCU અને Raspberry Pi
                    "NodeMCU", "રાસ્પબેરી પાઇ", "બ્લોક ડાયાગ્રામ", "પિન કન્ફિગરેશન",
                    "ESP8266", "ESP32", "GPIO પિન્સ", "પાવર સપ્લાય", "WiFi મોડ્યુલ",
                    "બ્લુટૂથ મોડ્યુલ", "એનાલોગ પિન્સ", "ડિજિટલ પિન્સ", "PWM પિન્સ",
                    
                    # ક્લાઉડ ઇન્ટિગ્રેશન અને ડિવાઇસ કંટ્રોલ
                    "સેન્સર ડેટા", "ક્લાઉડ ટ્રાન્સમિશન", "ક્લાઉડ પ્લેટફોર્મ", "ડેટા અપલોડ",
                    "ડિવાઇસ કંટ્રોલ", "રિમોટ કંટ્રોલ", "મોબાઇલ એપ્લિકેશન", "વેબ એપ્લિકેશન",
                    "ક્લાઉડ સર્વિસિસ", "AWS IoT", "Google Cloud IoT", "Azure IoT",
                    "ThingSpeak", "Blynk", "Firebase", "રીઅલ ટાઇમ ડેટાબેઝ"
                ]
            },
            
            "Unit-V": {
                "english": [
                    # Broad Categories of IoT Applications
                    "IoT applications", "consumer IoT", "commercial IoT", "industrial IoT",
                    "infrastructure IoT", "military things", "IoMT", "categories",
                    "classification", "application domains", "use cases",
                    
                    # Consumer IoT
                    "smart home", "home automation", "smart appliances", "wearable devices",
                    "fitness trackers", "smart watches", "connected devices", "personal IoT",
                    
                    # Commercial IoT
                    "retail IoT", "office automation", "building management", "energy management",
                    "facility management", "asset tracking", "inventory management",
                    
                    # Industrial IoT (IIoT)
                    "industry 4.0", "smart manufacturing", "predictive maintenance",
                    "process automation", "quality control", "supply chain management",
                    "factory automation", "machine monitoring",
                    
                    # Infrastructure IoT
                    "smart city", "smart transportation", "traffic management", "smart grid",
                    "water management", "waste management", "public safety", "environmental monitoring",
                    
                    # Real World IoT Applications
                    "smart home automation", "home security", "lighting control", "HVAC control",
                    "smart thermostat", "smart locks", "smart cameras", "voice control",
                    "remote monitoring", "energy efficiency", "convenience", "comfort",
                    
                    # IoT Healthcare Monitoring
                    "healthcare monitoring", "patient monitoring", "remote patient monitoring",
                    "vital signs", "heart rate", "blood pressure", "blood glucose",
                    "telemedicine", "medical devices", "health sensors", "emergency alerts",
                    "chronic disease management", "elderly care", "medication reminders",
                    
                    # Smart Parking System
                    "smart parking", "parking management", "parking sensors", "occupancy detection",
                    "parking guidance", "payment systems", "mobile app", "real time availability",
                    "traffic reduction", "urban mobility", "space optimization",
                    
                    # Smart Street Light Control
                    "smart street lighting", "intelligent lighting", "lighting control", "motion sensors",
                    "light sensors", "dimming control", "energy savings", "maintenance alerts",
                    "remote monitoring", "adaptive lighting", "LED technology",
                    
                    # Voice Apps on IoT
                    "voice applications", "voice control", "voice assistants", "speech recognition",
                    "natural language processing", "voice commands", "smart speakers",
                    "voice user interface", "conversational AI", "voice automation"
                ],
                "gujarati": [
                    # IoT એપ્લિકેશન્સની વ્યાપક શ્રેણીઓ
                    "IoT એપ્લિકેશન્સ", "કન્ઝ્યુમર IoT", "કોમર્શિયલ IoT", "ઇન્ડસ્ટ્રિયલ IoT",
                    "ઇન્ફ્રાસ્ટ્રક્ચર IoT", "મિલિટરી થિંગ્સ", "IoMT", "કેટેગરીઝ",
                    "વર્ગીકરણ", "એપ્લિકેશન ડોમેઇન્સ", "ઉપયોગ કેસિસ",
                    
                    # કન્ઝ્યુમર IoT
                    "સ્માર્ટ હોમ", "હોમ ઓટોમેશન", "સ્માર્ટ એપ્લાયન્સિસ", "વેરેબલ ડિવાઇસિસ",
                    "ફિટનેસ ટ્રેકર્સ", "સ્માર્ટ વોચિસ", "કનેક્ટેડ ડિવાઇસિસ", "પર્સનલ IoT",
                    
                    # કોમર્શિયલ IoT
                    "રિટેલ IoT", "ઓફિસ ઓટોમેશન", "બિલ્ડિંગ મેનેજમેન્ટ", "એનર્જી મેનેજમેન્ટ",
                    "ફેસિલિટી મેનેજમેન્ટ", "એસેટ ટ્રેકિંગ", "ઇન્વેન્ટરી મેનેજમેન્ટ",
                    
                    # ઇન્ડસ્ટ્રિયલ IoT (IIoT)
                    "ઇન્ડસ્ટ્રી 4.0", "સ્માર્ટ મેન્યુફેક્ચરિંગ", "પ્રિડિક્ટિવ મેઇન્ટેનન્સ",
                    "પ્રોસેસ ઓટોમેશન", "ક્વોલિટી કંટ્રોલ", "સપ્લાય ચેઇન મેનેજમેન્ટ",
                    "ફેક્ટરી ઓટોમેશન", "મશીન મોનિટરિંગ",
                    
                    # ઇન્ફ્રાસ્ટ્રક્ચર IoT
                    "સ્માર્ટ સિટી", "સ્માર્ટ ટ્રાન્સપોર્ટેશન", "ટ્રાફિક મેનેજમેન્ટ", "સ્માર્ટ ગ્રિડ",
                    "વોટર મેનેજમેન્ટ", "વેસ્ટ મેનેજમેન્ટ", "પબ્લિક સેફ્ટી", "એન્વાયરનમેન્ટલ મોનિટરિંગ",
                    
                    # રીઅલ વર્લ્ડ IoT એપ્લિકેશન્સ
                    "સ્માર્ટ હોમ ઓટોમેશન", "હોમ સિક્યુરિટી", "લાઇટિંગ કંટ્રોલ", "HVAC કંટ્રોલ",
                    "સ્માર્ટ થર્મોસ્ટેટ", "સ્માર્ટ લોક્સ", "સ્માર્ટ કેમેરાઝ", "વોઇસ કંટ્રોલ",
                    "રિમોટ મોનિટરિંગ", "એનર્જી એફિશિયન્સી", "સુવિધા", "આરામ",
                    
                    # IoT હેલ્થકેર મોનિટરિંગ
                    "હેલ્થકેર મોનિટરિંગ", "પેશન્ટ મોનિટરિંગ", "રિમોટ પેશન્ટ મોનિટરિંગ",
                    "વાઇટલ સાઇન્સ", "હાર્ટ રેટ", "બ્લડ પ્રેશર", "બ્લડ ગ્લુકોઝ",
                    "ટેલિમેડિસિન", "મેડિકલ ડિવાઇસિસ", "હેલ્થ સેન્સર્સ", "ઇમર્જન્સી એલર્ટ્સ",
                    "ક્રોનિક ડિઝીઝ મેનેજમેન્ટ", "વૃદ્ધ સંભાળ", "દવા રિમાઇન્ડર્સ",
                    
                    # સ્માર્ટ પાર્કિંગ સિસ્ટમ
                    "સ્માર્ટ પાર્કિંગ", "પાર્કિંગ મેનેજમેન્ટ", "પાર્કિંગ સેન્સર્સ", "ઓક્યુપન્સી ડિટેક્શન",
                    "પાર્કિંગ ગાઇડન્સ", "પેમેન્ટ સિસ્ટમ્સ", "મોબાઇલ એપ", "રીઅલ ટાઇમ ઉપલબ્ધતા",
                    "ટ્રાફિક રિડક્શન", "અર્બન મોબિલિટી", "સ્પેસ ઓપ્ટિમાઇઝેશન",
                    
                    # સ્માર્ટ સ્ટ્રીટ લાઇટ કંટ્રોલ
                    "સ્માર્ટ સ્ટ્રીટ લાઇટિંગ", "ઇન્ટેલિજન્ટ લાઇટિંગ", "લાઇટિંગ કંટ્રોલ", "મોશન સેન્સર્સ",
                    "લાઇટ સેન્સર્સ", "ડિમિંગ કંટ્રોલ", "એનર્જી સેવિંગ્સ", "મેઇન્ટેનન્સ એલર્ટ્સ",
                    "રિમોટ મોનિટરિંગ", "એડેપ્ટિવ લાઇટિંગ", "LED ટેકનોલોજી",
                    
                    # IoT ડિવાઇસ પર વોઇસ એપ્સ
                    "વોઇસ એપ્લિકેશન્સ", "વોઇસ કંટ્રોલ", "વોઇસ એસિસ્ટન્ટ્સ", "સ્પીચ રેકગ્નિશન",
                    "નેચ્યુરલ લેંગ્વેજ પ્રોસેસિંગ", "વોઇસ કમાન્ડ્સ", "સ્માર્ટ સ્પીકર્સ",
                    "વોઇસ યુઝર ઇન્ટરફેસ", "કન્વર્સેશનલ AI", "વોઇસ ઓટોમેશન"
                ]
            }
        }
        
        # Enhanced unit-specific patterns for more accurate matching
        self.unit_specific_patterns = {
            "Unit-I": {
                "english": [
                    r"wireless sensor network|WSN",
                    r"sensor node\s+architecture",
                    r"hardware component|sensing subsystem|processor subsystem",
                    r"energy consumption|power consumption",
                    r"operating system|execution environment",
                    r"network architecture|optimization goals",
                    r"challenges|constraints|applications"
                ],
                "gujarati": [
                    r"વાયરલેસ સેન્સર નેટવર્ક|WSN",
                    r"સેન્સર નોડ\s+આર્કિટેક્ચર",
                    r"હાર્ડવેર ઘટકો|સેન્સિંગ સબસિસ્ટમ|પ્રોસેસર સબસિસ્ટમ",
                    r"એનર્જી વપરાશ|પાવર વપરાશ",
                    r"ઓપરેટિંગ સિસ્ટમ|એક્ઝિક્યુશન એન્વાયરનમેન્ટ",
                    r"નેટવર્ક આર્કિટેક્ચર|ઓપ્ટિમાઇઝેશન ગોલ્સ",
                    r"પડકારો|મર્યાદાઓ|એપ્લિકેશન્સ"
                ]
            },
            "Unit-II": {
                "english": [
                    r"physical layer|transceiver design",
                    r"MAC protocol|medium access control",
                    r"S-MAC|T-MAC|IEEE 802\.15\.4|duty cycle",
                    r"LEACH|SMACS|TRAMA|cluster",
                    r"address management|MAC address assignment",
                    r"routing protocol|energy efficient routing",
                    r"quality of service|QoS"
                ],
                "gujarati": [
                    r"ફિઝિકલ લેયર|ટ્રાન્સીવર ડિઝાઇન",
                    r"MAC પ્રોટોકોલ|મીડિયમ એક્સેસ કંટ્રોલ",
                    r"S-MAC|T-MAC|IEEE 802\.15\.4|ડ્યુટી સાયકલ",
                    r"LEACH|SMACS|TRAMA|ક્લસ્ટર",
                    r"એડ્રેસ મેનેજમેન્ટ|MAC એડ્રેસ અસાઇનમેન્ટ",
                    r"રાઉટિંગ પ્રોટોકોલ|એનર્જી એફિશિયન્ટ રાઉટિંગ",
                    r"ક્વોલિટી ઓફ સર્વિસ|QoS"
                ]
            },
            "Unit-III": {
                "english": [
                    r"internet of things|IoT|conceptual framework",
                    r"IoT architecture|architectural view",
                    r"IoT technology|enabling technologies",
                    r"M2M|machine to machine",
                    r"modified OSI|IoT OSI model",
                    r"IoT components|development boards",
                    r"IoT applications|smart home|smart city"
                ],
                "gujarati": [
                    r"ઇન્ટરનેટ ઓફ થિંગ્સ|IoT|કોન્સેપ્ચ્યુઅલ ફ્રેમવર્ક",
                    r"IoT આર્કિટેક્ચર|આર્કિટેક્ચરલ વ્યુ",
                    r"IoT ટેકનોલોજી|એનેબલિંગ ટેકનોલોજીઝ",
                    r"M2M|મશીન ટુ મશીન",
                    r"મોડિફાઇડ OSI|IoT OSI મોડેલ",
                    r"IoT ઘટકો|ડેવલપમેન્ટ બોર્ડ્સ",
                    r"IoT એપ્લિકેશન્સ|સ્માર્ટ હોમ|સ્માર્ટ સિટી"
                ]
            },
            "Unit-IV": {
                "english": [
                    r"sensors|actuators|temperature sensor|humidity sensor",
                    r"IoT components|implementation|microcontroller",
                    r"IoT protocols|communication protocols",
                    r"link layer|network layer|transport layer|application layer",
                    r"HTTP|HTTPS|CoAP|MQTT|XMPP",
                    r"IoT security|security issues|authentication",
                    r"NodeMCU|Raspberry Pi|ESP8266|ESP32",
                    r"cloud|sensor data|device control"
                ],
                "gujarati": [
                    r"સેન્સર્સ|એક્ચ્યુએટર્સ|ટેમ્પરેચર સેન્સર|હ્યુમિડિટી સેન્સર",
                    r"IoT ઘટકો|અમલીકરણ|માઇક્રોકંટ્રોલર",
                    r"IoT પ્રોટોકોલ્સ|કોમ્યુનિકેશન પ્રોટોકોલ્સ",
                    r"લિંક લેયર|નેટવર્ક લેયર|ટ્રાન્સપોર્ટ લેયર|એપ્લિકેશન લેયર",
                    r"HTTP|HTTPS|CoAP|MQTT|XMPP",
                    r"IoT સિક્યુરિટી|સિક્યુરિટી ઇશ્યુઝ|ઓથેન્ટિકેશન",
                    r"NodeMCU|રાસ્પબેરી પાઇ|ESP8266|ESP32",
                    r"ક્લાઉડ|સેન્સર ડેટા|ડિવાઇસ કંટ્રોલ"
                ]
            },
            "Unit-V": {
                "english": [
                    r"IoT applications|consumer IoT|commercial IoT|industrial IoT",
                    r"smart home|home automation|smart appliances",
                    r"healthcare monitoring|patient monitoring|vital signs",
                    r"smart parking|parking management|parking sensors",
                    r"smart street lighting|lighting control|motion sensors",
                    r"voice applications|voice control|voice assistants"
                ],
                "gujarati": [
                    r"IoT એપ્લિકેશન્સ|કન્ઝ્યુમર IoT|કોમર્શિયલ IoT|ઇન્ડસ્ટ્રિયલ IoT",
                    r"સ્માર્ટ હોમ|હોમ ઓટોમેશન|સ્માર્ટ એપ્લાયન્સિસ",
                    r"હેલ્થકેર મોનિટરિંગ|પેશન્ટ મોનિટરિંગ|વાઇટલ સાઇન્સ",
                    r"સ્માર્ટ પાર્કિંગ|પાર્કિંગ મેનેજમેન્ટ|પાર્કિંગ સેન્સર્સ",
                    r"સ્માર્ટ સ્ટ્રીટ લાઇટિંગ|લાઇટિંગ કંટ્રોલ|મોશન સેન્સર્સ",
                    r"વોઇસ એપ્લિકેશન્સ|વોઇસ કંટ્રોલ|વોઇસ એસિસ્ટન્ટ્સ"
                ]
            }
        }
        
        # Advanced scoring weights for enhanced accuracy
        self.scoring_weights = {
            'direct_match': 5.0,
            'partial_match': 2.0,
            'context_match': 3.0,
            'technical_term_bonus': 2.0,
            'length_bonus': 1.0,
            'gujarati_specific_bonus': 1.5,
            'pattern_match_bonus': 3.0
        }
    
    def load_syllabus(self):
        """Load syllabus data from JSON file"""
        syllabus_file = self.base_path / "4353201.json"
        if syllabus_file.exists():
            with open(syllabus_file, 'r', encoding='utf-8') as f:
                self.syllabus_data = json.load(f)
            print(f"✅ Loaded syllabus data: {self.syllabus_data.get('courseInfo', {}).get('courseTitle', 'Unknown')}")
        else:
            print(f"⚠️ Syllabus file not found: {syllabus_file}")
    
    def extract_questions_from_file(self, file_path: Path) -> List[Question]:
        """Extract questions from a solution file with enhanced parsing"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine language and extract metadata
            language = 'gujarati' if '.gu.' in file_path.name else 'english'
            
            # Extract year and season from filename
            year_match = re.search(r'(20\d{2})', file_path.name)
            year = year_match.group(1) if year_match else "2024"
            
            season_match = re.search(r'(summer|winter)', file_path.name.lower())
            season = season_match.group(1) if season_match else "unknown"
            
            # Enhanced question patterns for both languages
            question_patterns = [
                r'## (?:Question |પ્રશ્ન )(\d+)\(([^)]+)\)\s*\[(\d+)\s*(?:marks?|ગુણ)\]\s*\n\n\*\*([^*]+)\*\*',
                r'## (?:Question |પ્રશ્ન )(\d+)\(([^)]+)\)\s*\[(\d+)\s*(?:marks?|ગુણ)\]\s*\n\*\*([^*]+)\*\*',
                r'## (?:Question |પ્રશ્ન )(\d+)\s*\[(\d+)\s*(?:marks?|ગુણ)\]\s*\n\n\*\*([^*]+)\*\*',
                r'## (?:Question |પ્રશ્ન )(\d+)\s*\[(\d+)\s*(?:marks?|ગુણ)\]\s*\n\*\*([^*]+)\*\*'
            ]
            
            questions = []
            
            for pattern in question_patterns:
                matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL)
                
                for match in matches:
                    try:
                        groups = match.groups()
                        
                        if len(groups) == 4:
                            question_num, marks, text = groups[0], groups[2], groups[3]
                        elif len(groups) == 3:
                            question_num, marks, text = groups[0], groups[1], groups[2]
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
        
        # Enhanced pattern-based matching first (highest priority)
        unit_patterns = self.unit_specific_patterns.get(unit, {}).get(question.language, [])
        for pattern in unit_patterns:
            if re.search(pattern, question.text, re.IGNORECASE):
                score += self.scoring_weights['direct_match'] * 2  # Double score for pattern matches
                if question.language == 'gujarati':
                    score += self.scoring_weights['gujarati_specific_bonus']
        
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
        
        # Context matching based on common WSN and IoT terms with more specific mappings
        context_indicators = {
            "Unit-I": ["wireless sensor network", "sensor node", "hardware components", "energy consumption", 
                      "operating system", "network architecture", "optimization goals", "challenges", "applications",
                      "single node", "sensing subsystem", "processor subsystem", "communication subsystem"],
            "Unit-II": ["physical layer", "MAC protocol", "S-MAC", "LEACH", "routing protocol", "energy efficient",
                       "address management", "quality of service", "transceiver design", "duty cycle", "clustering"],
            "Unit-III": ["internet of things", "IoT architecture", "M2M communication", "IoT technology", 
                        "development boards", "conceptual framework", "enabling technologies", "IoT components"],
            "Unit-IV": ["sensors", "actuators", "IoT protocols", "NodeMCU", "Raspberry Pi", "cloud", "security",
                       "HTTP", "MQTT", "CoAP", "device control", "implementation", "prototyping"],
            "Unit-V": ["IoT applications", "smart home", "healthcare monitoring", "smart parking", "smart lighting",
                      "voice applications", "consumer IoT", "industrial IoT", "commercial IoT"]
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
            'accuracy_percentage': 0.0
        }
        
        if stats['total_questions'] > 0:
            stats['accuracy_percentage'] = (stats['mapped_questions'] / stats['total_questions']) * 100
        
        return stats
    
    def generate_question_bank_json(self) -> Dict:
        """Generate the final question bank JSON"""
        question_bank = {
            "metadata": {
                "subject_code": "4353201",
                "subject_name": "Wireless Sensor Networks and IoT",
                "generated_date": "2024-12-19",
                "total_questions": len(self.questions),
                "generator_version": "2.0",
                "mapping_accuracy": f"{self.validate_mapping_accuracy()['accuracy_percentage']:.2f}%"
            },
            "statistics": self.validate_mapping_accuracy(),
            "questions": []
        }
        
        # Group questions by unit for better organization
        questions_by_unit = defaultdict(list)
        for question in self.questions:
            questions_by_unit[question.unit].append(question)
        
        # Sort units
        unit_order = ["Unit-I", "Unit-II", "Unit-III", "Unit-IV", "Unit-V", "Unknown"]
        
        for unit in unit_order:
            if unit in questions_by_unit:
                unit_questions = questions_by_unit[unit]
                # Sort by confidence score (highest first)
                unit_questions.sort(key=lambda q: q.confidence, reverse=True)
                
                for question in unit_questions:
                    question_dict = asdict(question)
                    question_dict['topics'] = question_dict.get('topics', [])
                    question_bank["questions"].append(question_dict)
        
        return question_bank
    
    def save_question_bank(self, output_file: str = None):
        """Save question bank to JSON file"""
        if output_file is None:
            output_file = str(self.base_path / "4353201-question-bank-final.json")
        
        question_bank = self.generate_question_bank_json()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(question_bank, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Question bank saved to: {output_file}")
        return question_bank
    
    def generate_mapping_report(self) -> str:
        """Generate detailed mapping accuracy report"""
        stats = self.validate_mapping_accuracy()
        
        report = f"""
# WSN Question Bank Mapping Report

## Overall Statistics
- **Total Questions Extracted**: {stats['total_questions']}
- **Successfully Mapped**: {stats['mapped_questions']} ({stats['accuracy_percentage']:.2f}%)
- **High Confidence Mapping** (>70%): {stats['high_confidence']}
- **Medium Confidence Mapping** (40-70%): {stats['medium_confidence']}
- **Low Confidence Mapping** (≤40%): {stats['low_confidence']}

## Language Distribution
"""
        
        for language, count in stats['by_language'].items():
            percentage = (count / stats['total_questions']) * 100
            report += f"- **{language.title()}**: {count} questions ({percentage:.1f}%)\n"
        
        report += "\n## Unit Distribution\n"
        
        for unit, count in stats['by_unit'].items():
            percentage = (count / stats['total_questions']) * 100
            report += f"- **{unit}**: {count} questions ({percentage:.1f}%)\n"
        
        # Add unmapped questions if any
        unmapped_questions = [q for q in self.questions if q.unit == "Unknown"]
        if unmapped_questions:
            report += f"\n## Unmapped Questions ({len(unmapped_questions)})\n"
            for i, question in enumerate(unmapped_questions[:5], 1):  # Show first 5
                report += f"{i}. [{question.source_file}] {question.text[:100]}...\n"
            
            if len(unmapped_questions) > 5:
                report += f"... and {len(unmapped_questions) - 5} more\n"
        
        report += f"\n## Mapping Accuracy: {stats['accuracy_percentage']:.2f}%\n"
        
        if stats['accuracy_percentage'] >= 95:
            report += "🎯 **EXCELLENT** - Target accuracy achieved!\n"
        elif stats['accuracy_percentage'] >= 90:
            report += "✅ **VERY GOOD** - High accuracy mapping\n"
        elif stats['accuracy_percentage'] >= 80:
            report += "👍 **GOOD** - Acceptable accuracy\n"
        else:
            report += "⚠️ **NEEDS IMPROVEMENT** - Consider enhancing keyword mappings\n"
        
        return report

def main():
    """Main function to run the WSN question bank generator"""
    base_path = "/Users/milav/Code/studio/content/resources/study-materials/32-ict/sem-5/4353201-wsn"
    
    print("🚀 Starting WSN Question Bank Generator...")
    print("=" * 60)
    
    generator = EnhancedWSNQuestionBankGenerator(base_path)
    
    # Load syllabus
    generator.load_syllabus()
    
    # Process all questions
    print("\n📝 Processing solution files...")
    questions = generator.process_all_questions()
    
    # Generate and save question bank
    print("\n💾 Generating question bank...")
    question_bank = generator.save_question_bank()
    
    # Generate report
    print("\n📊 Generating mapping report...")
    report = generator.generate_mapping_report()
    print(report)
    
    # Save report
    report_file = f"{base_path}/WSN-Question-Bank-Mapping-Report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📋 Detailed report saved to: {report_file}")
    print("=" * 60)
    print("✅ WSN Question Bank Generation Complete!")

if __name__ == "__main__":
    main()