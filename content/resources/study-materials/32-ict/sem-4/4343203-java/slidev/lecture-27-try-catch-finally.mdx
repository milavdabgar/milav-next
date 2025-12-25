---
theme: default
background: https://source.unsplash.com/1024x768/?safety,rescue
title: Try-Catch-Finally Blocks
info: |
  ## Java Programming (4343203)
  
  Lecture 27: Try-Catch-Finally Blocks
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about try-catch-finally blocks, multiple catch blocks, exception handling syntax, and resource management in Java.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Try-Catch-Finally Blocks
## Lecture 27

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

- 🛡️ **Understand** the syntax and structure of try-catch-finally blocks
- 🎯 **Implement** proper exception handling using try-catch statements  
- 🔧 **Use** multiple catch blocks for different exception types
- 📋 **Apply** finally blocks for resource cleanup and guaranteed execution
- ⚡ **Handle** both checked and unchecked exceptions effectively
- 🔍 **Debug** programs using exception information and stack traces
- 🏗️ **Design** robust error handling strategies in real applications

</v-clicks>

---
layout: default
---

# Try-Catch Block Fundamentals

<div class="grid grid-cols-2 gap-6">

<div>

## Basic Syntax Structure
```java
try {
    // Code that might throw an exception
    // Risky operations go here
} catch (ExceptionType e) {
    // Code to handle the exception
    // Recovery or error reporting
}
```

## Simple Try-Catch Example
```java
public class BasicTryCatch {
    public static void main(String[] args) {
        System.out.println("Program started");
        
        try {
            // Risky operation that might fail
            int result = 10 / 0; // Division by zero
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            // Handle the specific exception
            System.out.println("Error: Cannot divide by zero!");
            System.out.println("Exception message: " + e.getMessage());
        }
        
        System.out.println("Program continues...");
        System.out.println("Program ended successfully");
    }
}

/* Output:
Program started
Error: Cannot divide by zero!
Exception message: / by zero
Program continues...
Program ended successfully
*/
```

**Key Points:**
- Program doesn't crash - execution continues
- Exception is caught and handled gracefully
- Meaningful error message displayed to user

</div>

<div>

## Without Try-Catch (Program Crash)
```java
public class WithoutTryCatch {
    public static void main(String[] args) {
        System.out.println("Program started");
        
        // No exception handling - program will crash
        int result = 10 / 0; // 🚨 Crash here!
        System.out.println("Result: " + result);
        
        // This line will NEVER execute
        System.out.println("Program ended successfully");
    }
}

/* Output:
Program started
Exception in thread "main" java.lang.ArithmeticException: / by zero
    at WithoutTryCatch.main(WithoutTryCatch.java:6)
*/
```

## Array Index Exception Example
```java
public class ArrayExceptionHandling {
    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        
        try {
            System.out.println("Accessing array elements...");
            
            // Valid access
            System.out.println("Element at index 2: " + numbers[2]);
            
            // Invalid access - will throw exception
            System.out.println("Element at index 10: " + numbers[10]);
            
            // This line won't execute due to exception above
            System.out.println("This won't be printed");
            
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: Invalid array index!");
            System.out.println("Details: " + e.getMessage());
        }
        
        System.out.println("Array processing completed");
    }
}

/* Output:
Accessing array elements...
Element at index 2: 30
Error: Invalid array index!
Details: Index 10 out of bounds for length 5
Array processing completed
*/
```

</div>

</div>

---
layout: default
---

# Multiple Catch Blocks

<div class="grid grid-cols-2 gap-6">

<div>

## Multiple Exception Types
You can handle different types of exceptions with separate catch blocks:

```java
public class MultipleCatchExample {
    public static void main(String[] args) {
        String[] data = {"10", "20", "abc", "0"};
        int[] results = new int[2]; // Small array for demonstration
        
        for (int i = 0; i < data.length; i++) {
            try {
                // Multiple potential exceptions here
                int value = Integer.parseInt(data[i]); // NumberFormatException
                int result = 100 / value;              // ArithmeticException
                results[i] = result;                   // ArrayIndexOutOfBoundsException
                
                System.out.println("Processed " + data[i] + " -> " + result);
                
            } catch (NumberFormatException e) {
                System.out.println("Invalid number format: " + data[i]);
                System.out.println("Error: " + e.getMessage());
                
            } catch (ArithmeticException e) {
                System.out.println("Math error with value: " + data[i]);
                System.out.println("Error: " + e.getMessage());
                
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Array full, cannot store more results");
                System.out.println("Error: " + e.getMessage());
                break; // Exit loop since array is full
            }
        }
        
        System.out.println("Processing complete");
    }
}

/* Output:
Processed 10 -> 10
Processed 20 -> 5
Invalid number format: abc
Error: For input string: "abc"
Math error with value: 0
Error: / by zero
Processing complete
*/
```

</div>

<div>

## Catch Block Order Matters!
Exception hierarchy affects catch block ordering:

```java
// CORRECT ORDER: Specific to general
public class CatchOrderCorrect {
    public static void processInput(String input) {
        try {
            int number = Integer.parseInt(input);
            int result = 100 / number;
            System.out.println("Result: " + result);
            
        } catch (NumberFormatException e) {
            // Specific exception first
            System.out.println("Invalid number: " + input);
            
        } catch (ArithmeticException e) {
            // Another specific exception
            System.out.println("Division by zero error");
            
        } catch (Exception e) {
            // General exception last
            System.out.println("Unexpected error: " + e.getMessage());
        }
    }
}

// INCORRECT ORDER: Will cause compile error
public class CatchOrderIncorrect {
    public static void processInput(String input) {
        try {
            int number = Integer.parseInt(input);
            int result = 100 / number;
            
        } catch (Exception e) {
            // 🚨 COMPILE ERROR: General exception first
            System.out.println("General error");
            
        } catch (NumberFormatException e) {
            // This will never be reached!
            System.out.println("Number format error");
        }
        /*
        Compile Error: Unreachable catch block for NumberFormatException. 
        It is already handled by the catch block for Exception
        */
    }
}
```

## Multi-Catch (Java 7+)
Handle multiple exception types in one catch block:

```java
public class MultiCatchExample {
    public static void processData(String input, int index) {
        int[] array = {1, 2, 3};
        
        try {
            int number = Integer.parseInt(input);
            int value = array[index];
            int result = number / value;
            System.out.println("Result: " + result);
            
        } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
            // Handle both exceptions the same way
            System.out.println("Input or index error: " + e.getMessage());
            
        } catch (ArithmeticException e) {
            // Handle arithmetic errors separately
            System.out.println("Mathematical error: " + e.getMessage());
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Finally Block

<div class="grid grid-cols-2 gap-6">

<div>

## Finally Block Fundamentals
The **finally** block executes **regardless** of whether an exception occurs or not.

```java
public class FinallyBasicExample {
    public static void demonstrateFinally() {
        System.out.println("Method started");
        
        try {
            System.out.println("In try block");
            int result = 10 / 2; // No exception
            System.out.println("Result: " + result);
            
        } catch (ArithmeticException e) {
            System.out.println("In catch block");
            System.out.println("Error: " + e.getMessage());
            
        } finally {
            // This ALWAYS executes
            System.out.println("In finally block - always executes!");
        }
        
        System.out.println("Method ended");
    }
    
    public static void main(String[] args) {
        demonstrateFinally();
    }
}

/* Output:
Method started
In try block
Result: 5
In finally block - always executes!
Method ended
*/
```

## Finally with Exception
```java
public class FinallyWithException {
    public static void demonstrateFinallyWithException() {
        System.out.println("Method started");
        
        try {
            System.out.println("In try block");
            int result = 10 / 0; // Exception will occur
            System.out.println("This won't execute");
            
        } catch (ArithmeticException e) {
            System.out.println("In catch block");
            System.out.println("Handled: " + e.getMessage());
            
        } finally {
            // Still executes even when exception occurred
            System.out.println("Finally block - cleanup completed");
        }
        
        System.out.println("Method ended normally");
    }
}

/* Output:
Method started
In try block
In catch block
Handled: / by zero
Finally block - cleanup completed
Method ended normally
*/
```

</div>

<div>

## Resource Cleanup with Finally
Most common use: Cleaning up resources like files, connections, etc.

```java
public class ResourceCleanupExample {
    public static void readFile(String filename) {
        FileInputStream file = null;
        BufferedReader reader = null;
        
        try {
            System.out.println("Opening file: " + filename);
            file = new FileInputStream(filename);
            reader = new BufferedReader(new InputStreamReader(file));
            
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Read: " + line);
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filename);
            System.out.println("Error: " + e.getMessage());
            
        } catch (IOException e) {
            System.out.println("Error reading file: " + filename);
            System.out.println("Error: " + e.getMessage());
            
        } finally {
            // Cleanup resources - ALWAYS executes
            System.out.println("Cleaning up resources...");
            
            try {
                if (reader != null) {
                    reader.close();
                    System.out.println("Reader closed");
                }
                if (file != null) {
                    file.close();
                    System.out.println("File closed");
                }
            } catch (IOException e) {
                System.out.println("Error closing resources: " + e.getMessage());
            }
        }
        
        System.out.println("File processing completed");
    }
    
    public static void main(String[] args) {
        readFile("data.txt");           // File exists
        System.out.println("---");
        readFile("nonexistent.txt");    // File doesn't exist
    }
}
```

## Finally Execution Scenarios
```java
public class FinallyScenarios {
    // Scenario 1: Normal execution
    public static void scenario1() {
        try {
            System.out.println("Normal operation");
            return; // Even with return, finally executes
        } finally {
            System.out.println("Finally executes despite return");
        }
    }
    
    // Scenario 2: Exception thrown and caught
    public static void scenario2() {
        try {
            throw new RuntimeException("Test exception");
        } catch (RuntimeException e) {
            System.out.println("Exception caught");
            return;
        } finally {
            System.out.println("Finally executes after catch");
        }
    }
    
    // Scenario 3: Exception not caught (re-thrown)
    public static void scenario3() throws Exception {
        try {
            throw new Exception("Uncaught exception");
        } finally {
            System.out.println("Finally executes even with uncaught exception");
        }
        // Exception will be thrown to caller after finally
    }
}
```

</div>

</div>

---
layout: default
---

# Nested Try-Catch Blocks

<div class="grid grid-cols-2 gap-6">

<div>

## Nested Exception Handling
You can have try-catch blocks inside other try-catch blocks:

```java
public class NestedTryCatchExample {
    public static void processData() {
        try {
            System.out.println("Outer try block - starting data processing");
            
            // First risky operation
            String[] data = {"10", "20", "abc", "5"};
            
            for (int i = 0; i < data.length; i++) {
                try {
                    System.out.println("Inner try - processing: " + data[i]);
                    
                    // Inner risky operations
                    int number = Integer.parseInt(data[i]);
                    int result = 100 / number;
                    
                    // Another nested operation
                    try {
                        int[] results = new int[2];
                        results[i] = result; // Might throw AIOOBE
                        System.out.println("Stored result: " + result);
                        
                    } catch (ArrayIndexOutOfBoundsException e) {
                        System.out.println("  Cannot store result - array full");
                    }
                    
                } catch (NumberFormatException e) {
                    System.out.println("  Invalid number format: " + data[i]);
                    
                } catch (ArithmeticException e) {
                    System.out.println("  Division by zero with: " + data[i]);
                }
            }
            
            System.out.println("Data processing completed successfully");
            
        } catch (Exception e) {
            System.out.println("Outer catch - Unexpected error occurred");
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    public static void main(String[] args) {
        processData();
    }
}

/* Output:
Outer try block - starting data processing
Inner try - processing: 10
Stored result: 10
Inner try - processing: 20
Stored result: 5
Inner try - processing: abc
  Invalid number format: abc
Inner try - processing: 5
  Cannot store result - array full
Data processing completed successfully
*/
```

</div>

<div>

## Method Call Exception Propagation
```java
public class MethodCallExceptionExample {
    public static void main(String[] args) {
        try {
            System.out.println("Main method - starting");
            level1Method();
            System.out.println("Main method - completed");
            
        } catch (ArithmeticException e) {
            System.out.println("Caught in main: " + e.getMessage());
        }
    }
    
    public static void level1Method() {
        try {
            System.out.println("Level 1 - calling level 2");
            level2Method();
            System.out.println("Level 1 - completed");
            
        } catch (NumberFormatException e) {
            System.out.println("Level 1 caught: " + e.getMessage());
        }
        // ArithmeticException not caught here - propagates up
    }
    
    public static void level2Method() {
        try {
            System.out.println("Level 2 - calling level 3");
            level3Method();
            System.out.println("Level 2 - completed");
            
        } catch (NullPointerException e) {
            System.out.println("Level 2 caught: " + e.getMessage());
        }
        // Other exceptions not caught here - propagate up
    }
    
    public static void level3Method() {
        System.out.println("Level 3 - performing risky operation");
        
        // This will throw ArithmeticException
        int result = 42 / 0;
        
        System.out.println("Level 3 - completed: " + result);
    }
}

/* Output:
Main method - starting
Level 1 - calling level 2
Level 2 - calling level 3
Level 3 - performing risky operation
Caught in main: / by zero
*/
```

## Complex Nested Example with Finally
```java
public class ComplexNestedExample {
    public static void complexOperation(String input) {
        try {
            System.out.println("Starting complex operation with: " + input);
            
            try {
                int number = Integer.parseInt(input);
                
                try {
                    int result = 100 / number;
                    System.out.println("Calculation successful: " + result);
                    
                } catch (ArithmeticException e) {
                    System.out.println("Division error: " + e.getMessage());
                } finally {
                    System.out.println("Inner finally - calculation cleanup");
                }
                
            } catch (NumberFormatException e) {
                System.out.println("Parsing error: " + e.getMessage());
            } finally {
                System.out.println("Middle finally - parsing cleanup");
            }
            
        } catch (Exception e) {
            System.out.println("Outer catch - unexpected error");
        } finally {
            System.out.println("Outer finally - operation cleanup");
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Try-with-Resources (Java 7+)

<div class="grid grid-cols-2 gap-6">

<div>

## Traditional Resource Management
Before Java 7, resource cleanup was verbose and error-prone:

```java
public class TraditionalResourceManagement {
    public static void readFileOldWay(String filename) {
        FileInputStream file = null;
        BufferedReader reader = null;
        
        try {
            file = new FileInputStream(filename);
            reader = new BufferedReader(new InputStreamReader(file));
            
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Read: " + line);
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            
        } catch (IOException e) {
            System.out.println("IO Error: " + e.getMessage());
            
        } finally {
            // Complex cleanup logic
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Error closing reader: " + e.getMessage());
                }
            }
            
            if (file != null) {
                try {
                    file.close();
                } catch (IOException e) {
                    System.out.println("Error closing file: " + e.getMessage());
                }
            }
        }
    }
}
```

**Problems with Traditional Approach:**
- Verbose and repetitive code
- Easy to forget resource cleanup
- Complex nested try-catch in finally
- Resources might not get closed if exceptions occur

</div>

<div>

## Try-with-Resources Syntax
Java 7+ provides automatic resource management:

```java
public class TryWithResourcesExample {
    // Simple try-with-resources
    public static void readFileNewWay(String filename) {
        // Resources declared in parentheses - automatically closed
        try (FileInputStream file = new FileInputStream(filename);
             BufferedReader reader = new BufferedReader(new InputStreamReader(file))) {
            
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("Read: " + line);
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            
        } catch (IOException e) {
            System.out.println("IO Error: " + e.getMessage());
        }
        // Resources automatically closed here - no finally needed!
    }
    
    // Multiple resources
    public static void copyFile(String source, String destination) {
        try (FileInputStream input = new FileInputStream(source);
             FileOutputStream output = new FileOutputStream(destination);
             BufferedInputStream bufferedInput = new BufferedInputStream(input);
             BufferedOutputStream bufferedOutput = new BufferedOutputStream(output)) {
            
            byte[] buffer = new byte[1024];
            int bytesRead;
            
            while ((bytesRead = bufferedInput.read(buffer)) != -1) {
                bufferedOutput.write(buffer, 0, bytesRead);
            }
            
            System.out.println("File copied successfully");
            
        } catch (IOException e) {
            System.out.println("Copy failed: " + e.getMessage());
        }
        // All four resources automatically closed in reverse order
    }
    
    // With database connections
    public static void queryDatabase(String query) {
        try (Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost/mydb", "user", "pass");
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {
            
            while (rs.next()) {
                System.out.println("Result: " + rs.getString(1));
            }
            
        } catch (SQLException e) {
            System.out.println("Database error: " + e.getMessage());
        }
        // Connection, statement, and result set automatically closed
    }
}
```

**Benefits of Try-with-Resources:**
- Automatic resource cleanup
- Cleaner, more readable code
- Guaranteed resource closing
- Handles exceptions in resource closing
- Works with any class implementing AutoCloseable

</div>

</div>

---
layout: default
---

# Practical Exception Handling Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## 1. Input Validation Pattern
```java
public class InputValidationPattern {
    private Scanner scanner = new Scanner(System.in);
    
    // Robust integer input
    public int getValidInteger(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                
                // Validate not empty
                if (input.isEmpty()) {
                    System.out.println("Input cannot be empty. Please try again.");
                    continue;
                }
                
                // Parse and return
                return Integer.parseInt(input);
                
            } catch (NumberFormatException e) {
                System.out.println("Invalid number format. Please enter a valid integer.");
            }
        }
    }
    
    // Robust integer input with range validation
    public int getValidIntegerInRange(String prompt, int min, int max) {
        while (true) {
            try {
                int value = getValidInteger(prompt + " (" + min + "-" + max + "): ");
                
                if (value < min || value > max) {
                    System.out.println("Value must be between " + min + " and " + max);
                    continue;
                }
                
                return value;
                
            } catch (Exception e) {
                System.out.println("Unexpected error: " + e.getMessage());
            }
        }
    }
    
    // Email validation pattern
    public String getValidEmail(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String email = scanner.nextLine().trim();
                
                if (email.isEmpty()) {
                    throw new IllegalArgumentException("Email cannot be empty");
                }
                
                if (!email.contains("@") || !email.contains(".")) {
                    throw new IllegalArgumentException("Invalid email format");
                }
                
                if (email.indexOf("@") > email.lastIndexOf(".")) {
                    throw new IllegalArgumentException("Invalid email format");
                }
                
                return email;
                
            } catch (IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
}
```

</div>

<div>

## 2. Configuration Loading Pattern
```java
public class ConfigurationManager {
    private Properties config = new Properties();
    private boolean isLoaded = false;
    
    public void loadConfiguration(String filename) {
        try (InputStream input = new FileInputStream(filename)) {
            config.load(input);
            isLoaded = true;
            System.out.println("Configuration loaded successfully from: " + filename);
            
        } catch (FileNotFoundException e) {
            System.out.println("Config file not found: " + filename);
            loadDefaultConfiguration();
            
        } catch (IOException e) {
            System.out.println("Error reading config file: " + e.getMessage());
            loadDefaultConfiguration();
            
        } catch (Exception e) {
            System.out.println("Unexpected error loading config: " + e.getMessage());
            loadDefaultConfiguration();
        }
    }
    
    private void loadDefaultConfiguration() {
        System.out.println("Loading default configuration...");
        config.setProperty("database.host", "localhost");
        config.setProperty("database.port", "3306");
        config.setProperty("app.timeout", "30");
        config.setProperty("app.retries", "3");
        isLoaded = true;
    }
    
    public String getProperty(String key, String defaultValue) {
        if (!isLoaded) {
            throw new IllegalStateException("Configuration not loaded");
        }
        
        return config.getProperty(key, defaultValue);
    }
    
    public int getIntProperty(String key, int defaultValue) {
        try {
            String value = getProperty(key, String.valueOf(defaultValue));
            return Integer.parseInt(value);
        } catch (NumberFormatException e) {
            System.out.println("Invalid integer value for " + key + 
                             ", using default: " + defaultValue);
            return defaultValue;
        }
    }
}
```

## 3. Database Operation Pattern
```java
public class DatabaseOperations {
    private String connectionUrl;
    
    public DatabaseOperations(String url) {
        this.connectionUrl = url;
    }
    
    public List<User> getAllUsers() {
        List<User> users = new ArrayList<>();
        
        try (Connection conn = DriverManager.getConnection(connectionUrl);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM users")) {
            
            while (rs.next()) {
                users.add(new User(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("email")
                ));
            }
            
        } catch (SQLException e) {
            System.err.println("Database error in getAllUsers: " + e.getMessage());
            // Log the error
            logError("getAllUsers", e);
            // Return empty list rather than null
            return new ArrayList<>();
        }
        
        return users;
    }
    
    public boolean createUser(User user) {
        try (Connection conn = DriverManager.getConnection(connectionUrl);
             PreparedStatement stmt = conn.prepareStatement(
                 "INSERT INTO users (name, email) VALUES (?, ?)")) {
            
            stmt.setString(1, user.getName());
            stmt.setString(2, user.getEmail());
            
            int rowsAffected = stmt.executeUpdate();
            return rowsAffected > 0;
            
        } catch (SQLException e) {
            System.err.println("Error creating user: " + e.getMessage());
            logError("createUser", e);
            return false;
        }
    }
    
    private void logError(String operation, Exception e) {
        // Simple logging - in real apps use proper logging framework
        System.err.println("[ERROR] " + new Date() + 
                          " - Operation: " + operation + 
                          " - Error: " + e.getMessage());
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: File Processing System

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build a Robust File Processor
Create a file processing system that handles various exceptions gracefully:

```java
public class FileProcessor {
    
    // Task 1: Implement robust file reading
    public List<String> readFileLines(String filename) {
        // TODO: Implement with proper exception handling
        // Handle: FileNotFoundException, IOException, SecurityException
        // Return empty list if file cannot be read
        // Log appropriate error messages
        
        return null; // Replace with implementation
    }
    
    // Task 2: Implement safe file writing
    public boolean writeToFile(String filename, List<String> lines) {
        // TODO: Implement with try-with-resources
        // Handle: IOException, SecurityException
        // Return true if successful, false otherwise
        // Create backup of existing file if it exists
        
        return false; // Replace with implementation
    }
    
    // Task 3: Implement file copying with progress
    public boolean copyFile(String source, String destination) {
        // TODO: Implement with exception handling
        // Handle: FileNotFoundException, IOException, SecurityException
        // Show progress during copying
        // Verify copy was successful
        
        return false; // Replace with implementation
    }
    
    // Task 4: Process CSV data with validation
    public List<Person> processCSVFile(String filename) {
        // TODO: Read CSV file and parse Person objects
        // Handle: File errors, parsing errors, validation errors
        // Skip invalid lines but continue processing
        // Log errors for each problematic line
        
        return null; // Replace with implementation
    }
}

class Person {
    private String name;
    private int age;
    private String email;
    
    // Constructor, getters, setters
}
```

**Requirements:**
- Use try-with-resources for all file operations
- Handle each exception type appropriately
- Provide meaningful error messages
- Log errors for debugging
- Graceful degradation (continue processing when possible)

</div>

<div>

## Solution Template

```java
public class FileProcessorSolution {
    
    public List<String> readFileLines(String filename) {
        List<String> lines = new ArrayList<>();
        
        try (BufferedReader reader = new BufferedReader(
                new FileReader(filename))) {
            
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
            
            System.out.println("Successfully read " + lines.size() + 
                             " lines from " + filename);
            
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + filename);
            System.err.println("Please check if the file exists and path is correct.");
            
        } catch (SecurityException e) {
            System.err.println("Access denied to file: " + filename);
            System.err.println("Check file permissions.");
            
        } catch (IOException e) {
            System.err.println("Error reading file " + filename + ": " + e.getMessage());
            
        } catch (Exception e) {
            System.err.println("Unexpected error reading file: " + e.getMessage());
        }
        
        return lines;
    }
    
    public boolean writeToFile(String filename, List<String> lines) {
        // Create backup if file exists
        File file = new File(filename);
        if (file.exists()) {
            try {
                Files.copy(file.toPath(), 
                          new File(filename + ".backup").toPath(),
                          StandardCopyOption.REPLACE_EXISTING);
                System.out.println("Backup created: " + filename + ".backup");
            } catch (IOException e) {
                System.out.println("Warning: Could not create backup");
            }
        }
        
        try (BufferedWriter writer = new BufferedWriter(
                new FileWriter(filename))) {
            
            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }
            
            System.out.println("Successfully wrote " + lines.size() + 
                             " lines to " + filename);
            return true;
            
        } catch (SecurityException e) {
            System.err.println("Access denied to write file: " + filename);
            return false;
            
        } catch (IOException e) {
            System.err.println("Error writing to file " + filename + ": " + e.getMessage());
            return false;
            
        } catch (Exception e) {
            System.err.println("Unexpected error writing file: " + e.getMessage());
            return false;
        }
    }
}
```

**Key Points:**
- Always use try-with-resources for file operations
- Handle specific exceptions before general ones
- Provide user-friendly error messages
- Return sensible default values
- Create backups for destructive operations

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Calculator with Exception Handling

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build a Robust Calculator
Create a calculator that handles all possible exceptions:

```java
public class RobustCalculator {
    private Scanner scanner = new Scanner(System.in);
    
    public void runCalculator() {
        System.out.println("=== Robust Calculator ===");
        
        while (true) {
            try {
                showMenu();
                int choice = getMenuChoice();
                
                if (choice == 5) {
                    System.out.println("Thank you for using the calculator!");
                    break;
                }
                
                performCalculation(choice);
                
            } catch (Exception e) {
                System.out.println("Unexpected error: " + e.getMessage());
                System.out.println("Please try again.");
            }
        }
    }
    
    private void showMenu() {
        System.out.println("\n--- Calculator Menu ---");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("5. Exit");
    }
    
    // TODO: Implement with exception handling
    private int getMenuChoice() {
        // Handle invalid input, out of range values
        return 0;
    }
    
    // TODO: Implement with exception handling
    private double getNumber(String prompt) {
        // Handle invalid number formats, empty input
        return 0.0;
    }
    
    // TODO: Implement with exception handling
    private void performCalculation(int operation) {
        // Handle division by zero, overflow, invalid operations
    }
    
    // TODO: Implement specific operations
    private double add(double a, double b) { return a + b; }
    private double subtract(double a, double b) { return a - b; }
    private double multiply(double a, double b) { return a * b; }
    private double divide(double a, double b) throws ArithmeticException {
        // Handle division by zero
        return 0.0;
    }
}
```

</div>

<div>

## Solution Implementation

```java
public class RobustCalculatorSolution {
    private Scanner scanner = new Scanner(System.in);
    
    private int getMenuChoice() {
        while (true) {
            try {
                System.out.print("Enter your choice (1-5): ");
                String input = scanner.nextLine().trim();
                
                if (input.isEmpty()) {
                    System.out.println("Please enter a choice.");
                    continue;
                }
                
                int choice = Integer.parseInt(input);
                
                if (choice < 1 || choice > 5) {
                    System.out.println("Please enter a number between 1 and 5.");
                    continue;
                }
                
                return choice;
                
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }
    
    private double getNumber(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                
                if (input.isEmpty()) {
                    System.out.println("Please enter a number.");
                    continue;
                }
                
                double number = Double.parseDouble(input);
                
                // Check for special values
                if (Double.isInfinite(number)) {
                    System.out.println("Number too large. Please enter a smaller number.");
                    continue;
                }
                
                if (Double.isNaN(number)) {
                    System.out.println("Invalid number. Please try again.");
                    continue;
                }
                
                return number;
                
            } catch (NumberFormatException e) {
                System.out.println("Invalid number format. Please enter a valid number.");
            }
        }
    }
    
    private void performCalculation(int operation) {
        try {
            double num1 = getNumber("Enter first number: ");
            double num2 = getNumber("Enter second number: ");
            double result;
            String operationName;
            
            switch (operation) {
                case 1:
                    result = add(num1, num2);
                    operationName = "Addition";
                    break;
                case 2:
                    result = subtract(num1, num2);
                    operationName = "Subtraction";
                    break;
                case 3:
                    result = multiply(num1, num2);
                    operationName = "Multiplication";
                    break;
                case 4:
                    result = divide(num1, num2);
                    operationName = "Division";
                    break;
                default:
                    throw new IllegalArgumentException("Invalid operation: " + operation);
            }
            
            System.out.println("\n" + operationName + " Result: " + num1 + 
                             " " + getOperatorSymbol(operation) + " " + num2 + " = " + result);
            
            // Check for overflow
            if (Double.isInfinite(result)) {
                System.out.println("Warning: Result is too large (infinity)");
            }
            
        } catch (ArithmeticException e) {
            System.out.println("Mathematical Error: " + e.getMessage());
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid Operation: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Calculation Error: " + e.getMessage());
        }
    }
    
    private double divide(double a, double b) throws ArithmeticException {
        if (b == 0.0) {
            throw new ArithmeticException("Division by zero is not allowed");
        }
        return a / b;
    }
    
    private String getOperatorSymbol(int operation) {
        switch (operation) {
            case 1: return "+";
            case 2: return "-";
            case 3: return "*";
            case 4: return "/";
            default: return "?";
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Real-world Applications

<div class="grid grid-cols-2 gap-6">

<div>

## 1. Web Application Error Handling
```java
@RestController
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        try {
            User user = userService.findById(id);
            return ResponseEntity.ok(user);
            
        } catch (UserNotFoundException e) {
            return ResponseEntity.notFound().build();
            
        } catch (DatabaseException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                .body(null);
                                
        } catch (Exception e) {
            // Log unexpected errors
            logger.error("Unexpected error in getUser", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                .body(null);
        }
    }
    
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@RequestBody User user) {
        try {
            // Validate input
            validateUser(user);
            
            User savedUser = userService.save(user);
            return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);
            
        } catch (ValidationException e) {
            return ResponseEntity.badRequest().build();
            
        } catch (DuplicateUserException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).build();
            
        } catch (Exception e) {
            logger.error("Error creating user", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                                .build();
        }
    }
    
    private void validateUser(User user) throws ValidationException {
        if (user.getName() == null || user.getName().trim().isEmpty()) {
            throw new ValidationException("Name is required");
        }
        
        if (user.getEmail() == null || !user.getEmail().contains("@")) {
            throw new ValidationException("Valid email is required");
        }
    }
}
```

## 2. File Upload Service
```java
@Service
public class FileUploadService {
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
    private static final String UPLOAD_DIR = "/uploads/";
    
    public String uploadFile(MultipartFile file) throws FileUploadException {
        try {
            // Validate file
            validateFile(file);
            
            // Create upload directory if not exists
            createUploadDirectory();
            
            // Generate unique filename
            String filename = generateUniqueFilename(file.getOriginalFilename());
            String filepath = UPLOAD_DIR + filename;
            
            // Save file using try-with-resources
            try (InputStream inputStream = file.getInputStream();
                 OutputStream outputStream = new FileOutputStream(filepath)) {
                
                byte[] buffer = new byte[1024];
                int bytesRead;
                
                while ((bytesRead = inputStream.read(buffer)) != -1) {
                    outputStream.write(buffer, 0, bytesRead);
                }
            }
            
            // Verify file was saved correctly
            File savedFile = new File(filepath);
            if (!savedFile.exists() || savedFile.length() != file.getSize()) {
                throw new FileUploadException("File was not saved correctly");
            }
            
            logger.info("File uploaded successfully: " + filename);
            return filename;
            
        } catch (IOException e) {
            throw new FileUploadException("Error saving file: " + e.getMessage(), e);
            
        } catch (SecurityException e) {
            throw new FileUploadException("Permission denied: " + e.getMessage(), e);
            
        } catch (Exception e) {
            throw new FileUploadException("Unexpected error: " + e.getMessage(), e);
        }
    }
    
    private void validateFile(MultipartFile file) throws FileUploadException {
        if (file == null || file.isEmpty()) {
            throw new FileUploadException("File is empty or null");
        }
        
        if (file.getSize() > MAX_FILE_SIZE) {
            throw new FileUploadException("File size exceeds maximum allowed size");
        }
        
        String filename = file.getOriginalFilename();
        if (filename == null || filename.trim().isEmpty()) {
            throw new FileUploadException("Invalid filename");
        }
        
        // Check file extension
        String extension = filename.substring(filename.lastIndexOf(".") + 1);
        if (!isAllowedExtension(extension)) {
            throw new FileUploadException("File type not allowed: " + extension);
        }
    }
}
```

</div>

<div>

## 3. Banking Transaction System
```java
@Service
public class BankingService {
    
    @Autowired
    private AccountRepository accountRepository;
    
    @Autowired
    private TransactionRepository transactionRepository;
    
    @Transactional
    public TransactionResult transfer(String fromAccountId, String toAccountId, 
                                    BigDecimal amount) {
        try {
            // Validate inputs
            validateTransferRequest(fromAccountId, toAccountId, amount);
            
            // Get accounts with locking to prevent concurrent modification
            Account fromAccount = accountRepository.findByIdForUpdate(fromAccountId);
            Account toAccount = accountRepository.findByIdForUpdate(toAccountId);
            
            if (fromAccount == null) {
                throw new AccountNotFoundException("Source account not found: " + fromAccountId);
            }
            
            if (toAccount == null) {
                throw new AccountNotFoundException("Destination account not found: " + toAccountId);
            }
            
            // Check business rules
            validateTransfer(fromAccount, toAccount, amount);
            
            // Perform transfer
            fromAccount.debit(amount);
            toAccount.credit(amount);
            
            // Save accounts
            accountRepository.save(fromAccount);
            accountRepository.save(toAccount);
            
            // Record transaction
            Transaction transaction = new Transaction(fromAccountId, toAccountId, 
                                                    amount, TransactionType.TRANSFER);
            transactionRepository.save(transaction);
            
            logger.info("Transfer completed successfully: {} from {} to {}", 
                       amount, fromAccountId, toAccountId);
            
            return new TransactionResult(true, transaction.getId(), "Transfer successful");
            
        } catch (AccountNotFoundException | InsufficientFundsException | 
                 AccountFrozenException e) {
            // Business exceptions - rollback transaction
            logger.warn("Transfer failed: {}", e.getMessage());
            return new TransactionResult(false, null, e.getMessage());
            
        } catch (DataAccessException e) {
            // Database exceptions - rollback transaction
            logger.error("Database error during transfer", e);
            return new TransactionResult(false, null, "System temporarily unavailable");
            
        } catch (Exception e) {
            // Unexpected exceptions - rollback transaction
            logger.error("Unexpected error during transfer", e);
            return new TransactionResult(false, null, "Transfer failed due to system error");
        }
    }
    
    private void validateTransfer(Account fromAccount, Account toAccount, 
                                BigDecimal amount) 
            throws InsufficientFundsException, AccountFrozenException {
        
        if (fromAccount.isFrozen()) {
            throw new AccountFrozenException("Source account is frozen");
        }
        
        if (toAccount.isFrozen()) {
            throw new AccountFrozenException("Destination account is frozen");
        }
        
        if (fromAccount.getBalance().compareTo(amount) < 0) {
            throw new InsufficientFundsException("Insufficient funds in source account");
        }
        
        // Check daily transfer limit
        BigDecimal dailyTransferTotal = transactionRepository
            .getDailyTransferTotal(fromAccount.getId(), LocalDate.now());
            
        if (dailyTransferTotal.add(amount).compareTo(fromAccount.getDailyLimit()) > 0) {
            throw new DailyLimitExceededException("Daily transfer limit exceeded");
        }
    }
}
```

## 4. Email Service
```java
@Service
public class EmailService {
    
    @Value("${smtp.host}")
    private String smtpHost;
    
    @Value("${smtp.port}")
    private int smtpPort;
    
    public boolean sendEmail(String to, String subject, String body) {
        Properties props = new Properties();
        props.put("mail.smtp.host", smtpHost);
        props.put("mail.smtp.port", smtpPort);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        
        try {
            Session session = Session.getInstance(props, new Authenticator() {
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(username, password);
                }
            });
            
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(fromEmail));
            message.setRecipients(Message.RecipientType.TO, 
                                InternetAddress.parse(to));
            message.setSubject(subject);
            message.setText(body);
            
            // Send with timeout handling
            Transport.send(message);
            
            logger.info("Email sent successfully to: {}", to);
            return true;
            
        } catch (AddressException e) {
            logger.error("Invalid email address: {}", to, e);
            return false;
            
        } catch (MessagingException e) {
            logger.error("Error sending email to: {}", to, e);
            return false;
            
        } catch (Exception e) {
            logger.error("Unexpected error sending email", e);
            return false;
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

- 🛡️ **Try-Catch Syntax**: Proper structure for handling exceptions
- 🎯 **Multiple Catch Blocks**: Handling different exception types specifically  
- 🔧 **Finally Block**: Guaranteed execution for cleanup operations
- 📋 **Try-with-Resources**: Automatic resource management (Java 7+)
- ⚡ **Exception Propagation**: How exceptions travel up the call stack
- 🔍 **Nested Try-Catch**: Complex exception handling scenarios
- 🏗️ **Practical Patterns**: Real-world exception handling strategies

</v-clicks>

## Exception Handling Best Practices

### Syntax Rules
- **Catch Order**: Specific exceptions before general ones
- **Resource Management**: Always use try-with-resources for AutoCloseable
- **Finally Block**: Use for guaranteed cleanup operations
- **Multiple Catch**: Handle different exceptions appropriately

### Design Principles
- **Fail Fast**: Detect problems early
- **Graceful Degradation**: Continue operation when possible
- **Meaningful Messages**: Provide clear error information
- **Proper Logging**: Record errors for debugging
- **Resource Cleanup**: Always close resources properly

</div>

<div>

## Key Patterns Recap

<v-clicks>

- **Input Validation**: Robust user input handling with retry logic
- **Configuration Loading**: Fallback to defaults when config fails
- **File Operations**: Safe file handling with backup and verification
- **Database Operations**: Transaction management with proper rollback
- **Service Integration**: Graceful handling of external service failures
- **Resource Management**: Automatic cleanup using try-with-resources

</v-clicks>

## Common Mistakes to Avoid

### Syntax Mistakes
- Wrong catch block order (general before specific)
- Forgetting to close resources in finally
- Empty catch blocks that hide errors
- Not using try-with-resources for AutoCloseable objects

### Design Mistakes
- Catching Exception instead of specific types
- Using exceptions for control flow
- Not providing meaningful error messages
- Ignoring exceptions silently
- Not logging errors for debugging

## Real-world Impact

### Without Proper Exception Handling
- Applications crash unexpectedly
- Data corruption and loss
- Poor user experience
- Difficult debugging and maintenance
- System instability

### With Proper Exception Handling
- Graceful error recovery
- Data integrity maintained
- User-friendly error messages
- Easy debugging and troubleshooting
- Robust, stable applications

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Try-Catch-Finally Blocks Complete

**Lecture 27 Successfully Completed!**  
You now know how to handle exceptions gracefully in Java

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready to create robust applications! <carbon:arrow-right class="inline"/>
  </span>
</div>