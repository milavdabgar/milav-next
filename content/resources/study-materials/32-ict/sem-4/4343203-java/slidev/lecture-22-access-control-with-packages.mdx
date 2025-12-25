---
theme: default
background: https://source.unsplash.com/1024x768/?security,access
title: Access Control with Packages
info: |
  ## Java Programming (4343203)
  
  Lecture 22: Access Control with Packages
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about package-level access control, protected access modifiers, visibility rules across packages, and designing secure class hierarchies.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Access Control with Packages
## Lecture 22

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

- 🔐 **Understand** Java's four access modifiers and their scope
- 📦 **Apply** package-level access control effectively
- 🛡️ **Implement** protected access across inheritance hierarchies
- 🎯 **Design** secure class structures using proper access control
- ⚡ **Resolve** access control conflicts and issues
- 📝 **Practice** advanced access control patterns
- 🏗️ **Build** well-encapsulated Java applications

</v-clicks>

---
layout: default
---

# Java Access Modifiers Overview

<div class="grid grid-cols-2 gap-6">

<div>

## Four Access Levels

| Modifier | Same Class | Same Package | Subclass | Different Package |
|----------|------------|--------------|----------|-------------------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| (default) | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

## Key Concepts
- **Encapsulation**: Hiding internal implementation
- **Controlled Access**: Exposing only necessary parts
- **Package Boundaries**: Natural access control barriers
- **Inheritance Support**: Protected access for subclasses

</div>

<div>

## Access Control Hierarchy

```java
public class AccessExample {
    private int privateField;       // Most restrictive
    int packageField;               // Package-private
    protected int protectedField;   // Subclass access
    public int publicField;         // Least restrictive
    
    private void privateMethod() { }
    void packageMethod() { }
    protected void protectedMethod() { }  
    public void publicMethod() { }
}
```

## Benefits
- **Security**: Prevents unauthorized access
- **Maintainability**: Clear API boundaries
- **Flexibility**: Easy to change internal implementation
- **Documentation**: Access level indicates intended usage

</div>

</div>

---
layout: default
---

# Package-Private Access (Default)

<div class="grid grid-cols-2 gap-6">

<div>

## Default Access Rules
- No access modifier specified
- Accessible within the same package only
- Cannot be accessed from different packages
- Provides package-level encapsulation

## Example: Same Package Access
```java
// File: com/example/math/Calculator.java
package com.example.math;

class MathUtils {  // package-private class
    int value = 10;  // package-private field
    
    void calculate() {  // package-private method
        System.out.println("Calculating: " + value);
    }
}

public class Calculator {
    public void performOperation() {
        MathUtils utils = new MathUtils();
        utils.value = 20;      // OK - same package
        utils.calculate();     // OK - same package
    }
}
```

</div>

<div>

## Different Package Access
```java
// File: com/example/app/App.java
package com.example.app;

import com.example.math.Calculator;
// Cannot import MathUtils - package-private

public class App {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        calc.performOperation();  // OK - public method
        
        // MathUtils utils = new MathUtils(); 
        // ERROR: Cannot access package-private class
    }
}
```

## When to Use Default Access
- Internal helper classes
- Implementation details
- Package-level utilities
- Classes that shouldn't be part of public API

</div>

</div>

---
layout: default
---

# Protected Access Modifier

<div class="grid grid-cols-2 gap-6">

<div>

## Protected Access Rules
- Accessible within same package
- Accessible by subclasses in any package
- Not accessible by non-subclasses in different packages
- Supports inheritance while maintaining encapsulation

## Base Class Example
```java
// File: com/example/shapes/Shape.java
package com.example.shapes;

public class Shape {
    protected double x, y;        // Position
    protected String color;       // Color
    
    protected void setPosition(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    protected void setColor(String color) {
        this.color = color;
    }
    
    public void display() {
        System.out.println("Shape at (" + x + "," + y + 
                         ") with color " + color);
    }
}
```

</div>

<div>

## Subclass Access
```java
// File: com/example/graphics/Circle.java
package com.example.graphics;

import com.example.shapes.Shape;

public class Circle extends Shape {
    private double radius;
    
    public Circle(double x, double y, 
                  double radius, String color) {
        // Can access protected members
        this.x = x;              // OK - protected field
        this.y = y;              // OK - protected field
        this.radius = radius;
        setColor(color);         // OK - protected method
    }
    
    public void resize(double newRadius) {
        this.radius = newRadius;
        // Can access inherited protected members
        setPosition(x, y);       // OK - protected method
    }
    
    public double getArea() {
        return Math.PI * radius * radius;
    }
}
```

</div>

</div>

---
layout: default
---

# Protected Access: Same vs Different Package

<div class="grid grid-cols-2 gap-6">

<div>

## Same Package Access
```java
// File: com/example/shapes/Rectangle.java
package com.example.shapes;

public class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double x, double y, 
                     double width, double height) {
        // Protected access within same package
        this.x = x;          // OK
        this.y = y;          // OK  
        this.width = width;
        this.height = height;
    }
}

// Non-subclass in same package
class ShapeUtil {
    public void moveShape(Shape shape) {
        // Protected access within same package
        shape.x = 10;        // OK - same package
        shape.y = 20;        // OK - same package
        shape.setColor("red"); // OK - same package
    }
}
```

</div>

<div>

## Different Package Access
```java
// File: com/example/graphics/Triangle.java
package com.example.graphics;

import com.example.shapes.Shape;

public class Triangle extends Shape {
    public Triangle() {
        // Protected access through inheritance
        this.x = 0;          // OK - subclass access
        this.y = 0;          // OK - subclass access
        setColor("blue");    // OK - inherited method
    }
}

// Non-subclass in different package
class GraphicsUtil {
    public void processShape(Shape shape) {
        // shape.x = 10;     // ERROR - different package, not subclass
        // shape.setColor("red"); // ERROR - different package
        shape.display();     // OK - public method
    }
}
```

## Key Rule
Protected members are accessible to subclasses **only through inheritance**, not through object references in different packages.

</div>

</div>

---
layout: default
---

# Public Access Modifier

<div class="grid grid-cols-2 gap-6">

<div>

## Public Access Characteristics
- Accessible from anywhere in the application
- No restrictions on access
- Forms the public API of classes
- Should be used judiciously

## Public API Example
```java
// File: com/example/library/Book.java
package com.example.library;

public class Book {
    private String isbn;           // Private
    private String title;          // Private
    private String author;         // Private
    
    // Public constructor
    public Book(String isbn, String title, 
                String author) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
    }
    
    // Public getter methods
    public String getIsbn() { return isbn; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    
    // Public utility method
    public String getFullInfo() {
        return title + " by " + author + 
               " (ISBN: " + isbn + ")";
    }
}
```

</div>

<div>

## Using Public API
```java
// File: com/example/app/LibraryApp.java
package com.example.app;

import com.example.library.Book;

public class LibraryApp {
    public static void main(String[] args) {
        // Can access public constructor
        Book book = new Book("978-0134685991", 
                           "Effective Java", 
                           "Joshua Bloch");
        
        // Can access public methods
        System.out.println("Title: " + book.getTitle());
        System.out.println("Author: " + book.getAuthor());
        System.out.println("Info: " + book.getFullInfo());
        
        // Cannot access private fields
        // System.out.println(book.isbn); // ERROR
    }
}
```

## Public Access Guidelines
- Use for API methods and constructors
- Keep public interface minimal
- Document public methods well
- Consider backward compatibility

</div>

</div>

---
layout: default
---

# Private Access Modifier

<div class="grid grid-cols-2 gap-6">

<div>

## Private Access Rules
- Accessible only within the same class
- Most restrictive access level
- Provides strong encapsulation
- Cannot be accessed by subclasses

## Private Implementation Example
```java
public class BankAccount {
    private double balance;        // Private field
    private String accountNumber;  // Private field
    private boolean isActive;      // Private field
    
    public BankAccount(String accountNumber) {
        this.accountNumber = accountNumber;
        this.balance = 0.0;
        this.isActive = true;
    }
    
    // Private helper methods
    private boolean validateAmount(double amount) {
        return amount > 0 && amount <= 10000;
    }
    
    private void logTransaction(String type, double amount) {
        System.out.println(type + ": " + amount + 
                         " | Balance: " + balance);
    }
    
    // Public methods using private members
    public boolean deposit(double amount) {
        if (validateAmount(amount)) {  // Private method
            balance += amount;         // Private field
            logTransaction("DEPOSIT", amount);
            return true;
        }
        return false;
    }
}
```

</div>

<div>

## Private Access Benefits
```java
public class StudentGradeCalculator {
    private double[] scores;
    private int numScores;
    private double average;
    private boolean calculated;
    
    public StudentGradeCalculator(int maxScores) {
        scores = new double[maxScores];
        numScores = 0;
        calculated = false;
    }
    
    // Private calculation logic
    private void calculateAverage() {
        if (numScores > 0) {
            double sum = 0;
            for (int i = 0; i < numScores; i++) {
                sum += scores[i];
            }
            average = sum / numScores;
            calculated = true;
        }
    }
    
    private char determineGrade(double avg) {
        if (avg >= 90) return 'A';
        if (avg >= 80) return 'B';
        if (avg >= 70) return 'C';
        if (avg >= 60) return 'D';
        return 'F';
    }
    
    // Public interface
    public void addScore(double score) {
        if (numScores < scores.length) {
            scores[numScores++] = score;
            calculated = false; // Invalidate calculation
        }
    }
    
    public char getFinalGrade() {
        if (!calculated) calculateAverage();
        return determineGrade(average);
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Example: Employee Management System

<div class="grid grid-cols-2 gap-6">

<div>

## Base Employee Class
```java
// File: com/company/hr/Employee.java
package com.company.hr;

public class Employee {
    private int employeeId;           // Private
    protected String name;            // Protected
    protected String department;      // Protected
    double salary;                    // Package-private
    public String email;              // Public
    
    public Employee(int id, String name, 
                    String dept, double salary) {
        this.employeeId = id;
        this.name = name;
        this.department = dept;
        this.salary = salary;
        this.email = generateEmail();
    }
    
    // Private helper method
    private String generateEmail() {
        return name.toLowerCase().replace(" ", ".") + 
               "@company.com";
    }
    
    // Protected method for subclasses
    protected void setSalary(double salary) {
        if (salary > 0) {
            this.salary = salary;
        }
    }
    
    // Package-private method
    void updateDepartment(String dept) {
        this.department = dept;
    }
    
    // Public methods
    public int getId() { return employeeId; }
    public String getName() { return name; }
    public void displayInfo() {
        System.out.println("Employee: " + name);
        System.out.println("Department: " + department);
        System.out.println("Email: " + email);
    }
}
```

</div>

<div>

## Manager Subclass (Different Package)
```java
// File: com/company/management/Manager.java
package com.company.management;

import com.company.hr.Employee;

public class Manager extends Employee {
    private int teamSize;
    private double bonus;
    
    public Manager(int id, String name, String dept, 
                   double salary, int teamSize) {
        super(id, name, dept, salary);
        this.teamSize = teamSize;
        this.bonus = 0;
    }
    
    // Can access protected members
    public void promoteEmployee() {
        System.out.println("Manager " + name +  // OK - protected
                         " promoting in " + department); // OK - protected
    }
    
    // Can use protected method
    public void giveRaise(double amount) {
        setSalary(salary + amount);  // OK - protected method
        // Note: salary is package-private, accessible through inheritance
    }
    
    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Team Size: " + teamSize);
        System.out.println("Bonus: " + bonus);
    }
}
```

</div>

</div>

---
layout: default
---

# Access Control in Different Scenarios

<div class="grid grid-cols-2 gap-6">

<div>

## Same Package, Non-Inheritance
```java
// File: com/company/hr/HRUtil.java
package com.company.hr;

public class HRUtil {
    public void processEmployee(Employee emp) {
        // Can access public
        System.out.println("Processing: " + emp.getName());
        
        // Can access package-private
        emp.salary *= 1.05;  // OK - same package
        emp.updateDepartment("Updated Dept"); // OK - same package
        
        // Can access protected (same package)
        emp.name = "Updated Name";  // OK - same package
        emp.setSalary(50000);       // OK - same package
        
        // Cannot access private
        // emp.employeeId = 123;    // ERROR - private
    }
}
```

## Different Package, Non-Inheritance
```java
// File: com/company/payroll/PayrollSystem.java
package com.company.payroll;

import com.company.hr.Employee;

public class PayrollSystem {
    public void calculatePay(Employee emp) {
        // Can access public only
        System.out.println("Processing pay for: " + 
                         emp.getName());    // OK - public
        
        // Cannot access others
        // emp.salary = 50000;      // ERROR - package-private
        // emp.name = "New Name";   // ERROR - protected
        // emp.setSalary(50000);    // ERROR - protected
    }
}
```

</div>

<div>

## Access Through Object Reference vs Inheritance
```java
// File: com/company/management/Director.java
package com.company.management;

import com.company.hr.Employee;

public class Director extends Employee {
    public Director(int id, String name, String dept, 
                   double salary) {
        super(id, name, dept, salary);
    }
    
    public void manageEmployees(Employee emp, 
                               Director other) {
        // Own protected members (inheritance)
        this.name = "Director " + this.name;  // OK
        this.setSalary(100000);               // OK
        
        // Other Director's protected members
        other.name = "Updated";               // OK - same class
        other.setSalary(95000);               // OK - same class
        
        // Employee's protected members (not through inheritance)
        // emp.name = "Updated";              // ERROR - not inheritance
        // emp.setSalary(50000);              // ERROR - not inheritance
        
        // Public members always accessible
        emp.displayInfo();                    // OK - public
    }
}
```

## Key Rule
Protected access through inheritance is different from protected access through object references across packages.

</div>

</div>

---
layout: default
---

# Common Access Control Mistakes

<div class="grid grid-cols-2 gap-6">

<div>

## Mistake 1: Overexposing Internal State
```java
// BAD: Public fields expose internal state
public class BadEmployee {
    public double salary;      // Anyone can modify
    public String ssn;         // Sensitive data exposed
    public List<String> projects; // Mutable collection
}

// GOOD: Proper encapsulation
public class GoodEmployee {
    private double salary;
    private String ssn;
    private List<String> projects = new ArrayList<>();
    
    public double getSalary() { return salary; }
    public void setSalary(double salary) {
        if (salary > 0) this.salary = salary;
    }
    
    public List<String> getProjects() {
        return new ArrayList<>(projects); // Defensive copy
    }
}
```

## Mistake 2: Wrong Access Level
```java
// BAD: Making everything public
public class BadClass {
    public void helperMethod() { } // Should be private
    public int internalCounter;    // Should be private
}

// GOOD: Appropriate access levels
public class GoodClass {
    private int internalCounter;
    
    private void helperMethod() { } // Implementation detail
    
    public void publicAPI() {      // Only public interface
        helperMethod();
    }
}
```

</div>

<div>

## Mistake 3: Protected Field Access
```java
// PROBLEMATIC: Protected fields
public class Shape {
    protected double x, y;     // Direct field access
}

class Circle extends Shape {
    public void move(double dx, double dy) {
        x += dx;  // Direct field access
        y += dy;  // No validation possible
    }
}

// BETTER: Protected methods
public class BetterShape {
    private double x, y;
    
    protected void setPosition(double x, double y) {
        if (x >= 0 && y >= 0) {  // Validation possible
            this.x = x;
            this.y = y;
        }
    }
    
    protected double getX() { return x; }
    protected double getY() { return y; }
}
```

## Mistake 4: Package-Private Collections
```java
// RISKY: Mutable package-private collection
class DataManager {
    List<String> data = new ArrayList<>(); // Mutable, exposed
}

// SAFER: Controlled access
class BetterDataManager {
    private List<String> data = new ArrayList<>();
    
    List<String> getData() {  // Package-private getter
        return Collections.unmodifiableList(data);
    }
    
    void addData(String item) {  // Controlled modification
        if (item != null && !item.isEmpty()) {
            data.add(item);
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Banking System Access Control

<div class="grid grid-cols-2 gap-6">

<div>

## Task
Design a banking system with proper access control:

## Account Base Class
```java
// File: com/bank/accounts/Account.java
package com.bank.accounts;

public abstract class Account {
    private String accountNumber;      // Private
    protected double balance;          // Protected
    protected String customerName;     // Protected
    String accountType;                // Package-private
    
    public Account(String accountNumber, 
                   String customerName, 
                   String accountType) {
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.accountType = accountType;
        this.balance = 0.0;
    }
    
    // Private validation
    private boolean isValidAmount(double amount) {
        return amount > 0;
    }
    
    // Protected methods for subclasses
    protected boolean canWithdraw(double amount) {
        return balance >= amount;
    }
    
    protected void updateBalance(double amount) {
        balance += amount;
    }
    
    // Public API
    public String getAccountNumber() {
        return accountNumber;
    }
    
    public double getBalance() {
        return balance;
    }
    
    public boolean deposit(double amount) {
        if (isValidAmount(amount)) {
            updateBalance(amount);
            return true;
        }
        return false;
    }
    
    public abstract boolean withdraw(double amount);
}
```

</div>

<div>

## Savings Account Implementation
```java
// File: com/bank/accounts/SavingsAccount.java
package com.bank.accounts;

public class SavingsAccount extends Account {
    private double minimumBalance = 100.0;  // Private
    private double interestRate = 0.03;     // Private
    
    public SavingsAccount(String accountNumber, 
                         String customerName) {
        super(accountNumber, customerName, "SAVINGS");
    }
    
    @Override
    public boolean withdraw(double amount) {
        // Use protected method from parent
        if (canWithdraw(amount) && 
            (balance - amount) >= minimumBalance) {
            updateBalance(-amount);  // Protected method
            return true;
        }
        return false;
    }
    
    // Private method
    private double calculateInterest() {
        return balance * interestRate / 12;
    }
    
    // Public method
    public void addMonthlyInterest() {
        double interest = calculateInterest();
        updateBalance(interest);  // Protected method
        System.out.println("Interest added: " + interest);
    }
    
    // Package-private method for bank operations
    void setMinimumBalance(double minBalance) {
        this.minimumBalance = minBalance;
    }
}
```

## Bank Manager Class
```java
// File: com/bank/accounts/BankManager.java  
package com.bank.accounts;

public class BankManager {
    public void manageAccount(SavingsAccount account) {
        // Can access package-private members
        account.accountType = "PREMIUM_SAVINGS";
        account.setMinimumBalance(500.0);
        
        // Can access public methods
        account.deposit(1000);
        System.out.println("Balance: " + account.getBalance());
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Library Management Access Control

<div class="grid grid-cols-2 gap-6">

<div>

## Library Item Base Class
```java
// File: com/library/items/LibraryItem.java
package com.library.items;

import java.time.LocalDate;

public abstract class LibraryItem {
    private String itemId;             // Private
    protected String title;            // Protected
    protected boolean isAvailable;     // Protected
    LocalDate lastAccessed;            // Package-private
    
    public LibraryItem(String itemId, String title) {
        this.itemId = itemId;
        this.title = title;
        this.isAvailable = true;
        this.lastAccessed = LocalDate.now();
    }
    
    // Private methods
    private boolean validateId(String id) {
        return id != null && id.length() > 5;
    }
    
    private void updateAccess() {
        lastAccessed = LocalDate.now();
    }
    
    // Protected methods for subclasses
    protected void setAvailability(boolean available) {
        this.isAvailable = available;
        updateAccess();
    }
    
    // Package-private method
    void performMaintenance() {
        updateAccess();
        System.out.println("Maintenance performed on: " + title);
    }
    
    // Public API
    public String getItemId() { return itemId; }
    public String getTitle() { return title; }
    public boolean isAvailable() { return isAvailable; }
    
    public abstract void displayDetails();
    public abstract double calculateFine(int daysLate);
}
```

</div>

<div>

## Book Implementation
```java
// File: com/library/items/Book.java
package com.library.items;

public class Book extends LibraryItem {
    private String author;      // Private
    private int pages;          // Private
    private String isbn;        // Private
    
    public Book(String itemId, String title, 
                String author, String isbn) {
        super(itemId, title);
        this.author = author;
        this.isbn = isbn;
    }
    
    // Private helper
    private String formatBookInfo() {
        return title + " by " + author;  // Protected field access
    }
    
    @Override
    public void displayDetails() {
        System.out.println("Book: " + formatBookInfo());
        System.out.println("ISBN: " + isbn);
        System.out.println("Available: " + 
                         (isAvailable ? "Yes" : "No"));  // Protected field
    }
    
    @Override
    public double calculateFine(int daysLate) {
        return daysLate * 0.50;  // 50 cents per day
    }
    
    // Public methods for checkout system
    public boolean checkout() {
        if (isAvailable) {       // Protected field
            setAvailability(false);  // Protected method
            return true;
        }
        return false;
    }
    
    public void returnBook() {
        setAvailability(true);   // Protected method
    }
}
```

## Library System
```java
// File: com/library/system/LibrarySystem.java
package com.library.system;

import com.library.items.Book;
import com.library.items.LibraryItem;

public class LibrarySystem {
    public void processItem(Book book) {
        // Can access public methods
        book.displayDetails();           // OK - public
        System.out.println("ID: " + book.getItemId()); // OK - public
        
        // Cannot access protected/private
        // book.title = "New Title";     // ERROR - different package
        // book.setAvailability(true);   // ERROR - protected
    }
}
```

</div>

</div>

---
layout: default
---

# Advanced Access Control Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Builder Pattern with Access Control
```java
public class User {
    private final String username;     // Immutable
    private final String email;        // Immutable
    private final String password;     // Private
    
    // Private constructor
    private User(Builder builder) {
        this.username = builder.username;
        this.email = builder.email;
        this.password = hashPassword(builder.password);
    }
    
    private String hashPassword(String password) {
        // Password hashing logic
        return "hashed_" + password;
    }
    
    public String getUsername() { return username; }
    public String getEmail() { return email; }
    
    // Public static builder class
    public static class Builder {
        private String username;
        private String email;
        private String password;
        
        public Builder setUsername(String username) {
            this.username = username;
            return this;
        }
        
        public Builder setEmail(String email) {
            this.email = email;
            return this;
        }
        
        public Builder setPassword(String password) {
            this.password = password;
            return this;
        }
        
        public User build() {
            return new User(this);  // Access private constructor
        }
    }
}
```

</div>

<div>

## Factory Pattern with Package-Private
```java
// File: com/example/factory/Vehicle.java
package com.example.factory;

public abstract class Vehicle {
    protected String model;
    protected String color;
    
    // Package-private constructor
    Vehicle(String model, String color) {
        this.model = model;
        this.color = color;
    }
    
    public abstract void start();
    public String getModel() { return model; }
}

// Concrete implementations
class Car extends Vehicle {
    Car(String model, String color) {
        super(model, color);
    }
    
    @Override
    public void start() {
        System.out.println("Car " + model + " starting...");
    }
}

class Motorcycle extends Vehicle {
    Motorcycle(String model, String color) {
        super(model, color);
    }
    
    @Override
    public void start() {
        System.out.println("Motorcycle " + model + " starting...");
    }
}

// Factory class
public class VehicleFactory {
    public static Vehicle createCar(String model, String color) {
        return new Car(model, color);  // Package-private access
    }
    
    public static Vehicle createMotorcycle(String model, String color) {
        return new Motorcycle(model, color);  // Package-private access
    }
}
```

## Usage
```java
Vehicle car = VehicleFactory.createCar("Toyota", "Red");
// new Car("Honda", "Blue");  // ERROR - package-private constructor
```

</div>

</div>

---
layout: default
---

# Access Control Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Design Principles

### 1. Principle of Least Privilege
```java
public class Calculator {
    private double result = 0;
    
    // Private helper - not part of public API
    private boolean isValidNumber(double num) {
        return !Double.isNaN(num) && !Double.isInfinite(num);
    }
    
    // Protected for specialized calculators
    protected void setResult(double result) {
        if (isValidNumber(result)) {
            this.result = result;
        }
    }
    
    // Public API - minimal interface
    public double add(double num) {
        if (isValidNumber(num)) {
            result += num;
        }
        return result;
    }
    
    public double getResult() { return result; }
}
```

### 2. Consistent Access Levels
```java
public class Student {
    private String studentId;      // All fields private
    private String name;
    private double gpa;
    
    public Student(String id, String name) {  // Public constructor
        this.studentId = id;
        this.name = name;
        this.gpa = 0.0;
    }
    
    // Consistent public getters
    public String getStudentId() { return studentId; }
    public String getName() { return name; }
    public double getGpa() { return gpa; }
    
    // Controlled modification
    public void updateGpa(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) {
            this.gpa = gpa;
        }
    }
}
```

</div>

<div>

## Common Patterns

### 3. Package-Private Implementation
```java
// Public interface
public interface DataProcessor {
    void processData(String data);
    String getResult();
}

// Package-private implementation
class SimpleDataProcessor implements DataProcessor {
    private String result;
    
    @Override
    public void processData(String data) {
        result = data.toUpperCase();
    }
    
    @Override
    public String getResult() { return result; }
}

// Public factory
public class ProcessorFactory {
    public static DataProcessor createProcessor() {
        return new SimpleDataProcessor();
    }
}
```

### 4. Protected Template Methods
```java
public abstract class GameCharacter {
    protected int health = 100;
    protected int energy = 50;
    
    // Template method - public
    public final void performAction() {
        if (canPerformAction()) {     // Protected hook
            executeAction();          // Protected abstract
            consumeEnergy();          // Private implementation
        }
    }
    
    // Protected hooks for subclasses
    protected boolean canPerformAction() {
        return energy > 0 && health > 0;
    }
    
    protected abstract void executeAction();
    
    // Private implementation detail
    private void consumeEnergy() {
        energy -= 10;
    }
}
```

</div>

</div>

---
layout: default
---

# Testing Access Control

<div class="grid grid-cols-2 gap-6">

<div>

## Unit Testing Considerations
```java
public class MathUtils {
    private static final double EPSILON = 0.0001;
    
    // Package-private for testing
    static boolean isEqual(double a, double b) {
        return Math.abs(a - b) < EPSILON;
    }
    
    public static double divide(double a, double b) {
        if (isEqual(b, 0.0)) {  // Use package-private method
            throw new IllegalArgumentException("Division by zero");
        }
        return a / b;
    }
}

// Test class in same package
class MathUtilsTest {
    @Test
    public void testIsEqual() {
        // Can access package-private method
        assertTrue(MathUtils.isEqual(1.0, 1.0001));
        assertFalse(MathUtils.isEqual(1.0, 2.0));
    }
    
    @Test
    public void testDivide() {
        assertEquals(2.0, MathUtils.divide(4.0, 2.0), 0.001);
        assertThrows(IllegalArgumentException.class, 
                    () -> MathUtils.divide(1.0, 0.0));
    }
}
```

</div>

<div>

## Reflection for Testing Private Methods
```java
import java.lang.reflect.Method;

public class ReflectionTestExample {
    
    @Test
    public void testPrivateMethod() throws Exception {
        Calculator calc = new Calculator();
        
        // Access private method via reflection
        Method privateMethod = Calculator.class
            .getDeclaredMethod("validateInput", double.class);
        privateMethod.setAccessible(true);
        
        // Test private method
        boolean result = (boolean) privateMethod.invoke(calc, 5.0);
        assertTrue(result);
        
        boolean invalidResult = (boolean) privateMethod.invoke(calc, Double.NaN);
        assertFalse(invalidResult);
    }
}
```

## Alternative: Package-Private Test Methods
```java
public class Calculator {
    private double result = 0;
    
    private boolean validateInput(double input) {
        return !Double.isNaN(input) && !Double.isInfinite(input);
    }
    
    // Package-private method for testing
    boolean testValidateInput(double input) {
        return validateInput(input);  // Delegate to private method
    }
    
    public double add(double value) {
        if (validateInput(value)) {
            result += value;
        }
        return result;
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

- 🔐 **Access Modifiers**: private, default, protected, public and their scope
- 📦 **Package-Level Control**: Default access within package boundaries
- 🛡️ **Protected Access**: Inheritance-based access across packages
- 🎯 **Design Patterns**: Proper access control in real applications
- ⚡ **Common Mistakes**: Overexposure and wrong access levels
- 📝 **Best Practices**: Principle of least privilege and consistent design
- 🏗️ **Testing**: Approaches for testing different access levels

</v-clicks>

</div>

<div>

## Access Control Hierarchy
```java
private     →  Most Restrictive
(default)   →  Package Level
protected   →  Inheritance + Package
public      →  Least Restrictive
```

## Best Practices Recap

<v-clicks>

- Start with most restrictive access level
- Use private for implementation details
- Use protected for inheritance-based extension
- Use package-private for internal APIs
- Use public sparingly for external APIs
- Document access level decisions
- Test access control boundaries
- Consider maintainability and evolution

</v-clicks>

## Next Lecture Preview
**Lecture 23: Interfaces**
- Interface declaration and structure
- Default and static methods
- Functional interfaces
- Interface-based design

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!

## Questions and Discussion

**Next Lecture**: Interfaces  
**Topic**: Interface declaration, default methods, functional interfaces

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Practice access control design patterns! <carbon:arrow-right class="inline"/>
  </span>
</div>