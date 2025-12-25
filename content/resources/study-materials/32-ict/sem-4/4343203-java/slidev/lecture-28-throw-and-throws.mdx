---
theme: default
background: https://source.unsplash.com/1024x768/?warning,alert
title: Throw and Throws Keywords
info: |
  ## Java Programming (4343203)
  
  Lecture 28: Throw and Throws Keywords
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about throw and throws keywords, creating and throwing exceptions, method declarations, and exception chaining in Java.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Throw and Throws Keywords
## Lecture 28

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

- 🎯 **Understand** the difference between throw and throws keywords
- 🚀 **Use** the throw keyword to create and throw exceptions manually
- 📋 **Implement** the throws keyword for method exception declarations
- ⚡ **Create** custom validation logic using throw statements
- 🔧 **Handle** both checked and unchecked exception declarations
- 🎭 **Apply** exception chaining for better error tracing
- 🏗️ **Design** methods with proper exception handling contracts

</v-clicks>

---
layout: default
---

# The 'throw' Keyword

<div class="grid grid-cols-2 gap-6">

<div>

## Basic 'throw' Syntax
The **throw** keyword is used to explicitly throw an exception from within a method or block.

```java
// Basic syntax
throw new ExceptionType("Error message");

// Examples
throw new IllegalArgumentException("Age cannot be negative");
throw new ArithmeticException("Division by zero attempted");
throw new NullPointerException("Object reference is null");
```

## Simple throw Example
```java
public class ThrowExample {
    public static void validateAge(int age) {
        System.out.println("Validating age: " + age);
        
        if (age < 0) {
            // Manually throw an exception
            throw new IllegalArgumentException(
                "Age cannot be negative. Received: " + age);
        }
        
        if (age > 150) {
            throw new IllegalArgumentException(
                "Age cannot exceed 150. Received: " + age);
        }
        
        System.out.println("Age validation successful: " + age);
    }
    
    public static void main(String[] args) {
        try {
            validateAge(25);    // Valid age
            validateAge(-5);    // Will throw exception
            validateAge(100);   // This won't execute
            
        } catch (IllegalArgumentException e) {
            System.out.println("Validation Error: " + e.getMessage());
        }
    }
}

/* Output:
Validating age: 25
Age validation successful: 25
Validating age: -5
Validation Error: Age cannot be negative. Received: -5
*/
```

</div>

<div>

## When to Use 'throw'

### 1. Input Validation
```java
public class BankAccount {
    private double balance;
    
    public void withdraw(double amount) {
        // Validate input parameters
        if (amount <= 0) {
            throw new IllegalArgumentException(
                "Withdrawal amount must be positive: " + amount);
        }
        
        if (amount > balance) {
            throw new IllegalArgumentException(
                "Insufficient funds. Balance: " + balance + 
                ", Requested: " + amount);
        }
        
        balance -= amount;
        System.out.println("Withdrawal successful. New balance: " + balance);
    }
    
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException(
                "Deposit amount must be positive: " + amount);
        }
        
        if (Double.isInfinite(amount) || Double.isNaN(amount)) {
            throw new IllegalArgumentException(
                "Invalid deposit amount: " + amount);
        }
        
        balance += amount;
        System.out.println("Deposit successful. New balance: " + balance);
    }
}
```

### 2. State Validation
```java
public class DatabaseConnection {
    private boolean isConnected = false;
    
    public void executeQuery(String query) {
        // Check object state before operation
        if (!isConnected) {
            throw new IllegalStateException(
                "Cannot execute query: Database not connected");
        }
        
        if (query == null || query.trim().isEmpty()) {
            throw new IllegalArgumentException(
                "Query cannot be null or empty");
        }
        
        System.out.println("Executing query: " + query);
        // Query execution logic here
    }
    
    public void connect() {
        if (isConnected) {
            throw new IllegalStateException(
                "Already connected to database");
        }
        
        isConnected = true;
        System.out.println("Database connection established");
    }
}
```

</div>

</div>

---
layout: default
---

# The 'throws' Keyword

<div class="grid grid-cols-2 gap-6">

<div>

## Basic 'throws' Syntax
The **throws** keyword is used in method signatures to declare that a method might throw certain exceptions.

```java
// Method that declares it might throw exceptions
public void methodName() throws ExceptionType1, ExceptionType2 {
    // Method implementation
}

// Examples
public void readFile(String filename) throws IOException {
    // File reading code that might throw IOException
}

public void connectToDatabase() throws SQLException, ClassNotFoundException {
    // Database connection code
}
```

## Simple throws Example
```java
public class ThrowsExample {
    // Method declares it might throw IOException
    public static String readFileContent(String filename) throws IOException {
        System.out.println("Attempting to read file: " + filename);
        
        // This might throw FileNotFoundException (subclass of IOException)
        FileReader file = new FileReader(filename);
        BufferedReader reader = new BufferedReader(file);
        
        StringBuilder content = new StringBuilder();
        String line;
        
        // This might throw IOException
        while ((line = reader.readLine()) != null) {
            content.append(line).append("\n");
        }
        
        reader.close();
        file.close();
        
        return content.toString();
    }
    
    public static void main(String[] args) {
        try {
            // Must handle the declared exception
            String content = readFileContent("data.txt");
            System.out.println("File content:\n" + content);
            
        } catch (IOException e) {
            System.out.println("File reading failed: " + e.getMessage());
        }
    }
}
```

</div>

<div>

## Checked vs Unchecked Exceptions with throws

### Checked Exceptions (Must Declare)
```java
public class CheckedExceptionExample {
    // Must declare IOException - it's checked
    public void writeToFile(String filename, String data) throws IOException {
        FileWriter writer = new FileWriter(filename);
        writer.write(data);
        writer.close();
    }
    
    // Must declare SQLException - it's checked
    public void queryDatabase(String query) throws SQLException {
        Connection conn = DriverManager.getConnection("jdbc:mysql://...");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        // Process results
    }
    
    // Must declare ClassNotFoundException - it's checked
    public Object createInstance(String className) throws ClassNotFoundException {
        Class<?> clazz = Class.forName(className);
        try {
            return clazz.newInstance();
        } catch (InstantiationException | IllegalAccessException e) {
            // Convert to unchecked exception
            throw new RuntimeException("Cannot create instance", e);
        }
    }
}
```

### Unchecked Exceptions (Optional to Declare)
```java
public class UncheckedExceptionExample {
    // Optional to declare RuntimeException - it's unchecked
    public void validateInput(String input) throws IllegalArgumentException {
        if (input == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        
        if (input.trim().isEmpty()) {
            throw new IllegalArgumentException("Input cannot be empty");
        }
    }
    
    // Can throw RuntimeException without declaring
    public int divide(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return a / b;
    }
    
    // Optional to declare - but good practice for documentation
    public void processArray(int[] arr, int index) throws ArrayIndexOutOfBoundsException {
        if (index < 0 || index >= arr.length) {
            throw new ArrayIndexOutOfBoundsException(
                "Index " + index + " out of bounds for array of length " + arr.length);
        }
        
        System.out.println("Processing element: " + arr[index]);
    }
}
```

</div>

</div>

---
layout: default
---

# Combining throw and throws

<div class="grid grid-cols-2 gap-6">

<div>

## Method with Both throw and throws
```java
public class ValidationService {
    // Method declares what it might throw
    public void validateUser(User user) throws ValidationException {
        System.out.println("Validating user: " + user.getName());
        
        // Check name
        if (user.getName() == null || user.getName().trim().isEmpty()) {
            // Explicitly throw the declared exception
            throw new ValidationException("User name cannot be empty");
        }
        
        // Check email
        if (user.getEmail() == null || !user.getEmail().contains("@")) {
            throw new ValidationException("Invalid email format: " + user.getEmail());
        }
        
        // Check age
        if (user.getAge() < 0 || user.getAge() > 150) {
            throw new ValidationException("Age must be between 0 and 150: " + user.getAge());
        }
        
        System.out.println("User validation successful");
    }
    
    // Method that calls another method with throws
    public boolean processUserRegistration(User user) {
        try {
            validateUser(user); // Must handle ValidationException
            
            // Additional processing
            saveUserToDatabase(user);  // Might throw SQLException
            sendWelcomeEmail(user);     // Might throw MailException
            
            System.out.println("User registration completed successfully");
            return true;
            
        } catch (ValidationException e) {
            System.err.println("Validation failed: " + e.getMessage());
            return false;
            
        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
            return false;
            
        } catch (MailException e) {
            System.err.println("Email sending failed: " + e.getMessage());
            // User is registered but email failed - still success
            return true;
            
        } catch (Exception e) {
            System.err.println("Unexpected error: " + e.getMessage());
            return false;
        }
    }
    
    private void saveUserToDatabase(User user) throws SQLException {
        // Database save logic that might throw SQLException
        System.out.println("Saving user to database: " + user.getName());
    }
    
    private void sendWelcomeEmail(User user) throws MailException {
        // Email sending logic that might throw MailException
        System.out.println("Sending welcome email to: " + user.getEmail());
    }
}
```

</div>

<div>

## Exception Propagation Chain
```java
public class FileProcessor {
    // Low-level method that detects and throws
    public String readConfigValue(String filename, String key) 
            throws IOException, ConfigurationException {
        
        try {
            // This might throw IOException
            Properties props = new Properties();
            FileInputStream fis = new FileInputStream(filename);
            props.load(fis);
            fis.close();
            
            String value = props.getProperty(key);
            if (value == null) {
                // Throw custom exception with context
                throw new ConfigurationException(
                    "Configuration key '" + key + "' not found in " + filename);
            }
            
            return value;
            
        } catch (IOException e) {
            // Re-throw IOException with more context
            throw new IOException("Failed to read configuration file: " + filename, e);
        }
    }
    
    // Mid-level method that propagates
    public DatabaseConfig loadDatabaseConfig() throws ConfigurationException {
        try {
            String host = readConfigValue("db.properties", "db.host");
            String port = readConfigValue("db.properties", "db.port");
            String database = readConfigValue("db.properties", "db.name");
            
            return new DatabaseConfig(host, Integer.parseInt(port), database);
            
        } catch (IOException e) {
            // Convert IOException to ConfigurationException
            throw new ConfigurationException("Database configuration loading failed", e);
            
        } catch (NumberFormatException e) {
            throw new ConfigurationException("Invalid port number in database configuration", e);
        }
    }
    
    // High-level method that handles
    public void initializeApplication() {
        try {
            DatabaseConfig config = loadDatabaseConfig();
            System.out.println("Application initialized with config: " + config);
            
        } catch (ConfigurationException e) {
            System.err.println("Configuration Error: " + e.getMessage());
            
            // Print the full exception chain
            Throwable cause = e.getCause();
            while (cause != null) {
                System.err.println("Caused by: " + cause.getMessage());
                cause = cause.getCause();
            }
            
            // Use default configuration
            useDefaultConfiguration();
        }
    }
    
    private void useDefaultConfiguration() {
        System.out.println("Using default database configuration");
        // Initialize with defaults
    }
}
```

</div>

</div>

---
layout: default
---

# Exception Chaining and Re-throwing

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Chaining
Exception chaining allows you to preserve the original exception while throwing a new one:

```java
public class ExceptionChainingExample {
    // Method that chains exceptions
    public void processData(String data) throws DataProcessingException {
        try {
            // Step 1: Parse data
            parseData(data);
            
            // Step 2: Validate parsed data
            validateData(data);
            
            // Step 3: Transform data
            transformData(data);
            
        } catch (ParseException e) {
            // Chain the original exception
            throw new DataProcessingException(
                "Failed to process data due to parsing error", e);
                
        } catch (ValidationException e) {
            // Chain the original exception
            throw new DataProcessingException(
                "Failed to process data due to validation error", e);
                
        } catch (TransformationException e) {
            // Chain the original exception
            throw new DataProcessingException(
                "Failed to process data due to transformation error", e);
        }
    }
    
    private void parseData(String data) throws ParseException {
        if (data == null) {
            throw new ParseException("Data cannot be null", 0);
        }
        
        if (!data.startsWith("{")) {
            throw new ParseException("Invalid data format: must start with '{'", 0);
        }
        
        System.out.println("Data parsing completed");
    }
    
    private void validateData(String data) throws ValidationException {
        if (data.length() < 10) {
            throw new ValidationException("Data too short: minimum 10 characters required");
        }
        
        System.out.println("Data validation completed");
    }
    
    private void transformData(String data) throws TransformationException {
        try {
            // Simulate complex transformation that might fail
            if (data.contains("ERROR")) {
                throw new RuntimeException("Transformation failed on ERROR keyword");
            }
            
            System.out.println("Data transformation completed");
            
        } catch (RuntimeException e) {
            // Wrap runtime exception in checked exception
            throw new TransformationException("Data transformation failed", e);
        }
    }
}
```

</div>

<div>

## Re-throwing Exceptions
Sometimes you want to catch an exception, do some processing, then re-throw:

```java
public class ReThrowingExample {
    private static final Logger logger = Logger.getLogger(ReThrowingExample.class.getName());
    
    public void processFile(String filename) throws IOException {
        try {
            System.out.println("Starting file processing: " + filename);
            
            // Risky file operation
            FileReader reader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(reader);
            
            String line;
            int lineCount = 0;
            while ((line = bufferedReader.readLine()) != null) {
                lineCount++;
                processLine(line, lineCount);
            }
            
            bufferedReader.close();
            reader.close();
            
            System.out.println("File processing completed successfully");
            
        } catch (FileNotFoundException e) {
            // Log the error but re-throw
            logger.error("File not found: " + filename, e);
            
            // Re-throw the same exception
            throw e;
            
        } catch (IOException e) {
            // Log the error and re-throw with additional context
            logger.error("IO error while processing file: " + filename, e);
            
            // Re-throw with additional message
            throw new IOException("Failed to process file: " + filename, e);
        }
    }
    
    private void processLine(String line, int lineNumber) throws IOException {
        try {
            // Process individual line
            if (line.trim().isEmpty()) {
                return; // Skip empty lines
            }
            
            // Simulate line processing that might fail
            if (line.contains("CORRUPT")) {
                throw new RuntimeException("Corrupted data found in line");
            }
            
            System.out.println("Processed line " + lineNumber + ": " + line.substring(0, Math.min(20, line.length())));
            
        } catch (RuntimeException e) {
            // Convert runtime exception to checked IOException with context
            throw new IOException("Error processing line " + lineNumber + ": " + line, e);
        }
    }
    
    // Method that handles the re-thrown exceptions
    public void handleFileProcessing(String filename) {
        try {
            processFile(filename);
            
        } catch (IOException e) {
            System.err.println("File processing failed: " + e.getMessage());
            
            // Print the full exception chain
            System.err.println("Exception chain:");
            Throwable current = e;
            int level = 0;
            while (current != null) {
                System.err.println("  " + "  ".repeat(level) + current.getClass().getSimpleName() + 
                                 ": " + current.getMessage());
                current = current.getCause();
                level++;
            }
        }
    }
}
```

## Exception Suppression (Java 7+)
```java
public class ExceptionSuppressionExample {
    public void demonstrateSuppression() throws IOException {
        FileInputStream input = null;
        
        try {
            input = new FileInputStream("data.txt");
            
            // This might throw an exception
            processFile(input);
            
        } finally {
            if (input != null) {
                try {
                    input.close(); // This might also throw an exception
                } catch (IOException closeException) {
                    // If an exception was already thrown in try block,
                    // this close exception will be suppressed
                    System.err.println("Error closing file: " + closeException.getMessage());
                }
            }
        }
    }
    
    // Better approach with try-with-resources (automatic suppression)
    public void demonstrateAutomaticSuppression() throws IOException {
        try (FileInputStream input = new FileInputStream("data.txt")) {
            processFile(input);
            // If both processFile() and close() throw exceptions,
            // the close() exception will be automatically suppressed
        }
    }
    
    private void processFile(FileInputStream input) throws IOException {
        // File processing logic that might throw IOException
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Validation Examples

<div class="grid grid-cols-2 gap-6">

<div>

## 1. User Registration System
```java
public class UserRegistrationService {
    
    public void registerUser(String username, String password, String email, int age) 
            throws RegistrationException {
        
        try {
            // Validate each field
            validateUsername(username);
            validatePassword(password);
            validateEmail(email);
            validateAge(age);
            
            // Check if user already exists
            checkUserExists(username, email);
            
            // Create and save user
            User user = new User(username, password, email, age);
            saveUser(user);
            
            System.out.println("User registered successfully: " + username);
            
        } catch (ValidationException e) {
            // Convert validation exception to registration exception
            throw new RegistrationException("Registration failed: " + e.getMessage(), e);
            
        } catch (UserAlreadyExistsException e) {
            throw new RegistrationException("Registration failed: " + e.getMessage(), e);
            
        } catch (DatabaseException e) {
            throw new RegistrationException("Registration failed due to system error", e);
        }
    }
    
    private void validateUsername(String username) throws ValidationException {
        if (username == null || username.trim().isEmpty()) {
            throw new ValidationException("Username cannot be empty");
        }
        
        if (username.length() < 3) {
            throw new ValidationException("Username must be at least 3 characters long");
        }
        
        if (username.length() > 20) {
            throw new ValidationException("Username cannot exceed 20 characters");
        }
        
        if (!username.matches("[a-zA-Z0-9_]+")) {
            throw new ValidationException("Username can only contain letters, numbers, and underscores");
        }
    }
    
    private void validatePassword(String password) throws ValidationException {
        if (password == null || password.isEmpty()) {
            throw new ValidationException("Password cannot be empty");
        }
        
        if (password.length() < 8) {
            throw new ValidationException("Password must be at least 8 characters long");
        }
        
        boolean hasUpper = password.chars().anyMatch(Character::isUpperCase);
        boolean hasLower = password.chars().anyMatch(Character::isLowerCase);
        boolean hasDigit = password.chars().anyMatch(Character::isDigit);
        
        if (!hasUpper || !hasLower || !hasDigit) {
            throw new ValidationException(
                "Password must contain at least one uppercase letter, one lowercase letter, and one digit");
        }
    }
    
    private void validateEmail(String email) throws ValidationException {
        if (email == null || email.trim().isEmpty()) {
            throw new ValidationException("Email cannot be empty");
        }
        
        String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$";
        if (!email.matches(emailRegex)) {
            throw new ValidationException("Invalid email format: " + email);
        }
    }
    
    private void validateAge(int age) throws ValidationException {
        if (age < 13) {
            throw new ValidationException("Age must be at least 13 years");
        }
        
        if (age > 120) {
            throw new ValidationException("Age cannot exceed 120 years");
        }
    }
    
    private void checkUserExists(String username, String email) 
            throws UserAlreadyExistsException, DatabaseException {
        // Simulate database check
        if (isUsernameTaken(username)) {
            throw new UserAlreadyExistsException("Username already exists: " + username);
        }
        
        if (isEmailTaken(email)) {
            throw new UserAlreadyExistsException("Email already registered: " + email);
        }
    }
    
    private boolean isUsernameTaken(String username) throws DatabaseException {
        // Simulate database query
        return false; // Simplified
    }
    
    private boolean isEmailTaken(String email) throws DatabaseException {
        // Simulate database query
        return false; // Simplified
    }
    
    private void saveUser(User user) throws DatabaseException {
        // Simulate user saving
        System.out.println("Saving user to database: " + user.getUsername());
    }
}
```

</div>

<div>

## 2. File Upload System
```java
public class FileUploadService {
    private static final long MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
    private static final Set<String> ALLOWED_EXTENSIONS = 
        Set.of("jpg", "jpeg", "png", "gif", "pdf", "doc", "docx");
    
    public String uploadFile(MultipartFile file, String uploadDir) 
            throws FileUploadException {
        
        try {
            // Validate file
            validateFile(file);
            
            // Create upload directory
            createUploadDirectory(uploadDir);
            
            // Generate unique filename
            String filename = generateUniqueFilename(file.getOriginalFilename());
            String fullPath = uploadDir + "/" + filename;
            
            // Save file
            saveFile(file, fullPath);
            
            // Verify file was saved correctly
            verifyFileSaved(fullPath, file.getSize());
            
            System.out.println("File uploaded successfully: " + filename);
            return filename;
            
        } catch (ValidationException e) {
            throw new FileUploadException("File validation failed: " + e.getMessage(), e);
            
        } catch (IOException e) {
            throw new FileUploadException("File save failed: " + e.getMessage(), e);
            
        } catch (SecurityException e) {
            throw new FileUploadException("Permission denied: " + e.getMessage(), e);
        }
    }
    
    private void validateFile(MultipartFile file) throws ValidationException {
        if (file == null || file.isEmpty()) {
            throw new ValidationException("File is empty or null");
        }
        
        // Check file size
        if (file.getSize() > MAX_FILE_SIZE) {
            throw new ValidationException(
                "File size (" + file.getSize() + " bytes) exceeds maximum allowed (" + 
                MAX_FILE_SIZE + " bytes)");
        }
        
        // Check filename
        String originalFilename = file.getOriginalFilename();
        if (originalFilename == null || originalFilename.trim().isEmpty()) {
            throw new ValidationException("Invalid filename");
        }
        
        // Check file extension
        String extension = getFileExtension(originalFilename);
        if (!ALLOWED_EXTENSIONS.contains(extension.toLowerCase())) {
            throw new ValidationException(
                "File type not allowed: " + extension + ". Allowed types: " + ALLOWED_EXTENSIONS);
        }
        
        // Check for potentially dangerous filenames
        if (originalFilename.contains("..") || originalFilename.contains("/") || originalFilename.contains("\\")) {
            throw new ValidationException("Filename contains invalid characters: " + originalFilename);
        }
    }
    
    private void createUploadDirectory(String uploadDir) throws IOException {
        File directory = new File(uploadDir);
        
        if (!directory.exists()) {
            boolean created = directory.mkdirs();
            if (!created) {
                throw new IOException("Failed to create upload directory: " + uploadDir);
            }
        }
        
        if (!directory.canWrite()) {
            throw new SecurityException("Cannot write to upload directory: " + uploadDir);
        }
    }
    
    private String generateUniqueFilename(String originalFilename) {
        String extension = getFileExtension(originalFilename);
        String baseName = getBaseName(originalFilename);
        String timestamp = String.valueOf(System.currentTimeMillis());
        String random = String.valueOf((int)(Math.random() * 1000));
        
        return baseName + "_" + timestamp + "_" + random + "." + extension;
    }
    
    private void saveFile(MultipartFile file, String fullPath) throws IOException {
        try (InputStream inputStream = file.getInputStream();
             FileOutputStream outputStream = new FileOutputStream(fullPath)) {
            
            byte[] buffer = new byte[8192];
            int bytesRead;
            long totalBytesRead = 0;
            long fileSize = file.getSize();
            
            while ((bytesRead = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, bytesRead);
                totalBytesRead += bytesRead;
                
                // Show progress for large files
                if (fileSize > 1024 * 1024) { // Files larger than 1MB
                    int progress = (int) ((totalBytesRead * 100) / fileSize);
                    if (progress % 10 == 0) {
                        System.out.println("Upload progress: " + progress + "%");
                    }
                }
            }
        }
    }
    
    private void verifyFileSaved(String fullPath, long expectedSize) throws IOException {
        File savedFile = new File(fullPath);
        
        if (!savedFile.exists()) {
            throw new IOException("File was not saved: " + fullPath);
        }
        
        if (savedFile.length() != expectedSize) {
            // Delete incomplete file
            savedFile.delete();
            throw new IOException(
                "File size mismatch. Expected: " + expectedSize + ", Actual: " + savedFile.length());
        }
    }
    
    private String getFileExtension(String filename) {
        int lastDotIndex = filename.lastIndexOf('.');
        if (lastDotIndex == -1) {
            throw new IllegalArgumentException("File has no extension: " + filename);
        }
        return filename.substring(lastDotIndex + 1);
    }
    
    private String getBaseName(String filename) {
        int lastDotIndex = filename.lastIndexOf('.');
        if (lastDotIndex == -1) {
            return filename;
        }
        return filename.substring(0, lastDotIndex);
    }
}
```

</div>

</div>

---
layout: default
---

# Method Signature Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Declaration Guidelines

### 1. Be Specific with Exception Types
```java
// BAD: Too generic
public void processData(String data) throws Exception {
    // What could go wrong? Hard to tell!
}

// GOOD: Specific exception types
public void processData(String data) 
        throws ParseException, ValidationException, TransformationException {
    // Clear what exceptions to expect and handle
}

// EVEN BETTER: Custom exception hierarchy
public void processData(String data) throws DataProcessingException {
    // Single exception type that wraps specific causes
}
```

### 2. Document Exception Conditions
```java
public class OrderService {
    /**
     * Processes a customer order
     * 
     * @param order The order to process
     * @throws IllegalArgumentException if order is null or invalid
     * @throws InsufficientInventoryException if items are out of stock
     * @throws PaymentProcessingException if payment fails
     * @throws OrderProcessingException if order cannot be processed
     */
    public void processOrder(Order order) 
            throws IllegalArgumentException, 
                   InsufficientInventoryException,
                   PaymentProcessingException, 
                   OrderProcessingException {
        
        // Validate order
        if (order == null) {
            throw new IllegalArgumentException("Order cannot be null");
        }
        
        if (order.getItems().isEmpty()) {
            throw new IllegalArgumentException("Order must contain at least one item");
        }
        
        // Check inventory
        for (OrderItem item : order.getItems()) {
            if (!isInStock(item)) {
                throw new InsufficientInventoryException(
                    "Item out of stock: " + item.getProductName());
            }
        }
        
        // Process payment
        try {
            processPayment(order.getPaymentInfo(), order.getTotalAmount());
        } catch (PaymentException e) {
            throw new PaymentProcessingException("Payment failed", e);
        }
        
        // Save order
        try {
            saveOrder(order);
        } catch (DatabaseException e) {
            throw new OrderProcessingException("Failed to save order", e);
        }
    }
    
    private boolean isInStock(OrderItem item) {
        // Check inventory logic
        return true; // Simplified
    }
    
    private void processPayment(PaymentInfo paymentInfo, BigDecimal amount) 
            throws PaymentException {
        // Payment processing logic
    }
    
    private void saveOrder(Order order) throws DatabaseException {
        // Database save logic
    }
}
```

</div>

<div>

## Exception Hierarchy Design

### 1. Create Meaningful Exception Hierarchies
```java
// Base application exception
public class ApplicationException extends Exception {
    public ApplicationException(String message) {
        super(message);
    }
    
    public ApplicationException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Business logic exceptions
public class BusinessException extends ApplicationException {
    public BusinessException(String message) {
        super(message);
    }
    
    public BusinessException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Specific business exceptions
public class ValidationException extends BusinessException {
    private String fieldName;
    private Object invalidValue;
    
    public ValidationException(String message, String fieldName, Object invalidValue) {
        super(message);
        this.fieldName = fieldName;
        this.invalidValue = invalidValue;
    }
    
    public String getFieldName() { return fieldName; }
    public Object getInvalidValue() { return invalidValue; }
}

public class InsufficientFundsException extends BusinessException {
    private BigDecimal requestedAmount;
    private BigDecimal availableAmount;
    
    public InsufficientFundsException(BigDecimal requested, BigDecimal available) {
        super("Insufficient funds. Requested: " + requested + ", Available: " + available);
        this.requestedAmount = requested;
        this.availableAmount = available;
    }
    
    public BigDecimal getRequestedAmount() { return requestedAmount; }
    public BigDecimal getAvailableAmount() { return availableAmount; }
}

// System-level exceptions
public class SystemException extends ApplicationException {
    public SystemException(String message) {
        super(message);
    }
    
    public SystemException(String message, Throwable cause) {
        super(message, cause);
    }
}

public class DatabaseException extends SystemException {
    private String operation;
    
    public DatabaseException(String operation, String message, Throwable cause) {
        super("Database operation failed: " + operation + " - " + message, cause);
        this.operation = operation;
    }
    
    public String getOperation() { return operation; }
}
```

### 2. Exception Handling Strategy
```java
public class ServiceLayer {
    // Service methods catch and convert exceptions appropriately
    public void transferMoney(String fromAccount, String toAccount, BigDecimal amount) 
            throws BusinessException {
        try {
            // Call DAO layer
            Account from = accountDao.findById(fromAccount);
            Account to = accountDao.findById(toAccount);
            
            // Business validation
            if (from.getBalance().compareTo(amount) < 0) {
                throw new InsufficientFundsException(amount, from.getBalance());
            }
            
            // Perform transfer
            from.debit(amount);
            to.credit(amount);
            
            accountDao.update(from);
            accountDao.update(to);
            
        } catch (DatabaseException e) {
            // Convert system exception to business exception
            throw new BusinessException("Transfer failed due to system error", e);
            
        } catch (BusinessException e) {
            // Re-throw business exceptions as-is
            throw e;
            
        } catch (Exception e) {
            // Convert unexpected exceptions
            throw new BusinessException("Unexpected error during transfer", e);
        }
    }
}

public class ControllerLayer {
    // Controllers handle business exceptions and return appropriate responses
    public ResponseEntity<?> transferMoney(TransferRequest request) {
        try {
            serviceLayer.transferMoney(
                request.getFromAccount(), 
                request.getToAccount(), 
                request.getAmount()
            );
            
            return ResponseEntity.ok("Transfer completed successfully");
            
        } catch (InsufficientFundsException e) {
            return ResponseEntity.badRequest()
                .body("Insufficient funds: " + e.getMessage());
                
        } catch (ValidationException e) {
            return ResponseEntity.badRequest()
                .body("Validation error: " + e.getMessage());
                
        } catch (BusinessException e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body("Service temporarily unavailable");
                
        } catch (Exception e) {
            // Log unexpected exceptions
            logger.error("Unexpected error in transferMoney", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body("An unexpected error occurred");
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Employee Management System

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build Employee Validation System
Create a comprehensive employee management system with proper exception handling:

```java
public class EmployeeService {
    private List<Employee> employees = new ArrayList<>();
    
    // TODO: Implement with proper throw/throws
    public void addEmployee(Employee employee) throws EmployeeException {
        // Validate employee data
        // Check for duplicates
        // Add to collection
    }
    
    // TODO: Implement with proper validation
    public void validateEmployee(Employee employee) throws ValidationException {
        // Validate name (not null, not empty, reasonable length)
        // Validate employee ID (format: EMP-XXXX)
        // Validate email (proper format)
        // Validate age (18-65 years)
        // Validate salary (positive, reasonable range)
        // Validate department (not null, valid department)
    }
    
    // TODO: Implement with proper exception handling
    public Employee findEmployeeById(String employeeId) throws EmployeeNotFoundException {
        // Search for employee
        // Throw exception if not found
    }
    
    // TODO: Implement with proper validation
    public void updateEmployee(String employeeId, Employee updatedEmployee) 
            throws EmployeeNotFoundException, ValidationException {
        // Find existing employee
        // Validate updated data
        // Update employee
    }
    
    // TODO: Implement with business rules
    public void promoteEmployee(String employeeId, String newDepartment, 
                               BigDecimal newSalary) 
            throws EmployeeNotFoundException, PromotionException {
        // Find employee
        // Validate promotion rules
        // Apply promotion
    }
    
    // TODO: Implement batch operation with error handling
    public EmployeeImportResult importEmployees(List<Employee> employeesToImport) {
        // Import employees one by one
        // Collect successes and failures
        // Return detailed result
    }
}

class Employee {
    private String employeeId;
    private String name;
    private String email;
    private int age;
    private BigDecimal salary;
    private String department;
    
    // Constructor, getters, setters
}

class EmployeeImportResult {
    private int successCount;
    private int failureCount;
    private List<String> errors;
    
    // Constructor, getters, setters
}
```

**Requirements:**
- Create custom exception hierarchy
- Implement comprehensive validation
- Use throw for validation failures
- Use throws for method declarations
- Handle batch operations gracefully

</div>

<div>

## Solution Framework

```java
// Exception hierarchy
public abstract class EmployeeException extends Exception {
    public EmployeeException(String message) {
        super(message);
    }
    
    public EmployeeException(String message, Throwable cause) {
        super(message, cause);
    }
}

public class ValidationException extends EmployeeException {
    private String fieldName;
    private Object invalidValue;
    
    public ValidationException(String fieldName, Object invalidValue, String message) {
        super("Validation failed for " + fieldName + ": " + message);
        this.fieldName = fieldName;
        this.invalidValue = invalidValue;
    }
    
    public String getFieldName() { return fieldName; }
    public Object getInvalidValue() { return invalidValue; }
}

public class EmployeeNotFoundException extends EmployeeException {
    private String employeeId;
    
    public EmployeeNotFoundException(String employeeId) {
        super("Employee not found: " + employeeId);
        this.employeeId = employeeId;
    }
    
    public String getEmployeeId() { return employeeId; }
}

public class DuplicateEmployeeException extends EmployeeException {
    public DuplicateEmployeeException(String employeeId) {
        super("Employee already exists: " + employeeId);
    }
}

public class PromotionException extends EmployeeException {
    public PromotionException(String message) {
        super(message);
    }
}

// Validation implementation
public void validateEmployee(Employee employee) throws ValidationException {
    // Name validation
    if (employee.getName() == null || employee.getName().trim().isEmpty()) {
        throw new ValidationException("name", employee.getName(), "Name cannot be empty");
    }
    
    if (employee.getName().length() > 100) {
        throw new ValidationException("name", employee.getName(), "Name too long (max 100 characters)");
    }
    
    // Employee ID validation
    String employeeId = employee.getEmployeeId();
    if (employeeId == null || !employeeId.matches("EMP-\\d{4}")) {
        throw new ValidationException("employeeId", employeeId, "Invalid format (expected: EMP-XXXX)");
    }
    
    // Email validation
    String email = employee.getEmail();
    if (email == null || !email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$")) {
        throw new ValidationException("email", email, "Invalid email format");
    }
    
    // Age validation
    int age = employee.getAge();
    if (age < 18 || age > 65) {
        throw new ValidationException("age", age, "Age must be between 18 and 65");
    }
    
    // Salary validation
    BigDecimal salary = employee.getSalary();
    if (salary == null || salary.compareTo(BigDecimal.ZERO) <= 0) {
        throw new ValidationException("salary", salary, "Salary must be positive");
    }
    
    if (salary.compareTo(new BigDecimal("1000000")) > 0) {
        throw new ValidationException("salary", salary, "Salary exceeds maximum limit");
    }
    
    // Department validation
    String department = employee.getDepartment();
    Set<String> validDepartments = Set.of("HR", "IT", "FINANCE", "MARKETING", "OPERATIONS");
    if (department == null || !validDepartments.contains(department.toUpperCase())) {
        throw new ValidationException("department", department, "Invalid department");
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Configuration Manager

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build Configuration System
Create a robust configuration manager with comprehensive error handling:

```java
public class ConfigurationManager {
    private Properties properties = new Properties();
    private boolean isLoaded = false;
    
    // TODO: Implement with multiple exception types
    public void loadConfiguration(String... configFiles) 
            throws ConfigurationException {
        // Load configuration from multiple files
        // Handle missing files gracefully
        // Validate configuration after loading
        // Support property inheritance/override
    }
    
    // TODO: Implement with validation
    public void validateConfiguration() throws ConfigurationException {
        // Check required properties exist
        // Validate property formats and ranges
        // Check property dependencies
    }
    
    // TODO: Implement with type conversion and validation
    public String getStringProperty(String key) throws PropertyException {
        // Get string property
        // Throw exception if not found or invalid
    }
    
    public int getIntProperty(String key, int min, int max) throws PropertyException {
        // Get integer property with range validation
        // Convert string to int with error handling
    }
    
    public boolean getBooleanProperty(String key) throws PropertyException {
        // Get boolean property
        // Handle various boolean representations (true/false, yes/no, 1/0)
    }
    
    // TODO: Implement with fallback handling
    public DatabaseConfig getDatabaseConfig() throws ConfigurationException {
        // Extract database configuration
        // Validate database connection parameters
        // Test connection if requested
    }
    
    // TODO: Implement with encryption support
    public String getEncryptedProperty(String key) 
            throws PropertyException, DecryptionException {
        // Get encrypted property
        // Decrypt value
        // Handle decryption failures
    }
    
    // TODO: Implement configuration saving
    public void saveConfiguration(String filename) 
            throws IOException, SecurityException {
        // Save current configuration to file
        // Handle file permissions
        // Create backup of existing file
    }
}

// Supporting classes
class DatabaseConfig {
    private String host;
    private int port;
    private String database;
    private String username;
    private String password;
    
    // Constructor, getters, setters
}
```

**Requirements:**
- Handle multiple configuration sources
- Provide type-safe property access
- Support property validation
- Handle missing/corrupted configuration gracefully
- Provide meaningful error messages

</div>

<div>

## Solution Implementation

```java
// Exception hierarchy for configuration
public abstract class ConfigurationException extends Exception {
    public ConfigurationException(String message) {
        super(message);
    }
    
    public ConfigurationException(String message, Throwable cause) {
        super(message, cause);
    }
}

public class PropertyException extends ConfigurationException {
    private String propertyKey;
    
    public PropertyException(String propertyKey, String message) {
        super("Property '" + propertyKey + "': " + message);
        this.propertyKey = propertyKey;
    }
    
    public PropertyException(String propertyKey, String message, Throwable cause) {
        super("Property '" + propertyKey + "': " + message, cause);
        this.propertyKey = propertyKey;
    }
    
    public String getPropertyKey() { return propertyKey; }
}

public class ConfigurationValidationException extends ConfigurationException {
    private List<String> validationErrors;
    
    public ConfigurationValidationException(List<String> errors) {
        super("Configuration validation failed: " + String.join(", ", errors));
        this.validationErrors = new ArrayList<>(errors);
    }
    
    public List<String> getValidationErrors() { return validationErrors; }
}

// Implementation
public void loadConfiguration(String... configFiles) throws ConfigurationException {
    if (configFiles == null || configFiles.length == 0) {
        throw new ConfigurationException("No configuration files specified");
    }
    
    List<String> loadErrors = new ArrayList<>();
    boolean anyLoaded = false;
    
    for (String configFile : configFiles) {
        try {
            loadSingleConfiguration(configFile);
            System.out.println("Loaded configuration from: " + configFile);
            anyLoaded = true;
            
        } catch (IOException e) {
            String error = "Failed to load " + configFile + ": " + e.getMessage();
            loadErrors.add(error);
            System.err.println("Warning: " + error);
        }
    }
    
    if (!anyLoaded) {
        throw new ConfigurationException(
            "No configuration files could be loaded. Errors: " + String.join("; ", loadErrors));
    }
    
    // Validate configuration after loading
    validateConfiguration();
    
    isLoaded = true;
    System.out.println("Configuration loaded and validated successfully");
}

private void loadSingleConfiguration(String configFile) throws IOException {
    try (FileInputStream fis = new FileInputStream(configFile)) {
        properties.load(fis);
    }
}

public void validateConfiguration() throws ConfigurationException {
    List<String> errors = new ArrayList<>();
    
    // Check required properties
    String[] requiredProperties = {
        "database.host", "database.port", "database.name",
        "app.name", "app.version", "logging.level"
    };
    
    for (String required : requiredProperties) {
        if (!properties.containsKey(required) || 
            properties.getProperty(required).trim().isEmpty()) {
            errors.add("Required property missing or empty: " + required);
        }
    }
    
    // Validate specific property formats
    try {
        int port = getIntProperty("database.port", 1, 65535);
    } catch (PropertyException e) {
        errors.add(e.getMessage());
    }
    
    // Validate logging level
    String logLevel = properties.getProperty("logging.level");
    if (logLevel != null) {
        Set<String> validLevels = Set.of("TRACE", "DEBUG", "INFO", "WARN", "ERROR");
        if (!validLevels.contains(logLevel.toUpperCase())) {
            errors.add("Invalid logging level: " + logLevel);
        }
    }
    
    if (!errors.isEmpty()) {
        throw new ConfigurationValidationException(errors);
    }
}

public int getIntProperty(String key, int min, int max) throws PropertyException {
    if (!isLoaded) {
        throw new PropertyException(key, "Configuration not loaded");
    }
    
    String value = properties.getProperty(key);
    if (value == null) {
        throw new PropertyException(key, "Property not found");
    }
    
    try {
        int intValue = Integer.parseInt(value.trim());
        
        if (intValue < min || intValue > max) {
            throw new PropertyException(key, 
                "Value " + intValue + " is out of range [" + min + ", " + max + "]");
        }
        
        return intValue;
        
    } catch (NumberFormatException e) {
        throw new PropertyException(key, "Invalid integer format: " + value, e);
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

## 1. Banking Transaction System
```java
@Service
public class BankingTransactionService {
    
    /**
     * Transfers money between accounts
     * @throws InsufficientFundsException if source account lacks funds
     * @throws AccountNotFoundException if either account doesn't exist
     * @throws AccountFrozenException if either account is frozen
     * @throws TransferLimitException if transfer exceeds limits
     * @throws SystemException if system error occurs
     */
    @Transactional
    public TransactionResult transferMoney(String fromAccountId, String toAccountId, 
                                         BigDecimal amount, String description) 
            throws InsufficientFundsException, AccountNotFoundException, 
                   AccountFrozenException, TransferLimitException, SystemException {
        
        // Input validation
        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Transfer amount must be positive");
        }
        
        if (fromAccountId == null || toAccountId == null) {
            throw new IllegalArgumentException("Account IDs cannot be null");
        }
        
        if (fromAccountId.equals(toAccountId)) {
            throw new IllegalArgumentException("Cannot transfer to same account");
        }
        
        try {
            // Get accounts with locking
            Account fromAccount = getAccountForUpdate(fromAccountId);
            Account toAccount = getAccountForUpdate(toAccountId);
            
            // Validate account states
            validateAccountForTransfer(fromAccount, amount, true);  // source account
            validateAccountForTransfer(toAccount, amount, false);   // destination account
            
            // Check transfer limits
            validateTransferLimits(fromAccount, amount);
            
            // Perform the transfer
            fromAccount.debit(amount);
            toAccount.credit(amount);
            
            // Save accounts
            accountRepository.save(fromAccount);
            accountRepository.save(toAccount);
            
            // Record transaction
            Transaction transaction = createTransaction(
                fromAccountId, toAccountId, amount, description);
            transactionRepository.save(transaction);
            
            // Send notifications
            notifyAccountHolders(fromAccount, toAccount, amount, transaction.getId());
            
            logger.info("Transfer completed: {} from {} to {}", 
                       amount, fromAccountId, toAccountId);
            
            return new TransactionResult(transaction.getId(), "Transfer completed successfully");
            
        } catch (AccountNotFoundException | InsufficientFundsException | 
                 AccountFrozenException | TransferLimitException e) {
            // Business exceptions - log and re-throw
            logger.warn("Transfer failed - business rule violation: {}", e.getMessage());
            throw e;
            
        } catch (DataAccessException e) {
            // Database exceptions
            logger.error("Transfer failed - database error", e);
            throw new SystemException("Transfer failed due to system error", e);
            
        } catch (Exception e) {
            // Unexpected exceptions
            logger.error("Transfer failed - unexpected error", e);
            throw new SystemException("Transfer failed due to unexpected system error", e);
        }
    }
    
    private Account getAccountForUpdate(String accountId) throws AccountNotFoundException {
        Account account = accountRepository.findByIdForUpdate(accountId);
        if (account == null) {
            throw new AccountNotFoundException("Account not found: " + accountId);
        }
        return account;
    }
    
    private void validateAccountForTransfer(Account account, BigDecimal amount, boolean isSource) 
            throws AccountFrozenException, InsufficientFundsException {
        
        if (account.getStatus() == AccountStatus.FROZEN) {
            throw new AccountFrozenException("Account is frozen: " + account.getAccountId());
        }
        
        if (account.getStatus() == AccountStatus.CLOSED) {
            throw new AccountNotFoundException("Account is closed: " + account.getAccountId());
        }
        
        if (isSource && account.getBalance().compareTo(amount) < 0) {
            throw new InsufficientFundsException(
                "Insufficient funds. Available: " + account.getBalance() + 
                ", Requested: " + amount);
        }
    }
    
    private void validateTransferLimits(Account account, BigDecimal amount) 
            throws TransferLimitException {
        
        // Check single transaction limit
        if (amount.compareTo(account.getSingleTransferLimit()) > 0) {
            throw new TransferLimitException(
                "Amount exceeds single transfer limit: " + account.getSingleTransferLimit());
        }
        
        // Check daily limit
        BigDecimal todayTotal = transactionRepository.getDailyTransferTotal(
            account.getAccountId(), LocalDate.now());
            
        if (todayTotal.add(amount).compareTo(account.getDailyTransferLimit()) > 0) {
            throw new TransferLimitException(
                "Transfer would exceed daily limit: " + account.getDailyTransferLimit());
        }
    }
}
```

</div>

<div>

## 2. E-commerce Order Processing
```java
@Service
public class OrderProcessingService {
    
    /**
     * Processes customer order
     * @throws ValidationException if order data is invalid
     * @throws InventoryException if items are unavailable
     * @throws PaymentException if payment processing fails
     * @throws ShippingException if shipping calculation fails
     * @throws OrderException if order cannot be processed
     */
    public OrderResult processOrder(Order order) 
            throws ValidationException, InventoryException, PaymentException, 
                   ShippingException, OrderException {
        
        String orderId = generateOrderId();
        
        try {
            logger.info("Processing order: {}", orderId);
            
            // Step 1: Validate order
            validateOrder(order);
            
            // Step 2: Check inventory and reserve items
            List<InventoryReservation> reservations = reserveInventory(order.getItems());
            
            try {
                // Step 3: Calculate totals
                OrderTotals totals = calculateOrderTotals(order);
                
                // Step 4: Process payment
                PaymentResult paymentResult = processPayment(order.getPayment(), totals);
                
                try {
                    // Step 5: Calculate shipping
                    ShippingInfo shipping = calculateShipping(order);
                    
                    // Step 6: Create order record
                    Order savedOrder = createOrderRecord(order, orderId, totals, 
                                                        paymentResult, shipping);
                    
                    // Step 7: Update inventory
                    updateInventory(reservations);
                    
                    // Step 8: Send confirmation
                    sendOrderConfirmation(savedOrder);
                    
                    logger.info("Order processed successfully: {}", orderId);
                    return new OrderResult(orderId, OrderStatus.CONFIRMED, savedOrder);
                    
                } catch (Exception e) {
                    // Rollback payment if order creation fails
                    try {
                        refundPayment(paymentResult);
                    } catch (Exception refundException) {
                        logger.error("Failed to refund payment for failed order", refundException);
                    }
                    throw e;
                }
                
            } catch (Exception e) {
                // Release inventory reservations if payment or later steps fail
                releaseInventoryReservations(reservations);
                throw e;
            }
            
        } catch (ValidationException | InventoryException e) {
            // Business validation failures - don't retry
            logger.warn("Order processing failed - validation error: {}", e.getMessage());
            throw e;
            
        } catch (PaymentException e) {
            // Payment failures - might be retryable
            logger.warn("Order processing failed - payment error: {}", e.getMessage());
            throw e;
            
        } catch (Exception e) {
            // System errors
            logger.error("Order processing failed - system error", e);
            throw new OrderException("Order processing failed due to system error", e);
        }
    }
    
    private void validateOrder(Order order) throws ValidationException {
        List<String> errors = new ArrayList<>();
        
        // Validate customer
        if (order.getCustomerId() == null) {
            errors.add("Customer ID is required");
        }
        
        // Validate items
        if (order.getItems() == null || order.getItems().isEmpty()) {
            errors.add("Order must contain at least one item");
        } else {
            for (int i = 0; i < order.getItems().size(); i++) {
                OrderItem item = order.getItems().get(i);
                if (item.getProductId() == null) {
                    errors.add("Item " + (i + 1) + ": Product ID is required");
                }
                if (item.getQuantity() <= 0) {
                    errors.add("Item " + (i + 1) + ": Quantity must be positive");
                }
                if (item.getPrice() == null || item.getPrice().compareTo(BigDecimal.ZERO) <= 0) {
                    errors.add("Item " + (i + 1) + ": Valid price is required");
                }
            }
        }
        
        // Validate shipping address
        if (order.getShippingAddress() == null) {
            errors.add("Shipping address is required");
        } else {
            validateAddress(order.getShippingAddress(), "Shipping address", errors);
        }
        
        // Validate payment info
        if (order.getPayment() == null) {
            errors.add("Payment information is required");
        } else {
            validatePaymentInfo(order.getPayment(), errors);
        }
        
        if (!errors.isEmpty()) {
            throw new ValidationException("Order validation failed", errors);
        }
    }
    
    private List<InventoryReservation> reserveInventory(List<OrderItem> items) 
            throws InventoryException {
        
        List<InventoryReservation> reservations = new ArrayList<>();
        List<String> unavailableItems = new ArrayList<>();
        
        for (OrderItem item : items) {
            try {
                InventoryReservation reservation = inventoryService.reserveItem(
                    item.getProductId(), item.getQuantity());
                reservations.add(reservation);
                
            } catch (InsufficientInventoryException e) {
                unavailableItems.add(item.getProductId() + " (requested: " + 
                                   item.getQuantity() + ", available: " + e.getAvailableQuantity() + ")");
            }
        }
        
        if (!unavailableItems.isEmpty()) {
            // Release any successful reservations
            releaseInventoryReservations(reservations);
            
            throw new InventoryException(
                "The following items are not available: " + String.join(", ", unavailableItems));
        }
        
        return reservations;
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

- 🎯 **throw keyword**: Manually creating and throwing exceptions
- 📋 **throws keyword**: Declaring exceptions in method signatures  
- ⚡ **Exception chaining**: Preserving original exception information
- 🔧 **Re-throwing exceptions**: Catching, processing, and re-throwing
- 🎭 **Custom validation**: Creating business rule validation
- 🏗️ **Exception hierarchy**: Designing meaningful exception types
- 🚀 **Best practices**: Proper exception declaration and handling

</v-clicks>

## Key Differences: throw vs throws

### `throw` Statement
- **Used inside methods** to create and throw exceptions
- **Followed by exception object** (new ExceptionType())
- **Causes immediate termination** of method execution
- **Used for validation** and error detection

### `throws` Declaration  
- **Used in method signatures** to declare possible exceptions
- **Followed by exception class names** (ExceptionType1, ExceptionType2)
- **Documents what exceptions** method might throw
- **Required for checked exceptions** (optional for unchecked)

</div>

<div>

## Exception Handling Patterns

<v-clicks>

- **Input Validation**: Use throw for parameter validation
- **State Validation**: Use throw to check object state
- **Resource Management**: Use throws to declare resource exceptions
- **Exception Conversion**: Catch and re-throw with different types
- **Exception Chaining**: Preserve original exception information
- **Graceful Degradation**: Handle errors without crashing
- **Meaningful Messages**: Provide clear error descriptions

</v-clicks>

## Best Practices Recap

### Exception Declaration
- Be specific about exception types
- Document exception conditions clearly
- Use custom exception hierarchies
- Group related exceptions appropriately

### Exception Creation
- Provide meaningful error messages
- Include relevant context information
- Use exception chaining when appropriate
- Validate inputs before processing

### Real-world Impact

#### Without Proper Exception Handling
- Silent failures that are hard to debug
- Generic error messages that don't help users
- Lost context about what went wrong
- Difficult troubleshooting and maintenance

#### With Proper Exception Handling
- Clear error reporting and logging
- Meaningful error messages for users
- Detailed context for debugging
- Robust, maintainable applications

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Throw and Throws Keywords Complete

**Lecture 28 Successfully Completed!**  
You can now create and declare exceptions effectively in Java

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready to build robust exception handling! <carbon:arrow-right class="inline"/>
  </span>
</div>