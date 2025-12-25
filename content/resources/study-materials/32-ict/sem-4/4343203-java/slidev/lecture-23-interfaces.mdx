---
theme: default
background: https://source.unsplash.com/1024x768/?interface,contract
title: Interfaces
info: |
  ## Java Programming (4343203)
  
  Lecture 23: Interfaces
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about Java interfaces, interface declaration, default methods, static methods, functional interfaces, and interface-based design patterns.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Interfaces
## Lecture 23

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

- 🎯 **Understand** the concept and purpose of interfaces in Java
- 📋 **Declare** interfaces with abstract, default, and static methods
- 🔧 **Implement** interfaces in classes and handle multiple inheritance
- 🚀 **Apply** interface-based design patterns effectively
- ⚡ **Create** functional interfaces for lambda expressions
- 📝 **Design** flexible and maintainable code using interfaces
- 🏗️ **Practice** advanced interface concepts and best practices

</v-clicks>

---
layout: default
---

# What are Interfaces?

<div class="grid grid-cols-2 gap-6">

<div>

## Definition
- **Interface** is a contract that defines what a class can do
- Contains method signatures without implementation (abstract methods)
- Specifies behavior that implementing classes must provide
- Supports multiple inheritance through implementation

## Key Characteristics
- All methods are implicitly `public abstract` (before Java 8)
- All variables are implicitly `public static final`
- Cannot be instantiated directly
- Can contain default methods (Java 8+)
- Can contain static methods (Java 8+)
- Can contain private methods (Java 9+)

</div>

<div>

## Interface vs Class vs Abstract Class

| Feature | Interface | Abstract Class | Class |
|---------|-----------|----------------|-------|
| Instantiation | ❌ | ❌ | ✅ |
| Multiple Inheritance | ✅ | ❌ | ❌ |
| Constructor | ❌ | ✅ | ✅ |
| Instance Variables | ❌ | ✅ | ✅ |
| Abstract Methods | ✅ | ✅ | ❌ |
| Concrete Methods | ✅* | ✅ | ✅ |

*Default methods (Java 8+)

## Benefits
- **Abstraction**: Hide implementation details
- **Multiple Inheritance**: Implement multiple interfaces
- **Polymorphism**: Reference by interface type
- **Loose Coupling**: Depend on abstraction, not implementation

</div>

</div>

---
layout: default
---

# Basic Interface Declaration

<div class="grid grid-cols-2 gap-6">

<div>

## Simple Interface
```java
public interface Drawable {
    // Abstract method (implicitly public abstract)
    void draw();
    
    // Constants (implicitly public static final)
    String DEFAULT_COLOR = "BLACK";
    int MAX_SIZE = 1000;
}
```

## Interface Implementation
```java
public class Circle implements Drawable {
    private double radius;
    private String color;
    
    public Circle(double radius) {
        this.radius = radius;
        this.color = Drawable.DEFAULT_COLOR;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius: " 
                         + radius + " and color: " + color);
    }
    
    public void setColor(String color) {
        this.color = color;
    }
}
```

</div>

<div>

## Multiple Method Interface
```java
public interface Shape {
    // Abstract methods
    double calculateArea();
    double calculatePerimeter();
    void display();
    
    // Constants
    String SHAPE_TYPE = "GEOMETRIC_SHAPE";
    double PI = 3.14159;
}

public class Rectangle implements Shape {
    private double length, width;
    
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }
    
    @Override
    public double calculateArea() {
        return length * width;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * (length + width);
    }
    
    @Override
    public void display() {
        System.out.println("Rectangle: " + length + " x " + width);
        System.out.println("Area: " + calculateArea());
        System.out.println("Perimeter: " + calculatePerimeter());
    }
}
```

</div>

</div>

---
layout: default
---

# Default Methods (Java 8+)

<div class="grid grid-cols-2 gap-6">

<div>

## Default Method Syntax
```java
public interface Vehicle {
    // Abstract methods
    void start();
    void stop();
    
    // Default method with implementation
    default void displayInfo() {
        System.out.println("This is a vehicle");
        System.out.println("Brand: " + getBrand());
    }
    
    default String getBrand() {
        return "Generic Vehicle";
    }
    
    // Static method
    static void showVehicleTypes() {
        System.out.println("Types: Car, Bike, Truck");
    }
}
```

## Using Default Methods
```java
public class Car implements Vehicle {
    private String model;
    private String brand;
    
    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }
    
    @Override
    public void start() {
        System.out.println(brand + " " + model + " is starting...");
    }
    
    @Override
    public void stop() {
        System.out.println(brand + " " + model + " has stopped.");
    }
    
    // Override default method (optional)
    @Override
    public String getBrand() {
        return brand;
    }
    
    // Can use default displayInfo() as is
    // or override it if needed
}
```

</div>

<div>

## Benefits of Default Methods
```java
// Usage example
public class VehicleDemo {
    public static void main(String[] args) {
        Car car = new Car("Toyota", "Camry");
        
        // Abstract methods
        car.start();
        car.stop();
        
        // Default method (inherited)
        car.displayInfo();
        
        // Static method
        Vehicle.showVehicleTypes();
    }
}
```

### Output:
```
Toyota Camry is starting...
Toyota Camry has stopped.
This is a vehicle
Brand: Toyota
Types: Car, Bike, Truck
```

## Why Default Methods?
- **Backward Compatibility**: Add new methods without breaking existing implementations
- **Code Reuse**: Provide common implementation for similar behavior
- **Evolution**: Allow interfaces to evolve over time
- **Utility Methods**: Include helper methods in interfaces

## Rules for Default Methods
- Can be overridden in implementing classes
- Cannot be static or final
- Cannot override Object class methods
- Must be declared with `default` keyword

</div>

</div>

---
layout: default
---

# Static Methods in Interfaces

<div class="grid grid-cols-2 gap-6">

<div>

## Static Method Declaration
```java
public interface MathOperations {
    // Abstract methods
    double calculate(double a, double b);
    
    // Default method
    default void showResult(double result) {
        System.out.println("Result: " + result);
    }
    
    // Static methods
    static double add(double a, double b) {
        return a + b;
    }
    
    static double multiply(double a, double b) {
        return a * b;
    }
    
    static boolean isPositive(double value) {
        return value > 0;
    }
    
    static void showHelp() {
        System.out.println("Available operations:");
        System.out.println("- Addition");
        System.out.println("- Multiplication");
        System.out.println("- Validation");
    }
}
```

## Implementation and Usage
```java
public class Calculator implements MathOperations {
    @Override
    public double calculate(double a, double b) {
        // Using static method from interface
        if (MathOperations.isPositive(a) && 
            MathOperations.isPositive(b)) {
            return MathOperations.multiply(a, b);
        } else {
            return MathOperations.add(a, b);
        }
    }
}

public class MathDemo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        // Using implemented method
        double result = calc.calculate(5.0, 3.0);
        calc.showResult(result);  // Default method
        
        // Using static methods directly
        double sum = MathOperations.add(10, 20);
        double product = MathOperations.multiply(4, 5);
        
        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
        
        MathOperations.showHelp();  // Static method
    }
}
```

</div>

<div>

## Static Method Characteristics

### Key Properties
- Belong to the interface, not implementing classes
- Called using interface name (InterfaceName.methodName)
- Cannot be overridden in implementing classes
- Provide utility functionality related to the interface

### Utility Interface Example
```java
public interface StringUtils {
    // Static utility methods
    static boolean isEmpty(String str) {
        return str == null || str.trim().isEmpty();
    }
    
    static String capitalize(String str) {
        if (isEmpty(str)) return str;
        return str.substring(0, 1).toUpperCase() + 
               str.substring(1).toLowerCase();
    }
    
    static String reverse(String str) {
        if (isEmpty(str)) return str;
        return new StringBuilder(str).reverse().toString();
    }
    
    static int countWords(String str) {
        if (isEmpty(str)) return 0;
        return str.trim().split("\\s+").length;
    }
}
```

### Usage
```java
public class StringDemo {
    public static void main(String[] args) {
        String text = "hello world";
        
        System.out.println("Original: " + text);
        System.out.println("Capitalized: " + 
                          StringUtils.capitalize(text));
        System.out.println("Reversed: " + 
                          StringUtils.reverse(text));
        System.out.println("Word count: " + 
                          StringUtils.countWords(text));
        System.out.println("Is empty: " + 
                          StringUtils.isEmpty(text));
    }
}
```

</div>

</div>

---
layout: default
---

# Multiple Interface Implementation

<div class="grid grid-cols-2 gap-6">

<div>

## Multiple Interfaces
```java
public interface Flyable {
    void fly();
    
    default void takeOff() {
        System.out.println("Taking off...");
    }
}

public interface Swimmable {
    void swim();
    
    default void dive() {
        System.out.println("Diving...");
    }
}

public interface Walkable {
    void walk();
    
    default void run() {
        System.out.println("Running...");
    }
}
```

## Implementing Multiple Interfaces
```java
public class Duck implements Flyable, Swimmable, Walkable {
    private String name;
    
    public Duck(String name) {
        this.name = name;
    }
    
    @Override
    public void fly() {
        System.out.println(name + " is flying in the sky");
    }
    
    @Override
    public void swim() {
        System.out.println(name + " is swimming in the pond");
    }
    
    @Override
    public void walk() {
        System.out.println(name + " is walking on land");
    }
    
    // Can use all default methods
    public void performAllActivities() {
        takeOff();  // From Flyable
        fly();
        dive();     // From Swimmable
        swim();
        walk();
        run();      // From Walkable
    }
}
```

</div>

<div>

## Diamond Problem Resolution
```java
public interface A {
    default void method() {
        System.out.println("A's method");
    }
}

public interface B {
    default void method() {
        System.out.println("B's method");
    }
}

// Compilation error without explicit resolution
public class Diamond implements A, B {
    @Override
    public void method() {
        // Must explicitly choose or provide new implementation
        A.super.method();  // Call A's default method
        // or B.super.method();  // Call B's default method
        // or provide completely new implementation
        System.out.println("Diamond's custom method");
    }
}
```

## Using Multiple Interfaces
```java
public class AnimalDemo {
    public static void main(String[] args) {
        Duck duck = new Duck("Donald");
        
        // Duck can be referenced by any of its interfaces
        Flyable flyingDuck = duck;
        Swimmable swimmingDuck = duck;
        Walkable walkingDuck = duck;
        
        flyingDuck.fly();
        swimmingDuck.swim();
        walkingDuck.walk();
        
        // Or use as Duck directly
        duck.performAllActivities();
    }
}
```

## Interface Inheritance
```java
public interface Animal {
    void makeSound();
}

public interface Pet extends Animal {
    void play();
    String getName();
}

public class Dog implements Pet {
    private String name;
    
    public Dog(String name) { this.name = name; }
    
    @Override
    public void makeSound() {
        System.out.println(name + " says Woof!");
    }
    
    @Override
    public void play() {
        System.out.println(name + " is playing fetch");
    }
    
    @Override
    public String getName() { return name; }
}
```

</div>

</div>

---
layout: default
---

# Functional Interfaces

<div class="grid grid-cols-2 gap-6">

<div>

## Functional Interface Definition
- Interface with exactly **one abstract method**
- Can have default and static methods
- Annotated with `@FunctionalInterface` (optional but recommended)
- Can be used with lambda expressions

## Basic Functional Interface
```java
@FunctionalInterface
public interface Calculator {
    // Single abstract method (SAM)
    double calculate(double a, double b);
    
    // Default methods allowed
    default void showResult(double result) {
        System.out.println("Result: " + result);
    }
    
    // Static methods allowed
    static void showInfo() {
        System.out.println("Calculator interface");
    }
}
```

## Using with Lambda Expressions
```java
public class LambdaDemo {
    public static void main(String[] args) {
        // Lambda expressions
        Calculator add = (a, b) -> a + b;
        Calculator multiply = (a, b) -> a * b;
        Calculator subtract = (a, b) -> a - b;
        
        // Using functional interfaces
        System.out.println("Addition: " + add.calculate(10, 5));
        System.out.println("Multiplication: " + multiply.calculate(10, 5));
        System.out.println("Subtraction: " + subtract.calculate(10, 5));
        
        // Using default method
        add.showResult(add.calculate(15, 25));
    }
}
```

</div>

<div>

## Built-in Functional Interfaces
```java
import java.util.function.*;
import java.util.Arrays;
import java.util.List;

public class BuiltInFunctionalInterfaces {
    public static void main(String[] args) {
        // Predicate<T> - boolean test(T t)
        Predicate<Integer> isEven = num -> num % 2 == 0;
        System.out.println("Is 10 even? " + isEven.test(10));
        
        // Function<T, R> - R apply(T t)
        Function<String, Integer> stringLength = str -> str.length();
        System.out.println("Length of 'Hello': " + 
                          stringLength.apply("Hello"));
        
        // Consumer<T> - void accept(T t)
        Consumer<String> printer = str -> System.out.println(str.toUpperCase());
        printer.accept("hello world");
        
        // Supplier<T> - T get()
        Supplier<Double> randomValue = () -> Math.random();
        System.out.println("Random value: " + randomValue.get());
        
        // Using with collections
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
        
        // Filter with Predicate
        numbers.stream()
               .filter(isEven)
               .forEach(System.out::println);
        
        // Transform with Function
        numbers.stream()
               .map(num -> num * num)
               .forEach(System.out::println);
    }
}
```

## Custom Functional Interfaces
```java
@FunctionalInterface
public interface StringProcessor {
    String process(String input);
}

@FunctionalInterface
public interface NumberValidator {
    boolean isValid(int number);
}

public class CustomFunctionalDemo {
    public static void main(String[] args) {
        StringProcessor upperCase = str -> str.toUpperCase();
        StringProcessor reverse = str -> new StringBuilder(str).reverse().toString();
        
        NumberValidator positive = num -> num > 0;
        NumberValidator even = num -> num % 2 == 0;
        
        String text = "hello";
        System.out.println(upperCase.process(text));
        System.out.println(reverse.process(text));
        
        int number = 10;
        System.out.println("Is positive: " + positive.isValid(number));
        System.out.println("Is even: " + even.isValid(number));
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Example: Media Player System

<div class="grid grid-cols-2 gap-6">

<div>

## Interface Hierarchy
```java
// Base media interface
public interface Media {
    void load();
    void play();
    void stop();
    
    // Default methods
    default void displayInfo() {
        System.out.println("Media Type: " + getType());
        System.out.println("Duration: " + getDuration() + " seconds");
    }
    
    default String getType() {
        return "Generic Media";
    }
    
    default int getDuration() {
        return 0;
    }
    
    // Static utility
    static boolean isValidFormat(String format) {
        return format != null && 
               (format.endsWith(".mp3") || 
                format.endsWith(".mp4") || 
                format.endsWith(".wav"));
    }
}

// Audio-specific interface
public interface AudioMedia extends Media {
    void setVolume(int volume);
    int getVolume();
    
    @Override
    default String getType() {
        return "Audio";
    }
}

// Video-specific interface
public interface VideoMedia extends Media {
    void setResolution(String resolution);
    String getResolution();
    void enableSubtitles(boolean enable);
    
    @Override
    default String getType() {
        return "Video";
    }
}
```

</div>

<div>

## Implementation Classes
```java
// Audio implementation
public class MP3Player implements AudioMedia {
    private String filename;
    private int volume = 50;
    private int duration;
    private boolean isPlaying = false;
    
    public MP3Player(String filename, int duration) {
        this.filename = filename;
        this.duration = duration;
    }
    
    @Override
    public void load() {
        if (Media.isValidFormat(filename)) {
            System.out.println("Loading MP3: " + filename);
        } else {
            throw new IllegalArgumentException("Invalid format");
        }
    }
    
    @Override
    public void play() {
        if (!isPlaying) {
            isPlaying = true;
            System.out.println("Playing " + filename + 
                             " at volume " + volume);
        }
    }
    
    @Override
    public void stop() {
        if (isPlaying) {
            isPlaying = false;
            System.out.println("Stopped " + filename);
        }
    }
    
    @Override
    public void setVolume(int volume) {
        this.volume = Math.max(0, Math.min(100, volume));
    }
    
    @Override
    public int getVolume() { return volume; }
    
    @Override
    public int getDuration() { return duration; }
}

// Video implementation
public class MP4Player implements VideoMedia {
    private String filename;
    private String resolution = "1080p";
    private boolean subtitlesEnabled = false;
    private int duration;
    
    public MP4Player(String filename, int duration) {
        this.filename = filename;
        this.duration = duration;
    }
    
    @Override
    public void load() {
        System.out.println("Loading MP4: " + filename);
    }
    
    @Override
    public void play() {
        System.out.println("Playing " + filename + 
                         " in " + resolution +
                         (subtitlesEnabled ? " with subtitles" : ""));
    }
    
    @Override
    public void stop() {
        System.out.println("Stopped " + filename);
    }
    
    @Override
    public void setResolution(String resolution) {
        this.resolution = resolution;
    }
    
    @Override
    public String getResolution() { return resolution; }
    
    @Override
    public void enableSubtitles(boolean enable) {
        this.subtitlesEnabled = enable;
    }
    
    @Override
    public int getDuration() { return duration; }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: E-commerce Payment System

<div class="grid grid-cols-2 gap-6">

<div>

## Task
Design a payment processing system using interfaces:

## Payment Interfaces
```java
// Base payment interface
public interface PaymentProcessor {
    boolean processPayment(double amount);
    String getTransactionId();
    
    default void generateReceipt(double amount) {
        System.out.println("=== RECEIPT ===");
        System.out.println("Amount: $" + amount);
        System.out.println("Transaction ID: " + getTransactionId());
        System.out.println("Payment Method: " + getPaymentMethod());
        System.out.println("Status: " + 
                         (processPayment(amount) ? "SUCCESS" : "FAILED"));
    }
    
    default String getPaymentMethod() {
        return "Generic Payment";
    }
    
    static boolean isValidAmount(double amount) {
        return amount > 0 && amount <= 10000;
    }
}

// Refundable payment interface
public interface Refundable {
    boolean refund(String transactionId, double amount);
    
    default void processRefund(String transactionId, double amount) {
        if (refund(transactionId, amount)) {
            System.out.println("Refund processed: $" + amount);
        } else {
            System.out.println("Refund failed");
        }
    }
}

// Recurring payment interface
public interface RecurringPayment {
    void setupRecurring(int days);
    void cancelRecurring();
    boolean isRecurringActive();
    
    default void displayRecurringInfo() {
        System.out.println("Recurring payment: " + 
                         (isRecurringActive() ? "Active" : "Inactive"));
    }
}
```

</div>

<div>

## Payment Implementation
```java
// Credit Card payment
public class CreditCardProcessor 
    implements PaymentProcessor, Refundable, RecurringPayment {
    
    private String cardNumber;
    private String transactionId;
    private boolean recurringActive = false;
    
    public CreditCardProcessor(String cardNumber) {
        this.cardNumber = cardNumber;
        this.transactionId = "CC" + System.currentTimeMillis();
    }
    
    @Override
    public boolean processPayment(double amount) {
        if (PaymentProcessor.isValidAmount(amount)) {
            System.out.println("Processing credit card payment: $" + amount);
            // Simulate payment processing
            return true;
        }
        return false;
    }
    
    @Override
    public String getTransactionId() { return transactionId; }
    
    @Override
    public String getPaymentMethod() { return "Credit Card"; }
    
    @Override
    public boolean refund(String transactionId, double amount) {
        if (this.transactionId.equals(transactionId)) {
            System.out.println("Credit card refund: $" + amount);
            return true;
        }
        return false;
    }
    
    @Override
    public void setupRecurring(int days) {
        this.recurringActive = true;
        System.out.println("Recurring payment setup every " + days + " days");
    }
    
    @Override
    public void cancelRecurring() {
        this.recurringActive = false;
        System.out.println("Recurring payment cancelled");
    }
    
    @Override
    public boolean isRecurringActive() { return recurringActive; }
}

// PayPal payment
public class PayPalProcessor implements PaymentProcessor, Refundable {
    private String email;
    private String transactionId;
    
    public PayPalProcessor(String email) {
        this.email = email;
        this.transactionId = "PP" + System.currentTimeMillis();
    }
    
    @Override
    public boolean processPayment(double amount) {
        if (PaymentProcessor.isValidAmount(amount)) {
            System.out.println("Processing PayPal payment: $" + amount);
            return true;
        }
        return false;
    }
    
    @Override
    public String getTransactionId() { return transactionId; }
    
    @Override
    public String getPaymentMethod() { return "PayPal"; }
    
    @Override
    public boolean refund(String transactionId, double amount) {
        if (this.transactionId.equals(transactionId)) {
            System.out.println("PayPal refund: $" + amount);
            return true;
        }
        return false;
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Shape Drawing System

<div class="grid grid-cols-2 gap-6">

<div>

## Drawing System Interfaces
```java
// Base drawable interface
@FunctionalInterface
public interface Drawable {
    void draw();
    
    static void drawBorder() {
        System.out.println("==================");
    }
}

// Shape interface extending drawable
public interface Shape extends Drawable {
    double calculateArea();
    double calculatePerimeter();
    
    default void displayDetails() {
        Drawable.drawBorder();
        System.out.println("Shape: " + getShapeType());
        System.out.println("Area: " + calculateArea());
        System.out.println("Perimeter: " + calculatePerimeter());
        draw();
        Drawable.drawBorder();
    }
    
    default String getShapeType() {
        return "Generic Shape";
    }
}

// Colorable interface
public interface Colorable {
    void setColor(String color);
    String getColor();
    
    default void displayColor() {
        System.out.println("Color: " + getColor());
    }
}

// Resizable interface
public interface Resizable {
    void resize(double factor);
    
    default void doubleSize() {
        resize(2.0);
    }
    
    default void halveSize() {
        resize(0.5);
    }
}
```

</div>

<div>

## Shape Implementations
```java
// Circle implementation
public class Circle implements Shape, Colorable, Resizable {
    private double radius;
    private String color = "BLACK";
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius: " + radius);
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
    
    @Override
    public String getShapeType() { return "Circle"; }
    
    @Override
    public void setColor(String color) { this.color = color; }
    
    @Override
    public String getColor() { return color; }
    
    @Override
    public void resize(double factor) {
        if (factor > 0) {
            radius *= factor;
            System.out.println("Circle resized by factor: " + factor);
        }
    }
}

// Rectangle implementation
public class Rectangle implements Shape, Colorable, Resizable {
    private double length, width;
    private String color = "BLACK";
    
    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing rectangle: " + length + " x " + width);
    }
    
    @Override
    public double calculateArea() {
        return length * width;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * (length + width);
    }
    
    @Override
    public String getShapeType() { return "Rectangle"; }
    
    @Override
    public void setColor(String color) { this.color = color; }
    
    @Override
    public String getColor() { return color; }
    
    @Override
    public void resize(double factor) {
        if (factor > 0) {
            length *= factor;
            width *= factor;
            System.out.println("Rectangle resized by factor: " + factor);
        }
    }
}
```

## Usage Example
```java
public class ShapeDemo {
    public static void main(String[] args) {
        Shape circle = new Circle(5.0);
        Shape rectangle = new Rectangle(4.0, 6.0);
        
        // Use as Shape
        circle.displayDetails();
        rectangle.displayDetails();
        
        // Use as Colorable
        ((Colorable) circle).setColor("RED");
        ((Colorable) rectangle).setColor("BLUE");
        
        // Use as Resizable
        ((Resizable) circle).doubleSize();
        ((Resizable) rectangle).halveSize();
        
        circle.displayDetails();
    }
}
```

</div>

</div>

---
layout: default
---

# Interface Design Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Strategy Pattern
```java
// Strategy interface
@FunctionalInterface
public interface SortingStrategy {
    void sort(int[] array);
}

// Context class
public class Sorter {
    private SortingStrategy strategy;
    
    public Sorter(SortingStrategy strategy) {
        this.strategy = strategy;
    }
    
    public void setStrategy(SortingStrategy strategy) {
        this.strategy = strategy;
    }
    
    public void performSort(int[] array) {
        strategy.sort(array);
    }
}

// Usage with lambdas
public class StrategyDemo {
    public static void main(String[] args) {
        int[] data = {5, 2, 8, 1, 9};
        
        Sorter sorter = new Sorter(Arrays::sort); // Method reference
        
        // Bubble sort strategy
        sorter.setStrategy(array -> {
            for (int i = 0; i < array.length - 1; i++) {
                for (int j = 0; j < array.length - i - 1; j++) {
                    if (array[j] > array[j + 1]) {
                        int temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                    }
                }
            }
        });
        
        sorter.performSort(data);
        System.out.println(Arrays.toString(data));
    }
}
```

</div>

<div>

## Observer Pattern
```java
// Observer interface
@FunctionalInterface
public interface Observer {
    void update(String message);
}

// Subject interface
public interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers(String message);
}

// Concrete subject
public class NewsAgency implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String news;
    
    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }
    
    @Override
    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
    
    public void setNews(String news) {
        this.news = news;
        notifyObservers("Breaking News: " + news);
    }
}

// Usage
public class ObserverDemo {
    public static void main(String[] args) {
        NewsAgency agency = new NewsAgency();
        
        // Lambda observers
        Observer tvChannel = msg -> System.out.println("TV: " + msg);
        Observer newspaper = msg -> System.out.println("Print: " + msg);
        Observer website = msg -> System.out.println("Web: " + msg);
        
        agency.attach(tvChannel);
        agency.attach(newspaper);
        agency.attach(website);
        
        agency.setNews("New technology breakthrough!");
    }
}
```

## Factory Pattern
```java
// Product interface
public interface Animal {
    void makeSound();
    String getType();
}

// Factory interface
@FunctionalInterface
public interface AnimalFactory {
    Animal createAnimal(String name);
}

// Usage
public class FactoryDemo {
    public static void main(String[] args) {
        Map<String, AnimalFactory> factories = Map.of(
            "dog", name -> new Dog(name),
            "cat", name -> new Cat(name),
            "bird", name -> new Bird(name)
        );
        
        Animal dog = factories.get("dog").createAnimal("Buddy");
        dog.makeSound();
    }
}
```

</div>

</div>

---
layout: default
---

# Interface Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Design Principles

### 1. Interface Segregation Principle
```java
// BAD: Fat interface
public interface Worker {
    void work();
    void eat();
    void sleep();
    void program();
    void managePeople();
}

// GOOD: Segregated interfaces
public interface Workable {
    void work();
}

public interface Eatable {
    void eat();
}

public interface Sleepable {
    void sleep();
}

public interface Programmable {
    void program();
}

public interface Manageable {
    void managePeople();
}

// Classes implement only what they need
public class Programmer implements Workable, Programmable, Eatable {
    @Override
    public void work() { /* implementation */ }
    
    @Override
    public void program() { /* implementation */ }
    
    @Override
    public void eat() { /* implementation */ }
}
```

### 2. Dependency Inversion Principle
```java
// BAD: Depend on concrete class
public class EmailService {
    private SMTPMailer mailer; // Concrete dependency
    
    public void sendEmail(String message) {
        mailer.send(message);
    }
}

// GOOD: Depend on abstraction
public interface MailSender {
    void send(String message);
}

public class EmailService {
    private MailSender mailer; // Interface dependency
    
    public EmailService(MailSender mailer) {
        this.mailer = mailer;
    }
    
    public void sendEmail(String message) {
        mailer.send(message);
    }
}
```

</div>

<div>

## Naming Conventions

### Interface Naming
```java
// Good naming patterns
public interface Readable { }          // -able suffix
public interface Comparable<T> { }     // -able suffix
public interface Runnable { }          // -able suffix

public interface PaymentProcessor { }   // Function-based naming
public interface DataValidator { }      // Function-based naming
public interface MessageHandler { }     // Function-based naming

// Avoid 'I' prefix (C# convention, not Java)
// BAD: IPaymentProcessor
// GOOD: PaymentProcessor
```

### Documentation Best Practices
```java
/**
 * Represents a data source that can be queried and updated.
 * 
 * <p>Implementations should ensure thread safety if the data source
 * will be accessed from multiple threads concurrently.</p>
 * 
 * @param <T> the type of data stored in this source
 * @since 1.0
 */
public interface DataSource<T> {
    /**
     * Retrieves data by the specified key.
     * 
     * @param key the unique identifier for the data
     * @return the data associated with the key, or null if not found
     * @throws IllegalArgumentException if key is null
     */
    T getData(String key);
    
    /**
     * Stores data with the specified key.
     * 
     * @param key the unique identifier for the data
     * @param data the data to store
     * @throws IllegalArgumentException if key or data is null
     */
    void setData(String key, T data);
    
    /**
     * Checks if data exists for the specified key.
     * 
     * @param key the key to check
     * @return true if data exists, false otherwise
     */
    default boolean hasData(String key) {
        return getData(key) != null;
    }
}
```

### Performance Considerations
```java
public interface CacheManager<K, V> {
    V get(K key);
    void put(K key, V value);
    
    // Default method with efficient implementation
    default void putAll(Map<K, V> data) {
        // Bulk operation for better performance
        data.forEach(this::put);
    }
    
    // Method to get statistics
    default CacheStats getStats() {
        return CacheStats.empty(); // Default implementation
    }
}
```

</div>

</div>

---
layout: default
---

# Common Interface Pitfalls

<div class="grid grid-cols-2 gap-6">

<div>

## Pitfall 1: Overusing Interfaces
```java
// BAD: Unnecessary interface for simple value object
public interface PersonData {
    String getName();
    int getAge();
    void setName(String name);
    void setAge(int age);
}

// GOOD: Simple class for data
public class Person {
    private String name;
    private int age;
    
    // constructors, getters, setters
}
```

## Pitfall 2: Fat Interfaces
```java
// BAD: Interface doing too many things
public interface DatabaseManager {
    void connect();
    void disconnect();
    void createTable(String name);
    void dropTable(String name);
    List<String> executeQuery(String sql);
    void executeUpdate(String sql);
    void backup();
    void restore();
    void optimize();
}

// GOOD: Separated concerns
public interface ConnectionManager {
    void connect();
    void disconnect();
}

public interface QueryExecutor {
    List<String> executeQuery(String sql);
    void executeUpdate(String sql);
}

public interface DatabaseMaintenance {
    void backup();
    void restore();
    void optimize();
}
```

</div>

<div>

## Pitfall 3: Exposing Implementation Details
```java
// BAD: Interface exposing internal structures
public interface UserManager {
    HashMap<String, User> getUserMap(); // Exposes internal structure
    ArrayList<User> getUserList();      // Exposes internal structure
}

// GOOD: Abstract interface
public interface UserManager {
    User getUser(String id);
    Collection<User> getAllUsers();      // Abstract collection
    boolean addUser(User user);
    boolean removeUser(String id);
}
```

## Pitfall 4: Marker Interfaces Abuse
```java
// BAD: Using marker interfaces for configuration
public interface FastProcessing { } // Empty marker
public interface SlowProcessing { } // Empty marker

// GOOD: Use enums or configuration
public enum ProcessingSpeed {
    FAST, NORMAL, SLOW
}

public interface DataProcessor {
    void process(Data data, ProcessingSpeed speed);
}
```

## Pitfall 5: Ignoring Default Method Conflicts
```java
// Problematic: Same default method signature
public interface A {
    default String getValue() { return "A"; }
}

public interface B {
    default String getValue() { return "B"; }
}

// GOOD: Explicit resolution
public class Implementation implements A, B {
    @Override
    public String getValue() {
        return A.super.getValue() + " and " + B.super.getValue();
    }
}
```

</div>

</div>

---
layout: default
---

# Advanced Interface Concepts

<div class="grid grid-cols-2 gap-6">

<div>

## Generic Interfaces
```java
// Generic interface with type parameters
public interface Repository<T, ID> {
    void save(T entity);
    T findById(ID id);
    List<T> findAll();
    void deleteById(ID id);
    boolean existsById(ID id);
    
    // Default method with generics
    default void saveAll(Collection<T> entities) {
        entities.forEach(this::save);
    }
}

// Specific implementation
public class UserRepository implements Repository<User, Long> {
    private Map<Long, User> users = new HashMap<>();
    
    @Override
    public void save(User user) {
        users.put(user.getId(), user);
    }
    
    @Override
    public User findById(Long id) {
        return users.get(id);
    }
    
    @Override
    public List<User> findAll() {
        return new ArrayList<>(users.values());
    }
    
    @Override
    public void deleteById(Long id) {
        users.remove(id);
    }
    
    @Override
    public boolean existsById(Long id) {
        return users.containsKey(id);
    }
}
```

</div>

<div>

## Bounded Generic Interfaces
```java
// Bounded type parameters
public interface Comparable<T> {
    int compareTo(T other);
}

public interface NumberProcessor<T extends Number> {
    T process(T input);
    
    default double toDouble(T value) {
        return value.doubleValue();
    }
    
    default boolean isPositive(T value) {
        return toDouble(value) > 0;
    }
}

// Implementation with bounded types
public class IntegerProcessor implements NumberProcessor<Integer> {
    @Override
    public Integer process(Integer input) {
        return input * 2;
    }
}

// Wildcard usage
public class ProcessorUtil {
    public static void processNumbers(
        List<? extends Number> numbers,
        NumberProcessor<? super Number> processor) {
        
        for (Number num : numbers) {
            Number result = processor.process(num);
            System.out.println("Processed: " + result);
        }
    }
}
```

## Nested Interfaces
```java
public interface OuterInterface {
    void outerMethod();
    
    // Nested interface
    interface NestedInterface {
        void nestedMethod();
        
        // Static nested interface
        static interface StaticNested {
            void staticNestedMethod();
        }
    }
    
    // Default method using nested interface
    default void processWithNested(NestedInterface nested) {
        nested.nestedMethod();
    }
}

// Implementation
public class Implementation implements OuterInterface, 
                                      OuterInterface.NestedInterface {
    @Override
    public void outerMethod() {
        System.out.println("Outer method");
    }
    
    @Override
    public void nestedMethod() {
        System.out.println("Nested method");
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

- 🎯 **Interface Fundamentals**: Contract definition and implementation
- 📋 **Method Types**: Abstract, default, static, and private methods
- 🔧 **Multiple Inheritance**: Implementing multiple interfaces safely
- 🚀 **Functional Interfaces**: Single abstract method and lambda support
- ⚡ **Design Patterns**: Strategy, Observer, Factory using interfaces
- 📝 **Best Practices**: Interface segregation and dependency inversion
- 🏗️ **Advanced Concepts**: Generics, bounded types, nested interfaces

</v-clicks>

</div>

<div>

## Interface Evolution in Java

### Java 8+
- Default methods
- Static methods
- Functional interfaces
- Lambda expressions

### Java 9+
- Private methods in interfaces
- Private static methods

### Best Practices Recap

<v-clicks>

- Keep interfaces focused and cohesive
- Use meaningful and consistent naming
- Prefer composition over inheritance
- Document interface contracts clearly
- Use default methods for backward compatibility
- Avoid exposing implementation details
- Consider generic interfaces for reusability
- Test interface implementations thoroughly

</v-clicks>

## Next Lecture Preview
**Lecture 24: Interface Implementation**
- Multiple interface implementation
- Interface relationships and hierarchies
- Resolving method conflicts
- Advanced implementation patterns

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!

## Questions and Discussion

**Next Lecture**: Interface Implementation  
**Topic**: Multiple inheritance, interface relationships, advanced patterns

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Practice interface design and implementation! <carbon:arrow-right class="inline"/>
  </span>
</div>