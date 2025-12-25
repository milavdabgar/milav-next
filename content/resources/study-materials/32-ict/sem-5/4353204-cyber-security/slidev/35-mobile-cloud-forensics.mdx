---
theme: default
background: https://source.unsplash.com/1920x1080/?mobile,cloud,forensics,smartphone,investigation
title: Mobile Device and Cloud Forensics
info: |
  ## Cyber Security (4353204)
  Unit V: Cybercrime & Digital Forensics
  Lecture 35: Modern Digital Evidence Investigation
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Mobile Device and Cloud Forensics
## Unit V: Cybercrime & Digital Forensics
### Lecture 35: Investigating Modern Digital Ecosystems

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Semester V | Diploma ICT | Author: Milav Dabgar
</div>

---
layout: default
---

# Mobile Device Forensics Overview

<div class="grid grid-cols-2 gap-8">

<div>

## 📱 Mobile Ecosystem Evolution

**Mobile forensics** involves the scientific examination of mobile devices to recover digital evidence while maintaining its integrity and admissibility in legal proceedings.

### 📊 Mobile Device Statistics (2024)
- **Global smartphone users**: 6.8 billion (86% of population)
- **Data generated per device**: 2.5GB daily
- **App installations**: 230 billion annually
- **Mobile crime cases**: 78% involve smartphones
- **Evidence recovery rate**: 65% from locked devices
- **Cloud synchronization**: 91% of users enabled

### 🔐 Mobile Security Evolution
```yaml
Early Mobile Devices (2000-2010):
  - Basic PIN protection
  - Limited encryption
  - Simple file systems
  - Minimal app ecosystem
  - Easy physical access

Modern Smartphones (2010-Present):
  - Biometric authentication
  - Hardware security modules
  - Full disk encryption
  - Secure boot processes
  - App sandboxing
  - Regular security updates

Next Generation (2024+):
  - AI-powered security
  - Quantum-resistant encryption
  - Advanced biometrics
  - Zero-trust architectures
  - Privacy-by-design
```

</div>

<div>

## 🛠️ Mobile Forensic Challenges

### 🔒 Technical Barriers
```yaml
Device Security:
  Encryption Challenges:
    - AES-256 full disk encryption
    - Hardware-backed keystores
    - Secure enclave protection
    - Anti-tampering mechanisms
    - Remote wipe capabilities

  Authentication Barriers:
    - Biometric locks (fingerprint, face, iris)
    - Multi-factor authentication
    - Pattern and PIN complexity
    - Account lockout mechanisms
    - Time-based restrictions

Operating System Protection:
  iOS Security:
    - Locked bootloader
    - Code signing requirements
    - App Store restrictions
    - System integrity protection
    - Jailbreak detection

  Android Security:
    - SELinux implementation
    - Verified boot process
    - Permission model
    - SafetyNet attestation
    - Anti-root detection
```

### ⚖️ Legal and Procedural Issues
```yaml
Legal Challenges:
  Privacy Rights:
    - Fourth Amendment protections (US)
    - GDPR compliance (EU)
    - Personal data protection laws
    - Reasonable expectation of privacy
    - Cloud data jurisdiction

  Technical Limitations:
    - Warrant scope and specificity
    - Technical assistance orders
    - Compelled decryption debates
    - Third-party data access
    - International cooperation requirements

Procedural Requirements:
  - Chain of custody maintenance
  - Evidence preservation protocols
  - Expert witness qualifications
  - Court admissibility standards
  - Documentation requirements
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: default
---

# Mobile Acquisition Techniques

<div class="grid grid-cols-2 gap-8">

<div>

## 🔓 Logical Acquisition

### 📲 Standard Logical Extraction
```python
# Mobile forensics logical acquisition framework
import subprocess
import sqlite3
import json
from datetime import datetime

class MobileLogicalForensics:
    def __init__(self, device_id, device_type):
        self.device_id = device_id
        self.device_type = device_type
        self.extraction_log = []
        self.artifacts = {}
    
    def android_logical_extraction(self):
        """Android logical data extraction using ADB"""
        adb_commands = [
            "adb devices",  # Verify device connection
            "adb shell getprop",  # Device properties
            "adb shell dumpsys",  # System services info
            "adb shell pm list packages",  # Installed packages
            "adb backup -shared -nosystem -apk -all",  # Full backup
        ]
        
        for cmd in adb_commands:
            try:
                result = subprocess.run(cmd.split(), capture_output=True, text=True)
                self.extraction_log.append({
                    'timestamp': datetime.now(),
                    'command': cmd,
                    'success': result.returncode == 0,
                    'output_size': len(result.stdout)
                })
            except Exception as e:
                self.log_error(f"Command failed: {cmd} - {str(e)}")
    
    def extract_application_data(self, app_package):
        """Extract specific application data"""
        app_data_paths = [
            f"/data/data/{app_package}/",
            f"/sdcard/Android/data/{app_package}/",
            f"/data/media/0/Android/data/{app_package}/"
        ]
        
        extracted_data = {}
        for path in app_data_paths:
            try:
                # Use ADB to pull application data
                cmd = f"adb pull {path} ./evidence/{app_package}/"
                result = subprocess.run(cmd.split(), capture_output=True, text=True)
                
                if result.returncode == 0:
                    extracted_data[path] = "Successfully extracted"
                else:
                    extracted_data[path] = f"Access denied: {result.stderr}"
                    
            except Exception as e:
                extracted_data[path] = f"Error: {str(e)}"
        
        return extracted_data
    
    def analyze_sqlite_databases(self, db_path):
        """Analyze SQLite databases commonly found in mobile apps"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            database_analysis = {}
            for table in tables:
                table_name = table[0]
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                row_count = cursor.fetchone()[0]
                
                # Get table schema
                cursor.execute(f"PRAGMA table_info({table_name})")
                schema = cursor.fetchall()
                
                database_analysis[table_name] = {
                    'row_count': row_count,
                    'schema': schema
                }
            
            conn.close()
            return database_analysis
            
        except Exception as e:
            return {'error': str(e)}
```

### 📊 iOS Logical Extraction
```bash
# iOS logical acquisition methods
# iTunes backup extraction (unencrypted)
idevicebackup2 backup --udid <device_udid> ./evidence/ios_backup/

# Device information gathering
ideviceinfo --udid <device_udid> > device_info.plist
idevicesyslog --udid <device_udid> > system_logs.txt

# Application list
ideviceinstaller --udid <device_udid> -l > installed_apps.txt

# Crash logs
idevicecrashreport --udid <device_udid> ./crash_logs/

# Screen capture (if unlocked)
idevicescreenshot --udid <device_udid> screenshot.png
```

</div>

<div>

## ⚡ Physical and Advanced Acquisition

### 🔬 Physical Extraction Methods
```yaml
Chip-off Forensics:
  Process:
    1. Device disassembly
    2. Flash memory chip identification
    3. Chip desoldering and removal
    4. Chip reading with specialized equipment
    5. Data reconstruction and analysis

  Equipment Required:
    - Hot air rework station
    - Microscope and fine tools
    - Chip readers (NAND, eMMC, UFS)
    - Data recovery software
    - Clean room environment

  Advantages:
    - Bypasses OS-level security
    - Maximum data recovery potential
    - Works on severely damaged devices
    - No dependency on device functionality

  Disadvantages:
    - Device destruction
    - High technical skill requirement
    - Expensive equipment needed
    - Time-intensive process
    - Potential data damage risk
```

### 🔌 JTAG/ISP Methods
```yaml
JTAG (Joint Test Action Group):
  Connection Points:
    - TDI (Test Data In)
    - TDO (Test Data Out)
    - TCK (Test Clock)
    - TMS (Test Mode Select)
    - TRST (Test Reset)

  Process:
    1. Device teardown and PCB access
    2. JTAG connection point identification
    3. Connection establishment
    4. Bootloader/firmware access
    5. Memory dump extraction

ISP (In-System Programming):
  Features:
    - Direct flash memory access
    - Bypasses main processor
    - Lower-level than JTAG
    - Hardware-specific protocols
    - Specialized adapters required
```

### 🛠️ Commercial Forensic Tools
```yaml
Cellebrite UFED (Universal Forensic Extraction Device):
  Capabilities:
    - Logical and physical extraction
    - Wide device support (10,000+ models)
    - Automated analysis
    - Password bypassing
    - Cloud data acquisition

  Supported Extractions:
    - File system extraction
    - Physical memory dumps
    - Bootloader unlocking
    - Root/jailbreak automation
    - Live data monitoring

Oxygen Detective Suite:
  Features:
    - Mobile and cloud forensics
    - Social media analysis
    - Timeline reconstruction
    - Advanced search capabilities
    - Multi-device correlation

MSAB XRY Mobile:
  Specializations:
    - Law enforcement focus
    - Court-ready reports
    - Encrypted device handling
    - Cloud evidence integration
    - Training and certification
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: default
---

# Mobile Evidence Analysis

<div class="grid grid-cols-2 gap-8">

<div>

## 💬 Communication Evidence

### 📨 Messaging Applications
```python
# WhatsApp database analysis
import sqlite3
import pandas as pd
from datetime import datetime

class WhatsAppForensics:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
    
    def extract_messages(self):
        """Extract all messages from WhatsApp database"""
        query = """
        SELECT 
            m.key_remote_jid as chat_id,
            m.key_from_me as from_me,
            m.data as message_data,
            m.timestamp as timestamp,
            m.media_wa_type as media_type,
            c.subject as group_name
        FROM messages m
        LEFT JOIN chat_list c ON m.key_remote_jid = c.key_remote_jid
        ORDER BY m.timestamp
        """
        
        df = pd.read_sql_query(query, self.conn)
        
        # Convert timestamp (WhatsApp uses milliseconds since epoch)
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        return df
    
    def analyze_deleted_messages(self):
        """Detect and analyze deleted messages"""
        query = """
        SELECT * FROM messages 
        WHERE data IS NULL OR data = ''
        ORDER BY timestamp
        """
        
        deleted_messages = pd.read_sql_query(query, self.conn)
        
        # Look for message gaps in conversation
        all_messages = self.extract_messages()
        
        deleted_analysis = {
            'explicit_deletions': len(deleted_messages),
            'message_gaps': self.detect_message_gaps(all_messages),
            'deletion_patterns': self.analyze_deletion_patterns(deleted_messages)
        }
        
        return deleted_analysis
    
    def extract_media_references(self):
        """Extract media file references and metadata"""
        query = """
        SELECT 
            key_remote_jid as chat_id,
            media_wa_type as media_type,
            media_size as file_size,
            media_name as filename,
            media_url as media_url,
            timestamp
        FROM messages 
        WHERE media_wa_type IS NOT NULL
        ORDER BY timestamp
        """
        
        return pd.read_sql_query(query, self.conn)
```

### 📞 Call Records Analysis
```yaml
Call Log Artifacts:
  Standard Fields:
    - Phone number (caller/callee)
    - Call duration
    - Call type (incoming/outgoing/missed)
    - Timestamp (start/end times)
    - Contact name (if available)

  Advanced Analysis:
    - Frequency patterns
    - Duration anomalies
    - Geographic correlation
    - Time zone analysis
    - Communication networks

Communication Pattern Analysis:
  Social Network Mapping:
    - Contact frequency ranking
    - Communication clusters
    - Relationship inference
    - Group communication patterns
    - Temporal activity analysis

  Behavioral Indicators:
    - Late night communications
    - Repeated short calls
    - Sudden communication cessation
    - Geographic movement correlation
    - Multi-platform coordination
```

</div>

<div>

## 🗺️ Location and Movement Evidence

### 📍 GPS and Location Services
```python
# Location data analysis framework
import json
import folium
from geopy.distance import geodesic
from datetime import datetime, timedelta

class LocationForensics:
    def __init__(self, location_data_file):
        self.location_data = self.load_location_data(location_data_file)
        self.significant_locations = []
        self.travel_patterns = []
    
    def load_location_data(self, file_path):
        """Load location data from various sources"""
        try:
            if file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    return json.load(f)
            elif file_path.endswith('.gpx'):
                return self.parse_gpx_file(file_path)
            else:
                return self.parse_generic_location_data(file_path)
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_movement_patterns(self):
        """Analyze movement and travel patterns"""
        if not self.location_data:
            return None
        
        movement_analysis = {
            'total_points': len(self.location_data),
            'time_range': self.calculate_time_range(),
            'distance_traveled': self.calculate_total_distance(),
            'average_speed': self.calculate_average_speed(),
            'significant_locations': self.identify_significant_locations(),
            'travel_routes': self.identify_travel_routes()
        }
        
        return movement_analysis
    
    def identify_significant_locations(self, min_duration_hours=2, radius_meters=100):
        """Identify locations where device spent significant time"""
        significant_locations = []
        
        for i, point in enumerate(self.location_data):
            nearby_points = self.find_nearby_points(point, radius_meters)
            
            if len(nearby_points) > 10:  # Minimum points for significance
                duration = self.calculate_duration_at_location(nearby_points)
                
                if duration.total_seconds() / 3600 >= min_duration_hours:
                    significant_locations.append({
                        'latitude': point['latitude'],
                        'longitude': point['longitude'],
                        'duration_hours': duration.total_seconds() / 3600,
                        'visit_count': len(nearby_points),
                        'first_visit': min(p['timestamp'] for p in nearby_points),
                        'last_visit': max(p['timestamp'] for p in nearby_points)
                    })
        
        return significant_locations
    
    def create_movement_map(self, output_file='movement_map.html'):
        """Create interactive map showing movement patterns"""
        if not self.location_data:
            return None
        
        # Calculate map center
        center_lat = sum(p['latitude'] for p in self.location_data) / len(self.location_data)
        center_lon = sum(p['longitude'] for p in self.location_data) / len(self.location_data)
        
        # Create folium map
        m = folium.Map(location=[center_lat, center_lon], zoom_start=10)
        
        # Add location points
        for point in self.location_data:
            folium.CircleMarker(
                location=[point['latitude'], point['longitude']],
                radius=3,
                popup=f"Time: {point['timestamp']}",
                color='blue',
                fillColor='blue'
            ).add_to(m)
        
        # Add significant locations
        for loc in self.significant_locations:
            folium.Marker(
                location=[loc['latitude'], loc['longitude']],
                popup=f"Duration: {loc['duration_hours']:.2f} hours",
                icon=folium.Icon(color='red', icon='home')
            ).add_to(m)
        
        m.save(output_file)
        return output_file
```

### 📊 Geofencing and Location Correlation
```yaml
Location Evidence Types:
  GPS Coordinates:
    - Precise positioning data
    - Timestamp correlation
    - Accuracy measurements
    - Movement velocity
    - Altitude information

  Cell Tower Data:
    - Cell site location information
    - Signal strength measurements
    - Handoff patterns
    - Coverage area analysis
    - Historical tower data

  Wi-Fi Access Points:
    - SSID and BSSID information
    - Signal strength indicators
    - Known location databases
    - Connection history
    - Network topology mapping

Forensic Applications:
  Criminal Investigations:
    - Suspect location verification
    - Alibi confirmation/refutation
    - Crime scene presence
    - Movement pattern analysis
    - Co-location with victims/witnesses

  Civil Cases:
    - Insurance fraud investigation
    - Employment verification
    - Custody dispute evidence
    - Personal injury claims
    - Property boundary disputes
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: default
---

# Cloud Forensics Fundamentals

<div class="grid grid-cols-2 gap-8">

<div>

## ☁️ Cloud Computing Models

### 🏗️ Service Models and Forensic Implications
```yaml
Infrastructure as a Service (IaaS):
  Examples: Amazon EC2, Google Compute Engine, Azure VMs
  Forensic Access:
    - Virtual machine snapshots
    - Storage volume imaging
    - Network traffic logs
    - Hypervisor-level analysis
    - Instance metadata

  Challenges:
    - Shared physical infrastructure
    - Dynamic resource allocation
    - Limited physical access
    - Multi-tenancy isolation
    - Provider cooperation requirements

Platform as a Service (PaaS):
  Examples: Google App Engine, Heroku, Azure App Service
  Forensic Evidence:
    - Application logs
    - Database transaction records
    - Code deployment history
    - Runtime environment data
    - API access logs

  Limitations:
    - Abstract infrastructure layer
    - Limited system-level access
    - Platform-specific tools required
    - Vendor-dependent capabilities
    - Reduced evidence granularity

Software as a Service (SaaS):
  Examples: Office 365, Google Workspace, Salesforce
  Available Evidence:
    - User activity logs
    - Document access records
    - Email communications
    - Collaboration histories
    - Administrative audit trails

  Constraints:
    - Application-level evidence only
    - Vendor-controlled retention
    - Limited customization options
    - API-based access required
    - Privacy policy restrictions
```

### 🌐 Deployment Models
```yaml
Public Cloud:
  - Shared infrastructure
  - Third-party provider control
  - Geographic distribution
  - Jurisdictional complexities
  - Cost-effective scalability

Private Cloud:
  - Dedicated infrastructure
  - Organization control
  - Enhanced security options
  - Simplified legal process
  - Higher cost and complexity

Hybrid Cloud:
  - Mixed deployment models
  - Complex data flows
  - Multiple evidence sources
  - Varied access controls
  - Integration challenges

Multi-Cloud:
  - Multiple cloud providers
  - Distributed evidence
  - Correlation complexity
  - Provider-specific tools
  - Unified analysis challenges
```

</div>

<div>

## 🔍 Cloud Evidence Acquisition

### 📋 Legal Process Requirements
```yaml
Legal Challenges:
  Jurisdictional Issues:
    - Data location uncertainty
    - Cross-border legal processes
    - Conflicting privacy laws
    - International cooperation treaties
    - Service provider policies

  Evidence Preservation:
    - Litigation hold notices
    - Data retention policies
    - Automatic deletion prevention
    - Backup and archival access
    - Chain of custody maintenance

  Access Methods:
    - Search warrants and subpoenas
    - Mutual legal assistance treaties
    - Emergency disclosure procedures
    - User consent and authorization
    - Third-party service agreements
```

### 🛠️ Technical Acquisition Methods
```python
# Cloud forensics acquisition framework
import boto3
import requests
import json
from datetime import datetime, timedelta

class CloudForensics:
    def __init__(self, cloud_provider, credentials):
        self.provider = cloud_provider
        self.credentials = credentials
        self.evidence_log = []
    
    def aws_evidence_collection(self):
        """AWS evidence collection procedures"""
        session = boto3.Session(
            aws_access_key_id=self.credentials['access_key'],
            aws_secret_access_key=self.credentials['secret_key'],
            region_name=self.credentials['region']
        )
        
        evidence = {
            'cloudtrail_logs': self.collect_cloudtrail_logs(session),
            'vpc_flow_logs': self.collect_vpc_flow_logs(session),
            'ec2_instances': self.collect_ec2_metadata(session),
            's3_access_logs': self.collect_s3_access_logs(session),
            'iam_activity': self.collect_iam_activity(session)
        }
        
        return evidence
    
    def collect_cloudtrail_logs(self, session, days=30):
        """Collect AWS CloudTrail audit logs"""
        cloudtrail = session.client('cloudtrail')
        
        end_time = datetime.now()
        start_time = end_time - timedelta(days=days)
        
        try:
            events = cloudtrail.lookup_events(
                LookupAttributes=[
                    {
                        'AttributeKey': 'EventTime',
                        'AttributeValue': start_time.isoformat()
                    }
                ],
                StartTime=start_time,
                EndTime=end_time
            )
            
            return {
                'event_count': len(events['Events']),
                'events': events['Events'],
                'collection_time': datetime.now().isoformat()
            }
        except Exception as e:
            return {'error': str(e)}
    
    def office365_evidence_collection(self):
        """Office 365 evidence collection via Graph API"""
        headers = {
            'Authorization': f'Bearer {self.credentials["access_token"]}',
            'Content-Type': 'application/json'
        }
        
        evidence_sources = {
            'audit_logs': 'https://graph.microsoft.com/v1.0/auditLogs/directoryAudits',
            'sign_ins': 'https://graph.microsoft.com/v1.0/auditLogs/signIns',
            'mail_activity': 'https://graph.microsoft.com/v1.0/me/messages',
            'sharepoint_activity': 'https://graph.microsoft.com/v1.0/sites/root/activities'
        }
        
        collected_evidence = {}
        for source_name, url in evidence_sources.items():
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    collected_evidence[source_name] = response.json()
                else:
                    collected_evidence[source_name] = {'error': f'HTTP {response.status_code}'}
            except Exception as e:
                collected_evidence[source_name] = {'error': str(e)}
        
        return collected_evidence
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: default
---

# Cloud Evidence Analysis

<div class="grid grid-cols-2 gap-8">

<div>

## 📊 Log Analysis and Correlation

### 🔍 Cloud Audit Trail Analysis
```python
# Cloud audit log analysis framework
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

class CloudAuditAnalyzer:
    def __init__(self, audit_logs):
        self.logs = pd.DataFrame(audit_logs)
        self.suspicious_activities = []
        self.user_behavior_profiles = {}
    
    def detect_anomalous_access(self):
        """Detect unusual access patterns"""
        # Time-based anomalies
        self.logs['hour'] = pd.to_datetime(self.logs['timestamp']).dt.hour
        hourly_activity = self.logs.groupby('hour').size()
        
        # Identify off-hours activity (outside 9 AM - 6 PM)
        off_hours_activity = self.logs[
            (self.logs['hour'] < 9) | (self.logs['hour'] > 18)
        ]
        
        # Geographic anomalies
        location_patterns = self.analyze_location_patterns()
        
        # Failed login attempts
        failed_logins = self.logs[
            self.logs['event_type'].str.contains('failed', case=False, na=False)
        ]
        
        anomalies = {
            'off_hours_count': len(off_hours_activity),
            'unusual_locations': location_patterns['anomalous_locations'],
            'failed_login_attempts': len(failed_logins),
            'bulk_operations': self.detect_bulk_operations()
        }
        
        return anomalies
    
    def analyze_data_access_patterns(self):
        """Analyze data access and exfiltration patterns"""
        data_events = self.logs[
            self.logs['event_type'].str.contains('download|export|share', case=False, na=False)
        ]
        
        # Group by user and analyze volumes
        user_data_access = data_events.groupby('user_id').agg({
            'file_size': ['sum', 'mean', 'count'],
            'timestamp': ['min', 'max']
        }).reset_index()
        
        # Identify potential data exfiltration
        threshold_size = user_data_access['file_size']['sum'].quantile(0.95)
        potential_exfiltration = user_data_access[
            user_data_access['file_size']['sum'] > threshold_size
        ]
        
        return {
            'total_data_events': len(data_events),
            'potential_exfiltration_users': len(potential_exfiltration),
            'largest_downloads': data_events.nlargest(10, 'file_size'),
            'access_patterns': self.calculate_access_patterns(data_events)
        }
    
    def generate_timeline_analysis(self):
        """Generate comprehensive timeline analysis"""
        timeline_events = self.logs.copy()
        timeline_events['timestamp'] = pd.to_datetime(timeline_events['timestamp'])
        timeline_events = timeline_events.sort_values('timestamp')
        
        # Identify event clusters
        timeline_events['time_diff'] = timeline_events['timestamp'].diff().dt.total_seconds()
        event_clusters = self.identify_event_clusters(timeline_events)
        
        return {
            'total_events': len(timeline_events),
            'event_clusters': event_clusters,
            'peak_activity_periods': self.identify_peak_periods(timeline_events),
            'user_activity_timeline': self.create_user_timeline(timeline_events)
        }
```

### 📈 Behavioral Pattern Analysis
```yaml
User Behavior Analytics:
  Normal Behavior Baselines:
    - Login time patterns
    - Geographic location consistency
    - Application usage patterns
    - Data access volumes
    - Collaboration behaviors

  Anomaly Detection:
    - Off-hours access
    - Unusual geographic locations
    - Bulk data downloads
    - Administrative privilege usage
    - Failed authentication patterns

  Risk Scoring:
    - Deviation from baseline
    - Multiple risk factors
    - Historical context
    - Peer group comparison
    - Temporal patterns

Data Exfiltration Indicators:
  Volume Anomalies:
    - Unusual download volumes
    - Bulk file operations
    - Compressed archive creation
    - External sharing activities
    - Print/screenshot activities

  Behavioral Indicators:
    - Pre-resignation activity spikes
    - Access to unrelated data
    - Weekend/holiday activity
    - VPN usage patterns
    - Device registration changes
```

</div>

<div>

## 🔗 Multi-Platform Evidence Correlation

### 🌐 Cross-Platform Timeline Reconstruction
```python
# Multi-platform evidence correlation
import json
from datetime import datetime
from collections import defaultdict

class MultiPlatformCorrelator:
    def __init__(self):
        self.evidence_sources = {}
        self.unified_timeline = []
        self.correlations = defaultdict(list)
    
    def add_evidence_source(self, source_name, evidence_data, timestamp_field, user_field):
        """Add evidence source with standardized format"""
        self.evidence_sources[source_name] = {
            'data': evidence_data,
            'timestamp_field': timestamp_field,
            'user_field': user_field,
            'normalized_events': self.normalize_events(evidence_data, timestamp_field, user_field)
        }
    
    def normalize_events(self, events, timestamp_field, user_field):
        """Normalize events to common format"""
        normalized = []
        
        for event in events:
            try:
                normalized_event = {
                    'timestamp': self.parse_timestamp(event.get(timestamp_field)),
                    'user': event.get(user_field, 'unknown'),
                    'event_type': self.classify_event(event),
                    'source': event.get('source', 'unknown'),
                    'original_data': event
                }
                normalized.append(normalized_event)
            except Exception as e:
                continue
        
        return sorted(normalized, key=lambda x: x['timestamp'])
    
    def correlate_user_activities(self, time_window_minutes=30):
        """Correlate activities across platforms for each user"""
        user_correlations = defaultdict(list)
        
        # Group events by user
        user_events = defaultdict(list)
        for source_name, source_data in self.evidence_sources.items():
            for event in source_data['normalized_events']:
                user_events[event['user']].append({
                    **event,
                    'source_platform': source_name
                })
        
        # Find temporal correlations for each user
        for user, events in user_events.items():
            events.sort(key=lambda x: x['timestamp'])
            
            for i, event1 in enumerate(events):
                correlations = []
                
                for j, event2 in enumerate(events[i+1:], i+1):
                    time_diff = abs((event2['timestamp'] - event1['timestamp']).total_seconds() / 60)
                    
                    if time_diff <= time_window_minutes:
                        correlations.append({
                            'event2': event2,
                            'time_difference_minutes': time_diff,
                            'platforms': [event1['source_platform'], event2['source_platform']]
                        })
                
                if correlations:
                    user_correlations[user].append({
                        'primary_event': event1,
                        'correlated_events': correlations
                    })
        
        return dict(user_correlations)
    
    def generate_unified_timeline(self):
        """Generate unified timeline across all platforms"""
        all_events = []
        
        for source_name, source_data in self.evidence_sources.items():
            for event in source_data['normalized_events']:
                all_events.append({
                    **event,
                    'platform': source_name
                })
        
        # Sort by timestamp
        unified_timeline = sorted(all_events, key=lambda x: x['timestamp'])
        
        return unified_timeline
    
    def detect_coordinated_activities(self):
        """Detect potentially coordinated activities across platforms"""
        coordinated_patterns = []
        timeline = self.generate_unified_timeline()
        
        # Look for rapid sequential activities across platforms
        for i, event in enumerate(timeline[:-2]):
            next_events = timeline[i+1:i+4]  # Look at next 3 events
            
            platforms_involved = {event['platform']}
            users_involved = {event['user']}
            time_span = 0
            
            for next_event in next_events:
                time_diff = (next_event['timestamp'] - event['timestamp']).total_seconds()
                if time_diff > 300:  # 5 minutes window
                    break
                
                platforms_involved.add(next_event['platform'])
                users_involved.add(next_event['user'])
                time_span = time_diff
            
            # Flag if multiple platforms involved in short timespan
            if len(platforms_involved) > 1 and time_span < 300:
                coordinated_patterns.append({
                    'start_time': event['timestamp'],
                    'duration_seconds': time_span,
                    'platforms': list(platforms_involved),
                    'users': list(users_involved),
                    'event_count': len(next_events) + 1
                })
        
        return coordinated_patterns
```

</div>

</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: default
---

# Practical Exercise: Mobile and Cloud Investigation

<div class="exercise-container">

## 🎯 Integrated Digital Investigation (35 minutes)

### Mission: Corporate Espionage Investigation

**"InnovaTech Solutions"** suspects a senior engineer of stealing trade secrets before joining a competitor. Your team must investigate across mobile devices and cloud platforms.

### 📱 Investigation Scope
**Evidence Sources:**
- **iPhone 13** (company device, encrypted)
- **Personal Android Samsung Galaxy** 
- **Office 365** corporate account
- **Google Drive** personal account  
- **iCloud** personal backup
- **Slack and Teams** communication logs
- **Corporate Wi-Fi** connection logs

### Phase 1: Multi-Platform Evidence Strategy (15 minutes)

**Team Assignment: Comprehensive Investigation Framework**

1. **Legal and Technical Planning**
   - Define legal authority and consent requirements for each platform
   - Plan evidence preservation procedures for volatile cloud data
   - Design systematic acquisition approach across mobile and cloud platforms
   - Create correlation methodology for cross-platform evidence

2. **Evidence Prioritization Matrix**
   - Assess volatility and importance of each evidence source
   - Plan acquisition sequence based on technical and legal constraints
   - Design backup procedures for critical evidence sources
   - Create documentation framework for multi-platform investigation

### Phase 2: Technical Acquisition and Analysis (12 minutes)

**Forensic Implementation:**
1. **Mobile Device Investigation**
   - Plan logical and physical extraction approaches for both devices
   - Design communication and location data analysis procedures
   - Create application-specific analysis for messaging, email, and file sharing
   - Plan deleted data recovery and timeline reconstruction

2. **Cloud Platform Investigation**
   - Design cloud evidence acquisition using APIs and legal process
   - Plan audit log analysis for data access and sharing activities
   - Create cross-platform user behavior analysis
   - Design data exfiltration detection methodology

### Phase 3: Evidence Correlation and Case Building (8 minutes)

**Investigation Synthesis:**
1. **Timeline Reconstruction and Pattern Analysis**
   - Correlate activities across mobile devices and cloud platforms
   - Identify data access, copying, and sharing patterns
   - Analyze communication with external parties and timing
   - Map physical location to digital activities

2. **Legal Case Preparation**
   - Document chain of custody for all evidence sources
   - Prepare technical findings for non-technical stakeholders
   - Create comprehensive investigation report with supporting evidence
   - Plan expert witness testimony and evidence presentation

**Deliverables:**
- Multi-platform forensic investigation methodology
- Evidence correlation analysis with timeline reconstruction
- Technical findings report with legal admissibility compliance
- Expert witness presentation materials and supporting documentation

</div>

<style>
.exercise-container {
  @apply bg-indigo-50 border-2 border-indigo-300 rounded-lg p-6;
}
</style>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: center
class: text-center
---

# Questions & Discussion

## 🤔 Modern Investigation Challenges:
- How do you handle encryption and privacy protection in mobile forensics?
- What are the jurisdictional challenges in cloud evidence acquisition?
- How do you correlate evidence across multiple platforms and time zones?

### 💡 Exercise Review
Present your multi-platform investigation strategies and discuss correlation methodologies

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>

---
layout: center
class: text-center
---

# Thank You!

## Next Lecture: Cyber Law and Legal Procedures
### Navigating the Legal Framework of Cybercrime

<div class="pt-8 text-gray-500">
  <p>Cyber Security (4353204) - Lecture 35 Complete</p>
  <p>Modern forensics: Investigating the connected digital world! 📱☁️</p>
</div>

<div class="absolute bottom-5 left-5 text-xs text-gray-500">
Course: Cyber Security (4353204) | Unit V | Lecture 35 | Author: Milav Dabgar
</div>