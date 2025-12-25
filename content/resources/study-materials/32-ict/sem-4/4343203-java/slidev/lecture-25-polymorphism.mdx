---
theme: default
background: https://source.unsplash.com/1024x768/?transformation,shape
title: Polymorphism
info: |
  ## Java Programming (4343203)
  
  Lecture 25: Polymorphism
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about polymorphism in Java, runtime polymorphism, method dispatch, polymorphic behavior, and advanced polymorphism patterns in object-oriented programming.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Polymorphism
## Lecture 25

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

- 🎭 **Understand** the concept of polymorphism and its types in Java
- 🔄 **Implement** runtime polymorphism using inheritance and interfaces
- ⚡ **Explain** method dispatch and dynamic binding mechanisms
- 🎯 **Apply** polymorphic behavior in real-world applications
- 📝 **Design** flexible systems using polymorphic patterns
- 🏗️ **Practice** advanced polymorphism techniques and best practices
- 🛠️ **Create** maintainable code using polymorphic principles

</v-clicks>

---
layout: default
---

# What is Polymorphism?

<div class="grid grid-cols-2 gap-6">

<div>

## Definition
**Polymorphism** (Greek: "many forms") is the ability of objects of different types to be treated as objects of a common base type, while still maintaining their own specific behavior.

## Types of Polymorphism in Java

### 1. Compile-time Polymorphism (Static)
- **Method Overloading**: Same method name, different parameters
- **Operator Overloading**: Not supported in Java (except + for strings)

### 2. Runtime Polymorphism (Dynamic)
- **Method Overriding**: Subclass provides specific implementation
- **Interface Implementation**: Different classes implement same interface

</div>

<div>

## Benefits of Polymorphism

<v-clicks>

- 🔄 **Code Reusability**: Write once, use with many types
- 🎯 **Flexibility**: Easy to extend with new implementations
- 🏗️ **Maintainability**: Changes localized to specific classes
- 📦 **Abstraction**: Hide implementation details behind common interface
- 🔧 **Extensibility**: Add new types without modifying existing code

</v-clicks>

## Real-world Analogy
```java
// Like a remote control that works with different devices
RemoteControl remote = new UniversalRemote();

// Can control different devices polymorphically
Device tv = new Television();
Device sound = new SoundSystem();
Device lights = new SmartLights();

remote.turnOn(tv);      // TV-specific behavior
remote.turnOn(sound);   // Sound-specific behavior
remote.turnOn(lights);  // Light-specific behavior
```

Each device responds differently to the same `turnOn()` command!

</div>

</div>

---
layout: default
---

# Method Overloading (Compile-time Polymorphism)

<div class="grid grid-cols-2 gap-6">

<div>

## Method Overloading Rules
- Same method name, different parameter lists
- Different number of parameters
- Different parameter types
- Different parameter order
- Return type alone cannot differentiate methods

## Basic Overloading Example
```java
public class Calculator {
    // Different number of parameters
    public int add(int a, int b) {
        System.out.println("Adding two integers: " + a + " + " + b);
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        System.out.println("Adding three integers");
        return a + b + c;
    }
    
    // Different parameter types
    public double add(double a, double b) {
        System.out.println("Adding two doubles: " + a + " + " + b);
        return a + b;
    }
    
    public String add(String a, String b) {
        System.out.println("Concatenating strings");
        return a + b;
    }
    
    // Variable arguments (varargs)
    public int add(int... numbers) {
        System.out.println("Adding variable number of integers");
        int sum = 0;
        for (int num : numbers) {
            sum += num;
        }
        return sum;
    }
}
```

</div>

<div>

## Advanced Overloading Examples
```java
public class DataProcessor {
    // Different parameter order
    public void process(String data, int priority) {
        System.out.println("Processing string with priority: " + priority);
    }
    
    public void process(int priority, String data) {
        System.out.println("Processing with priority " + priority + ": " + data);
    }
    
    // Array vs varargs
    public void process(int[] numbers) {
        System.out.println("Processing array of " + numbers.length + " numbers");
    }
    
    public void process(int... numbers) {
        System.out.println("Processing varargs of " + numbers.length + " numbers");
    }
    
    // Generic overloading
    public <T> void process(T item) {
        System.out.println("Processing generic item: " + item);
    }
    
    public <T> void process(List<T> items) {
        System.out.println("Processing list of " + items.size() + " items");
    }
}

// Usage demonstration
public class OverloadingDemo {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        
        System.out.println(calc.add(5, 3));           // int, int
        System.out.println(calc.add(5, 3, 2));        // int, int, int
        System.out.println(calc.add(5.5, 3.2));       // double, double
        System.out.println(calc.add("Hello", "World")); // String, String
        System.out.println(calc.add(1, 2, 3, 4, 5));  // varargs
        
        DataProcessor processor = new DataProcessor();
        processor.process("data", 1);           // String, int
        processor.process(2, "more data");      // int, String
        processor.process(new int[]{1, 2, 3});  // array
        processor.process(4, 5, 6);            // varargs
    }
}
```

</div>

</div>

---
layout: default
---

# Method Overriding (Runtime Polymorphism)

<div class="grid grid-cols-2 gap-6">

<div>

## Method Overriding Rules
- Must have same method signature (name, parameters, return type)
- Cannot reduce visibility (can increase)
- Cannot throw broader checked exceptions
- Use `@Override` annotation for clarity and safety

## Basic Overriding Example
```java
// Base class
public abstract class Animal {
    protected String name;
    protected String species;
    
    public Animal(String name, String species) {
        this.name = name;
        this.species = species;
    }
    
    // Method to be overridden
    public abstract void makeSound();
    
    // Method with default implementation
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
    
    // Method that uses polymorphic behavior
    public void performDailyRoutine() {
        System.out.println(name + " starts daily routine:");
        makeSound();  // Polymorphic call
        sleep();
    }
    
    public String getName() { return name; }
    public String getSpecies() { return species; }
}

// Derived classes
public class Dog extends Animal {
    private String breed;
    
    public Dog(String name, String breed) {
        super(name, "Canine");
        this.breed = breed;
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + " (a " + breed + ") says: Woof! Woof!");
    }
    
    @Override
    public void sleep() {
        System.out.println(name + " curls up in a cozy spot and sleeps");
    }
    
    // Additional dog-specific method
    public void wagTail() {
        System.out.println(name + " is wagging tail happily!");
    }
}
```

</div>

<div>

## More Override Examples
```java
public class Cat extends Animal {
    private boolean isIndoor;
    
    public Cat(String name, boolean isIndoor) {
        super(name, "Feline");
        this.isIndoor = isIndoor;
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + " says: Meow! Purr...");
    }
    
    @Override
    public void sleep() {
        if (isIndoor) {
            System.out.println(name + " finds a sunny windowsill to nap");
        } else {
            System.out.println(name + " climbs a tree to sleep safely");
        }
    }
    
    public void hunt() {
        System.out.println(name + " is stalking prey silently");
    }
}

public class Bird extends Animal {
    private boolean canFly;
    
    public Bird(String name, boolean canFly) {
        super(name, "Avian");
        this.canFly = canFly;
    }
    
    @Override
    public void makeSound() {
        System.out.println(name + " chirps melodiously: Tweet! Tweet!");
    }
    
    @Override
    public void sleep() {
        if (canFly) {
            System.out.println(name + " perches on a high branch to sleep");
        } else {
            System.out.println(name + " nestles on the ground to sleep");
        }
    }
    
    public void fly() {
        if (canFly) {
            System.out.println(name + " soars through the sky gracefully");
        } else {
            System.out.println(name + " cannot fly but runs quickly");
        }
    }
}
```

## Polymorphic Usage
```java
public class AnimalShelter {
    public static void main(String[] args) {
        // Polymorphic array - different objects, same reference type
        Animal[] animals = {
            new Dog("Buddy", "Golden Retriever"),
            new Cat("Whiskers", true),
            new Bird("Tweety", true),
            new Dog("Max", "German Shepherd"),
            new Cat("Shadow", false)
        };
        
        System.out.println("=== Animal Shelter Daily Routine ===");
        for (Animal animal : animals) {
            animal.performDailyRoutine(); // Polymorphic method call
            System.out.println();
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Dynamic Method Dispatch

<div class="grid grid-cols-2 gap-6">

<div>

## How Dynamic Dispatch Works

### At Runtime:
1. **Object Type Determination**: JVM determines actual object type
2. **Method Lookup**: Searches for method in actual class
3. **Method Invocation**: Calls the overridden method
4. **Late Binding**: Method binding happens at runtime

## Method Dispatch Example
```java
public class Shape {
    protected String color = "white";
    
    public void draw() {
        System.out.println("Drawing a generic shape in " + color);
    }
    
    public void calculateArea() {
        System.out.println("Area calculation not implemented");
    }
    
    public String getInfo() {
        return "Generic shape in " + color;
    }
}

public class Circle extends Shape {
    private double radius;
    
    public Circle(double radius, String color) {
        this.radius = radius;
        this.color = color;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius " + radius + 
                         " in " + color);
    }
    
    @Override
    public void calculateArea() {
        double area = Math.PI * radius * radius;
        System.out.println("Circle area: " + area);
    }
    
    @Override
    public String getInfo() {
        return "Circle with radius " + radius + " in " + color;
    }
}
```

</div>

<div>

## Runtime Behavior Analysis
```java
public class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double width, double height, String color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a rectangle " + width + "x" + height + 
                         " in " + color);
    }
    
    @Override
    public void calculateArea() {
        double area = width * height;
        System.out.println("Rectangle area: " + area);
    }
    
    @Override
    public String getInfo() {
        return "Rectangle " + width + "x" + height + " in " + color;
    }
}

// Demonstration of dynamic dispatch
public class DispatchDemo {
    public static void main(String[] args) {
        // Reference type is Shape, object types are different
        Shape shape1 = new Circle(5.0, "red");
        Shape shape2 = new Rectangle(4.0, 6.0, "blue");
        Shape shape3 = new Shape(); // Base class object
        
        // Array of Shape references
        Shape[] shapes = {shape1, shape2, shape3};
        
        System.out.println("=== Dynamic Method Dispatch ===");
        for (int i = 0; i < shapes.length; i++) {
            System.out.println("\nShape " + (i + 1) + ":");
            System.out.println("Info: " + shapes[i].getInfo());
            
            // These calls are resolved at runtime based on actual object type
            shapes[i].draw();           // Polymorphic call
            shapes[i].calculateArea();  // Polymorphic call
        }
        
        // Demonstrating method resolution
        System.out.println("\n=== Method Resolution Analysis ===");
        analyzeMethodCalls(shape1); // Circle object
        analyzeMethodCalls(shape2); // Rectangle object
        analyzeMethodCalls(shape3); // Shape object
    }
    
    public static void analyzeMethodCalls(Shape shape) {
        System.out.println("\nAnalyzing: " + shape.getClass().getSimpleName());
        System.out.println("Method call resolution:");
        shape.draw();           // Calls overridden method in actual class
        shape.calculateArea();  // Calls overridden method in actual class
    }
}
```

</div>

</div>

---
layout: default
---

# Interface-based Polymorphism

<div class="grid grid-cols-2 gap-6">

<div>

## Interface Polymorphism
```java
// Interface definition
public interface Drawable {
    void draw();
    
    default void prepare() {
        System.out.println("Preparing to draw...");
    }
    
    default void cleanup() {
        System.out.println("Cleaning up after drawing");
    }
}

public interface Movable {
    void move(int x, int y);
    
    default void resetPosition() {
        move(0, 0);
    }
}

public interface Scalable {
    void scale(double factor);
    
    default void doubleSize() {
        scale(2.0);
    }
    
    default void halveSize() {
        scale(0.5);
    }
}

// Multiple interface implementation
public class GameObject implements Drawable, Movable, Scalable {
    private String name;
    private int x, y;
    private double size = 1.0;
    
    public GameObject(String name) {
        this.name = name;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing " + name + " at (" + x + "," + y + 
                         ") with size " + size);
    }
    
    @Override
    public void move(int x, int y) {
        this.x = x;
        this.y = y;
        System.out.println(name + " moved to (" + x + "," + y + ")");
    }
    
    @Override
    public void scale(double factor) {
        size *= factor;
        System.out.println(name + " scaled by " + factor + 
                         ", new size: " + size);
    }
    
    public String getName() { return name; }
}
```

</div>

<div>

## Polymorphic Interface Usage
```java
public class GraphicsEngine {
    // Polymorphic collections
    private List<Drawable> drawableObjects = new ArrayList<>();
    private List<Movable> movableObjects = new ArrayList<>();
    private List<Scalable> scalableObjects = new ArrayList<>();
    
    public void addGameObject(GameObject obj) {
        // Same object can be stored in multiple polymorphic collections
        drawableObjects.add(obj);   // As Drawable
        movableObjects.add(obj);    // As Movable  
        scalableObjects.add(obj);   // As Scalable
    }
    
    // Polymorphic operations
    public void renderAll() {
        System.out.println("=== Rendering All Objects ===");
        for (Drawable drawable : drawableObjects) {
            drawable.prepare();     // Interface default method
            drawable.draw();        // Polymorphic call
            drawable.cleanup();     // Interface default method
        }
    }
    
    public void moveAll(int deltaX, int deltaY) {
        System.out.println("=== Moving All Objects ===");
        for (Movable movable : movableObjects) {
            // Get current position if possible (casting)
            if (movable instanceof GameObject) {
                GameObject obj = (GameObject) movable;
                System.out.println("Moving " + obj.getName());
            }
            movable.move(deltaX, deltaY);  // Polymorphic call
        }
    }
    
    public void scaleAll(double factor) {
        System.out.println("=== Scaling All Objects ===");
        for (Scalable scalable : scalableObjects) {
            scalable.scale(factor);  // Polymorphic call
        }
    }
    
    public void resetAllPositions() {
        System.out.println("=== Resetting Positions ===");
        for (Movable movable : movableObjects) {
            movable.resetPosition(); // Default interface method
        }
    }
}

// Usage demonstration
public class GameDemo {
    public static void main(String[] args) {
        GraphicsEngine engine = new GraphicsEngine();
        
        // Create different game objects
        GameObject player = new GameObject("Player");
        GameObject enemy = new GameObject("Enemy");
        GameObject powerUp = new GameObject("PowerUp");
        
        // Add to engine
        engine.addGameObject(player);
        engine.addGameObject(enemy);
        engine.addGameObject(powerUp);
        
        // Polymorphic operations
        engine.renderAll();
        engine.moveAll(10, 20);
        engine.scaleAll(1.5);
        engine.resetAllPositions();
    }
}
```

</div>

</div>

---
layout: default
---

# Polymorphic Collections and Generic Types

<div class="grid grid-cols-2 gap-6">

<div>

## Polymorphic Collections
```java
// Base class hierarchy
public abstract class Vehicle {
    protected String brand;
    protected String model;
    protected double price;
    
    public Vehicle(String brand, String model, double price) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }
    
    public abstract void start();
    public abstract void stop();
    public abstract double calculateMaintenanceCost();
    
    public void displayInfo() {
        System.out.println(brand + " " + model + " - $" + price);
    }
    
    // Getters
    public String getBrand() { return brand; }
    public String getModel() { return model; }
    public double getPrice() { return price; }
}

public class Car extends Vehicle {
    private int doors;
    private String fuelType;
    
    public Car(String brand, String model, double price, 
               int doors, String fuelType) {
        super(brand, model, price);
        this.doors = doors;
        this.fuelType = fuelType;
    }
    
    @Override
    public void start() {
        System.out.println("Car " + brand + " " + model + 
                         " engine started (" + fuelType + ")");
    }
    
    @Override
    public void stop() {
        System.out.println("Car engine stopped, parking brake engaged");
    }
    
    @Override
    public double calculateMaintenanceCost() {
        return price * 0.05; // 5% of car value annually
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("  Type: " + doors + "-door car, Fuel: " + fuelType);
    }
}

public class Motorcycle extends Vehicle {
    private int engineCC;
    private boolean hasWindshield;
    
    public Motorcycle(String brand, String model, double price, 
                     int engineCC, boolean hasWindshield) {
        super(brand, model, price);
        this.engineCC = engineCC;
        this.hasWindshield = hasWindshield;
    }
    
    @Override
    public void start() {
        System.out.println("Motorcycle " + brand + " " + model + 
                         " (" + engineCC + "cc) kick-started!");
    }
    
    @Override
    public void stop() {
        System.out.println("Motorcycle engine stopped, kickstand down");
    }
    
    @Override
    public double calculateMaintenanceCost() {
        return price * 0.08; // 8% of bike value annually
    }
    
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("  Type: " + engineCC + "cc motorcycle" + 
                         (hasWindshield ? " with windshield" : ""));
    }
}
```

</div>

<div>

## Collection Operations
```java
public class VehicleManager {
    private List<Vehicle> vehicles;
    
    public VehicleManager() {
        vehicles = new ArrayList<>();
    }
    
    public void addVehicle(Vehicle vehicle) {
        vehicles.add(vehicle);
        System.out.println("Added: " + vehicle.getBrand() + " " + 
                          vehicle.getModel());
    }
    
    // Polymorphic operations on collections
    public void startAllVehicles() {
        System.out.println("\n=== Starting All Vehicles ===");
        for (Vehicle vehicle : vehicles) {
            vehicle.start(); // Polymorphic call
        }
    }
    
    public void stopAllVehicles() {
        System.out.println("\n=== Stopping All Vehicles ===");
        for (Vehicle vehicle : vehicles) {
            vehicle.stop(); // Polymorphic call
        }
    }
    
    public void displayInventory() {
        System.out.println("\n=== Vehicle Inventory ===");
        for (Vehicle vehicle : vehicles) {
            vehicle.displayInfo(); // Polymorphic call
        }
    }
    
    public double calculateTotalMaintenanceCost() {
        double total = 0;
        for (Vehicle vehicle : vehicles) {
            total += vehicle.calculateMaintenanceCost(); // Polymorphic call
        }
        return total;
    }
    
    // Type-specific operations using instanceof
    public void performCarSpecificMaintenance() {
        System.out.println("\n=== Car-Specific Maintenance ===");
        for (Vehicle vehicle : vehicles) {
            if (vehicle instanceof Car) {
                Car car = (Car) vehicle;
                System.out.println("Performing car maintenance on: " + 
                                 car.getBrand() + " " + car.getModel());
                // Car-specific maintenance logic
            }
        }
    }
    
    // Filtering with polymorphism
    public List<Vehicle> getVehiclesByBrand(String brand) {
        List<Vehicle> result = new ArrayList<>();
        for (Vehicle vehicle : vehicles) {
            if (vehicle.getBrand().equalsIgnoreCase(brand)) {
                result.add(vehicle);
            }
        }
        return result;
    }
    
    public List<Vehicle> getVehiclesAbovePrice(double minPrice) {
        return vehicles.stream()
                      .filter(v -> v.getPrice() > minPrice)
                      .collect(Collectors.toList());
    }
}

// Usage demonstration
public class VehicleManagerDemo {
    public static void main(String[] args) {
        VehicleManager manager = new VehicleManager();
        
        // Adding different types of vehicles
        manager.addVehicle(new Car("Toyota", "Camry", 25000, 4, "Gasoline"));
        manager.addVehicle(new Car("Tesla", "Model 3", 40000, 4, "Electric"));
        manager.addVehicle(new Motorcycle("Harley", "Sportster", 15000, 883, true));
        manager.addVehicle(new Motorcycle("Honda", "CBR", 12000, 600, false));
        
        // Polymorphic operations
        manager.displayInventory();
        manager.startAllVehicles();
        manager.stopAllVehicles();
        
        System.out.println("\nTotal maintenance cost: $" + 
                          manager.calculateTotalMaintenanceCost());
        
        manager.performCarSpecificMaintenance();
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Example: Graphics Drawing System

<div class="grid grid-cols-2 gap-6">

<div>

## Graphics System Design
```java
// Base graphics interface
public interface Graphic {
    void draw();
    void move(int dx, int dy);
    void resize(double factor);
    
    default void display() {
        System.out.println("Displaying: " + getDescription());
        draw();
    }
    
    String getDescription();
}

// Abstract base for shapes
public abstract class Shape implements Graphic {
    protected int x, y;
    protected String color;
    protected boolean filled;
    
    public Shape(int x, int y, String color, boolean filled) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.filled = filled;
    }
    
    @Override
    public void move(int dx, int dy) {
        x += dx;
        y += dy;
        System.out.println(getDescription() + " moved by (" + dx + "," + dy + 
                         ") to (" + x + "," + y + ")");
    }
    
    @Override
    public String getDescription() {
        return (filled ? "Filled " : "Outlined ") + 
               color + " " + getShapeType() + " at (" + x + "," + y + ")";
    }
    
    protected abstract String getShapeType();
    public abstract double getArea();
    public abstract double getPerimeter();
}

// Concrete shape implementations
public class Circle extends Shape {
    private double radius;
    
    public Circle(int x, int y, String color, boolean filled, double radius) {
        super(x, y, color, filled);
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing circle: center(" + x + "," + y + 
                         "), radius=" + radius + ", " + 
                         (filled ? "filled" : "outline") + ", color=" + color);
    }
    
    @Override
    public void resize(double factor) {
        radius *= factor;
        System.out.println("Circle resized by factor " + factor + 
                         ", new radius: " + radius);
    }
    
    @Override
    protected String getShapeType() { return "Circle"; }
    
    @Override
    public double getArea() { return Math.PI * radius * radius; }
    
    @Override
    public double getPerimeter() { return 2 * Math.PI * radius; }
}

public class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(int x, int y, String color, boolean filled, 
                    double width, double height) {
        super(x, y, color, filled);
        this.width = width;
        this.height = height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing rectangle: corner(" + x + "," + y + 
                         "), size=" + width + "x" + height + ", " + 
                         (filled ? "filled" : "outline") + ", color=" + color);
    }
    
    @Override
    public void resize(double factor) {
        width *= factor;
        height *= factor;
        System.out.println("Rectangle resized by factor " + factor + 
                         ", new size: " + width + "x" + height);
    }
    
    @Override
    protected String getShapeType() { return "Rectangle"; }
    
    @Override
    public double getArea() { return width * height; }
    
    @Override
    public double getPerimeter() { return 2 * (width + height); }
}
```

</div>

<div>

## Graphics Engine Implementation
```java
// Text graphics
public class Text implements Graphic {
    private int x, y;
    private String content;
    private String font;
    private int size;
    private String color;
    
    public Text(int x, int y, String content, String font, 
               int size, String color) {
        this.x = x;
        this.y = y;
        this.content = content;
        this.font = font;
        this.size = size;
        this.color = color;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing text: \"" + content + "\" at (" + x + "," + y + 
                         "), font=" + font + ", size=" + size + ", color=" + color);
    }
    
    @Override
    public void move(int dx, int dy) {
        x += dx;
        y += dy;
        System.out.println("Text moved to (" + x + "," + y + ")");
    }
    
    @Override
    public void resize(double factor) {
        size = (int)(size * factor);
        System.out.println("Text resized, new size: " + size);
    }
    
    @Override
    public String getDescription() {
        return "Text \"" + content + "\" at (" + x + "," + y + ")";
    }
}

// Composite graphics - can contain other graphics
public class GraphicsGroup implements Graphic {
    private List<Graphic> graphics;
    private String name;
    
    public GraphicsGroup(String name) {
        this.name = name;
        this.graphics = new ArrayList<>();
    }
    
    public void add(Graphic graphic) {
        graphics.add(graphic);
        System.out.println("Added " + graphic.getDescription() + " to " + name);
    }
    
    public void remove(Graphic graphic) {
        graphics.remove(graphic);
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing group: " + name);
        for (Graphic graphic : graphics) {
            graphic.draw(); // Polymorphic call
        }
    }
    
    @Override
    public void move(int dx, int dy) {
        System.out.println("Moving group: " + name);
        for (Graphic graphic : graphics) {
            graphic.move(dx, dy); // Polymorphic call
        }
    }
    
    @Override
    public void resize(double factor) {
        System.out.println("Resizing group: " + name);
        for (Graphic graphic : graphics) {
            graphic.resize(factor); // Polymorphic call
        }
    }
    
    @Override
    public String getDescription() {
        return "Group \"" + name + "\" with " + graphics.size() + " elements";
    }
}

// Graphics canvas/engine
public class Canvas {
    private List<Graphic> elements;
    private String title;
    
    public Canvas(String title) {
        this.title = title;
        this.elements = new ArrayList<>();
    }
    
    public void add(Graphic element) {
        elements.add(element);
    }
    
    public void render() {
        System.out.println("\n=== Rendering Canvas: " + title + " ===");
        for (Graphic element : elements) {
            element.display(); // Uses default method + polymorphic draw()
            System.out.println();
        }
    }
    
    public void moveAll(int dx, int dy) {
        System.out.println("\n=== Moving All Elements ===");
        for (Graphic element : elements) {
            element.move(dx, dy); // Polymorphic call
        }
    }
    
    public void resizeAll(double factor) {
        System.out.println("\n=== Resizing All Elements ===");
        for (Graphic element : elements) {
            element.resize(factor); // Polymorphic call
        }
    }
    
    public void calculateShapeAreas() {
        System.out.println("\n=== Shape Areas ===");
        for (Graphic element : elements) {
            if (element instanceof Shape) {
                Shape shape = (Shape) element;
                System.out.println(shape.getDescription() + 
                                 " - Area: " + shape.getArea());
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

# Hands-on Exercise 1: Media Player System

<div class="grid grid-cols-2 gap-6">

<div>

## Task
Create a polymorphic media player system:

## Media System Design
```java
// Base media interface
public interface Media {
    void play();
    void pause();
    void stop();
    String getTitle();
    int getDuration(); // in seconds
    String getFormat();
    
    default void displayInfo() {
        System.out.println("Title: " + getTitle());
        System.out.println("Duration: " + formatTime(getDuration()));
        System.out.println("Format: " + getFormat());
    }
    
    default String formatTime(int seconds) {
        int minutes = seconds / 60;
        int secs = seconds % 60;
        return String.format("%d:%02d", minutes, secs);
    }
}

// Audio media interface
public interface AudioMedia extends Media {
    void setVolume(int volume); // 0-100
    int getVolume();
    void setEqualizer(String preset);
    
    default void fade(int targetVolume, int seconds) {
        int currentVolume = getVolume();
        System.out.println("Fading from " + currentVolume + 
                         " to " + targetVolume + " over " + seconds + " seconds");
        setVolume(targetVolume);
    }
}

// Video media interface
public interface VideoMedia extends Media {
    void setResolution(String resolution);
    String getResolution();
    void setFullscreen(boolean fullscreen);
    void enableSubtitles(boolean enable);
    
    default void toggleFullscreen() {
        // This would typically track current state
        setFullscreen(!isFullscreen());
        System.out.println("Toggled fullscreen mode");
    }
    
    // Helper method (would normally track state)
    default boolean isFullscreen() { 
        return false; // Simplified implementation
    }
}

// Streaming capability
public interface Streamable {
    void startStreaming(String url);
    void stopStreaming();
    boolean isStreaming();
    int getBitrate();
    
    default String getStreamQuality() {
        int bitrate = getBitrate();
        if (bitrate >= 1080) return "HD";
        if (bitrate >= 720) return "Standard";
        return "Low";
    }
}
```

</div>

<div>

## Media Implementations
```java
// Music file implementation
public class MusicFile implements AudioMedia, Streamable {
    private String title;
    private String artist;
    private String album;
    private int duration;
    private String format;
    private int volume = 75;
    private String equalizer = "Normal";
    private boolean isPlaying = false;
    private boolean isPaused = false;
    private boolean streaming = false;
    private int bitrate = 320;
    
    public MusicFile(String title, String artist, String album, 
                    int duration, String format) {
        this.title = title;
        this.artist = artist;
        this.album = album;
        this.duration = duration;
        this.format = format;
    }
    
    @Override
    public void play() {
        if (isPaused) {
            System.out.println("Resuming: " + title + " by " + artist);
            isPaused = false;
        } else {
            System.out.println("Playing: " + title + " by " + artist + 
                             " (Volume: " + volume + "%)");
            isPlaying = true;
        }
    }
    
    @Override
    public void pause() {
        if (isPlaying) {
            System.out.println("Paused: " + title);
            isPaused = true;
        }
    }
    
    @Override
    public void stop() {
        System.out.println("Stopped: " + title);
        isPlaying = false;
        isPaused = false;
    }
    
    @Override
    public String getTitle() { return title + " - " + artist; }
    
    @Override
    public int getDuration() { return duration; }
    
    @Override
    public String getFormat() { return format; }
    
    @Override
    public void setVolume(int volume) {
        this.volume = Math.max(0, Math.min(100, volume));
        System.out.println("Volume set to: " + this.volume + "%");
    }
    
    @Override
    public int getVolume() { return volume; }
    
    @Override
    public void setEqualizer(String preset) {
        this.equalizer = preset;
        System.out.println("Equalizer set to: " + preset);
    }
    
    // Streamable implementation
    @Override
    public void startStreaming(String url) {
        streaming = true;
        System.out.println("Started streaming " + title + " to " + url);
    }
    
    @Override
    public void stopStreaming() {
        streaming = false;
        System.out.println("Stopped streaming " + title);
    }
    
    @Override
    public boolean isStreaming() { return streaming; }
    
    @Override
    public int getBitrate() { return bitrate; }
    
    @Override
    public void displayInfo() {
        System.out.println("♪ " + title + " by " + artist);
        System.out.println("  Album: " + album);
        System.out.println("  Duration: " + formatTime(duration));
        System.out.println("  Format: " + format + " (" + bitrate + " kbps)");
        System.out.println("  Volume: " + volume + "%, EQ: " + equalizer);
    }
}

// Video file implementation
public class VideoFile implements VideoMedia, Streamable {
    private String title;
    private String director;
    private int duration;
    private String format;
    private String resolution = "1080p";
    private boolean fullscreen = false;
    private boolean subtitlesEnabled = false;
    private boolean isPlaying = false;
    private boolean streaming = false;
    private int bitrate = 1080;
    
    public VideoFile(String title, String director, int duration, String format) {
        this.title = title;
        this.director = director;
        this.duration = duration;
        this.format = format;
    }
    
    @Override
    public void play() {
        System.out.println("Playing video: " + title + 
                         " (" + resolution + (fullscreen ? " Fullscreen" : "") + 
                         (subtitlesEnabled ? " with subtitles" : "") + ")");
        isPlaying = true;
    }
    
    @Override
    public void pause() {
        System.out.println("Video paused: " + title);
    }
    
    @Override
    public void stop() {
        System.out.println("Video stopped: " + title);
        isPlaying = false;
    }
    
    @Override
    public String getTitle() { return title; }
    
    @Override
    public int getDuration() { return duration; }
    
    @Override
    public String getFormat() { return format; }
    
    @Override
    public void setResolution(String resolution) {
        this.resolution = resolution;
        System.out.println("Resolution set to: " + resolution);
    }
    
    @Override
    public String getResolution() { return resolution; }
    
    @Override
    public void setFullscreen(boolean fullscreen) {
        this.fullscreen = fullscreen;
        System.out.println("Fullscreen: " + (fullscreen ? "ON" : "OFF"));
    }
    
    @Override
    public void enableSubtitles(boolean enable) {
        this.subtitlesEnabled = enable;
        System.out.println("Subtitles: " + (enable ? "ON" : "OFF"));
    }
    
    @Override
    public boolean isFullscreen() { return fullscreen; }
    
    // Streamable implementation
    @Override
    public void startStreaming(String url) {
        streaming = true;
        System.out.println("Started streaming " + title + " to " + url + 
                         " (" + getStreamQuality() + " quality)");
    }
    
    @Override
    public void stopStreaming() {
        streaming = false;
        System.out.println("Stopped streaming " + title);
    }
    
    @Override
    public boolean isStreaming() { return streaming; }
    
    @Override
    public int getBitrate() { return bitrate; }
    
    @Override
    public void displayInfo() {
        System.out.println("🎬 " + title);
        System.out.println("  Director: " + director);
        System.out.println("  Duration: " + formatTime(duration));
        System.out.println("  Format: " + format + " (" + resolution + ")");
        System.out.println("  Streaming: " + (streaming ? "Yes" : "No"));
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: E-commerce Product System

<div class="grid grid-cols-2 gap-6">

<div>

## Product System Design
```java
// Base product interface
public interface Product {
    String getName();
    double getPrice();
    String getCategory();
    String getDescription();
    boolean isInStock();
    
    default void displayBasicInfo() {
        System.out.println("Product: " + getName());
        System.out.println("Price: $" + getPrice());
        System.out.println("Category: " + getCategory());
        System.out.println("In Stock: " + (isInStock() ? "Yes" : "No"));
    }
    
    default String getPriceDisplay() {
        return String.format("$%.2f", getPrice());
    }
}

// Shippable product interface
public interface Shippable extends Product {
    double getWeight();
    String getDimensions();
    double calculateShippingCost(String destination);
    
    default boolean requiresSpecialHandling() {
        return getWeight() > 50.0; // Over 50 lbs needs special handling
    }
    
    default String getShippingInfo() {
        return "Weight: " + getWeight() + " lbs, Dimensions: " + getDimensions();
    }
}

// Digital product interface
public interface DigitalProduct extends Product {
    String getDownloadUrl();
    long getFileSize(); // in bytes
    String getFileFormat();
    int getDownloadCount();
    
    default String getFileSizeDisplay() {
        long size = getFileSize();
        if (size >= 1_000_000_000) {
            return String.format("%.1f GB", size / 1_000_000_000.0);
        } else if (size >= 1_000_000) {
            return String.format("%.1f MB", size / 1_000_000.0);
        } else {
            return String.format("%.1f KB", size / 1_000.0);
        }
    }
}

// Reviewable product interface
public interface Reviewable {
    void addReview(int rating, String comment);
    double getAverageRating();
    int getReviewCount();
    
    default String getRatingDisplay() {
        double rating = getAverageRating();
        return String.format("%.1f/5.0 (%d reviews)", rating, getReviewCount());
    }
    
    default String getStarRating() {
        int stars = (int) Math.round(getAverageRating());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            sb.append(i < stars ? "★" : "☆");
        }
        return sb.toString();
    }
}
```

</div>

<div>

## Product Implementations
```java
// Physical book implementation
public class PhysicalBook implements Shippable, Reviewable {
    private String title;
    private String author;
    private String isbn;
    private double price;
    private double weight;
    private String dimensions;
    private boolean inStock;
    private List<Review> reviews;
    
    public PhysicalBook(String title, String author, String isbn, 
                       double price, double weight, String dimensions) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.price = price;
        this.weight = weight;
        this.dimensions = dimensions;
        this.inStock = true;
        this.reviews = new ArrayList<>();
    }
    
    @Override
    public String getName() { return title + " by " + author; }
    
    @Override
    public double getPrice() { return price; }
    
    @Override
    public String getCategory() { return "Books"; }
    
    @Override
    public String getDescription() { 
        return "Physical book: " + title + " by " + author + " (ISBN: " + isbn + ")"; 
    }
    
    @Override
    public boolean isInStock() { return inStock; }
    
    @Override
    public double getWeight() { return weight; }
    
    @Override
    public String getDimensions() { return dimensions; }
    
    @Override
    public double calculateShippingCost(String destination) {
        double baseCost = 3.99;
        if ("international".equalsIgnoreCase(destination)) {
            baseCost *= 3;
        }
        if (requiresSpecialHandling()) {
            baseCost += 5.00;
        }
        return baseCost;
    }
    
    @Override
    public void addReview(int rating, String comment) {
        reviews.add(new Review(rating, comment));
    }
    
    @Override
    public double getAverageRating() {
        if (reviews.isEmpty()) return 0.0;
        return reviews.stream().mapToInt(Review::getRating).average().orElse(0.0);
    }
    
    @Override
    public int getReviewCount() { return reviews.size(); }
    
    @Override
    public void displayBasicInfo() {
        System.out.println("📚 " + getName());
        System.out.println("  Price: " + getPriceDisplay());
        System.out.println("  " + getShippingInfo());
        System.out.println("  Rating: " + getRatingDisplay() + " " + getStarRating());
        System.out.println("  ISBN: " + isbn);
    }
}

// Digital software implementation  
public class Software implements DigitalProduct, Reviewable {
    private String name;
    private String version;
    private double price;
    private String downloadUrl;
    private long fileSize;
    private String fileFormat;
    private int downloadCount;
    private boolean inStock;
    private List<Review> reviews;
    
    public Software(String name, String version, double price, 
                   long fileSize, String fileFormat) {
        this.name = name;
        this.version = version;
        this.price = price;
        this.downloadUrl = "https://downloads.example.com/" + 
                          name.toLowerCase().replace(" ", "-");
        this.fileSize = fileSize;
        this.fileFormat = fileFormat;
        this.downloadCount = 0;
        this.inStock = true;
        this.reviews = new ArrayList<>();
    }
    
    @Override
    public String getName() { return name + " v" + version; }
    
    @Override
    public double getPrice() { return price; }
    
    @Override
    public String getCategory() { return "Software"; }
    
    @Override
    public String getDescription() { 
        return "Digital software: " + name + " version " + version; 
    }
    
    @Override
    public boolean isInStock() { return inStock; }
    
    @Override
    public String getDownloadUrl() { return downloadUrl; }
    
    @Override
    public long getFileSize() { return fileSize; }
    
    @Override
    public String getFileFormat() { return fileFormat; }
    
    @Override
    public int getDownloadCount() { return downloadCount; }
    
    public void incrementDownloadCount() { downloadCount++; }
    
    @Override
    public void addReview(int rating, String comment) {
        reviews.add(new Review(rating, comment));
    }
    
    @Override
    public double getAverageRating() {
        if (reviews.isEmpty()) return 0.0;
        return reviews.stream().mapToInt(Review::getRating).average().orElse(0.0);
    }
    
    @Override
    public int getReviewCount() { return reviews.size(); }
    
    @Override
    public void displayBasicInfo() {
        System.out.println("💾 " + getName());
        System.out.println("  Price: " + getPriceDisplay());
        System.out.println("  File Size: " + getFileSizeDisplay());
        System.out.println("  Format: " + fileFormat);
        System.out.println("  Downloads: " + downloadCount);
        System.out.println("  Rating: " + getRatingDisplay() + " " + getStarRating());
    }
}

// Review helper class
class Review {
    private int rating;
    private String comment;
    
    public Review(int rating, String comment) {
        this.rating = rating;
        this.comment = comment;
    }
    
    public int getRating() { return rating; }
    public String getComment() { return comment; }
}
```

## E-commerce Store Manager
```java
public class StoreManager {
    private List<Product> products;
    
    public StoreManager() {
        products = new ArrayList<>();
    }
    
    public void addProduct(Product product) {
        products.add(product);
        System.out.println("Added: " + product.getName());
    }
    
    public void displayAllProducts() {
        System.out.println("\n=== Store Inventory ===");
        for (Product product : products) {
            product.displayBasicInfo(); // Polymorphic call
            System.out.println();
        }
    }
    
    public void calculateShippingCosts(String destination) {
        System.out.println("\n=== Shipping Costs to " + destination + " ===");
        for (Product product : products) {
            if (product instanceof Shippable) {
                Shippable shippable = (Shippable) product;
                double cost = shippable.calculateShippingCost(destination);
                System.out.println(product.getName() + ": $" + 
                                 String.format("%.2f", cost));
            }
        }
    }
    
    public void showDigitalProducts() {
        System.out.println("\n=== Digital Products ===");
        for (Product product : products) {
            if (product instanceof DigitalProduct) {
                DigitalProduct digital = (DigitalProduct) product;
                System.out.println(product.getName() + " - " + 
                                 digital.getFileSizeDisplay());
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

# Polymorphism Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Design Principles

### 1. Program to Interfaces
```java
// GOOD: Program to interface
public class PaymentProcessor {
    private PaymentMethod paymentMethod;
    
    public PaymentProcessor(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }
    
    public boolean processPayment(double amount) {
        return paymentMethod.charge(amount); // Polymorphic call
    }
}

// BAD: Program to concrete class
public class BadPaymentProcessor {
    private CreditCard creditCard; // Tightly coupled
    
    public boolean processPayment(double amount) {
        return creditCard.charge(amount); // Limited to credit cards only
    }
}
```

### 2. Liskov Substitution Principle
```java
// Base class behavior
public abstract class Bird {
    public abstract void fly();
    public abstract void makeSound();
}

// GOOD: Proper substitution
public class Sparrow extends Bird {
    @Override
    public void fly() {
        System.out.println("Sparrow flies with quick wing beats");
    }
    
    @Override
    public void makeSound() {
        System.out.println("Sparrow chirps");
    }
}

// PROBLEMATIC: Violates LSP
public class Penguin extends Bird {
    @Override
    public void fly() {
        throw new UnsupportedOperationException("Penguins can't fly!");
    }
    
    @Override
    public void makeSound() {
        System.out.println("Penguin makes honking sound");
    }
}

// BETTER: Separate flying capability
public interface Flyable {
    void fly();
}

public abstract class Bird {
    public abstract void makeSound();
}

public class Sparrow extends Bird implements Flyable {
    @Override
    public void fly() { /* implementation */ }
    
    @Override
    public void makeSound() { /* implementation */ }
}

public class Penguin extends Bird {
    @Override
    public void makeSound() { /* implementation */ }
    // No fly method - doesn't implement Flyable
}
```

</div>

<div>

### 3. Proper Use of instanceof
```java
// ACCEPTABLE: Type-specific operations
public void processShape(Shape shape) {
    // Common operations
    shape.draw();
    shape.calculateArea();
    
    // Type-specific operations
    if (shape instanceof Circle) {
        Circle circle = (Circle) shape;
        System.out.println("Circumference: " + circle.getCircumference());
    } else if (shape instanceof Rectangle) {
        Rectangle rect = (Rectangle) shape;
        System.out.println("Diagonal: " + rect.getDiagonal());
    }
}

// BETTER: Use polymorphism instead
public abstract class Shape {
    public abstract void draw();
    public abstract double calculateArea();
    public abstract void displaySpecificInfo(); // Let each shape implement
}
```

### 4. Avoiding Common Pitfalls
```java
// PITFALL: Overriding with different behavior contracts
public class BankAccount {
    protected double balance;
    
    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        }
    }
}

// PROBLEMATIC: Changes expected behavior
public class OverdraftAccount extends BankAccount {
    @Override
    public void withdraw(double amount) {
        balance -= amount; // Allows overdraft - unexpected behavior
        if (balance < 0) {
            balance -= 35; // Overdraft fee
        }
    }
}

// BETTER: Maintain behavioral contract
public class OverdraftAccount extends BankAccount {
    private double overdraftLimit = 500;
    
    @Override
    public void withdraw(double amount) {
        if (amount <= balance + overdraftLimit) {
            balance -= amount;
            if (balance < 0) {
                balance -= 35; // Overdraft fee
            }
        }
        // Still respects the general contract of checking limits
    }
}
```

### 5. Performance Considerations
```java
public class ShapeProcessor {
    // Cache method lookups for better performance
    private static final Map<Class<?>, Method> methodCache = new HashMap<>();
    
    public void processShapes(List<Shape> shapes) {
        for (Shape shape : shapes) {
            // Polymorphic calls are slightly slower than direct calls
            shape.draw(); // JVM optimizes this with HotSpot
            
            // For high-performance scenarios, consider type checking
            if (shape instanceof Circle) {
                processCircle((Circle) shape);
            } else if (shape instanceof Rectangle) {
                processRectangle((Rectangle) shape);
            }
        }
    }
    
    private void processCircle(Circle circle) {
        // Direct method calls - faster
        circle.drawCircle();
    }
    
    private void processRectangle(Rectangle rectangle) {
        rectangle.drawRectangle();
    }
}
```

</div>

</div>

---
layout: default
---

# Advanced Polymorphism Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Visitor Pattern
```java
// Element interface
public interface Shape {
    void accept(ShapeVisitor visitor);
}

// Visitor interface
public interface ShapeVisitor {
    void visit(Circle circle);
    void visit(Rectangle rectangle);
    void visit(Triangle triangle);
}

// Concrete elements
public class Circle implements Shape {
    private double radius;
    
    public Circle(double radius) { this.radius = radius; }
    
    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visit(this); // Double dispatch
    }
    
    public double getRadius() { return radius; }
    public double getArea() { return Math.PI * radius * radius; }
}

public class Rectangle implements Shape {
    private double width, height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public void accept(ShapeVisitor visitor) {
        visitor.visit(this);
    }
    
    public double getWidth() { return width; }
    public double getHeight() { return height; }
    public double getArea() { return width * height; }
}

// Concrete visitors
public class AreaCalculatorVisitor implements ShapeVisitor {
    private double totalArea = 0;
    
    @Override
    public void visit(Circle circle) {
        totalArea += circle.getArea();
        System.out.println("Circle area: " + circle.getArea());
    }
    
    @Override
    public void visit(Rectangle rectangle) {
        totalArea += rectangle.getArea();
        System.out.println("Rectangle area: " + rectangle.getArea());
    }
    
    @Override
    public void visit(Triangle triangle) {
        totalArea += triangle.getArea();
        System.out.println("Triangle area: " + triangle.getArea());
    }
    
    public double getTotalArea() { return totalArea; }
}

public class DrawingVisitor implements ShapeVisitor {
    @Override
    public void visit(Circle circle) {
        System.out.println("Drawing circle with radius: " + circle.getRadius());
    }
    
    @Override
    public void visit(Rectangle rectangle) {
        System.out.println("Drawing rectangle: " + rectangle.getWidth() + 
                         "x" + rectangle.getHeight());
    }
    
    @Override
    public void visit(Triangle triangle) {
        System.out.println("Drawing triangle with base: " + triangle.getBase());
    }
}
```

</div>

<div>

## Template Method Pattern
```java
// Abstract template class
public abstract class DataProcessor {
    // Template method - defines algorithm structure
    public final void processData() {
        loadData();
        validateData();
        if (isValidData()) {
            transformData();
            saveData();
            cleanup();
        } else {
            handleInvalidData();
        }
    }
    
    // Abstract methods - must be implemented by subclasses
    protected abstract void loadData();
    protected abstract void validateData();
    protected abstract void transformData();
    protected abstract void saveData();
    
    // Hook methods - can be overridden
    protected boolean isValidData() {
        return true; // Default implementation
    }
    
    protected void handleInvalidData() {
        System.out.println("Data validation failed");
    }
    
    protected void cleanup() {
        System.out.println("Cleanup completed");
    }
}

// Concrete implementations
public class CSVDataProcessor extends DataProcessor {
    private String csvData;
    private boolean dataValid = false;
    
    @Override
    protected void loadData() {
        System.out.println("Loading CSV data from file");
        csvData = "sample,csv,data"; // Simulate loading
    }
    
    @Override
    protected void validateData() {
        System.out.println("Validating CSV format");
        dataValid = csvData != null && csvData.contains(",");
    }
    
    @Override
    protected boolean isValidData() {
        return dataValid;
    }
    
    @Override
    protected void transformData() {
        System.out.println("Transforming CSV to internal format");
        csvData = csvData.toUpperCase();
    }
    
    @Override
    protected void saveData() {
        System.out.println("Saving transformed data: " + csvData);
    }
    
    @Override
    protected void handleInvalidData() {
        System.out.println("Invalid CSV format detected");
    }
}

public class XMLDataProcessor extends DataProcessor {
    private String xmlData;
    private boolean dataValid = false;
    
    @Override
    protected void loadData() {
        System.out.println("Loading XML data from service");
        xmlData = "<root><data>sample</data></root>";
    }
    
    @Override
    protected void validateData() {
        System.out.println("Validating XML schema");
        dataValid = xmlData != null && xmlData.startsWith("<") && xmlData.endsWith(">");
    }
    
    @Override
    protected boolean isValidData() {
        return dataValid;
    }
    
    @Override
    protected void transformData() {
        System.out.println("Parsing XML and extracting data");
        // XML processing logic
    }
    
    @Override
    protected void saveData() {
        System.out.println("Saving parsed XML data");
    }
}

// Usage
public class ProcessorDemo {
    public static void main(String[] args) {
        DataProcessor csvProcessor = new CSVDataProcessor();
        DataProcessor xmlProcessor = new XMLDataProcessor();
        
        System.out.println("=== Processing CSV ===");
        csvProcessor.processData();
        
        System.out.println("\n=== Processing XML ===");
        xmlProcessor.processData();
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

- 🎭 **Polymorphism Types**: Compile-time (overloading) vs Runtime (overriding)
- 🔄 **Dynamic Dispatch**: How JVM resolves method calls at runtime
- ⚡ **Interface Polymorphism**: Using interfaces for flexible design
- 🎯 **Polymorphic Collections**: Working with mixed object types
- 📝 **Design Patterns**: Visitor, Template Method, Strategy patterns
- 🏗️ **Best Practices**: LSP, program to interfaces, proper instanceof usage
- 🛠️ **Real Applications**: Graphics systems, media players, e-commerce

</v-clicks>

</div>

<div>

## Polymorphism Benefits

### Code Quality
- **Flexibility**: Easy to add new types
- **Maintainability**: Changes localized to specific classes
- **Reusability**: Same code works with different types
- **Testability**: Easy to mock and test

### Design Benefits
- **Loose Coupling**: Depend on abstractions, not implementations
- **Open/Closed Principle**: Open for extension, closed for modification
- **Single Responsibility**: Each class handles its own behavior

## Key Principles Recap

<v-clicks>

- Use method overloading for convenience methods
- Apply method overriding for specialized behavior
- Program to interfaces, not implementations
- Follow Liskov Substitution Principle
- Use polymorphic collections effectively
- Avoid excessive instanceof checking
- Consider performance implications
- Apply appropriate design patterns

</v-clicks>

## Course Unit III Completion
**Unit III: Inheritance, Packages & Interfaces** ✅
- Inheritance fundamentals and types
- Method overriding and super keyword
- Abstract classes and methods
- Packages and access control
- Interfaces and implementation
- **Polymorphism and dynamic behavior**

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Unit III Complete: Inheritance, Packages & Interfaces

**Lectures 21-25 Successfully Completed!**  
You now have a solid foundation in advanced OOP concepts

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Master polymorphic programming patterns! <carbon:arrow-right class="inline"/>
  </span>
</div>

---
layout: center
class: text-center
---

# 🎉 Congratulations! 

## You've Successfully Completed:
### Unit III - Inheritance, Packages & Interfaces

**Lectures 21-25 are now ready for delivery!**

### What You've Learned:
- 📦 **Package Organization** - Structure and manage Java applications
- 🔐 **Access Control** - Secure your code with proper visibility
- 🎯 **Interface Design** - Create flexible, maintainable contracts
- 🏗️ **Implementation Patterns** - Build robust, scalable systems
- 🎭 **Polymorphism Mastery** - Write elegant, polymorphic code

### Ready for GTU Java Programming Course! 🚀