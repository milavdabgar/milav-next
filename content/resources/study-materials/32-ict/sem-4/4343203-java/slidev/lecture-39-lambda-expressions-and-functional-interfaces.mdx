---
theme: default
background: https://source.unsplash.com/1024x768/?java,programming
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: Java Programming - Lecture 39
mdc: true
---

# Java Programming
## Lecture 39: Lambda Expressions and Functional Interfaces
### GTU Diploma in Computer Engineering

---
layout: two-cols
---

# Learning Objectives

After this lecture, you will be able to:

- Understand functional programming concepts in Java
- Write and use lambda expressions effectively
- Work with built-in functional interfaces
- Create custom functional interfaces
- Use method references and constructor references
- Apply functional programming patterns
- Understand the benefits of functional style programming

::right::

# Lecture Overview

1. **Introduction to Functional Programming**
2. **Lambda Expression Syntax**
3. **Functional Interfaces**
4. **Built-in Functional Interfaces**
5. **Method References**
6. **Custom Functional Interfaces**
7. **Functional Programming Patterns**
8. **Best Practices**
9. **Hands-on Exercises**

---

# What is Functional Programming?

Functional programming is a programming paradigm that treats computation as evaluation of mathematical functions.

## Key Concepts

1. **Functions as First-Class Objects**: Functions can be assigned to variables, passed as parameters
2. **Immutability**: Data doesn't change after creation
3. **Pure Functions**: Functions with no side effects
4. **Higher-Order Functions**: Functions that take or return other functions

## Java 8 and Functional Programming

```java
// Traditional approach (before Java 8)
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
Collections.sort(names, new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return a.compareTo(b);
    }
});

// Functional approach (Java 8+)
names.sort((a, b) -> a.compareTo(b));
// Or even simpler
names.sort(String::compareTo);
```

---

# Introduction to Lambda Expressions

Lambda expressions provide a concise way to represent anonymous functions.

## Syntax

```java
// Basic syntax
(parameters) -> expression
(parameters) -> { statements; }

// Examples
() -> System.out.println("Hello")                    // No parameters
x -> x * x                                           // Single parameter
(x, y) -> x + y                                     // Multiple parameters
(String s) -> s.length()                            // Explicit type
x -> { return x * x; }                              // Block body
(x, y) -> { 
    int sum = x + y; 
    return sum * 2; 
}                                                   // Multi-statement block
```

## Comparison with Anonymous Classes

```java
// Anonymous class
Runnable runnable1 = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello from anonymous class");
    }
};

// Lambda expression
Runnable runnable2 = () -> System.out.println("Hello from lambda");

// Both work the same way
new Thread(runnable1).start();
new Thread(runnable2).start();
new Thread(() -> System.out.println("Direct lambda")).start();
```

---

# Lambda Expression Examples

## Basic Examples

```java
import java.util.*;
import java.util.function.*;

public class LambdaBasics {
    public static void main(String[] args) {
        // Example 1: Simple operations
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        
        // Print each number
        numbers.forEach(n -> System.out.println(n));
        
        // Example 2: Filtering
        List<Integer> evenNumbers = new ArrayList<>();
        numbers.forEach(n -> {
            if (n % 2 == 0) {
                evenNumbers.add(n);
            }
        });
        System.out.println("Even numbers: " + evenNumbers);
        
        // Example 3: Transformation
        List<Integer> squares = new ArrayList<>();
        numbers.forEach(n -> squares.add(n * n));
        System.out.println("Squares: " + squares);
        
        // Example 4: Comparison
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");
        names.sort((a, b) -> a.length() - b.length());  // Sort by length
        System.out.println("Sorted by length: " + names);
        
        names.sort((a, b) -> a.compareTo(b));  // Sort alphabetically
        System.out.println("Sorted alphabetically: " + names);
    }
}
```

---

# Functional Interfaces

A functional interface has exactly one abstract method (SAM - Single Abstract Method).

## @FunctionalInterface Annotation

```java
@FunctionalInterface
public interface Calculator {
    int calculate(int a, int b);
    
    // Default methods are allowed
    default void printResult(int a, int b) {
        System.out.println("Result: " + calculate(a, b));
    }
    
    // Static methods are allowed
    static void info() {
        System.out.println("Calculator interface");
    }
}
```

## Using Functional Interfaces

```java
public class FunctionalInterfaceDemo {
    public static void main(String[] args) {
        // Using lambda expressions
        Calculator add = (a, b) -> a + b;
        Calculator subtract = (a, b) -> a - b;
        Calculator multiply = (a, b) -> a * b;
        Calculator divide = (a, b) -> a / b;
        
        System.out.println("Addition: " + add.calculate(10, 5));
        System.out.println("Subtraction: " + subtract.calculate(10, 5));
        System.out.println("Multiplication: " + multiply.calculate(10, 5));
        System.out.println("Division: " + divide.calculate(10, 5));
        
        // Using default method
        add.printResult(10, 5);
        
        // Using static method
        Calculator.info();
        
        // Passing lambda as parameter
        performOperation(15, 3, (a, b) -> a % b);
    }
    
    public static void performOperation(int x, int y, Calculator calc) {
        int result = calc.calculate(x, y);
        System.out.println("Operation result: " + result);
    }
}
```

---

# Built-in Functional Interfaces

Java 8 provides many built-in functional interfaces in `java.util.function` package.

## Predicate&lt;T&gt;

Tests a condition and returns boolean.

```java
import java.util.function.Predicate;
import java.util.*;

public class PredicateDemo {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // Basic predicates
        Predicate<Integer> isEven = n -> n % 2 == 0;
        Predicate<Integer> isPositive = n -> n > 0;
        Predicate<Integer> isGreaterThan5 = n -> n > 5;
        
        // Using predicates
        System.out.println("Even numbers:");
        filterAndPrint(numbers, isEven);
        
        System.out.println("Numbers greater than 5:");
        filterAndPrint(numbers, isGreaterThan5);
        
        // Combining predicates
        Predicate<Integer> evenAndGreaterThan5 = isEven.and(isGreaterThan5);
        System.out.println("Even numbers greater than 5:");
        filterAndPrint(numbers, evenAndGreaterThan5);
        
        Predicate<Integer> evenOrGreaterThan8 = isEven.or(n -> n > 8);
        System.out.println("Even numbers or greater than 8:");
        filterAndPrint(numbers, evenOrGreaterThan8);
        
        // Negation
        Predicate<Integer> notEven = isEven.negate();
        System.out.println("Odd numbers:");
        filterAndPrint(numbers, notEven);
        
        // String predicates
        List<String> words = Arrays.asList("Java", "Python", "JavaScript", "C++");
        Predicate<String> startsWithJ = s -> s.startsWith("J");
        Predicate<String> longerThan4 = s -> s.length() > 4;
        
        System.out.println("Words starting with 'J':");
        filterAndPrint(words, startsWithJ);
        
        System.out.println("Words starting with 'J' and longer than 4 characters:");
        filterAndPrint(words, startsWithJ.and(longerThan4));
    }
    
    public static <T> void filterAndPrint(List<T> list, Predicate<T> predicate) {
        list.stream().filter(predicate).forEach(System.out::println);
    }
}
```

---

# Function&lt;T, R&gt;

Represents a function that takes one argument and returns a result.

```java
import java.util.function.Function;
import java.util.*;

public class FunctionDemo {
    public static void main(String[] args) {
        // Basic functions
        Function<String, Integer> stringLength = s -> s.length();
        Function<Integer, Integer> square = n -> n * n;
        Function<String, String> uppercase = s -> s.toUpperCase();
        Function<Integer, String> numberToString = n -> "Number: " + n;
        
        // Using functions
        System.out.println("Length of 'Hello': " + stringLength.apply("Hello"));
        System.out.println("Square of 5: " + square.apply(5));
        System.out.println("Uppercase 'hello': " + uppercase.apply("hello"));
        System.out.println(numberToString.apply(42));
        
        // Function composition
        Function<String, String> trimAndUppercase = 
            ((Function<String, String>) String::trim).andThen(String::toUpperCase);
        
        System.out.println("Trim and uppercase '  hello  ': '" + 
                          trimAndUppercase.apply("  hello  ") + "'");
        
        // Chaining functions
        Function<Integer, Integer> multiplyBy2 = n -> n * 2;
        Function<Integer, Integer> add10 = n -> n + 10;
        
        Function<Integer, Integer> multiplyThenAdd = multiplyBy2.andThen(add10);
        Function<Integer, Integer> addThenMultiply = add10.compose(multiplyBy2);
        
        System.out.println("5 * 2 + 10 = " + multiplyThenAdd.apply(5));  // (5*2)+10 = 20
        System.out.println("(5 + 10) * 2 = " + addThenMultiply.apply(5)); // 5*2+10 = 20
        
        // Working with lists
        List<String> names = Arrays.asList("alice", "bob", "charlie");
        List<Integer> nameLengths = transform(names, stringLength);
        List<String> upperNames = transform(names, uppercase);
        
        System.out.println("Original: " + names);
        System.out.println("Lengths: " + nameLengths);
        System.out.println("Uppercase: " + upperNames);
    }
    
    public static <T, R> List<R> transform(List<T> list, Function<T, R> function) {
        List<R> result = new ArrayList<>();
        for (T item : list) {
            result.add(function.apply(item));
        }
        return result;
    }
}
```

---

# Consumer&lt;T&gt; and Supplier&lt;T&gt;

## Consumer&lt;T&gt; - Consumes input, returns nothing

```java
import java.util.function.Consumer;
import java.util.*;

public class ConsumerDemo {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        
        // Basic consumers
        Consumer<String> print = s -> System.out.println(s);
        Consumer<String> printUppercase = s -> System.out.println(s.toUpperCase());
        Consumer<String> printLength = s -> System.out.println("Length: " + s.length());
        
        // Using consumers
        System.out.println("Using print consumer:");
        names.forEach(print);
        
        System.out.println("\nUsing printUppercase consumer:");
        names.forEach(printUppercase);
        
        // Chaining consumers
        Consumer<String> printAndLength = print.andThen(printLength);
        
        System.out.println("\nUsing chained consumer:");
        names.forEach(printAndLength);
        
        // Consumer with side effects
        List<String> processedNames = new ArrayList<>();
        Consumer<String> addToList = s -> processedNames.add(s.toUpperCase());
        
        names.forEach(addToList);
        System.out.println("Processed names: " + processedNames);
        
        // Bi-Consumer example
        Map<String, Integer> nameAges = new HashMap<>();
        nameAges.put("Alice", 25);
        nameAges.put("Bob", 30);
        nameAges.put("Charlie", 35);
        
        nameAges.forEach((name, age) -> 
            System.out.println(name + " is " + age + " years old"));
    }
}
```

---

# Supplier&lt;T&gt; - Supplies a value

```java
import java.util.function.Supplier;
import java.util.*;
import java.time.LocalDateTime;

public class SupplierDemo {
    public static void main(String[] args) {
        // Basic suppliers
        Supplier<String> helloSupplier = () -> "Hello World";
        Supplier<Double> randomSupplier = () -> Math.random();
        Supplier<LocalDateTime> timeSupplier = () -> LocalDateTime.now();
        Supplier<List<String>> listSupplier = () -> new ArrayList<>();
        
        // Using suppliers
        System.out.println("Hello supplier: " + helloSupplier.get());
        System.out.println("Random number: " + randomSupplier.get());
        System.out.println("Current time: " + timeSupplier.get());
        
        // Supplier for lazy initialization
        Supplier<String> expensiveOperation = () -> {
            System.out.println("Performing expensive operation...");
            try {
                Thread.sleep(1000); // Simulate expensive operation
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            return "Expensive result";
        };
        
        System.out.println("Before calling supplier");
        String result = expensiveOperation.get(); // Operation happens here
        System.out.println("Result: " + result);
        
        // Using supplier to generate test data
        Supplier<Person> personSupplier = () -> new Person(
            "Person" + (int)(Math.random() * 1000),
            (int)(Math.random() * 50) + 18
        );
        
        List<Person> people = generateList(personSupplier, 5);
        people.forEach(System.out::println);
    }
    
    public static <T> List<T> generateList(Supplier<T> supplier, int count) {
        List<T> list = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            list.add(supplier.get());
        }
        return list;
    }
    
    static class Person {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + '}';
        }
    }
}
```

---

# Method References

Method references provide a way to refer to methods without executing them.

## Types of Method References

```java
import java.util.*;
import java.util.function.*;

public class MethodReferencesDemo {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");
        
        // 1. Reference to static method
        // Lambda: s -> Integer.parseInt(s)
        Function<String, Integer> parseInt = Integer::parseInt;
        System.out.println("Parsed number: " + parseInt.apply("123"));
        
        // 2. Reference to instance method of particular object
        String prefix = "Hello, ";
        // Lambda: s -> prefix.concat(s)
        Function<String, String> greeting = prefix::concat;
        System.out.println(greeting.apply("World"));
        
        // 3. Reference to instance method of arbitrary object
        // Lambda: s -> s.length()
        Function<String, Integer> length = String::length;
        names.stream()
             .map(String::length)  // Same as s -> s.length()
             .forEach(System.out::println);
        
        // Lambda: s -> s.toUpperCase()
        names.stream()
             .map(String::toUpperCase)  // Same as s -> s.toUpperCase()
             .forEach(System.out::println);
        
        // 4. Reference to constructor
        // Lambda: () -> new ArrayList<>()
        Supplier<List<String>> listSupplier = ArrayList::new;
        List<String> newList = listSupplier.get();
        
        // Lambda: s -> new String(s)
        Function<String, String> stringConstructor = String::new;
        
        // More complex constructor reference
        BiFunction<String, Integer, Person> personConstructor = Person::new;
        Person person = personConstructor.apply("Alice", 25);
        System.out.println("Created person: " + person);
        
        // Using method references with collections
        List<Integer> numbers = Arrays.asList(3, 1, 4, 1, 5, 9);
        
        // Method reference for comparison
        numbers.sort(Integer::compareTo);
        System.out.println("Sorted numbers: " + numbers);
        
        // Method reference for printing
        System.out.println("Numbers:");
        numbers.forEach(System.out::println);
    }
    
    static class Person {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + '}';
        }
    }
}
```

---

# Constructor References

Constructor references are a special form of method references.

```java
import java.util.*;
import java.util.function.*;

public class ConstructorReferencesDemo {
    
    static class Product {
        private String name;
        private double price;
        private String category;
        
        // Default constructor
        public Product() {
            this("Unknown", 0.0, "General");
        }
        
        // Constructor with name and price
        public Product(String name, double price) {
            this.name = name;
            this.price = price;
            this.category = "General";
        }
        
        // Constructor with all parameters
        public Product(String name, double price, String category) {
            this.name = name;
            this.price = price;
            this.category = category;
        }
        
        // Getters
        public String getName() { return name; }
        public double getPrice() { return price; }
        public String getCategory() { return category; }
        
        @Override
        public String toString() {
            return String.format("Product{name='%s', price=%.2f, category='%s'}", 
                               name, price, category);
        }
    }
    
    public static void main(String[] args) {
        // Constructor reference for default constructor
        Supplier<Product> defaultConstructor = Product::new;
        Product product1 = defaultConstructor.get();
        System.out.println("Default product: " + product1);
        
        // Constructor reference for two-parameter constructor
        BiFunction<String, Double, Product> twoParamConstructor = Product::new;
        Product product2 = twoParamConstructor.apply("Laptop", 999.99);
        System.out.println("Two-param product: " + product2);
        
        // Constructor reference for three-parameter constructor
        TriFunction<String, Double, String, Product> threeParamConstructor = Product::new;
        Product product3 = threeParamConstructor.apply("Smartphone", 599.99, "Electronics");
        System.out.println("Three-param product: " + product3);
        
        // Using constructor references with collections
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        
        // Create list of products using constructor reference
        List<Product> products = names.stream()
            .map(name -> new Product(name, Math.random() * 100))
            .collect(ArrayList::new,  // Constructor reference for collection
                    ArrayList::add,   // Method reference for adding
                    ArrayList::addAll); // Method reference for combining
        
        System.out.println("\nGenerated products:");
        products.forEach(System.out::println);
        
        // Array constructor references
        IntFunction<Product[]> arrayConstructor = Product[]::new;
        Product[] productArray = arrayConstructor.apply(3);
        System.out.println("Created array of length: " + productArray.length);
    }
    
    // Custom functional interface for three parameters
    @FunctionalInterface
    interface TriFunction<T, U, V, R> {
        R apply(T t, U u, V v);
    }
}
```

---

# Custom Functional Interfaces

Creating your own functional interfaces for specific use cases.

```java
@FunctionalInterface
interface StringProcessor {
    String process(String input);
    
    // Default methods are allowed
    default String processWithPrefix(String input, String prefix) {
        return prefix + process(input);
    }
    
    // Static methods are allowed
    static StringProcessor identity() {
        return s -> s;
    }
    
    static StringProcessor chain(StringProcessor first, StringProcessor second) {
        return s -> second.process(first.process(s));
    }
}

@FunctionalInterface
interface MathOperation {
    double calculate(double a, double b);
    
    default boolean isCommutative() {
        return false; // Override in specific implementations if needed
    }
}

@FunctionalInterface
interface Validator<T> {
    ValidationResult validate(T input);
    
    default Validator<T> and(Validator<T> other) {
        return input -> {
            ValidationResult result = this.validate(input);
            return result.isValid() ? other.validate(input) : result;
        };
    }
    
    default Validator<T> or(Validator<T> other) {
        return input -> {
            ValidationResult result = this.validate(input);
            return result.isValid() ? result : other.validate(input);
        };
    }
}

class ValidationResult {
    private final boolean valid;
    private final String message;
    
    public ValidationResult(boolean valid, String message) {
        this.valid = valid;
        this.message = message;
    }
    
    public boolean isValid() { return valid; }
    public String getMessage() { return message; }
    
    public static ValidationResult valid() {
        return new ValidationResult(true, "Valid");
    }
    
    public static ValidationResult invalid(String message) {
        return new ValidationResult(false, message);
    }
    
    @Override
    public String toString() {
        return valid ? "Valid" : "Invalid: " + message;
    }
}
```

---

# Using Custom Functional Interfaces

```java
public class CustomFunctionalInterfacesDemo {
    public static void main(String[] args) {
        // String processors
        StringProcessor uppercase = s -> s.toUpperCase();
        StringProcessor reverse = s -> new StringBuilder(s).reverse().toString();
        StringProcessor removeSpaces = s -> s.replaceAll("\\s+", "");
        
        String input = "hello world";
        
        System.out.println("Original: " + input);
        System.out.println("Uppercase: " + uppercase.process(input));
        System.out.println("Reverse: " + reverse.process(input));
        System.out.println("No spaces: " + removeSpaces.process(input));
        
        // Using default method
        System.out.println("With prefix: " + 
            uppercase.processWithPrefix(input, "Processed: "));
        
        // Chaining processors
        StringProcessor chainedProcessor = StringProcessor.chain(
            removeSpaces, 
            StringProcessor.chain(uppercase, reverse)
        );
        System.out.println("Chained (remove spaces -> uppercase -> reverse): " + 
            chainedProcessor.process(input));
        
        // Math operations
        MathOperation add = (a, b) -> a + b;
        MathOperation multiply = (a, b) -> a * b;
        MathOperation power = (a, b) -> Math.pow(a, b);
        
        System.out.println("\nMath Operations:");
        System.out.println("5 + 3 = " + add.calculate(5, 3));
        System.out.println("5 * 3 = " + multiply.calculate(5, 3));
        System.out.println("5^3 = " + power.calculate(5, 3));
        
        // Validators
        Validator<String> notEmpty = s -> 
            s != null && !s.trim().isEmpty() ? 
                ValidationResult.valid() : 
                ValidationResult.invalid("String cannot be empty");
        
        Validator<String> minLength = s -> 
            s != null && s.length() >= 3 ? 
                ValidationResult.valid() : 
                ValidationResult.invalid("String must be at least 3 characters");
        
        Validator<String> noSpaces = s -> 
            s != null && !s.contains(" ") ? 
                ValidationResult.valid() : 
                ValidationResult.invalid("String cannot contain spaces");
        
        Validator<String> combinedValidator = notEmpty.and(minLength).and(noSpaces);
        
        // Testing validators
        String[] testInputs = {"", "ab", "abc", "ab c", "hello", "valid_input"};
        
        System.out.println("\nValidation Results:");
        for (String testInput : testInputs) {
            ValidationResult result = combinedValidator.validate(testInput);
            System.out.println("'" + testInput + "': " + result);
        }
    }
}
```

---

# Functional Programming Patterns

## Higher-Order Functions

```java
import java.util.*;
import java.util.function.*;

public class HigherOrderFunctions {
    
    // Function that returns another function
    public static Function<Integer, Integer> createMultiplier(int factor) {
        return x -> x * factor;
    }
    
    // Function that takes functions as parameters
    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        List<T> result = new ArrayList<>();
        for (T item : list) {
            if (predicate.test(item)) {
                result.add(item);
            }
        }
        return result;
    }
    
    public static <T, R> List<R> map(List<T> list, Function<T, R> mapper) {
        List<R> result = new ArrayList<>();
        for (T item : list) {
            result.add(mapper.apply(item));
        }
        return result;
    }
    
    public static <T> Optional<T> reduce(List<T> list, BinaryOperator<T> accumulator) {
        if (list.isEmpty()) {
            return Optional.empty();
        }
        
        T result = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            result = accumulator.apply(result, list.get(i));
        }
        return Optional.of(result);
    }
    
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // Using higher-order functions
        Function<Integer, Integer> double_func = createMultiplier(2);
        Function<Integer, Integer> triple = createMultiplier(3);
        
        System.out.println("Original numbers: " + numbers);
        
        // Filter even numbers
        List<Integer> evenNumbers = filter(numbers, n -> n % 2 == 0);
        System.out.println("Even numbers: " + evenNumbers);
        
        // Map to squares
        List<Integer> squares = map(numbers, n -> n * n);
        System.out.println("Squares: " + squares);
        
        // Map using created multiplier functions
        List<Integer> doubled = map(numbers, double_func);
        List<Integer> tripled = map(numbers, triple);
        System.out.println("Doubled: " + doubled);
        System.out.println("Tripled: " + tripled);
        
        // Reduce to sum
        Optional<Integer> sum = reduce(numbers, (a, b) -> a + b);
        System.out.println("Sum: " + sum.orElse(0));
        
        // Reduce to product
        Optional<Integer> product = reduce(numbers, (a, b) -> a * b);
        System.out.println("Product: " + product.orElse(0));
        
        // Chain operations
        List<Integer> result = map(
            filter(numbers, n -> n % 2 == 0),  // Get even numbers
            n -> n * n                         // Square them
        );
        System.out.println("Even numbers squared: " + result);
    }
}
```

---

# Currying and Partial Application

```java
import java.util.function.*;

public class CurryingDemo {
    
    // Traditional method with multiple parameters
    public static int add(int a, int b, int c) {
        return a + b + c;
    }
    
    // Curried version - returns function that returns function
    public static Function<Integer, Function<Integer, Function<Integer, Integer>>> curriedAdd() {
        return a -> b -> c -> a + b + c;
    }
    
    // Partial application example
    public static Function<Integer, Function<Integer, Integer>> partialAdd(int a) {
        return b -> c -> a + b + c;
    }
    
    // Generic currying utility
    public static <A, B, C, R> Function<A, Function<B, Function<C, R>>> curry(
            TriFunction<A, B, C, R> function) {
        return a -> b -> c -> function.apply(a, b, c);
    }
    
    // Uncurrying utility
    public static <A, B, C, R> TriFunction<A, B, C, R> uncurry(
            Function<A, Function<B, Function<C, R>>> curried) {
        return (a, b, c) -> curried.apply(a).apply(b).apply(c);
    }
    
    @FunctionalInterface
    interface TriFunction<A, B, C, R> {
        R apply(A a, B b, C c);
    }
    
    public static void main(String[] args) {
        // Traditional approach
        int result1 = add(1, 2, 3);
        System.out.println("Traditional add(1, 2, 3): " + result1);
        
        // Curried approach
        Function<Integer, Function<Integer, Function<Integer, Integer>>> curriedAddFunc = curriedAdd();
        int result2 = curriedAddFunc.apply(1).apply(2).apply(3);
        System.out.println("Curried add(1)(2)(3): " + result2);
        
        // Partial application
        Function<Integer, Function<Integer, Integer>> addWith5 = partialAdd(5);
        Function<Integer, Integer> addWith5And10 = addWith5.apply(10);
        int result3 = addWith5And10.apply(15);
        System.out.println("Partial application 5 + 10 + 15: " + result3);
        
        // More practical example - creating specialized functions
        Function<Integer, Function<Integer, Integer>> addWithFirst = partialAdd(100);
        Function<Integer, Integer> addWith100And20 = addWithFirst.apply(20);
        
        // Use the specialized function multiple times
        System.out.println("100 + 20 + 1 = " + addWith100And20.apply(1));
        System.out.println("100 + 20 + 5 = " + addWith100And20.apply(5));
        System.out.println("100 + 20 + 10 = " + addWith100And20.apply(10));
        
        // Generic currying example
        TriFunction<String, String, String, String> concat = (a, b, c) -> a + b + c;
        Function<String, Function<String, Function<String, String>>> curriedConcat = curry(concat);
        
        String result4 = curriedConcat.apply("Hello").apply(" ").apply("World");
        System.out.println("Curried concat: " + result4);
        
        // Partial application with concat
        Function<String, Function<String, String>> greetingBuilder = 
            curriedConcat.apply("Hello ");
        Function<String, String> sayHelloTo = greetingBuilder.apply("Mr. ");
        
        System.out.println(sayHelloTo.apply("Smith"));
        System.out.println(sayHelloTo.apply("Johnson"));
        System.out.println(sayHelloTo.apply("Brown"));
    }
}
```

---

# Functional Composition

```java
import java.util.function.*;
import java.util.*;

public class FunctionComposition {
    
    // Helper method to create function pipeline
    @SafeVarargs
    public static <T> Function<T, T> pipeline(Function<T, T>... functions) {
        return Arrays.stream(functions)
                     .reduce(Function.identity(), Function::andThen);
    }
    
    public static void main(String[] args) {
        // Basic function composition
        Function<String, String> removeSpaces = s -> s.replaceAll("\\s+", "");
        Function<String, String> toUpperCase = String::toUpperCase;
        Function<String, String> reverse = s -> new StringBuilder(s).reverse().toString();
        
        // Compose using andThen
        Function<String, String> processString1 = removeSpaces.andThen(toUpperCase).andThen(reverse);
        
        // Compose using compose (reverse order)
        Function<String, String> processString2 = reverse.compose(toUpperCase).compose(removeSpaces);
        
        String input = "Hello World Java";
        System.out.println("Original: " + input);
        System.out.println("Using andThen: " + processString1.apply(input));
        System.out.println("Using compose: " + processString2.apply(input));
        
        // More complex composition - number processing
        Function<Integer, Integer> addOne = x -> x + 1;
        Function<Integer, Integer> multiplyByTwo = x -> x * 2;
        Function<Integer, Integer> square = x -> x * x;
        
        Function<Integer, Integer> complexOperation = 
            addOne.andThen(multiplyByTwo).andThen(square);
        
        System.out.println("\nNumber processing:");
        System.out.println("5 -> add1 -> *2 -> square = " + complexOperation.apply(5));
        // (5 + 1) * 2 = 12, 12^2 = 144
        
        // Using pipeline helper method
        Function<String, String> pipeline = pipeline(
            s -> s.toLowerCase(),
            s -> s.replaceAll("[^a-z]", ""),
            s -> s.substring(0, Math.min(5, s.length())),
            String::toUpperCase
        );
        
        System.out.println("\nPipeline processing:");
        System.out.println("'Hello World 123!' -> " + pipeline.apply("Hello World 123!"));
        
        // Predicate composition
        Predicate<Integer> isPositive = x -> x > 0;
        Predicate<Integer> isEven = x -> x % 2 == 0;
        Predicate<Integer> isLessThan100 = x -> x < 100;
        
        Predicate<Integer> complexPredicate = isPositive.and(isEven).and(isLessThan100);
        
        List<Integer> numbers = Arrays.asList(-2, 0, 1, 2, 4, 50, 99, 100, 150);
        
        System.out.println("\nFiltering with complex predicate (positive AND even AND < 100):");
        numbers.stream()
               .filter(complexPredicate)
               .forEach(System.out::println);
        
        // Consumer composition
        Consumer<String> print = System.out::println;
        Consumer<String> printLength = s -> System.out.println("Length: " + s.length());
        Consumer<String> printUppercase = s -> System.out.println("Uppercase: " + s.toUpperCase());
        
        Consumer<String> combinedConsumer = print.andThen(printLength).andThen(printUppercase);
        
        System.out.println("\nCombined consumer:");
        combinedConsumer.accept("functional programming");
    }
}
```

---

# Best Practices

## 1. Keep Lambdas Simple and Readable

```java
// Good - simple and clear
list.stream().filter(s -> s.length() > 5).collect(toList());

// Avoid - complex logic in lambda
list.stream().filter(s -> {
    if (s == null) return false;
    String trimmed = s.trim();
    return trimmed.length() > 5 && trimmed.startsWith("A") && !trimmed.contains(" ");
}).collect(toList());

// Better - extract to method
list.stream().filter(this::isValidString).collect(toList());

private boolean isValidString(String s) {
    if (s == null) return false;
    String trimmed = s.trim();
    return trimmed.length() > 5 && trimmed.startsWith("A") && !trimmed.contains(" ");
}
```

## 2. Prefer Method References When Appropriate

```java
// Less readable
list.forEach(item -> System.out.println(item));
list.stream().map(s -> s.toUpperCase()).collect(toList());

// More readable
list.forEach(System.out::println);
list.stream().map(String::toUpperCase).collect(toList());
```

## 3. Use Appropriate Functional Interfaces

```java
// Avoid creating unnecessary functional interfaces
@FunctionalInterface
interface StringChecker {
    boolean check(String s);
}

// Use built-in Predicate instead
Predicate<String> checker = s -> s.length() > 5;
```

---

# Performance Considerations

```java
import java.util.*;
import java.util.function.*;
import java.time.Instant;
import java.time.Duration;

public class PerformanceDemo {
    
    public static void measureTime(String description, Runnable operation) {
        Instant start = Instant.now();
        operation.run();
        Instant end = Instant.now();
        Duration duration = Duration.between(start, end);
        System.out.println(description + ": " + duration.toMillis() + "ms");
    }
    
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < 1_000_000; i++) {
            numbers.add(i);
        }
        
        // Traditional for loop
        measureTime("Traditional for loop", () -> {
            List<Integer> evens = new ArrayList<>();
            for (Integer num : numbers) {
                if (num % 2 == 0) {
                    evens.add(num);
                }
            }
        });
        
        // Lambda with stream
        measureTime("Lambda with stream", () -> {
            List<Integer> evens = numbers.stream()
                                        .filter(n -> n % 2 == 0)
                                        .collect(ArrayList::new, 
                                               ArrayList::add, 
                                               ArrayList::addAll);
        });
        
        // Parallel stream
        measureTime("Parallel stream", () -> {
            List<Integer> evens = numbers.parallelStream()
                                        .filter(n -> n % 2 == 0)
                                        .collect(ArrayList::new, 
                                               ArrayList::add, 
                                               ArrayList::addAll);
        });
        
        // Method reference vs lambda performance
        Predicate<Integer> isEvenLambda = n -> n % 2 == 0;
        Predicate<Integer> isEvenMethod = PerformanceDemo::isEven;
        
        measureTime("Lambda predicate", () -> {
            numbers.stream().filter(isEvenLambda).count();
        });
        
        measureTime("Method reference predicate", () -> {
            numbers.stream().filter(isEvenMethod).count();
        });
    }
    
    public static boolean isEven(Integer n) {
        return n % 2 == 0;
    }
}
```

---

# Hands-on Exercise 1: Event Processing System

Create a functional event processing system with the following requirements:

```java
// Event class
class Event {
    private String type;
    private String data;
    private long timestamp;
    
    public Event(String type, String data) {
        this.type = type;
        this.data = data;
        this.timestamp = System.currentTimeMillis();
    }
    
    // Getters
    public String getType() { return type; }
    public String getData() { return data; }
    public long getTimestamp() { return timestamp; }
    
    @Override
    public String toString() {
        return String.format("Event{type='%s', data='%s', timestamp=%d}", 
                           type, data, timestamp);
    }
}

// TODO: Create EventProcessor interface
@FunctionalInterface
interface EventProcessor {
    // TODO: Define process method
}

// TODO: Create EventFilter interface
@FunctionalInterface 
interface EventFilter {
    // TODO: Define filter method
}

// TODO: Implement EventManager class
class EventManager {
    // TODO: Add methods to register processors and filters
    // TODO: Add method to process events
    // TODO: Use functional programming concepts
}
```

Test your implementation with different event types and processors.

---

# Hands-on Exercise 2: Functional Calculator

Implement a calculator using functional programming concepts:

```java
public class FunctionalCalculator {
    
    // TODO: Define Operation functional interface
    @FunctionalInterface
    interface Operation {
        // TODO: Define calculate method
    }
    
    // TODO: Create a map of operation names to Operation implementations
    private static final Map<String, Operation> operations = new HashMap<>();
    
    static {
        // TODO: Initialize operations map with lambda expressions
        // add, subtract, multiply, divide, power, etc.
    }
    
    // TODO: Implement calculate method that takes operation name and operands
    public static double calculate(String operationName, double a, double b) {
        // TODO: Your implementation
    }
    
    // TODO: Implement method to add custom operations
    public static void addOperation(String name, Operation operation) {
        // TODO: Your implementation
    }
    
    // TODO: Implement method to get available operations
    public static Set<String> getAvailableOperations() {
        // TODO: Your implementation
    }
    
    public static void main(String[] args) {
        // TODO: Test your calculator with various operations
        // TODO: Add custom operations using lambdas
    }
}
```

Include error handling and support for custom operations.

---

# Hands-on Exercise 3: Data Processing Pipeline

Create a functional data processing pipeline:

```java
import java.util.*;
import java.util.function.*;

public class DataPipeline<T> {
    
    private List<Function<Stream<T>, Stream<T>>> operations = new ArrayList<>();
    
    // TODO: Implement filter method
    public DataPipeline<T> filter(Predicate<T> predicate) {
        // TODO: Add filter operation to pipeline
        return this;
    }
    
    // TODO: Implement map method
    public <R> DataPipeline<R> map(Function<T, R> mapper) {
        // TODO: Create new pipeline with mapped type
    }
    
    // TODO: Implement sort method
    public DataPipeline<T> sort(Comparator<T> comparator) {
        // TODO: Add sort operation to pipeline
        return this;
    }
    
    // TODO: Implement limit method
    public DataPipeline<T> limit(long maxSize) {
        // TODO: Add limit operation to pipeline
        return this;
    }
    
    // TODO: Implement skip method
    public DataPipeline<T> skip(long n) {
        // TODO: Add skip operation to pipeline
        return this;
    }
    
    // TODO: Implement distinct method
    public DataPipeline<T> distinct() {
        // TODO: Add distinct operation to pipeline
        return this;
    }
    
    // TODO: Implement execute method to run the pipeline
    public List<T> execute(List<T> input) {
        // TODO: Apply all operations in sequence
    }
    
    // TODO: Implement executeToStream method
    public Stream<T> executeToStream(List<T> input) {
        // TODO: Return stream after applying all operations
    }
}
```

Test with various data transformations and operations.

---

# Exercise Solutions: Event Processing System

```java
import java.util.*;
import java.util.function.*;

@FunctionalInterface
interface EventProcessor {
    void process(Event event);
    
    default EventProcessor andThen(EventProcessor after) {
        return event -> {
            this.process(event);
            after.process(event);
        };
    }
}

@FunctionalInterface 
interface EventFilter {
    boolean accept(Event event);
    
    default EventFilter and(EventFilter other) {
        return event -> this.accept(event) && other.accept(event);
    }
    
    default EventFilter or(EventFilter other) {
        return event -> this.accept(event) || other.accept(event);
    }
}

class EventManager {
    private List<EventFilter> filters = new ArrayList<>();
    private List<EventProcessor> processors = new ArrayList<>();
    
    public void addFilter(EventFilter filter) {
        filters.add(filter);
    }
    
    public void addProcessor(EventProcessor processor) {
        processors.add(processor);
    }
    
    public void processEvent(Event event) {
        // Apply all filters
        boolean shouldProcess = filters.stream()
            .allMatch(filter -> filter.accept(event));
        
        if (shouldProcess) {
            // Apply all processors
            processors.forEach(processor -> processor.process(event));
        }
    }
    
    public void processEvents(List<Event> events) {
        events.forEach(this::processEvent);
    }
}

// Usage example
public class EventSystemDemo {
    public static void main(String[] args) {
        EventManager manager = new EventManager();
        
        // Add filters
        manager.addFilter(event -> "ERROR".equals(event.getType()));
        manager.addFilter(event -> event.getData().contains("database"));
        
        // Add processors
        manager.addProcessor(event -> 
            System.out.println("Logging: " + event));
        manager.addProcessor(event -> 
            System.out.println("Alerting administrators about: " + event.getType()));
        
        // Test events
        List<Event> events = Arrays.asList(
            new Event("INFO", "User logged in"),
            new Event("ERROR", "Database connection failed"),
            new Event("WARNING", "High memory usage"),
            new Event("ERROR", "Database timeout occurred")
        );
        
        manager.processEvents(events);
    }
}
```

---

# Summary

## Key Concepts Covered

1. **Functional Programming**: Treating functions as first-class objects
2. **Lambda Expressions**: Concise syntax for anonymous functions
3. **Functional Interfaces**: Interfaces with single abstract method
4. **Built-in Interfaces**: Predicate, Function, Consumer, Supplier
5. **Method References**: Referencing methods without executing them
6. **Constructor References**: Referencing constructors as functions
7. **Function Composition**: Combining functions to create complex operations

## Benefits of Functional Programming

- **Conciseness**: Less boilerplate code
- **Readability**: More expressive code
- **Reusability**: Functions can be composed and reused
- **Testability**: Pure functions are easier to test
- **Parallelization**: Functional code is often easier to parallelize

## When to Use Functional Programming

- Data processing and transformations
- Event handling and filtering
- Collections operations
- Configuration and setup code
- Validation and business rules

---

# Next Lecture Preview

## Lecture 40: Stream API

- Introduction to Java Streams
- Creating and Operating on Streams
- Intermediate and Terminal Operations
- Parallel Streams
- Collectors and Custom Collectors
- Stream Performance and Best Practices

## Preparation

- Practice with lambda expressions and functional interfaces
- Review collections framework
- Understand the concept of lazy evaluation

---

# Thank You!

## Questions and Discussion

- How do lambda expressions improve code readability?
- When would you choose lambda expressions over anonymous classes?
- What are the performance implications of functional programming?

## Resources for Further Learning

- Oracle Java Lambda Tutorial
- Functional Programming in Java by Venkat Subramaniam
- Practice functional programming with different use cases

**Next: Stream API and Functional Data Processing**