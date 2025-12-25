---
theme: default
background: https://source.unsplash.com/1024x768/?files,data
title: File Handling Basics
info: |
  ## Java Programming (4343203)
  
  Lecture 32: File Handling Basics
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about file handling fundamentals in Java, File class operations, path manipulation, and basic file system interactions.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# File Handling Basics
## Lecture 32

**Java Programming (4343203)**  
Diploma in ICT - Semester IV  
Gujarat Technological University

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: default
---

# Learning Objectives

By the end of this lecture, you will be able to:

<v-clicks>

- 📁 **Understand** file handling concepts and importance
- 🔧 **Use** the File class for file and directory operations
- 📂 **Navigate** file systems and handle paths
- ✅ **Check** file properties and permissions
- 📝 **Create** and manipulate files and directories
- 🔍 **List** directory contents and filter files
- 🛡️ **Handle** file-related exceptions properly
- 💡 **Apply** best practices for file operations

</v-clicks>

---
layout: default
---

# Introduction to File Handling

<div class="grid grid-cols-2 gap-6">

<div>

## What is File Handling?

**File handling** refers to the operations performed on files and directories in a computer system. It includes:

- **Creating** files and directories
- **Reading** data from files
- **Writing** data to files
- **Deleting** files and directories
- **Checking** file properties
- **Navigating** directory structures

## Why File Handling is Important

### 1. **Data Persistence**
- Store data permanently on disk
- Survive program termination
- Share data between applications

### 2. **Configuration Management**
- Store application settings
- User preferences
- System configurations

### 3. **Data Processing**
- Process large datasets
- Generate reports
- Import/export data

### 4. **Logging and Debugging**
- Record application events
- Track errors and exceptions
- Monitor system behavior

## File System Structure

```
Computer File System
├── Root Directory (/ or C:\)
├── System Directories
│   ├── bin/
│   ├── lib/
│   └── etc/
├── User Directories
│   ├── Documents/
│   ├── Pictures/
│   └── Downloads/
└── Application Data
    ├── Logs/
    ├── Config/
    └── Temp/
```

</div>

<div>

## Java File Handling Overview

### Core Classes for File Handling

1. **java.io.File** - Legacy file operations
2. **java.nio.file.Path** - Modern path operations
3. **java.nio.file.Files** - Utility methods
4. **java.io.FileInputStream/FileOutputStream** - Byte streams
5. **java.io.FileReader/FileWriter** - Character streams

### File Types in Java Context

#### Text Files
```java
// Common text file extensions
.txt  - Plain text files
.csv  - Comma-separated values
.log  - Log files
.xml  - XML documents
.json - JSON data files
.properties - Configuration files
```

#### Binary Files
```java
// Common binary file extensions
.exe  - Executable files
.jpg, .png - Image files
.pdf  - PDF documents
.zip  - Compressed archives
.class - Java bytecode files
```

### File Operations Categories

#### 1. **Metadata Operations**
- Check if file exists
- Get file size
- Get creation/modification time
- Check permissions

#### 2. **Content Operations**
- Read file contents
- Write data to files
- Append data to files
- Copy file contents

#### 3. **Structure Operations**
- Create/delete files
- Create/delete directories
- Move/rename files
- List directory contents

</div>

</div>

---
layout: default
---

# The File Class

<div class="grid grid-cols-2 gap-6">

<div>

## Creating File Objects

### Basic File Creation
```java
import java.io.File;
import java.io.IOException;

public class FileBasicsDemo {
    public static void main(String[] args) {
        // Different ways to create File objects
        
        // 1. Using file path
        File file1 = new File("document.txt");
        File file2 = new File("C:\\Users\\student\\documents\\data.txt");
        File file3 = new File("/home/student/documents/data.txt");
        
        // 2. Using parent directory and file name
        File parentDir = new File("documents");
        File file4 = new File(parentDir, "report.pdf");
        
        // 3. Using parent path string and file name
        File file5 = new File("documents", "report.pdf");
        
        // 4. Platform-independent path separator
        String path = "documents" + File.separator + "data" + 
                     File.separator + "input.txt";
        File file6 = new File(path);
        
        System.out.println("File separators:");
        System.out.println("Path separator: " + File.pathSeparator);
        System.out.println("File separator: " + File.separator);
        
        // Display file information
        displayFileInfo(file1, "document.txt");
        displayFileInfo(file6, "platform-independent path");
    }
    
    private static void displayFileInfo(File file, String description) {
        System.out.println("\n" + description + ":");
        System.out.println("Absolute path: " + file.getAbsolutePath());
        System.out.println("Name: " + file.getName());
        System.out.println("Parent: " + file.getParent());
        System.out.println("Exists: " + file.exists());
    }
}
```

### Path Manipulation
```java
public class PathManipulationDemo {
    public static void main(String[] args) {
        File file = new File("documents/projects/java/MyApp.java");
        
        System.out.println("Path Analysis:");
        System.out.println("Name: " + file.getName());
        System.out.println("Parent: " + file.getParent());
        System.out.println("Absolute Path: " + file.getAbsolutePath());
        
        try {
            System.out.println("Canonical Path: " + file.getCanonicalPath());
        } catch (IOException e) {
            System.err.println("Error getting canonical path: " + e.getMessage());
        }
        
        // Extract file extension
        String fileName = file.getName();
        String extension = "";
        int dotIndex = fileName.lastIndexOf('.');
        if (dotIndex > 0) {
            extension = fileName.substring(dotIndex + 1);
        }
        System.out.println("Extension: " + extension);
        
        // Get file name without extension
        String nameWithoutExt = "";
        if (dotIndex > 0) {
            nameWithoutExt = fileName.substring(0, dotIndex);
        }
        System.out.println("Name without extension: " + nameWithoutExt);
    }
}
```

</div>

<div>

## File Properties and Metadata

### Checking File Properties
```java
import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FilePropertiesDemo {
    public static void main(String[] args) {
        // Create sample files for demonstration
        createSampleFiles();
        
        // Check different file types
        File[] testFiles = {
            new File("sample.txt"),
            new File("testDirectory"),
            new File("nonexistent.txt")
        };
        
        for (File file : testFiles) {
            analyzeFile(file);
            System.out.println("---");
        }
    }
    
    private static void createSampleFiles() {
        try {
            // Create a sample file
            File sampleFile = new File("sample.txt");
            if (!sampleFile.exists()) {
                sampleFile.createNewFile();
                System.out.println("Created sample.txt");
            }
            
            // Create a sample directory
            File sampleDir = new File("testDirectory");
            if (!sampleDir.exists()) {
                sampleDir.mkdir();
                System.out.println("Created testDirectory");
            }
            
        } catch (IOException e) {
            System.err.println("Error creating sample files: " + e.getMessage());
        }
    }
    
    private static void analyzeFile(File file) {
        System.out.println("Analyzing: " + file.getName());
        
        // Basic properties
        System.out.println("Exists: " + file.exists());
        System.out.println("Is File: " + file.isFile());
        System.out.println("Is Directory: " + file.isDirectory());
        System.out.println("Is Hidden: " + file.isHidden());
        
        if (file.exists()) {
            // Size information
            System.out.println("Size: " + file.length() + " bytes");
            System.out.println("Size: " + formatFileSize(file.length()));
            
            // Permissions
            System.out.println("Can Read: " + file.canRead());
            System.out.println("Can Write: " + file.canWrite());
            System.out.println("Can Execute: " + file.canExecute());
            
            // Timestamps
            long lastModified = file.lastModified();
            if (lastModified != 0) {
                Date date = new Date(lastModified);
                SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                System.out.println("Last Modified: " + formatter.format(date));
            }
            
            // Path information
            System.out.println("Absolute Path: " + file.getAbsolutePath());
            System.out.println("Parent Directory: " + file.getParent());
            
            try {
                System.out.println("Canonical Path: " + file.getCanonicalPath());
            } catch (IOException e) {
                System.err.println("Error getting canonical path");
            }
        }
    }
    
    private static String formatFileSize(long bytes) {
        if (bytes >= 1_073_741_824) {
            return String.format("%.2f GB", bytes / 1_073_741_824.0);
        } else if (bytes >= 1_048_576) {
            return String.format("%.2f MB", bytes / 1_048_576.0);
        } else if (bytes >= 1_024) {
            return String.format("%.2f KB", bytes / 1_024.0);
        } else {
            return bytes + " bytes";
        }
    }
}
```

</div>

</div>

---
layout: default
---

# File and Directory Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Creating Files and Directories

### File Creation
```java
import java.io.File;
import java.io.IOException;

public class FileCreationDemo {
    public static void main(String[] args) {
        createFiles();
        createDirectories();
        createComplexStructure();
    }
    
    private static void createFiles() {
        System.out.println("=== Creating Files ===");
        
        try {
            // Create a new file
            File newFile = new File("created_file.txt");
            
            if (newFile.createNewFile()) {
                System.out.println("File created: " + newFile.getName());
            } else {
                System.out.println("File already exists: " + newFile.getName());
            }
            
            // Create file in subdirectory
            File subDir = new File("output");
            if (!subDir.exists()) {
                subDir.mkdir();
            }
            
            File fileInSubDir = new File(subDir, "output_data.txt");
            if (fileInSubDir.createNewFile()) {
                System.out.println("File created: " + fileInSubDir.getPath());
            }
            
            // Create multiple files
            String[] fileNames = {"file1.txt", "file2.log", "data.csv"};
            
            for (String fileName : fileNames) {
                File file = new File("temp", fileName);
                
                // Create parent directory if it doesn't exist
                File parent = file.getParentFile();
                if (parent != null && !parent.exists()) {
                    parent.mkdirs();
                }
                
                if (file.createNewFile()) {
                    System.out.println("Created: " + file.getPath());
                }
            }
            
        } catch (IOException e) {
            System.err.println("Error creating files: " + e.getMessage());
        }
    }
    
    private static void createDirectories() {
        System.out.println("\n=== Creating Directories ===");
        
        // Create single directory
        File singleDir = new File("documents");
        if (singleDir.mkdir()) {
            System.out.println("Directory created: " + singleDir.getName());
        } else {
            System.out.println("Directory already exists or couldn't be created: " + 
                             singleDir.getName());
        }
        
        // Create nested directories
        File nestedDirs = new File("projects/java/myapp/src/main/java");
        if (nestedDirs.mkdirs()) {
            System.out.println("Nested directories created: " + nestedDirs.getPath());
        } else {
            System.out.println("Nested directories already exist: " + nestedDirs.getPath());
        }
        
        // Create directory with specific name pattern
        String timestamp = String.valueOf(System.currentTimeMillis());
        File timestampDir = new File("backup_" + timestamp);
        if (timestampDir.mkdir()) {
            System.out.println("Timestamp directory created: " + timestampDir.getName());
        }
    }
    
    private static void createComplexStructure() {
        System.out.println("\n=== Creating Complex Structure ===");
        
        String[] structure = {
            "myproject/src/main/java",
            "myproject/src/main/resources",
            "myproject/src/test/java",
            "myproject/target/classes",
            "myproject/docs",
            "myproject/lib"
        };
        
        for (String path : structure) {
            File dir = new File(path);
            if (dir.mkdirs()) {
                System.out.println("Created: " + path);
            }
            
            // Create some sample files in specific directories
            if (path.endsWith("java")) {
                try {
                    File javaFile = new File(dir, "Main.java");
                    javaFile.createNewFile();
                    System.out.println("  + Created file: " + javaFile.getPath());
                } catch (IOException e) {
                    System.err.println("Error creating Java file: " + e.getMessage());
                }
            }
        }
    }
}
```

</div>

<div>

## Directory Listing and Navigation

### Listing Directory Contents
```java
import java.io.File;
import java.io.FileFilter;
import java.util.Arrays;
import java.util.Comparator;

public class DirectoryListingDemo {
    public static void main(String[] args) {
        // List current directory
        listDirectory(".");
        
        // List specific directory
        File dir = new File("myproject");
        if (dir.exists() && dir.isDirectory()) {
            listDirectory(dir.getPath());
        }
        
        // Filter and sort listings
        filterAndSortListings();
        
        // Recursive directory listing
        recursiveDirectoryListing(new File("."), 0);
    }
    
    private static void listDirectory(String dirPath) {
        System.out.println("\n=== Listing Directory: " + dirPath + " ===");
        
        File directory = new File(dirPath);
        
        if (!directory.exists()) {
            System.out.println("Directory does not exist: " + dirPath);
            return;
        }
        
        if (!directory.isDirectory()) {
            System.out.println("Not a directory: " + dirPath);
            return;
        }
        
        // List all files and directories
        String[] entries = directory.list();
        if (entries != null) {
            System.out.println("Total entries: " + entries.length);
            
            for (String entry : entries) {
                File file = new File(directory, entry);
                String type = file.isDirectory() ? "[DIR]" : "[FILE]";
                String size = file.isFile() ? "(" + file.length() + " bytes)" : "";
                
                System.out.println(type + " " + entry + " " + size);
            }
        } else {
            System.out.println("Could not list directory contents");
        }
    }
    
    private static void filterAndSortListings() {
        System.out.println("\n=== Filtered and Sorted Listings ===");
        
        File directory = new File(".");
        
        // Filter only .java files
        File[] javaFiles = directory.listFiles(new FileFilter() {
            @Override
            public boolean accept(File file) {
                return file.isFile() && file.getName().endsWith(".java");
            }
        });
        
        if (javaFiles != null && javaFiles.length > 0) {
            System.out.println("Java files:");
            Arrays.sort(javaFiles, Comparator.comparing(File::getName));
            
            for (File file : javaFiles) {
                System.out.println("  " + file.getName() + 
                                 " (" + file.length() + " bytes)");
            }
        }
        
        // Filter directories only
        File[] directories = directory.listFiles(File::isDirectory);
        
        if (directories != null && directories.length > 0) {
            System.out.println("\nDirectories:");
            Arrays.sort(directories, Comparator.comparing(File::getName));
            
            for (File dir : directories) {
                System.out.println("  " + dir.getName() + "/");
            }
        }
        
        // Filter files larger than certain size
        File[] largeFiles = directory.listFiles(file -> 
            file.isFile() && file.length() > 1000);
        
        if (largeFiles != null && largeFiles.length > 0) {
            System.out.println("\nFiles larger than 1000 bytes:");
            Arrays.sort(largeFiles, Comparator.comparing(File::length).reversed());
            
            for (File file : largeFiles) {
                System.out.println("  " + file.getName() + 
                                 " (" + formatFileSize(file.length()) + ")");
            }
        }
    }
    
    private static void recursiveDirectoryListing(File directory, int level) {
        if (!directory.exists() || !directory.isDirectory()) {
            return;
        }
        
        // Create indentation based on level
        String indent = "  ".repeat(level);
        
        if (level == 0) {
            System.out.println("\n=== Recursive Directory Listing ===");
        }
        
        File[] entries = directory.listFiles();
        if (entries != null) {
            // Sort entries: directories first, then files
            Arrays.sort(entries, (a, b) -> {
                if (a.isDirectory() && !b.isDirectory()) return -1;
                if (!a.isDirectory() && b.isDirectory()) return 1;
                return a.getName().compareTo(b.getName());
            });
            
            for (File entry : entries) {
                if (entry.isDirectory()) {
                    System.out.println(indent + "[DIR] " + entry.getName() + "/");
                    
                    // Recursive call with increased level (limit depth to avoid infinite loops)
                    if (level < 3) {
                        recursiveDirectoryListing(entry, level + 1);
                    }
                } else {
                    System.out.println(indent + "[FILE] " + entry.getName() + 
                                     " (" + formatFileSize(entry.length()) + ")");
                }
            }
        }
    }
    
    private static String formatFileSize(long bytes) {
        if (bytes >= 1_048_576) {
            return String.format("%.2f MB", bytes / 1_048_576.0);
        } else if (bytes >= 1_024) {
            return String.format("%.2f KB", bytes / 1_024.0);
        } else {
            return bytes + " bytes";
        }
    }
}
```

</div>

</div>

---
layout: default
---

# File Deletion and Renaming

<div class="grid grid-cols-2 gap-6">

<div>

## File Deletion Operations

### Basic File Deletion
```java
import java.io.File;
import java.io.IOException;

public class FileDeletionDemo {
    public static void main(String[] args) {
        // Create test files and directories
        setupTestEnvironment();
        
        // Demonstrate different deletion scenarios
        deleteFiles();
        deleteDirectories();
        deleteRecursively();
        
        // Clean up
        cleanupTestEnvironment();
    }
    
    private static void setupTestEnvironment() {
        System.out.println("=== Setting up test environment ===");
        
        try {
            // Create test files
            new File("test1.txt").createNewFile();
            new File("test2.txt").createNewFile();
            new File("temp.log").createNewFile();
            
            // Create test directories with files
            new File("testdir").mkdir();
            new File("testdir/file1.txt").createNewFile();
            new File("testdir/file2.txt").createNewFile();
            
            new File("emptydir").mkdir();
            
            System.out.println("Test environment created");
            
        } catch (IOException e) {
            System.err.println("Error setting up test environment: " + e.getMessage());
        }
    }
    
    private static void deleteFiles() {
        System.out.println("\n=== Deleting Files ===");
        
        // Delete single file
        File fileToDelete = new File("test1.txt");
        if (fileToDelete.exists()) {
            if (fileToDelete.delete()) {
                System.out.println("Deleted: " + fileToDelete.getName());
            } else {
                System.out.println("Failed to delete: " + fileToDelete.getName());
            }
        }
        
        // Check file existence before deletion
        File anotherFile = new File("test2.txt");
        if (anotherFile.exists() && anotherFile.isFile()) {
            System.out.println("File exists: " + anotherFile.getName());
            
            if (anotherFile.delete()) {
                System.out.println("Successfully deleted: " + anotherFile.getName());
            } else {
                System.out.println("Failed to delete: " + anotherFile.getName());
            }
        }
        
        // Delete with error handling
        deleteFileWithErrorHandling("temp.log");
        deleteFileWithErrorHandling("nonexistent.txt");
    }
    
    private static void deleteFileWithErrorHandling(String fileName) {
        File file = new File(fileName);
        
        try {
            if (file.exists()) {
                // Check if file is writable
                if (!file.canWrite()) {
                    System.out.println("File is read-only: " + fileName);
                    // Try to make it writable
                    file.setWritable(true);
                }
                
                if (file.delete()) {
                    System.out.println("Deleted: " + fileName);
                } else {
                    System.out.println("Failed to delete: " + fileName);
                    System.out.println("File properties:");
                    System.out.println("  Exists: " + file.exists());
                    System.out.println("  Can Write: " + file.canWrite());
                    System.out.println("  Is File: " + file.isFile());
                }
            } else {
                System.out.println("File does not exist: " + fileName);
            }
        } catch (SecurityException e) {
            System.err.println("Security error deleting " + fileName + ": " + e.getMessage());
        }
    }
    
    private static void deleteDirectories() {
        System.out.println("\n=== Deleting Directories ===");
        
        // Delete empty directory
        File emptyDir = new File("emptydir");
        if (emptyDir.exists() && emptyDir.isDirectory()) {
            if (emptyDir.delete()) {
                System.out.println("Deleted empty directory: " + emptyDir.getName());
            } else {
                System.out.println("Failed to delete empty directory: " + emptyDir.getName());
            }
        }
        
        // Try to delete non-empty directory (will fail)
        File nonEmptyDir = new File("testdir");
        if (nonEmptyDir.exists() && nonEmptyDir.isDirectory()) {
            System.out.println("Attempting to delete non-empty directory...");
            
            if (nonEmptyDir.delete()) {
                System.out.println("Deleted non-empty directory: " + nonEmptyDir.getName());
            } else {
                System.out.println("Failed to delete non-empty directory: " + nonEmptyDir.getName());
                System.out.println("Directory contents:");
                
                String[] contents = nonEmptyDir.list();
                if (contents != null) {
                    for (String item : contents) {
                        System.out.println("  " + item);
                    }
                }
            }
        }
    }
    
    private static void deleteRecursively() {
        System.out.println("\n=== Recursive Deletion ===");
        
        File rootDir = new File("testdir");
        if (rootDir.exists()) {
            deleteDirectoryRecursively(rootDir);
        }
    }
    
    private static boolean deleteDirectoryRecursively(File directory) {
        if (!directory.exists()) {
            return true;
        }
        
        if (directory.isDirectory()) {
            File[] entries = directory.listFiles();
            
            if (entries != null) {
                for (File entry : entries) {
                    if (entry.isDirectory()) {
                        // Recursive call for subdirectories
                        System.out.println("Entering directory: " + entry.getName());
                        deleteDirectoryRecursively(entry);
                    } else {
                        // Delete file
                        System.out.println("Deleting file: " + entry.getName());
                        entry.delete();
                    }
                }
            }
        }
        
        // Delete the directory itself
        System.out.println("Deleting directory: " + directory.getName());
        return directory.delete();
    }
    
    private static void cleanupTestEnvironment() {
        System.out.println("\n=== Cleanup ===");
        
        // Clean up any remaining test files
        String[] testFiles = {"test1.txt", "test2.txt", "temp.log"};
        
        for (String fileName : testFiles) {
            File file = new File(fileName);
            if (file.exists()) {
                file.delete();
                System.out.println("Cleaned up: " + fileName);
            }
        }
    }
}
```

</div>

<div>

## File Renaming and Moving

### Renaming Operations
```java
import java.io.File;
import java.io.IOException;
import java.nio.file.*;

public class FileRenamingDemo {
    public static void main(String[] args) {
        // Create test files
        setupForRenaming();
        
        // Demonstrate renaming operations
        basicRenaming();
        renamingWithValidation();
        movingFiles();
        batchRenaming();
        
        // Cleanup
        cleanupRenaming();
    }
    
    private static void setupForRenaming() {
        System.out.println("=== Setting up files for renaming ===");
        
        try {
            // Create test files
            new File("oldname.txt").createNewFile();
            new File("document.doc").createNewFile();
            new File("image.jpg").createNewFile();
            new File("data_old.csv").createNewFile();
            
            // Create directories
            new File("source").mkdir();
            new File("destination").mkdir();
            
            new File("source/moveme.txt").createNewFile();
            
            System.out.println("Test files created for renaming demo");
            
        } catch (IOException e) {
            System.err.println("Error creating test files: " + e.getMessage());
        }
    }
    
    private static void basicRenaming() {
        System.out.println("\n=== Basic Renaming ===");
        
        File oldFile = new File("oldname.txt");
        File newFile = new File("newname.txt");
        
        if (oldFile.exists()) {
            if (oldFile.renameTo(newFile)) {
                System.out.println("Successfully renamed: " + 
                                 oldFile.getName() + " -> " + newFile.getName());
            } else {
                System.out.println("Failed to rename: " + oldFile.getName());
            }
        }
        
        // Rename with extension change
        File docFile = new File("document.doc");
        File docxFile = new File("document.docx");
        
        if (docFile.exists()) {
            if (docFile.renameTo(docxFile)) {
                System.out.println("Changed extension: " + 
                                 docFile.getName() + " -> " + docxFile.getName());
            }
        }
    }
    
    private static void renamingWithValidation() {
        System.out.println("\n=== Renaming with Validation ===");
        
        renameFileWithValidation("image.jpg", "renamed_image.jpg");
        renameFileWithValidation("nonexistent.txt", "whatever.txt");
        renameFileWithValidation("data_old.csv", "newname.txt"); // Will fail if newname.txt exists
    }
    
    private static void renameFileWithValidation(String oldName, String newName) {
        File oldFile = new File(oldName);
        File newFile = new File(newName);
        
        System.out.println("Attempting to rename: " + oldName + " -> " + newName);
        
        // Validation checks
        if (!oldFile.exists()) {
            System.out.println("  Error: Source file does not exist");
            return;
        }
        
        if (!oldFile.isFile()) {
            System.out.println("  Error: Source is not a file");
            return;
        }
        
        if (newFile.exists()) {
            System.out.println("  Warning: Destination file already exists");
            System.out.println("  Renaming will overwrite existing file");
        }
        
        if (!oldFile.canWrite()) {
            System.out.println("  Error: Cannot write to source file (permission denied)");
            return;
        }
        
        // Perform rename
        boolean success = oldFile.renameTo(newFile);
        
        if (success) {
            System.out.println("  Success: File renamed successfully");
        } else {
            System.out.println("  Error: Rename operation failed");
            
            // Additional diagnostic information
            System.out.println("  Diagnostics:");
            System.out.println("    Old file exists: " + oldFile.exists());
            System.out.println("    Old file can read: " + oldFile.canRead());
            System.out.println("    Old file can write: " + oldFile.canWrite());
            System.out.println("    New file parent exists: " + 
                             (newFile.getParentFile() == null || newFile.getParentFile().exists()));
        }
    }
    
    private static void movingFiles() {
        System.out.println("\n=== Moving Files ===");
        
        // Move file to different directory using renameTo
        File sourceFile = new File("source/moveme.txt");
        File destinationFile = new File("destination/moved_file.txt");
        
        if (sourceFile.exists()) {
            if (sourceFile.renameTo(destinationFile)) {
                System.out.println("File moved successfully: " + 
                                 sourceFile.getPath() + " -> " + destinationFile.getPath());
            } else {
                System.out.println("Failed to move file");
            }
        }
        
        // Using Java NIO for more reliable file moving
        try {
            Path sourcePath = Paths.get("data_old.csv");
            Path destinationPath = Paths.get("destination/data_new.csv");
            
            if (Files.exists(sourcePath)) {
                Files.move(sourcePath, destinationPath, StandardCopyOption.REPLACE_EXISTING);
                System.out.println("File moved using NIO: " + 
                                 sourcePath + " -> " + destinationPath);
            }
        } catch (IOException e) {
            System.err.println("Error moving file with NIO: " + e.getMessage());
        }
    }
    
    private static void batchRenaming() {
        System.out.println("\n=== Batch Renaming ===");
        
        // Create multiple test files for batch renaming
        try {
            for (int i = 1; i <= 5; i++) {
                new File("file" + i + ".tmp").createNewFile();
            }
        } catch (IOException e) {
            System.err.println("Error creating test files: " + e.getMessage());
        }
        
        // Batch rename all .tmp files to .bak files
        File currentDir = new File(".");
        File[] tmpFiles = currentDir.listFiles((dir, name) -> name.endsWith(".tmp"));
        
        if (tmpFiles != null) {
            System.out.println("Batch renaming " + tmpFiles.length + " .tmp files to .bak");
            
            for (File tmpFile : tmpFiles) {
                String newName = tmpFile.getName().replace(".tmp", ".bak");
                File newFile = new File(newName);
                
                if (tmpFile.renameTo(newFile)) {
                    System.out.println("  Renamed: " + tmpFile.getName() + " -> " + newName);
                } else {
                    System.out.println("  Failed: " + tmpFile.getName());
                }
            }
        }
    }
    
    private static void cleanupRenaming() {
        System.out.println("\n=== Cleanup ===");
        
        // Clean up all test files
        String[] testFiles = {
            "newname.txt", "document.docx", "renamed_image.jpg"
        };
        
        for (String fileName : testFiles) {
            File file = new File(fileName);
            if (file.exists()) {
                file.delete();
                System.out.println("Cleaned up: " + fileName);
            }
        }
        
        // Clean up .bak files
        File currentDir = new File(".");
        File[] bakFiles = currentDir.listFiles((dir, name) -> name.endsWith(".bak"));
        if (bakFiles != null) {
            for (File bakFile : bakFiles) {
                bakFile.delete();
                System.out.println("Cleaned up: " + bakFile.getName());
            }
        }
        
        // Clean up directories recursively
        deleteDirectoryRecursively(new File("source"));
        deleteDirectoryRecursively(new File("destination"));
    }
    
    private static boolean deleteDirectoryRecursively(File directory) {
        if (!directory.exists()) return true;
        
        if (directory.isDirectory()) {
            File[] entries = directory.listFiles();
            if (entries != null) {
                for (File entry : entries) {
                    if (entry.isDirectory()) {
                        deleteDirectoryRecursively(entry);
                    } else {
                        entry.delete();
                    }
                }
            }
        }
        
        boolean deleted = directory.delete();
        if (deleted) {
            System.out.println("Cleaned up directory: " + directory.getName());
        }
        return deleted;
    }
}
```

</div>

</div>

---
layout: default
---

# Exception Handling in File Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Common File Exceptions

### Types of File Exceptions
```java
import java.io.*;
import java.nio.file.AccessDeniedException;

public class FileExceptionHandlingDemo {
    public static void main(String[] args) {
        demonstrateCommonExceptions();
        properExceptionHandling();
        multipleExceptionHandling();
    }
    
    private static void demonstrateCommonExceptions() {
        System.out.println("=== Common File Exceptions ===");
        
        // 1. FileNotFoundException
        try {
            FileInputStream fis = new FileInputStream("nonexistent_file.txt");
        } catch (FileNotFoundException e) {
            System.out.println("FileNotFoundException: " + e.getMessage());
        }
        
        // 2. SecurityException
        try {
            File restrictedFile = new File("/root/restricted.txt");
            // This might throw SecurityException on some systems
            restrictedFile.createNewFile();
        } catch (SecurityException e) {
            System.out.println("SecurityException: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IOException during restricted file creation: " + e.getMessage());
        }
        
        // 3. IOException during file operations
        try {
            createAndAccessFile();
        } catch (IOException e) {
            System.out.println("IOException: " + e.getMessage());
        }
    }
    
    private static void createAndAccessFile() throws IOException {
        File tempFile = File.createTempFile("demo", ".tmp");
        tempFile.deleteOnExit();
        
        // Simulate various IO operations that might fail
        try (FileWriter writer = new FileWriter(tempFile)) {
            writer.write("Test content");
            writer.flush();
            
            // Force an exception by trying to write after closing
            writer.close();
            writer.write("This will fail"); // IOException
        }
    }
    
    private static void properExceptionHandling() {
        System.out.println("\n=== Proper Exception Handling ===");
        
        String fileName = "test_file.txt";
        
        // Method 1: Try-catch with specific exceptions
        try {
            File file = new File(fileName);
            
            // Check if file can be created
            if (!file.exists()) {
                boolean created = file.createNewFile();
                if (created) {
                    System.out.println("File created successfully: " + fileName);
                } else {
                    System.out.println("Failed to create file: " + fileName);
                }
            }
            
            // Check permissions before operations
            if (!file.canRead()) {
                throw new IOException("Cannot read file: " + fileName);
            }
            
            if (!file.canWrite()) {
                throw new IOException("Cannot write to file: " + fileName);
            }
            
            System.out.println("File operations completed successfully");
            
        } catch (SecurityException e) {
            System.err.println("Security error: " + e.getMessage());
            System.err.println("Check file permissions and security policy");
        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
            System.err.println("Check file path and disk space");
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    private static void multipleExceptionHandling() {
        System.out.println("\n=== Multiple Exception Handling ===");
        
        performFileOperations("valid_file.txt");
        performFileOperations("C:/invalid/path/file.txt");
        performFileOperations("");
    }
    
    private static void performFileOperations(String fileName) {
        System.out.println("Processing file: " + fileName);
        
        if (fileName == null || fileName.trim().isEmpty()) {
            System.err.println("Error: Invalid file name");
            return;
        }
        
        File file = null;
        FileWriter writer = null;
        
        try {
            file = new File(fileName);
            
            // Create parent directories if they don't exist
            File parentDir = file.getParentFile();
            if (parentDir != null && !parentDir.exists()) {
                boolean dirsCreated = parentDir.mkdirs();
                if (!dirsCreated) {
                    throw new IOException("Could not create parent directories for: " + fileName);
                }
            }
            
            // Create file if it doesn't exist
            if (!file.exists()) {
                boolean fileCreated = file.createNewFile();
                if (!fileCreated) {
                    throw new IOException("Could not create file: " + fileName);
                }
            }
            
            // Write some content
            writer = new FileWriter(file, true); // Append mode
            writer.write("Sample content written at: " + new java.util.Date() + "\n");
            writer.flush();
            
            System.out.println("Successfully processed: " + fileName);
            
        } catch (SecurityException e) {
            System.err.println("Security Exception for " + fileName + ": " + e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.println("File Not Found for " + fileName + ": " + e.getMessage());
        } catch (IOException e) {
            System.err.println("IO Exception for " + fileName + ": " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Unexpected Exception for " + fileName + ": " + e.getMessage());
        } finally {
            // Cleanup resources
            if (writer != null) {
                try {
                    writer.close();
                } catch (IOException e) {
                    System.err.println("Error closing writer: " + e.getMessage());
                }
            }
            
            // Clean up test file
            if (file != null && file.exists() && file.getName().equals("valid_file.txt")) {
                if (file.delete()) {
                    System.out.println("Cleaned up test file: " + file.getName());
                }
            }
        }
    }
}
```

</div>

<div>

## Best Practices for Exception Handling

### Robust File Operations
```java
import java.io.*;
import java.nio.file.*;
import java.util.logging.*;

public class RobustFileOperations {
    private static final Logger logger = Logger.getLogger(RobustFileOperations.class.getName());
    
    public static void main(String[] args) {
        // Setup logging
        setupLogging();
        
        // Demonstrate robust file operations
        safeFileCreation("documents/reports/quarterly_report.txt");
        safeFileReading("config.properties");
        safeFileWriting("output/results.txt", "Sample data");
        safeBatchOperations();
    }
    
    private static void setupLogging() {
        Logger rootLogger = Logger.getLogger("");
        Handler consoleHandler = new ConsoleHandler();
        consoleHandler.setLevel(Level.ALL);
        rootLogger.addHandler(consoleHandler);
        rootLogger.setLevel(Level.INFO);
    }
    
    public static boolean safeFileCreation(String filePath) {
        logger.info("Attempting to create file: " + filePath);
        
        if (filePath == null || filePath.trim().isEmpty()) {
            logger.warning("Invalid file path provided: " + filePath);
            return false;
        }
        
        try {
            Path path = Paths.get(filePath);
            
            // Create parent directories if they don't exist
            Path parentDir = path.getParent();
            if (parentDir != null) {
                Files.createDirectories(parentDir);
                logger.info("Created parent directories: " + parentDir);
            }
            
            // Create file if it doesn't exist
            if (!Files.exists(path)) {
                Files.createFile(path);
                logger.info("File created successfully: " + filePath);
                return true;
            } else {
                logger.info("File already exists: " + filePath);
                return true;
            }
            
        } catch (InvalidPathException e) {
            logger.severe("Invalid path: " + filePath + " - " + e.getMessage());
            return false;
        } catch (FileAlreadyExistsException e) {
            logger.info("File already exists: " + filePath);
            return true;
        } catch (NoSuchFileException e) {
            logger.severe("Parent directory does not exist: " + e.getMessage());
            return false;
        } catch (AccessDeniedException e) {
            logger.severe("Access denied: " + e.getMessage());
            return false;
        } catch (IOException e) {
            logger.severe("IO error creating file " + filePath + ": " + e.getMessage());
            return false;
        } catch (SecurityException e) {
            logger.severe("Security error: " + e.getMessage());
            return false;
        }
    }
    
    public static String safeFileReading(String filePath) {
        logger.info("Attempting to read file: " + filePath);
        
        if (filePath == null || filePath.trim().isEmpty()) {
            logger.warning("Invalid file path for reading: " + filePath);
            return null;
        }
        
        BufferedReader reader = null;
        StringBuilder content = new StringBuilder();
        
        try {
            File file = new File(filePath);
            
            // Validate file before reading
            if (!file.exists()) {
                logger.warning("File does not exist: " + filePath);
                return null;
            }
            
            if (!file.isFile()) {
                logger.warning("Path is not a file: " + filePath);
                return null;
            }
            
            if (!file.canRead()) {
                logger.warning("Cannot read file (permission denied): " + filePath);
                return null;
            }
            
            // Check file size to prevent memory issues
            long fileSize = file.length();
            if (fileSize > 10 * 1024 * 1024) { // 10MB limit
                logger.warning("File too large to read: " + fileSize + " bytes");
                return null;
            }
            
            reader = new BufferedReader(new FileReader(file));
            String line;
            
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            
            logger.info("File read successfully: " + filePath + 
                       " (" + fileSize + " bytes)");
            return content.toString();
            
        } catch (FileNotFoundException e) {
            logger.severe("File not found: " + filePath);
            return null;
        } catch (IOException e) {
            logger.severe("IO error reading file " + filePath + ": " + e.getMessage());
            return null;
        } catch (SecurityException e) {
            logger.severe("Security error reading file " + filePath + ": " + e.getMessage());
            return null;
        } catch (OutOfMemoryError e) {
            logger.severe("Out of memory reading file " + filePath + ": " + e.getMessage());
            return null;
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    logger.warning("Error closing reader: " + e.getMessage());
                }
            }
        }
    }
    
    public static boolean safeFileWriting(String filePath, String content) {
        logger.info("Attempting to write to file: " + filePath);
        
        if (filePath == null || filePath.trim().isEmpty()) {
            logger.warning("Invalid file path for writing: " + filePath);
            return false;
        }
        
        if (content == null) {
            content = ""; // Allow writing empty content
        }
        
        // Create backup if file exists
        File file = new File(filePath);
        File backupFile = null;
        
        if (file.exists()) {
            backupFile = new File(filePath + ".backup");
            try {
                Files.copy(file.toPath(), backupFile.toPath(), 
                          StandardCopyOption.REPLACE_EXISTING);
                logger.info("Created backup: " + backupFile.getName());
            } catch (IOException e) {
                logger.warning("Could not create backup: " + e.getMessage());
            }
        }
        
        BufferedWriter writer = null;
        
        try {
            // Ensure parent directory exists
            File parentDir = file.getParentFile();
            if (parentDir != null && !parentDir.exists()) {
                boolean created = parentDir.mkdirs();
                if (!created) {
                    throw new IOException("Could not create parent directories");
                }
            }
            
            writer = new BufferedWriter(new FileWriter(file));
            writer.write(content);
            writer.flush();
            
            logger.info("File written successfully: " + filePath + 
                       " (" + content.length() + " characters)");
            
            // Remove backup if write was successful
            if (backupFile != null && backupFile.exists()) {
                backupFile.delete();
                logger.info("Backup file removed after successful write");
            }
            
            return true;
            
        } catch (IOException e) {
            logger.severe("IO error writing file " + filePath + ": " + e.getMessage());
            
            // Restore backup if available
            if (backupFile != null && backupFile.exists()) {
                try {
                    Files.move(backupFile.toPath(), file.toPath(), 
                              StandardCopyOption.REPLACE_EXISTING);
                    logger.info("Restored backup after write failure");
                } catch (IOException restoreError) {
                    logger.severe("Could not restore backup: " + restoreError.getMessage());
                }
            }
            
            return false;
        } catch (SecurityException e) {
            logger.severe("Security error writing file " + filePath + ": " + e.getMessage());
            return false;
        } finally {
            if (writer != null) {
                try {
                    writer.close();
                } catch (IOException e) {
                    logger.warning("Error closing writer: " + e.getMessage());
                }
            }
        }
    }
    
    private static void safeBatchOperations() {
        logger.info("Performing safe batch operations");
        
        String[] testFiles = {
            "batch/file1.txt",
            "batch/file2.txt", 
            "batch/file3.txt"
        };
        
        int successCount = 0;
        int failureCount = 0;
        
        for (String filePath : testFiles) {
            boolean created = safeFileCreation(filePath);
            
            if (created) {
                boolean written = safeFileWriting(filePath, 
                    "Content for " + filePath + "\nCreated at: " + new java.util.Date());
                
                if (written) {
                    successCount++;
                    logger.info("Batch operation successful for: " + filePath);
                } else {
                    failureCount++;
                    logger.warning("Write failed for: " + filePath);
                }
            } else {
                failureCount++;
                logger.warning("Creation failed for: " + filePath);
            }
        }
        
        logger.info("Batch operations completed. Success: " + successCount + 
                   ", Failures: " + failureCount);
        
        // Cleanup
        cleanup();
    }
    
    private static void cleanup() {
        logger.info("Starting cleanup");
        
        try {
            // Clean up test files
            Files.deleteIfExists(Paths.get("documents/reports/quarterly_report.txt"));
            Files.deleteIfExists(Paths.get("documents/reports"));
            Files.deleteIfExists(Paths.get("documents"));
            Files.deleteIfExists(Paths.get("output/results.txt"));
            Files.deleteIfExists(Paths.get("output"));
            
            // Clean up batch files
            String[] batchFiles = {"batch/file1.txt", "batch/file2.txt", "batch/file3.txt"};
            for (String file : batchFiles) {
                Files.deleteIfExists(Paths.get(file));
            }
            Files.deleteIfExists(Paths.get("batch"));
            
            logger.info("Cleanup completed");
            
        } catch (IOException e) {
            logger.warning("Error during cleanup: " + e.getMessage());
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise: File Explorer

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build Simple File Explorer
Create a console-based file explorer with comprehensive file management capabilities:

```java
// TODO: Implement File Explorer Menu System
public class SimpleFileExplorer {
    private File currentDirectory;
    private Scanner scanner;
    
    public SimpleFileExplorer() {
        // Initialize with current directory
        // Setup scanner for user input
    }
    
    public void start() {
        // Main program loop
        // Display menu and handle user commands
    }
    
    private void displayMenu() {
        // Show available commands:
        // 1. List files and directories
        // 2. Change directory
        // 3. Create file
        // 4. Create directory
        // 5. Delete file/directory
        // 6. Rename file/directory
        // 7. Show file properties
        // 8. Search files
        // 9. Exit
    }
    
    private void listContents() {
        // List current directory contents with details
        // Show file sizes, dates, permissions
    }
    
    private void changeDirectory(String path) {
        // Navigate to specified directory
        // Handle relative and absolute paths
    }
    
    private void createFile(String fileName) {
        // Create new file with validation
    }
    
    private void createDirectory(String dirName) {
        // Create new directory with validation
    }
    
    private void deleteFileOrDirectory(String name) {
        // Delete file or directory with confirmation
        // Handle recursive deletion for directories
    }
    
    private void renameFileOrDirectory(String oldName, String newName) {
        // Rename file or directory with validation
    }
    
    private void showProperties(String fileName) {
        // Display comprehensive file properties
    }
    
    private void searchFiles(String pattern) {
        // Search for files matching pattern
        // Support wildcard matching
    }
}

// TODO: Implement main class
public class FileExplorerApp {
    public static void main(String[] args) {
        SimpleFileExplorer explorer = new SimpleFileExplorer();
        explorer.start();
    }
}
```

**Requirements:**
- Interactive menu system
- Robust error handling
- Support for both files and directories
- File property display (size, dates, permissions)
- Search functionality with pattern matching
- Confirmation for destructive operations
- Navigation history (bonus)
- Cross-platform compatibility

</div>

<div>

## Solution Framework

```java
import java.io.*;
import java.text.SimpleDateFormat;
import java.util.*;

public class SimpleFileExplorer {
    private File currentDirectory;
    private Scanner scanner;
    private Stack<File> navigationHistory;
    private SimpleDateFormat dateFormat;
    
    public SimpleFileExplorer() {
        this.currentDirectory = new File(System.getProperty("user.dir"));
        this.scanner = new Scanner(System.in);
        this.navigationHistory = new Stack<>();
        this.dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    }
    
    public void start() {
        System.out.println("=== Simple File Explorer ===");
        System.out.println("Starting in: " + currentDirectory.getAbsolutePath());
        
        while (true) {
            displayCurrentLocation();
            displayMenu();
            
            System.out.print("Enter command: ");
            String input = scanner.nextLine().trim();
            
            if (input.isEmpty()) {
                continue;
            }
            
            String[] parts = input.split("\\s+", 2);
            String command = parts[0].toLowerCase();
            String argument = parts.length > 1 ? parts[1] : "";
            
            try {
                switch (command) {
                    case "1":
                    case "ls":
                    case "list":
                        listContents();
                        break;
                    case "2":
                    case "cd":
                        changeDirectory(argument);
                        break;
                    case "3":
                    case "touch":
                        createFile(argument);
                        break;
                    case "4":
                    case "mkdir":
                        createDirectory(argument);
                        break;
                    case "5":
                    case "rm":
                        deleteFileOrDirectory(argument);
                        break;
                    case "6":
                    case "mv":
                        handleRename(argument);
                        break;
                    case "7":
                    case "info":
                        showProperties(argument);
                        break;
                    case "8":
                    case "find":
                        searchFiles(argument);
                        break;
                    case "9":
                    case "exit":
                    case "quit":
                        System.out.println("Goodbye!");
                        return;
                    case "back":
                        goBack();
                        break;
                    case "help":
                        displayHelp();
                        break;
                    default:
                        System.out.println("Unknown command: " + command);
                        System.out.println("Type 'help' for available commands.");
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
            }
            
            System.out.println(); // Empty line for readability
        }
    }
    
    private void displayCurrentLocation() {
        System.out.println("\nCurrent Directory: " + currentDirectory.getAbsolutePath());
    }
    
    private void displayMenu() {
        System.out.println("Commands:");
        System.out.println("1/ls   - List files and directories");
        System.out.println("2/cd   - Change directory");
        System.out.println("3/touch- Create file");
        System.out.println("4/mkdir- Create directory");
        System.out.println("5/rm   - Delete file/directory");
        System.out.println("6/mv   - Rename file/directory");
        System.out.println("7/info - Show file properties");
        System.out.println("8/find - Search files");
        System.out.println("9/exit - Exit explorer");
        System.out.println("back   - Go back to previous directory");
        System.out.println("help   - Show detailed help");
    }
    
    private void listContents() {
        File[] entries = currentDirectory.listFiles();
        
        if (entries == null) {
            System.out.println("Cannot access directory contents");
            return;
        }
        
        if (entries.length == 0) {
            System.out.println("Directory is empty");
            return;
        }
        
        // Sort entries: directories first, then files
        Arrays.sort(entries, (a, b) -> {
            if (a.isDirectory() && !b.isDirectory()) return -1;
            if (!a.isDirectory() && b.isDirectory()) return 1;
            return a.getName().compareToIgnoreCase(b.getName());
        });
        
        System.out.printf("%-20s %-10s %-15s %-20s%n", 
                         "Name", "Type", "Size", "Modified");
        System.out.println("-".repeat(70));
        
        for (File entry : entries) {
            String name = entry.getName();
            String type = entry.isDirectory() ? "[DIR]" : "[FILE]";
            String size = entry.isDirectory() ? "-" : formatFileSize(entry.length());
            String modified = dateFormat.format(new Date(entry.lastModified()));
            
            System.out.printf("%-20s %-10s %-15s %-20s%n", 
                             name, type, size, modified);
        }
        
        System.out.println("\nTotal: " + entries.length + " items");
    }
    
    private void changeDirectory(String path) {
        if (path.isEmpty()) {
            System.out.println("Please specify directory path");
            return;
        }
        
        File targetDir;
        
        if (path.equals("..")) {
            targetDir = currentDirectory.getParentFile();
        } else if (path.equals(".")) {
            return; // Stay in current directory
        } else if (path.equals("~")) {
            targetDir = new File(System.getProperty("user.home"));
        } else {
            targetDir = new File(path);
            if (!targetDir.isAbsolute()) {
                targetDir = new File(currentDirectory, path);
            }
        }
        
        if (targetDir == null) {
            System.out.println("Cannot go up from root directory");
            return;
        }
        
        if (!targetDir.exists()) {
            System.out.println("Directory does not exist: " + path);
            return;
        }
        
        if (!targetDir.isDirectory()) {
            System.out.println("Not a directory: " + path);
            return;
        }
        
        if (!targetDir.canRead()) {
            System.out.println("Cannot access directory: " + path);
            return;
        }
        
        // Save current directory to history
        navigationHistory.push(currentDirectory);
        currentDirectory = targetDir;
        
        System.out.println("Changed to: " + currentDirectory.getAbsolutePath());
    }
    
    private void createFile(String fileName) {
        if (fileName.isEmpty()) {
            System.out.print("Enter file name: ");
            fileName = scanner.nextLine().trim();
        }
        
        if (fileName.isEmpty()) {
            System.out.println("File name cannot be empty");
            return;
        }
        
        File newFile = new File(currentDirectory, fileName);
        
        if (newFile.exists()) {
            System.out.println("File already exists: " + fileName);
            return;
        }
        
        try {
            if (newFile.createNewFile()) {
                System.out.println("File created successfully: " + fileName);
            } else {
                System.out.println("Failed to create file: " + fileName);
            }
        } catch (IOException e) {
            System.err.println("Error creating file: " + e.getMessage());
        }
    }
    
    private void createDirectory(String dirName) {
        if (dirName.isEmpty()) {
            System.out.print("Enter directory name: ");
            dirName = scanner.nextLine().trim();
        }
        
        if (dirName.isEmpty()) {
            System.out.println("Directory name cannot be empty");
            return;
        }
        
        File newDir = new File(currentDirectory, dirName);
        
        if (newDir.exists()) {
            System.out.println("Directory already exists: " + dirName);
            return;
        }
        
        if (newDir.mkdir()) {
            System.out.println("Directory created successfully: " + dirName);
        } else {
            System.out.println("Failed to create directory: " + dirName);
        }
    }
    
    private void deleteFileOrDirectory(String name) {
        if (name.isEmpty()) {
            System.out.print("Enter file/directory name to delete: ");
            name = scanner.nextLine().trim();
        }
        
        if (name.isEmpty()) {
            System.out.println("Name cannot be empty");
            return;
        }
        
        File target = new File(currentDirectory, name);
        
        if (!target.exists()) {
            System.out.println("File/directory does not exist: " + name);
            return;
        }
        
        // Confirmation
        System.out.print("Are you sure you want to delete '" + name + "'? (y/N): ");
        String confirmation = scanner.nextLine().trim().toLowerCase();
        
        if (!confirmation.equals("y") && !confirmation.equals("yes")) {
            System.out.println("Deletion cancelled");
            return;
        }
        
        if (target.isDirectory()) {
            if (deleteDirectoryRecursively(target)) {
                System.out.println("Directory deleted successfully: " + name);
            } else {
                System.out.println("Failed to delete directory: " + name);
            }
        } else {
            if (target.delete()) {
                System.out.println("File deleted successfully: " + name);
            } else {
                System.out.println("Failed to delete file: " + name);
            }
        }
    }
    
    private void handleRename(String argument) {
        String[] parts = argument.split("\\s+", 2);
        String oldName = parts.length > 0 ? parts[0] : "";
        String newName = parts.length > 1 ? parts[1] : "";
        
        if (oldName.isEmpty()) {
            System.out.print("Enter current name: ");
            oldName = scanner.nextLine().trim();
        }
        
        if (newName.isEmpty()) {
            System.out.print("Enter new name: ");
            newName = scanner.nextLine().trim();
        }
        
        renameFileOrDirectory(oldName, newName);
    }
    
    private void renameFileOrDirectory(String oldName, String newName) {
        if (oldName.isEmpty() || newName.isEmpty()) {
            System.out.println("Both old and new names are required");
            return;
        }
        
        File oldFile = new File(currentDirectory, oldName);
        File newFile = new File(currentDirectory, newName);
        
        if (!oldFile.exists()) {
            System.out.println("File/directory does not exist: " + oldName);
            return;
        }
        
        if (newFile.exists()) {
            System.out.println("Target name already exists: " + newName);
            return;
        }
        
        if (oldFile.renameTo(newFile)) {
            System.out.println("Renamed successfully: " + oldName + " -> " + newName);
        } else {
            System.out.println("Failed to rename: " + oldName);
        }
    }
    
    private void showProperties(String fileName) {
        if (fileName.isEmpty()) {
            System.out.print("Enter file/directory name: ");
            fileName = scanner.nextLine().trim();
        }
        
        if (fileName.isEmpty()) {
            System.out.println("Name cannot be empty");
            return;
        }
        
        File file = new File(currentDirectory, fileName);
        
        if (!file.exists()) {
            System.out.println("File/directory does not exist: " + fileName);
            return;
        }
        
        System.out.println("=== Properties of " + fileName + " ===");
        System.out.println("Name: " + file.getName());
        System.out.println("Type: " + (file.isDirectory() ? "Directory" : "File"));
        System.out.println("Size: " + formatFileSize(file.length()));
        System.out.println("Location: " + file.getAbsolutePath());
        System.out.println("Parent: " + file.getParent());
        System.out.println("Hidden: " + file.isHidden());
        System.out.println("Can Read: " + file.canRead());
        System.out.println("Can Write: " + file.canWrite());
        System.out.println("Can Execute: " + file.canExecute());
        System.out.println("Last Modified: " + dateFormat.format(new Date(file.lastModified())));
        
        if (file.isDirectory()) {
            File[] contents = file.listFiles();
            int itemCount = contents != null ? contents.length : 0;
            System.out.println("Contains: " + itemCount + " items");
        }
    }
    
    private void searchFiles(String pattern) {
        if (pattern.isEmpty()) {
            System.out.print("Enter search pattern (wildcards * and ? supported): ");
            pattern = scanner.nextLine().trim();
        }
        
        if (pattern.isEmpty()) {
            System.out.println("Search pattern cannot be empty");
            return;
        }
        
        System.out.println("Searching for: " + pattern);
        List<File> results = new ArrayList<>();
        searchRecursively(currentDirectory, pattern, results);
        
        if (results.isEmpty()) {
            System.out.println("No files found matching pattern: " + pattern);
        } else {
            System.out.println("Found " + results.size() + " matching files:");
            for (File result : results) {
                String relativePath = getRelativePath(result);
                String type = result.isDirectory() ? "[DIR]" : "[FILE]";
                System.out.println(type + " " + relativePath);
            }
        }
    }
    
    private void searchRecursively(File directory, String pattern, List<File> results) {
        File[] entries = directory.listFiles();
        if (entries == null) return;
        
        for (File entry : entries) {
            if (matchesPattern(entry.getName(), pattern)) {
                results.add(entry);
            }
            
            if (entry.isDirectory()) {
                searchRecursively(entry, pattern, results);
            }
        }
    }
    
    private boolean matchesPattern(String fileName, String pattern) {
        // Simple wildcard matching
        pattern = pattern.replace("*", ".*").replace("?", ".");
        return fileName.matches(pattern);
    }
    
    private String getRelativePath(File file) {
        String currentPath = currentDirectory.getAbsolutePath();
        String filePath = file.getAbsolutePath();
        
        if (filePath.startsWith(currentPath)) {
            return filePath.substring(currentPath.length() + 1);
        }
        return filePath;
    }
    
    private void goBack() {
        if (navigationHistory.isEmpty()) {
            System.out.println("No previous directory in history");
            return;
        }
        
        currentDirectory = navigationHistory.pop();
        System.out.println("Returned to: " + currentDirectory.getAbsolutePath());
    }
    
    private void displayHelp() {
        System.out.println("=== Detailed Help ===");
        System.out.println("Navigation:");
        System.out.println("  cd <path>  - Change to directory (use .. for parent, ~ for home)");
        System.out.println("  back       - Go to previous directory");
        System.out.println("  ls         - List current directory contents");
        System.out.println();
        System.out.println("File Operations:");
        System.out.println("  touch <name>    - Create new file");
        System.out.println("  mkdir <name>    - Create new directory");
        System.out.println("  rm <name>       - Delete file or directory");
        System.out.println("  mv <old> <new>  - Rename file or directory");
        System.out.println();
        System.out.println("Information:");
        System.out.println("  info <name>     - Show detailed file properties");
        System.out.println("  find <pattern>  - Search files (supports * and ? wildcards)");
        System.out.println();
        System.out.println("Other:");
        System.out.println("  help            - Show this help");
        System.out.println("  exit            - Exit file explorer");
    }
    
    private boolean deleteDirectoryRecursively(File directory) {
        File[] entries = directory.listFiles();
        if (entries != null) {
            for (File entry : entries) {
                if (entry.isDirectory()) {
                    deleteDirectoryRecursively(entry);
                } else {
                    entry.delete();
                }
            }
        }
        return directory.delete();
    }
    
    private String formatFileSize(long bytes) {
        if (bytes >= 1_073_741_824) {
            return String.format("%.2f GB", bytes / 1_073_741_824.0);
        } else if (bytes >= 1_048_576) {
            return String.format("%.2f MB", bytes / 1_048_576.0);
        } else if (bytes >= 1_024) {
            return String.format("%.2f KB", bytes / 1_024.0);
        } else {
            return bytes + " bytes";
        }
    }
}

public class FileExplorerApp {
    public static void main(String[] args) {
        SimpleFileExplorer explorer = new SimpleFileExplorer();
        explorer.start();
    }
}
```

</div>

</div>

---
layout: default
---

# Summary and Key Takeaways

<div class="grid grid-cols-2 gap-6">

<div>

## What We Learned

<v-clicks>

- 📁 **File Handling Basics**: Understanding files, directories, and file systems
- 🔧 **File Class Operations**: Creating File objects and basic operations
- 📂 **Path Manipulation**: Working with file paths and directories
- ✅ **File Properties**: Checking existence, permissions, size, and timestamps
- 📝 **File Operations**: Creating, deleting, renaming files and directories
- 🔍 **Directory Navigation**: Listing contents, filtering, and recursive operations
- 🛡️ **Exception Handling**: Proper error handling for file operations
- 💡 **Best Practices**: Robust file handling techniques

</v-clicks>

## Key File Operations

### File Creation and Manipulation
```java
// Create file
File file = new File("path/to/file.txt");
file.createNewFile();

// Create directories
File dir = new File("path/to/directory");
dir.mkdirs(); // Creates parent directories too

// Check properties
boolean exists = file.exists();
boolean isFile = file.isFile();
long size = file.length();
```

### Directory Operations
```java
// List directory contents
File dir = new File(".");
String[] entries = dir.list();
File[] files = dir.listFiles();

// Filter files
File[] txtFiles = dir.listFiles(
    (dir, name) -> name.endsWith(".txt"));
```

</div>

<div>

## Important Concepts Recap

<v-clicks>

- **File vs Directory**: Different types of file system entries
- **Absolute vs Relative Paths**: Different ways to specify locations
- **File Permissions**: Read, write, execute permissions
- **File Metadata**: Size, timestamps, hidden status
- **Exception Handling**: FileNotFoundException, IOException, SecurityException
- **Platform Independence**: Using File.separator for cross-platform code
- **Resource Management**: Proper cleanup and error handling

</v-clicks>

## Common File Operations Patterns

### Safe File Creation
```java
try {
    File file = new File("data.txt");
    if (!file.exists()) {
        file.createNewFile();
    }
} catch (IOException e) {
    System.err.println("Error: " + e.getMessage());
}
```

### Directory Traversal
```java
public void listRecursively(File dir, int level) {
    File[] entries = dir.listFiles();
    if (entries != null) {
        for (File entry : entries) {
            System.out.println("  ".repeat(level) + entry.getName());
            if (entry.isDirectory()) {
                listRecursively(entry, level + 1);
            }
        }
    }
}
```

## Best Practices Summary

1. **Always check file existence before operations**
2. **Handle exceptions properly with specific catch blocks**
3. **Use platform-independent path separators**
4. **Validate user input for file names and paths**
5. **Create parent directories when needed**
6. **Clean up resources in finally blocks**
7. **Provide meaningful error messages**
8. **Use confirmation for destructive operations**

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## File Handling Basics Complete

**Lecture 32 Successfully Completed!**  
You now understand the fundamentals of file handling in Java

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for advanced file I/O operations! <carbon:arrow-right class="inline"/>
  </span>
</div>