---
theme: default
background: https://source.unsplash.com/1024x768/?list,set,data
title: List and Set Collections
info: |
  ## Java Programming (4343203)
  
  Lecture 35: List and Set Collections
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Explore List and Set collections in detail, their implementations, performance characteristics, and practical usage scenarios.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# List and Set Collections
## Lecture 35

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

- 📋 **Understand** List interface and its key characteristics
- 🔗 **Compare** ArrayList, LinkedList, and Vector implementations
- 📊 **Use** Set interface for unique element collections
- 🎯 **Differentiate** HashSet, LinkedHashSet, and TreeSet
- ⚡ **Choose** appropriate implementation based on performance needs
- 🔍 **Implement** searching, sorting, and manipulation operations
- 🛠️ **Apply** advanced List and Set operations effectively
- 💡 **Handle** concurrent modifications and thread safety

</v-clicks>

---
layout: default
---

# List Interface Deep Dive

<div class="grid grid-cols-2 gap-6">

<div>

## List Characteristics

### Key Features
- **Ordered Collection**: Elements maintain insertion order
- **Indexed Access**: Elements accessible by integer index
- **Allows Duplicates**: Same element can appear multiple times
- **Dynamic Size**: Can grow and shrink during runtime

### List Interface Methods
```java
// Index-based operations
E get(int index)
E set(int index, E element)
void add(int index, E element)  
E remove(int index)

// Search operations
int indexOf(Object o)
int lastIndexOf(Object o)

// Range view
List<E> subList(int fromIndex, int toIndex)

// List iterator
ListIterator<E> listIterator()
ListIterator<E> listIterator(int index)
```

## ArrayList Implementation

### ArrayList Characteristics
```java
public class ArrayListDemo {
    public static void main(String[] args) {
        demonstrateBasicOperations();
        demonstrateCapacityManagement();
        demonstratePerformanceCharacteristics();
        demonstrateCommonUseCases();
    }
    
    private static void demonstrateBasicOperations() {
        System.out.println("=== ArrayList Basic Operations ===");
        
        // Creation and initialization
        List<String> fruits = new ArrayList<>();
        System.out.println("Initial size: " + fruits.size());
        
        // Adding elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        fruits.add("Date");
        System.out.println("After adding: " + fruits);
        
        // Index-based operations
        fruits.add(1, "Avocado"); // Insert at index 1
        System.out.println("After insert at index 1: " + fruits);
        
        // Accessing elements
        String firstFruit = fruits.get(0);
        String lastFruit = fruits.get(fruits.size() - 1);
        System.out.println("First: " + firstFruit + ", Last: " + lastFruit);
        
        // Modifying elements
        String oldValue = fruits.set(2, "Coconut");
        System.out.println("Replaced '" + oldValue + "' with 'Coconut': " + fruits);
        
        // Removing elements
        fruits.remove(0); // Remove by index
        fruits.remove("Date"); // Remove by object
        System.out.println("After removals: " + fruits);
        
        // Search operations
        int bananaIndex = fruits.indexOf("Banana");
        System.out.println("Index of 'Banana': " + bananaIndex);
        
        boolean hasCherry = fruits.contains("Cherry");
        System.out.println("Contains 'Cherry': " + hasCherry);
    }
    
    private static void demonstrateCapacityManagement() {
        System.out.println("\n=== ArrayList Capacity Management ===");
        
        // Default capacity
        ArrayList<Integer> numbers = new ArrayList<>();
        System.out.println("Default capacity demonstration:");
        
        for (int i = 1; i <= 15; i++) {
            numbers.add(i);
            if (i % 5 == 0) {
                System.out.println("Added " + i + " elements, size: " + numbers.size());
            }
        }
        
        // Pre-sized ArrayList for better performance
        ArrayList<Integer> preSized = new ArrayList<>(1000);
        long startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            preSized.add(i);
        }
        long preSizedTime = System.nanoTime() - startTime;
        
        // Default size ArrayList
        ArrayList<Integer> defaultSize = new ArrayList<>();
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            defaultSize.add(i);
        }
        long defaultTime = System.nanoTime() - startTime;
        
        System.out.println("Pre-sized ArrayList time: " + preSizedTime + " ns");
        System.out.println("Default size ArrayList time: " + defaultTime + " ns");
        System.out.println("Performance ratio: " + (double) defaultTime / preSizedTime);
        
        // trimToSize for memory efficiency
        ArrayList<String> oversized = new ArrayList<>(1000);
        oversized.add("One");
        oversized.add("Two");
        oversized.add("Three");
        
        System.out.println("Before trim - Size: " + oversized.size());
        oversized.trimToSize(); // Reduce capacity to match size
        System.out.println("After trimToSize - Size: " + oversized.size());
    }
    
    private static void demonstratePerformanceCharacteristics() {
        System.out.println("\n=== ArrayList Performance Characteristics ===");
        
        ArrayList<Integer> list = new ArrayList<>();
        
        // Fill with test data
        for (int i = 0; i < 10000; i++) {
            list.add(i);
        }
        
        // Random access performance (strength of ArrayList)
        long startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            int randomIndex = (int) (Math.random() * list.size());
            list.get(randomIndex);
        }
        long accessTime = System.nanoTime() - startTime;
        System.out.println("Random access (1000 operations): " + accessTime + " ns");
        
        // Insertion in middle performance (weakness of ArrayList)
        startTime = System.nanoTime();
        for (int i = 0; i < 100; i++) {
            list.add(list.size() / 2, -1); // Insert in middle
        }
        long insertTime = System.nanoTime() - startTime;
        System.out.println("Middle insertions (100 operations): " + insertTime + " ns");
        
        // Append performance (strength of ArrayList)
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            list.add(i);
        }
        long appendTime = System.nanoTime() - startTime;
        System.out.println("Append operations (1000 operations): " + appendTime + " ns");
    }
    
    private static void demonstrateCommonUseCases() {
        System.out.println("\n=== ArrayList Common Use Cases ===");
        
        // Use case 1: Collecting results
        List<String> results = new ArrayList<>();
        String[] data = {"apple", "banana", "cherry", "date", "elderberry"};
        
        // Filter strings longer than 5 characters
        for (String item : data) {
            if (item.length() > 5) {
                results.add(item);
            }
        }
        System.out.println("Filtered results: " + results);
        
        // Use case 2: Building dynamic content
        List<String> htmlLines = new ArrayList<>();
        htmlLines.add("<html>");
        htmlLines.add("<head><title>Dynamic Content</title></head>");
        htmlLines.add("<body>");
        
        for (int i = 1; i <= 3; i++) {
            htmlLines.add("  <h" + i + ">Heading " + i + "</h" + i + ">");
            htmlLines.add("  <p>This is paragraph " + i + "</p>");
        }
        
        htmlLines.add("</body>");
        htmlLines.add("</html>");
        
        System.out.println("Generated HTML:");
        htmlLines.forEach(System.out::println);
        
        // Use case 3: Maintaining order with duplicates
        List<String> playlist = new ArrayList<>();
        playlist.add("Song A");
        playlist.add("Song B");
        playlist.add("Song A"); // Duplicate allowed
        playlist.add("Song C");
        playlist.add("Song B"); // Another duplicate
        
        System.out.println("Playlist (with duplicates): " + playlist);
        
        // Use case 4: SubList operations
        List<String> topSongs = playlist.subList(0, 3);
        System.out.println("Top 3 songs: " + topSongs);
        
        // Modifying sublist affects original
        topSongs.set(0, "New Song A");
        System.out.println("After modifying sublist: " + playlist);
    }
}
```

</div>

<div>

## LinkedList Implementation

### LinkedList Characteristics
```java
import java.util.*;

public class LinkedListDemo {
    public static void main(String[] args) {
        demonstrateBasicOperations();
        demonstrateDequeOperations();
        demonstratePerformanceComparison();
        demonstrateMemoryEfficiency();
    }
    
    private static void demonstrateBasicOperations() {
        System.out.println("=== LinkedList Basic Operations ===");
        
        LinkedList<String> animals = new LinkedList<>();
        
        // Adding elements
        animals.add("Cat");
        animals.add("Dog");
        animals.add("Elephant");
        System.out.println("Initial list: " + animals);
        
        // LinkedList specific methods
        animals.addFirst("Ant");    // Add to beginning
        animals.addLast("Zebra");   // Add to end
        System.out.println("After addFirst/addLast: " + animals);
        
        // Accessing elements
        String first = animals.getFirst();
        String last = animals.getLast();
        System.out.println("First: " + first + ", Last: " + last);
        
        // Removing elements
        String removedFirst = animals.removeFirst();
        String removedLast = animals.removeLast();
        System.out.println("Removed first: " + removedFirst + ", last: " + removedLast);
        System.out.println("After removal: " + animals);
        
        // Peek operations (don't remove)
        String peekFirst = animals.peekFirst();
        String peekLast = animals.peekLast();
        System.out.println("Peek first: " + peekFirst + ", last: " + peekLast);
        System.out.println("List unchanged: " + animals);
    }
    
    private static void demonstrateDequeOperations() {
        System.out.println("\n=== LinkedList as Deque ===");
        
        Deque<Integer> deque = new LinkedList<>();
        
        // Adding elements from both ends
        deque.addFirst(2);
        deque.addFirst(1);
        deque.addLast(3);
        deque.addLast(4);
        System.out.println("Deque after additions: " + deque);
        
        // Using offer methods (similar to add, but returns boolean)
        deque.offerFirst(0);
        deque.offerLast(5);
        System.out.println("After offer operations: " + deque);
        
        // Poll operations (remove and return, or null if empty)
        Integer first = deque.pollFirst();
        Integer last = deque.pollLast();
        System.out.println("Polled first: " + first + ", last: " + last);
        System.out.println("Deque after polling: " + deque);
        
        // Stack operations (LIFO)
        System.out.println("Using as Stack (LIFO):");
        Deque<String> stack = new LinkedList<>();
        
        // Push elements
        stack.push("First");
        stack.push("Second");
        stack.push("Third");
        System.out.println("Stack after pushes: " + stack);
        
        // Pop elements
        while (!stack.isEmpty()) {
            System.out.println("Popped: " + stack.pop());
        }
        
        // Queue operations (FIFO)
        System.out.println("Using as Queue (FIFO):");
        Queue<String> queue = new LinkedList<>();
        
        // Enqueue elements
        queue.offer("First");
        queue.offer("Second");  
        queue.offer("Third");
        System.out.println("Queue after offers: " + queue);
        
        // Dequeue elements
        while (!queue.isEmpty()) {
            System.out.println("Dequeued: " + queue.poll());
        }
    }
    
    private static void demonstratePerformanceComparison() {
        System.out.println("\n=== ArrayList vs LinkedList Performance ===");
        
        int size = 100000;
        
        // Test 1: Random access
        ArrayList<Integer> arrayList = new ArrayList<>();
        LinkedList<Integer> linkedList = new LinkedList<>();
        
        // Populate both lists
        for (int i = 0; i < size; i++) {
            arrayList.add(i);
            linkedList.add(i);
        }
        
        // Random access test
        long startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            int randomIndex = (int) (Math.random() * size);
            arrayList.get(randomIndex);
        }
        long arrayListAccessTime = System.nanoTime() - startTime;
        
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            int randomIndex = (int) (Math.random() * size);
            linkedList.get(randomIndex);
        }
        long linkedListAccessTime = System.nanoTime() - startTime;
        
        System.out.println("Random Access (1000 operations):");
        System.out.println("ArrayList: " + arrayListAccessTime + " ns");
        System.out.println("LinkedList: " + linkedListAccessTime + " ns");
        System.out.println("ArrayList is " + (linkedListAccessTime / arrayListAccessTime) + 
                          "x faster for random access");
        
        // Test 2: Insertion at beginning
        ArrayList<Integer> arrayList2 = new ArrayList<>();
        LinkedList<Integer> linkedList2 = new LinkedList<>();
        
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            arrayList2.add(0, i); // Insert at beginning
        }
        long arrayListInsertTime = System.nanoTime() - startTime;
        
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            linkedList2.addFirst(i); // Insert at beginning
        }
        long linkedListInsertTime = System.nanoTime() - startTime;
        
        System.out.println("\nInsertion at Beginning (10000 operations):");
        System.out.println("ArrayList: " + arrayListInsertTime + " ns");
        System.out.println("LinkedList: " + linkedListInsertTime + " ns");
        System.out.println("LinkedList is " + (arrayListInsertTime / linkedListInsertTime) + 
                          "x faster for beginning insertion");
    }
    
    private static void demonstrateMemoryEfficiency() {
        System.out.println("\n=== Memory Efficiency Comparison ===");
        
        // ArrayList: stores only the objects + some overhead for the array
        // LinkedList: stores objects + node overhead (previous, next references)
        
        List<Integer> arrayList = new ArrayList<>();
        List<Integer> linkedList = new LinkedList<>();
        
        // Add same elements to both
        for (int i = 0; i < 1000; i++) {
            arrayList.add(i);
            linkedList.add(i);
        }
        
        System.out.println("Both lists contain 1000 integers");
        System.out.println("ArrayList: More memory efficient per element");
        System.out.println("LinkedList: Higher memory overhead due to node structure");
        System.out.println();
        System.out.println("ArrayList node: [value]");
        System.out.println("LinkedList node: [previous_ref][value][next_ref]");
        System.out.println();
        System.out.println("Choose ArrayList when:");
        System.out.println("- Memory efficiency is important");
        System.out.println("- Frequent random access needed");
        System.out.println("- More reads than insertions/deletions");
        System.out.println();
        System.out.println("Choose LinkedList when:");
        System.out.println("- Frequent insertions/deletions at beginning/end");
        System.out.println("- Implementing stack, queue, or deque");
        System.out.println("- Sequential access is sufficient");
    }
}
```

</div>

</div>

---
layout: default
---

# Set Interface Deep Dive

<div class="grid grid-cols-2 gap-6">

<div>

## Set Characteristics

### Key Features
- **No Duplicates**: Each element appears at most once
- **Mathematical Set**: Based on mathematical set theory
- **Unique Elements**: Duplicate additions are ignored
- **Implementations Vary**: Different ordering and performance characteristics

### HashSet Implementation
```java
import java.util.*;

public class HashSetDemo {
    public static void main(String[] args) {
        demonstrateBasicOperations();
        demonstrateSetOperations();
        demonstratePerformanceCharacteristics();
        demonstrateHashingConcepts();
    }
    
    private static void demonstrateBasicOperations() {
        System.out.println("=== HashSet Basic Operations ===");
        
        Set<String> colors = new HashSet<>();
        
        // Adding elements
        colors.add("Red");
        colors.add("Green");
        colors.add("Blue");
        colors.add("Red");    // Duplicate - will be ignored
        System.out.println("Colors set: " + colors);
        System.out.println("Size: " + colors.size()); // Size is 3, not 4
        
        // Checking existence
        System.out.println("Contains 'Red': " + colors.contains("Red"));
        System.out.println("Contains 'Yellow': " + colors.contains("Yellow"));
        
        // Removing elements
        boolean removed = colors.remove("Green");
        System.out.println("Removed 'Green': " + removed);
        System.out.println("After removal: " + colors);
        
        // Iteration (order is not guaranteed)
        System.out.print("Iterating colors: ");
        for (String color : colors) {
            System.out.print(color + " ");
        }
        System.out.println();
        
        // Converting to array
        String[] colorArray = colors.toArray(new String[0]);
        System.out.println("As array: " + Arrays.toString(colorArray));
    }
    
    private static void demonstrateSetOperations() {
        System.out.println("\n=== Mathematical Set Operations ===");
        
        Set<Integer> set1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Set<Integer> set2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8));
        
        System.out.println("Set1: " + set1);
        System.out.println("Set2: " + set2);
        
        // Union (set1 ∪ set2)
        Set<Integer> union = new HashSet<>(set1);
        union.addAll(set2);
        System.out.println("Union (set1 ∪ set2): " + union);
        
        // Intersection (set1 ∩ set2)
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        System.out.println("Intersection (set1 ∩ set2): " + intersection);
        
        // Difference (set1 - set2)
        Set<Integer> difference = new HashSet<>(set1);
        difference.removeAll(set2);
        System.out.println("Difference (set1 - set2): " + difference);
        
        // Symmetric difference ((set1 ∪ set2) - (set1 ∩ set2))
        Set<Integer> symmetricDiff = new HashSet<>(set1);
        symmetricDiff.addAll(set2); // Union
        Set<Integer> intersectionCopy = new HashSet<>(set1);
        intersectionCopy.retainAll(set2);
        symmetricDiff.removeAll(intersectionCopy); // Remove intersection
        System.out.println("Symmetric difference: " + symmetricDiff);
        
        // Subset check
        Set<Integer> subset = new HashSet<>(Arrays.asList(1, 2));
        boolean isSubset = set1.containsAll(subset);
        System.out.println(subset + " is subset of set1: " + isSubset);
        
        // Disjoint sets check
        Set<Integer> disjointSet = new HashSet<>(Arrays.asList(9, 10, 11));
        boolean areDisjoint = Collections.disjoint(set1, disjointSet);
        System.out.println("set1 and " + disjointSet + " are disjoint: " + areDisjoint);
    }
    
    private static void demonstratePerformanceCharacteristics() {
        System.out.println("\n=== HashSet Performance Characteristics ===");
        
        HashSet<Integer> hashSet = new HashSet<>();
        
        // Add performance test
        long startTime = System.nanoTime();
        for (int i = 0; i < 100000; i++) {
            hashSet.add(i);
        }
        long addTime = System.nanoTime() - startTime;
        System.out.println("Adding 100,000 elements: " + addTime + " ns");
        
        // Contains performance test (strength of HashSet)
        startTime = System.nanoTime();
        for (int i = 0; i < 10000; i++) {
            int randomElement = (int) (Math.random() * 100000);
            hashSet.contains(randomElement);
        }
        long containsTime = System.nanoTime() - startTime;
        System.out.println("10,000 contains operations: " + containsTime + " ns");
        
        // Remove performance test
        startTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            hashSet.remove(i);
        }
        long removeTime = System.nanoTime() - startTime;
        System.out.println("Removing 1,000 elements: " + removeTime + " ns");
        
        System.out.println("HashSet provides O(1) average-case performance for:");
        System.out.println("- add()");
        System.out.println("- remove()");
        System.out.println("- contains()");
    }
    
    private static void demonstrateHashingConcepts() {
        System.out.println("\n=== Hashing Concepts ===");
        
        // Demonstrate hash collision handling
        Set<HashObject> objectSet = new HashSet<>();
        
        // Objects with same hash code (collision)
        HashObject obj1 = new HashObject(1, "Same hash");
        HashObject obj2 = new HashObject(2, "Same hash");
        HashObject obj3 = new HashObject(1, "Same hash"); // Same as obj1
        
        objectSet.add(obj1);
        objectSet.add(obj2); // Different object, same hash
        objectSet.add(obj3); // Equal to obj1, should not be added
        
        System.out.println("Set size: " + objectSet.size());
        System.out.println("Objects in set:");
        for (HashObject obj : objectSet) {
            System.out.println("  " + obj);
        }
        
        // Demonstrate importance of hashCode and equals contract
        System.out.println("\nHash codes:");
        System.out.println("obj1 hash: " + obj1.hashCode());
        System.out.println("obj2 hash: " + obj2.hashCode());
        System.out.println("obj3 hash: " + obj3.hashCode());
        
        System.out.println("\nEquality checks:");
        System.out.println("obj1.equals(obj2): " + obj1.equals(obj2));
        System.out.println("obj1.equals(obj3): " + obj1.equals(obj3));
    }
    
    // Helper class to demonstrate hashing concepts
    static class HashObject {
        private int id;
        private String data;
        
        public HashObject(int id, String data) {
            this.id = id;
            this.data = data;
        }
        
        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            HashObject that = (HashObject) obj;
            return id == that.id && Objects.equals(data, that.data);
        }
        
        @Override
        public int hashCode() {
            // Intentionally simple hash function to demonstrate collisions
            return data.hashCode() % 3; // Will cause collisions
        }
        
        @Override
        public String toString() {
            return "HashObject{id=" + id + ", data='" + data + "'}";
        }
    }
}
```

</div>

<div>

## LinkedHashSet and TreeSet

### LinkedHashSet Implementation
```java
import java.util.*;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        demonstrateInsertionOrder();
        demonstratePerformanceComparison();
        demonstrateUseCases();
    }
    
    private static void demonstrateInsertionOrder() {
        System.out.println("=== LinkedHashSet Insertion Order ===");
        
        // HashSet - no guaranteed order
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Zebra");
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Cherry");
        System.out.println("HashSet order: " + hashSet);
        
        // LinkedHashSet - maintains insertion order
        Set<String> linkedHashSet = new LinkedHashSet<>();
        linkedHashSet.add("Zebra");
        linkedHashSet.add("Apple");
        linkedHashSet.add("Banana");
        linkedHashSet.add("Cherry");
        System.out.println("LinkedHashSet order: " + linkedHashSet);
        
        // Demonstrate that duplicates don't change order
        linkedHashSet.add("Apple"); // Already exists
        linkedHashSet.add("Date");  // New element
        System.out.println("After adding duplicate and new: " + linkedHashSet);
        
        // Order is preserved during iteration
        System.out.print("Iteration order: ");
        for (String fruit : linkedHashSet) {
            System.out.print(fruit + " ");
        }
        System.out.println();
    }
    
    private static void demonstratePerformanceComparison() {
        System.out.println("\n=== Performance Comparison ===");
        
        int iterations = 100000;
        
        // HashSet performance
        Set<Integer> hashSet = new HashSet<>();
        long startTime = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            hashSet.add(i);
        }
        long hashSetTime = System.nanoTime() - startTime;
        
        // LinkedHashSet performance
        Set<Integer> linkedHashSet = new LinkedHashSet<>();
        startTime = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            linkedHashSet.add(i);
        }
        long linkedHashSetTime = System.nanoTime() - startTime;
        
        System.out.println("Adding " + iterations + " elements:");
        System.out.println("HashSet: " + hashSetTime + " ns");
        System.out.println("LinkedHashSet: " + linkedHashSetTime + " ns");
        System.out.println("Performance overhead: " + 
                          ((double) linkedHashSetTime / hashSetTime) + "x");
        
        System.out.println("\nLinkedHashSet trades slight performance for order preservation");
    }
    
    private static void demonstrateUseCases() {
        System.out.println("\n=== LinkedHashSet Use Cases ===");
        
        // Use case 1: Removing duplicates while preserving order
        List<String> listWithDuplicates = Arrays.asList(
            "Java", "Python", "Java", "JavaScript", "Python", "C++", "Java"
        );
        
        System.out.println("Original list: " + listWithDuplicates);
        
        Set<String> uniqueLanguages = new LinkedHashSet<>(listWithDuplicates);
        System.out.println("Unique languages (order preserved): " + uniqueLanguages);
        
        // Convert back to list if needed
        List<String> uniqueList = new ArrayList<>(uniqueLanguages);
        System.out.println("As unique list: " + uniqueList);
        
        // Use case 2: LRU-like behavior (though not true LRU)
        Set<String> accessLog = new LinkedHashSet<>();
        
        String[] accesses = {"page1", "page2", "page3", "page1", "page4", "page2"};
        System.out.println("\nPage access simulation:");
        
        for (String page : accesses) {
            if (accessLog.contains(page)) {
                accessLog.remove(page); // Remove to add at end
            }
            accessLog.add(page); // Add at end (most recent)
            System.out.println("Accessed " + page + " -> Order: " + accessLog);
        }
    }
}

// TreeSet Implementation
public class TreeSetDemo {
    public static void main(String[] args) {
        demonstrateNaturalOrdering();
        demonstrateCustomOrdering();
        demonstrateNavigableSetMethods();
        demonstratePerformanceCharacteristics();
    }
    
    private static void demonstrateNaturalOrdering() {
        System.out.println("=== TreeSet Natural Ordering ===");
        
        TreeSet<Integer> numbers = new TreeSet<>();
        
        // Add numbers in random order
        int[] randomNumbers = {5, 2, 8, 1, 9, 3, 7, 4, 6};
        for (int num : randomNumbers) {
            numbers.add(num);
        }
        
        System.out.println("Added in order: " + Arrays.toString(randomNumbers));
        System.out.println("TreeSet (sorted): " + numbers);
        
        // String ordering
        TreeSet<String> words = new TreeSet<>();
        words.add("zebra");
        words.add("apple");
        words.add("banana");
        words.add("cherry");
        
        System.out.println("String TreeSet: " + words); // Alphabetical order
        
        // Automatic duplicate removal with sorting
        TreeSet<Double> scores = new TreeSet<>();
        scores.add(85.5);
        scores.add(92.0);
        scores.add(78.5);
        scores.add(85.5); // Duplicate
        scores.add(95.0);
        
        System.out.println("Scores (sorted, no duplicates): " + scores);
    }
    
    private static void demonstrateCustomOrdering() {
        System.out.println("\n=== TreeSet Custom Ordering ===");
        
        // Custom comparator - reverse order
        TreeSet<Integer> reverseNumbers = new TreeSet<>(Collections.reverseOrder());
        reverseNumbers.addAll(Arrays.asList(5, 2, 8, 1, 9));
        System.out.println("Reverse order numbers: " + reverseNumbers);
        
        // Custom comparator - string length
        TreeSet<String> lengthSorted = new TreeSet<>(Comparator.comparing(String::length));
        lengthSorted.add("Java");
        lengthSorted.add("C");
        lengthSorted.add("Python");
        lengthSorted.add("Go");
        lengthSorted.add("JavaScript");
        System.out.println("Length sorted strings: " + lengthSorted);
        
        // Complex custom ordering - Person by age, then by name
        TreeSet<Person> people = new TreeSet<>(
            Comparator.comparing(Person::getAge)
                     .thenComparing(Person::getName)
        );
        
        people.add(new Person("Alice", 30));
        people.add(new Person("Bob", 25));
        people.add(new Person("Charlie", 30)); // Same age as Alice
        people.add(new Person("David", 25));   // Same age as Bob
        
        System.out.println("People sorted by age, then name:");
        for (Person person : people) {
            System.out.println("  " + person);
        }
    }
    
    private static void demonstrateNavigableSetMethods() {
        System.out.println("\n=== NavigableSet Methods ===");
        
        NavigableSet<Integer> treeSet = new TreeSet<>();
        treeSet.addAll(Arrays.asList(10, 20, 30, 40, 50, 60, 70, 80, 90));
        
        System.out.println("TreeSet: " + treeSet);
        
        // Ceiling and floor methods
        System.out.println("ceiling(35): " + treeSet.ceiling(35)); // ≥35
        System.out.println("floor(35): " + treeSet.floor(35));     // ≤35
        System.out.println("higher(35): " + treeSet.higher(35));   // >35
        System.out.println("lower(35): " + treeSet.lower(35));     // <35
        
        // First and last
        System.out.println("first(): " + treeSet.first());
        System.out.println("last(): " + treeSet.last());
        
        // Poll methods (remove and return)
        System.out.println("pollFirst(): " + treeSet.pollFirst());
        System.out.println("pollLast(): " + treeSet.pollLast());
        System.out.println("After polling: " + treeSet);
        
        // Subset views
        SortedSet<Integer> headSet = treeSet.headSet(50); // < 50
        SortedSet<Integer> tailSet = treeSet.tailSet(50); // ≥ 50
        NavigableSet<Integer> subSet = treeSet.subSet(30, true, 70, false); // [30, 70)
        
        System.out.println("headSet(50): " + headSet);
        System.out.println("tailSet(50): " + tailSet);
        System.out.println("subSet(30, 70): " + subSet);
        
        // Descending view
        NavigableSet<Integer> descendingSet = treeSet.descendingSet();
        System.out.println("Descending view: " + descendingSet);
    }
    
    private static void demonstratePerformanceCharacteristics() {
        System.out.println("\n=== TreeSet Performance Characteristics ===");
        
        TreeSet<Integer> treeSet = new TreeSet<>();
        HashSet<Integer> hashSet = new HashSet<>();
        
        // Add performance comparison
        long startTime = System.nanoTime();
        for (int i = 0; i < 100000; i++) {
            treeSet.add(i);
        }
        long treeSetAddTime = System.nanoTime() - startTime;
        
        startTime = System.nanoTime();
        for (int i = 0; i < 100000; i++) {
            hashSet.add(i);
        }
        long hashSetAddTime = System.nanoTime() - startTime;
        
        System.out.println("Adding 100,000 elements:");
        System.out.println("TreeSet: " + treeSetAddTime + " ns (O(log n) per operation)");
        System.out.println("HashSet: " + hashSetAddTime + " ns (O(1) average per operation)");
        System.out.println("HashSet is " + (treeSetAddTime / hashSetAddTime) + "x faster");
        
        System.out.println("\nTreeSet advantages:");
        System.out.println("- Maintains sorted order");
        System.out.println("- Range operations (subSet, headSet, tailSet)");
        System.out.println("- NavigableSet methods (ceiling, floor, etc.)");
        System.out.println("- No hash code requirements");
        
        System.out.println("\nHashSet advantages:");
        System.out.println("- Faster basic operations (O(1) vs O(log n))");
        System.out.println("- Lower memory overhead");
        System.out.println("- No ordering requirements on elements");
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

# Summary and Key Takeaways

<div class="grid grid-cols-2 gap-6">

<div>

## What We Learned

<v-clicks>

- 📋 **List Interface**: Ordered collections with indexed access and duplicates
- 🔗 **ArrayList**: Dynamic array with fast random access
- 📊 **LinkedList**: Doubly-linked list with fast insertion/deletion
- 🎯 **Set Interface**: Collections with unique elements only
- ⚡ **HashSet**: Hash table implementation with O(1) operations
- 🔍 **LinkedHashSet**: HashSet with insertion order preservation
- 🌳 **TreeSet**: Red-black tree with sorted elements
- 💡 **Performance Trade-offs**: Speed vs order vs memory

</v-clicks>

## Implementation Comparison

| Feature | ArrayList | LinkedList | HashSet | LinkedHashSet | TreeSet |
|---------|-----------|------------|---------|---------------|---------|
| **Order** | Insertion | Insertion | None | Insertion | Sorted |
| **Duplicates** | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Random Access** | O(1) | O(n) | N/A | N/A | N/A |
| **Insertion** | O(1)* | O(1) | O(1) | O(1) | O(log n) |
| **Search** | O(n) | O(n) | O(1) | O(1) | O(log n) |
| **Memory** | Low | High | Medium | Medium | High |

*Amortized time, occasionally O(n) during resize

## When to Use Each

### ArrayList
- Need indexed access
- More reads than modifications
- Memory efficiency important
- Random access patterns

### LinkedList
- Frequent insertions/deletions
- Stack/Queue/Deque operations
- Sequential access sufficient
- Unknown final size

</div>

<div>

## Important Concepts Recap

<v-clicks>

- **Indexed Access**: List interface provides get(index) and set(index, element)
- **Iterator Safety**: Use iterator.remove() to avoid ConcurrentModificationException
- **Set Mathematics**: Union, intersection, difference operations
- **Hash Contracts**: equals() and hashCode() must be consistent
- **Natural Ordering**: TreeSet requires Comparable or Comparator
- **NavigableSet**: TreeSet provides range and navigation methods
- **Performance Trade-offs**: O(1) vs O(log n) vs ordering guarantees
- **Memory Overhead**: LinkedList nodes vs array elements

</v-clicks>

### Set Operations Examples
```java
Set<Integer> set1 = Set.of(1, 2, 3);
Set<Integer> set2 = Set.of(2, 3, 4);

// Union
Set<Integer> union = new HashSet<>(set1);
union.addAll(set2); // {1, 2, 3, 4}

// Intersection
Set<Integer> intersection = new HashSet<>(set1);
intersection.retainAll(set2); // {2, 3}

// Difference
Set<Integer> difference = new HashSet<>(set1);
difference.removeAll(set2); // {1}
```

### TreeSet Navigation
```java
TreeSet<Integer> tree = new TreeSet<>(Set.of(10, 20, 30, 40, 50));

tree.ceiling(25);  // 30 (≥25)
tree.floor(25);    // 20 (≤25)
tree.higher(30);   // 40 (>30)
tree.lower(30);    // 20 (<30)

tree.headSet(30);  // [10, 20]
tree.tailSet(30);  // [30, 40, 50]
tree.subSet(20, 40); // [20, 30]
```

## Best Practices

1. **Choose appropriate implementation** based on usage patterns
2. **Override equals() and hashCode()** for custom objects in Sets
3. **Use diamond operator** for type inference
4. **Prefer enhanced for-loop** for simple iteration
5. **Use ListIterator** for bidirectional navigation
6. **Consider thread safety** requirements
7. **Initialize with capacity** when size is known
8. **Use Collections.unmodifiable** for read-only views

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## List and Set Collections Complete

**Lecture 35 Successfully Completed!**  
You now understand List and Set collections thoroughly

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for Map Collections! <carbon:arrow-right class="inline"/>
  </span>
</div>