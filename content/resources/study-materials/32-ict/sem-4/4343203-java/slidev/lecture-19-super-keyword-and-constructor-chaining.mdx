---
theme: default
background: https://source.unsplash.com/1024x768/?chain,connection
title: super Keyword and Constructor Chaining
info: |
  ## Java Programming (4343203)
  
  Lecture 19: super Keyword and Constructor Chaining
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about the super keyword, constructor chaining, accessing parent methods, and proper inheritance initialization.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# super Keyword and Constructor Chaining
## Lecture 19

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

- 🔗 **Understand** the super keyword and its applications
- 🏗️ **Implement** constructor chaining with super()
- 🎯 **Access** parent class methods using super
- ⚡ **Design** proper initialization hierarchies
- 🛠️ **Apply** super in method overriding scenarios
- 📝 **Practice** with complex inheritance chains

</v-clicks>

<br>

<div v-click="7" class="text-center text-2xl text-blue-600 font-bold">
Let's master parent-child communication! 🔗🏗️
</div>

---
layout: center
---

# What is the super Keyword?

<div class="flex justify-center">

```mermaid
graph TD
    A[super Keyword] --> B[Access Parent Constructor]
    A --> C[Access Parent Methods]
    A --> D[Access Parent Variables]
    
    B --> E[super()]
    B --> F[super(parameters)]
    
    C --> G[super.method()]
    C --> H[Method Extension]
    
    D --> I[super.variable]
    D --> J[Variable Access]
    
    style A fill:#e3f2fd
    style B fill:#e8f5e8
    style C fill:#fff3e0
    style D fill:#f3e5f5
```

</div>

<div class="mt-8 grid grid-cols-2 gap-6">

<div class="bg-blue-50 p-4 rounded-lg">
<h3 class="font-bold text-blue-700">🎯 super Keyword Uses</h3>
<ul class="text-sm space-y-1">
<li>• Call parent class constructor</li>
<li>• Access parent class methods</li>
<li>• Access parent class variables</li>
<li>• Extend parent functionality</li>
</ul>
</div>

<div class="bg-green-50 p-4 rounded-lg">
<h3 class="font-bold text-green-700">🔧 Key Benefits</h3>
<ul class="text-sm space-y-1">
<li>• Proper initialization chain</li>
<li>• Code reuse and extension</li>
<li>• Maintains inheritance contract</li>
<li>• Enables flexible design</li>
</ul>
</div>

</div>

---
layout: default
---

# super() Constructor Chaining

<div class="grid grid-cols-2 gap-8">

<div>

## 🏗️ Basic Constructor Chaining

```java
// Parent class
class Vehicle {
    protected String brand;
    protected String model;
    protected int year;
    protected double price;
    
    // Default constructor
    public Vehicle() {
        this.brand = "Unknown";
        this.model = "Unknown";  
        this.year = 2024;
        this.price = 0.0;
        System.out.println("Vehicle default constructor called");
    }
    
    // Parameterized constructor
    public Vehicle(String brand, String model, int year, double price) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.price = price;
        
        // Validation
        if (year < 1900 || year > 2025) {
            throw new IllegalArgumentException("Invalid year: " + year);
        }
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative");
        }
        
        System.out.println("Vehicle parameterized constructor called");
        System.out.println("Created vehicle: " + brand + " " + model);
    }
    
    public void displayInfo() {
        System.out.println("Vehicle: " + brand + " " + model + 
                          " (" + year + ") - $" + price);
    }
    
    public void start() {
        System.out.println(brand + " " + model + " is starting");
    }
}
```

</div>

<div>

## 🚗 Child Class with super()

```java
// Child class
class Car extends Vehicle {
    private int numberOfDoors;
    private String fuelType;
    private boolean isAutomatic;
    
    // Default constructor - calls parent default constructor
    public Car() {
        super();  // Must be first statement
        this.numberOfDoors = 4;
        this.fuelType = "Gasoline";
        this.isAutomatic = true;
        System.out.println("Car default constructor called");
    }
    
    // Constructor with basic parameters
    public Car(String brand, String model, int year) {
        super(brand, model, year, 25000.0);  // Call parent constructor
        this.numberOfDoors = 4;
        this.fuelType = "Gasoline";
        this.isAutomatic = true;
        System.out.println("Car basic constructor called");
    }
    
    // Full constructor
    public Car(String brand, String model, int year, double price,
              int doors, String fuel, boolean automatic) {
        super(brand, model, year, price);  // Call parent constructor first
        this.numberOfDoors = doors;
        this.fuelType = fuel;
        this.isAutomatic = automatic;
        
        // Additional validation for car-specific properties
        if (doors < 2 || doors > 6) {
            throw new IllegalArgumentException("Invalid number of doors");
        }
        
        System.out.println("Car full constructor called");
    }
    
    // Override parent method and extend it
    @Override
    public void displayInfo() {
        super.displayInfo();  // Call parent method
        System.out.println("Doors: " + numberOfDoors);
        System.out.println("Fuel Type: " + fuelType);
        System.out.println("Automatic: " + isAutomatic);
    }
    
    @Override
    public void start() {
        System.out.println("Inserting key into " + brand + " " + model);
        super.start();  // Call parent implementation
        System.out.println("Car engine started!");
    }
}
```

</div>

</div>

---
layout: default
---

# Constructor Chaining Demonstration

<div class="grid grid-cols-2 gap-8">

<div>

## 🎬 Constructor Chain in Action

```java
public class ConstructorChainingDemo {
    public static void main(String[] args) {
        System.out.println("=== Creating Car with Default Constructor ===");
        Car car1 = new Car();
        car1.displayInfo();
        
        System.out.println("\n=== Creating Car with Basic Constructor ===");
        Car car2 = new Car("Toyota", "Camry", 2024);
        car2.displayInfo();
        
        System.out.println("\n=== Creating Car with Full Constructor ===");
        Car car3 = new Car("Honda", "Civic", 2024, 32000.0, 
                          4, "Hybrid", true);
        car3.displayInfo();
        
        System.out.println("\n=== Testing Method Extension ===");
        car3.start();
        
        System.out.println("\n=== Error Handling ===");
        try {
            Car invalidCar = new Car("Tesla", "Model 3", 1800, 50000.0,
                                   8, "Electric", true);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

</div>

<div>

## 📄 Expected Output

```text
=== Creating Car with Default Constructor ===
Vehicle default constructor called
Car default constructor called
Vehicle: Unknown Unknown (2024) - $0.0
Doors: 4
Fuel Type: Gasoline
Automatic: true

=== Creating Car with Basic Constructor ===
Vehicle parameterized constructor called
Created vehicle: Toyota Camry
Car basic constructor called
Vehicle: Toyota Camry (2024) - $25000.0
Doors: 4
Fuel Type: Gasoline
Automatic: true

=== Creating Car with Full Constructor ===
Vehicle parameterized constructor called
Created vehicle: Honda Civic
Car full constructor called
Vehicle: Honda Civic (2024) - $32000.0
Doors: 4
Fuel Type: Hybrid
Automatic: true

=== Testing Method Extension ===
Inserting key into Honda Civic
Honda Civic is starting
Car engine started!

=== Error Handling ===
Error: Invalid year: 1800
```

**Key Observations:**
- Parent constructor always called before child constructor
- super() must be the first statement in constructor
- Validation happens at each level
- Method extension preserves parent behavior

</div>

</div>

---
layout: default
---

# Multi-Level Constructor Chaining

<div class="grid grid-cols-2 gap-8">

<div>

## 🏗️ Three-Level Inheritance Chain

```java
// Level 1: Base class
class Animal {
    protected String name;
    protected String species;
    protected int age;
    
    public Animal(String name, String species, int age) {
        this.name = name;
        this.species = species;
        this.age = age;
        
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        
        System.out.println("Animal constructor: " + name + " (" + species + ")");
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Species: " + species);
        System.out.println("Age: " + age + " years");
    }
    
    public void makeSound() {
        System.out.println(name + " makes a generic animal sound");
    }
}

// Level 2: Intermediate class
class Mammal extends Animal {
    protected boolean hasFur;
    protected double bodyTemperature;
    
    public Mammal(String name, String species, int age, 
                 boolean hasFur, double bodyTemp) {
        super(name, species, age);  // Chain to Animal constructor
        this.hasFur = hasFur;
        this.bodyTemperature = bodyTemp;
        
        if (bodyTemp < 30.0 || bodyTemp > 45.0) {
            throw new IllegalArgumentException("Invalid body temperature for mammal");
        }
        
        System.out.println("Mammal constructor: " + name);
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();  // Call parent method
        System.out.println("Has Fur: " + hasFur);
        System.out.println("Body Temperature: " + bodyTemperature + "°C");
    }
    
    public void regulateTemperature() {
        System.out.println(name + " maintains body temperature at " + 
                          bodyTemperature + "°C");
    }
}
```

</div>

<div>

## 🐕 Specific Implementation

```java
// Level 3: Specific class
class Dog extends Mammal {
    private String breed;
    private String size;
    private boolean isTrained;
    
    // Constructor with essential parameters
    public Dog(String name, String breed, String size) {
        super(name, "Canis lupus", 2, true, 38.5);  // Chain to Mammal
        this.breed = breed;
        this.size = size;
        this.isTrained = false;
        System.out.println("Dog constructor: " + name + " (" + breed + ")");
    }
    
    // Constructor with all parameters
    public Dog(String name, String breed, String size, int age, boolean trained) {
        super(name, "Canis lupus", age, true, 38.5);  // Chain to Mammal
        this.breed = breed;
        this.size = size;
        this.isTrained = trained;
        System.out.println("Dog full constructor: " + name);
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();  // Chain through all parent methods
        System.out.println("Breed: " + breed);
        System.out.println("Size: " + size);
        System.out.println("Trained: " + isTrained);
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + " barks: Woof! Woof!");
    }
    
    // Dog-specific method that extends parent behavior
    public void performTrick() {
        if (isTrained) {
            super.makeSound();  // Call parent's makeSound first
            System.out.println(name + " sits and gives paw!");
        } else {
            System.out.println(name + " needs training first");
        }
    }
}

// Usage demonstration
public class MultiLevelChainDemo {
    public static void main(String[] args) {
        System.out.println("=== Creating Dog with Basic Constructor ===");
        Dog dog1 = new Dog("Buddy", "Golden Retriever", "Large");
        dog1.displayInfo();
        dog1.makeSound();
        dog1.regulateTemperature();  // From Mammal
        
        System.out.println("\n=== Creating Trained Dog ===");
        Dog dog2 = new Dog("Rex", "German Shepherd", "Large", 5, true);
        dog2.displayInfo();
        dog2.performTrick();  // Uses super.makeSound()
    }
}
```

</div>

</div>

---
layout: default
---

# super vs this

<div class="grid grid-cols-2 gap-8">

<div>

## 🔗 super Keyword Usage

```java
class Parent {
    protected String name;
    protected int value;
    
    public Parent(String name, int value) {
        this.name = name;
        this.value = value;
    }
    
    public void display() {
        System.out.println("Parent - Name: " + name + ", Value: " + value);
    }
    
    public void process() {
        System.out.println("Parent processing");
    }
}

class Child extends Parent {
    private String name;  // Hides parent's name
    private double extraValue;
    
    public Child(String parentName, int value, String childName, double extra) {
        super(parentName, value);  // Call parent constructor
        this.name = childName;     // Child's name field
        this.extraValue = extra;
    }
    
    @Override
    public void display() {
        System.out.println("=== Child Display Method ===");
        
        // Access parent's name field
        System.out.println("Parent name: " + super.name);
        
        // Access child's name field  
        System.out.println("Child name: " + this.name);
        
        // Call parent's display method
        System.out.print("Parent display: ");
        super.display();
        
        System.out.println("Extra value: " + extraValue);
    }
    
    public void processAll() {
        // Call parent's process method first
        super.process();
        
        // Then child's specific processing
        this.processChild();
    }
    
    private void processChild() {
        System.out.println("Child processing with extra value: " + extraValue);
    }
}
```

</div>

<div>

## 🎯 Comparison: super vs this

| Aspect | super | this |
|--------|-------|------|
| **Purpose** | Access parent class members | Access current class members |
| **Constructor** | super() calls parent constructor | this() calls another constructor in same class |
| **Method Access** | super.method() calls parent method | this.method() calls current class method |
| **Variable Access** | super.var accesses parent variable | this.var accesses current class variable |
| **Usage Context** | Inheritance relationships | Within same class |

## 📝 Practical Example

```java
public class SuperVsThisDemo {
    public static void main(String[] args) {
        Child child = new Child("ParentName", 100, "ChildName", 99.5);
        
        System.out.println("=== Demonstrating super vs this ===");
        child.display();
        
        System.out.println("\n=== Method Chaining ===");
        child.processAll();
        
        System.out.println("\n=== Accessing Hidden Variables ===");
        // child.name would access child's name field
        // super.name within child accesses parent's name field
        
        demonstrateVariableAccess(child);
    }
    
    private static void demonstrateVariableAccess(Child child) {
        System.out.println("From outside class:");
        // Can only access public/protected members
        System.out.println("Parent value: " + child.value);  // Inherited
        // System.out.println("Parent name: " + child.super.name);  // Not allowed
    }
}
```

<div class="mt-4 p-4 bg-blue-50 rounded-lg">
<strong>💡 Key Difference:</strong> super refers to parent class context, this refers to current object context.
</div>

</div>

</div>

---
layout: default
---

# Method Extension with super

<div class="grid grid-cols-2 gap-8">

<div>

## 🎨 Extending Parent Functionality

```java
// Base logging class
class Logger {
    protected String logLevel;
    protected String loggerName;
    
    public Logger(String name, String level) {
        this.loggerName = name;
        this.logLevel = level;
    }
    
    public void log(String message) {
        String timestamp = java.time.LocalDateTime.now().toString();
        System.out.println("[" + timestamp + "] " + logLevel + " - " + 
                          loggerName + ": " + message);
    }
    
    public void logError(String error) {
        log("ERROR: " + error);
    }
    
    protected String formatMessage(String message) {
        return message.toUpperCase();
    }
}

// Enhanced logger with file output
class FileLogger extends Logger {
    private String filename;
    private boolean appendToFile;
    
    public FileLogger(String name, String level, String filename) {
        super(name, level);  // Initialize parent
        this.filename = filename;
        this.appendToFile = true;
    }
    
    @Override
    public void log(String message) {
        // Extend parent functionality
        super.log(message);  // Call parent's log method
        
        // Add file logging
        writeToFile(message);
    }
    
    @Override
    public void logError(String error) {
        // Pre-processing
        System.out.println(">>> CRITICAL ERROR DETECTED <<<");
        
        // Call parent implementation
        super.logError(error);
        
        // Post-processing
        writeToFile("CRITICAL: " + error);
        sendEmailAlert(error);
    }
    
    private void writeToFile(String message) {
        System.out.println("Writing to file '" + filename + "': " + message);
        // Actual file writing logic would go here
    }
    
    private void sendEmailAlert(String error) {
        System.out.println("Sending email alert for: " + error);
        // Email sending logic would go here
    }
}
```

</div>

<div>

## 📊 Database Logger Extension

```java
// Further extension with database logging
class DatabaseLogger extends FileLogger {
    private String databaseUrl;
    private String tableName;
    
    public DatabaseLogger(String name, String level, String filename, 
                         String dbUrl, String table) {
        super(name, level, filename);  // Chain to FileLogger
        this.databaseUrl = dbUrl;
        this.tableName = table;
    }
    
    @Override
    public void log(String message) {
        // Call parent's extended functionality
        super.log(message);  // This calls FileLogger.log() which calls Logger.log()
        
        // Add database logging
        saveToDatabase(message);
    }
    
    @Override
    protected String formatMessage(String message) {
        // Extend parent's formatting
        String parentFormatted = super.formatMessage(message);  // Call parent
        return "[DB] " + parentFormatted + " [/DB]";  // Add database-specific formatting
    }
    
    public void logWithCustomFormat(String message) {
        // Use extended formatting
        String formatted = formatMessage(message);
        log(formatted);
    }
    
    private void saveToDatabase(String message) {
        System.out.println("Saving to database '" + databaseUrl + 
                          "' table '" + tableName + "': " + message);
        // Database saving logic would go here
    }
}

// Usage demonstration
public class MethodExtensionDemo {
    public static void main(String[] args) {
        System.out.println("=== Basic Logger ===");
        Logger basicLogger = new Logger("BasicApp", "INFO");
        basicLogger.log("Application started");
        basicLogger.logError("Connection failed");
        
        System.out.println("\n=== File Logger (Extended) ===");
        FileLogger fileLogger = new FileLogger("FileApp", "DEBUG", "app.log");
        fileLogger.log("User logged in");
        fileLogger.logError("Database connection lost");
        
        System.out.println("\n=== Database Logger (Double Extended) ===");
        DatabaseLogger dbLogger = new DatabaseLogger("DBApp", "INFO", "app.log", 
                                                     "jdbc:mysql://localhost", "logs");
        dbLogger.log("Transaction completed");
        dbLogger.logWithCustomFormat("Custom formatted message");
    }
}
```

</div>

</div>

---
layout: default
---

# super in Constructor Rules

<div class="grid grid-cols-2 gap-8">

<div>

## 📜 Constructor Chain Rules

<v-clicks>

**super() Call Rules:**
- Must be the first statement in constructor
- Cannot be used in static context
- Cannot call both super() and this() in same constructor
- If no explicit super() call, compiler adds super()
- Cannot be used in regular methods, only constructors

**Implicit vs Explicit:**
- Compiler automatically calls super() if not specified
- Must explicitly call super(params) for parameterized parent constructor
- Cannot have parent class without default constructor unless explicit super() call

</v-clicks>

<div v-click="4">

## ❌ Common Mistakes

```java
class Parent {
    public Parent(String name) {  // No default constructor
        // Parent constructor with parameter
    }
}

class Child extends Parent {
    public Child() {
        // ❌ Compilation error - no matching parent constructor
        // Compiler tries to call super() but Parent() doesn't exist
    }
}
```

</div>

</div>

<div>

## ✅ Correct Usage Patterns

```java
class Parent {
    public Parent(String name) {
        // Parent constructor with parameter
    }
}

class Child extends Parent {
    public Child() {
        super("Default Name");  // ✅ Explicit call to Parent(String)
    }
    
    public Child(String name) {
        super(name);  // ✅ Pass parameter to parent
    }
}

// Constructor chaining within same class
class ComplexChild extends Parent {
    private int value;
    
    public ComplexChild() {
        this("Default", 0);  // ✅ Call another constructor in same class
    }
    
    public ComplexChild(String name) {
        this(name, 100);     // ✅ Chain to full constructor
    }
    
    public ComplexChild(String name, int value) {
        super(name);         // ✅ Call parent constructor
        this.value = value;
    }
}

// Cannot mix super() and this()
class InvalidChild extends Parent {
    public InvalidChild() {
        // ❌ Cannot call both
        // super("name");
        // this("other constructor");
    }
}
```

<div class="mt-4 p-4 bg-green-50 rounded-lg">
<strong>✅ Best Practice:</strong> Always ensure parent class has appropriate constructor for child class initialization!
</div>

</div>

</div>

---
layout: default
---

# Real-World Example: Banking System

<div class="grid grid-cols-2 gap-8">

<div>

## 🏦 Account Hierarchy

```java
// Base account class
abstract class Account {
    protected String accountNumber;
    protected String holderName;
    protected double balance;
    protected java.time.LocalDate openingDate;
    protected String branchCode;
    
    public Account(String accountNumber, String holderName, 
                  double initialBalance, String branchCode) {
        this.accountNumber = accountNumber;
        this.holderName = holderName;
        this.balance = initialBalance;
        this.openingDate = java.time.LocalDate.now();
        this.branchCode = branchCode;
        
        // Validation
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        
        System.out.println("Base account created: " + accountNumber);
    }
    
    public void displayAccountInfo() {
        System.out.println("=== Account Information ===");
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Holder Name: " + holderName);
        System.out.println("Balance: $" + String.format("%.2f", balance));
        System.out.println("Opening Date: " + openingDate);
        System.out.println("Branch Code: " + branchCode);
    }
    
    public boolean deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Deposit amount must be positive");
            return false;
        }
        
        balance += amount;
        System.out.println("Deposited: $" + amount);
        return true;
    }
    
    public abstract boolean withdraw(double amount);
    public abstract double calculateInterest();
}

// Savings account implementation
class SavingsAccount extends Account {
    private double interestRate;
    private double minimumBalance;
    private int withdrawalCount;
    private static final int MAX_FREE_WITHDRAWALS = 5;
    
    public SavingsAccount(String accountNumber, String holderName,
                         double initialBalance, String branchCode,
                         double interestRate, double minimumBalance) {
        super(accountNumber, holderName, initialBalance, branchCode);
        this.interestRate = interestRate;
        this.minimumBalance = minimumBalance;
        this.withdrawalCount = 0;
        
        // Additional validation for savings account
        if (initialBalance < minimumBalance) {
            throw new IllegalArgumentException("Initial balance below minimum required");
        }
        
        System.out.println("Savings account created with interest rate: " + 
                          (interestRate * 100) + "%");
    }
}
```

</div>

<div>

## 💳 Enhanced Account Methods

```java
    @Override
    public boolean withdraw(double amount) {
        // Pre-withdrawal validation
        if (amount <= 0) {
            System.out.println("Withdrawal amount must be positive");
            return false;
        }
        
        if (balance - amount < minimumBalance) {
            System.out.println("Insufficient funds. Minimum balance: $" + minimumBalance);
            return false;
        }
        
        // Apply withdrawal fee after free limit
        double fee = 0.0;
        if (withdrawalCount >= MAX_FREE_WITHDRAWALS) {
            fee = 2.0;  // $2 fee
            System.out.println("Withdrawal fee applied: $" + fee);
        }
        
        balance -= (amount + fee);
        withdrawalCount++;
        System.out.println("Withdrawn: $" + amount + " (Fee: $" + fee + ")");
        return true;
    }
    
    @Override
    public double calculateInterest() {
        double interest = balance * interestRate / 12;  // Monthly interest
        System.out.println("Monthly interest: $" + String.format("%.2f", interest));
        return interest;
    }
    
    @Override
    public void displayAccountInfo() {
        super.displayAccountInfo();  // Call parent method
        System.out.println("Account Type: Savings");
        System.out.println("Interest Rate: " + (interestRate * 100) + "% per annum");
        System.out.println("Minimum Balance: $" + minimumBalance);
        System.out.println("Withdrawals this month: " + withdrawalCount);
        System.out.println("Remaining free withdrawals: " + 
                          Math.max(0, MAX_FREE_WITHDRAWALS - withdrawalCount));
    }
    
    public void addInterest() {
        double interest = calculateInterest();
        super.deposit(interest);  // Use parent's deposit method
        System.out.println("Interest credited to account");
    }
}

// Current account with overdraft facility
class CurrentAccount extends Account {
    private double overdraftLimit;
    private double overdraftUsed;
    private double overdraftInterestRate;
    
    public CurrentAccount(String accountNumber, String holderName,
                         double initialBalance, String branchCode,
                         double overdraftLimit) {
        super(accountNumber, holderName, initialBalance, branchCode);
        this.overdraftLimit = overdraftLimit;
        this.overdraftUsed = 0.0;
        this.overdraftInterestRate = 0.15;  // 15% per annum
        System.out.println("Current account created with overdraft limit: $" + overdraftLimit);
    }
    
    @Override
    public boolean withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Withdrawal amount must be positive");
            return false;
        }
        
        double availableBalance = balance + (overdraftLimit - overdraftUsed);
        
        if (amount > availableBalance) {
            System.out.println("Insufficient funds including overdraft facility");
            return false;
        }
        
        if (amount <= balance) {
            balance -= amount;
        } else {
            double overdraftUsage = amount - balance;
            balance = 0;
            overdraftUsed += overdraftUsage;
            System.out.println("Overdraft used: $" + overdraftUsage);
        }
        
        System.out.println("Withdrawn: $" + amount);
        return true;
    }
    
    @Override
    public double calculateInterest() {
        // Current account pays no interest, but charges overdraft interest
        if (overdraftUsed > 0) {
            double overdraftInterest = overdraftUsed * overdraftInterestRate / 12;
            System.out.println("Overdraft interest charge: $" + String.format("%.2f", overdraftInterest));
            return -overdraftInterest;  // Negative because it's a charge
        }
        return 0.0;
    }
    
    @Override
    public void displayAccountInfo() {
        super.displayAccountInfo();  // Call parent method
        System.out.println("Account Type: Current");
        System.out.println("Overdraft Limit: $" + overdraftLimit);
        System.out.println("Overdraft Used: $" + overdraftUsed);
        System.out.println("Available Overdraft: $" + (overdraftLimit - overdraftUsed));
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Exercise: Employee System

<div class="grid grid-cols-2 gap-8">

<div>

## 👥 Design Challenge

**Requirements:**
1. Create an Employee base class with proper initialization
2. Implement Manager and Developer subclasses  
3. Use super() for constructor chaining
4. Use super.method() to extend parent functionality
5. Demonstrate proper validation at each level
6. Show method extension patterns

```java
public class Employee {
    // TODO: Protected fields for inheritance
    // TODO: Constructor with validation
    // TODO: Methods that can be extended
    // TODO: Display method using template pattern
}

public class Manager extends Employee {
    // TODO: Manager-specific fields
    // TODO: Constructor chaining with super()
    // TODO: Method overriding with super calls
    // TODO: Additional validation
}

public class Developer extends Employee {
    // TODO: Developer-specific fields  
    // TODO: Constructor chaining with super()
    // TODO: Method extension using super
    // TODO: Specialized behavior
}
```

</div>

<div>

## 🎯 Expected Implementation

**Features to Implement:**
- Employee base class with comprehensive initialization
- Manager class with team management capabilities
- Developer class with project tracking
- Constructor chaining through all levels
- Method extension preserving parent behavior
- Validation at appropriate levels

**Success Criteria:**
- Proper super() usage in all constructors
- Method extension using super.method()
- Constructor chain validation working
- Parent functionality preserved and extended
- Clean separation of concerns
- Real-world applicability

**Usage Example:**
```java
// Should work after implementation
Manager manager = new Manager("M001", "Alice Johnson", "IT", 
                             80000, "Development Team", 5);

Developer dev = new Developer("D001", "Bob Smith", "IT",
                             70000, "Java", 3);

// All methods should properly chain through inheritance
manager.displayEmployeeInfo();  // Uses super calls
dev.generateReport();           // Extends parent functionality

// Validation should work at all levels
Employee[] employees = {manager, dev};
PayrollSystem.processAll(employees);  // Polymorphic behavior
```

</div>

</div>

---
layout: default
---

# Common super Keyword Mistakes

<div class="space-y-4">

<div class="bg-red-50 p-4 rounded-lg">
<h4 class="font-bold text-red-700">❌ super Keyword Pitfalls</h4>
<div class="grid grid-cols-2 gap-4 mt-2">
<div>
```java
// WRONG: super() not as first statement
class Child extends Parent {
    public Child() {
        int x = 10;      // ❌ Code before super()
        super();         // Must be first statement
    }
}

// WRONG: Using super() in static method
class Child extends Parent {
    public static void method() {
        super.method();  // ❌ Cannot use super in static context
    }
}

// WRONG: Calling both super() and this()
class Child extends Parent {
    public Child() {
        super();         // ❌ Cannot call both
        this("default"); // in same constructor
    }
}
```
</div>
<div>
```java
// WRONG: super() in regular method
class Child extends Parent {
    public void someMethod() {
        super();         // ❌ super() only in constructors
    }
}

// WRONG: Accessing private parent members
class Parent {
    private int value;
}
class Child extends Parent {
    public void method() {
        super.value = 10; // ❌ Cannot access private members
    }
}

// WRONG: Not handling parent constructor requirements
class Parent {
    public Parent(String required) { }
}
class Child extends Parent {
    public Child() {
        // ❌ Missing super(required)
    }
}
```
</div>
</div>
</div>

<div class="bg-green-50 p-4 rounded-lg">
<h4 class="font-bold text-green-700">✅ Correct Approaches</h4>
<div class="grid grid-cols-2 gap-4 mt-2">
<div>
```java
// CORRECT: super() as first statement
class Child extends Parent {
    public Child() {
        super();         // ✅ First statement
        int x = 10;      // Other code after super()
    }
}

// CORRECT: Cannot use super in static context
class Child extends Parent {
    public static void method() {
        Parent.staticMethod(); // ✅ Use class name instead
    }
}

// CORRECT: Either super() or this(), not both
class Child extends Parent {
    public Child() {
        super();         // ✅ Call parent constructor
    }
    
    public Child(String name) {
        this();          // ✅ Call other constructor (which calls super)
    }
}
```
</div>
<div>
```java
// CORRECT: Use super.method() for method calls
class Child extends Parent {
    public void someMethod() {
        super.someMethod(); // ✅ Call parent method
    }
}

// CORRECT: Access protected parent members
class Parent {
    protected int value;
}
class Child extends Parent {
    public void method() {
        super.value = 10; // ✅ Can access protected members
    }
}

// CORRECT: Handle parent constructor requirements
class Parent {
    public Parent(String required) { }
}
class Child extends Parent {
    public Child() {
        super("default"); // ✅ Provide required parameter
    }
}
```
</div>
</div>
</div>

</div>

---
layout: center
class: text-center
---

# Summary

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="bg-blue-50 p-6 rounded-lg">
<h3 class="font-bold text-lg mb-4">📖 What We Learned</h3>
<ul class="text-left space-y-2">
<li>• super keyword for accessing parent class members</li>
<li>• Constructor chaining with super()</li>
<li>• Method extension using super.method()</li>
<li>• Multi-level constructor chaining</li>
<li>• super vs this keyword differences</li>
<li>• Best practices and common mistakes</li>
</ul>
</div>

<div class="bg-green-50 p-6 rounded-lg">
<h3 class="font-bold text-lg mb-4">🎯 Next Steps</h3>
<ul class="text-left space-y-2">
<li>• Abstract classes and abstract methods</li>
<li>• Interface implementation</li>
<li>• Polymorphism and dynamic binding</li>
<li>• Design patterns with inheritance</li>
<li>• Advanced OOP concepts</li>
</ul>
</div>

</div>

<div class="mt-8 text-2xl font-bold text-purple-600">
super keyword mastered! Ready for abstract classes! 🔗🏗️
</div>

---
layout: center
class: text-center
---

# Questions & Discussion

<div class="text-6xl mb-8">❓</div>

<div class="text-xl mb-8">
Any questions about super keyword, constructor chaining, or method extension?
</div>

<div class="text-lg text-gray-600">
Next lecture: **Abstract Classes and Methods**
</div>

<div class="mt-8">
<span class="px-4 py-2 bg-blue-500 text-white rounded-lg">
Ready to explore abstract concepts! 👏
</span>
</div>