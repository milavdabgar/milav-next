---
theme: default
background: https://source.unsplash.com/1920x1080/?computer,forensics,network,investigation,analysis
title: Computer and Network Forensics
info: |
  ## Cyber Security (4353204)
  Unit V: Cybercrime & Digital Forensics
  Lecture 34: Technical Investigation of Digital Systems
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Computer and Network Forensics
## Unit V: Cybercrime & Digital Forensics
### Lecture 34: Technical Analysis of Digital Evidence

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Semester V | Diploma ICT | Author: Milav Dabgar
</div>

---
layout: default
---

# Computer Forensics Fundamentals

<div class="grid grid-cols-2 gap-8">

<div>

## 💾 Digital Storage Analysis

**Computer forensics** involves the scientific examination of computer systems, storage devices, and digital media to recover and analyze evidence of criminal or malicious activity.

### 📊 Storage Technology Overview
- **Traditional Hard Drives** (HDD) - Magnetic storage
- **Solid State Drives** (SSD) - Flash memory
- **Optical Media** (CD/DVD/Blu-ray) - Laser-etched data
- **USB Flash Drives** - Portable flash memory
- **Memory Cards** - SD, microSD, CompactFlash
- **Tape Storage** - Sequential magnetic storage

### 🔍 File System Types
```yaml
Windows File Systems:
  NTFS (New Technology File System):
    - Advanced permissions and encryption
    - File compression and journaling
    - Alternate Data Streams (ADS)
    - Master File Table (MFT)
    - Volume Shadow Copies

  FAT32 (File Allocation Table):
    - Simple structure
    - Limited file size (4GB)
    - Cross-platform compatibility
    - No built-in security

  exFAT (Extended FAT):
    - Large file support
    - Flash memory optimization
    - Cross-platform compatibility
    - No journaling

Unix/Linux File Systems:
  ext4 (Fourth Extended):
    - Journaling capabilities
    - Large file system support
    - Backward compatibility
    - Extents for performance

  XFS (SGI Extended):
    - High-performance journaling
    - Parallel I/O support
    - Online defragmentation
    - Metadata optimization
```

</div>

<div>

## 🛠️ Forensic Acquisition Techniques

### 📷 Imaging Methods
```yaml
Physical Imaging:
  - Bit-by-bit copy of entire drive
  - Includes unallocated space
  - Sector-level duplication
  - Most comprehensive method
  - Required for deleted data recovery

Logical Imaging:
  - File-by-file copy
  - Only allocated data copied
  - Faster acquisition process
  - Smaller image files
  - Limited forensic value

Live Imaging:
  - System remains operational
  - Network-based acquisition
  - Minimal system impact
  - Encrypted drive access
  - Remote forensics capability
```

### 🔐 Acquisition Challenges
```bash
# DD command examples for different scenarios
# Basic disk imaging
dd if=/dev/sda of=/evidence/disk.dd bs=4096 conv=noerror,sync

# Imaging with progress monitoring
dd if=/dev/sda of=/evidence/disk.dd bs=4096 conv=noerror,sync status=progress

# DC3DD with forensic features
dc3dd if=/dev/sda of=/evidence/disk.dd hash=sha256 log=/evidence/acquisition.log progress=on

# Imaging encrypted drives (after decryption)
dd if=/dev/mapper/encrypted_volume of=/evidence/decrypted.dd bs=4096

# Network imaging with netcat
# On forensic workstation:
nc -l -p 9999 | dd of=/evidence/remote_disk.dd bs=4096

# On target system:
dd if=/dev/sda bs=4096 | nc forensic_workstation 9999
```

### 📋 Acquisition Documentation
```yaml
Required Information:
  Case Details:
    - Case number and reference
    - Investigating officer
    - Date and time of acquisition
    - Location of acquisition

  System Information:
    - Make, model, and serial numbers
    - Hardware specifications
    - Operating system version
    - Network configuration

  Acquisition Details:
    - Imaging method used
    - Tools and software versions
    - Hash values (MD5/SHA1/SHA256)
    - Any errors encountered
    - Chain of custody information
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: default
---

# File System Analysis Techniques

<div class="grid grid-cols-2 gap-8">

<div>

## 📂 File System Structures

### 🗃️ NTFS Analysis
```yaml
Master File Table (MFT):
  Structure:
    - File record entries (1024 bytes each)
    - Metadata about every file/folder
    - Timestamps (MACE - Modified, Accessed, Created, Entry)
    - File attributes and permissions
    - Resident and non-resident data

  Forensic Significance:
    - Deleted file recovery
    - Timeline reconstruction
    - File activity tracking
    - Alternate data streams
    - Journaling information

Key MFT Records:
  - $MFT (Record 0): MFT itself
  - $MFTMirr (Record 1): MFT backup
  - $LogFile (Record 2): NTFS journal
  - $Volume (Record 3): Volume information
  - $AttrDef (Record 4): Attribute definitions
  - $Root (Record 5): Root directory
  - $Bitmap (Record 6): Cluster allocation
  - $Boot (Record 7): Boot sector backup
  - $BadClus (Record 8): Bad cluster list
  - $Secure (Record 9): Security descriptors
```

### 🔍 Deleted File Recovery
```python
# Python script for basic deleted file detection
import struct

def analyze_mft_record(mft_data, record_number):
    """Analyze individual MFT record"""
    offset = record_number * 1024  # Each MFT record is 1024 bytes
    record = mft_data[offset:offset + 1024]
    
    # Check if record is in use or deleted
    flags = struct.unpack('<H', record[22:24])[0]
    in_use = flags & 0x0001
    is_directory = flags & 0x0002
    
    if not in_use:
        # This is a deleted record
        filename = extract_filename(record)
        timestamps = extract_timestamps(record)
        file_size = extract_file_size(record)
        
        return {
            'record_number': record_number,
            'filename': filename,
            'is_deleted': True,
            'is_directory': bool(is_directory),
            'timestamps': timestamps,
            'size': file_size
        }
    
    return None

def extract_filename(record):
    """Extract filename from MFT record"""
    # Look for $FILE_NAME attribute (0x30)
    attribute_offset = 56  # Start of attributes
    while attribute_offset < len(record):
        attr_type = struct.unpack('<I', record[attribute_offset:attribute_offset+4])[0]
        
        if attr_type == 0x30:  # $FILE_NAME
            # Extract filename from attribute
            filename_length = record[attribute_offset + 88]
            filename_offset = attribute_offset + 90
            filename = record[filename_offset:filename_offset + filename_length*2].decode('utf-16le', errors='ignore')
            return filename
        
        # Move to next attribute
        attr_length = struct.unpack('<I', record[attribute_offset+4:attribute_offset+8])[0]
        if attr_length == 0:
            break
        attribute_offset += attr_length
    
    return "Unknown"
```

</div>

<div>

## 🕰️ Timeline Analysis

### ⏰ Timestamp Examination
```yaml
NTFS Timestamps (MACE):
  Modified (M): Last write time to file data
  Accessed (A): Last access to file data
  Created (C): File creation time
  Entry Modified (E): Last modification of MFT record

Timestamp Resolution:
  - NTFS: 100-nanosecond precision
  - FAT32: 2-second precision for modified
  - ext4: Nanosecond precision
  - APFS: Nanosecond precision

Forensic Significance:
  - User activity patterns
  - File creation sequences
  - Evidence tampering detection
  - Alibi verification
  - Attack timeline reconstruction
```

### 📊 Timeline Construction Tools
```bash
# Log2timeline/Plaso for comprehensive timeline creation
log2timeline.py --storage-file timeline.plaso disk_image.dd

# Convert to readable format
psort.py -w timeline.csv timeline.plaso

# Mactime for file system timeline
fls -r -m / disk_image.dd > bodyfile.txt
mactime -b bodyfile.txt -d > timeline.txt

# Volatility for memory timeline
volatility -f memory.dmp --profile=Win10x64 timeliner --output-file=memory_timeline.txt
```

### 🔍 Artifact Analysis
```yaml
Windows Artifacts:
  Registry Hives:
    - SYSTEM: System configuration
    - SOFTWARE: Installed applications
    - SECURITY: Security policies
    - SAM: User account information
    - NTUSER.DAT: User-specific settings

  Log Files:
    - Windows Event Logs (.evtx)
    - IIS web server logs
    - Application-specific logs
    - Security audit logs

  Browser Artifacts:
    - History databases
    - Cache files
    - Cookies
    - Download records
    - Bookmarks

  Email Artifacts:
    - PST/OST files (Outlook)
    - EDB files (Exchange)
    - Thunderbird profiles
    - Web-based email traces
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: default
---

# Network Forensics Techniques

<div class="grid grid-cols-2 gap-8">

<div>

## 🌐 Network Evidence Collection

### 📡 Packet Capture Analysis
```python
# Python script for network forensics analysis
import dpkt
import socket
import struct
from collections import Counter

class NetworkForensics:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.connections = {}
        self.dns_queries = []
        self.http_requests = []
        self.suspicious_patterns = []
    
    def analyze_pcap(self):
        """Comprehensive PCAP analysis"""
        with open(self.pcap_file, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            
            for timestamp, buf in pcap:
                try:
                    eth = dpkt.ethernet.Ethernet(buf)
                    if isinstance(eth.data, dpkt.ip.IP):
                        self.analyze_ip_packet(eth.data, timestamp)
                except:
                    continue
    
    def analyze_ip_packet(self, ip_packet, timestamp):
        """Analyze individual IP packets"""
        src_ip = socket.inet_ntoa(ip_packet.src)
        dst_ip = socket.inet_ntoa(ip_packet.dst)
        
        # Track connections
        connection_key = f"{src_ip}->{dst_ip}"
        if connection_key not in self.connections:
            self.connections[connection_key] = {
                'packets': 0,
                'bytes': 0,
                'first_seen': timestamp,
                'last_seen': timestamp,
                'protocols': set()
            }
        
        self.connections[connection_key]['packets'] += 1
        self.connections[connection_key]['bytes'] += len(ip_packet)
        self.connections[connection_key]['last_seen'] = timestamp
        
        # Analyze specific protocols
        if isinstance(ip_packet.data, dpkt.tcp.TCP):
            self.analyze_tcp(ip_packet, src_ip, dst_ip, timestamp)
        elif isinstance(ip_packet.data, dpkt.udp.UDP):
            self.analyze_udp(ip_packet, src_ip, dst_ip, timestamp)
    
    def analyze_tcp(self, ip_packet, src_ip, dst_ip, timestamp):
        """Analyze TCP traffic"""
        tcp = ip_packet.data
        
        # HTTP traffic analysis
        if tcp.dport == 80 or tcp.sport == 80:
            if tcp.data:
                self.analyze_http(tcp.data, src_ip, dst_ip, timestamp)
        
        # HTTPS traffic (encrypted but metadata available)
        elif tcp.dport == 443 or tcp.sport == 443:
            self.analyze_tls(tcp.data, src_ip, dst_ip, timestamp)
    
    def analyze_http(self, data, src_ip, dst_ip, timestamp):
        """Analyze HTTP requests and responses"""
        try:
            if data.startswith(b'GET') or data.startswith(b'POST'):
                http_request = dpkt.http.Request(data)
                self.http_requests.append({
                    'timestamp': timestamp,
                    'src_ip': src_ip,
                    'dst_ip': dst_ip,
                    'method': http_request.method,
                    'uri': http_request.uri,
                    'headers': dict(http_request.headers)
                })
        except:
            pass
```

### 🔍 Traffic Pattern Analysis
```yaml
Suspicious Indicators:
  Volume Anomalies:
    - Unusual data transfer volumes
    - Off-hours network activity
    - Bandwidth consumption spikes
    - Asymmetric traffic patterns

  Protocol Anomalies:
    - Non-standard port usage
    - Protocol tunneling
    - Encrypted traffic on unusual ports
    - Malformed packet structures

  Behavioral Indicators:
    - Beaconing (C&C communication)
    - Data exfiltration patterns
    - Lateral movement traces
    - Reconnaissance activities
```

</div>

<div>

## 🚨 Intrusion Detection Analysis

### 📊 Log File Analysis
```bash
# Apache/Nginx log analysis for attacks
# SQL injection attempts
grep -i "select\|union\|insert\|delete\|drop" /var/log/apache2/access.log

# XSS attempts
grep -i "script\|alert\|onload\|onerror" /var/log/apache2/access.log

# Directory traversal attempts
grep -i "\.\.\/" /var/log/apache2/access.log

# Brute force detection
awk '{print $1}' /var/log/apache2/access.log | sort | uniq -c | sort -nr | head -20

# Failed login attempts (SSH)
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr

# Windows Event Log analysis with PowerShell
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} | 
    Group-Object Properties[19].Value | 
    Sort-Object Count -Descending | 
    Select-Object Count, Name
```

### 🔗 Network Behavior Analysis
```yaml
Attack Pattern Recognition:
  Reconnaissance Phase:
    - Port scanning activities
    - DNS enumeration
    - Service fingerprinting
    - Vulnerability scanning
    - WHOIS queries

  Exploitation Phase:
    - Exploit payload delivery
    - Shell code execution
    - Privilege escalation attempts
    - System compromise indicators

  Post-Exploitation:
    - Command and control communication
    - Data collection activities
    - Lateral movement attempts
    - Persistence establishment
    - Exfiltration preparation
```

### 🛡️ Firewall and IDS Log Analysis
```python
# Firewall log parser for forensic analysis
import re
from datetime import datetime
from collections import defaultdict

class FirewallLogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.blocked_ips = defaultdict(int)
        self.attack_patterns = defaultdict(list)
        self.port_scan_detection = defaultdict(set)
    
    def parse_logs(self):
        """Parse and analyze firewall logs"""
        with open(self.log_file, 'r') as f:
            for line in f:
                self.analyze_log_entry(line)
    
    def analyze_log_entry(self, log_line):
        """Analyze individual log entries"""
        # Parse common firewall log format
        pattern = r'(\w+\s+\d+\s+\d+:\d+:\d+).*SRC=(\d+\.\d+\.\d+\.\d+).*DST=(\d+\.\d+\.\d+\.\d+).*DPT=(\d+)'
        match = re.search(pattern, log_line)
        
        if match:
            timestamp, src_ip, dst_ip, dst_port = match.groups()
            
            # Count blocked attempts per IP
            self.blocked_ips[src_ip] += 1
            
            # Detect port scanning
            self.port_scan_detection[src_ip].add(dst_port)
            
            # Pattern analysis
            if 'DROP' in log_line or 'DENY' in log_line:
                self.attack_patterns['blocked_attempts'].append({
                    'timestamp': timestamp,
                    'src_ip': src_ip,
                    'dst_ip': dst_ip,
                    'dst_port': dst_port
                })
    
    def generate_report(self):
        """Generate forensic analysis report"""
        report = {
            'top_attackers': sorted(self.blocked_ips.items(), 
                                  key=lambda x: x[1], reverse=True)[:10],
            'port_scanners': {ip: len(ports) for ip, ports 
                             in self.port_scan_detection.items() if len(ports) > 10},
            'attack_timeline': sorted(self.attack_patterns['blocked_attempts'],
                                    key=lambda x: x['timestamp'])
        }
        return report
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: default
---

# Advanced Forensic Techniques

<div class="grid grid-cols-2 gap-8">

<div>

## 🧠 Memory Forensics

### 💾 Memory Acquisition
```bash
# Memory dump acquisition methods
# Linux - using LiME (Linux Memory Extractor)
insmod lime.ko "path=/evidence/memory.lime format=lime"

# Windows - using WinPmem
winpmem.exe -o /evidence/memory.raw

# DumpIt (Windows)
DumpIt.exe /output C:\evidence\memory.dmp

# FTK Imager memory capture
# File > Capture Memory > Select output location
```

### 🔍 Memory Analysis with Volatility
```bash
# Volatility Framework commands
# Identify operating system profile
volatility -f memory.dmp imageinfo

# List running processes
volatility -f memory.dmp --profile=Win10x64 pslist

# Process tree view
volatility -f memory.dmp --profile=Win10x64 pstree

# Network connections
volatility -f memory.dmp --profile=Win10x64 netscan

# Command history
volatility -f memory.dmp --profile=Win10x64 cmdscan
volatility -f memory.dmp --profile=Win10x64 consoles

# Registry analysis
volatility -f memory.dmp --profile=Win10x64 hivelist
volatility -f memory.dmp --profile=Win10x64 printkey -K "Software\Microsoft\Windows\CurrentVersion\Run"

# Malware detection
volatility -f memory.dmp --profile=Win10x64 malfind
volatility -f memory.dmp --profile=Win10x64 yarascan -y malware_rules.yar
```

### 🦠 Malware Analysis in Memory
```python
# Memory forensics analysis script
import volatility.conf as conf
import volatility.registry as registry
from volatility.framework import interfaces, plugins
from volatility.framework.configuration import requirements

class MemoryForensics:
    def __init__(self, memory_dump, profile):
        self.memory_dump = memory_dump
        self.profile = profile
        self.config = self.setup_config()
    
    def setup_config(self):
        """Setup Volatility configuration"""
        registry.PluginImporter()
        config = conf.ConfObject()
        config.PROFILE = self.profile
        config.LOCATION = f"file://{self.memory_dump}"
        return config
    
    def find_hidden_processes(self):
        """Detect process hiding techniques"""
        # Compare pslist with psscan results
        pslist_processes = self.get_process_list()
        psscan_processes = self.get_process_scan()
        
        hidden_processes = []
        for proc in psscan_processes:
            if proc not in pslist_processes:
                hidden_processes.append(proc)
        
        return hidden_processes
    
    def analyze_network_artifacts(self):
        """Analyze network connections in memory"""
        connections = self.get_network_connections()
        suspicious_connections = []
        
        for conn in connections:
            # Check for suspicious indicators
            if self.is_suspicious_connection(conn):
                suspicious_connections.append(conn)
        
        return suspicious_connections
    
    def detect_code_injection(self):
        """Detect code injection techniques"""
        injected_code = []
        processes = self.get_process_list()
        
        for proc in processes:
            if self.has_injected_code(proc):
                injected_code.append(proc)
        
        return injected_code
```

</div>

<div>

## 📱 Mobile Device Forensics

### 🔓 Mobile Acquisition Methods
```yaml
Logical Extraction:
  - File system access through OS
  - Limited to accessible data
  - Quick and non-intrusive
  - May miss deleted data
  - Tools: Cellebrite UFED, Oxygen Detective

Physical Extraction:
  - Bit-by-bit copy of storage
  - Requires device rooting/jailbreaking
  - Maximum data recovery
  - May void warranty
  - Tools: XRY Mobile, MSAB Mobile Forensics

Chip-off Analysis:
  - Physical memory chip removal
  - Direct chip reading
  - Last resort method
  - Destructive to device
  - Specialized hardware required

JTAG/ISP Methods:
  - Debug interface access
  - Firmware-level extraction
  - Bypasses OS security
  - Technical expertise required
  - May damage device
```

### 📊 Mobile Evidence Types
```yaml
Communication Evidence:
  - Call logs and duration
  - SMS/MMS messages
  - Instant messaging (WhatsApp, Telegram)
  - Email communications
  - Voice messages and recordings

Location Evidence:
  - GPS coordinates and tracks
  - Cell tower connections
  - Wi-Fi access point data
  - Location-based app data
  - Geofenced areas

Application Data:
  - Social media posts and messages
  - Photo and video metadata
  - Banking and financial apps
  - Navigation and travel data
  - Gaming and entertainment apps

System Artifacts:
  - Device information and IMEI
  - Installed applications
  - System logs and crash reports
  - Network connection history
  - Security events and locks
```

### 🔍 Cloud Forensics Integration
```yaml
Cloud Evidence Sources:
  - Backup and synchronization services
  - Email and calendar services
  - Document storage and sharing
  - Photo and video cloud storage
  - Application data synchronization

Challenges:
  - Multi-jurisdictional issues
  - Data location uncertainty
  - Service provider cooperation
  - Legal process requirements
  - Technical access limitations

Acquisition Methods:
  - Legal process to service providers
  - User consent and credentials
  - API-based data extraction
  - Account preservation requests
  - Emergency disclosure procedures
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: default
---

# Practical Exercise: Digital Investigation Lab

<div class="exercise-container">

## 🎯 Comprehensive Forensic Analysis (35 minutes)

### Mission: Multi-Platform Digital Investigation

Your forensic team must analyze evidence from a sophisticated cybercrime involving **"TechCorp Industries"** where attackers compromised multiple systems and exfiltrated sensitive data.

### 🖥️ Evidence Sources Available
**Investigation Assets:**
- **Windows 10 workstation** disk image (500GB)
- **Linux web server** disk image (1TB)
- **Network packet capture** (48 hours of traffic)
- **Mobile device** (Android smartphone)
- **Memory dumps** from compromised systems
- **Router and firewall logs** (1 week period)

### Phase 1: Evidence Prioritization and Analysis Planning (15 minutes)

**Team Assignment: Forensic Strategy Development**

1. **Evidence Triage and Prioritization**
   - Assess volatility and importance of each evidence source
   - Create systematic examination timeline
   - Plan resource allocation for analysis tasks
   - Design evidence correlation methodology

2. **Technical Analysis Framework**
   - File system examination procedures for Windows and Linux
   - Network traffic analysis and pattern recognition
   - Memory forensics for malware and process analysis
   - Mobile device data extraction and interpretation

### Phase 2: Multi-Platform Analysis Implementation (12 minutes)

**Forensic Examination Procedures:**
1. **Disk Image Analysis**
   - File system timeline reconstruction
   - Deleted file recovery and analysis
   - Registry examination (Windows)
   - Log file analysis (Linux)
   - Artifact correlation across systems

2. **Network and Memory Analysis**
   - Packet capture analysis for attack vectors
   - Memory dump examination for persistence mechanisms
   - Network behavior pattern analysis
   - Command and control communication detection

### Phase 3: Evidence Correlation and Timeline Reconstruction (8 minutes)

**Investigation Synthesis:**
1. **Cross-Platform Evidence Correlation**
   - Timeline alignment across all evidence sources
   - Attack vector identification and progression
   - Data exfiltration path reconstruction
   - Attacker attribution and methodology analysis

2. **Comprehensive Reporting Framework**
   - Technical findings documentation
   - Evidence chain of custody maintenance
   - Executive summary preparation
   - Legal admissibility compliance verification

**Deliverables:**
- Complete multi-platform forensic analysis methodology
- Evidence correlation timeline with attack progression
- Technical analysis results with supporting evidence
- Comprehensive investigative report with legal compliance

</div>

<style>
.exercise-container {
  @apply bg-green-50 border-2 border-green-300 rounded-lg p-6;
}
</style>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: center
class: text-center
---

# Questions & Discussion

## 🤔 Technical Investigation Points:
- How do you handle encrypted evidence in digital forensics?
- What are the challenges of analyzing modern SSD drives vs traditional HDDs?
- How do you ensure forensic analysis doesn't alter original evidence?

### 💡 Exercise Review
Present your multi-platform forensic analysis strategies and discuss correlation techniques

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>

---
layout: center
class: text-center
---

# Thank You!

## Next Lecture: Mobile Device and Cloud Forensics
### Modern Digital Investigation Challenges

<div class="pt-8 text-gray-500">
  <p>Cyber Security (4353204) - Lecture 34 Complete</p>
  <p>Technical forensics: Uncovering digital truth through science! 🔬💻</p>
</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 34 | Author: Milav Dabgar
</div>