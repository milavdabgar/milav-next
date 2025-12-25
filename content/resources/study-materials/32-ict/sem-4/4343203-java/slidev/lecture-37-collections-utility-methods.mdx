---
theme: default
background: https://source.unsplash.com/1024x768/?utility,tools
title: Collections Utility Methods
info: |
  ## Java Programming (4343203)
  
  Lecture 37: Collections Utility Methods
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Explore the Collections utility class and its powerful methods for sorting, searching, and manipulating collections.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Collections Utility Methods
## Lecture 37

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

- 🛠️ **Master** Collections class utility methods
- 🔧 **Sort** collections using natural and custom ordering
- 🔍 **Search** collections efficiently with binary search
- 🔄 **Manipulate** collections with reverse, shuffle, rotate operations
- 📊 **Create** immutable and unmodifiable collections
- 🎯 **Apply** algorithms like min, max, frequency finding
- 🚫 **Handle** empty and singleton collections appropriately
- 💡 **Choose** optimal utility methods for different scenarios

</v-clicks>

---
layout: default
---

# Collections Class Overview

<div class="grid grid-cols-2 gap-6">

<div>

## Collections Utility Class

### Key Characteristics
- **Static Methods Only**: No instance methods
- **Polymorphic Algorithms**: Work with any collection type
- **Performance Optimized**: Efficient implementations
- **Null-Safe**: Handle null values appropriately

### Categories of Methods
1. **Sorting and Ordering**
2. **Searching and Finding**
3. **Collection Manipulation**
4. **Immutable Collections**
5. **Specialized Collections**
6. **Min/Max Operations**

## Sorting Operations

```java
import java.util.*;

public class SortingDemo {
    public static void main(String[] args) {
        demonstrateNaturalSorting();
        demonstrateCustomSorting();
        demonstrateStableSorting();
        demonstrateSortingPerformance();
    }
    
    private static void demonstrateNaturalSorting() {
        System.out.println("=== Natural Sorting ===");
        
        // Integer list
        List<Integer> numbers = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 9, 3));
        System.out.println("Original numbers: " + numbers);
        
        Collections.sort(numbers);
        System.out.println("Sorted numbers: " + numbers);
        
        // String list
        List<String> words = new ArrayList<>(Arrays.asList("zebra", "apple", "banana", "cherry"));
        System.out.println("Original words: " + words);
        
        Collections.sort(words);
        System.out.println("Sorted words: " + words);
        
        // Reverse sorting
        Collections.sort(numbers, Collections.reverseOrder());
        System.out.println("Reverse sorted numbers: " + numbers);
        
        Collections.sort(words, Collections.reverseOrder());
        System.out.println("Reverse sorted words: " + words);
    }
    
    private static void demonstrateCustomSorting() {
        System.out.println("\n=== Custom Sorting ===");
        
        List<Person> people = Arrays.asList(
            new Person("Alice", 30, 85000),
            new Person("Bob", 25, 75000),
            new Person("Charlie", 35, 95000),
            new Person("Diana", 28, 80000)
        );
        
        System.out.println("Original people: " + people);
        
        // Sort by age
        List<Person> byAge = new ArrayList<>(people);
        Collections.sort(byAge, Comparator.comparing(Person::getAge));
        System.out.println("Sorted by age: " + byAge);
        
        // Sort by salary (descending)
        List<Person> bySalary = new ArrayList<>(people);
        Collections.sort(bySalary, Comparator.comparing(Person::getSalary).reversed());
        System.out.println("Sorted by salary (desc): " + bySalary);
        
        // Sort by name length, then alphabetically
        List<Person> byNameLength = new ArrayList<>(people);
        Collections.sort(byNameLength, 
            Comparator.comparing((Person p) -> p.getName().length())
                     .thenComparing(Person::getName));
        System.out.println("Sorted by name length, then name: " + byNameLength);
        
        // Multiple criteria sorting
        List<Person> multiSort = new ArrayList<>(people);
        Collections.sort(multiSort, 
            Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName)
                     .thenComparing(Person::getSalary));
        System.out.println("Multi-criteria sort: " + multiSort);
    }
    
    private static void demonstrateStableSorting() {
        System.out.println("\n=== Stable Sorting ===");
        
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", "Engineering", 1),
            new Employee("Bob", "Marketing", 2),
            new Employee("Charlie", "Engineering", 3),
            new Employee("Diana", "Marketing", 4),
            new Employee("Eve", "Engineering", 5)
        );
        
        System.out.println("Original employees (by hire order):");
        employees.forEach(System.out::println);
        
        // Stable sort by department (preserves original order within department)
        List<Employee> stableSorted = new ArrayList<>(employees);
        Collections.sort(stableSorted, Comparator.comparing(Employee::getDepartment));
        
        System.out.println("\nStable sort by department (hire order preserved):");
        stableSorted.forEach(System.out::println);
        
        // Demonstrate stability
        System.out.println("\nNotice: Within each department, original order is maintained");
    }
    
    private static void demonstrateSortingPerformance() {
        System.out.println("\n=== Sorting Performance ===");
        
        // Create large random list
        List<Integer> largeList = new ArrayList<>();
        Random random = new Random(42); // Fixed seed for reproducibility
        for (int i = 0; i < 100000; i++) {
            largeList.add(random.nextInt(1000000));
        }
        
        // Test Collections.sort()
        List<Integer> testList1 = new ArrayList<>(largeList);
        long startTime = System.nanoTime();
        Collections.sort(testList1);
        long sortTime = System.nanoTime() - startTime;
        
        // Test with custom comparator
        List<Integer> testList2 = new ArrayList<>(largeList);
        startTime = System.nanoTime();
        Collections.sort(testList2, Integer::compareTo);
        long customSortTime = System.nanoTime() - startTime;
        
        System.out.println("Sorting 100,000 integers:");
        System.out.println("Natural sort: " + sortTime / 1_000_000 + " ms");
        System.out.println("Custom comparator: " + customSortTime / 1_000_000 + " ms");
        System.out.println("Collections.sort() uses Timsort algorithm (stable, adaptive)");
    }
    
    static class Person {
        private String name;
        private int age;
        private double salary;
        
        public Person(String name, int age, double salary) {
            this.name = name;
            this.age = age;
            this.salary = salary;
        }
        
        public String getName() { return name; }
        public int getAge() { return age; }
        public double getSalary() { return salary; }
        
        @Override
        public String toString() {
            return String.format("%s(%d, $%.0f)", name, age, salary);
        }
    }
    
    static class Employee {
        private String name;
        private String department;
        private int hireOrder;
        
        public Employee(String name, String department, int hireOrder) {
            this.name = name;
            this.department = department;
            this.hireOrder = hireOrder;
        }
        
        public String getName() { return name; }
        public String getDepartment() { return department; }
        public int getHireOrder() { return hireOrder; }
        
        @Override
        public String toString() {
            return String.format("%s (%s, hired #%d)", name, department, hireOrder);
        }
    }
}
```

</div>

<div>

## Searching and Finding Operations

```java
import java.util.*;

public class SearchingDemo {
    public static void main(String[] args) {
        demonstrateBinarySearch();
        demonstrateMinMaxOperations();
        demonstrateFrequencyOperations();
        demonstrateIndexOperations();
    }
    
    private static void demonstrateBinarySearch() {
        System.out.println("=== Binary Search ===");
        
        List<Integer> numbers = Arrays.asList(1, 3, 5, 7, 9, 11, 13, 15, 17, 19);
        System.out.println("Sorted list: " + numbers);
        
        // Binary search for existing elements
        int index = Collections.binarySearch(numbers, 7);
        System.out.println("Index of 7: " + index);
        
        index = Collections.binarySearch(numbers, 15);
        System.out.println("Index of 15: " + index);
        
        // Binary search for non-existing elements
        index = Collections.binarySearch(numbers, 6);
        System.out.println("Index of 6 (not found): " + index);
        System.out.println("Insertion point for 6: " + (-index - 1));
        
        index = Collections.binarySearch(numbers, 20);
        System.out.println("Index of 20 (not found): " + index);
        System.out.println("Insertion point for 20: " + (-index - 1));
        
        // Binary search with custom comparator
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date", "elderberry");
        System.out.println("\nString list: " + words);
        
        // Search ignoring case
        index = Collections.binarySearch(words, "Cherry", String.CASE_INSENSITIVE_ORDER);
        System.out.println("Index of 'Cherry' (case insensitive): " + index);
        
        // Custom object binary search
        List<Person> people = Arrays.asList(
            new Person("Alice", 25),
            new Person("Bob", 30),
            new Person("Charlie", 35),
            new Person("Diana", 40)
        );
        
        // Must sort by same criteria used for search
        Collections.sort(people, Comparator.comparing(Person::getAge));
        System.out.println("\nPeople sorted by age: " + people);
        
        index = Collections.binarySearch(people, new Person("Unknown", 35), 
                                        Comparator.comparing(Person::getAge));
        if (index >= 0) {
            System.out.println("Person with age 35: " + people.get(index));
        }
    }
    
    private static void demonstrateMinMaxOperations() {
        System.out.println("\n=== Min/Max Operations ===");
        
        List<Integer> numbers = Arrays.asList(5, 2, 8, 1, 9, 3, 7);
        System.out.println("Numbers: " + numbers);
        
        // Natural ordering min/max
        Integer min = Collections.min(numbers);
        Integer max = Collections.max(numbers);
        System.out.println("Min: " + min + ", Max: " + max);
        
        // Custom comparator min/max
        List<String> words = Arrays.asList("elephant", "cat", "dog", "butterfly", "ant");
        System.out.println("Words: " + words);
        
        String shortest = Collections.min(words, Comparator.comparing(String::length));
        String longest = Collections.max(words, Comparator.comparing(String::length));
        System.out.println("Shortest: " + shortest + ", Longest: " + longest);
        
        // Min/max with multiple criteria
        List<Person> people = Arrays.asList(
            new Person("Alice", 30),
            new Person("Bob", 25),
            new Person("Charlie", 30),
            new Person("Diana", 25)
        );
        
        // Youngest person (if tie, first alphabetically)
        Person youngest = Collections.min(people, 
            Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName));
        System.out.println("Youngest person: " + youngest);
        
        // Oldest person (if tie, last alphabetically)  
        Person oldest = Collections.max(people, 
            Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName));
        System.out.println("Oldest person: " + oldest);
    }
    
    private static void demonstrateFrequencyOperations() {
        System.out.println("\n=== Frequency Operations ===");
        
        List<String> colors = Arrays.asList("red", "blue", "red", "green", "blue", "red", "yellow");
        System.out.println("Colors: " + colors);
        
        // Count frequency of each color
        Set<String> uniqueColors = new HashSet<>(colors);
        for (String color : uniqueColors) {
            int frequency = Collections.frequency(colors, color);
            System.out.println(color + ": " + frequency);
        }
        
        // Find most frequent element
        String mostFrequent = uniqueColors.stream()
            .max(Comparator.comparing(color -> Collections.frequency(colors, color)))
            .orElse(null);
        System.out.println("Most frequent color: " + mostFrequent + 
                          " (appears " + Collections.frequency(colors, mostFrequent) + " times)");
        
        // Character frequency in string
        String text = "hello world";
        List<Character> chars = new ArrayList<>();
        for (char c : text.toCharArray()) {
            chars.add(c);
        }
        
        System.out.println("\nCharacter frequencies in '" + text + "':");
        Set<Character> uniqueChars = new HashSet<>(chars);
        for (Character c : uniqueChars) {
            if (c != ' ') { // Skip spaces
                int freq = Collections.frequency(chars, c);
                System.out.println("'" + c + "': " + freq);
            }
        }
    }
    
    private static void demonstrateIndexOperations() {
        System.out.println("\n=== Index Operations ===");
        
        List<String> items = Arrays.asList("apple", "banana", "apple", "cherry", "banana", "apple");
        System.out.println("Items: " + items);
        
        // Find first and last index of elements
        int firstApple = items.indexOf("apple");
        int lastApple = items.lastIndexOf("apple");
        System.out.println("First apple at index: " + firstApple);
        System.out.println("Last apple at index: " + lastApple);
        
        // Use Collections.indexOfSubList and lastIndexOfSubList
        List<String> sublist = Arrays.asList("banana", "apple");
        int subIndex = Collections.indexOfSubList(items, sublist);
        System.out.println("Sublist " + sublist + " starts at index: " + subIndex);
        
        // Check for disjoint collections
        List<String> fruits = Arrays.asList("apple", "banana", "cherry");
        List<String> vegetables = Arrays.asList("carrot", "lettuce", "tomato");
        List<String> mixed = Arrays.asList("apple", "carrot");
        
        boolean disjoint1 = Collections.disjoint(fruits, vegetables);
        boolean disjoint2 = Collections.disjoint(fruits, mixed);
        
        System.out.println("Fruits and vegetables are disjoint: " + disjoint1);
        System.out.println("Fruits and mixed are disjoint: " + disjoint2);
    }
    
    static class Person {
        private String name;
        private int age;
        
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        public String getName() { return name; }
        public int getAge() { return age; }
        
        @Override
        public String toString() {
            return name + "(" + age + ")";
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Collection Manipulation Operations

<div class="grid grid-cols-2 gap-6">

<div>

## Modification Operations

```java
import java.util.*;

public class ManipulationDemo {
    public static void main(String[] args) {
        demonstrateReverseOperations();
        demonstrateShuffleOperations();
        demonstrateRotateOperations();
        demonstrateFillReplaceOperations();
        demonstrateSwapOperations();
    }
    
    private static void demonstrateReverseOperations() {
        System.out.println("=== Reverse Operations ===");
        
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Original: " + numbers);
        
        Collections.reverse(numbers);
        System.out.println("Reversed: " + numbers);
        
        // Reverse with strings
        List<String> words = new ArrayList<>(Arrays.asList("first", "second", "third", "fourth"));
        System.out.println("Original words: " + words);
        
        Collections.reverse(words);
        System.out.println("Reversed words: " + words);
        
        // Reverse a portion using subList
        List<String> sentence = new ArrayList<>(Arrays.asList("The", "quick", "brown", "fox", "jumps"));
        System.out.println("Original sentence: " + sentence);
        
        // Reverse middle 3 words
        Collections.reverse(sentence.subList(1, 4));
        System.out.println("Middle reversed: " + sentence);
    }
    
    private static void demonstrateShuffleOperations() {
        System.out.println("\n=== Shuffle Operations ===");
        
        List<String> deck = new ArrayList<>(Arrays.asList(
            "Ace", "King", "Queen", "Jack", "10", "9", "8", "7"));
        System.out.println("Original deck: " + deck);
        
        // Shuffle with default random
        Collections.shuffle(deck);
        System.out.println("Shuffled deck: " + deck);
        
        // Shuffle with seeded random for reproducibility
        List<String> cards = new ArrayList<>(Arrays.asList(
            "A♠", "K♠", "Q♠", "J♠", "A♥", "K♥", "Q♥", "J♥"));
        System.out.println("Original cards: " + cards);
        
        Random seededRandom = new Random(42);
        Collections.shuffle(cards, seededRandom);
        System.out.println("Seeded shuffle 1: " + cards);
        
        // Reset and shuffle again with same seed
        cards = new ArrayList<>(Arrays.asList("A♠", "K♠", "Q♠", "J♠", "A♥", "K♥", "Q♥", "J♥"));
        seededRandom = new Random(42);
        Collections.shuffle(cards, seededRandom);
        System.out.println("Seeded shuffle 2: " + cards + " (same as shuffle 1)");
        
        // Practical example: random team assignment
        List<String> players = new ArrayList<>(Arrays.asList(
            "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"));
        Collections.shuffle(players);
        
        System.out.println("\nRandom team assignment:");
        System.out.println("Team A: " + players.subList(0, 4));
        System.out.println("Team B: " + players.subList(4, 8));
    }
    
    private static void demonstrateRotateOperations() {
        System.out.println("\n=== Rotate Operations ===");
        
        List<String> items = new ArrayList<>(Arrays.asList("A", "B", "C", "D", "E"));
        System.out.println("Original: " + items);
        
        // Rotate right by 2 positions
        Collections.rotate(items, 2);
        System.out.println("Rotate right 2: " + items);
        
        // Rotate left by 3 positions (negative value)
        Collections.rotate(items, -3);
        System.out.println("Rotate left 3: " + items);
        
        // Practical example: circular array simulation
        List<String> queue = new ArrayList<>(Arrays.asList("Task1", "Task2", "Task3", "Task4"));
        System.out.println("\nTask queue simulation:");
        System.out.println("Initial queue: " + queue);
        
        // Process first task (move to end)
        Collections.rotate(queue, -1);
        System.out.println("After processing Task1: " + queue);
        
        Collections.rotate(queue, -1);
        System.out.println("After processing Task2: " + queue);
        
        // Rotate a sublist
        List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8));
        System.out.println("\nOriginal numbers: " + numbers);
        
        // Rotate middle portion
        Collections.rotate(numbers.subList(2, 6), 1); // Rotate positions 2-5
        System.out.println("Middle rotated: " + numbers);
    }
    
    private static void demonstrateFillReplaceOperations() {
        System.out.println("\n=== Fill and Replace Operations ===");
        
        // Fill operation
        List<String> buffer = new ArrayList<>(Arrays.asList("old1", "old2", "old3", "old4"));
        System.out.println("Original buffer: " + buffer);
        
        Collections.fill(buffer, "empty");
        System.out.println("After fill: " + buffer);
        
        // Replace all occurrences
        List<String> text = new ArrayList<>(Arrays.asList("cat", "dog", "cat", "bird", "cat"));
        System.out.println("Original text: " + text);
        
        boolean replaced = Collections.replaceAll(text, "cat", "kitten");
        System.out.println("Replaced 'cat' with 'kitten': " + replaced);
        System.out.println("After replace: " + text);
        
        // Replace with no matches
        replaced = Collections.replaceAll(text, "elephant", "mouse");
        System.out.println("Tried to replace 'elephant': " + replaced);
        System.out.println("Text unchanged: " + text);
        
        // Practical example: data cleaning
        List<String> data = new ArrayList<>(Arrays.asList("null", "42", "null", "17", "null", "99"));
        System.out.println("\nData cleaning example:");
        System.out.println("Raw data: " + data);
        
        Collections.replaceAll(data, "null", "0");
        System.out.println("After cleaning nulls: " + data);
        
        // Fill part of list
        List<Integer> scores = new ArrayList<>(Arrays.asList(85, 92, 78, 0, 0, 88, 94));
        System.out.println("Scores with missing values: " + scores);
        
        // Fill missing scores (positions 3-4) with default value
        Collections.fill(scores.subList(3, 5), -1); // -1 indicates missing
        System.out.println("After marking missing: " + scores);
    }
    
    private static void demonstrateSwapOperations() {
        System.out.println("\n=== Swap Operations ===");
        
        List<String> items = new ArrayList<>(Arrays.asList("first", "second", "third", "fourth"));
        System.out.println("Original: " + items);
        
        // Swap elements at positions 1 and 3
        Collections.swap(items, 1, 3);
        System.out.println("After swap(1,3): " + items);
        
        // Swap back
        Collections.swap(items, 1, 3);
        System.out.println("After swap back: " + items);
        
        // Practical example: bubble sort implementation
        List<Integer> numbers = new ArrayList<>(Arrays.asList(64, 34, 25, 12, 22, 11, 90));
        System.out.println("\nBubble sort demonstration:");
        System.out.println("Original: " + numbers);
        
        bubbleSort(numbers);
        System.out.println("Sorted: " + numbers);
        
        // Selection sort example
        numbers = new ArrayList<>(Arrays.asList(29, 10, 14, 37, 13));
        System.out.println("\nSelection sort demonstration:");
        System.out.println("Original: " + numbers);
        
        selectionSort(numbers);
        System.out.println("Sorted: " + numbers);
    }
    
    // Helper method: bubble sort using Collections.swap
    private static void bubbleSort(List<Integer> list) {
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (list.get(j) > list.get(j + 1)) {
                    Collections.swap(list, j, j + 1);
                }
            }
        }
    }
    
    // Helper method: selection sort using Collections.swap
    private static void selectionSort(List<Integer> list) {
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (list.get(j) < list.get(minIndex)) {
                    minIndex = j;
                }
            }
            Collections.swap(list, i, minIndex);
        }
    }
}
```

</div>

<div>

## Copy and Synchronization Operations

```java
import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

public class CopyAndSyncDemo {
    public static void main(String[] args) {
        demonstrateCopyOperations();
        demonstrateSynchronizedWrappers();
        demonstrateUnmodifiableWrappers();
        demonstrateCheckedWrappers();
    }
    
    private static void demonstrateCopyOperations() {
        System.out.println("=== Copy Operations ===");
        
        List<String> source = Arrays.asList("apple", "banana", "cherry", "date");
        List<String> destination = new ArrayList<>(Arrays.asList("old1", "old2", "old3", "old4"));
        
        System.out.println("Source: " + source);
        System.out.println("Destination before: " + destination);
        
        // Copy all elements from source to destination
        Collections.copy(destination, source);
        System.out.println("Destination after copy: " + destination);
        
        // Destination must be at least as large as source
        List<String> smallDest = new ArrayList<>(Arrays.asList("x", "y"));
        try {
            Collections.copy(smallDest, source);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Copy failed: destination too small");
        }
        
        // Proper way to handle different sizes
        List<String> properDest = new ArrayList<>(Collections.nCopies(source.size(), null));
        Collections.copy(properDest, source);
        System.out.println("Proper copy result: " + properDest);
        
        // Partial copy using subList
        List<String> partial = new ArrayList<>(Arrays.asList("a", "b", "c", "d", "e"));
        Collections.copy(partial.subList(1, 4), Arrays.asList("X", "Y", "Z"));
        System.out.println("Partial copy result: " + partial);
        
        // nCopies for creating repeated elements
        List<String> repeated = Collections.nCopies(5, "default");
        System.out.println("nCopies result: " + repeated);
        
        // Practical use: initialize with default values
        List<Integer> scores = new ArrayList<>(Collections.nCopies(10, 0));
        System.out.println("Initial scores: " + scores);
        scores.set(3, 85);
        scores.set(7, 92);
        System.out.println("Updated scores: " + scores);
    }
    
    private static void demonstrateSynchronizedWrappers() {
        System.out.println("\n=== Synchronized Wrappers ===");
        
        // Create synchronized collections
        List<String> syncList = Collections.synchronizedList(new ArrayList<>());
        Set<Integer> syncSet = Collections.synchronizedSet(new HashSet<>());
        Map<String, Integer> syncMap = Collections.synchronizedMap(new HashMap<>());
        
        System.out.println("Created synchronized collections");
        
        // Add some data
        syncList.add("thread-safe");
        syncList.add("access");
        
        syncSet.add(1);
        syncSet.add(2);
        syncSet.add(3);
        
        syncMap.put("key1", 100);
        syncMap.put("key2", 200);
        
        System.out.println("Sync list: " + syncList);
        System.out.println("Sync set: " + syncSet);
        System.out.println("Sync map: " + syncMap);
        
        // Important: iteration still needs manual synchronization
        synchronized (syncList) {
            Iterator<String> it = syncList.iterator();
            while (it.hasNext()) {
                System.out.println("Safe iteration: " + it.next());
            }
        }
        
        // Demonstrate thread safety
        List<Integer> unsafeList = new ArrayList<>();
        List<Integer> safeList = Collections.synchronizedList(new ArrayList<>());
        
        // Simulate concurrent access
        simulateConcurrentAccess(unsafeList, "Unsafe List");
        simulateConcurrentAccess(safeList, "Safe List");
        
        System.out.println("Note: synchronized wrappers provide thread safety");
        System.out.println("But ConcurrentHashMap, etc. are often better choices");
    }
    
    private static void simulateConcurrentAccess(List<Integer> list, String name) {
        final int numThreads = 3;
        final int itemsPerThread = 100;
        
        Thread[] threads = new Thread[numThreads];
        
        for (int i = 0; i < numThreads; i++) {
            final int threadId = i;
            threads[i] = new Thread(() -> {
                for (int j = 0; j < itemsPerThread; j++) {
                    try {
                        list.add(threadId * itemsPerThread + j);
                    } catch (Exception e) {
                        // May fail with unsafe list
                    }
                }
            });
            threads[i].start();
        }
        
        // Wait for all threads to complete
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        
        System.out.println(name + " final size: " + list.size() + 
                          " (expected: " + (numThreads * itemsPerThread) + ")");
    }
    
    private static void demonstrateUnmodifiableWrappers() {
        System.out.println("\n=== Unmodifiable Wrappers ===");
        
        // Create modifiable collections
        List<String> modifiableList = new ArrayList<>(Arrays.asList("apple", "banana", "cherry"));
        Set<Integer> modifiableSet = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Map<String, String> modifiableMap = new HashMap<>();
        modifiableMap.put("key1", "value1");
        modifiableMap.put("key2", "value2");
        
        // Create unmodifiable views
        List<String> unmodifiableList = Collections.unmodifiableList(modifiableList);
        Set<Integer> unmodifiableSet = Collections.unmodifiableSet(modifiableSet);
        Map<String, String> unmodifiableMap = Collections.unmodifiableMap(modifiableMap);
        
        System.out.println("Unmodifiable list: " + unmodifiableList);
        System.out.println("Unmodifiable set: " + unmodifiableSet);
        System.out.println("Unmodifiable map: " + unmodifiableMap);
        
        // Try to modify - will throw UnsupportedOperationException
        try {
            unmodifiableList.add("date");
        } catch (UnsupportedOperationException e) {
            System.out.println("Cannot modify unmodifiable list");
        }
        
        try {
            unmodifiableSet.remove(3);
        } catch (UnsupportedOperationException e) {
            System.out.println("Cannot modify unmodifiable set");
        }
        
        try {
            unmodifiableMap.put("key3", "value3");
        } catch (UnsupportedOperationException e) {
            System.out.println("Cannot modify unmodifiable map");
        }
        
        // Changes to original affect unmodifiable view
        System.out.println("\nModifying original collections:");
        modifiableList.add("date");
        modifiableSet.add(6);
        modifiableMap.put("key3", "value3");
        
        System.out.println("Unmodifiable list now: " + unmodifiableList);
        System.out.println("Unmodifiable set now: " + unmodifiableSet);
        System.out.println("Unmodifiable map now: " + unmodifiableMap);
        
        // Factory methods (Java 9+) create truly immutable collections
        List<String> immutableList = List.of("fixed1", "fixed2", "fixed3");
        Set<Integer> immutableSet = Set.of(10, 20, 30);
        Map<String, Integer> immutableMap = Map.of("a", 1, "b", 2);
        
        System.out.println("\nImmutable collections (Java 9+):");
        System.out.println("Immutable list: " + immutableList);
        System.out.println("Immutable set: " + immutableSet);
        System.out.println("Immutable map: " + immutableMap);
    }
    
    private static void demonstrateCheckedWrappers() {
        System.out.println("\n=== Checked Type Wrappers ===");
        
        // Create checked collections for type safety at runtime
        List<String> checkedList = Collections.checkedList(new ArrayList<>(), String.class);
        Set<Integer> checkedSet = Collections.checkedSet(new HashSet<>(), Integer.class);
        Map<String, Double> checkedMap = Collections.checkedMap(new HashMap<>(), String.class, Double.class);
        
        // Normal usage works fine
        checkedList.add("valid string");
        checkedSet.add(42);
        checkedMap.put("pi", 3.14159);
        
        System.out.println("Checked list: " + checkedList);
        System.out.println("Checked set: " + checkedSet);
        System.out.println("Checked map: " + checkedMap);
        
        // Demonstrate type checking at runtime
        List rawList = checkedList; // Raw type reference
        
        try {
            rawList.add(123); // Integer into String list
        } catch (ClassCastException e) {
            System.out.println("Type check caught invalid addition: " + e.getMessage());
        }
        
        // Without checked wrapper, this would fail later during retrieval
        List<String> normalList = new ArrayList<>();
        List rawNormal = normalList;
        rawNormal.add(123); // No immediate error
        
        try {
            String str = normalList.get(0); // ClassCastException here
        } catch (ClassCastException e) {
            System.out.println("Late type error: " + e.getMessage());
        }
        
        System.out.println("Checked collections provide early type error detection");
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

- 🛠️ **Collections Class**: Comprehensive utility methods for collection operations
- 🔧 **Sorting**: Natural and custom ordering with stable algorithms
- 🔍 **Searching**: Binary search for efficient element finding
- 🔄 **Manipulation**: Reverse, shuffle, rotate, fill, replace, swap operations
- 📊 **Analysis**: Min, max, frequency, and statistical operations
- 🚫 **Immutability**: Unmodifiable and checked collection wrappers
- 🔒 **Thread Safety**: Synchronized wrappers for concurrent access
- 💡 **Performance**: Choosing optimal algorithms for different scenarios

</v-clicks>

## Key Utility Categories

### Sorting and Ordering
```java
Collections.sort(list)              // Natural order
Collections.sort(list, comparator)  // Custom order
Collections.reverse(list)           // Reverse order
Collections.shuffle(list)           // Random order
```

### Searching and Analysis
```java
Collections.binarySearch(list, key) // O(log n) search
Collections.min(collection)         // Find minimum
Collections.max(collection)         // Find maximum
Collections.frequency(collection, o) // Count occurrences
```

### Manipulation
```java
Collections.rotate(list, distance)  // Circular shift
Collections.swap(list, i, j)        // Exchange elements
Collections.fill(list, obj)         // Replace all elements
Collections.copy(dest, src)         // Copy elements
```

### Creation and Wrapping
```java
Collections.emptyList()             // Immutable empty
Collections.singletonList(obj)      // Immutable single
Collections.nCopies(n, obj)         // Repeated elements
Collections.unmodifiableList(list)  // Read-only view
Collections.synchronizedList(list)  // Thread-safe wrapper
```

</div>

<div>

## Important Concepts Recap

<v-clicks>

- **Polymorphic Algorithms**: Work with any Collection implementation
- **Stable Sorting**: Maintains relative order of equal elements
- **Binary Search**: Requires sorted input for O(log n) performance
- **View Collections**: Wrappers reflect changes to original collection
- **Thread Safety**: Synchronized wrappers vs concurrent collections
- **Type Safety**: Checked collections catch type errors early
- **Immutability**: Unmodifiable vs truly immutable collections
- **Performance**: Understanding time complexity of operations

</v-clicks>

## Performance Characteristics

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| **sort()** | O(n log n) | Timsort algorithm, stable |
| **binarySearch()** | O(log n) | Requires sorted input |
| **min()/max()** | O(n) | Linear scan required |
| **frequency()** | O(n) | Counts all occurrences |
| **reverse()** | O(n) | In-place reversal |
| **shuffle()** | O(n) | Fisher-Yates algorithm |
| **rotate()** | O(n) | Efficient circular shift |
| **copy()** | O(n) | Element-by-element copy |

## Best Practices

### 1. **Choose Appropriate Methods**
```java
// Use binary search for sorted data
Collections.sort(list);
int index = Collections.binarySearch(list, target);

// Use frequency for counting
int count = Collections.frequency(list, element);
```

### 2. **Understand Wrapper Behavior**
```java
// Unmodifiable views reflect original changes
List<String> original = new ArrayList<>();
List<String> view = Collections.unmodifiableList(original);
original.add("item"); // Affects view too

// For true immutability, use copy
List<String> immutable = Collections.unmodifiableList(
    new ArrayList<>(original));
```

### 3. **Thread Safety Considerations**
```java
// Synchronized wrappers need manual sync for iteration
List<String> syncList = Collections.synchronizedList(new ArrayList<>());
synchronized (syncList) {
    for (String item : syncList) {
        // Safe iteration
    }
}

// Consider ConcurrentHashMap over synchronized Map
```

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Collections Utility Methods Complete

**Lecture 37 Successfully Completed!**  
You now master the Collections utility class and its powerful methods

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for Advanced Java Generics! <carbon:arrow-right class="inline"/>
  </span>
</div>