#!/bin/bash

# Script to remove LaTeX auxiliary/residual files and Typora PDFs recursively
# Preserves .tex and .pdf files (except Typora-generated PDFs)

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Target directory
TARGET_DIR="content/resources/study-materials"

# Check if directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Error: Directory '$TARGET_DIR' not found!${NC}"
    exit 1
fi

echo -e "${YELLOW}Cleaning LaTeX auxiliary files from: $TARGET_DIR${NC}"
echo ""

# Array of file extensions to remove
EXTENSIONS=(
    "aux"
    "log"
    "toc"
    "out"
    "fdb_latexmk"
    "fls"
    "synctex.gz"
    "bbl"
    "blg"
    "idx"
    "ind"
    "ilg"
    "lof"
    "lot"
    "nav"
    "snm"
    "vrb"
    "bcf"
    "run.xml"
    "xdv"
)

# Counter for deleted files
total_deleted=0

# Loop through each extension and delete files
for ext in "${EXTENSIONS[@]}"; do
    echo -e "${YELLOW}Searching for *.${ext} files...${NC}"
    
    # Find and count files with this extension
    count=$(find "$TARGET_DIR" -type f -name "*.${ext}" 2>/dev/null | wc -l | tr -d ' ')
    
    if [ "$count" -gt 0 ]; then
        echo -e "${GREEN}Found $count *.${ext} file(s)${NC}"
        
        # Delete the files
        find "$TARGET_DIR" -type f -name "*.${ext}" -delete
        
        total_deleted=$((total_deleted + count))
    fi
done

echo ""
echo -e "${YELLOW}Cleaning Typora-generated PDF files...${NC}"
echo ""

# Remove Typora PDF files
typora_patterns=(
    "*-solution-typora.pdf"
    "*-solution-typora.gu.pdf"
)

for pattern in "${typora_patterns[@]}"; do
    echo -e "${YELLOW}Searching for $pattern files...${NC}"
    
    # Find and count files with this pattern
    count=$(find "$TARGET_DIR" -type f -name "$pattern" 2>/dev/null | wc -l | tr -d ' ')
    
    if [ "$count" -gt 0 ]; then
        echo -e "${GREEN}Found $count $pattern file(s)${NC}"
        
        # Delete the files
        find "$TARGET_DIR" -type f -name "$pattern" -delete
        
        total_deleted=$((total_deleted + count))
    fi
done

echo ""
echo -e "${GREEN}✓ Cleanup complete!${NC}"
echo -e "${GREEN}Total files deleted: $total_deleted${NC}"
echo ""
echo -e "${YELLOW}Note: LaTeX source (.tex) and compiled PDFs (.pdf) have been preserved.${NC}"
echo -e "${YELLOW}      Only auxiliary files and Typora-generated PDFs were removed.${NC}"

