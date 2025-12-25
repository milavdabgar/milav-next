---
theme: default
background: https://source.unsplash.com/1024x768/?package,organization
title: Packages in Java
info: |
  ## Java Programming (4343203)
  
  Lecture 21: Packages in Java
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about Java packages, package organization, import statements, classpath, and how to create well-structured Java applications.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Packages in Java
## Lecture 21

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

- 📦 **Understand** the concept and importance of packages in Java
- 🏗️ **Create** packages and organize classes effectively  
- 📥 **Import** classes and packages using different import statements
- 🔧 **Configure** classpath for package compilation and execution
- 🎯 **Apply** naming conventions for packages
- 📝 **Build** structured Java applications using packages
- ⚡ **Resolve** common package-related compilation issues

</v-clicks>

---
layout: default
---

# What are Packages?

<div class="grid grid-cols-2 gap-6">

<div>

## Definition
- **Package** is a namespace that groups related classes and interfaces
- Provides a way to organize classes in a hierarchical manner
- Similar to folders/directories in a file system
- Helps avoid naming conflicts between classes

## Benefits
- **Organization**: Logical grouping of related classes
- **Namespace**: Prevents naming conflicts
- **Access Control**: Package-level access protection
- **Maintenance**: Easier to locate and maintain code

</div>

<div>

```java
// Without packages - naming conflicts possible
class Date { } // Which Date class?

// With packages - clear identification
java.util.Date utilDate;
java.sql.Date sqlDate;
```

## Built-in Packages
```java
java.lang    // String, System, Object
java.util    // ArrayList, Scanner
java.io      // File, InputStream
java.awt     // GUI components
javax.swing  // Swing components
```

</div>

</div>

---
layout: default
---

# Package Declaration

<div class="grid grid-cols-2 gap-6">

<div>

## Syntax
```java
package package_name;
package package.subpackage;
```

## Rules
- Must be first non-comment statement
- Only one package declaration per file
- Package name should be lowercase
- Use reverse domain naming convention

## Example
```java
package com.company.project.module;

public class MyClass {
    // Class implementation
}
```

</div>

<div>

## Directory Structure
```
src/
  com/
    company/
      project/
        module/
          MyClass.java
```

## Naming Convention
```java
// Domain: example.com
// Reverse: com.example

package com.example.utilities;
package com.example.graphics.shapes;
package com.example.database.connection;
```

## Benefits of Convention
- Ensures global uniqueness
- Follows standard practice
- Easy to organize and locate

</div>

</div>

---
layout: default
---

# Creating Packages - Step by Step

<div class="grid grid-cols-2 gap-6">

<div>

## Step 1: Create Directory Structure
```bash
mkdir -p com/university/student
```

## Step 2: Create Class with Package
```java
// File: com/university/student/Student.java
package com.university.student;

public class Student {
    private String name;
    private int rollNo;
    
    public Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }
    
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
    }
}
```

</div>

<div>

## Step 3: Compile from Source Root
```bash
javac com/university/student/Student.java
```

## Step 4: Create Main Class
```java
// File: StudentTest.java
import com.university.student.Student;

public class StudentTest {
    public static void main(String[] args) {
        Student s = new Student("John", 101);
        s.display();
    }
}
```

## Step 5: Compile and Run
```bash
javac StudentTest.java
java StudentTest
```

</div>

</div>

---
layout: default
---

# Import Statements

<div class="grid grid-cols-2 gap-6">

<div>

## Types of Import

### 1. Single Class Import
```java
import java.util.ArrayList;
import java.util.Scanner;
```

### 2. Wildcard Import
```java
import java.util.*;
```

### 3. Static Import
```java
import static java.lang.Math.PI;
import static java.lang.Math.*;
```

### 4. Fully Qualified Names
```java
// No import needed
java.util.ArrayList<String> list = 
    new java.util.ArrayList<>();
```

</div>

<div>

## Import Rules
- Import statements come after package declaration
- Import statements come before class declaration
- No circular imports allowed
- Classes in same package don't need import

```java
package com.example.app;

import java.util.List;
import java.util.ArrayList;
import static java.lang.System.out;

public class MyApp {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        out.println("Hello from package!");
    }
}
```

</div>

</div>

---
layout: default
---

# Default Package vs Named Packages

<div class="grid grid-cols-2 gap-6">

<div>

## Default Package
```java
// No package declaration
public class MyClass {
    public static void main(String[] args) {
        System.out.println("In default package");
    }
}
```

### Characteristics
- No package declaration
- Classes stored in current directory
- Limited access from other packages
- Not recommended for real projects

</div>

<div>

## Named Package
```java
package com.mycompany.myapp;

public class MyClass {
    public static void main(String[] args) {
        System.out.println("In named package");
    }
}
```

### Advantages
- Better organization
- Namespace protection
- Professional structure
- Easy maintenance
- Follows Java conventions

</div>

</div>

---
layout: default
---

# Practical Example: Library Management System

<div class="grid grid-cols-2 gap-6">

<div>

## Package Structure
```
library/
  management/
    books/
      Book.java
      BookManager.java
    members/
      Member.java
      MemberManager.java
    utils/
      DatabaseUtil.java
      ValidationUtil.java
```

## Book.java
```java
package library.management.books;

public class Book {
    private String isbn;
    private String title;
    private String author;
    
    // Constructor
    public Book(String isbn, String title, 
                String author) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
    }
    
    // Getters and setters
    public String getIsbn() { return isbn; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
}
```

</div>

<div>

## Member.java
```java
package library.management.members;

public class Member {
    private int memberId;
    private String name;
    private String email;
    
    public Member(int memberId, String name, 
                  String email) {
        this.memberId = memberId;
        this.name = name;
        this.email = email;
    }
    
    public void displayInfo() {
        System.out.println("ID: " + memberId);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
    }
}
```

## LibraryApp.java (Main)
```java
import library.management.books.Book;
import library.management.members.Member;

public class LibraryApp {
    public static void main(String[] args) {
        Book book = new Book("978-0134685991", 
            "Effective Java", "Joshua Bloch");
        Member member = new Member(1001, 
            "Alice", "alice@email.com");
        
        System.out.println("Library System Started");
        member.displayInfo();
    }
}
```

</div>

</div>

---
layout: default
---

# Classpath and Compilation

<div class="grid grid-cols-2 gap-6">

<div>

## Understanding Classpath
- **Classpath**: Path where Java looks for classes
- Can include directories and JAR files
- Set using -cp or -classpath option

## Setting Classpath
```bash
# Compile with classpath
javac -cp /path/to/classes MyClass.java

# Run with classpath
java -cp /path/to/classes MyClass

# Multiple paths (Unix/Linux)
java -cp /path1:/path2:/path3 MyClass

# Multiple paths (Windows)
java -cp /path1;/path2;/path3 MyClass
```

</div>

<div>

## Compilation Example
```bash
# Directory structure
src/
  com/
    example/
      utils/
        Helper.java
  MyApp.java

# Compile from src directory
cd src
javac com/example/utils/Helper.java
javac -cp . MyApp.java

# Run application
java -cp . MyApp
```

## Common Issues
- ClassNotFoundException
- NoClassDefFoundError  
- Wrong classpath settings
- Missing package declarations

</div>

</div>

---
layout: default
---

# Package Access and Visibility

<div class="grid grid-cols-2 gap-6">

<div>

## Package-Private Access
```java
package com.example.math;

class MathHelper {  // package-private class
    int value;      // package-private field
    
    void calculate() {  // package-private method
        System.out.println("Calculating...");
    }
}

public class Calculator {
    public void performOperation() {
        MathHelper helper = new MathHelper();
        helper.calculate(); // Accessible in same package
    }
}
```

</div>

<div>

## Access from Different Package
```java
package com.example.app;

import com.example.math.Calculator;
// Cannot import MathHelper - not public

public class App {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        calc.performOperation(); // OK
        
        // MathHelper helper = new MathHelper(); 
        // ERROR: Cannot access package-private class
    }
}
```

### Key Points
- Package-private = default access
- Accessible within same package only
- Provides encapsulation at package level

</div>

</div>

---
layout: default
---

# Best Practices for Packages

<div class="grid grid-cols-2 gap-6">

<div>

## Naming Conventions
```java
// Good package names
com.company.project.module
org.apache.commons.lang
edu.university.department.course

// Poor package names
MyPackage
com.Company.Project  // Capital letters
default_package      // Underscores
```

## Organization Principles
- **Logical grouping**: Related classes together
- **Layer separation**: UI, business logic, data access
- **Feature-based**: Each feature in separate package
- **Depth balance**: Not too deep, not too shallow

</div>

<div>

## Package Structure Example
```
com.ecommerce.system/
  ui/
    controllers/
    views/
  business/
    services/
    models/
  data/
    repositories/
    entities/
  utils/
    validation/
    formatting/
```

## Common Mistakes to Avoid
- Circular dependencies between packages
- Too many classes in one package
- Package names with uppercase letters
- Deep nesting (more than 4-5 levels)
- Mixing different concerns in one package

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Creating a Banking Package

<div class="grid grid-cols-2 gap-6">

<div>

## Task
Create a banking application with the following package structure:

```
com.bank.system/
  accounts/
    Account.java
    SavingsAccount.java
  customers/
    Customer.java
  transactions/
    Transaction.java
  utils/
    Calculator.java
```

## Account.java
```java
package com.bank.system.accounts;

public class Account {
    protected String accountNumber;
    protected double balance;
    protected String customerName;
    
    public Account(String accountNumber, 
                   String customerName) {
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.balance = 0.0;
    }
    
    public void deposit(double amount) {
        balance += amount;
    }
    
    public boolean withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    public double getBalance() {
        return balance;
    }
}
```

</div>

<div>

## Customer.java
```java
package com.bank.system.customers;

public class Customer {
    private int customerId;
    private String name;
    private String email;
    private String phone;
    
    public Customer(int customerId, String name, 
                    String email, String phone) {
        this.customerId = customerId;
        this.name = name;
        this.email = email;
        this.phone = phone;
    }
    
    // Getters
    public String getName() { return name; }
    public String getEmail() { return email; }
}
```

## BankApp.java (Main)
```java
import com.bank.system.accounts.Account;
import com.bank.system.customers.Customer;

public class BankApp {
    public static void main(String[] args) {
        Customer customer = new Customer(1001, 
            "John Doe", "john@email.com", "123-456-7890");
        
        Account account = new Account("ACC001", 
            customer.getName());
        
        account.deposit(1000);
        account.withdraw(200);
        
        System.out.println("Balance: " + 
            account.getBalance());
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: E-commerce Package System

<div class="grid grid-cols-2 gap-6">

<div>

## Package Structure
```
com.shop.ecommerce/
  products/
    Product.java
    Category.java
  orders/
    Order.java
    OrderItem.java
  customers/
    Customer.java
    Address.java
  Main.java
```

## Product.java
```java
package com.shop.ecommerce.products;

public class Product {
    private int productId;
    private String name;
    private double price;
    private String category;
    private int stock;
    
    public Product(int productId, String name, 
                   double price, String category) {
        this.productId = productId;
        this.name = name;
        this.price = price;
        this.category = category;
        this.stock = 0;
    }
    
    public void addStock(int quantity) {
        this.stock += quantity;
    }
    
    public boolean isAvailable(int quantity) {
        return stock >= quantity;
    }
    
    // Getters
    public String getName() { return name; }
    public double getPrice() { return price; }
    public int getStock() { return stock; }
}
```

</div>

<div>

## Order.java
```java
package com.shop.ecommerce.orders;

import com.shop.ecommerce.products.Product;
import java.util.ArrayList;
import java.util.List;

public class Order {
    private int orderId;
    private String customerName;
    private List<OrderItem> items;
    private double total;
    
    public Order(int orderId, String customerName) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.items = new ArrayList<>();
        this.total = 0.0;
    }
    
    public void addItem(Product product, int quantity) {
        if (product.isAvailable(quantity)) {
            OrderItem item = new OrderItem(product, quantity);
            items.add(item);
            total += product.getPrice() * quantity;
        }
    }
    
    public double getTotal() { return total; }
    public int getItemCount() { return items.size(); }
}
```

## OrderItem.java
```java
package com.shop.ecommerce.orders;

import com.shop.ecommerce.products.Product;

public class OrderItem {
    private Product product;
    private int quantity;
    private double subtotal;
    
    public OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
        this.subtotal = product.getPrice() * quantity;
    }
    
    public double getSubtotal() { return subtotal; }
}
```

</div>

</div>

---
layout: default
---

# Working with JAR Files and Packages

<div class="grid grid-cols-2 gap-6">

<div>

## Creating JAR Files
```bash
# Create JAR file with packages
jar cvf mylib.jar com/

# Create JAR with manifest
jar cvfm myapp.jar manifest.txt com/

# List JAR contents
jar tvf myapp.jar

# Extract JAR
jar xvf myapp.jar
```

## Manifest File Example
```
Manifest-Version: 1.0
Main-Class: com.example.app.MainApp
Class-Path: lib/utils.jar lib/database.jar
```

</div>

<div>

## Using JAR in Classpath
```bash
# Compile with JAR dependency
javac -cp mylib.jar MyApp.java

# Run with JAR in classpath
java -cp .:mylib.jar MyApp

# Multiple JARs
java -cp .:lib/jar1.jar:lib/jar2.jar MyApp
```

## Benefits of JAR Packaging
- **Portability**: Single file distribution
- **Compression**: Reduced file size
- **Security**: Can be signed
- **Metadata**: Manifest information
- **Classpath**: Easy dependency management

</div>

</div>

---
layout: default
---

# Common Package-Related Issues

<div class="grid grid-cols-2 gap-6">

<div>

## ClassNotFoundException
```java
// Cause: Class not in classpath
Exception in thread "main" 
java.lang.ClassNotFoundException: 
  com.example.MyClass

// Solutions:
// 1. Check classpath setting
// 2. Verify package declaration
// 3. Ensure proper directory structure
// 4. Check compilation location
```

## NoClassDefFoundError
```java
// Cause: Class was available during compilation 
//        but not at runtime

// Solutions:
// 1. Add missing JAR to classpath
// 2. Check for corrupted class files
// 3. Verify all dependencies included
```

</div>

<div>

## Package Declaration Issues
```java
// Wrong: Package doesn't match directory
// File: com/example/MyClass.java
package com.wrong.package;  // ERROR

// Correct:
package com.example;
```

## Import Issues
```java
// Circular import (not allowed)
// Package A imports Package B
// Package B imports Package A

// Solution: Refactor to remove circular dependency
// Use common base package or interface
```

## Compilation Order
```bash
# Wrong: Compile dependent class first
javac MyApp.java  # Uses MyClass
javac com/example/MyClass.java

# Correct: Compile dependencies first
javac com/example/MyClass.java
javac MyApp.java
```

</div>

</div>

---
layout: default
---

# Advanced Package Concepts

<div class="grid grid-cols-2 gap-6">

<div>

## Package Sealing
```java
// In Manifest file
Name: com/example/secure/
Sealed: true

// Prevents external classes from being added
// to the package at runtime
```

## Unnamed Packages
- Classes without package declaration
- Cannot be imported by named packages
- Should be avoided in production code

```java
// Cannot import unnamed package classes
import MyClass;  // ERROR

// Must use fully qualified name or 
// put in same unnamed package
```

</div>

<div>

## Package Versioning
```java
// Use separate packages for different versions
com.mycompany.mylib.v1.API
com.mycompany.mylib.v2.API
```

## Module System (Java 9+)
```java
// module-info.java
module com.example.myapp {
    requires java.base;
    requires com.example.utils;
    
    exports com.example.myapp.api;
}
```

## Reflection with Packages
```java
Package pkg = MyClass.class.getPackage();
System.out.println("Package: " + pkg.getName());
System.out.println("Version: " + 
    pkg.getImplementationVersion());
```

</div>

</div>

---
layout: default
---

# Real-world Application: MVC Package Structure

<div class="grid grid-cols-2 gap-6">

<div>

## MVC Package Organization
```
com.webapp.system/
  controllers/
    UserController.java
    ProductController.java
  models/
    User.java
    Product.java
    DatabaseConnection.java
  views/
    UserView.java
    ProductView.java
  utils/
    ValidationUtil.java
    DateUtil.java
  config/
    AppConfig.java
  Main.java
```

## Controller Example
```java
package com.webapp.system.controllers;

import com.webapp.system.models.User;
import com.webapp.system.views.UserView;

public class UserController {
    private UserView view;
    
    public UserController() {
        this.view = new UserView();
    }
    
    public void createUser(String name, String email) {
        User user = new User(name, email);
        // Process user creation
        view.displayUser(user);
    }
    
    public void listAllUsers() {
        // Get all users and display
        view.displayUserList();
    }
}
```

</div>

<div>

## Model Example
```java
package com.webapp.system.models;

public class User {
    private int userId;
    private String name;
    private String email;
    private boolean active;
    
    public User(String name, String email) {
        this.name = name;
        this.email = email;
        this.active = true;
        // Generate unique ID
        this.userId = generateId();
    }
    
    private int generateId() {
        return (int) (Math.random() * 10000);
    }
    
    // Getters and setters
    public String getName() { return name; }
    public String getEmail() { return email; }
    public boolean isActive() { return active; }
    
    public void activate() { this.active = true; }
    public void deactivate() { this.active = false; }
}
```

## View Example  
```java
package com.webapp.system.views;

import com.webapp.system.models.User;

public class UserView {
    public void displayUser(User user) {
        System.out.println("=== User Details ===");
        System.out.println("Name: " + user.getName());
        System.out.println("Email: " + user.getEmail());
        System.out.println("Status: " + 
            (user.isActive() ? "Active" : "Inactive"));
    }
    
    public void displayUserList() {
        System.out.println("=== User List ===");
        // Display list of users
    }
}
```

</div>

</div>

---
layout: default
---

# Exercise Solutions and Practice

<div class="grid grid-cols-2 gap-6">

<div>

## Exercise 3: University Management
Create a package structure for university management:

```java
// com.university.management.students.Student.java
package com.university.management.students;

public class Student {
    private String studentId;
    private String name;
    private String course;
    private double gpa;
    
    public Student(String studentId, String name, 
                   String course) {
        this.studentId = studentId;
        this.name = name;
        this.course = course;
        this.gpa = 0.0;
    }
    
    public void updateGPA(double newGPA) {
        if (newGPA >= 0.0 && newGPA <= 4.0) {
            this.gpa = newGPA;
        }
    }
    
    public void displayInfo() {
        System.out.println("Student ID: " + studentId);
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
        System.out.println("GPA: " + gpa);
    }
}
```

</div>

<div>

## Testing the Package System
```java
// Main application class
import com.university.management.students.Student;
import com.university.management.courses.Course;
import com.university.management.faculty.Professor;

public class UniversityApp {
    public static void main(String[] args) {
        // Create student
        Student student = new Student("S001", 
            "Alice Johnson", "Computer Science");
        student.updateGPA(3.8);
        
        // Create course
        Course course = new Course("CS101", 
            "Introduction to Programming", 4);
        
        // Create professor
        Professor prof = new Professor("P001", 
            "Dr. Smith", "Computer Science");
        
        // Display information
        student.displayInfo();
        course.displayInfo();
        prof.displayInfo();
        
        System.out.println("University Management System Initialized!");
    }
}
```

## Compilation Steps
```bash
# Create directory structure
mkdir -p com/university/management/{students,courses,faculty}

# Compile all classes
javac com/university/management/*/*.java

# Compile main application
javac UniversityApp.java

# Run application
java UniversityApp
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

- 📦 **Package Fundamentals**: Namespace organization and benefits
- 🏗️ **Package Creation**: Declaration, directory structure, compilation
- 📥 **Import Mechanisms**: Different types of import statements
- 🔧 **Classpath Management**: Setting and managing classpath
- 🎯 **Naming Conventions**: Best practices for package naming
- 📝 **Real Applications**: MVC, banking, e-commerce examples
- ⚡ **Common Issues**: Troubleshooting package problems

</v-clicks>

</div>

<div>

## Best Practices Recap

<v-clicks>

- Use reverse domain naming convention
- Keep package names lowercase
- Organize classes logically
- Avoid circular dependencies
- Use meaningful package structure
- Follow consistent naming patterns
- Document package purposes
- Test package integration

</v-clicks>

## Next Lecture Preview
**Lecture 22: Access Control with Packages**
- Package-level access control
- Protected access across packages
- Visibility rules and inheritance
- Advanced access control patterns

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!

## Questions and Discussion

**Next Lecture**: Access Control with Packages  
**Topic**: Package-level access control, protected access, visibility rules

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Practice the exercises and explore Java packages! <carbon:arrow-right class="inline"/>
  </span>
</div>