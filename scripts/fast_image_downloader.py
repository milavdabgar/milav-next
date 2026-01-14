import os
import urllib.request
import urllib.parse
import urllib.error
import re
import json
import time

# Configuration
SAVE_DIR = "content/resources/study-materials/11-ec/sem-1/4311102-funda-electronics/figures/imgs"
QUERIES = [
    "Bridge Rectifier Circuit Diagram white background",
    "Zener Diode Voltage Regulator Circuit Diagram",
    "Pi Filter Circuit Diagram",
    "NPN Transistor Current Flow Diagram",
    "LDR Construction Diagram",
    "LED Internal Structure Diagram",
    "Photodiode Structure Diagram",
    "Capacitor Types Construction Diagram",
    "Inductor Core Types Diagram",
    # Syllabus Expansion (Unit 3 - Special Diodes Structures)
    "Varactor Diode Construction Diagram",
    "Schottky Diode Structure Diagram",
    "Point Contact Crystal Diode Construction",
    # Syllabus Expansion (Unit 4 - Transistor Characteristics)
    "PNP Transistor Structure Diagram",
    "Common Emitter Input Characteristics Curve",
    "Common Emitter Output Characteristics Curve",
    # Syllabus Expansion (Unit 5 - E-waste)
    "E-waste Management Hierarchy Pyramid Diagram",
    # Syllabus Expansion (Unit 1 - Physics)
    "Faraday Law Electromagnetic Induction Experiment"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://duckduckgo.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

def get_vqd(query):
    """Get the VQD token from DuckDuckGo."""
    try:
        url = "https://duckduckgo.com/"
        data = urllib.parse.urlencode({'q': query}).encode()
        req = urllib.request.Request(url, data=data, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            search_obj = re.search(r'vqd=([\d-]+)\&', html, re.M | re.I)
            if search_obj:
                return search_obj.group(1)
    except Exception as e:
        print(f"  Error getting VQD for {query}: {e}")
    return None

def search_ddg_images(query, max_results=1):
    """Searches DuckDuckGo for images using urllib."""
    print(f"Searching: {query}...")
    vqd = get_vqd(query)
    if not vqd:
        print("  Could not initialize search.")
        return []

    params = {
        'l': 'us-en',
        'o': 'json',
        'q': query,
        'vqd': vqd,
        'f': ',,,',
        'p': '1'
    }
    url = "https://duckduckgo.com/i.js?" + urllib.parse.urlencode(params)
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return [result['image'] for result in data.get("results", [])[:max_results]]
    except Exception as e:
        print(f"  Search error: {e}")
        return []

def download_image(url, filename):
    print(f"  Downloading: {url}")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
            print(f"  Saved to {os.path.basename(filename)}")
            return True
    except Exception as e:
        print(f"  Download failed: {e}")
    return False

def main():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        
    for query in QUERIES:
        # Create a safe filename from query
        short_name = "_".join(query.split()[:3]).lower()
        filepath = os.path.join(SAVE_DIR, short_name + ".png")
        
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            print(f"Skipping {short_name} (already exists)")
            continue
            
        print(f"Processing: {query}")
        # Add a random delay to avoid rate limiting
        time.sleep(3) 
        
        urls = search_ddg_images(query)
        if urls:
            success = False
            for url in urls: 
                if download_image(url, filepath):
                    success = True
                    break
            if not success:
                print(f"  Could not download any images for {query}")
        else:
            print(f"  No results for {query}")
            
if __name__ == "__main__":
    main()
