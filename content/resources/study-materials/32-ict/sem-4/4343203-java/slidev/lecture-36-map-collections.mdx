---
theme: default
background: https://source.unsplash.com/1024x768/?map,key,value
title: Map Collections
info: |
  ## Java Programming (4343203)
  
  Lecture 36: Map Collections
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Master Map collections including HashMap, LinkedHashMap, TreeMap, and their practical applications in key-value data storage.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Map Collections
## Lecture 36

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

- 🗺️ **Understand** Map interface and key-value pair concepts
- 🔑 **Master** HashMap, LinkedHashMap, and TreeMap implementations
- ⚡ **Compare** performance characteristics of different Map types
- 🎯 **Handle** key collision and hashing strategies effectively
- 🔍 **Navigate** maps using various iteration techniques
- 📊 **Apply** maps for caching, indexing, and data organization
- 🛠️ **Implement** advanced map operations and transformations
- 💡 **Choose** appropriate Map implementation for specific use cases

</v-clicks>

---
layout: default
---

# Map Interface Fundamentals

<div class="grid grid-cols-2 gap-6">

<div>

## Map Characteristics

### Key-Value Association
- **Keys**: Unique identifiers (no duplicates)
- **Values**: Associated data (duplicates allowed)
- **Mappings**: Key-value pairs (entries)
- **Not Part of Collection**: Separate hierarchy

### Core Map Operations
```java
import java.util.*;

public class MapBasicsDemo {
    public static void main(String[] args) {
        demonstrateBasicOperations();
        demonstrateBulkOperations();
        demonstrateViewOperations();
        demonstrateEntryOperations();
    }
    
    private static void demonstrateBasicOperations() {
        System.out.println("=== Basic Map Operations ===");
        
        Map<String, Integer> scores = new HashMap<>();
        
        // Adding key-value pairs
        scores.put("Alice", 95);
        scores.put("Bob", 87);
        scores.put("Charlie", 92);
        scores.put("Diana", 88);
        
        System.out.println("Scores map: " + scores);
        System.out.println("Map size: " + scores.size());
        
        // Accessing values
        Integer aliceScore = scores.get("Alice");
        System.out.println("Alice's score: " + aliceScore);
        
        Integer frankScore = scores.get("Frank"); // Non-existent key
        System.out.println("Frank's score: " + frankScore); // null
        
        // Default value for missing keys
        Integer defaultScore = scores.getOrDefault("Frank", 0);
        System.out.println("Frank's score (with default): " + defaultScore);
        
        // Checking for keys and values
        System.out.println("Contains key 'Bob': " + scores.containsKey("Bob"));
        System.out.println("Contains value 95: " + scores.containsValue(95));
        
        // Updating values
        Integer oldValue = scores.put("Bob", 90); // Updates existing key
        System.out.println("Bob's old score: " + oldValue);
        System.out.println("Updated scores: " + scores);
        
        // Removing entries
        Integer removedScore = scores.remove("Diana");
        System.out.println("Removed Diana's score: " + removedScore);
        System.out.println("After removal: " + scores);
        
        // putIfAbsent - only adds if key doesn't exist
        scores.putIfAbsent("Eve", 85); // Adds
        scores.putIfAbsent("Alice", 100); // Doesn't add (Alice exists)
        System.out.println("After putIfAbsent: " + scores);
    }
    
    private static void demonstrateBulkOperations() {
        System.out.println("\n=== Bulk Operations ===");
        
        Map<String, String> countries = new HashMap<>();
        countries.put("US", "United States");
        countries.put("UK", "United Kingdom");
        countries.put("CA", "Canada");
        
        Map<String, String> moreCountries = new HashMap<>();
        moreCountries.put("FR", "France");
        moreCountries.put("DE", "Germany");
        moreCountries.put("JP", "Japan");
        
        System.out.println("Original countries: " + countries);
        System.out.println("More countries: " + moreCountries);
        
        // putAll - adds all mappings from another map
        countries.putAll(moreCountries);
        System.out.println("After putAll: " + countries);
        
        // clear - removes all mappings
        Map<String, String> tempMap = new HashMap<>(countries);
        tempMap.clear();
        System.out.println("After clear: " + tempMap);
        System.out.println("Is empty: " + tempMap.isEmpty());
        
        // replaceAll - transforms all values
        Map<String, Integer> wordLengths = new HashMap<>();
        wordLengths.put("Java", 4);
        wordLengths.put("Python", 6);
        wordLengths.put("JavaScript", 10);
        
        System.out.println("Original word lengths: " + wordLengths);
        
        // Double all values
        wordLengths.replaceAll((key, value) -> value * 2);
        System.out.println("After replaceAll (doubled): " + wordLengths);
    }
    
    private static void demonstrateViewOperations() {
        System.out.println("\n=== View Operations ===");
        
        Map<String, Integer> inventory = new HashMap<>();
        inventory.put("Apples", 50);
        inventory.put("Bananas", 30);
        inventory.put("Cherries", 25);
        inventory.put("Dates", 15);
        
        System.out.println("Inventory: " + inventory);
        
        // Key set view
        Set<String> products = inventory.keySet();
        System.out.println("Products: " + products);
        
        // Values collection view
        Collection<Integer> quantities = inventory.values();
        System.out.println("Quantities: " + quantities);
        System.out.println("Total quantity: " + 
                          quantities.stream().mapToInt(Integer::intValue).sum());
        
        // Entry set view
        Set<Map.Entry<String, Integer>> entries = inventory.entrySet();
        System.out.println("Entries:");
        for (Map.Entry<String, Integer> entry : entries) {
            System.out.println("  " + entry.getKey() + " -> " + entry.getValue());
        }
        
        // Modifying views affects original map
        products.remove("Dates"); // Removes from original map
        System.out.println("After removing from key set: " + inventory);
        
        // Cannot add to key set or values collection
        try {
            // products.add("Grapes"); // UnsupportedOperationException
            // quantities.add(100);    // UnsupportedOperationException
        } catch (UnsupportedOperationException e) {
            System.out.println("Cannot add to views directly");
        }
    }
    
    private static void demonstrateEntryOperations() {
        System.out.println("\n=== Entry Operations ===");
        
        Map<String, Double> prices = new HashMap<>();
        prices.put("Coffee", 4.50);
        prices.put("Tea", 3.25);
        prices.put("Juice", 5.75);
        prices.put("Water", 2.00);
        
        System.out.println("Original prices: " + prices);
        
        // Working with entries
        for (Map.Entry<String, Double> entry : prices.entrySet()) {
            String product = entry.getKey();
            Double price = entry.getValue();
            
            // Apply 10% discount to expensive items
            if (price > 4.0) {
                entry.setValue(price * 0.9);
                System.out.println("Applied discount to " + product);
            }
        }
        
        System.out.println("After discounts: " + prices);
        
        // merge operation - combines values for same key
        Map<String, Integer> sales = new HashMap<>();
        sales.put("Monday", 100);
        sales.put("Tuesday", 150);
        
        // Add more sales data
        sales.merge("Monday", 50, Integer::sum);    // 100 + 50 = 150
        sales.merge("Wednesday", 75, Integer::sum); // New entry: 75
        
        System.out.println("Sales data: " + sales);
        
        // compute - calculate value for a key
        sales.compute("Thursday", (key, value) -> {
            return (value == null) ? 80 : value + 20;
        });
        
        sales.computeIfAbsent("Friday", key -> 90);
        sales.computeIfPresent("Monday", (key, value) -> value + 25);
        
        System.out.println("After compute operations: " + sales);
    }
}
```

</div>

<div>

## HashMap Implementation

### HashMap Deep Dive
```java
import java.util.*;

public class HashMapDemo {
    public static void main(String[] args) {
        demonstrateHashingConcepts();
        demonstrateCollisionHandling();
        demonstratePerformanceCharacteristics();
        demonstrateCapacityAndLoadFactor();
    }
    
    private static void demonstrateHashingConcepts() {
        System.out.println("=== HashMap Hashing Concepts ===");
        
        Map<String, String> map = new HashMap<>();
        
        // Add some key-value pairs
        map.put("name", "John");
        map.put("age", "30");
        map.put("city", "New York");
        
        System.out.println("Map contents: " + map);
        
        // Demonstrate hash codes of keys
        System.out.println("\nHash codes of keys:");
        for (String key : map.keySet()) {
            System.out.println(key + " -> hash: " + key.hashCode());
        }
        
        // Show that hash code affects internal organization
        Map<Integer, String> numberMap = new HashMap<>();
        for (int i = 1; i <= 10; i++) {
            numberMap.put(i, "Value" + i);
        }
        
        System.out.println("\nNumber map: " + numberMap);
        System.out.println("Note: Order is not insertion order due to hashing");
    }
    
    private static void demonstrateCollisionHandling() {
        System.out.println("\n=== Collision Handling ===");
        
        // Custom class that demonstrates hash collisions
        Map<HashKey, String> collisionMap = new HashMap<>();
        
        HashKey key1 = new HashKey(1, "A");
        HashKey key2 = new HashKey(2, "B");
        HashKey key3 = new HashKey(3, "C");
        HashKey key4 = new HashKey(4, "A"); // Same hash as key1
        
        collisionMap.put(key1, "Value1");
        collisionMap.put(key2, "Value2");
        collisionMap.put(key3, "Value3");
        collisionMap.put(key4, "Value4"); // Hash collision with key1
        
        System.out.println("Map with hash collisions:");
        for (Map.Entry<HashKey, String> entry : collisionMap.entrySet()) {
            HashKey key = entry.getKey();
            System.out.println(key + " (hash: " + key.hashCode() + ") -> " + entry.getValue());
        }
        
        System.out.println("\nHashMap handles collisions using:");
        System.out.println("1. Chaining (linked list/tree for same hash bucket)");
        System.out.println("2. equals() method to distinguish between keys");
        System.out.println("3. Tree structure for long chains (Java 8+)");
    }
    
    private static void demonstratePerformanceCharacteristics() {
        System.out.println("\n=== Performance Characteristics ===");
        
        Map<Integer, String> hashMap = new HashMap<>();
        
        // Performance test: put operations
        long startTime = System.nanoTime();
        for (int i = 0; i < 100000; i++) {
            hashMap.put(i, "Value" + i);
        }
        long putTime = System.nanoTime() - startTime;
        
        // Performance test: get operations
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            int randomKey = (int) (Math.random() * 100000);
            hashMap.get(randomKey);
        }
        long getTime = System.nanoTime() - startTime;
        
        // Performance test: containsKey operations
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            int randomKey = (int) (Math.random() * 100000);
            hashMap.containsKey(randomKey);
        }
        long containsTime = System.nanoTime() - startTime;
        
        System.out.println("Performance results:");
        System.out.println("Put 100,000 elements: " + putTime + " ns");
        System.out.println("Get 10,000 elements: " + getTime + " ns");
        System.out.println("Contains 10,000 elements: " + containsTime + " ns");
        System.out.println("\nHashMap provides O(1) average-case performance");
        System.out.println("Worst case: O(n) if all keys hash to same bucket");
    }
    
    private static void demonstrateCapacityAndLoadFactor() {
        System.out.println("\n=== Capacity and Load Factor ===");
        
        // Default HashMap (capacity=16, load factor=0.75)
        Map<Integer, String> defaultMap = new HashMap<>();
        System.out.println("Default HashMap created");
        
        // HashMap with initial capacity
        Map<Integer, String> capacityMap = new HashMap<>(100);
        System.out.println("HashMap with initial capacity 100");
        
        // HashMap with capacity and load factor
        Map<Integer, String> customMap = new HashMap<>(50, 0.9f);
        System.out.println("HashMap with capacity 50 and load factor 0.9");
        
        // Demonstrate resizing effect
        Map<Integer, String> resizeTest = new HashMap<>(4); // Small initial capacity
        
        System.out.println("\nDemonstrating resize behavior:");
        for (int i = 0; i < 10; i++) {
            resizeTest.put(i, "Value" + i);
            if (i == 2 || i == 5 || i == 9) {
                System.out.println("After adding " + (i + 1) + " elements: " + 
                                 "size=" + resizeTest.size());
                // Internal capacity would have grown at load factor threshold
            }
        }
        
        System.out.println("\nLoad factor controls when HashMap resizes:");
        System.out.println("- Default load factor: 0.75");
        System.out.println("- Resize occurs when: size > capacity * load_factor");
        System.out.println("- New capacity: old_capacity * 2");
        System.out.println("- Choose initial capacity to minimize resizing");
    }
    
    // Helper class for collision demonstration
    static class HashKey {
        private int id;
        private String category;
        
        public HashKey(int id, String category) {
            this.id = id;
            this.category = category;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            HashKey hashKey = (HashKey) obj;
            return id == hashKey.id && Objects.equals(category, hashKey.category);
        }
        
        @Override
        public int hashCode() {
            // Deliberately simple hash function to create collisions
            return category.hashCode() % 3;
        }
        
        @Override
        public String toString() {
            return "HashKey{id=" + id + ", category='" + category + "'}";
        }
    }
}
```

</div>

</div>

---
layout: default
---

# LinkedHashMap and TreeMap

<div class="grid grid-cols-2 gap-6">

<div>

## LinkedHashMap Implementation

### LinkedHashMap Features
```java
import java.util.*;

public class LinkedHashMapDemo {
    public static void main(String[] args) {
        demonstrateInsertionOrder();
        demonstrateAccessOrder();
        demonstrateLRUCache();
        demonstratePerformanceComparison();
    }
    
    private static void demonstrateInsertionOrder() {
        System.out.println("=== LinkedHashMap Insertion Order ===");
        
        // HashMap - no guaranteed order
        Map<String, Integer> hashMap = new HashMap<>();
        hashMap.put("Zebra", 1);
        hashMap.put("Apple", 2);
        hashMap.put("Banana", 3);
        hashMap.put("Cherry", 4);
        
        System.out.println("HashMap order: " + hashMap);
        
        // LinkedHashMap - maintains insertion order
        Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put("Zebra", 1);
        linkedHashMap.put("Apple", 2);
        linkedHashMap.put("Banana", 3);
        linkedHashMap.put("Cherry", 4);
        
        System.out.println("LinkedHashMap order: " + linkedHashMap);
        
        // Order preserved during iteration
        System.out.print("Iteration order: ");
        for (Map.Entry<String, Integer> entry : linkedHashMap.entrySet()) {
            System.out.print(entry.getKey() + " ");
        }
        System.out.println();
        
        // Updating value doesn't change order
        linkedHashMap.put("Apple", 22); // Update existing key
        linkedHashMap.put("Date", 5);   // Add new key
        System.out.println("After update and addition: " + linkedHashMap);
    }
    
    private static void demonstrateAccessOrder() {
        System.out.println("\n=== LinkedHashMap Access Order ===");
        
        // LinkedHashMap with access order (true parameter)
        Map<String, String> accessOrderMap = new LinkedHashMap<>(16, 0.75f, true);
        
        accessOrderMap.put("First", "1st");
        accessOrderMap.put("Second", "2nd");
        accessOrderMap.put("Third", "3rd");
        accessOrderMap.put("Fourth", "4th");
        
        System.out.println("Initial order: " + accessOrderMap);
        
        // Access elements (get operations change order)
        accessOrderMap.get("Second"); // Moves "Second" to end
        System.out.println("After accessing 'Second': " + accessOrderMap);
        
        accessOrderMap.get("First");  // Moves "First" to end
        System.out.println("After accessing 'First': " + accessOrderMap);
        
        // put operation also counts as access
        accessOrderMap.put("Third", "3rd updated"); // Moves "Third" to end
        System.out.println("After updating 'Third': " + accessOrderMap);
        
        System.out.println("\nAccess order maintains recently accessed items at the end");
    }
    
    private static void demonstrateLRUCache() {
        System.out.println("\n=== LRU Cache Implementation ===");
        
        // LRU Cache with maximum capacity of 3
        LRUCache<String, String> cache = new LRUCache<>(3);
        
        System.out.println("Adding items to LRU cache (capacity=3):");
        
        cache.put("Page1", "Content1");
        System.out.println("Added Page1: " + cache);
        
        cache.put("Page2", "Content2");
        System.out.println("Added Page2: " + cache);
        
        cache.put("Page3", "Content3");
        System.out.println("Added Page3: " + cache);
        
        // Access Page1 (moves to end)
        cache.get("Page1");
        System.out.println("Accessed Page1: " + cache);
        
        // Add Page4 (should evict Page2 - least recently used)
        cache.put("Page4", "Content4");
        System.out.println("Added Page4 (Page2 evicted): " + cache);
        
        // Access Page3 and add Page5
        cache.get("Page3");
        cache.put("Page5", "Content5");
        System.out.println("Added Page5 (Page1 evicted): " + cache);
    }
    
    private static void demonstratePerformanceComparison() {
        System.out.println("\n=== Performance Comparison ===");
        
        int operations = 100000;
        
        // HashMap performance
        Map<Integer, String> hashMap = new HashMap<>();
        long startTime = System.nanoTime();
        for (int i = 0; i < operations; i++) {
            hashMap.put(i, "Value" + i);
        }
        long hashMapTime = System.nanoTime() - startTime;
        
        // LinkedHashMap performance
        Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
        startTime = System.nanoTime();
        for (int i = 0; i < operations; i++) {
            linkedHashMap.put(i, "Value" + i);
        }
        long linkedHashMapTime = System.nanoTime() - startTime;
        
        System.out.println("Performance for " + operations + " put operations:");
        System.out.println("HashMap: " + hashMapTime + " ns");
        System.out.println("LinkedHashMap: " + linkedHashMapTime + " ns");
        System.out.println("Overhead: " + 
                          ((double) linkedHashMapTime / hashMapTime) + "x");
        
        System.out.println("\nLinkedHashMap trades performance for order preservation");
        System.out.println("Additional memory overhead for maintaining doubly-linked list");
    }
    
    // LRU Cache implementation using LinkedHashMap
    static class LRUCache<K, V> extends LinkedHashMap<K, V> {
        private final int capacity;
        
        public LRUCache(int capacity) {
            super(capacity + 1, 1.0f, true); // access-order = true
            this.capacity = capacity;
        }
        
        @Override
        protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
            return size() > capacity;
        }
        
        @Override
        public String toString() {
            return "LRUCache" + super.toString();
        }
    }
}
```

</div>

<div>

## TreeMap Implementation

### TreeMap Features
```java
import java.util.*;
import java.util.concurrent.ConcurrentSkipListMap;

public class TreeMapDemo {
    public static void main(String[] args) {
        demonstrateNaturalOrdering();
        demonstrateCustomOrdering();
        demonstrateNavigationMethods();
        demonstrateSubMapOperations();
        demonstratePerformanceAnalysis();
    }
    
    private static void demonstrateNaturalOrdering() {
        System.out.println("=== TreeMap Natural Ordering ===");
        
        TreeMap<String, Integer> wordCounts = new TreeMap<>();
        
        // Add words in random order
        wordCounts.put("zebra", 1);
        wordCounts.put("apple", 5);
        wordCounts.put("banana", 3);
        wordCounts.put("cherry", 7);
        wordCounts.put("date", 2);
        
        System.out.println("TreeMap (alphabetically sorted): " + wordCounts);
        
        // Numeric keys are sorted numerically
        TreeMap<Integer, String> scores = new TreeMap<>();
        scores.put(85, "Bob");
        scores.put(92, "Alice");
        scores.put(78, "Charlie");
        scores.put(95, "Diana");
        
        System.out.println("Score TreeMap (numerically sorted): " + scores);
        
        // Iteration is in sorted order
        System.out.println("Iteration order:");
        for (Map.Entry<Integer, String> entry : scores.entrySet()) {
            System.out.println("  Score " + entry.getKey() + ": " + entry.getValue());
        }
    }
    
    private static void demonstrateCustomOrdering() {
        System.out.println("\n=== TreeMap Custom Ordering ===");
        
        // Reverse order comparator
        TreeMap<String, Integer> reverseMap = new TreeMap<>(Collections.reverseOrder());
        reverseMap.put("Alpha", 1);
        reverseMap.put("Beta", 2);
        reverseMap.put("Gamma", 3);
        reverseMap.put("Delta", 4);
        
        System.out.println("Reverse alphabetical order: " + reverseMap);
        
        // Custom comparator - by string length
        TreeMap<String, Integer> lengthMap = new TreeMap<>(
            Comparator.comparing(String::length).thenComparing(String::compareTo)
        );
        
        lengthMap.put("Java", 1);
        lengthMap.put("C", 2);
        lengthMap.put("Python", 3);
        lengthMap.put("Go", 4);
        lengthMap.put("JavaScript", 5);
        lengthMap.put("C++", 6);
        
        System.out.println("Length-based ordering: " + lengthMap);
        
        // Complex object sorting
        TreeMap<Person, String> personMap = new TreeMap<>(
            Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName)
        );
        
        personMap.put(new Person("Alice", 30), "Engineer");
        personMap.put(new Person("Bob", 25), "Designer");
        personMap.put(new Person("Charlie", 30), "Manager"); // Same age as Alice
        personMap.put(new Person("Diana", 28), "Analyst");
        
        System.out.println("Person map (by age, then name):");
        for (Map.Entry<Person, String> entry : personMap.entrySet()) {
            System.out.println("  " + entry.getKey() + " -> " + entry.getValue());
        }
    }
    
    private static void demonstrateNavigationMethods() {
        System.out.println("\n=== TreeMap Navigation Methods ===");
        
        NavigableMap<Integer, String> treeMap = new TreeMap<>();
        treeMap.put(10, "Ten");
        treeMap.put(20, "Twenty");
        treeMap.put(30, "Thirty");
        treeMap.put(40, "Forty");
        treeMap.put(50, "Fifty");
        
        System.out.println("TreeMap: " + treeMap);
        
        // Navigation methods
        System.out.println("firstKey(): " + treeMap.firstKey());
        System.out.println("lastKey(): " + treeMap.lastKey());
        System.out.println("lowerKey(35): " + treeMap.lowerKey(35));   // < 35
        System.out.println("floorKey(35): " + treeMap.floorKey(35));   // <= 35
        System.out.println("ceilingKey(35): " + treeMap.ceilingKey(35)); // >= 35
        System.out.println("higherKey(35): " + treeMap.higherKey(35)); // > 35
        
        // Entry methods
        Map.Entry<Integer, String> firstEntry = treeMap.firstEntry();
        Map.Entry<Integer, String> lastEntry = treeMap.lastEntry();
        
        System.out.println("firstEntry(): " + firstEntry);
        System.out.println("lastEntry(): " + lastEntry);
        
        // Poll methods (remove and return)
        System.out.println("pollFirstEntry(): " + treeMap.pollFirstEntry());
        System.out.println("pollLastEntry(): " + treeMap.pollLastEntry());
        System.out.println("After polling: " + treeMap);
        
        // Descending view
        NavigableMap<Integer, String> descendingMap = treeMap.descendingMap();
        System.out.println("Descending view: " + descendingMap);
        
        // Descending key set
        NavigableSet<Integer> descendingKeys = treeMap.descendingKeySet();
        System.out.println("Descending keys: " + descendingKeys);
    }
    
    private static void demonstrateSubMapOperations() {
        System.out.println("\n=== TreeMap SubMap Operations ===");
        
        TreeMap<Integer, String> fullMap = new TreeMap<>();
        for (int i = 10; i <= 100; i += 10) {
            fullMap.put(i, "Value" + i);
        }
        
        System.out.println("Full map: " + fullMap);
        
        // SubMap operations
        SortedMap<Integer, String> headMap = fullMap.headMap(50); // < 50
        SortedMap<Integer, String> tailMap = fullMap.tailMap(50); // >= 50
        SortedMap<Integer, String> subMap = fullMap.subMap(30, 70); // [30, 70)
        
        System.out.println("headMap(50): " + headMap);
        System.out.println("tailMap(50): " + tailMap);
        System.out.println("subMap(30, 70): " + subMap);
        
        // NavigableMap versions with inclusive/exclusive bounds
        NavigableMap<Integer, String> navMap = fullMap;
        
        NavigableMap<Integer, String> headMapInclusive = navMap.headMap(50, true); // <= 50
        NavigableMap<Integer, String> subMapCustom = navMap.subMap(30, false, 70, true); // (30, 70]
        
        System.out.println("headMap(50, inclusive): " + headMapInclusive);
        System.out.println("subMap(30, false, 70, true): " + subMapCustom);
        
        // SubMaps are views - changes reflect in original
        headMap.put(25, "Value25"); // Adds to original map
        System.out.println("After adding to headMap: " + fullMap);
        
        // Range validation
        try {
            headMap.put(60, "Value60"); // Outside range
        } catch (IllegalArgumentException e) {
            System.out.println("Cannot add 60 to headMap: outside range");
        }
    }
    
    private static void demonstratePerformanceAnalysis() {
        System.out.println("\n=== Performance Analysis ===");
        
        int operations = 100000;
        
        // TreeMap performance
        Map<Integer, String> treeMap = new TreeMap<>();
        long startTime = System.nanoTime();
        for (int i = 0; i < operations; i++) {
            treeMap.put(i, "Value" + i);
        }
        long treeMapTime = System.nanoTime() - startTime;
        
        // HashMap performance for comparison
        Map<Integer, String> hashMap = new HashMap<>();
        startTime = System.nanoTime();
        for (int i = 0; i < operations; i++) {
            hashMap.put(i, "Value" + i);
        }
        long hashMapTime = System.nanoTime() - startTime;
        
        System.out.println("Performance for " + operations + " put operations:");
        System.out.println("TreeMap: " + treeMapTime + " ns (O(log n) per operation)");
        System.out.println("HashMap: " + hashMapTime + " ns (O(1) average per operation)");
        System.out.println("HashMap is " + ((double) treeMapTime / hashMapTime) + "x faster");
        
        // Search performance comparison
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            int key = (int) (Math.random() * operations);
            treeMap.containsKey(key);
        }
        long treeMapSearchTime = System.nanoTime() - startTime;
        
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            int key = (int) (Math.random() * operations);
            hashMap.containsKey(key);
        }
        long hashMapSearchTime = System.nanoTime() - startTime;
        
        System.out.println("\nSearch performance (10,000 operations):");
        System.out.println("TreeMap: " + treeMapSearchTime + " ns");
        System.out.println("HashMap: " + hashMapSearchTime + " ns");
        
        System.out.println("\nTreeMap advantages:");
        System.out.println("- Sorted order iteration");
        System.out.println("- Range queries (subMap, headMap, tailMap)");
        System.out.println("- Navigation methods (floor, ceiling, etc.)");
        System.out.println("- Consistent O(log n) performance");
        
        System.out.println("\nHashMap advantages:");
        System.out.println("- Faster basic operations O(1) average");
        System.out.println("- Lower memory overhead");
        System.out.println("- No ordering requirements");
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

# Advanced Map Operations and Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Map Utility Methods and Patterns

### Modern Map Operations (Java 8+)
```java
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Function;
import java.util.stream.Collectors;

public class AdvancedMapOperations {
    public static void main(String[] args) {
        demonstrateComputeMethods();
        demonstrateMergeMethods();
        demonstrateStreamOperations();
        demonstratePatterns();
    }
    
    private static void demonstrateComputeMethods() {
        System.out.println("=== Compute Methods ===");
        
        Map<String, Integer> wordCount = new HashMap<>();
        String[] words = {"java", "python", "java", "javascript", "python", "java", "go"};
        
        // Traditional approach
        for (String word : words) {
            if (wordCount.containsKey(word)) {
                wordCount.put(word, wordCount.get(word) + 1);
            } else {
                wordCount.put(word, 1);
            }
        }
        System.out.println("Traditional word count: " + wordCount);
        
        // Using compute methods
        Map<String, Integer> betterWordCount = new HashMap<>();
        
        for (String word : words) {
            // compute: always calculates new value
            betterWordCount.compute(word, (key, value) -> 
                (value == null) ? 1 : value + 1);
        }
        System.out.println("Using compute: " + betterWordCount);
        
        // Using merge for same result
        Map<String, Integer> mergeWordCount = new HashMap<>();
        for (String word : words) {
            mergeWordCount.merge(word, 1, Integer::sum);
        }
        System.out.println("Using merge: " + mergeWordCount);
        
        // computeIfAbsent - for caching pattern
        Map<String, List<String>> categories = new HashMap<>();
        
        // Add items to categories
        addToCategory(categories, "programming", "Java");
        addToCategory(categories, "programming", "Python");
        addToCategory(categories, "database", "MySQL");
        addToCategory(categories, "programming", "JavaScript");
        addToCategory(categories, "database", "PostgreSQL");
        
        System.out.println("Categories: " + categories);
    }
    
    private static void addToCategory(Map<String, List<String>> categories, 
                                    String category, String item) {
        // Old way
        // List<String> items = categories.get(category);
        // if (items == null) {
        //     items = new ArrayList<>();
        //     categories.put(category, items);
        // }
        // items.add(item);
        
        // New way with computeIfAbsent
        categories.computeIfAbsent(category, k -> new ArrayList<>()).add(item);
    }
    
    private static void demonstrateMergeMethods() {
        System.out.println("\n=== Merge Methods ===");
        
        // Merging two maps
        Map<String, Integer> sales1 = new HashMap<>();
        sales1.put("Product A", 100);
        sales1.put("Product B", 150);
        sales1.put("Product C", 80);
        
        Map<String, Integer> sales2 = new HashMap<>();
        sales2.put("Product B", 120); // Overlapping key
        sales2.put("Product C", 90);  // Overlapping key
        sales2.put("Product D", 200); // New key
        
        System.out.println("Sales Q1: " + sales1);
        System.out.println("Sales Q2: " + sales2);
        
        // Merge sales2 into sales1
        Map<String, Integer> totalSales = new HashMap<>(sales1);
        sales2.forEach((product, amount) -> 
            totalSales.merge(product, amount, Integer::sum));
        
        System.out.println("Total sales: " + totalSales);
        
        // Replace vs merge behavior
        Map<String, String> config1 = new HashMap<>();
        config1.put("timeout", "30");
        config1.put("retries", "3");
        
        Map<String, String> config2 = new HashMap<>();
        config2.put("timeout", "60");
        config2.put("cache", "true");
        
        // Using putAll (replaces values)
        Map<String, String> combinedReplace = new HashMap<>(config1);
        combinedReplace.putAll(config2);
        System.out.println("putAll result: " + combinedReplace);
        
        // Using merge (can combine values)
        Map<String, String> combinedMerge = new HashMap<>(config1);
        config2.forEach((key, value) -> 
            combinedMerge.merge(key, value, (oldVal, newVal) -> oldVal + "," + newVal));
        System.out.println("merge result: " + combinedMerge);
    }
    
    private static void demonstrateStreamOperations() {
        System.out.println("\n=== Stream Operations with Maps ===");
        
        Map<String, Integer> inventory = new HashMap<>();
        inventory.put("Laptops", 15);
        inventory.put("Smartphones", 32);
        inventory.put("Tablets", 8);
        inventory.put("Monitors", 22);
        inventory.put("Keyboards", 45);
        
        System.out.println("Inventory: " + inventory);
        
        // Filter entries
        Map<String, Integer> lowStock = inventory.entrySet().stream()
            .filter(entry -> entry.getValue() < 20)
            .collect(Collectors.toMap(
                Map.Entry::getKey, 
                Map.Entry::getValue));
        System.out.println("Low stock items: " + lowStock);
        
        // Transform values
        Map<String, String> stockStatus = inventory.entrySet().stream()
            .collect(Collectors.toMap(
                Map.Entry::getKey,
                entry -> entry.getValue() > 20 ? "High" : "Low"));
        System.out.println("Stock status: " + stockStatus);
        
        // Group by value ranges
        Map<String, List<String>> stockRanges = inventory.entrySet().stream()
            .collect(Collectors.groupingBy(
                entry -> {
                    int qty = entry.getValue();
                    if (qty < 15) return "Low";
                    else if (qty < 30) return "Medium";
                    else return "High";
                },
                Collectors.mapping(Map.Entry::getKey, Collectors.toList())
            ));
        System.out.println("Stock ranges: " + stockRanges);
        
        // Calculate statistics
        IntSummaryStatistics stats = inventory.values().stream()
            .mapToInt(Integer::intValue)
            .summaryStatistics();
        
        System.out.println("Inventory statistics:");
        System.out.println("  Total items: " + stats.getSum());
        System.out.println("  Average: " + String.format("%.1f", stats.getAverage()));
        System.out.println("  Min: " + stats.getMin());
        System.out.println("  Max: " + stats.getMax());
    }
    
    private static void demonstratePatterns() {
        System.out.println("\n=== Common Map Patterns ===");
        
        // Pattern 1: Frequency counter
        String text = "the quick brown fox jumps over the lazy dog the fox";
        Map<String, Long> wordFrequency = Arrays.stream(text.split("\\s+"))
            .collect(Collectors.groupingBy(
                Function.identity(),
                Collectors.counting()));
        System.out.println("Word frequency: " + wordFrequency);
        
        // Pattern 2: Index building
        List<String> words = Arrays.asList("apple", "banana", "apricot", "blueberry", "cherry");
        Map<Character, List<String>> index = words.stream()
            .collect(Collectors.groupingBy(word -> word.charAt(0)));
        System.out.println("First letter index: " + index);
        
        // Pattern 3: Lookup table
        Map<Integer, String> statusCodes = Map.of(
            200, "OK",
            404, "Not Found",
            500, "Internal Server Error",
            403, "Forbidden"
        );
        
        int[] codes = {200, 404, 418, 500};
        for (int code : codes) {
            String status = statusCodes.getOrDefault(code, "Unknown Status");
            System.out.println("HTTP " + code + ": " + status);
        }
        
        // Pattern 4: Multi-value map
        Map<String, Set<String>> authorBooks = new HashMap<>();
        addBook(authorBooks, "Martin Fowler", "Refactoring");
        addBook(authorBooks, "Martin Fowler", "Patterns of Enterprise Application Architecture");
        addBook(authorBooks, "Robert Martin", "Clean Code");
        addBook(authorBooks, "Robert Martin", "Clean Architecture");
        addBook(authorBooks, "Martin Fowler", "Domain-Specific Languages");
        
        System.out.println("Author books: " + authorBooks);
        
        // Pattern 5: Caching with computeIfAbsent
        Map<String, ExpensiveResult> cache = new HashMap<>();
        
        String[] queries = {"query1", "query2", "query1", "query3", "query2"};
        for (String query : queries) {
            ExpensiveResult result = cache.computeIfAbsent(query, 
                key -> performExpensiveOperation(key));
            System.out.println("Query: " + query + " -> " + result.getValue() + 
                             " (cached: " + result.isCached() + ")");
        }
    }
    
    private static void addBook(Map<String, Set<String>> authorBooks, 
                              String author, String book) {
        authorBooks.computeIfAbsent(author, k -> new HashSet<>()).add(book);
    }
    
    private static ExpensiveResult performExpensiveOperation(String query) {
        // Simulate expensive operation
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return new ExpensiveResult("Result for " + query, false);
    }
    
    static class ExpensiveResult {
        private String value;
        private boolean cached;
        
        public ExpensiveResult(String value, boolean cached) {
            this.value = value;
            this.cached = cached;
        }
        
        public String getValue() { return value; }
        public boolean isCached() { return cached; }
    }
}
```

</div>

<div>

## Thread-Safe Maps and Concurrent Operations

### Concurrent Map Implementations
```java
import java.util.*;
import java.util.concurrent.*;

public class ConcurrentMapDemo {
    public static void main(String[] args) throws InterruptedException {
        demonstrateConcurrentHashMap();
        demonstrateAtomicOperations();
        demonstrateParallelOperations();
        comparePerformance();
    }
    
    private static void demonstrateConcurrentHashMap() throws InterruptedException {
        System.out.println("=== ConcurrentHashMap Demo ===");
        
        // Problem with regular HashMap in concurrent environment
        Map<String, Integer> unsafeMap = new HashMap<>();
        
        // Safe concurrent map
        ConcurrentMap<String, Integer> safeMap = new ConcurrentHashMap<>();
        
        int threadCount = 10;
        int operationsPerThread = 1000;
        CountDownLatch latch = new CountDownLatch(threadCount);
        
        // Launch threads that modify the maps
        for (int i = 0; i < threadCount; i++) {
            final int threadId = i;
            new Thread(() -> {
                try {
                    for (int j = 0; j < operationsPerThread; j++) {
                        String key = "key" + (j % 100);
                        
                        // Unsafe operation on HashMap
                        try {
                            unsafeMap.merge(key, 1, Integer::sum);
                        } catch (Exception e) {
                            // May throw ConcurrentModificationException or cause corruption
                        }
                        
                        // Safe operation on ConcurrentHashMap
                        safeMap.merge(key, 1, Integer::sum);
                    }
                } finally {
                    latch.countDown();
                }
            }).start();
        }
        
        latch.await(); // Wait for all threads to complete
        
        System.out.println("Expected total operations: " + (threadCount * operationsPerThread));
        System.out.println("Unsafe map size: " + unsafeMap.size());
        System.out.println("Safe map size: " + safeMap.size());
        
        // Verify safe map integrity
        int totalOperations = safeMap.values().stream().mapToInt(Integer::intValue).sum();
        System.out.println("Safe map total operations: " + totalOperations);
    }
    
    private static void demonstrateAtomicOperations() {
        System.out.println("\n=== Atomic Operations ===");
        
        ConcurrentMap<String, AtomicInteger> counters = new ConcurrentHashMap<>();
        
        // Thread-safe counter increment
        String[] events = {"login", "logout", "purchase", "login", "purchase", "login"};
        
        for (String event : events) {
            // Old way - not atomic
            // counters.putIfAbsent(event, new AtomicInteger(0));
            // counters.get(event).incrementAndGet();
            
            // New way - atomic
            counters.computeIfAbsent(event, k -> new AtomicInteger(0))
                   .incrementAndGet();
        }
        
        System.out.println("Event counters: " + counters);
        
        // Demonstrate putIfAbsent atomicity
        ConcurrentMap<String, String> cache = new ConcurrentHashMap<>();
        
        // Atomic "get or create" pattern
        String result = cache.putIfAbsent("key1", "value1");
        System.out.println("First putIfAbsent result: " + result); // null
        
        result = cache.putIfAbsent("key1", "value2");
        System.out.println("Second putIfAbsent result: " + result); // value1
        System.out.println("Cache contents: " + cache);
        
        // replace operations
        boolean replaced = cache.replace("key1", "value1", "newValue1");
        System.out.println("Replaced: " + replaced);
        System.out.println("After replace: " + cache);
    }
    
    private static void demonstrateParallelOperations() {
        System.out.println("\n=== Parallel Operations ===");
        
        ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
        
        // Populate map
        for (int i = 1; i <= 1000; i++) {
            map.put("key" + i, i);
        }
        
        // Parallel forEach
        System.out.println("Parallel forEach (sum of values):");
        LongAdder sum = new LongAdder();
        map.forEach(100, (key, value) -> sum.add(value)); // parallelism threshold = 100
        System.out.println("Sum: " + sum.sum());
        
        // Parallel search
        String found = map.search(100, (key, value) -> 
            value > 500 ? key : null);
        System.out.println("First key with value > 500: " + found);
        
        // Parallel reduce
        Integer maxValue = map.reduce(100, 
            (key, value) -> value, // transformer
            Integer::max);         // reducer
        System.out.println("Maximum value: " + maxValue);
        
        // reduceValues
        Integer totalSum = map.reduceValues(100, Integer::sum);
        System.out.println("Total sum (reduceValues): " + totalSum);
        
        // Parallel key operations
        Set<String> longKeys = ConcurrentHashMap.newKeySet();
        map.forEachKey(100, key -> {
            if (key.length() > 4) {
                longKeys.add(key);
            }
        });
        System.out.println("Keys longer than 4 chars: " + longKeys.size());
    }
    
    private static void comparePerformance() throws InterruptedException {
        System.out.println("\n=== Performance Comparison ===");
        
        int threadCount = 8;
        int operationsPerThread = 100000;
        
        // Test ConcurrentHashMap
        Map<Integer, Integer> concurrentMap = new ConcurrentHashMap<>();
        long startTime = System.nanoTime();
        runConcurrentTest(concurrentMap, threadCount, operationsPerThread);
        long concurrentTime = System.nanoTime() - startTime;
        
        // Test synchronized HashMap
        Map<Integer, Integer> syncMap = Collections.synchronizedMap(new HashMap<>());
        startTime = System.nanoTime();
        runConcurrentTest(syncMap, threadCount, operationsPerThread);
        long syncTime = System.nanoTime() - startTime;
        
        // Test Hashtable
        Map<Integer, Integer> hashtable = new Hashtable<>();
        startTime = System.nanoTime();
        runConcurrentTest(hashtable, threadCount, operationsPerThread);
        long hashtableTime = System.nanoTime() - startTime;
        
        System.out.println("Performance results (" + threadCount + " threads, " + 
                          operationsPerThread + " ops/thread):");
        System.out.println("ConcurrentHashMap: " + concurrentTime / 1_000_000 + " ms");
        System.out.println("Synchronized HashMap: " + syncTime / 1_000_000 + " ms");
        System.out.println("Hashtable: " + hashtableTime / 1_000_000 + " ms");
        
        System.out.println("\nPerformance ratios:");
        System.out.println("ConcurrentHashMap vs Synchronized: " + 
                          String.format("%.2fx faster", (double) syncTime / concurrentTime));
        System.out.println("ConcurrentHashMap vs Hashtable: " + 
                          String.format("%.2fx faster", (double) hashtableTime / concurrentTime));
        
        System.out.println("\nConcurrentHashMap advantages:");
        System.out.println("- Lock-free reads in most cases");
        System.out.println("- Segmented locking for writes");
        System.out.println("- Better scalability with multiple threads");
        System.out.println("- Atomic compound operations");
    }
    
    private static void runConcurrentTest(Map<Integer, Integer> map, 
                                        int threadCount, 
                                        int operationsPerThread) throws InterruptedException {
        CountDownLatch latch = new CountDownLatch(threadCount);
        
        for (int i = 0; i < threadCount; i++) {
            new Thread(() -> {
                try {
                    for (int j = 0; j < operationsPerThread; j++) {
                        int key = j % 1000; // Reuse keys to create contention
                        
                        // Mix of operations
                        if (j % 3 == 0) {
                            map.put(key, j);
                        } else if (j % 3 == 1) {
                            map.get(key);
                        } else {
                            map.remove(key);
                        }
                    }
                } finally {
                    latch.countDown();
                }
            }).start();
        }
        
        latch.await();
    }
}

// Weak reference map for memory-sensitive caching
class WeakValueMap<K, V> {
    private final ConcurrentHashMap<K, WeakReference<V>> map = new ConcurrentHashMap<>();
    private final ReferenceQueue<V> queue = new ReferenceQueue<>();
    
    public void put(K key, V value) {
        cleanUp();
        map.put(key, new WeakReference<>(value, queue));
    }
    
    public V get(K key) {
        cleanUp();
        WeakReference<V> ref = map.get(key);
        if (ref != null) {
            V value = ref.get();
            if (value == null) {
                map.remove(key); // Clean up stale reference
            }
            return value;
        }
        return null;
    }
    
    private void cleanUp() {
        Reference<? extends V> ref;
        while ((ref = queue.poll()) != null) {
            // Remove stale entries
            map.values().remove(ref);
        }
    }
    
    public int size() {
        cleanUp();
        return map.size();
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

- 🗺️ **Map Interface**: Key-value pair storage with unique keys
- 🔑 **HashMap**: Hash table implementation with O(1) average performance
- ⚡ **LinkedHashMap**: HashMap with insertion/access order preservation
- 🌳 **TreeMap**: Red-black tree with sorted key ordering
- 🎯 **ConcurrentHashMap**: Thread-safe map with excellent scalability
- 🔍 **Navigation**: TreeMap's NavigableMap methods for range operations
- 📊 **Modern Operations**: compute, merge, stream integration
- 💡 **Patterns**: Caching, indexing, counting, grouping

</v-clicks>

## Map Implementation Comparison

| Feature | HashMap | LinkedHashMap | TreeMap | ConcurrentHashMap |
|---------|---------|---------------|---------|-------------------|
| **Ordering** | None | Insertion/Access | Sorted | None |
| **Null Keys** | 1 allowed | 1 allowed | Not allowed | Not allowed |
| **Null Values** | Allowed | Allowed | Allowed | Not allowed |
| **Performance** | O(1) avg | O(1) avg | O(log n) | O(1) avg |
| **Thread Safe** | No | No | No | Yes |
| **Memory** | Low | Medium | High | Medium |

## Key Operations Performance

### HashMap/LinkedHashMap/ConcurrentHashMap
- **get()**: O(1) average, O(n) worst case
- **put()**: O(1) average, O(n) worst case
- **remove()**: O(1) average, O(n) worst case
- **containsKey()**: O(1) average, O(n) worst case

### TreeMap
- **get()**: O(log n)
- **put()**: O(log n)
- **remove()**: O(log n)
- **containsKey()**: O(log n)

</div>

<div>

## Important Concepts Recap

<v-clicks>

- **Hash Function**: Maps keys to array indices for O(1) access
- **Collision Resolution**: Chaining and tree structure for same-hash keys
- **Load Factor**: Ratio that triggers resize (default 0.75)
- **Fail-Fast Iterators**: Detect concurrent modifications
- **View Collections**: keySet(), values(), entrySet() are live views
- **Navigation Methods**: TreeMap's floor, ceiling, higher, lower
- **Atomic Operations**: ConcurrentMap's thread-safe compound operations
- **Weak References**: Memory-sensitive caching patterns

</v-clicks>

### Modern Map Patterns (Java 8+)

#### Compute Operations
```java
// Frequency counting
map.merge(key, 1, Integer::sum);

// Caching pattern
map.computeIfAbsent(key, k -> expensiveOperation(k));

// Update if present
map.computeIfPresent(key, (k, v) -> transform(v));
```

#### Stream Integration
```java
// Transform to new map
Map<K, V2> transformed = originalMap.entrySet()
    .stream()
    .collect(Collectors.toMap(
        Map.Entry::getKey,
        entry -> transform(entry.getValue())
    ));

// Group by criteria
Map<String, List<Person>> byAge = people.stream()
    .collect(Collectors.groupingBy(Person::getAgeGroup));
```

## When to Use Each Map

### HashMap
- General-purpose mapping
- Fast access required
- Order not important
- Single-threaded access

### LinkedHashMap
- Need predictable iteration order
- LRU cache implementation
- Debugging/logging scenarios

### TreeMap
- Need sorted keys
- Range queries required
- Navigation operations needed
- Consistent performance preferred

### ConcurrentHashMap
- Multi-threaded environment
- High-performance concurrent access
- Atomic compound operations needed

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Map Collections Complete

**Lecture 36 Successfully Completed!**  
You now master Map collections and their practical applications

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for Collections Utilities! <carbon:arrow-right class="inline"/>
  </span>
</div>