---
theme: default
background: https://source.unsplash.com/1024x768/?java,programming
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: Java Programming - Lecture 38
mdc: true
---

# Java Programming
## Lecture 38: Generics in Java
### GTU Diploma in Computer Engineering

---
layout: two-cols
---

# Learning Objectives

After this lecture, you will be able to:

- Understand the concept and benefits of Generics in Java
- Create generic classes, interfaces, and methods
- Work with bounded type parameters and wildcards
- Implement type erasure concepts
- Use generic collections effectively
- Apply generic programming best practices

::right::

# Lecture Overview

1. **Introduction to Generics**
2. **Generic Classes and Interfaces**
3. **Generic Methods**
4. **Bounded Type Parameters**
5. **Wildcards in Generics**
6. **Type Erasure**
7. **Generic Collections**
8. **Best Practices**
9. **Hands-on Exercises**

---

# What are Generics?

Generics enable **type safety** at compile time and eliminate the need for casting.

```java
// Without Generics (Java < 5)
List list = new ArrayList();
list.add("Hello");
String s = (String) list.get(0); // Cast required
```

```java
// With Generics (Java 5+)
List<String> list = new ArrayList<String>();
list.add("Hello");
String s = list.get(0); // No cast needed
```

## Benefits of Generics

1. **Type Safety**: Compile-time type checking
2. **Elimination of Casting**: No explicit casting needed
3. **Code Clarity**: Code is more readable and self-documenting
4. **Performance**: No boxing/unboxing overhead

---

# Generic Classes

Generic classes allow you to create classes that work with different types.

```java
// Generic class definition
public class Container<T> {
    private T item;
    
    public void set(T item) {
        this.item = item;
    }
    
    public T get() {
        return item;
    }
    
    public boolean isEmpty() {
        return item == null;
    }
}
```

```java
// Using generic class
public class GenericClassDemo {
    public static void main(String[] args) {
        // Container for String
        Container<String> stringContainer = new Container<String>();
        stringContainer.set("Hello World");
        String value = stringContainer.get();
        
        // Container for Integer
        Container<Integer> intContainer = new Container<Integer>();
        intContainer.set(42);
        Integer number = intContainer.get();
        
        System.out.println("String: " + value);
        System.out.println("Integer: " + number);
    }
}
```

---

# Multiple Type Parameters

Classes can have multiple generic type parameters.

```java
public class Pair<T, U> {
    private T first;
    private U second;
    
    public Pair(T first, U second) {
        this.first = first;
        this.second = second;
    }
    
    public T getFirst() { return first; }
    public U getSecond() { return second; }
    
    public void setFirst(T first) { this.first = first; }
    public void setSecond(U second) { this.second = second; }
    
    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}
```

```java
public class PairDemo {
    public static void main(String[] args) {
        Pair<String, Integer> nameAge = new Pair<>("Alice", 25);
        Pair<Integer, String> idName = new Pair<>(101, "Bob");
        
        System.out.println("Name-Age: " + nameAge);
        System.out.println("ID-Name: " + idName);
        
        // Accessing elements
        String name = nameAge.getFirst();
        Integer age = nameAge.getSecond();
        
        System.out.println(name + " is " + age + " years old");
    }
}
```

---

# Generic Interfaces

Interfaces can also be generic.

```java
// Generic interface
public interface Repository<T> {
    void save(T entity);
    T findById(int id);
    List<T> findAll();
    boolean delete(T entity);
}
```

```java
// Implementing generic interface
public class StudentRepository implements Repository<Student> {
    private List<Student> students = new ArrayList<>();
    
    @Override
    public void save(Student student) {
        students.add(student);
    }
    
    @Override
    public Student findById(int id) {
        return students.stream()
                      .filter(s -> s.getId() == id)
                      .findFirst()
                      .orElse(null);
    }
    
    @Override
    public List<Student> findAll() {
        return new ArrayList<>(students);
    }
    
    @Override
    public boolean delete(Student student) {
        return students.remove(student);
    }
}
```

---

# Generic Methods

Methods can be generic independently of their class.

```java
public class GenericMethods {
    
    // Generic method to swap array elements
    public static <T> void swap(T[] array, int i, int j) {
        if (i >= 0 && i < array.length && j >= 0 && j < array.length) {
            T temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    
    // Generic method to find element in array
    public static <T> boolean contains(T[] array, T element) {
        for (T item : array) {
            if (item != null && item.equals(element)) {
                return true;
            }
        }
        return false;
    }
    
    // Generic method to convert array to list
    public static <T> List<T> arrayToList(T[] array) {
        List<T> list = new ArrayList<>();
        for (T element : array) {
            list.add(element);
        }
        return list;
    }
}
```

---

# Generic Method Usage

```java
public class GenericMethodDemo {
    public static void main(String[] args) {
        // String array operations
        String[] names = {"Alice", "Bob", "Charlie", "Diana"};
        System.out.println("Original: " + Arrays.toString(names));
        
        GenericMethods.swap(names, 0, 2);
        System.out.println("After swap: " + Arrays.toString(names));
        
        boolean found = GenericMethods.contains(names, "Bob");
        System.out.println("Contains 'Bob': " + found);
        
        // Integer array operations
        Integer[] numbers = {1, 2, 3, 4, 5};
        GenericMethods.swap(numbers, 1, 3);
        System.out.println("Numbers after swap: " + Arrays.toString(numbers));
        
        List<Integer> numberList = GenericMethods.arrayToList(numbers);
        System.out.println("Converted to list: " + numberList);
        
        // Generic method with return type
        String max = findMax("hello", "world");
        Integer maxNum = findMax(10, 20);
        
        System.out.println("Max string: " + max);
        System.out.println("Max number: " + maxNum);
    }
    
    public static <T extends Comparable<T>> T findMax(T a, T b) {
        return a.compareTo(b) > 0 ? a : b;
    }
}
```

---

# Bounded Type Parameters

You can restrict the types that can be used as type arguments.

```java
// Bounded by class (extends)
public class NumberContainer<T extends Number> {
    private T number;
    
    public NumberContainer(T number) {
        this.number = number;
    }
    
    public double getDoubleValue() {
        return number.doubleValue(); // Number method available
    }
    
    public boolean isPositive() {
        return number.doubleValue() > 0;
    }
    
    public T getNumber() {
        return number;
    }
}
```

```java
// Bounded by interface
public class ComparableContainer<T extends Comparable<T>> {
    private List<T> items = new ArrayList<>();
    
    public void add(T item) {
        items.add(item);
    }
    
    public T findMax() {
        if (items.isEmpty()) return null;
        
        T max = items.get(0);
        for (T item : items) {
            if (item.compareTo(max) > 0) {
                max = item;
            }
        }
        return max;
    }
    
    public T findMin() {
        if (items.isEmpty()) return null;
        
        T min = items.get(0);
        for (T item : items) {
            if (item.compareTo(min) < 0) {
                min = item;
            }
        }
        return min;
    }
}
```

---

# Multiple Bounds

A type parameter can have multiple bounds.

```java
// Interface for objects that can be serialized
interface Serializable {
    String serialize();
}

// Interface for objects that can be compared
interface Comparable<T> {
    int compareTo(T other);
}

// Class with multiple bounds
public class DataProcessor<T extends Number & Serializable & Comparable<T>> {
    private List<T> data = new ArrayList<>();
    
    public void addData(T item) {
        data.add(item);
    }
    
    public String serializeAll() {
        StringBuilder sb = new StringBuilder();
        for (T item : data) {
            sb.append(item.serialize()).append("\n");
        }
        return sb.toString();
    }
    
    public T findMaximum() {
        if (data.isEmpty()) return null;
        
        T max = data.get(0);
        for (T item : data) {
            if (item.compareTo(max) > 0) {
                max = item;
            }
        }
        return max;
    }
    
    public double getSum() {
        return data.stream()
                   .mapToDouble(Number::doubleValue)
                   .sum();
    }
}
```

---

# Wildcards in Generics

Wildcards represent unknown types in generics.

## Unbounded Wildcard (?)

```java
public class WildcardDemo {
    
    // Method that accepts list of any type
    public static void printList(List<?> list) {
        for (Object item : list) {
            System.out.println(item);
        }
    }
    
    public static int getListSize(List<?> list) {
        return list.size();
    }
    
    public static void main(String[] args) {
        List<String> stringList = Arrays.asList("A", "B", "C");
        List<Integer> intList = Arrays.asList(1, 2, 3);
        
        printList(stringList);  // Works
        printList(intList);     // Works
        
        System.out.println("String list size: " + getListSize(stringList));
        System.out.println("Integer list size: " + getListSize(intList));
    }
}
```

---

# Upper Bounded Wildcards

Use `? extends Type` for reading from a generic collection.

```java
public class UpperBoundedWildcard {
    
    // Method that calculates sum of numbers
    public static double calculateSum(List<? extends Number> numbers) {
        double sum = 0.0;
        for (Number num : numbers) {
            sum += num.doubleValue();
        }
        return sum;
    }
    
    // Method to find maximum number
    public static double findMax(List<? extends Number> numbers) {
        if (numbers.isEmpty()) {
            throw new IllegalArgumentException("List cannot be empty");
        }
        
        double max = numbers.get(0).doubleValue();
        for (Number num : numbers) {
            if (num.doubleValue() > max) {
                max = num.doubleValue();
            }
        }
        return max;
    }
    
    public static void main(String[] args) {
        List<Integer> integers = Arrays.asList(1, 2, 3, 4, 5);
        List<Double> doubles = Arrays.asList(1.5, 2.7, 3.9);
        List<Float> floats = Arrays.asList(1.1f, 2.2f, 3.3f);
        
        System.out.println("Sum of integers: " + calculateSum(integers));
        System.out.println("Sum of doubles: " + calculateSum(doubles));
        System.out.println("Sum of floats: " + calculateSum(floats));
        
        System.out.println("Max integer: " + findMax(integers));
        System.out.println("Max double: " + findMax(doubles));
        System.out.println("Max float: " + findMax(floats));
    }
}
```

---

# Lower Bounded Wildcards

Use `? super Type` for writing to a generic collection.

```java
public class LowerBoundedWildcard {
    
    // Method to add integers to a collection
    public static void addNumbers(List<? super Integer> numbers) {
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
    }
    
    // Method to copy from source to destination
    public static <T> void copy(List<? extends T> source, 
                                List<? super T> destination) {
        for (T item : source) {
            destination.add(item);
        }
    }
    
    public static void main(String[] args) {
        // Lower bounded wildcard example
        List<Number> numbers = new ArrayList<>();
        List<Object> objects = new ArrayList<>();
        
        addNumbers(numbers);  // Integer is subtype of Number
        addNumbers(objects);  // Integer is subtype of Object
        
        System.out.println("Numbers: " + numbers);
        System.out.println("Objects: " + objects);
        
        // Copy example
        List<String> source = Arrays.asList("A", "B", "C");
        List<Object> destination = new ArrayList<>();
        
        copy(source, destination);
        System.out.println("Destination: " + destination);
        
        // Another copy example
        List<Integer> intSource = Arrays.asList(1, 2, 3);
        List<Number> numberDest = new ArrayList<>();
        
        copy(intSource, numberDest);
        System.out.println("Number destination: " + numberDest);
    }
}
```

---

# PECS Principle

**Producer Extends, Consumer Super** - A guideline for using wildcards.

```java
public class PECSDemo {
    
    // Producer - use extends (reading from collection)
    public static double sumAll(List<? extends Number> numbers) {
        double sum = 0;
        for (Number n : numbers) {  // Reading/Producing
            sum += n.doubleValue();
        }
        return sum;
    }
    
    // Consumer - use super (writing to collection)
    public static void addIntegers(List<? super Integer> numbers) {
        numbers.add(1);  // Writing/Consuming
        numbers.add(2);
        numbers.add(3);
    }
    
    // Complex example: copying with PECS
    public static <T> void copy(List<? extends T> source,    // Producer
                                List<? super T> destination) { // Consumer
        for (T element : source) {      // Reading from source (Producer)
            destination.add(element);   // Writing to destination (Consumer)
        }
    }
    
    public static void main(String[] args) {
        // Producer example
        List<Integer> integers = Arrays.asList(1, 2, 3, 4, 5);
        List<Double> doubles = Arrays.asList(1.1, 2.2, 3.3);
        
        System.out.println("Sum of integers: " + sumAll(integers));
        System.out.println("Sum of doubles: " + sumAll(doubles));
        
        // Consumer example
        List<Number> numbers = new ArrayList<>();
        List<Object> objects = new ArrayList<>();
        
        addIntegers(numbers);
        addIntegers(objects);
        
        System.out.println("Numbers: " + numbers);
        System.out.println("Objects: " + objects);
    }
}
```

---

# Type Erasure

Java implements generics through **type erasure** - generic type information is removed at runtime.

```java
public class TypeErasureDemo {
    
    public static void demonstrateTypeErasure() {
        List<String> stringList = new ArrayList<String>();
        List<Integer> integerList = new ArrayList<Integer>();
        
        // At runtime, both lists have the same class
        System.out.println("String list class: " + stringList.getClass());
        System.out.println("Integer list class: " + integerList.getClass());
        
        // Both print: class java.util.ArrayList
        System.out.println("Are classes equal? " + 
                          stringList.getClass().equals(integerList.getClass()));
    }
    
    // Generic method
    public static <T> void genericMethod(T parameter) {
        System.out.println("Parameter type at runtime: " + 
                          parameter.getClass().getName());
    }
    
    public static void main(String[] args) {
        demonstrateTypeErasure();
        
        genericMethod("Hello");     // String
        genericMethod(42);          // Integer
        genericMethod(3.14);        // Double
        
        // Demonstrating limitations of type erasure
        List<String> list = new ArrayList<>();
        
        // This won't work - cannot check parameterized type
        // if (list instanceof List<String>) { } // Compilation error
        
        // This works - raw type check
        if (list instanceof List) {
            System.out.println("list is a List");
        }
    }
}
```

---

# Generic Collections in Practice

Using generics with Java Collections Framework.

```java
import java.util.*;

public class GenericCollectionsDemo {
    
    public static void main(String[] args) {
        // Generic List
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Orange");
        
        System.out.println("Fruits: " + fruits);
        
        // Generic Set
        Set<Integer> uniqueNumbers = new HashSet<>();
        uniqueNumbers.add(1);
        uniqueNumbers.add(2);
        uniqueNumbers.add(1); // Duplicate - won't be added
        
        System.out.println("Unique numbers: " + uniqueNumbers);
        
        // Generic Map
        Map<String, Integer> ages = new HashMap<>();
        ages.put("Alice", 25);
        ages.put("Bob", 30);
        ages.put("Charlie", 35);
        
        System.out.println("Ages: " + ages);
        
        // Iterating with enhanced for loop
        System.out.println("\nIterating through collections:");
        
        for (String fruit : fruits) {
            System.out.println("Fruit: " + fruit);
        }
        
        for (Integer number : uniqueNumbers) {
            System.out.println("Number: " + number);
        }
        
        for (Map.Entry<String, Integer> entry : ages.entrySet()) {
            System.out.println(entry.getKey() + " is " + entry.getValue() + " years old");
        }
    }
}
```

---

# Advanced Generic Collections

Working with nested generics and complex types.

```java
public class AdvancedGenericCollections {
    
    public static void main(String[] args) {
        // List of Lists
        List<List<String>> matrix = new ArrayList<>();
        matrix.add(Arrays.asList("A1", "A2", "A3"));
        matrix.add(Arrays.asList("B1", "B2", "B3"));
        matrix.add(Arrays.asList("C1", "C2", "C3"));
        
        System.out.println("Matrix:");
        for (List<String> row : matrix) {
            System.out.println(row);
        }
        
        // Map of Lists
        Map<String, List<Integer>> studentGrades = new HashMap<>();
        studentGrades.put("Alice", Arrays.asList(85, 90, 88));
        studentGrades.put("Bob", Arrays.asList(75, 80, 85));
        studentGrades.put("Charlie", Arrays.asList(95, 92, 98));
        
        System.out.println("\nStudent Grades:");
        for (Map.Entry<String, List<Integer>> entry : studentGrades.entrySet()) {
            String student = entry.getKey();
            List<Integer> grades = entry.getValue();
            double average = grades.stream().mapToInt(Integer::intValue).average().orElse(0);
            System.out.println(student + ": " + grades + " (Average: " + average + ")");
        }
        
        // Set of Maps
        Set<Map<String, String>> records = new HashSet<>();
        
        Map<String, String> record1 = new HashMap<>();
        record1.put("name", "Alice");
        record1.put("age", "25");
        records.add(record1);
        
        Map<String, String> record2 = new HashMap<>();
        record2.put("name", "Bob");
        record2.put("age", "30");
        records.add(record2);
        
        System.out.println("\nRecords:");
        for (Map<String, String> record : records) {
            System.out.println(record);
        }
    }
}
```

---

# Generic Best Practices

## 1. Use Meaningful Type Parameter Names

```java
// Poor naming
public class Container<T, U, V> { }

// Better naming
public class DatabaseConnection<Entity, Key, Result> { }

// Common conventions
// T - Type
// E - Element (used by collections)
// K - Key (used by maps)
// V - Value (used by maps)
// N - Number
```

## 2. Favor Generic Types Over Raw Types

```java
// Avoid raw types
List list = new ArrayList(); // Raw type
list.add("Hello");
String s = (String) list.get(0); // Cast required

// Use generic types
List<String> list = new ArrayList<String>();
list.add("Hello");
String s = list.get(0); // No cast needed
```

---

# More Best Practices

## 3. Use Bounded Wildcards for Flexibility

```java
// Too restrictive
public void processNumbers(List<Number> numbers) { }

// More flexible
public void processNumbers(List<? extends Number> numbers) { }
```

## 4. Eliminate Unchecked Warnings

```java
// Causes unchecked warning
Set<String> set = new HashSet();

// Clean - no warnings
Set<String> set = new HashSet<String>();

// Java 7+ Diamond operator
Set<String> set = new HashSet<>();
```

## 5. Prefer Lists to Arrays for Type Safety

```java
// Arrays are covariant - can cause runtime errors
Number[] numbers = new Integer[10];
numbers[0] = 1.5; // Compiles but throws ArrayStoreException at runtime

// Lists with generics are safer
List<Number> numbers = new ArrayList<Integer>(); // Compilation error - caught early
```

---

# Real-World Generic Example: Repository Pattern

```java
// Generic repository interface
public interface Repository<T, ID> {
    T save(T entity);
    Optional<T> findById(ID id);
    List<T> findAll();
    void deleteById(ID id);
    boolean existsById(ID id);
}

// Generic abstract implementation
public abstract class AbstractRepository<T, ID> implements Repository<T, ID> {
    protected Map<ID, T> storage = new HashMap<>();
    
    @Override
    public T save(T entity) {
        ID id = getId(entity);
        storage.put(id, entity);
        return entity;
    }
    
    @Override
    public Optional<T> findById(ID id) {
        return Optional.ofNullable(storage.get(id));
    }
    
    @Override
    public List<T> findAll() {
        return new ArrayList<>(storage.values());
    }
    
    @Override
    public void deleteById(ID id) {
        storage.remove(id);
    }
    
    @Override
    public boolean existsById(ID id) {
        return storage.containsKey(id);
    }
    
    protected abstract ID getId(T entity);
}
```

---

# Repository Implementation Example

```java
// Student entity
public class Student {
    private Long id;
    private String name;
    private String email;
    
    public Student(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
    
    // Getters and setters
    public Long getId() { return id; }
    public String getName() { return name; }
    public String getEmail() { return email; }
    
    @Override
    public String toString() {
        return "Student{id=" + id + ", name='" + name + "', email='" + email + "'}";
    }
}

// Concrete repository implementation
public class StudentRepository extends AbstractRepository<Student, Long> {
    
    @Override
    protected Long getId(Student entity) {
        return entity.getId();
    }
    
    // Additional specific methods
    public List<Student> findByName(String name) {
        return storage.values().stream()
                      .filter(student -> student.getName().equalsIgnoreCase(name))
                      .collect(Collectors.toList());
    }
    
    public Optional<Student> findByEmail(String email) {
        return storage.values().stream()
                      .filter(student -> student.getEmail().equalsIgnoreCase(email))
                      .findFirst();
    }
}
```

---

# Using the Generic Repository

```java
public class RepositoryDemo {
    public static void main(String[] args) {
        StudentRepository repository = new StudentRepository();
        
        // Save students
        Student alice = repository.save(new Student(1L, "Alice", "alice@email.com"));
        Student bob = repository.save(new Student(2L, "Bob", "bob@email.com"));
        Student charlie = repository.save(new Student(3L, "Charlie", "charlie@email.com"));
        
        System.out.println("All students:");
        repository.findAll().forEach(System.out::println);
        
        // Find by ID
        Optional<Student> found = repository.findById(2L);
        if (found.isPresent()) {
            System.out.println("\nFound student: " + found.get());
        }
        
        // Find by name (custom method)
        List<Student> bobs = repository.findByName("Bob");
        System.out.println("\nStudents named Bob: " + bobs);
        
        // Find by email (custom method)
        Optional<Student> studentByEmail = repository.findByEmail("alice@email.com");
        if (studentByEmail.isPresent()) {
            System.out.println("\nStudent with email alice@email.com: " + studentByEmail.get());
        }
        
        // Check existence
        boolean exists = repository.existsById(1L);
        System.out.println("\nStudent with ID 1 exists: " + exists);
        
        // Delete student
        repository.deleteById(2L);
        System.out.println("\nAfter deleting student with ID 2:");
        repository.findAll().forEach(System.out::println);
    }
}
```

---

# Hands-on Exercise 1: Generic Stack Implementation

Create a generic Stack class with the following requirements:

```java
public class GenericStack<T> {
    // TODO: Implement using ArrayList internally
    
    // TODO: Implement push method
    public void push(T item) {
        // Your implementation
    }
    
    // TODO: Implement pop method
    public T pop() {
        // Your implementation
        // Throw EmptyStackException if stack is empty
    }
    
    // TODO: Implement peek method
    public T peek() {
        // Your implementation
        // Throw EmptyStackException if stack is empty
    }
    
    // TODO: Implement isEmpty method
    public boolean isEmpty() {
        // Your implementation
    }
    
    // TODO: Implement size method
    public int size() {
        // Your implementation
    }
    
    // TODO: Override toString method
    @Override
    public String toString() {
        // Your implementation
    }
}
```

Test your implementation with different data types.

---

# Hands-on Exercise 2: Generic Utility Methods

Implement the following generic utility methods:

```java
public class GenericUtils {
    
    // TODO: Implement method to reverse any array
    public static <T> void reverse(T[] array) {
        // Your implementation
    }
    
    // TODO: Implement method to find element in array
    public static <T> int indexOf(T[] array, T element) {
        // Your implementation
        // Return -1 if not found
    }
    
    // TODO: Implement method to get maximum element
    public static <T extends Comparable<T>> T max(T[] array) {
        // Your implementation
        // Throw IllegalArgumentException if array is empty
    }
    
    // TODO: Implement method to filter list based on predicate
    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        // Your implementation
        // Use Predicate functional interface
    }
}
```

Create test cases for each method with different data types.

---

# Hands-on Exercise 3: Generic Cache Implementation

Create a generic LRU (Least Recently Used) cache:

```java
public class LRUCache<K, V> {
    private final int capacity;
    
    // TODO: Use appropriate data structures
    // Hint: Consider using LinkedHashMap or implement with HashMap + doubly linked list
    
    public LRUCache(int capacity) {
        // TODO: Initialize cache with given capacity
    }
    
    public V get(K key) {
        // TODO: Get value and mark as recently used
        // Return null if key doesn't exist
    }
    
    public void put(K key, V value) {
        // TODO: Put key-value pair
        // If at capacity, remove least recently used item
    }
    
    public int size() {
        // TODO: Return current size
    }
    
    public boolean containsKey(K key) {
        // TODO: Check if key exists
    }
    
    public void clear() {
        // TODO: Clear all entries
    }
    
    // TODO: Override toString for debugging
}
```

Test your cache with different key-value types and verify LRU behavior.

---

# Exercise Solutions: Generic Stack

```java
import java.util.*;

public class GenericStack<T> {
    private List<T> elements;
    
    public GenericStack() {
        elements = new ArrayList<>();
    }
    
    public void push(T item) {
        elements.add(item);
    }
    
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return elements.remove(elements.size() - 1);
    }
    
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return elements.get(elements.size() - 1);
    }
    
    public boolean isEmpty() {
        return elements.isEmpty();
    }
    
    public int size() {
        return elements.size();
    }
    
    @Override
    public String toString() {
        return "Stack{" + elements + "}";
    }
}
```

---

# Exercise Solutions: Generic Utilities

```java
import java.util.*;
import java.util.function.Predicate;

public class GenericUtils {
    
    public static <T> void reverse(T[] array) {
        if (array == null) return;
        
        int left = 0;
        int right = array.length - 1;
        
        while (left < right) {
            T temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            left++;
            right--;
        }
    }
    
    public static <T> int indexOf(T[] array, T element) {
        if (array == null) return -1;
        
        for (int i = 0; i < array.length; i++) {
            if (Objects.equals(array[i], element)) {
                return i;
            }
        }
        return -1;
    }
    
    public static <T extends Comparable<T>> T max(T[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Array cannot be null or empty");
        }
        
        T max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] != null && array[i].compareTo(max) > 0) {
                max = array[i];
            }
        }
        return max;
    }
    
    public static <T> List<T> filter(List<T> list, Predicate<T> predicate) {
        List<T> result = new ArrayList<>();
        for (T element : list) {
            if (predicate.test(element)) {
                result.add(element);
            }
        }
        return result;
    }
}
```

---

# Performance Considerations

## Generic Collections Performance

```java
import java.util.*;

public class GenericPerformanceDemo {
    
    public static void demonstrateAutoboxing() {
        long startTime, endTime;
        
        // Test with raw ArrayList (boxing overhead)
        List rawList = new ArrayList();
        startTime = System.nanoTime();
        for (int i = 0; i < 1000000; i++) {
            rawList.add(i); // Boxing: int -> Integer
        }
        endTime = System.nanoTime();
        System.out.println("Raw list (with boxing): " + (endTime - startTime) + " ns");
        
        // Test with generic ArrayList
        List<Integer> genericList = new ArrayList<>();
        startTime = System.nanoTime();
        for (int i = 0; i < 1000000; i++) {
            genericList.add(i); // Boxing: int -> Integer
        }
        endTime = System.nanoTime();
        System.out.println("Generic list: " + (endTime - startTime) + " ns");
        
        // Test with primitive array (no boxing)
        int[] primitiveArray = new int[1000000];
        startTime = System.nanoTime();
        for (int i = 0; i < 1000000; i++) {
            primitiveArray[i] = i; // No boxing
        }
        endTime = System.nanoTime();
        System.out.println("Primitive array: " + (endTime - startTime) + " ns");
    }
    
    public static void main(String[] args) {
        demonstrateAutoboxing();
    }
}
```

---

# Common Generic Pitfalls

## 1. Generic Array Creation

```java
public class GenericPitfalls {
    
    // This won't compile - cannot create generic arrays
    // T[] array = new T[10]; // Compilation error
    
    // Workaround 1: Use Object array and cast (unsafe)
    @SuppressWarnings("unchecked")
    public static <T> T[] createArray(int size) {
        return (T[]) new Object[size];
    }
    
    // Workaround 2: Use reflection (safer but requires Class parameter)
    public static <T> T[] createArrayReflection(Class<T> type, int size) {
        return (T[]) Array.newInstance(type, size);
    }
    
    // Best practice: Use List instead of array
    public static <T> List<T> createList(int initialCapacity) {
        return new ArrayList<>(initialCapacity);
    }
}
```

## 2. Static Context and Generics

```java
public class StaticGenericPitfall<T> {
    
    // This won't compile - static context can't access type parameters
    // private static T staticField; // Compilation error
    
    // This works - static generic method
    public static <U> void staticGenericMethod(U parameter) {
        System.out.println("Parameter: " + parameter);
    }
}
```

---

# Summary

## Key Concepts Covered

1. **Generic Classes and Interfaces**: Type-safe containers and contracts
2. **Generic Methods**: Methods that work with different types
3. **Bounded Type Parameters**: Restricting generic types
4. **Wildcards**: Flexible type handling with ?, extends, and super
5. **Type Erasure**: Runtime behavior of generics
6. **PECS Principle**: Producer Extends, Consumer Super
7. **Best Practices**: Writing clean, safe generic code

## Benefits of Generics

- **Type Safety**: Compile-time error detection
- **Code Reusability**: Same code works with different types
- **Performance**: Elimination of casting overhead
- **Clarity**: Self-documenting code

## When to Use Generics

- Collections and data structures
- Utility methods that work with multiple types
- APIs that need type safety
- Framework and library development

---

# Next Lecture Preview

## Lecture 39: Lambda Expressions and Functional Interfaces

- Introduction to Functional Programming in Java
- Lambda Expression Syntax
- Method References
- Built-in Functional Interfaces
- Custom Functional Interfaces
- Functional Programming Patterns

## Preparation

- Review interfaces and anonymous classes
- Practice with generic collections
- Understand the concept of functions as first-class objects

---

# Thank You!

## Questions and Discussion

- How do generics improve code safety and maintainability?
- When would you choose wildcards over specific type parameters?
- What are the trade-offs between generic collections and arrays?

## Resources for Further Learning

- Oracle Java Generics Tutorial
- Effective Java by Joshua Bloch (Chapter on Generics)
- Practice generic programming with different data structures

**Next: Lambda Expressions and Functional Programming**