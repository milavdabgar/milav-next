---
theme: default
background: https://source.unsplash.com/1024x768/?error,debugging
title: Exception Handling Fundamentals
info: |
  ## Java Programming (4343203)
  
  Lecture 26: Exception Handling Fundamentals
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about exception handling fundamentals in Java, exception hierarchy, error vs exception, and basic exception handling strategies.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Exception Handling Fundamentals
## Lecture 26

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

- 🚨 **Understand** the concept of exceptions and error handling in Java
- 🏗️ **Explain** the exception hierarchy and types of exceptions
- ⚡ **Differentiate** between errors, checked exceptions, and unchecked exceptions
- 🎯 **Recognize** common built-in exceptions in Java
- 📝 **Understand** the importance of exception handling in robust programming
- 🛠️ **Identify** scenarios where exceptions occur
- 🔍 **Analyze** exception propagation and stack traces

</v-clicks>

---
layout: default
---

# What are Exceptions?

<div class="grid grid-cols-2 gap-6">

<div>

## Definition
An **exception** is an event that occurs during program execution that disrupts the normal flow of program instructions.

## Key Characteristics

<v-clicks>

- 🚨 **Abnormal Events**: Represent unexpected situations
- 🔄 **Recoverable**: Can often be handled gracefully
- 📍 **Runtime Events**: Occur during program execution
- 🎯 **Specific Information**: Provide details about what went wrong
- 🛠️ **Handleable**: Can be caught and managed

</v-clicks>

## Why Exception Handling?

<v-clicks>

- **Program Stability**: Prevent crashes from unexpected errors
- **User Experience**: Provide meaningful error messages
- **Debugging**: Help locate and fix problems
- **Resource Management**: Ensure proper cleanup
- **Robustness**: Make programs more reliable

</v-clicks>

</div>

<div>

## Real-world Analogy
Think of exceptions like traffic problems:

```java
// Normal traffic flow
public void driveToWork() {
    startCar();        // ✅ Normal
    driveRoute();      // ✅ Normal  
    parkAtOffice();    // ✅ Normal
}

// With potential problems
public void driveToWorkSafely() {
    try {
        startCar();        // Could throw CarWontStartException
        driveRoute();      // Could throw TrafficJamException
        parkAtOffice();    // Could throw NoParkingException
    } catch (CarException e) {
        callMechanic();    // Handle car problems
    } catch (TrafficException e) {
        takeAlternateRoute(); // Handle traffic problems
    }
}
```

## Exception Examples
- **FileNotFoundException**: File doesn't exist
- **ArrayIndexOutOfBoundsException**: Invalid array access
- **NullPointerException**: Accessing null reference
- **SQLException**: Database operation fails
- **NetworkException**: Network connection issues

</div>

</div>

---
layout: default
---

# Exception vs Error vs Normal Flow

<div class="grid grid-cols-2 gap-6">

<div>

## Normal Program Flow
```java
public class NormalFlow {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        int result = a / b;  // Normal division
        System.out.println("Result: " + result); // Output: Result: 2
        
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println("Element: " + numbers[2]); // Output: Element: 3
        
        String text = "Hello World";
        System.out.println("Length: " + text.length()); // Output: Length: 11
    }
}
```

## Exception Scenarios
```java
public class ExceptionScenarios {
    public static void main(String[] args) {
        // Division by zero - ArithmeticException
        int a = 10;
        int b = 0;
        int result = a / b;  // 🚨 Exception!
        
        // Array index out of bounds
        int[] numbers = {1, 2, 3};
        System.out.println(numbers[5]); // 🚨 Exception!
        
        // Null pointer access
        String text = null;
        System.out.println(text.length()); // 🚨 Exception!
        
        // File not found
        FileReader file = new FileReader("nonexistent.txt"); // 🚨 Exception!
    }
}
```

</div>

<div>

## What Happens Without Exception Handling?

### Program Crash Example
```java
public class CrashExample {
    public static void main(String[] args) {
        System.out.println("Program started");
        
        int[] arr = {1, 2, 3};
        System.out.println("Accessing element at index 5...");
        
        // This will crash the program
        System.out.println(arr[5]); // 🚨 CRASH!
        
        // This line will never execute
        System.out.println("Program ended successfully");
    }
}

/* Output:
Program started
Accessing element at index 5...
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 
    Index 5 out of bounds for length 3
    at CrashExample.main(CrashExample.java:8)
*/
```

### Impact of Unhandled Exceptions
- **Program Termination**: Entire program stops abruptly
- **Lost Work**: User data may be lost
- **Poor User Experience**: Cryptic error messages
- **System Instability**: May affect other parts of system
- **Debugging Difficulty**: Hard to trace the root cause

### Benefits of Exception Handling
- **Graceful Recovery**: Continue execution where possible
- **User-Friendly Messages**: Clear error communication
- **Resource Cleanup**: Proper closing of files, connections
- **Logging**: Record errors for debugging
- **Alternative Actions**: Provide fallback options

</div>

</div>

---
layout: default
---

# Exception Hierarchy in Java

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Class Hierarchy
```java
java.lang.Object
    ↓
java.lang.Throwable
    ↓
    ├── java.lang.Error
    │   ├── OutOfMemoryError
    │   ├── StackOverflowError
    │   └── VirtualMachineError
    │
    └── java.lang.Exception
        ├── IOException (Checked)
        │   ├── FileNotFoundException
        │   ├── EOFException
        │   └── SocketException
        │
        ├── SQLException (Checked)
        ├── ClassNotFoundException (Checked)
        │
        └── RuntimeException (Unchecked)
            ├── NullPointerException
            ├── ArrayIndexOutOfBoundsException
            ├── ArithmeticException
            ├── IllegalArgumentException
            └── NumberFormatException
```

## Throwable Class
```java
public class Throwable {
    private String message;
    private Throwable cause;
    
    // Constructor
    public Throwable(String message) {
        this.message = message;
    }
    
    // Key methods
    public String getMessage() { return message; }
    public void printStackTrace() { /* prints stack trace */ }
    public StackTraceElement[] getStackTrace() { /* returns trace */ }
    public String toString() { return getClass() + ": " + message; }
}
```

</div>

<div>

## Understanding the Hierarchy

### 1. **Throwable** - Root Class
- Base class for all exceptions and errors
- Provides common functionality like stack trace
- Has two main subclasses: Error and Exception

### 2. **Error** - System Level Problems
```java
// Examples of Errors (DO NOT catch these)
public class ErrorExamples {
    public static void causeOutOfMemoryError() {
        List<byte[]> list = new ArrayList<>();
        while (true) {
            list.add(new byte[1024 * 1024]); // Allocate 1MB
        }
        // Eventually throws OutOfMemoryError
    }
    
    public static void causeStackOverflowError() {
        causeStackOverflowError(); // Infinite recursion
        // Eventually throws StackOverflowError
    }
}
```

### 3. **Exception** - Application Level Problems
- Represents conditions that applications should handle
- Two categories: Checked and Unchecked

### 4. **Checked Exceptions**
```java
// Must be declared or caught
public void readFile(String filename) throws IOException {
    FileReader file = new FileReader(filename); // May throw IOException
    // Compiler enforces handling
}
```

### 5. **Unchecked Exceptions (RuntimeException)**
```java
// No need to declare or catch (but can be)
public int divide(int a, int b) {
    return a / b; // May throw ArithmeticException
}
```

</div>

</div>

---
layout: default
---

# Types of Exceptions

<div class="grid grid-cols-2 gap-6">

<div>

## 1. Checked Exceptions
**Must be handled** or declared to be thrown.

### Characteristics:
- **Compile-time checking**: Must handle or declare
- **External dependencies**: Often related to I/O, networking
- **Recoverable**: Usually can be handled gracefully
- **Explicit handling**: Forces developer to consider error cases

### Common Checked Exceptions:
```java
// IOException - File and I/O operations
try {
    FileReader file = new FileReader("data.txt");
    BufferedReader reader = new BufferedReader(file);
    String line = reader.readLine();
} catch (IOException e) {
    System.err.println("File operation failed: " + e.getMessage());
}

// SQLException - Database operations
try {
    Connection conn = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/mydb", "user", "pass");
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery("SELECT * FROM users");
} catch (SQLException e) {
    System.err.println("Database error: " + e.getMessage());
}

// ClassNotFoundException - Dynamic class loading
try {
    Class<?> clazz = Class.forName("com.example.MyClass");
    Object instance = clazz.newInstance();
} catch (ClassNotFoundException e) {
    System.err.println("Class not found: " + e.getMessage());
}

// InterruptedException - Thread operations
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    System.err.println("Thread interrupted: " + e.getMessage());
}
```

</div>

<div>

## 2. Unchecked Exceptions (Runtime)
**Optional to handle** - occur during runtime.

### Characteristics:
- **Runtime checking**: Occur during execution
- **Programming errors**: Often indicate bugs
- **Optional handling**: No compile-time requirement
- **Should be prevented**: Better to fix the root cause

### Common Unchecked Exceptions:
```java
// NullPointerException - Most common runtime exception
String text = null;
int length = text.length(); // 🚨 NullPointerException

// ArithmeticException - Mathematical errors
int result = 10 / 0; // 🚨 ArithmeticException

// ArrayIndexOutOfBoundsException - Invalid array access
int[] numbers = {1, 2, 3};
int value = numbers[5]; // 🚨 ArrayIndexOutOfBoundsException

// IllegalArgumentException - Invalid method arguments
public void setAge(int age) {
    if (age < 0 || age > 150) {
        throw new IllegalArgumentException("Invalid age: " + age);
    }
    this.age = age;
}

// NumberFormatException - Invalid string to number conversion
int number = Integer.parseInt("abc"); // 🚨 NumberFormatException

// ClassCastException - Invalid type casting
Object obj = "Hello";
Integer num = (Integer) obj; // 🚨 ClassCastException
```

### Prevention Strategies:
```java
// Prevent NullPointerException
if (text != null) {
    int length = text.length(); // Safe
}

// Prevent ArrayIndexOutOfBoundsException
if (index >= 0 && index < array.length) {
    int value = array[index]; // Safe
}

// Prevent NumberFormatException
try {
    int number = Integer.parseInt(input);
} catch (NumberFormatException e) {
    // Handle invalid input
    number = 0; // Default value
}
```

</div>

</div>

---
layout: default
---

# Common Built-in Exceptions

<div class="grid grid-cols-2 gap-6">

<div>

## Runtime Exceptions (Unchecked)

### 1. NullPointerException
```java
public class NullPointerExamples {
    public static void demonstrateNPE() {
        String str = null;
        
        // Various ways NPE can occur
        int length = str.length();           // 🚨 NPE
        String upper = str.toUpperCase();    // 🚨 NPE
        boolean empty = str.isEmpty();       // 🚨 NPE
        char first = str.charAt(0);         // 🚨 NPE
        
        // Object method calls on null
        Object obj = null;
        String result = obj.toString();      // 🚨 NPE
        
        // Array of objects
        String[] arr = new String[5];
        int len = arr[0].length();          // 🚨 NPE (array elements are null)
        
        // Method chaining
        String text = getText().trim().toUpperCase(); // 🚨 NPE if getText() returns null
    }
    
    // Prevention techniques
    public static void preventNPE() {
        String str = getValue();
        
        // Null check
        if (str != null) {
            int length = str.length(); // Safe
        }
        
        // Using Objects utility
        int length = Objects.requireNonNull(str).length();
        
        // Optional (Java 8+)
        Optional<String> optional = Optional.ofNullable(str);
        optional.ifPresent(s -> System.out.println(s.length()));
    }
}
```

### 2. ArrayIndexOutOfBoundsException
```java
public class ArrayIndexExamples {
    public static void demonstrateAIOBE() {
        int[] numbers = {10, 20, 30, 40, 50};
        
        // Valid indices: 0, 1, 2, 3, 4
        System.out.println(numbers[0]);  // ✅ Valid: 10
        System.out.println(numbers[4]);  // ✅ Valid: 50
        
        // Invalid indices
        System.out.println(numbers[-1]); // 🚨 AIOBE: negative index
        System.out.println(numbers[5]);  // 🚨 AIOBE: index >= length
        System.out.println(numbers[10]); // 🚨 AIOBE: way out of bounds
        
        // Dynamic access
        Scanner input = new Scanner(System.in);
        int index = input.nextInt();
        System.out.println(numbers[index]); // 🚨 Potential AIOBE
    }
    
    // Prevention
    public static void preventAIOBE() {
        int[] numbers = {10, 20, 30, 40, 50};
        int index = getUserInput();
        
        // Bounds checking
        if (index >= 0 && index < numbers.length) {
            System.out.println(numbers[index]); // Safe
        } else {
            System.out.println("Invalid index: " + index);
        }
        
        // Using enhanced for loop (no index needed)
        for (int number : numbers) {
            System.out.println(number); // Safe
        }
    }
}
```

</div>

<div>

### 3. ArithmeticException
```java
public class ArithmeticExamples {
    public static void demonstrateAE() {
        // Division by zero
        int a = 10;
        int b = 0;
        int result = a / b;     // 🚨 ArithmeticException
        int mod = a % b;        // 🚨 ArithmeticException
        
        // Note: Floating point division doesn't throw exception
        double da = 10.0;
        double db = 0.0;
        double dresult = da / db; // Result: Infinity (no exception)
    }
    
    // Prevention
    public static void preventAE() {
        int a = 10;
        int b = getUserInput();
        
        if (b != 0) {
            int result = a / b; // Safe
            System.out.println("Result: " + result);
        } else {
            System.out.println("Cannot divide by zero");
        }
        
        // Using try-catch
        try {
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Division by zero attempted");
        }
    }
}
```

### 4. IllegalArgumentException
```java
public class IllegalArgumentExamples {
    private int age;
    private String email;
    
    // Method that validates arguments
    public void setAge(int age) {
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException(
                "Age must be between 0 and 150, got: " + age);
        }
        this.age = age;
    }
    
    public void setEmail(String email) {
        if (email == null || email.trim().isEmpty()) {
            throw new IllegalArgumentException(
                "Email cannot be null or empty");
        }
        if (!email.contains("@")) {
            throw new IllegalArgumentException(
                "Invalid email format: " + email);
        }
        this.email = email;
    }
    
    // String and collection methods that throw IAE
    public static void stringExamples() {
        String text = "Hello World";
        
        // substring with invalid indices
        String sub1 = text.substring(-1);     // 🚨 IllegalArgumentException
        String sub2 = text.substring(5, 2);   // 🚨 IllegalArgumentException
        
        // Thread.sleep with negative argument
        Thread.sleep(-1000);                  // 🚨 IllegalArgumentException
    }
}
```

</div>

</div>

---
layout: default
---

# Exception Propagation and Stack Traces

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Propagation
When an exception is thrown, it **propagates up** the call stack until it's caught or reaches the main method.

### Call Stack Example
```java
public class PropagationExample {
    public static void main(String[] args) {
        System.out.println("Main method starts");
        try {
            methodA();
        } catch (ArithmeticException e) {
            System.out.println("Caught in main: " + e.getMessage());
        }
        System.out.println("Main method ends");
    }
    
    public static void methodA() {
        System.out.println("Method A starts");
        methodB();
        System.out.println("Method A ends"); // Won't execute if exception
    }
    
    public static void methodB() {
        System.out.println("Method B starts");
        methodC();
        System.out.println("Method B ends"); // Won't execute if exception
    }
    
    public static void methodC() {
        System.out.println("Method C starts");
        int result = 10 / 0; // 🚨 ArithmeticException thrown here
        System.out.println("Method C ends"); // Won't execute
    }
}

/* Output:
Main method starts
Method A starts
Method B starts
Method C starts
Caught in main: / by zero
Main method ends
*/
```

### Propagation Flow
1. **Exception occurs** in methodC()
2. **methodC() terminates** immediately
3. **Exception propagates** to methodB()
4. **methodB() terminates** without completing
5. **Exception propagates** to methodA()  
6. **methodA() terminates** without completing
7. **Exception propagates** to main()
8. **main() catches** the exception and handles it

</div>

<div>

## Understanding Stack Traces
A **stack trace** shows the sequence of method calls that led to an exception.

### Stack Trace Example
```java
public class StackTraceExample {
    public static void main(String[] args) {
        calculateTotal();
    }
    
    public static void calculateTotal() {
        processData();
    }
    
    public static void processData() {
        String[] data = {"10", "20", "abc", "30"};
        for (int i = 0; i < data.length; i++) {
            int value = parseInt(data[i]);
            System.out.println("Parsed: " + value);
        }
    }
    
    public static int parseInt(String str) {
        return Integer.parseInt(str); // Exception on "abc"
    }
}

/* Stack Trace Output:
Exception in thread "main" java.lang.NumberFormatException: For input string: "abc"
    at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
    at java.base/java.lang.Integer.parseInt(Integer.java:660)
    at java.base/java.lang.Integer.parseInt(Integer.java:778)
    at StackTraceExample.parseInt(StackTraceExample.java:15)
    at StackTraceExample.processData(StackTraceExample.java:11)
    at StackTraceExample.calculateTotal(StackTraceExample.java:6)
    at StackTraceExample.main(StackTraceExample.java:3)
*/
```

### Reading Stack Traces
```java
// Exception type and message
NumberFormatException: For input string: "abc"

// Stack trace (bottom to top shows call sequence)
at StackTraceExample.parseInt(StackTraceExample.java:15)      ← Exception origin
at StackTraceExample.processData(StackTraceExample.java:11)   ← Called parseInt
at StackTraceExample.calculateTotal(StackTraceExample.java:6) ← Called processData
at StackTraceExample.main(StackTraceExample.java:3)          ← Called calculateTotal
```

### Analyzing Stack Traces
- **Exception Type**: What kind of exception occurred
- **Error Message**: Specific details about the problem
- **Method Sequence**: Chain of method calls leading to exception
- **Line Numbers**: Exact location where exception occurred
- **File Names**: Source files involved

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Exception Identification

<div class="grid grid-cols-2 gap-6">

<div>

## Exercise: Identify Exception Types
Analyze the following code snippets and predict what exceptions will occur:

```java
// Snippet 1
public class ExceptionQuiz {
    public static void snippet1() {
        String[] names = {"Alice", "Bob", "Charlie"};
        for (int i = 0; i <= names.length; i++) {
            System.out.println("Name: " + names[i]);
        }
    }
    
    // Snippet 2
    public static void snippet2() {
        String text = null;
        if (text.equals("Hello")) {
            System.out.println("Found Hello");
        }
    }
    
    // Snippet 3
    public static void snippet3() {
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
        for (int i = 1; i <= 5; i++) {
            sum += numbers[i];
        }
        System.out.println("Sum: " + sum);
    }
    
    // Snippet 4
    public static void snippet4() {
        String input = "12.34abc";
        int value = Integer.parseInt(input);
        System.out.println("Value: " + value);
    }
    
    // Snippet 5
    public static void snippet5() {
        List<String> list = new ArrayList<>();
        list.add("Item1");
        list.add("Item2");
        String item = list.get(5);
        System.out.println("Item: " + item);
    }
}
```

**Questions:**
1. What exception will snippet1() throw and why?
2. What exception will snippet2() throw and why?
3. What exception will snippet3() throw and why?
4. What exception will snippet4() throw and why?
5. What exception will snippet5() throw and why?

</div>

<div>

## Solutions and Explanations

### Snippet 1: ArrayIndexOutOfBoundsException
```java
// Problem: Loop condition uses <= instead of <
for (int i = 0; i <= names.length; i++) // i goes 0,1,2,3
    System.out.println("Name: " + names[i]); // names[3] doesn't exist
```
**Fix:**
```java
for (int i = 0; i < names.length; i++) // Correct condition
```

### Snippet 2: NullPointerException  
```java
// Problem: Calling method on null reference
String text = null;
if (text.equals("Hello")) // text is null, can't call equals()
```
**Fix:**
```java
if ("Hello".equals(text)) // Use string literal first
// or
if (text != null && text.equals("Hello")) // Null check
```

### Snippet 3: ArrayIndexOutOfBoundsException
```java
// Problem: Loop starts from 1, but array is 0-indexed
for (int i = 1; i <= 5; i++) // i goes 1,2,3,4,5
    sum += numbers[i]; // numbers[5] doesn't exist (only 0-4)
```
**Fix:**
```java
for (int i = 0; i < numbers.length; i++) // Start from 0
```

### Snippet 4: NumberFormatException
```java
// Problem: "12.34abc" is not a valid integer
int value = Integer.parseInt("12.34abc"); // Can't parse "abc" part
```
**Fix:**
```java
// Use Double.parseDouble() or clean the string first
String cleaned = input.replaceAll("[^0-9]", ""); // Remove non-digits
```

### Snippet 5: IndexOutOfBoundsException
```java
// Problem: List has only 2 elements (indices 0,1), but accessing index 5
String item = list.get(5); // Index 5 doesn't exist
```
**Fix:**
```java
if (index >= 0 && index < list.size()) {
    String item = list.get(index);
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Exception Analysis

<div class="grid grid-cols-2 gap-6">

<div>

## Exercise: Banking System
Create a simple banking system and identify potential exceptions:

```java
public class BankAccount {
    private String accountNumber;
    private double balance;
    private String ownerName;
    
    public BankAccount(String accountNumber, String ownerName) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = 0.0;
    }
    
    // Deposit money
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: $" + amount);
        System.out.println("New balance: $" + balance);
    }
    
    // Withdraw money
    public void withdraw(double amount) {
        balance -= amount;
        System.out.println("Withdrew: $" + amount);
        System.out.println("New balance: $" + balance);
    }
    
    // Transfer money to another account
    public void transfer(BankAccount toAccount, double amount) {
        this.withdraw(amount);
        toAccount.deposit(amount);
        System.out.println("Transferred $" + amount + 
                         " to " + toAccount.getOwnerName());
    }
    
    // Calculate interest (annual percentage rate)
    public double calculateInterest(double rate, int years) {
        double interest = balance * (rate / 100) * years;
        return interest;
    }
    
    public String getOwnerName() { return ownerName; }
    public double getBalance() { return balance; }
}
```

**Tasks:**
1. Identify at least 5 potential exception scenarios
2. What inputs could cause problems?
3. What validation should be added?

</div>

<div>

## Solution: Potential Exception Scenarios

### 1. Constructor Issues
```java
// NullPointerException scenarios
BankAccount account1 = new BankAccount(null, "John"); // Null account number
BankAccount account2 = new BankAccount("123", null);  // Null owner name

// Later usage issues
String owner = account2.getOwnerName().toUpperCase(); // NPE!
```

### 2. Deposit Method Issues  
```java
// IllegalArgumentException scenarios
account.deposit(-100);     // Negative deposit
account.deposit(0);        // Zero deposit
account.deposit(Double.NaN); // Invalid number
account.deposit(Double.POSITIVE_INFINITY); // Infinite amount
```

### 3. Withdraw Method Issues
```java
// ArithmeticException or logic error scenarios
account.withdraw(1000);    // Withdraw more than balance (overdraft)
account.withdraw(-50);     // Negative withdrawal
```

### 4. Transfer Method Issues
```java
// NullPointerException
account1.transfer(null, 100); // Null destination account

// Cascading exceptions
account1.transfer(account2, -100); // Negative transfer
account1.transfer(account2, 5000); // Insufficient funds
```

### 5. Interest Calculation Issues
```java
// ArithmeticException or invalid results
double interest = account.calculateInterest(-5, 10);    // Negative rate
double interest = account.calculateInterest(100, -2);   // Negative years
double interest = account.calculateInterest(Double.NaN, 5); // Invalid rate
```

### Improved Version with Validation
```java
public void deposit(double amount) {
    if (amount <= 0) {
        throw new IllegalArgumentException("Deposit amount must be positive");
    }
    if (Double.isNaN(amount) || Double.isInfinite(amount)) {
        throw new IllegalArgumentException("Invalid amount: " + amount);
    }
    balance += amount;
}

public void transfer(BankAccount toAccount, double amount) {
    if (toAccount == null) {
        throw new IllegalArgumentException("Destination account cannot be null");
    }
    if (amount <= 0) {
        throw new IllegalArgumentException("Transfer amount must be positive");  
    }
    if (balance < amount) {
        throw new IllegalArgumentException("Insufficient funds");
    }
    this.withdraw(amount);
    toAccount.deposit(amount);
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

## 1. File Processing System
```java
public class FileProcessor {
    public void processFile(String filename) {
        // Potential Exceptions:
        // - FileNotFoundException: File doesn't exist
        // - SecurityException: No permission to read
        // - IOException: Disk error, network failure
        
        FileReader reader = new FileReader(filename);
        BufferedReader buffer = new BufferedReader(reader);
        
        String line;
        while ((line = buffer.readLine()) != null) {
            processLine(line);
        }
        
        buffer.close();
        reader.close();
    }
    
    private void processLine(String line) {
        // Potential Exceptions:
        // - NullPointerException: Line is null
        // - NumberFormatException: Invalid number format
        // - ArrayIndexOutOfBoundsException: Missing data fields
        
        String[] parts = line.split(",");
        int id = Integer.parseInt(parts[0]);
        String name = parts[1];
        double salary = Double.parseDouble(parts[2]);
        
        System.out.println("Employee: " + name + ", Salary: $" + salary);
    }
}
```

## 2. Database Connection
```java
public class DatabaseManager {
    public void connectAndQuery() {
        // Potential Exceptions:
        // - ClassNotFoundException: JDBC driver not found
        // - SQLException: Connection failed, invalid query
        // - SecurityException: Database access denied
        
        Class.forName("com.mysql.cj.jdbc.Driver");
        
        Connection conn = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/mydb", 
            "username", "password");
        
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM users");
        
        while (rs.next()) {
            System.out.println("User: " + rs.getString("name"));
        }
    }
}
```

</div>

<div>

## 3. Web Service Communication
```java
public class WebServiceClient {
    public String fetchData(String url) {
        // Potential Exceptions:
        // - MalformedURLException: Invalid URL format
        // - IOException: Network timeout, connection refused
        // - ProtocolException: HTTP protocol error
        // - SecurityException: Access denied
        
        URL serviceUrl = new URL(url);
        HttpURLConnection connection = 
            (HttpURLConnection) serviceUrl.openConnection();
        
        connection.setRequestMethod("GET");
        connection.setConnectTimeout(5000); // 5 second timeout
        
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(connection.getInputStream()));
        
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }
        
        reader.close();
        connection.disconnect();
        
        return response.toString();
    }
}
```

## 4. User Input Validation
```java
public class UserInputProcessor {
    private Scanner scanner = new Scanner(System.in);
    
    public int getValidAge() {
        // Potential Exceptions:
        // - NumberFormatException: Non-numeric input
        // - InputMismatchException: Wrong data type
        // - NoSuchElementException: No more input available
        
        System.out.print("Enter your age: ");
        String input = scanner.nextLine();
        
        int age = Integer.parseInt(input); // Can throw NFE
        
        // Business logic validation
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("Age must be between 0 and 150");
        }
        
        return age;
    }
    
    public String getValidEmail() {
        System.out.print("Enter email: ");
        String email = scanner.nextLine();
        
        // Potential NullPointerException if email is null
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Invalid email format");
        }
        
        return email;
    }
}
```

</div>

</div>

---
layout: default
---

# Exception Handling Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Do's and Don'ts

### ✅ **DO's**

#### 1. Handle Specific Exceptions
```java
// GOOD: Handle specific exceptions differently
try {
    processFile(filename);
} catch (FileNotFoundException e) {
    System.err.println("File not found: " + filename);
    // Maybe create default file or use alternative
} catch (IOException e) {
    System.err.println("I/O error: " + e.getMessage());
    // Maybe retry or log error
} catch (SecurityException e) {
    System.err.println("Access denied: " + filename);
    // Request permissions or use alternative
}
```

#### 2. Provide Meaningful Error Messages
```java
// GOOD: Descriptive error messages
public void setAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException(
            "Age cannot be negative. Received: " + age);
    }
    if (age > 150) {
        throw new IllegalArgumentException(
            "Age cannot exceed 150. Received: " + age);
    }
    this.age = age;
}
```

#### 3. Log Exceptions for Debugging
```java
// GOOD: Log exceptions with context
try {
    processUserData(userData);
} catch (DataValidationException e) {
    Logger.getLogger(getClass()).error(
        "Data validation failed for user: " + userData.getId(), e);
    throw e; // Re-throw if needed
}
```

#### 4. Clean Up Resources
```java
// GOOD: Always clean up resources
FileInputStream fis = null;
try {
    fis = new FileInputStream("data.txt");
    // Process file
} catch (IOException e) {
    System.err.println("File processing error: " + e.getMessage());
} finally {
    if (fis != null) {
        try {
            fis.close();
        } catch (IOException e) {
            System.err.println("Error closing file: " + e.getMessage());
        }
    }
}
```

</div>

<div>

### ❌ **DON'Ts**

#### 1. Don't Catch Generic Exception
```java
// BAD: Too generic, hides different error types
try {
    processFile(filename);
} catch (Exception e) {
    System.out.println("Something went wrong");
    // Can't tell what actually happened
}
```

#### 2. Don't Ignore Exceptions
```java
// BAD: Silent failure
try {
    int result = Integer.parseInt(userInput);
} catch (NumberFormatException e) {
    // Ignoring exception - very bad!
}

// BAD: Empty catch block
try {
    riskyOperation();
} catch (Exception e) {
    // TODO: Handle exception - never gets done!
}
```

#### 3. Don't Use Exceptions for Control Flow
```java
// BAD: Using exceptions for normal logic
public boolean isValidNumber(String str) {
    try {
        Integer.parseInt(str);
        return true;
    } catch (NumberFormatException e) {
        return false; // Using exception for control flow
    }
}

// GOOD: Proper validation
public boolean isValidNumber(String str) {
    if (str == null || str.isEmpty()) return false;
    
    for (char c : str.toCharArray()) {
        if (!Character.isDigit(c)) return false;
    }
    return true;
}
```

#### 4. Don't Catch and Re-throw Without Purpose
```java
// BAD: Unnecessary catch and re-throw
public void processData() throws IOException {
    try {
        readDataFile();
    } catch (IOException e) {
        throw e; // Why catch if just re-throwing?
    }
}

// GOOD: Add value when catching and re-throwing
public void processData() throws DataProcessingException {
    try {
        readDataFile();
    } catch (IOException e) {
        throw new DataProcessingException(
            "Failed to process data file", e);
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

- 🚨 **Exception Fundamentals**: Abnormal events that disrupt program flow
- 🏗️ **Exception Hierarchy**: Throwable → Error/Exception → Checked/Unchecked
- ⚡ **Exception Types**: Checked (compile-time) vs Unchecked (runtime)
- 🎯 **Common Exceptions**: NPE, AIOBE, ArithmeticException, etc.
- 📝 **Exception Propagation**: How exceptions travel up the call stack
- 🛠️ **Stack Traces**: Reading and understanding error information
- 🔍 **Best Practices**: Specific handling, meaningful messages, proper cleanup

</v-clicks>

## Exception Handling Benefits

### For Developers
- **Debugging**: Easier to identify and fix problems
- **Code Quality**: More robust and reliable programs  
- **Maintenance**: Cleaner error handling logic
- **Testing**: Better error scenario coverage

### For Users
- **Better Experience**: Graceful error recovery
- **Clear Messages**: Understanding what went wrong
- **Data Safety**: Prevention of data loss
- **System Stability**: Continued operation after errors

</div>

<div>

## Key Principles Recap

<v-clicks>

- **Fail Fast**: Detect problems early
- **Fail Gracefully**: Handle errors without crashing
- **Specific Handling**: Catch specific exception types
- **Meaningful Messages**: Provide clear error information
- **Resource Cleanup**: Always clean up properly
- **Don't Ignore**: Never swallow exceptions silently
- **Log Everything**: Record errors for debugging
- **Prevention First**: Validate input to prevent exceptions

</v-clicks>

## Real-world Impact

### Without Exception Handling
- Programs crash unexpectedly
- Data gets corrupted or lost
- Users see cryptic error messages
- Systems become unreliable
- Debugging becomes very difficult

### With Proper Exception Handling
- Graceful error recovery
- Data integrity maintained
- User-friendly error messages
- System remains stable
- Easy debugging and maintenance

## Next Steps
In the following lectures, we'll learn:
- **Try-Catch-Finally**: Actual exception handling syntax
- **Throw/Throws**: Creating and declaring exceptions
- **Custom Exceptions**: Building your own exception types
- **Best Practices**: Advanced exception handling patterns

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Exception Handling Fundamentals Complete

**Lecture 26 Successfully Completed!**  
Understanding exceptions is crucial for writing robust Java programs

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready to handle exceptions like a pro! <carbon:arrow-right class="inline"/>
  </span>
</div>