---
theme: default
background: https://source.unsplash.com/1024x768/?collection,framework
title: Collections Framework Overview
info: |
  ## Java Programming (4343203)
  
  Lecture 34: Collections Framework Overview
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about Java Collections Framework, its hierarchy, core interfaces, and when to use different collection types.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Collections Framework Overview
## Lecture 34

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

- 🏗️ **Understand** the Java Collections Framework architecture
- 📊 **Identify** core collection interfaces and their relationships
- 🔄 **Differentiate** between Collection types: List, Set, Queue, Map
- ⚡ **Choose** appropriate collection implementations for different scenarios
- 🎯 **Use** generic collections for type safety
- 📈 **Compare** performance characteristics of different collections
- 🔧 **Apply** iterators and enhanced for loops with collections
- 💡 **Implement** best practices for collection usage

</v-clicks>

---
layout: default
---

# Introduction to Collections Framework

<div class="grid grid-cols-2 gap-6">

<div>

## What is Collections Framework?

The **Java Collections Framework** is a unified architecture for representing and manipulating collections of objects. It provides:

- **Interfaces**: Abstract data types representing collections
- **Implementations**: Concrete implementations of collection interfaces  
- **Algorithms**: Methods for searching and sorting collections

## Why Collections Framework?

### Before Collections (Legacy)
```java
// Array limitations
int[] numbers = new int[10]; // Fixed size
String[] names = new String[5]; // Type specific

// Vector and Hashtable (synchronized, heavy)
Vector<String> vector = new Vector<>();
Hashtable<String, Integer> table = new Hashtable<>();
```

### With Collections Framework
```java
// Dynamic size, generic type safety
List<String> names = new ArrayList<>();
Set<Integer> numbers = new HashSet<>();
Map<String, Integer> scores = new HashMap<>();

// Flexible and efficient
names.add("John");
numbers.add(42);
scores.put("Alice", 95);
```

## Key Benefits

### 1. **Reduces Programming Effort**
- Standard data structures and algorithms
- No need to implement basic structures

### 2. **Increases Performance**
- Optimized implementations
- Better than custom implementations

### 3. **Provides Type Safety**
- Generic support prevents ClassCastException
- Compile-time type checking

### 4. **Promotes Reusability**
- Common interfaces allow interoperability
- Polymorphic programming

</div>

<div>

## Collections Framework Hierarchy

```
Collection<E> (Interface)
├── List<E> (Interface)
│   ├── ArrayList<E>
│   ├── LinkedList<E>
│   ├── Vector<E>
│   └── Stack<E>
├── Set<E> (Interface)
│   ├── HashSet<E>
│   ├── LinkedHashSet<E>
│   └── SortedSet<E> (Interface)
│       └── TreeSet<E>
└── Queue<E> (Interface)
    ├── PriorityQueue<E>
    ├── LinkedList<E>
    └── Deque<E> (Interface)
        ├── ArrayDeque<E>
        └── LinkedList<E>

Map<K,V> (Interface) - Not part of Collection
├── HashMap<K,V>
├── LinkedHashMap<K,V>
├── Hashtable<K,V>
└── SortedMap<K,V> (Interface)
    └── TreeMap<K,V>
```

## Core Collection Interfaces

### Collection&lt;E&gt;
- Root interface of collection hierarchy
- Basic operations: add, remove, contains, size
- Iterable support

### List&lt;E&gt;
- Ordered collection (sequence)
- Allows duplicates
- Index-based access

### Set&lt;E&gt;
- No duplicate elements
- Mathematical set abstraction
- Unique elements only

### Queue&lt;E&gt;
- Elements processed in specific order
- FIFO (First In, First Out) typically
- Head and tail operations

### Map&lt;K,V&gt;
- Key-value pair associations
- No duplicate keys
- Dictionary/associative array

</div>

</div>

---
layout: default
---

# Collection Interface Deep Dive

<div class="grid grid-cols-2 gap-6">

<div>

## Collection Interface Methods

### Basic Operations
```java
import java.util.*;

public class CollectionBasicsDemo {
    public static void main(String[] args) {
        demonstrateBasicOperations();
        demonstrateBulkOperations();
        demonstrateArrayOperations();
        demonstrateIterationMethods();
    }
    
    private static void demonstrateBasicOperations() {
        System.out.println("=== Basic Collection Operations ===");
        
        Collection<String> collection = new ArrayList<>();
        
        // Adding elements
        collection.add("Java");
        collection.add("Python");
        collection.add("JavaScript");
        collection.add("Java"); // Duplicates allowed in ArrayList
        
        System.out.println("Collection: " + collection);
        System.out.println("Size: " + collection.size());
        System.out.println("Is empty: " + collection.isEmpty());
        
        // Checking elements
        System.out.println("Contains 'Java': " + collection.contains("Java"));
        System.out.println("Contains 'C++': " + collection.contains("C++"));
        
        // Removing elements
        boolean removed = collection.remove("Python");
        System.out.println("Removed 'Python': " + removed);
        System.out.println("Collection after removal: " + collection);
        
        // Clear all elements
        Collection<String> tempCollection = new ArrayList<>(collection);
        tempCollection.clear();
        System.out.println("After clear: " + tempCollection);
        System.out.println("Is empty after clear: " + tempCollection.isEmpty());
    }
    
    private static void demonstrateBulkOperations() {
        System.out.println("\n=== Bulk Operations ===");
        
        Collection<Integer> numbers1 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        Collection<Integer> numbers2 = new ArrayList<>(Arrays.asList(4, 5, 6, 7, 8));
        Collection<Integer> numbers3 = new ArrayList<>(Arrays.asList(1, 2, 3));
        
        System.out.println("Numbers1: " + numbers1);
        System.out.println("Numbers2: " + numbers2);
        System.out.println("Numbers3: " + numbers3);
        
        // containsAll - checks if all elements of specified collection are present
        System.out.println("Numbers1 contains all of Numbers3: " + 
                          numbers1.containsAll(numbers3));
        System.out.println("Numbers1 contains all of Numbers2: " + 
                          numbers1.containsAll(numbers2));
        
        // addAll - adds all elements from specified collection
        Collection<Integer> combined = new ArrayList<>(numbers1);
        combined.addAll(numbers2);
        System.out.println("After addAll(numbers2): " + combined);
        
        // removeAll - removes all elements that are also in specified collection
        Collection<Integer> difference = new ArrayList<>(numbers1);
        difference.removeAll(numbers2);
        System.out.println("Numbers1 removeAll Numbers2: " + difference);
        
        // retainAll - keeps only elements that are also in specified collection
        Collection<Integer> intersection = new ArrayList<>(numbers1);
        intersection.retainAll(numbers2);
        System.out.println("Numbers1 retainAll Numbers2 (intersection): " + intersection);
    }
    
    private static void demonstrateArrayOperations() {
        System.out.println("\n=== Array Operations ===");
        
        Collection<String> languages = new ArrayList<>();
        languages.add("Java");
        languages.add("Python");
        languages.add("JavaScript");
        languages.add("C++");
        
        // toArray() - returns Object[]
        Object[] objectArray = languages.toArray();
        System.out.println("Object array: " + Arrays.toString(objectArray));
        
        // toArray(T[]) - returns typed array
        String[] stringArray = languages.toArray(new String[0]);
        System.out.println("String array: " + Arrays.toString(stringArray));
        
        // Using pre-sized array
        String[] preSizedArray = new String[languages.size()];
        languages.toArray(preSizedArray);
        System.out.println("Pre-sized array: " + Arrays.toString(preSizedArray));
        
        // Converting array back to collection
        Collection<String> fromArray = Arrays.asList(stringArray);
        System.out.println("From array to collection: " + fromArray);
    }
    
    private static void demonstrateIterationMethods() {
        System.out.println("\n=== Iteration Methods ===");
        
        Collection<Integer> numbers = new ArrayList<>(Arrays.asList(10, 20, 30, 40, 50));
        
        // Enhanced for loop (for-each)
        System.out.print("Enhanced for loop: ");
        for (Integer number : numbers) {
            System.out.print(number + " ");
        }
        System.out.println();
        
        // Iterator
        System.out.print("Iterator: ");
        Iterator<Integer> iterator = numbers.iterator();
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println();
        
        // Stream API (Java 8+)
        System.out.print("Stream forEach: ");
        numbers.stream().forEach(num -> System.out.print(num + " "));
        System.out.println();
        
        // Collection forEach (Java 8+)
        System.out.print("Collection forEach: ");
        numbers.forEach(num -> System.out.print(num + " "));
        System.out.println();
    }
}
```

</div>

<div>

## Iterator Pattern

### Iterator Interface
```java
public class IteratorDemo {
    public static void main(String[] args) {
        demonstrateIterator();
        demonstrateListIterator();
        demonstrateSafeRemoval();
        demonstrateIteratorComparison();
    }
    
    private static void demonstrateIterator() {
        System.out.println("=== Basic Iterator ===");
        
        List<String> fruits = new ArrayList<>(Arrays.asList(
            "Apple", "Banana", "Cherry", "Date", "Elderberry"));
        
        System.out.println("Original list: " + fruits);
        
        // Basic iterator usage
        Iterator<String> iterator = fruits.iterator();
        System.out.print("Using iterator: ");
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            System.out.print(fruit + " ");
        }
        System.out.println();
        
        // Iterator methods
        iterator = fruits.iterator();
        System.out.println("Iterator hasNext(): " + iterator.hasNext());
        if (iterator.hasNext()) {
            System.out.println("First element: " + iterator.next());
            System.out.println("After next(), hasNext(): " + iterator.hasNext());
        }
    }
    
    private static void demonstrateListIterator() {
        System.out.println("\n=== ListIterator ===");
        
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Original list: " + numbers);
        
        ListIterator<Integer> listIterator = numbers.listIterator();
        
        // Forward iteration with modification
        System.out.print("Forward with modification: ");
        while (listIterator.hasNext()) {
            Integer num = listIterator.next();
            listIterator.set(num * 2); // Double each number
            System.out.print(num + "->" + (num * 2) + " ");
        }
        System.out.println();
        System.out.println("Modified list: " + numbers);
        
        // Backward iteration
        System.out.print("Backward iteration: ");
        while (listIterator.hasPrevious()) {
            System.out.print(listIterator.previous() + " ");
        }
        System.out.println();
        
        // Adding elements during iteration
        listIterator = numbers.listIterator();
        listIterator.next(); // Move to index 1
        listIterator.add(99); // Add between first and second element
        System.out.println("After adding 99: " + numbers);
        
        // Index information
        listIterator = numbers.listIterator(2); // Start from index 2
        System.out.println("Starting from index 2:");
        System.out.println("Next index: " + listIterator.nextIndex());
        System.out.println("Previous index: " + listIterator.previousIndex());
    }
    
    private static void demonstrateSafeRemoval() {
        System.out.println("\n=== Safe Element Removal ===");
        
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        System.out.println("Original list: " + numbers);
        
        // WRONG WAY - ConcurrentModificationException
        try {
            System.out.println("Attempting unsafe removal (will fail):");
            List<Integer> unsafeList = new ArrayList<>(numbers);
            for (Integer num : unsafeList) {
                if (num % 2 == 0) {
                    unsafeList.remove(num); // This will throw exception
                }
            }
        } catch (ConcurrentModificationException e) {
            System.out.println("ConcurrentModificationException caught: " + e.getClass().getSimpleName());
        }
        
        // CORRECT WAY - Using iterator
        System.out.println("Safe removal using iterator:");
        List<Integer> safeList = new ArrayList<>(numbers);
        Iterator<Integer> iterator = safeList.iterator();
        while (iterator.hasNext()) {
            Integer num = iterator.next();
            if (num % 2 == 0) {
                iterator.remove(); // Safe removal
                System.out.println("Removed: " + num);
            }
        }
        System.out.println("After safe removal: " + safeList);
        
        // Alternative: removeIf (Java 8+)
        System.out.println("Using removeIf:");
        List<Integer> removeIfList = new ArrayList<>(numbers);
        removeIfList.removeIf(num -> num % 3 == 0);
        System.out.println("After removeIf (multiples of 3): " + removeIfList);
    }
    
    private static void demonstrateIteratorComparison() {
        System.out.println("\n=== Iterator vs Enhanced For Loop ===");
        
        List<String> items = new ArrayList<>(Arrays.asList("A", "B", "C", "D", "E"));
        
        // Performance comparison for different operations
        System.out.println("Original list: " + items);
        
        // 1. Simple iteration (both are equivalent)
        long startTime = System.nanoTime();
        for (String item : items) {
            // Process item
        }
        long enhancedForTime = System.nanoTime() - startTime;
        
        startTime = System.nanoTime();
        Iterator<String> iter = items.iterator();
        while (iter.hasNext()) {
            String item = iter.next();
            // Process item
        }
        long iteratorTime = System.nanoTime() - startTime;
        
        System.out.println("Enhanced for loop time: " + enhancedForTime + " ns");
        System.out.println("Iterator time: " + iteratorTime + " ns");
        
        // 2. When you need to modify during iteration
        System.out.println("\nWhen modification is needed:");
        System.out.println("Enhanced for loop: Cannot modify safely");
        System.out.println("Iterator: Can remove safely with iterator.remove()");
        
        // 3. When you need index information
        System.out.println("\nWhen index information is needed:");
        System.out.println("Enhanced for loop: Index not directly available");
        System.out.println("ListIterator: Provides nextIndex() and previousIndex()");
        
        // Demonstrate ListIterator index methods
        ListIterator<String> listIter = items.listIterator();
        while (listIter.hasNext()) {
            System.out.println("Index " + listIter.nextIndex() + ": " + listIter.next());
        }
    }
}
```

### Fail-Fast vs Fail-Safe Iterators
```java
public class IteratorBehaviorDemo {
    public static void main(String[] args) {
        demonstrateFailFast();
        demonstrateFailSafe();
        demonstrateConcurrentModification();
    }
    
    private static void demonstrateFailFast() {
        System.out.println("=== Fail-Fast Iterator ===");
        
        List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C", "D"));
        System.out.println("Original list: " + list);
        
        Iterator<String> iterator = list.iterator();
        
        // This will work fine
        System.out.println("First element: " + iterator.next());
        
        // Modify collection after creating iterator
        list.add("E"); // Modification detected
        
        try {
            System.out.println("Trying to access next element after modification...");
            iterator.next(); // This will throw ConcurrentModificationException
        } catch (ConcurrentModificationException e) {
            System.out.println("ConcurrentModificationException: Fail-fast iterator detected modification");
        }
    }
    
    private static void demonstrateFailSafe() {
        System.out.println("\n=== Fail-Safe Iterator (CopyOnWriteArrayList) ===");
        
        List<String> list = new java.util.concurrent.CopyOnWriteArrayList<>(
            Arrays.asList("A", "B", "C", "D"));
        System.out.println("Original list: " + list);
        
        Iterator<String> iterator = list.iterator();
        
        System.out.println("First element: " + iterator.next());
        
        // Modify collection after creating iterator
        list.add("E"); // No exception will be thrown
        
        System.out.println("List after modification: " + list);
        System.out.println("Continuing iteration:");
        while (iterator.hasNext()) {
            System.out.print(iterator.next() + " ");
        }
        System.out.println("\nNote: Iterator shows snapshot at creation time, doesn't see 'E'");
    }
    
    private static void demonstrateConcurrentModification() {
        System.out.println("\n=== Avoiding Concurrent Modification ===");
        
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
        System.out.println("Original: " + numbers);
        
        // Method 1: Use iterator for safe removal
        List<Integer> method1 = new ArrayList<>(numbers);
        Iterator<Integer> iter = method1.iterator();
        while (iter.hasNext()) {
            if (iter.next() % 2 == 0) {
                iter.remove();
            }
        }
        System.out.println("Method 1 (iterator removal): " + method1);
        
        // Method 2: Use removeIf
        List<Integer> method2 = new ArrayList<>(numbers);
        method2.removeIf(n -> n % 2 == 0);
        System.out.println("Method 2 (removeIf): " + method2);
        
        // Method 3: Collect items to remove, then remove them
        List<Integer> method3 = new ArrayList<>(numbers);
        List<Integer> toRemove = new ArrayList<>();
        for (Integer num : method3) {
            if (num % 2 == 0) {
                toRemove.add(num);
            }
        }
        method3.removeAll(toRemove);
        System.out.println("Method 3 (collect then remove): " + method3);
        
        // Method 4: Reverse iteration for index-based removal
        List<Integer> method4 = new ArrayList<>(numbers);
        for (int i = method4.size() - 1; i >= 0; i--) {
            if (method4.get(i) % 2 == 0) {
                method4.remove(i);
            }
        }
        System.out.println("Method 4 (reverse iteration): " + method4);
    }
}
```

</div>

</div>

---
layout: default
---

# Generics in Collections

<div class="grid grid-cols-2 gap-6">

<div>

## Type Safety with Generics

### Before Generics (Raw Types)
```java
public class PreGenericsDemo {
    public static void main(String[] args) {
        demonstrateRawTypes();
        demonstrateTypeProblems();
    }
    
    @SuppressWarnings({"unchecked", "rawtypes"})
    private static void demonstrateRawTypes() {
        System.out.println("=== Raw Types (Pre-Generics) ===");
        
        // Raw type - no type safety
        List rawList = new ArrayList();
        
        // Can add any type of object
        rawList.add("String");
        rawList.add(42);
        rawList.add(new Date());
        rawList.add(true);
        
        System.out.println("Raw list: " + rawList);
        
        // No compile-time type checking
        Object item1 = rawList.get(0);  // Must cast
        Object item2 = rawList.get(1);  // Must cast
        
        // Unsafe casting - could cause ClassCastException
        try {
            String str1 = (String) item1;  // OK
            String str2 = (String) item2;  // Runtime exception!
        } catch (ClassCastException e) {
            System.out.println("ClassCastException: Cannot cast Integer to String");
        }
    }
    
    @SuppressWarnings({"unchecked", "rawtypes"})
    private static void demonstrateTypeProblems() {
        System.out.println("\n=== Type Problems with Raw Types ===");
        
        List rawNumbers = new ArrayList();
        rawNumbers.add(1);
        rawNumbers.add(2);
        rawNumbers.add("three"); // Oops! String in number list
        rawNumbers.add(4);
        
        System.out.println("Mixed type list: " + rawNumbers);
        
        // Attempting to process as numbers
        int sum = 0;
        for (Object obj : rawNumbers) {
            try {
                sum += (Integer) obj;
            } catch (ClassCastException e) {
                System.out.println("Error processing: " + obj + 
                                 " (type: " + obj.getClass().getSimpleName() + ")");
            }
        }
        
        System.out.println("Sum of numbers: " + sum);
    }
}
```

### With Generics (Type Safe)
```java
public class GenericsDemo {
    public static void main(String[] args) {
        demonstrateTypeSafety();
        demonstrateGenericMethods();
        demonstrateWildcards();
        demonstrateBoundedTypes();
    }
    
    private static void demonstrateTypeSafety() {
        System.out.println("=== Type Safety with Generics ===");
        
        // Generic type - compile-time type safety
        List<String> stringList = new ArrayList<>();
        
        // Can only add Strings
        stringList.add("Java");
        stringList.add("Python");
        stringList.add("JavaScript");
        // stringList.add(42);  // Compile-time error!
        
        System.out.println("String list: " + stringList);
        
        // No casting needed
        String firstItem = stringList.get(0);  // No cast required
        System.out.println("First item: " + firstItem + 
                          " (length: " + firstItem.length() + ")");
        
        // Type-safe iteration
        for (String language : stringList) {
            System.out.println("Language: " + language.toUpperCase());
        }
        
        // Different generic types
        List<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        
        int sum = numbers.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Sum: " + sum);
        
        // Generic Map
        Map<String, Integer> scores = new HashMap<>();
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        
        System.out.println("Scores: " + scores);
        System.out.println("Alice's score: " + scores.get("Alice"));
    }
    
    private static void demonstrateGenericMethods() {
        System.out.println("\n=== Generic Methods ===");
        
        // Generic method for swapping elements
        List<String> names = new ArrayList<>(Arrays.asList("John", "Jane", "Bob"));
        System.out.println("Before swap: " + names);
        swap(names, 0, 2);
        System.out.println("After swap: " + names);
        
        // Generic method works with different types
        List<Integer> numbers = new ArrayList<>(Arrays.asList(10, 20, 30));
        System.out.println("Before swap: " + numbers);
        swap(numbers, 0, 1);
        System.out.println("After swap: " + numbers);
        
        // Generic method for finding element
        int index = findIndex(names, "Jane");
        System.out.println("Index of 'Jane': " + index);
        
        // Generic utility methods
        List<String> fruits = Arrays.asList("Apple", "Banana", "Cherry");
        String[] fruitArray = toArray(fruits, new String[0]);
        System.out.println("Converted to array: " + Arrays.toString(fruitArray));
    }
    
    // Generic method to swap elements
    public static <T> void swap(List<T> list, int i, int j) {
        T temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }
    
    // Generic method to find index
    public static <T> int findIndex(List<T> list, T element) {
        return list.indexOf(element);
    }
    
    // Generic method to convert to array
    public static <T> T[] toArray(List<T> list, T[] array) {
        return list.toArray(array);
    }
    
    private static void demonstrateWildcards() {
        System.out.println("\n=== Wildcards ===");
        
        List<Integer> integers = Arrays.asList(1, 2, 3, 4, 5);
        List<Double> doubles = Arrays.asList(1.1, 2.2, 3.3, 4.4, 5.5);
        List<String> strings = Arrays.asList("A", "B", "C");
        
        // Unbounded wildcard
        printList(integers);
        printList(doubles);
        printList(strings);
        
        // Upper bounded wildcard
        System.out.println("Sum of integers: " + sumNumbers(integers));
        System.out.println("Sum of doubles: " + sumNumbers(doubles));
        
        // Lower bounded wildcard
        List<Number> numbers = new ArrayList<>();
        addNumbers(numbers);
        System.out.println("Numbers list: " + numbers);
    }
    
    // Unbounded wildcard - can read any type
    public static void printList(List<?> list) {
        System.out.print("List contents: ");
        for (Object item : list) {
            System.out.print(item + " ");
        }
        System.out.println();
    }
    
    // Upper bounded wildcard - can read Number or its subtypes
    public static double sumNumbers(List<? extends Number> numbers) {
        double sum = 0.0;
        for (Number num : numbers) {
            sum += num.doubleValue();
        }
        return sum;
    }
    
    // Lower bounded wildcard - can add Number or its subtypes
    public static void addNumbers(List<? super Number> numbers) {
        numbers.add(42);        // Integer
        numbers.add(3.14);      // Double
        numbers.add(7L);        // Long
    }
    
    private static void demonstrateBoundedTypes() {
        System.out.println("\n=== Bounded Type Parameters ===");
        
        List<Integer> integerList = Arrays.asList(5, 2, 8, 1, 9);
        List<String> stringList = Arrays.asList("Zebra", "Apple", "Banana");
        
        System.out.println("Original integer list: " + integerList);
        System.out.println("Max integer: " + findMax(integerList));
        
        System.out.println("Original string list: " + stringList);
        System.out.println("Max string: " + findMax(stringList));
        
        // Demonstrate custom comparable class
        List<Person> people = Arrays.asList(
            new Person("Alice", 30),
            new Person("Bob", 25),
            new Person("Charlie", 35)
        );
        
        System.out.println("People list: " + people);
        System.out.println("Oldest person: " + findMax(people));
    }
    
    // Bounded type parameter - T must implement Comparable
    public static <T extends Comparable<T>> T findMax(List<T> list) {
        if (list.isEmpty()) {
            return null;
        }
        
        T max = list.get(0);
        for (T item : list) {
            if (item.compareTo(max) > 0) {
                max = item;
            }
        }
        return max;
    }
    
    // Example class implementing Comparable
    static class Person implements Comparable<Person> {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        @Override
        public int compareTo(Person other) {
            return Integer.compare(this.age, other.age);
        }
        
        @Override
        public String toString() {
            return name + "(" + age + ")";
        }
    }
}
```

</div>

<div>

## Generic Collections Best Practices

### Diamond Operator (Java 7+)
```java
public class DiamondOperatorDemo {
    public static void main(String[] args) {
        demonstrateDiamondOperator();
        demonstrateNestedGenerics();
        demonstrateMethodReferences();
    }
    
    private static void demonstrateDiamondOperator() {
        System.out.println("=== Diamond Operator ===");
        
        // Before Java 7 - redundant type specification
        List<String> oldWay = new ArrayList<String>();
        Map<String, List<Integer>> oldWayMap = 
            new HashMap<String, List<Integer>>();
        
        // Java 7+ Diamond operator - type inference
        List<String> newWay = new ArrayList<>();
        Map<String, List<Integer>> newWayMap = new HashMap<>();
        
        // Examples
        newWay.add("Java");
        newWay.add("Generics");
        
        newWayMap.put("numbers", Arrays.asList(1, 2, 3, 4, 5));
        newWayMap.put("primes", Arrays.asList(2, 3, 5, 7, 11));
        
        System.out.println("List: " + newWay);
        System.out.println("Map: " + newWayMap);
        
        // Complex nested types
        List<Map<String, Set<Integer>>> complexStructure = new ArrayList<>();
        Map<String, Set<Integer>> mapItem = new HashMap<>();
        mapItem.put("evens", new HashSet<>(Arrays.asList(2, 4, 6, 8)));
        mapItem.put("odds", new HashSet<>(Arrays.asList(1, 3, 5, 7)));
        complexStructure.add(mapItem);
        
        System.out.println("Complex structure: " + complexStructure);
    }
    
    private static void demonstrateNestedGenerics() {
        System.out.println("\n=== Nested Generics ===");
        
        // List of Lists
        List<List<String>> matrix = new ArrayList<>();
        matrix.add(Arrays.asList("A1", "A2", "A3"));
        matrix.add(Arrays.asList("B1", "B2", "B3"));
        matrix.add(Arrays.asList("C1", "C2", "C3"));
        
        System.out.println("Matrix:");
        for (int i = 0; i < matrix.size(); i++) {
            System.out.println("Row " + (i + 1) + ": " + matrix.get(i));
        }
        
        // Map of Lists
        Map<String, List<Integer>> groupedNumbers = new HashMap<>();
        groupedNumbers.put("small", Arrays.asList(1, 2, 3, 4, 5));
        groupedNumbers.put("medium", Arrays.asList(10, 20, 30, 40, 50));
        groupedNumbers.put("large", Arrays.asList(100, 200, 300, 400, 500));
        
        System.out.println("\nGrouped numbers:");
        for (Map.Entry<String, List<Integer>> entry : groupedNumbers.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        
        // Set of Maps
        Set<Map<String, Object>> recordSet = new HashSet<>();
        
        Map<String, Object> person1 = new HashMap<>();
        person1.put("name", "John");
        person1.put("age", 30);
        person1.put("skills", Arrays.asList("Java", "Python"));
        
        Map<String, Object> person2 = new HashMap<>();
        person2.put("name", "Alice");
        person2.put("age", 25);
        person2.put("skills", Arrays.asList("JavaScript", "React"));
        
        recordSet.add(person1);
        recordSet.add(person2);
        
        System.out.println("\nRecord set:");
        for (Map<String, Object> record : recordSet) {
            System.out.println(record);
        }
    }
    
    private static void demonstrateMethodReferences() {
        System.out.println("\n=== Method References with Generics ===");
        
        List<String> words = Arrays.asList("java", "generics", "collections", "framework");
        
        // Method reference with generics
        System.out.println("Original words: " + words);
        
        // Convert to uppercase using method reference
        List<String> upperWords = words.stream()
            .map(String::toUpperCase)
            .collect(Collectors.toList());
        System.out.println("Uppercase words: " + upperWords);
        
        // Filter and collect
        List<String> longWords = words.stream()
            .filter(word -> word.length() > 5)
            .collect(Collectors.toList());
        System.out.println("Long words (>5 chars): " + longWords);
        
        // Complex processing
        Map<Integer, List<String>> wordsByLength = words.stream()
            .collect(Collectors.groupingBy(String::length));
        System.out.println("Words grouped by length: " + wordsByLength);
        
        // Custom functional interface
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        List<Integer> processed = processNumbers(numbers, x -> x * x); // Square
        System.out.println("Squared numbers: " + processed);
        
        processed = processNumbers(numbers, x -> x * 2 + 1); // Transform
        System.out.println("Transformed (2x+1): " + processed);
    }
    
    // Generic method with functional interface
    public static <T, R> List<R> processNumbers(List<T> input, java.util.function.Function<T, R> processor) {
        return input.stream()
            .map(processor)
            .collect(Collectors.toList());
    }
}
```

### Common Generic Patterns
```java
public class GenericPatternsDemo {
    public static void main(String[] args) {
        demonstrateBuilderPattern();
        demonstrateFactoryPattern();
        demonstrateUtilityMethods();
    }
    
    private static void demonstrateBuilderPattern() {
        System.out.println("=== Generic Builder Pattern ===");
        
        // Using generic builder
        GenericBuilder<Person> personBuilder = new GenericBuilder<>(Person::new)
            .with(Person::setName, "John Doe")
            .with(Person::setAge, 30)
            .with(Person::setEmail, "john.doe@example.com");
        
        Person person = personBuilder.build();
        System.out.println("Built person: " + person);
        
        // Building a different type
        GenericBuilder<Product> productBuilder = new GenericBuilder<>(Product::new)
            .with(Product::setName, "Laptop")
            .with(Product::setPrice, 999.99)
            .with(Product::setCategory, "Electronics");
        
        Product product = productBuilder.build();
        System.out.println("Built product: " + product);
    }
    
    private static void demonstrateFactoryPattern() {
        System.out.println("\n=== Generic Factory Pattern ===");
        
        // Generic factory for collections
        CollectionFactory factory = new CollectionFactory();
        
        List<String> arrayList = factory.createList("ArrayList");
        List<String> linkedList = factory.createList("LinkedList");
        
        arrayList.addAll(Arrays.asList("A", "B", "C"));
        linkedList.addAll(Arrays.asList("X", "Y", "Z"));
        
        System.out.println("ArrayList: " + arrayList + 
                          " (type: " + arrayList.getClass().getSimpleName() + ")");
        System.out.println("LinkedList: " + linkedList + 
                          " (type: " + linkedList.getClass().getSimpleName() + ")");
        
        // Generic factory for maps
        Map<String, Integer> hashMap = factory.createMap("HashMap");
        Map<String, Integer> treeMap = factory.createMap("TreeMap");
        
        hashMap.put("One", 1);
        hashMap.put("Two", 2);
        
        treeMap.put("First", 1);
        treeMap.put("Second", 2);
        
        System.out.println("HashMap: " + hashMap);
        System.out.println("TreeMap: " + treeMap);
    }
    
    private static void demonstrateUtilityMethods() {
        System.out.println("\n=== Generic Utility Methods ===");
        
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        List<String> words = Arrays.asList("hello", "world", "java", "generics");
        
        // Generic utility methods
        System.out.println("First number: " + getFirst(numbers));
        System.out.println("First word: " + getFirst(words));
        System.out.println("Last number: " + getLast(numbers));
        System.out.println("Last word: " + getLast(words));
        
        // Generic collection operations
        List<Integer> reversedNumbers = reverse(numbers);
        System.out.println("Reversed numbers: " + reversedNumbers);
        
        List<String> reversedWords = reverse(words);
        System.out.println("Reversed words: " + reversedWords);
        
        // Generic pair operations
        Pair<String, Integer> pair1 = new Pair<>("Alice", 30);
        Pair<Integer, Boolean> pair2 = new Pair<>(42, true);
        
        System.out.println("Pair 1: " + pair1);
        System.out.println("Pair 2: " + pair2);
        
        Pair<Integer, String> swapped = pair1.swap();
        System.out.println("Swapped pair 1: " + swapped);
    }
    
    // Generic utility methods
    public static <T> T getFirst(List<T> list) {
        return list.isEmpty() ? null : list.get(0);
    }
    
    public static <T> T getLast(List<T> list) {
        return list.isEmpty() ? null : list.get(list.size() - 1);
    }
    
    public static <T> List<T> reverse(List<T> list) {
        List<T> reversed = new ArrayList<>(list);
        Collections.reverse(reversed);
        return reversed;
    }
    
    // Generic classes for demonstration
    static class Person {
        private String name;
        private int age;
        private String email;
        
        // Constructors, getters, setters
        public Person() {}
        
        public void setName(String name) { this.name = name; }
        public void setAge(int age) { this.age = age; }
        public void setEmail(String email) { this.email = email; }
        
        @Override
        public String toString() {
            return String.format("Person{name='%s', age=%d, email='%s'}", name, age, email);
        }
    }
    
    static class Product {
        private String name;
        private double price;
        private String category;
        
        public Product() {}
        
        public void setName(String name) { this.name = name; }
        public void setPrice(double price) { this.price = price; }
        public void setCategory(String category) { this.category = category; }
        
        @Override
        public String toString() {
            return String.format("Product{name='%s', price=%.2f, category='%s'}", name, price, category);
        }
    }
    
    // Generic Builder class
    static class GenericBuilder<T> {
        private final Supplier<T> instantiator;
        private List<Consumer<T>> modifiers = new ArrayList<>();
        
        public GenericBuilder(Supplier<T> instantiator) {
            this.instantiator = instantiator;
        }
        
        public <U> GenericBuilder<T> with(BiConsumer<T, U> setter, U value) {
            modifiers.add(instance -> setter.accept(instance, value));
            return this;
        }
        
        public T build() {
            T instance = instantiator.get();
            modifiers.forEach(modifier -> modifier.accept(instance));
            return instance;
        }
    }
    
    // Generic Factory class
    static class CollectionFactory {
        @SuppressWarnings("unchecked")
        public <T> List<T> createList(String type) {
            switch (type.toLowerCase()) {
                case "arraylist": return new ArrayList<>();
                case "linkedlist": return new LinkedList<>();
                case "vector": return new Vector<>();
                default: throw new IllegalArgumentException("Unknown list type: " + type);
            }
        }
        
        @SuppressWarnings("unchecked")
        public <K, V> Map<K, V> createMap(String type) {
            switch (type.toLowerCase()) {
                case "hashmap": return new HashMap<>();
                case "treemap": return new TreeMap<>();
                case "linkedhashmap": return new LinkedHashMap<>();
                default: throw new IllegalArgumentException("Unknown map type: " + type);
            }
        }
    }
    
    // Generic Pair class
    static class Pair<T, U> {
        private final T first;
        private final U second;
        
        public Pair(T first, U second) {
            this.first = first;
            this.second = second;
        }
        
        public T getFirst() { return first; }
        public U getSecond() { return second; }
        
        public <V, W> Pair<V, W> map(Function<T, V> firstMapper, Function<U, W> secondMapper) {
            return new Pair<>(firstMapper.apply(first), secondMapper.apply(second));
        }
        
        public Pair<U, T> swap() {
            return new Pair<>(second, first);
        }
        
        @Override
        public String toString() {
            return String.format("(%s, %s)", first, second);
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Pair<?, ?> pair = (Pair<?, ?>) obj;
            return Objects.equals(first, pair.first) && Objects.equals(second, pair.second);
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(first, second);
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

- 🏗️ **Collections Framework Architecture**: Interfaces, implementations, algorithms
- 📊 **Core Interfaces**: Collection, List, Set, Queue, Map hierarchies
- 🔄 **Collection Operations**: Basic operations, bulk operations, array conversions
- ⚡ **Iterator Pattern**: Safe iteration and modification of collections
- 🎯 **Generics**: Type safety, wildcards, bounded types, diamond operator
- 📈 **Performance Characteristics**: Understanding different collection behaviors
- 🔧 **Best Practices**: Generic programming patterns and utilities
- 💡 **Modern Features**: Stream API integration, method references

</v-clicks>

## Collection Interface Hierarchy

```
Collection<E>
├── List<E> - Ordered, allows duplicates, indexed access
├── Set<E> - No duplicates, mathematical set operations  
└── Queue<E> - Element processing order, head/tail operations

Map<K,V> - Key-value associations, no duplicate keys
```

## Key Design Principles

### Interface Segregation
- Small, focused interfaces (List, Set, Queue)
- Clients depend only on methods they use

### Implementation Variety
- Multiple implementations per interface
- Different performance characteristics
- Choose based on use case requirements

### Generic Type Safety
- Compile-time type checking
- Eliminates casting and ClassCastException
- Better code readability and maintainability

</div>

<div>

## Important Concepts Recap

<v-clicks>

- **Collection vs Collections**: Interface vs utility class
- **Fail-Fast Iterators**: Detect concurrent modifications
- **Generic Type Erasure**: Runtime type information removed
- **Wildcards**: Upper bounded (?  extends), lower bounded (? super)
- **Diamond Operator**: Type inference in object creation
- **Bulk Operations**: addAll, removeAll, retainAll, containsAll
- **Array Interoperability**: toArray() and Arrays.asList()
- **Modern Patterns**: Builder pattern, factory pattern with generics

</v-clicks>

## Performance Considerations

| Operation | ArrayList | LinkedList | HashSet | TreeSet |
|-----------|-----------|------------|---------|---------|
| Add | O(1) | O(1) | O(1) | O(log n) |
| Remove | O(n) | O(1)* | O(1) | O(log n) |
| Search | O(n) | O(n) | O(1) | O(log n) |
| Access | O(1) | O(n) | N/A | N/A |

*O(1) if you have iterator/reference to node

## When to Use Each Collection

### ArrayList
- Frequent random access by index
- More reads than modifications
- Need to maintain insertion order

### LinkedList  
- Frequent insertions/deletions in middle
- Implementing stack or queue
- Don't need random access

### HashSet
- Need unique elements
- Fast lookups required
- Order doesn't matter

### TreeSet
- Need unique elements in sorted order
- Range operations required
- Natural ordering important

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Collections Framework Overview Complete

**Lecture 34 Successfully Completed!**  
You now understand the Java Collections Framework architecture and core concepts

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for specific Collection implementations! <carbon:arrow-right class="inline"/>
  </span>
</div>