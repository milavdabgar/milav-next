#!/usr/bin/env python3
"""
Enhanced Question Bank Generator for Computer Networking (4343202)
Comprehensive bilingual question extraction and mapping system for Computer Networking
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

class EnhancedComputerNetworkingQuestionBankGenerator:
    """Enhanced question bank generator for Computer Networking"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.syllabus_data = {}
        self.questions = []
        
        # Enhanced bilingual keyword mappings for Computer Networking
        self.unit_keywords = {
            "Unit-I": {
                "english": [
                    # Computer network basics
                    "computer network", "computer networking", "network", "data communication", 
                    "communication", "advantages", "applications", "need",
                    
                    # Physical topologies
                    "topology", "topologies", "physical topology", "star", "ring", "bus", 
                    "mesh", "tree", "hybrid", "point to point", "network topology",
                    
                    # Internet standards and protocols
                    "internet standards", "protocol", "interface", "standards", "protocol stack",
                    
                    # Network classification
                    "network classification", "classification", "transmission technologies",
                    "point-to-point", "broadcast", "PAN", "LAN", "WAN", "MAN", "VPN", 
                    "internet", "peer to peer", "client server", "p2p", "architecture",
                    
                    # OSI and TCP/IP models
                    "OSI model", "OSI reference model", "OSI", "TCP/IP model", "TCP/IP", 
                    "layered model", "layer", "layers", "protocol suite", "comparison",
                    "seven layer", "four layer", "application layer", "transport layer",
                    "network layer", "data link layer", "physical layer", "session layer",
                    "presentation layer"
                ],
                "gujarati": [
                    # કમ્પ્યુટર નેટવર્ક મૂળભૂતો
                    "કમ્પ્યુટર નેટવર્ક", "કમ્પ્યુટર નેટવર્કિંગ", "નેટવર્ક", "ડેટા કોમ્યુનિકેશન",
                    "કોમ્યુનિકેશન", "ફાયદાઓ", "એપ્લિકેશન્સ", "જરૂર", "જરૂરિયાત",
                    
                    # ભૌતિક ટોપોલોજી
                    "ટોપોલોજી", "ભૌતિક ટોપોલોજી", "સ્ટાર", "રિંગ", "બસ", "મેશ", 
                    "ટ્રી", "હાઇબ્રિડ", "પોઇન્ટ ટુ પોઇન્ટ", "નેટવર્ક ટોપોલોજી",
                    
                    # ઇન્ટરનેટ સ્ટાન્ડર્ડ્સ અને પ્રોટોકોલ્સ
                    "ઇન્ટરનેટ સ્ટાન્ડર્ડ્સ", "પ્રોટોકોલ", "ઇન્ટરફેસ", "સ્ટાન્ડર્ડ્સ", "પ્રોટોકોલ સ્ટેક",
                    
                    # નેટવર્ક વર્ગીકરણ
                    "નેટવર્ક વર્ગીકરણ", "વર્ગીકરણ", "ટ્રાન્સમિશન ટેકનોલોજીઝ",
                    "પોઇન્ટ-ટુ-પોઇન્ટ", "બ્રોડકાસ્ટ", "PAN", "LAN", "WAN", "MAN", "VPN",
                    "ઇન્ટરનેટ", "પીઅર ટુ પીઅર", "ક્લાઇન્ટ સર્વર", "p2p", "આર્કિટેક્ચર",
                    
                    # OSI અને TCP/IP મોડેલ્સ
                    "OSI મોડેલ", "OSI રેફરન્સ મોડેલ", "OSI", "TCP/IP મોડેલ", "TCP/IP",
                    "લેયર્ડ મોડેલ", "લેયર", "સ્તર", "સ્તરો", "પ્રોટોકોલ સ્યુટ", "સરખામણી",
                    "સાત સ્તર", "ચાર સ્તર", "એપ્લિકેશન લેયર", "ટ્રાન્સપોર્ટ લેયર",
                    "નેટવર્ક લેયર", "ડેટા લિંક લેયર", "ફિઝિકલ લેયર", "સેશન લેયર",
                    "પ્રેઝન્ટેશન લેયર"
                ]
            },
            
            "Unit-II": {
                "english": [
                    # Network devices and transmission media
                    "transmission media", "guided", "unguided", "twisted pair", "coaxial cable",
                    "fiber optic", "optical fiber", "cable", "wireless", "medium", "media",
                    
                    # Network devices
                    "repeater", "hub", "bridge", "switch", "router", "gateway", "access point",
                    "network adapter", "wireless access point", "b-router", "brouter",
                    "layer 2", "layer 3", "network device", "switching", "routing",
                    
                    # Device functions and comparison
                    "difference", "compare", "differentiate", "functions", "role",
                    "OSI layer", "data handling", "addressing", "MAC address", "IP address",
                    
                    # Firewall and security
                    "firewall", "network security", "security", "trusted system", "kerberos",
                    "principle", "limitation", "concept",
                    
                    # Network management
                    "network management", "management system", "OS", "CLI", "administrative",
                    "interface", "SNMP", "network monitoring",
                    
                    # Ethernet technologies
                    "ethernet", "fast ethernet", "gigabit ethernet", "10base-t", "100base-tx",
                    "1000base-t", "speed", "bandwidth", "cable type", "standard",
                    
                    # Wireless and advanced technologies
                    "wireless LAN", "WLAN", "Wi-Fi", "FDDI", "CDDI", "software defined network",
                    "SDN", "802.11", "access point", "wireless technology"
                ],
                "gujarati": [
                    # નેટવર્ક ડિવાઇસ અને ટ્રાન્સમિશન મીડિયા
                    "ટ્રાન્સમિશન મીડિયા", "ગાઇડેડ", "અનગાઇડેડ", "ટ્વિસ્ટેડ પેર", "કોએક્સિયલ કેબલ",
                    "ફાઇબર ઓપ્ટિક", "ઓપ્ટિકલ ફાઇબર", "કેબલ", "વાયરલેસ", "માધ્યમ", "મીડિયા",
                    
                    # નેટવર્ક ડિવાઇસિસ
                    "રીપીટર", "હબ", "બ્રિજ", "સ્વિચ", "રાઉટર", "ગેટવે", "એક્સેસ પોઇન્ટ",
                    "નેટવર્ક એડેપ્ટર", "વાયરલેસ એક્સેસ પોઇન્ટ", "બી-રાઉટર", "બ્રાઉટર",
                    "લેયર 2", "લેયર 3", "નેટવર્ક ડિવાઇસ", "સ્વિચિંગ", "રાઉટિંગ",
                    
                    # ડિવાઇસ ફંક્શન અને સરખામણી
                    "તફાવત", "સરખામણી", "તફાવતો", "કાર્યો", "ભૂમિકા", "કામગીરી",
                    "OSI લેયર", "ડેટા હેન્ડલિંગ", "એડ્રેસિંગ", "MAC એડ્રેસ", "IP એડ્રેસ",
                    
                    # ફાયરવોલ અને સિક્યુરિટી
                    "ફાયરવોલ", "નેટવર્ક સિક્યુરિટી", "સિક્યુરિટી", "ટ્રસ્ટેડ સિસ્ટમ", "કર્બેરોસ",
                    "સિદ્ધાંત", "મર્યાદા", "કોન્સેપ્ટ", "ખ્યાલ",
                    
                    # નેટવર્ક મેનેજમેન્ટ
                    "નેટવર્ક મેનેજમેન્ટ", "મેનેજમેન્ટ સિસ્ટમ", "OS", "CLI", "એડમિનિસ્ટ્રેટિવ",
                    "ઇન્ટરફેસ", "SNMP", "નેટવર્ક મોનિટરિંગ",
                    
                    # ઇથરનેટ ટેકનોલોજીઝ
                    "ઇથરનેટ", "ફાસ્ટ ઇથરનેટ", "ગીગાબિટ ઇથરનેટ", "10base-t", "100base-tx",
                    "1000base-t", "સ્પીડ", "બેન્ડવિડ્થ", "કેબલ ટાઇપ", "સ્ટાન્ડર્ડ",
                    
                    # વાયરલેસ અને અદ્યતન ટેકનોલોજીઝ
                    "વાયરલેસ LAN", "WLAN", "Wi-Fi", "FDDI", "CDDI", "સોફ્ટવેર ડિફાઇન્ડ નેટવર્ક",
                    "SDN", "802.11", "એક્સેસ પોઇન્ટ", "વાયરલેસ ટેકનોલોજી"
                ]
            },
            
            "Unit-III": {
                "english": [
                    # Physical layer and transmission media
                    "physical layer", "transmission media", "twisted pair", "coaxial cable",
                    "fiber optic cable", "constructional details", "characteristics",
                    
                    # Wireless and ISM band
                    "wireless medium", "ISM band", "frequency", "radio", "microwave",
                    "satellite", "infrared", "frequency range",
                    
                    # DSL and cable modem
                    "DSL technology", "DSL", "xDSL", "ADSL", "SDSL", "VDSL", "advantages",
                    "limitations", "cable modem", "broadband", "last mile",
                    
                    # Data link layer
                    "data link layer", "sublayers", "functions", "error control", "flow control",
                    "error detection", "error correction", "automatic repeat request", "ARQ",
                    
                    # Network layer and packet switching
                    "network layer", "packet switching", "circuit switching", "virtual circuits",
                    "datagram", "connectionless", "connection oriented",
                    
                    # Routing algorithms
                    "routing", "routing algorithms", "static routing", "dynamic routing",
                    "distance vector", "link state", "path vector", "routing table",
                    
                    # IP addressing
                    "IP addressing", "IPv4", "IPv6", "classful", "classless", "subnetting",
                    "supernetting", "address classes", "class A", "class B", "class C",
                    
                    # CIDR and NAT
                    "CIDR", "classless inter-domain routing", "NAT", "network address translation",
                    "static NAT", "dynamic NAT", "PAT", "port address translation",
                    
                    # IP protocols
                    "ICMP", "ARP", "RARP", "DHCP", "BOOTP", "IP protocols", "internet protocols",
                    "address resolution", "reverse address resolution", "dynamic host configuration"
                ],
                "gujarati": [
                    # ફિઝિકલ લેયર અને ટ્રાન્સમિશન મીડિયા
                    "ફિઝિકલ લેયર", "ટ્રાન્સમિશન મીડિયા", "ટ્વિસ્ટેડ પેર", "કોએક્સિયલ કેબલ",
                    "ફાઇબર ઓપ્ટિક કેબલ", "બાંધકામ વિગતો", "લાક્ષણિકતાઓ",
                    
                    # વાયરલેસ અને ISM બેન્ડ
                    "વાયરલેસ માધ્યમ", "ISM બેન્ડ", "ફ્રીક્વન્સી", "રેડિયો", "માઇક્રોવેવ",
                    "સેટેલાઇટ", "ઇન્ફ્રારેડ", "ફ્રીક્વન્સી રેન્જ",
                    
                    # DSL અને કેબલ મોડેમ
                    "DSL ટેકનોલોજી", "DSL", "xDSL", "ADSL", "SDSL", "VDSL", "ફાયદાઓ",
                    "મર્યાદાઓ", "કેબલ મોડેમ", "બ્રોડબેન્ડ", "લાસ્ટ માઇલ",
                    
                    # ડેટા લિંક લેયર
                    "ડેટા લિંક લેયર", "સબલેયર્સ", "કાર્યો", "એરર કંટ્રોલ", "ફ્લો કંટ્રોલ",
                    "એરર ડિટેક્શન", "એરર કરેક્શન", "ઓટોમેટિક રીપીટ રિક્વેસ્ટ", "ARQ",
                    
                    # નેટવર્ક લેયર અને પેકેટ સ્વિચિંગ
                    "નેટવર્ક લેયર", "પેકેટ સ્વિચિંગ", "સર્કિટ સ્વિચિંગ", "વર્ચ્યુઅલ સર્કિટ્સ",
                    "ડેટાગ્રામ", "કનેક્શનલેસ", "કનેક્શન ઓરિએન્ટેડ",
                    
                    # રાઉટિંગ અલ્ગોરિધમ્સ
                    "રાઉટિંગ", "રાઉટિંગ અલ્ગોરિધમ્સ", "સ્ટેટિક રાઉટિંગ", "ડાયનેમિક રાઉટિંગ",
                    "ડિસ્ટન્સ વેક્ટર", "લિંક સ્ટેટ", "પાથ વેક્ટર", "રાઉટિંગ ટેબલ",
                    
                    # IP એડ્રેસિંગ
                    "IP એડ્રેસિંગ", "IPv4", "IPv6", "ક્લાસફુલ", "ક્લાસલેસ", "સબનેટિંગ",
                    "સુપરનેટિંગ", "એડ્રેસ ક્લાસેસ", "ક્લાસ A", "ક્લાસ B", "ક્લાસ C",
                    
                    # CIDR અને NAT
                    "CIDR", "ક્લાસલેસ ઇન્ટર-ડોમેઇન રાઉટિંગ", "NAT", "નેટવર્ક એડ્રેસ ટ્રાન્સલેશન",
                    "સ્ટેટિક NAT", "ડાયનેમિક NAT", "PAT", "પોર્ટ એડ્રેસ ટ્રાન્સલેશન",
                    
                    # IP પ્રોટોકોલ્સ
                    "ICMP", "ARP", "RARP", "DHCP", "BOOTP", "IP પ્રોટોકોલ્સ", "ઇન્ટરનેટ પ્રોટોકોલ્સ",
                    "એડ્રેસ રિઝોલ્યુશન", "રિવર્સ એડ્રેસ રિઝોલ્યુશન", "ડાયનેમિક હોસ્ટ કોન્ફિગરેશન"
                ]
            },
            
            "Unit-IV": {
                "english": [
                    # Transport layer protocols
                    "transport layer", "TCP", "UDP", "transmission control protocol",
                    "user datagram protocol", "connection oriented", "connectionless",
                    "reliable", "unreliable", "port", "socket", "segment",
                    
                    # Transport layer features
                    "flow control", "error control", "congestion control", "windowing",
                    "acknowledgment", "retransmission", "timeout", "sequence number",
                    
                    # Application layer protocols
                    "application layer", "DNS", "domain name system", "name resolution",
                    "DNS server", "DNS hierarchy", "DNS query", "domain name",
                    
                    # Web and HTTP
                    "HTTP", "hypertext transfer protocol", "web", "WWW", "world wide web",
                    "web browser", "web server", "HTML", "URL", "cookies", "session",
                    
                    # Email protocols
                    "email", "electronic mail", "SMTP", "POP3", "IMAP", "mail server",
                    "user agent", "message format", "mail protocols", "email system",
                    
                    # FTP and file transfer
                    "FTP", "file transfer protocol", "active FTP", "passive FTP",
                    "data connection", "control connection", "file transfer",
                    
                    # Remote access and other protocols
                    "remote login", "telnet", "SSH", "secure shell", "remote access",
                    "terminal emulation", "client server", "port number",
                    
                    # Voice and video
                    "voice over IP", "VoIP", "video over IP", "multimedia", "streaming",
                    "real-time", "QoS", "quality of service"
                ],
                "gujarati": [
                    # ટ્રાન્સપોર્ટ લેયર પ્રોટોકોલ્સ
                    "ટ્રાન્સપોર્ટ લેયર", "TCP", "UDP", "ટ્રાન્સમિશન કંટ્રોલ પ્રોટોકોલ",
                    "યુઝર ડેટાગ્રામ પ્રોટોકોલ", "કનેક્શન ઓરિએન્ટેડ", "કનેક્શનલેસ",
                    "વિશ્વસનીય", "અવિશ્વસનીય", "પોર્ટ", "સોકેટ", "સેગ્મેન્ટ",
                    
                    # ટ્રાન્સપોર્ટ લેયર ફીચર્સ
                    "ફ્લો કંટ્રોલ", "એરર કંટ્રોલ", "કન્જેશન કંટ્રોલ", "વિન્ડોઇંગ",
                    "એકનોલેજમેન્ટ", "રીટ્રાન્સમિશન", "ટાઇમઆઉટ", "સિક્વન્સ નંબર",
                    
                    # એપ્લિકેશન લેયર પ્રોટોકોલ્સ
                    "એપ્લિકેશન લેયર", "DNS", "ડોમેઇન નેમ સિસ્ટમ", "નેમ રિઝોલ્યુશન",
                    "DNS સર્વર", "DNS હાયરાર્કી", "DNS ક્વેરી", "ડોમેઇન નેમ",
                    
                    # વેબ અને HTTP
                    "HTTP", "હાઇપરટેક્સ્ટ ટ્રાન્સફર પ્રોટોકોલ", "વેબ", "WWW", "વર્લ્ડ વાઇડ વેબ",
                    "વેબ બ્રાઉઝર", "વેબ સર્વર", "HTML", "URL", "કુકીઝ", "સેશન",
                    
                    # ઇમેઇલ પ્રોટોકોલ્સ
                    "ઇમેઇલ", "ઇલેક્ટ્રોનિક મેઇલ", "SMTP", "POP3", "IMAP", "મેઇલ સર્વર",
                    "યુઝર એજન્ટ", "મેસેજ ફોર્મેટ", "મેઇલ પ્રોટોકોલ્સ", "ઇમેઇલ સિસ્ટમ",
                    
                    # FTP અને ફાઇલ ટ્રાન્સફર
                    "FTP", "ફાઇલ ટ્રાન્સફર પ્રોટોકોલ", "એક્ટિવ FTP", "પેસિવ FTP",
                    "ડેટા કનેક્શન", "કંટ્રોલ કનેક્શન", "ફાઇલ ટ્રાન્સફર",
                    
                    # રિમોટ એક્સેસ અને અન્ય પ્રોટોકોલ્સ
                    "રિમોટ લોગિન", "ટેલનેટ", "SSH", "સિક્યોર શેલ", "રિમોટ એક્સેસ",
                    "ટર્મિનલ ઇમ્યુલેશન", "ક્લાઇન્ટ સર્વર", "પોર્ટ નંબર",
                    
                    # વૉઇસ અને વિડીયો
                    "વૉઇસ ઓવર IP", "VoIP", "વિડીયો ઓવર IP", "મલ્ટીમીડીયા", "સ્ટ્રીમિંગ",
                    "રિયલ-ટાઇમ", "QoS", "ક્વોલિટી ઓફ સર્વિસ"
                ]
            },
            
            "Unit-V": {
                "english": [
                    # Network security introduction
                    "network security", "security", "cryptography", "encryption", "decryption",
                    "security threats", "vulnerabilities", "attacks", "malware", "virus",
                    
                    # Security topologies
                    "security topology", "security zones", "DMZ", "demilitarized zone",
                    "intranet", "internet", "VLAN", "virtual LAN", "security implication",
                    "tunneling", "VPN", "virtual private network",
                    
                    # Encryption and cryptographic algorithms
                    "symmetric encryption", "asymmetric encryption", "public key", "private key",
                    "digital signature", "certificate", "PKI", "public key infrastructure",
                    "hash function", "digital certificate",
                    
                    # IP security
                    "IPSec", "IP security", "architecture", "configuration", "AH", "ESP",
                    "authentication header", "encapsulating security payload", "SA",
                    "security association", "tunnel mode", "transport mode",
                    
                    # Email security
                    "email security", "email security standards", "PEM", "PGP", "S/MIME",
                    "pretty good privacy", "secure MIME", "digital signature", "spam",
                    "phishing", "email encryption",
                    
                    # Web security and SSL
                    "web security", "SSL", "TLS", "secure socket layer", "transport layer security",
                    "HTTPS", "secure HTTP", "certificate authority", "CA", "digital certificate",
                    
                    # Security protocols and standards
                    "SSH", "secure shell", "Kerberos", "authentication", "authorization",
                    "firewall", "intrusion detection", "access control", "security policy",
                    
                    # Legal and ethical aspects
                    "information security standards", "ISO", "IT act", "copyright act",
                    "cyber laws", "IT act 2000", "amendments", "privacy", "data protection",
                    "ethical considerations", "social issues", "hacking", "precautions"
                ],
                "gujarati": [
                    # નેટવર્ક સિક્યુરિટી પરિચય
                    "નેટવર્ક સિક્યુરિટી", "સિક્યુરિટી", "ક્રિપ્ટોગ્રાફી", "એન્ક્રિપ્શન", "ડિક્રિપ્શન",
                    "સિક્યુરિટી ધમકીઓ", "નબળાઇઓ", "આક્રમણો", "મેલવેર", "વાયરસ",
                    
                    # સિક્યુરિટી ટોપોલોજીઝ
                    "સિક્યુરિટી ટોપોલોજી", "સિક્યુરિટી ઝોન્સ", "DMZ", "ડેમિલિટરાઇઝ્ડ ઝોન",
                    "ઇન્ટ્રાનેટ", "ઇન્ટરનેટ", "VLAN", "વર્ચ્યુઅલ LAN", "સિક્યુરિટી અસર",
                    "ટનલિંગ", "VPN", "વર્ચ્યુઅલ પ્રાઇવેટ નેટવર્ક",
                    
                    # એન્ક્રિપ્શન અને ક્રિપ્ટોગ્રાફિક અલ્ગોરિધમ્સ
                    "સિમેટ્રિક એન્ક્રિપ્શન", "એસિમેટ્રિક એન્ક્રિપ્શન", "પબ્લિક કી", "પ્રાઇવેટ કી",
                    "ડિજિટલ સિગ્નેચર", "સર્ટિફિકેટ", "PKI", "પબ્લિક કી ઇન્ફ્રાસ્ટ્રક્ચર",
                    "હેશ ફંક્શન", "ડિજિટલ સર્ટિફિકેટ",
                    
                    # IP સિક્યુરિટી
                    "IPSec", "IP સિક્યુરિટી", "આર્કિટેક્ચર", "કોન્ફિગરેશન", "AH", "ESP",
                    "ઓથેન્ટિકેશન હેડર", "એન્કેપ્સ્યુલેટિંગ સિક્યુરિટી પેલોડ", "SA",
                    "સિક્યુરિટી એસોસિએશન", "ટનલ મોડ", "ટ્રાન્સપોર્ટ મોડ",
                    
                    # ઇમેઇલ સિક્યુરિટી
                    "ઇમેઇલ સિક્યુરિટી", "ઇમેઇલ સિક્યુરિટી સ્ટાન્ડર્ડ્સ", "PEM", "PGP", "S/MIME",
                    "પ્રીટી ગુડ પ્રાઇવસી", "સિક્યોર MIME", "ડિજિટલ સિગ્નેચર", "સ્પામ",
                    "ફિશિંગ", "ઇમેઇલ એન્ક્રિપ્શન",
                    
                    # વેબ સિક્યુરિટી અને SSL
                    "વેબ સિક્યુરિટી", "SSL", "TLS", "સિક્યોર સોકેટ લેયર", "ટ્રાન્સપોર્ટ લેયર સિક્યુરિટી",
                    "HTTPS", "સિક્યોર HTTP", "સર્ટિફિકેટ ઓથોરિટી", "CA", "ડિજિટલ સર્ટિફિકેટ",
                    
                    # સિક્યુરિટી પ્રોટોકોલ્સ અને સ્ટાન્ડર્ડ્સ
                    "SSH", "સિક્યોર શેલ", "કર્બેરોસ", "ઓથેન્ટિકેશન", "ઓથરાઇઝેશન",
                    "ફાયરવોલ", "ઇન્ટ્રુઝન ડિટેક્શન", "એક્સેસ કંટ્રોલ", "સિક્યુરિટી પોલિસી",
                    
                    # કાનૂની અને નૈતિક પાસાઓ
                    "ઇન્ફર્મેશન સિક્યુરિટી સ્ટાન્ડર્ડ્સ", "ISO", "IT એક્ટ", "કોપીરાઇટ એક્ટ",
                    "સાયબર કાયદાઓ", "IT એક્ટ 2000", "સુધારાઓ", "ગોપનીયતા", "ડેટા પ્રોટેક્શન",
                    "નૈતિક વિચારણાઓ", "સામાજિક મુદ્દાઓ", "હેકિંગ", "સાવચેતીઓ"
                ]
            }
        }
        
        # Enhanced scoring weights for better accuracy with Gujarati-specific adjustments
        self.scoring_weights = {
            'direct_match': 15.0,
            'partial_match': 7.0,
            'context_match': 4.0,
            'topic_match': 2.0,
            'length_bonus': 1.0,
            'technical_term_bonus': 3.0,
            'gujarati_specific_bonus': 5.0
        }
        
        # Specific mapping patterns for better unit classification
        self.unit_specific_patterns = {
            "Unit-I": {
                "english": [
                    r"OSI.*model", r"TCP\/IP.*model", r"layered.*architecture", r"reference.*model",
                    r"physical.*topology", r"star.*topology", r"bus.*topology", r"ring.*topology", 
                    r"mesh.*topology", r"tree.*topology", r"network.*topology.*diagram",
                    r"client.*server", r"peer.*to.*peer", r"LAN.*WAN.*MAN", r"network.*classification"
                ],
                "gujarati": [
                    r"OSI.*મોડેલ", r"TCP\/IP.*મોડેલ", r"સ્તરીય.*આર્કિટેક્ચર", r"રેફરન્સ.*મોડેલ",
                    r"ભૌતિક.*ટોપોલોજી", r"સ્ટાર.*ટોપોલોજી", r"બસ.*ટોપોલોજી", r"રિંગ.*ટોપોલોજી",
                    r"મેશ.*ટોપોલોજી", r"ટ્રી.*ટોપોલોજી", r"નેટવર્ક.*ટોપોલોજી.*આકૃતિ",
                    r"ક્લાઇન્ટ.*સર્વર", r"પીઅર.*ટુ.*પીઅર", r"LAN.*WAN.*MAN", r"નેટવર્ક.*વર્ગીકરણ"
                ]
            },
            "Unit-II": {
                "english": [
                    r"router.*hub.*switch", r"repeater", r"bridge", r"gateway", r"access.*point",
                    r"fast.*ethernet", r"gigabit.*ethernet", r"wireless.*LAN", r"network.*management"
                ],
                "gujarati": [
                    r"રાઉટર.*હબ.*સ્વિચ", r"રીપીટર", r"બ્રિજ", r"ગેટવે", r"એક્સેસ.*પોઇન્ટ",
                    r"ફાસ્ટ.*ઇથરનેટ", r"ગીગાબિટ.*ઇથરનેટ", r"વાયરલેસ.*LAN"
                ]
            },
            "Unit-III": {
                "english": [
                    r"IP.*address", r"CIDR", r"NAT", r"DHCP", r"ARP", r"RARP", r"routing.*algorithm",
                    r"data.*link.*layer", r"packet.*switching", r"DSL.*technology", r"cable.*modem"
                ],
                "gujarati": [
                    r"IP.*એડ્રેસ", r"CIDR", r"NAT", r"DHCP", r"ARP", r"RARP", r"રાઉટિંગ.*અલ્ગોરિધમ",
                    r"ડેટા.*લિંક.*લેયર", r"પેકેટ.*સ્વિચિંગ", r"DSL.*ટેકનોલોજી"
                ]
            },
            "Unit-IV": {
                "english": [
                    r"TCP.*UDP", r"connection.*oriented", r"connectionless", r"DNS", r"HTTP", 
                    r"email.*protocol", r"SMTP", r"POP3", r"IMAP", r"FTP", r"voice.*over.*IP"
                ],
                "gujarati": [
                    r"TCP.*UDP", r"કનેક્શન.*ઓરિએન્ટેડ", r"કનેક્શનલેસ", r"DNS", r"HTTP",
                    r"ઇમેઇલ.*પ્રોટોકોલ", r"SMTP", r"POP3", r"IMAP", r"FTP"
                ]
            },
            "Unit-V": {
                "english": [
                    r"network.*security", r"cryptography", r"encryption.*decryption", r"IPSec", 
                    r"SSL|TLS", r"digital.*signature", r"IT.*act", r"cyber.*law", r"VPN",
                    r"security.*topology", r"firewall.*security", r"hacking.*precautions", r"information.*security"
                ],
                "gujarati": [
                    r"નેટવર્ક.*સિક્યુરિટી", r"ક્રિપ્ટોગ્રાફી", r"એન્ક્રિપ્શન.*ડિક્રિપ્શન", 
                    r"IPSec", r"SSL|TLS", r"ડિજિટલ.*સિગ્નેચર", r"IT.*એક્ટ", r"VPN",
                    r"સિક્યુરિટી.*ટોપોલોજી", r"ફાયરવોલ.*સિક્યુરિટી", r"હેકિંગ.*સાવચેતીઓ", r"ઇન્ફર્મેશન.*સિક્યોરિટી"
                ]
            }
        }
        
    def load_syllabus(self) -> Dict:
        """Load syllabus JSON file"""
        syllabus_file = self.base_path / "4343202.json"
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
                    r'##\s+Q(?:uestion)?\s*(\d+)\.?([a-z]+)?\s*\[(\d+)\s*marks?\][\s\n]*\*\*(.+?)\*\*',
                    r'##\s+Q(?:uestion)?\s*(\d+)\.?([a-z]+)?\s*\[(\d+)\s*marks?\][\s\n]*(.+?)(?=##|$)',
                ]
            else:  # gujarati
                patterns = [
                    r'##\s+પ્રશ્ન\s+(\d+)\([અ-ઝ]+\)\s+\[(\d+)\s+ગુણ\][\s\n]*\*\*(.+?)\*\*',
                    r'##\s+પ્રશ્ન\s+(\d+)\([અ-ઝ]+\)\s+\[(\d+)\s+ગુણ\][\s\n]*(.+?)(?=##|$)',
                ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
                
                for match in matches:
                    try:
                        groups = match.groups()
                        
                        if len(groups) == 3:
                            question_num, marks, text = groups
                        elif len(groups) == 4:
                            question_num, sub_part, marks, text = groups
                            # Handle cases where sub_part might be the marks
                            if sub_part and sub_part.isdigit():
                                marks = sub_part
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
        
        # Context matching based on common Computer Networking terms with more specific mappings
        context_indicators = {
            "Unit-I": ["network topology", "OSI model", "TCP/IP model", "seven layer", "application layer", 
                      "transport layer", "network layer", "physical topology", "star topology", "bus topology",
                      "ring topology", "mesh topology", "tree topology", "hybrid topology", "PAN", "LAN", "WAN", 
                      "MAN", "client server", "peer to peer"],
            "Unit-II": ["repeater", "bridge", "gateway", "access point", "network adapter", "fast ethernet", 
                       "gigabit ethernet", "wireless LAN", "FDDI", "CDDI", "software defined network", "SDN",
                       "network management", "administrative", "SNMP"],
            "Unit-III": ["twisted pair", "coaxial cable", "fiber optic", "ISM band", "DSL technology", "cable modem",
                        "data link layer", "error control", "flow control", "packet switching", "circuit switching",
                        "static routing", "dynamic routing", "IP addressing", "IPv4", "IPv6", "CIDR", "subnetting",
                        "ICMP", "ARP", "RARP", "DHCP", "BOOTP"],
            "Unit-IV": ["transport layer", "TCP protocol", "UDP protocol", "connection oriented", "connectionless",
                       "DNS server", "domain name", "HTTP protocol", "web browser", "email system", "SMTP", "POP3",
                       "IMAP", "FTP protocol", "file transfer", "voice over IP", "VoIP", "multimedia"],
            "Unit-V": ["network security", "cryptography", "encryption", "decryption", "IPSec", "SSL", "TLS",
                      "digital signature", "certificate", "VPN", "firewall security", "intrusion detection",
                      "IT act", "cyber laws", "copyright act", "privacy", "authentication", "authorization"]
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
                "course_code": "4343202",
                "course_title": "Computer Networking",
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
        
        # Add unique questions to the question bank (deduplicate)
        unique_questions = {}
        for question in self.questions:
            # Use a combination of text and source for uniqueness
            unique_key = f"{question.text}_{question.source_file}"
            if unique_key not in unique_questions:
                unique_questions[unique_key] = question
            # Keep the one with higher confidence if duplicate
            elif question.confidence > unique_questions[unique_key].confidence:
                unique_questions[unique_key] = question
        
        for question in unique_questions.values():
            question_data = asdict(question)
            question_bank["questions"].append(question_data)
            
        # Update metadata with deduplicated count
        question_bank["metadata"]["total_questions"] = len(unique_questions)
        if len(unique_questions) > 0:
            mapped_count = len([q for q in unique_questions.values() if q.unit != "Unknown"])
            question_bank["metadata"]["mapping_accuracy"] = f"{(mapped_count / len(unique_questions)) * 100:.2f}%"
        
        return question_bank
    
    def save_question_bank(self, output_file: str = "4343202-question-bank-final.json"):
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
        print("🚀 Starting Enhanced Computer Networking Question Bank Generation...")
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
    base_path = "/Users/milav/Code/studio/content/resources/study-materials/32-ict/sem-4/4343202-computer-networking"
    
    generator = EnhancedComputerNetworkingQuestionBankGenerator(base_path)
    generator.run()


if __name__ == "__main__":
    main()