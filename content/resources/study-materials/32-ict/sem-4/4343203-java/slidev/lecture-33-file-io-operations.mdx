---
theme: default
background: https://source.unsplash.com/1024x768/?data,stream
title: File I/O Operations
info: |
  ## Java Programming (4343203)
  
  Lecture 33: File I/O Operations
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about file input/output operations in Java including byte streams, character streams, buffered I/O, and advanced file processing techniques.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# File I/O Operations
## Lecture 33

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

- 📚 **Understand** Java I/O stream hierarchy and types
- 🔤 **Differentiate** between byte streams and character streams
- 📖 **Read** data from files using various input streams
- ✍️ **Write** data to files using various output streams
- ⚡ **Implement** buffered I/O for improved performance
- 📝 **Handle** text files and binary files appropriately
- 🔧 **Use** modern Java NIO for advanced file operations
- 🛡️ **Apply** try-with-resources for proper resource management

</v-clicks>

---
layout: default
---

# Java I/O Stream Hierarchy

<div class="grid grid-cols-2 gap-6">

<div>

## Stream Types Overview

### Byte Streams (Binary Data)
- **InputStream** - Abstract base class for reading bytes
- **OutputStream** - Abstract base class for writing bytes
- Handle 8-bit data (binary files, images, etc.)
- Platform independent

### Character Streams (Text Data)
- **Reader** - Abstract base class for reading characters  
- **Writer** - Abstract base class for writing characters
- Handle 16-bit Unicode characters
- Better for text processing

## Stream Hierarchy

```
InputStream (abstract)
├── FileInputStream
├── BufferedInputStream  
├── DataInputStream
├── ObjectInputStream
└── ByteArrayInputStream

OutputStream (abstract)
├── FileOutputStream
├── BufferedOutputStream
├── DataOutputStream  
├── ObjectOutputStream
└── ByteArrayOutputStream

Reader (abstract)
├── FileReader
├── BufferedReader
├── InputStreamReader
└── StringReader

Writer (abstract)
├── FileWriter
├── BufferedWriter
├── OutputStreamWriter
└── StringWriter
```

</div>

<div>

## Choosing the Right Stream

### When to Use Byte Streams
- Binary files (images, executables, archives)
- Network data transfer
- Low-level data processing
- When exact byte control is needed

```java
// Reading binary file
FileInputStream fis = new FileInputStream("image.jpg");
byte[] buffer = new byte[1024];
int bytesRead = fis.read(buffer);
```

### When to Use Character Streams
- Text files (CSV, XML, JSON)
- Configuration files
- Log files
- Human-readable content

```java
// Reading text file
FileReader fr = new FileReader("config.txt");
char[] buffer = new char[1024];  
int charsRead = fr.read(buffer);
```

### Performance Considerations

#### Unbuffered I/O
```java
// Slow - each read/write is a system call
FileInputStream fis = new FileInputStream("data.txt");
int b;
while ((b = fis.read()) != -1) {
    // Process one byte at a time
}
```

#### Buffered I/O
```java
// Fast - reads/writes in chunks
BufferedInputStream bis = new BufferedInputStream(
    new FileInputStream("data.txt"));
int b;
while ((b = bis.read()) != -1) {
    // Same code, much better performance
}
```

## Stream Decorators Pattern

Java I/O uses the Decorator pattern for combining functionalities:

```java
// Combining multiple decorators
BufferedReader reader = new BufferedReader(
    new InputStreamReader(
        new FileInputStream("data.txt"), 
        StandardCharsets.UTF_8
    )
);
```

</div>

</div>

---
layout: default
---

# File Reading Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Byte Stream Reading

### FileInputStream - Basic Reading
```java
import java.io.*;

public class FileInputStreamDemo {
    public static void main(String[] args) {
        readFileByteByByte();
        readFileWithBuffer();
        readEntireFile();
    }
    
    // Method 1: Read byte by byte (slow)
    private static void readFileByteByByte() {
        System.out.println("=== Reading Byte by Byte ===");
        
        try (FileInputStream fis = new FileInputStream("sample.txt")) {
            int byteData;
            StringBuilder content = new StringBuilder();
            
            while ((byteData = fis.read()) != -1) {
                content.append((char) byteData);
            }
            
            System.out.println("Content: " + content.toString());
            
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
        }
    }
    
    // Method 2: Read with buffer (faster)
    private static void readFileWithBuffer() {
        System.out.println("\n=== Reading with Buffer ===");
        
        try (FileInputStream fis = new FileInputStream("sample.txt")) {
            byte[] buffer = new byte[1024];
            StringBuilder content = new StringBuilder();
            int bytesRead;
            
            while ((bytesRead = fis.read(buffer)) != -1) {
                content.append(new String(buffer, 0, bytesRead));
            }
            
            System.out.println("Content: " + content.toString());
            System.out.println("Buffer size: " + buffer.length + " bytes");
            
        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
        }
    }
    
    // Method 3: Read entire file at once
    private static void readEntireFile() {
        System.out.println("\n=== Reading Entire File ===");
        
        File file = new File("sample.txt");
        
        if (!file.exists()) {
            System.out.println("Creating sample file...");
            createSampleFile();
        }
        
        try (FileInputStream fis = new FileInputStream(file)) {
            byte[] fileBytes = new byte[(int) file.length()];
            int totalBytesRead = 0;
            int bytesRead;
            
            // Ensure we read the entire file
            while (totalBytesRead < fileBytes.length) {
                bytesRead = fis.read(fileBytes, totalBytesRead, 
                                   fileBytes.length - totalBytesRead);
                if (bytesRead == -1) {
                    break;
                }
                totalBytesRead += bytesRead;
            }
            
            String content = new String(fileBytes, 0, totalBytesRead);
            System.out.println("File size: " + file.length() + " bytes");
            System.out.println("Bytes read: " + totalBytesRead);
            System.out.println("Content: " + content);
            
        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
        }
    }
    
    private static void createSampleFile() {
        try (FileWriter writer = new FileWriter("sample.txt")) {
            writer.write("Hello, World!\n");
            writer.write("This is a sample file for demonstration.\n");
            writer.write("Java File I/O Operations\n");
            writer.write("Line 4 with special chars: àáâãäå\n");
            writer.write("Numbers: 123456789\n");
            
            System.out.println("Sample file created successfully");
            
        } catch (IOException e) {
            System.err.println("Error creating sample file: " + e.getMessage());
        }
    }
}
```

### BufferedInputStream - Improved Performance
```java
import java.io.*;

public class BufferedInputStreamDemo {
    public static void main(String[] args) {
        comparePerformance();
        readWithDifferentBufferSizes();
    }
    
    private static void comparePerformance() {
        System.out.println("=== Performance Comparison ===");
        
        // Create a larger test file
        createLargeTestFile("large_test.txt", 100000);
        
        // Test unbuffered reading
        long startTime = System.currentTimeMillis();
        readUnbuffered("large_test.txt");
        long unbufferedTime = System.currentTimeMillis() - startTime;
        
        // Test buffered reading
        startTime = System.currentTimeMillis();
        readBuffered("large_test.txt");
        long bufferedTime = System.currentTimeMillis() - startTime;
        
        System.out.println("Unbuffered reading time: " + unbufferedTime + " ms");
        System.out.println("Buffered reading time: " + bufferedTime + " ms");
        System.out.println("Performance improvement: " + 
                          (double) unbufferedTime / bufferedTime + "x");
        
        // Cleanup
        new File("large_test.txt").delete();
    }
    
    private static void readUnbuffered(String fileName) {
        try (FileInputStream fis = new FileInputStream(fileName)) {
            int byteData;
            int byteCount = 0;
            
            while ((byteData = fis.read()) != -1) {
                byteCount++;
            }
            
            System.out.println("Unbuffered - Bytes read: " + byteCount);
            
        } catch (IOException e) {
            System.err.println("Error in unbuffered reading: " + e.getMessage());
        }
    }
    
    private static void readBuffered(String fileName) {
        try (BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(fileName))) {
            
            int byteData;
            int byteCount = 0;
            
            while ((byteData = bis.read()) != -1) {
                byteCount++;
            }
            
            System.out.println("Buffered - Bytes read: " + byteCount);
            
        } catch (IOException e) {
            System.err.println("Error in buffered reading: " + e.getMessage());
        }
    }
    
    private static void readWithDifferentBufferSizes() {
        System.out.println("\n=== Different Buffer Sizes ===");
        
        createLargeTestFile("buffer_test.txt", 50000);
        
        int[] bufferSizes = {1024, 4096, 8192, 16384};
        
        for (int bufferSize : bufferSizes) {
            long startTime = System.currentTimeMillis();
            readWithCustomBuffer("buffer_test.txt", bufferSize);
            long elapsedTime = System.currentTimeMillis() - startTime;
            
            System.out.println("Buffer size " + bufferSize + 
                             ": " + elapsedTime + " ms");
        }
        
        // Cleanup
        new File("buffer_test.txt").delete();
    }
    
    private static void readWithCustomBuffer(String fileName, int bufferSize) {
        try (BufferedInputStream bis = new BufferedInputStream(
                new FileInputStream(fileName), bufferSize)) {
            
            byte[] buffer = new byte[1024];
            int bytesRead;
            int totalBytes = 0;
            
            while ((bytesRead = bis.read(buffer)) != -1) {
                totalBytes += bytesRead;
            }
            
            // System.out.println("Total bytes read with buffer " + 
            //                   bufferSize + ": " + totalBytes);
            
        } catch (IOException e) {
            System.err.println("Error reading with custom buffer: " + e.getMessage());
        }
    }
    
    private static void createLargeTestFile(String fileName, int lineCount) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (int i = 1; i <= lineCount; i++) {
                writer.write("This is line number " + i + 
                           " in the test file for performance testing.\n");
            }
        } catch (IOException e) {
            System.err.println("Error creating large test file: " + e.getMessage());
        }
    }
}
```

</div>

<div>

## Character Stream Reading

### FileReader and BufferedReader
```java
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class CharacterStreamReading {
    public static void main(String[] args) {
        // Create sample text file first
        createTextFile();
        
        // Demonstrate different reading methods
        readWithFileReader();
        readWithBufferedReader();
        readLineByLine();
        readWithScanner();
    }
    
    private static void createTextFile() {
        try (FileWriter writer = new FileWriter("text_sample.txt")) {
            writer.write("Java File I/O Operations\n");
            writer.write("=============================\n");
            writer.write("Line 1: This is a text file demonstration\n");
            writer.write("Line 2: Character streams handle Unicode properly\n");
            writer.write("Line 3: Special characters: àáâãäå ñø ¿¡\n");
            writer.write("Line 4: Numbers and symbols: 123!@#$%^&*()\n");
            writer.write("Line 5: Mixed content: Hello भारत 你好 مرحبا\n");
            writer.write("Line 6: Empty line follows:\n");
            writer.write("\n");
            writer.write("Line 8: Final line in the file\n");
            
            System.out.println("Text sample file created");
            
        } catch (IOException e) {
            System.err.println("Error creating text file: " + e.getMessage());
        }
    }
    
    private static void readWithFileReader() {
        System.out.println("\n=== Reading with FileReader ===");
        
        try (FileReader fr = new FileReader("text_sample.txt")) {
            int charData;
            StringBuilder content = new StringBuilder();
            int charCount = 0;
            
            while ((charData = fr.read()) != -1) {
                content.append((char) charData);
                charCount++;
            }
            
            System.out.println("Characters read: " + charCount);
            System.out.println("Content length: " + content.length());
            System.out.println("First 100 characters: " + 
                             content.substring(0, Math.min(100, content.length())));
            
        } catch (IOException e) {
            System.err.println("Error reading with FileReader: " + e.getMessage());
        }
    }
    
    private static void readWithBufferedReader() {
        System.out.println("\n=== Reading with BufferedReader ===");
        
        try (BufferedReader br = new BufferedReader(new FileReader("text_sample.txt"))) {
            char[] buffer = new char[50];
            StringBuilder content = new StringBuilder();
            int charsRead;
            
            while ((charsRead = br.read(buffer)) != -1) {
                content.append(buffer, 0, charsRead);
            }
            
            System.out.println("Total content length: " + content.length());
            System.out.println("\nContent:");
            System.out.println(content.toString());
            
        } catch (IOException e) {
            System.err.println("Error reading with BufferedReader: " + e.getMessage());
        }
    }
    
    private static void readLineByLine() {
        System.out.println("\n=== Reading Line by Line ===");
        
        try (BufferedReader br = new BufferedReader(new FileReader("text_sample.txt"))) {
            String line;
            int lineNumber = 1;
            List<String> lines = new ArrayList<>();
            
            while ((line = br.readLine()) != null) {
                lines.add(line);
                System.out.printf("%2d: %s%n", lineNumber++, line);
            }
            
            System.out.println("\nFile Statistics:");
            System.out.println("Total lines: " + lines.size());
            System.out.println("Non-empty lines: " + 
                             lines.stream().mapToInt(l -> l.trim().isEmpty() ? 0 : 1).sum());
            System.out.println("Average line length: " + 
                             lines.stream().mapToInt(String::length).average().orElse(0));
            System.out.println("Longest line: " + 
                             lines.stream().mapToInt(String::length).max().orElse(0) + " chars");
            
        } catch (IOException e) {
            System.err.println("Error reading line by line: " + e.getMessage());
        }
    }
    
    private static void readWithScanner() {
        System.out.println("\n=== Reading with Scanner ===");
        
        try (Scanner scanner = new Scanner(new File("text_sample.txt"))) {
            int lineCount = 0;
            int wordCount = 0;
            int charCount = 0;
            
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                lineCount++;
                charCount += line.length() + 1; // +1 for newline
                
                // Count words in this line
                String[] words = line.trim().split("\\s+");
                if (!line.trim().isEmpty()) {
                    wordCount += words.length;
                }
            }
            
            System.out.println("Statistics using Scanner:");
            System.out.println("Lines: " + lineCount);
            System.out.println("Words: " + wordCount);
            System.out.println("Characters: " + charCount);
            
            // Read specific data types
            readStructuredData();
            
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }
    
    private static void readStructuredData() {
        // Create a structured data file
        try (PrintWriter pw = new PrintWriter("structured_data.txt")) {
            pw.println("John 25 85.5");
            pw.println("Alice 30 92.3");
            pw.println("Bob 22 78.9");
            pw.println("Carol 28 95.1");
        } catch (IOException e) {
            System.err.println("Error creating structured data file: " + e.getMessage());
            return;
        }
        
        System.out.println("\nReading structured data:");
        
        try (Scanner scanner = new Scanner(new File("structured_data.txt"))) {
            while (scanner.hasNext()) {
                String name = scanner.next();
                int age = scanner.nextInt();
                double score = scanner.nextDouble();
                
                System.out.printf("Name: %-10s Age: %2d Score: %5.1f%n", 
                                name, age, score);
            }
            
        } catch (FileNotFoundException e) {
            System.err.println("Structured data file not found: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error reading structured data: " + e.getMessage());
        }
        
        // Cleanup
        new File("text_sample.txt").delete();
        new File("structured_data.txt").delete();
    }
}
```

</div>

</div>

---
layout: default
---

# File Writing Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Byte Stream Writing

### FileOutputStream Operations
```java
import java.io.*;

public class FileOutputStreamDemo {
    public static void main(String[] args) {
        writeByteByByte();
        writeWithBuffer();
        writeBinaryData();
        appendToFile();
    }
    
    private static void writeByteByByte() {
        System.out.println("=== Writing Byte by Byte ===");
        
        String data = "Hello, World! Byte by byte writing.";
        
        try (FileOutputStream fos = new FileOutputStream("byte_output.txt")) {
            for (char c : data.toCharArray()) {
                fos.write((byte) c);
            }
            
            // Force write to disk
            fos.flush();
            
            System.out.println("Data written byte by byte: " + data.length() + " bytes");
            
            // Verify by reading
            verifyFileContent("byte_output.txt");
            
        } catch (IOException e) {
            System.err.println("Error writing byte by byte: " + e.getMessage());
        }
    }
    
    private static void writeWithBuffer() {
        System.out.println("\n=== Writing with Buffer ===");
        
        String data = "This is buffered writing example.\n" +
                     "Multiple lines are written together.\n" +
                     "Buffer improves performance significantly.\n";
        
        try (FileOutputStream fos = new FileOutputStream("buffer_output.txt")) {
            byte[] buffer = data.getBytes();
            fos.write(buffer);
            fos.flush();
            
            System.out.println("Buffer data written: " + buffer.length + " bytes");
            
            verifyFileContent("buffer_output.txt");
            
        } catch (IOException e) {
            System.err.println("Error writing with buffer: " + e.getMessage());
        }
    }
    
    private static void writeBinaryData() {
        System.out.println("\n=== Writing Binary Data ===");
        
        try (FileOutputStream fos = new FileOutputStream("binary_data.bin")) {
            // Write different data types as bytes
            
            // Write integers (4 bytes each)
            for (int i = 1; i <= 10; i++) {
                writeInt(fos, i);
            }
            
            // Write some bytes directly
            byte[] binaryData = {0x41, 0x42, 0x43, 0x44, 0x45}; // ABCDE
            fos.write(binaryData);
            
            // Write a string as bytes
            String text = "Binary data example";
            fos.write(text.getBytes());
            
            fos.flush();
            
            File binaryFile = new File("binary_data.bin");
            System.out.println("Binary file created: " + binaryFile.length() + " bytes");
            
            // Read and display binary content
            readBinaryData("binary_data.bin");
            
        } catch (IOException e) {
            System.err.println("Error writing binary data: " + e.getMessage());
        }
    }
    
    private static void writeInt(FileOutputStream fos, int value) throws IOException {
        // Write integer as 4 bytes (big-endian)
        fos.write((value >> 24) & 0xFF);
        fos.write((value >> 16) & 0xFF);
        fos.write((value >> 8) & 0xFF);
        fos.write(value & 0xFF);
    }
    
    private static void readBinaryData(String fileName) {
        System.out.println("Reading binary data back:");
        
        try (FileInputStream fis = new FileInputStream(fileName)) {
            // Read first 10 integers
            System.out.print("Integers: ");
            for (int i = 0; i < 10; i++) {
                int value = readInt(fis);
                System.out.print(value + " ");
            }
            System.out.println();
            
            // Read the ABCDE bytes
            byte[] letterBytes = new byte[5];
            fis.read(letterBytes);
            System.out.println("Letters: " + new String(letterBytes));
            
            // Read remaining data as string
            byte[] remaining = fis.readAllBytes();
            System.out.println("Text: " + new String(remaining));
            
        } catch (IOException e) {
            System.err.println("Error reading binary data: " + e.getMessage());
        }
    }
    
    private static int readInt(FileInputStream fis) throws IOException {
        int b1 = fis.read();
        int b2 = fis.read();
        int b3 = fis.read();
        int b4 = fis.read();
        
        if (b1 == -1 || b2 == -1 || b3 == -1 || b4 == -1) {
            throw new IOException("Unexpected end of file");
        }
        
        return (b1 << 24) | (b2 << 16) | (b3 << 8) | b4;
    }
    
    private static void appendToFile() {
        System.out.println("\n=== Appending to File ===");
        
        String initialData = "Initial content in file.\n";
        String appendData = "This is appended content.\nLine 2 of appended content.\n";
        
        // Write initial content
        try (FileOutputStream fos = new FileOutputStream("append_test.txt")) {
            fos.write(initialData.getBytes());
            System.out.println("Initial content written");
        } catch (IOException e) {
            System.err.println("Error writing initial content: " + e.getMessage());
            return;
        }
        
        // Append additional content
        try (FileOutputStream fos = new FileOutputStream("append_test.txt", true)) { // true for append mode
            fos.write(appendData.getBytes());
            System.out.println("Content appended successfully");
        } catch (IOException e) {
            System.err.println("Error appending content: " + e.getMessage());
            return;
        }
        
        // Verify final content
        verifyFileContent("append_test.txt");
        
        // Cleanup test files
        cleanup();
    }
    
    private static void verifyFileContent(String fileName) {
        System.out.println("Content of " + fileName + ":");
        
        try (FileInputStream fis = new FileInputStream(fileName)) {
            byte[] content = fis.readAllBytes();
            System.out.println(new String(content));
            System.out.println("File size: " + content.length + " bytes");
            
        } catch (IOException e) {
            System.err.println("Error verifying file content: " + e.getMessage());
        }
    }
    
    private static void cleanup() {
        String[] testFiles = {
            "byte_output.txt", 
            "buffer_output.txt", 
            "binary_data.bin", 
            "append_test.txt"
        };
        
        System.out.println("\nCleaning up test files...");
        for (String fileName : testFiles) {
            File file = new File(fileName);
            if (file.delete()) {
                System.out.println("Deleted: " + fileName);
            }
        }
    }
}
```

</div>

<div>

## Character Stream Writing

### FileWriter and BufferedWriter
```java
import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class CharacterStreamWriting {
    public static void main(String[] args) {
        writeWithFileWriter();
        writeWithBufferedWriter();
        writeFormattedData();
        createCSVFile();
        createLogFile();
    }
    
    private static void writeWithFileWriter() {
        System.out.println("=== Writing with FileWriter ===");
        
        String content = "Java Character Stream Writing\n" +
                        "===============================\n" +
                        "This file was created using FileWriter.\n" +
                        "FileWriter handles character encoding automatically.\n" +
                        "Unicode characters: àáâãäå ñø ¿¡ भारत 你好\n";
        
        try (FileWriter fw = new FileWriter("filewriter_output.txt")) {
            fw.write(content);
            fw.flush();
            
            System.out.println("Content written with FileWriter");
            System.out.println("Characters written: " + content.length());
            
            // Read and display
            readAndDisplay("filewriter_output.txt");
            
        } catch (IOException e) {
            System.err.println("Error writing with FileWriter: " + e.getMessage());
        }
    }
    
    private static void writeWithBufferedWriter() {
        System.out.println("\n=== Writing with BufferedWriter ===");
        
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("buffered_output.txt"))) {
            // Write line by line
            bw.write("Java BufferedWriter Example");
            bw.newLine();
            bw.write("=".repeat(30));
            bw.newLine();
            bw.newLine();
            
            // Write multiple lines
            String[] lines = {
                "Line 1: BufferedWriter is more efficient than FileWriter",
                "Line 2: It reduces the number of system calls",
                "Line 3: Especially beneficial for frequent write operations",
                "Line 4: Always flush or close to ensure data is written"
            };
            
            for (int i = 0; i < lines.length; i++) {
                bw.write(lines[i]);
                bw.newLine();
                
                if ((i + 1) % 2 == 0) {
                    bw.flush(); // Periodic flush
                }
            }
            
            System.out.println("Buffered content written successfully");
            
            // Read and display
            readAndDisplay("buffered_output.txt");
            
        } catch (IOException e) {
            System.err.println("Error writing with BufferedWriter: " + e.getMessage());
        }
    }
    
    private static void writeFormattedData() {
        System.out.println("\n=== Writing Formatted Data ===");
        
        try (PrintWriter pw = new PrintWriter(new FileWriter("formatted_output.txt"))) {
            // Write formatted data
            pw.println("Student Performance Report");
            pw.println("=".repeat(50));
            pw.println();
            
            // Table header
            pw.printf("%-15s %5s %8s %8s %8s%n", 
                     "Name", "Age", "Math", "Science", "Average");
            pw.println("-".repeat(50));
            
            // Student data
            String[][] students = {
                {"John Doe", "20", "85", "92", "88.5"},
                {"Alice Smith", "19", "92", "88", "90.0"}, 
                {"Bob Johnson", "21", "78", "85", "81.5"},
                {"Carol Davis", "20", "95", "97", "96.0"}
            };
            
            for (String[] student : students) {
                pw.printf("%-15s %5s %8s %8s %8s%n",
                         student[0], student[1], student[2], 
                         student[3], student[4]);
            }
            
            pw.println();
            pw.println("Report generated on: " + 
                      LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
            
            System.out.println("Formatted data written successfully");
            
            readAndDisplay("formatted_output.txt");
            
        } catch (IOException e) {
            System.err.println("Error writing formatted data: " + e.getMessage());
        }
    }
    
    private static void createCSVFile() {
        System.out.println("\n=== Creating CSV File ===");
        
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("student_data.csv"))) {
            // CSV Header
            bw.write("ID,Name,Age,Grade,Subject,Score");
            bw.newLine();
            
            // CSV Data
            String[][] csvData = {
                {"1", "John Doe", "20", "A", "Mathematics", "85"},
                {"2", "Alice Smith", "19", "A+", "Physics", "92"},
                {"3", "Bob Johnson", "21", "B", "Chemistry", "78"},
                {"4", "Carol Davis", "20", "A+", "Biology", "95"},
                {"5", "David Brown", "22", "B+", "Mathematics", "88"}
            };
            
            for (String[] row : csvData) {
                bw.write(String.join(",", row));
                bw.newLine();
            }
            
            System.out.println("CSV file created successfully");
            System.out.println("Records written: " + csvData.length);
            
            readAndDisplay("student_data.csv");
            
        } catch (IOException e) {
            System.err.println("Error creating CSV file: " + e.getMessage());
        }
    }
    
    private static void createLogFile() {
        System.out.println("\n=== Creating Log File ===");
        
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("application.log"))) {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            
            // Simulate log entries
            String[] logLevels = {"INFO", "DEBUG", "WARN", "ERROR"};
            String[] logMessages = {
                "Application started successfully",
                "Database connection established",
                "User authentication successful",
                "Processing user request",
                "Cache miss for key: user_123",
                "Low memory warning: 85% used",
                "Database connection timeout",
                "Failed to process request: invalid input",
                "User session expired",
                "Application shutdown initiated"
            };
            
            for (int i = 0; i < logMessages.length; i++) {
                String timestamp = LocalDateTime.now().format(formatter);
                String level = logLevels[i % logLevels.length];
                String message = logMessages[i];
                
                String logEntry = String.format("[%s] %-5s %s", 
                                               timestamp, level, message);
                bw.write(logEntry);
                bw.newLine();
                
                // Simulate time delay
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
            
            System.out.println("Log file created successfully");
            System.out.println("Log entries: " + logMessages.length);
            
            readAndDisplay("application.log");
            
        } catch (IOException e) {
            System.err.println("Error creating log file: " + e.getMessage());
        }
        
        // Cleanup
        cleanup();
    }
    
    private static void readAndDisplay(String fileName) {
        System.out.println("\nContent of " + fileName + ":");
        System.out.println("-".repeat(40));
        
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            int lineNumber = 1;
            
            while ((line = br.readLine()) != null) {
                System.out.printf("%2d: %s%n", lineNumber++, line);
            }
            
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        
        System.out.println("-".repeat(40));
    }
    
    private static void cleanup() {
        String[] testFiles = {
            "filewriter_output.txt",
            "buffered_output.txt", 
            "formatted_output.txt",
            "student_data.csv",
            "application.log"
        };
        
        System.out.println("\nCleaning up test files...");
        for (String fileName : testFiles) {
            File file = new File(fileName);
            if (file.delete()) {
                System.out.println("Deleted: " + fileName);
            }
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Modern Java NIO File Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Java NIO.2 - Modern File API

### Path and Files Classes
```java
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.io.IOException;
import java.util.List;

public class NIOFileOperations {
    public static void main(String[] args) {
        pathOperations();
        basicFileOperations();
        readWriteOperations();
        advancedOperations();
    }
    
    private static void pathOperations() {
        System.out.println("=== Path Operations ===");
        
        // Creating paths
        Path path1 = Paths.get("documents", "reports", "annual.txt");
        Path path2 = Paths.get("/home/user/documents/data.csv");
        Path path3 = Paths.get(".");
        
        System.out.println("Path 1: " + path1);
        System.out.println("Path 2: " + path2);
        System.out.println("Current directory: " + path3.toAbsolutePath());
        
        // Path manipulation
        Path complexPath = Paths.get("../documents/./reports/../data/file.txt");
        Path normalizedPath = complexPath.normalize();
        
        System.out.println("Complex path: " + complexPath);
        System.out.println("Normalized path: " + normalizedPath);
        
        // Path components
        Path filePath = Paths.get("/home/user/documents/report.pdf");
        System.out.println("File name: " + filePath.getFileName());
        System.out.println("Parent: " + filePath.getParent());
        System.out.println("Root: " + filePath.getRoot());
        System.out.println("Name count: " + filePath.getNameCount());
        
        for (int i = 0; i < filePath.getNameCount(); i++) {
            System.out.println("Name " + i + ": " + filePath.getName(i));
        }
    }
    
    private static void basicFileOperations() {
        System.out.println("\n=== Basic File Operations ===");
        
        Path testFile = Paths.get("nio_test.txt");
        Path testDir = Paths.get("nio_test_dir");
        
        try {
            // Create file
            if (!Files.exists(testFile)) {
                Files.createFile(testFile);
                System.out.println("File created: " + testFile);
            }
            
            // Create directory
            if (!Files.exists(testDir)) {
                Files.createDirectory(testDir);
                System.out.println("Directory created: " + testDir);
            }
            
            // Check file properties
            System.out.println("File exists: " + Files.exists(testFile));
            System.out.println("Is regular file: " + Files.isRegularFile(testFile));
            System.out.println("Is directory: " + Files.isDirectory(testDir));
            System.out.println("Is readable: " + Files.isReadable(testFile));
            System.out.println("Is writable: " + Files.isWritable(testFile));
            System.out.println("File size: " + Files.size(testFile) + " bytes");
            
            // Get file attributes
            System.out.println("Last modified: " + Files.getLastModifiedTime(testFile));
            
            // Copy file
            Path copiedFile = Paths.get("nio_test_copy.txt");
            Files.copy(testFile, copiedFile, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File copied to: " + copiedFile);
            
            // Move/rename file
            Path movedFile = Paths.get(testDir.toString(), "moved_file.txt");
            Files.move(copiedFile, movedFile, StandardCopyOption.REPLACE_EXISTING);
            System.out.println("File moved to: " + movedFile);
            
            // Cleanup
            Files.deleteIfExists(testFile);
            Files.deleteIfExists(movedFile);
            Files.deleteIfExists(testDir);
            
        } catch (IOException e) {
            System.err.println("Error in basic file operations: " + e.getMessage());
        }
    }
    
    private static void readWriteOperations() {
        System.out.println("\n=== Read/Write Operations ===");
        
        Path textFile = Paths.get("nio_text_example.txt");
        
        try {
            // Write text to file
            String content = "Java NIO.2 File Operations\n" +
                           "==========================\n" +
                           "Line 1: Modern file I/O\n" +
                           "Line 2: Better performance\n" +
                           "Line 3: More features\n" +
                           "Line 4: Exception handling\n" +
                           "Line 5: Unicode support: àáâãäå ñø";
            
            Files.write(textFile, content.getBytes(StandardCharsets.UTF_8));
            System.out.println("Content written to file");
            
            // Read entire file as string
            String fileContent = Files.readString(textFile, StandardCharsets.UTF_8);
            System.out.println("File content:");
            System.out.println(fileContent);
            
            // Read file as lines
            List<String> lines = Files.readAllLines(textFile, StandardCharsets.UTF_8);
            System.out.println("\nFile lines (" + lines.size() + " lines):");
            for (int i = 0; i < lines.size(); i++) {
                System.out.printf("%2d: %s%n", i + 1, lines.get(i));
            }
            
            // Append to file
            String appendContent = "\nLine 6: Appended using NIO\n" +
                                 "Line 7: Files.write with append option";
            
            Files.write(textFile, appendContent.getBytes(StandardCharsets.UTF_8), 
                       StandardOpenOption.APPEND);
            
            System.out.println("\nContent after append:");
            System.out.println(Files.readString(textFile));
            
            // Read bytes
            byte[] fileBytes = Files.readAllBytes(textFile);
            System.out.println("File size in bytes: " + fileBytes.length);
            
            Files.delete(textFile);
            
        } catch (IOException e) {
            System.err.println("Error in read/write operations: " + e.getMessage());
        }
    }
    
    private static void advancedOperations() {
        System.out.println("\n=== Advanced Operations ===");
        
        try {
            // Create directory structure
            Path baseDir = Paths.get("nio_advanced_test");
            Path subDir1 = baseDir.resolve("subdir1");
            Path subDir2 = baseDir.resolve("subdir2");
            
            Files.createDirectories(subDir1);
            Files.createDirectories(subDir2);
            
            // Create test files
            Files.write(subDir1.resolve("file1.txt"), "Content of file 1".getBytes());
            Files.write(subDir1.resolve("file2.txt"), "Content of file 2".getBytes());
            Files.write(subDir2.resolve("data.csv"), "Name,Age\nJohn,25\nAlice,30".getBytes());
            
            // Walk directory tree
            System.out.println("Directory tree:");
            Files.walk(baseDir)
                 .forEach(path -> {
                     int depth = path.getNameCount() - baseDir.getNameCount();
                     String indent = "  ".repeat(depth);
                     String type = Files.isDirectory(path) ? "[DIR]" : "[FILE]";
                     System.out.println(indent + type + " " + path.getFileName());
                 });
            
            // Find files
            System.out.println("\nText files in directory:");
            Files.find(baseDir, 10, 
                      (path, basicFileAttributes) -> 
                          path.toString().endsWith(".txt"))
                 .forEach(System.out::println);
            
            // List directory contents
            System.out.println("\nContents of subdir1:");
            Files.list(subDir1)
                 .forEach(path -> System.out.println("  " + path.getFileName()));
            
            // Compare files
            Path file1 = subDir1.resolve("file1.txt");
            Path file2 = subDir1.resolve("file2.txt");
            
            System.out.println("\nFile comparison:");
            System.out.println("Files are identical: " + 
                             Files.mismatch(file1, file2) == -1);
            
            // Delete directory recursively
            Files.walk(baseDir)
                 .sorted((a, b) -> -a.compareTo(b)) // Reverse order for deletion
                 .forEach(path -> {
                     try {
                         Files.delete(path);
                         System.out.println("Deleted: " + path);
                     } catch (IOException e) {
                         System.err.println("Error deleting: " + path);
                     }
                 });
            
        } catch (IOException e) {
            System.err.println("Error in advanced operations: " + e.getMessage());
        }
    }
}
```

</div>

<div>

## File Watching and Monitoring

### WatchService for File System Events
```java
import java.nio.file.*;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

public class FileWatchingDemo {
    private WatchService watchService;
    private Path watchDirectory;
    private boolean watching = false;
    
    public FileWatchingDemo(String directoryPath) {
        try {
            this.watchService = FileSystems.getDefault().newWatchService();
            this.watchDirectory = Paths.get(directoryPath);
            
            // Ensure directory exists
            if (!Files.exists(watchDirectory)) {
                Files.createDirectories(watchDirectory);
                System.out.println("Created watch directory: " + watchDirectory);
            }
            
            // Register directory for watching
            watchDirectory.register(watchService,
                StandardWatchEventKinds.ENTRY_CREATE,
                StandardWatchEventKinds.ENTRY_DELETE,
                StandardWatchEventKinds.ENTRY_MODIFY);
            
            System.out.println("Started watching directory: " + watchDirectory);
            
        } catch (IOException e) {
            System.err.println("Error setting up file watching: " + e.getMessage());
        }
    }
    
    public void startWatching() {
        watching = true;
        
        System.out.println("File watcher started. Make changes to files in: " + 
                          watchDirectory.toAbsolutePath());
        System.out.println("Press Ctrl+C to stop watching");
        
        while (watching) {
            WatchKey key;
            
            try {
                // Wait for events (timeout after 2 seconds)
                key = watchService.poll(2, TimeUnit.SECONDS);
                
                if (key == null) {
                    continue; // No events, continue polling
                }
                
                // Process events
                for (WatchEvent<?> event : key.pollEvents()) {
                    WatchEvent.Kind<?> kind = event.kind();
                    
                    // Skip overflow events
                    if (kind == StandardWatchEventKinds.OVERFLOW) {
                        System.out.println("WARNING: Event overflow occurred");
                        continue;
                    }
                    
                    // Get file name
                    WatchEvent<Path> pathEvent = (WatchEvent<Path>) event;
                    Path fileName = pathEvent.context();
                    Path fullPath = watchDirectory.resolve(fileName);
                    
                    // Handle different event types
                    handleEvent(kind, fullPath);
                }
                
                // Reset the key
                boolean valid = key.reset();
                if (!valid) {
                    System.out.println("Watch key no longer valid");
                    break;
                }
                
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        
        try {
            watchService.close();
        } catch (IOException e) {
            System.err.println("Error closing watch service: " + e.getMessage());
        }
    }
    
    private void handleEvent(WatchEvent.Kind<?> kind, Path filePath) {
        String eventType = kind.name();
        String fileName = filePath.getFileName().toString();
        
        System.out.printf("[%s] %s: %s%n", 
                         java.time.LocalTime.now().toString().substring(0, 8),
                         eventType, fileName);
        
        try {
            if (kind == StandardWatchEventKinds.ENTRY_CREATE) {
                if (Files.isRegularFile(filePath)) {
                    System.out.println("  New file created, size: " + 
                                     Files.size(filePath) + " bytes");
                } else if (Files.isDirectory(filePath)) {
                    System.out.println("  New directory created");
                }
                
            } else if (kind == StandardWatchEventKinds.ENTRY_MODIFY) {
                if (Files.exists(filePath) && Files.isRegularFile(filePath)) {
                    System.out.println("  File modified, new size: " + 
                                     Files.size(filePath) + " bytes");
                    System.out.println("  Last modified: " + 
                                     Files.getLastModifiedTime(filePath));
                }
                
            } else if (kind == StandardWatchEventKinds.ENTRY_DELETE) {
                System.out.println("  File or directory deleted");
            }
            
        } catch (IOException e) {
            System.err.println("  Error getting file information: " + e.getMessage());
        }
    }
    
    public void stopWatching() {
        watching = false;
    }
    
    public static void main(String[] args) {
        // Create watch directory
        String watchDir = "watch_test_directory";
        FileWatchingDemo watcher = new FileWatchingDemo(watchDir);
        
        // Start watching in a separate thread
        Thread watchThread = new Thread(watcher::startWatching);
        watchThread.start();
        
        // Simulate file operations for demonstration
        simulateFileOperations(watchDir);
        
        // Stop watching after demo
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        watcher.stopWatching();
        
        // Cleanup
        cleanup(watchDir);
    }
    
    private static void simulateFileOperations(String watchDir) {
        Path dir = Paths.get(watchDir);
        
        try {
            Thread.sleep(1000); // Give watcher time to start
            
            System.out.println("\n=== Simulating File Operations ===");
            
            // Create files
            System.out.println("Creating files...");
            Files.write(dir.resolve("test1.txt"), "Initial content".getBytes());
            Thread.sleep(500);
            
            Files.write(dir.resolve("test2.txt"), "Another file".getBytes());
            Thread.sleep(500);
            
            // Create subdirectory
            System.out.println("Creating directory...");
            Files.createDirectory(dir.resolve("subdir"));
            Thread.sleep(500);
            
            // Modify file
            System.out.println("Modifying file...");
            Files.write(dir.resolve("test1.txt"), 
                       "Modified content with more text".getBytes(),
                       StandardOpenOption.TRUNCATE_EXISTING);
            Thread.sleep(500);
            
            // Append to file
            System.out.println("Appending to file...");
            Files.write(dir.resolve("test2.txt"), 
                       "\nAppended line".getBytes(),
                       StandardOpenOption.APPEND);
            Thread.sleep(500);
            
            // Delete file
            System.out.println("Deleting file...");
            Files.delete(dir.resolve("test1.txt"));
            Thread.sleep(500);
            
            System.out.println("=== File Operations Complete ===\n");
            
        } catch (IOException | InterruptedException e) {
            System.err.println("Error in file operations: " + e.getMessage());
            if (e instanceof InterruptedException) {
                Thread.currentThread().interrupt();
            }
        }
    }
    
    private static void cleanup(String watchDir) {
        try {
            Path dir = Paths.get(watchDir);
            
            if (Files.exists(dir)) {
                // Delete all files and subdirectories
                Files.walk(dir)
                     .sorted((a, b) -> -a.compareTo(b))
                     .forEach(path -> {
                         try {
                             Files.delete(path);
                         } catch (IOException e) {
                             System.err.println("Error deleting: " + path);
                         }
                     });
                
                System.out.println("Cleaned up watch directory");
            }
            
        } catch (IOException e) {
            System.err.println("Error during cleanup: " + e.getMessage());
        }
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

- 📚 **Stream Hierarchy**: Understanding byte streams vs character streams
- 🔤 **Character Streams**: FileReader, FileWriter, BufferedReader, BufferedWriter
- 📖 **Byte Streams**: FileInputStream, FileOutputStream, BufferedInputStream
- ✍️ **Modern NIO**: Path, Files classes for advanced file operations
- ⚡ **Performance**: Buffered I/O vs unbuffered I/O
- 📝 **Text vs Binary**: Appropriate stream types for different data
- 🔧 **Resource Management**: Try-with-resources pattern
- 🛡️ **Best Practices**: Exception handling and cleanup

</v-clicks>

## Stream Type Comparison

| Aspect | Byte Streams | Character Streams |
|--------|-------------|------------------|
| Data Type | 8-bit bytes | 16-bit Unicode chars |
| Use Case | Binary files | Text files |
| Base Classes | InputStream/OutputStream | Reader/Writer |
| Encoding | Manual handling | Automatic UTF-16 |
| Performance | Raw speed | Text processing |

## I/O Performance Tips

### Buffering Impact
```java
// Slow - unbuffered
FileInputStream fis = new FileInputStream("file.txt");

// Fast - buffered  
BufferedInputStream bis = new BufferedInputStream(
    new FileInputStream("file.txt"));
```

### Modern NIO Advantages
```java
// Traditional I/O
FileInputStream fis = new FileInputStream("data.txt");
byte[] buffer = new byte[1024];
fis.read(buffer);

// Modern NIO
Path path = Paths.get("data.txt");
byte[] data = Files.readAllBytes(path);
```

</div>

<div>

## Key Concepts Recap

<v-clicks>

- **Streams**: Sequential access to data
- **Buffering**: Improves performance by reducing system calls
- **Character Encoding**: Automatic handling in character streams
- **Resource Management**: Always close streams (try-with-resources)
- **Exception Handling**: IOException hierarchy
- **NIO.2**: Modern file API with better features
- **Path Operations**: Platform-independent path handling
- **File Watching**: Monitor file system changes

</v-clicks>

## Best Practices Summary

### Resource Management
```java
// Good - try-with-resources
try (BufferedReader br = new BufferedReader(
        new FileReader("file.txt"))) {
    // Use reader
} // Automatically closed

// Avoid - manual closing
BufferedReader br = new BufferedReader(
    new FileReader("file.txt"));
try {
    // Use reader
} finally {
    br.close(); // Manual close
}
```

### Exception Handling
```java
try {
    Files.write(path, data);
} catch (NoSuchFileException e) {
    // Handle missing file
} catch (AccessDeniedException e) {
    // Handle permission denied
} catch (IOException e) {
    // Handle other I/O errors
}
```

## Modern vs Legacy I/O

### Legacy I/O (java.io)
- File class for file operations
- InputStream/OutputStream for bytes
- Reader/Writer for characters
- Manual resource management

### Modern NIO.2 (java.nio.file)
- Path interface for paths
- Files class for operations
- Better exception handling
- Built-in resource management
- File system monitoring
- Atomic operations

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## File I/O Operations Complete

**Lecture 33 Successfully Completed!**  
You now understand comprehensive file input/output operations in Java

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for Collections Framework! <carbon:arrow-right class="inline"/>
  </span>
</div>