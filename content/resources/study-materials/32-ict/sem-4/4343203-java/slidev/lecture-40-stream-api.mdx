---
theme: default
background: https://source.unsplash.com/1024x768/?java,programming
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: Java Programming - Lecture 40
mdc: true
---

# Java Programming
## Lecture 40: Stream API
### GTU Diploma in Computer Engineering

---
layout: two-cols
---

# Learning Objectives

After this lecture, you will be able to:

- Understand the concept and benefits of Java Streams
- Create streams from various data sources
- Use intermediate operations for data transformation
- Apply terminal operations to produce results
- Work with parallel streams for performance
- Use collectors for data aggregation
- Create custom collectors for specific needs
- Apply stream best practices and performance optimization

::right::

# Lecture Overview

1. **Introduction to Stream API**
2. **Creating Streams**
3. **Intermediate Operations**
4. **Terminal Operations**
5. **Parallel Streams**
6. **Collectors**
7. **Custom Collectors**
8. **Advanced Stream Operations**
9. **Performance and Best Practices**
10. **Hands-on Exercises**

---

# What is Stream API?

Stream API provides a functional programming approach to processing collections of data.

## Key Characteristics

1. **No Storage**: Streams don't store data, they operate on data sources
2. **Functional in Nature**: Operations don't modify the source
3. **Lazy Evaluation**: Intermediate operations are not executed until terminal operation is called
4. **Possibly Unbounded**: Streams can be infinite
5. **Consumable**: Stream elements are visited only once

## Stream vs Collection

```java
import java.util.*;
import java.util.stream.*;

public class StreamIntroduction {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");
        
        // Traditional approach
        List<String> upperCaseNames = new ArrayList<>();
        for (String name : names) {
            if (name.length() > 3) {
                upperCaseNames.add(name.toUpperCase());
            }
        }
        Collections.sort(upperCaseNames);
        System.out.println("Traditional: " + upperCaseNames);
        
        // Stream approach
        List<String> streamResult = names.stream()
            .filter(name -> name.length() > 3)
            .map(String::toUpperCase)
            .sorted()
            .collect(Collectors.toList());
        System.out.println("Stream: " + streamResult);
    }
}
```

---

# Creating Streams

## From Collections

```java
import java.util.*;
import java.util.stream.*;

public class StreamCreation {
    public static void main(String[] args) {
        // From List
        List<String> list = Arrays.asList("apple", "banana", "cherry");
        Stream<String> streamFromList = list.stream();
        
        // From Array
        String[] array = {"red", "green", "blue"};
        Stream<String> streamFromArray = Arrays.stream(array);
        
        // From Set
        Set<Integer> set = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5));
        Stream<Integer> streamFromSet = set.stream();
        
        // From Map
        Map<String, Integer> map = new HashMap<>();
        map.put("Alice", 25);
        map.put("Bob", 30);
        map.put("Charlie", 35);
        
        Stream<String> keysStream = map.keySet().stream();
        Stream<Integer> valuesStream = map.values().stream();
        Stream<Map.Entry<String, Integer>> entriesStream = map.entrySet().stream();
        
        // Display results
        System.out.println("From list:");
        streamFromList.forEach(System.out::println);
        
        System.out.println("From array:");
        streamFromArray.forEach(System.out::println);
        
        System.out.println("From set:");
        streamFromSet.forEach(System.out::println);
        
        System.out.println("Map entries:");
        entriesStream.forEach(entry -> 
            System.out.println(entry.getKey() + " -> " + entry.getValue()));
    }
}
```

---

# Stream Factory Methods

```java
import java.util.stream.*;
import java.nio.file.*;
import java.util.*;

public class StreamFactoryMethods {
    public static void main(String[] args) {
        // Stream.of()
        Stream<String> streamOf = Stream.of("Java", "Python", "JavaScript");
        System.out.println("Stream.of():");
        streamOf.forEach(System.out::println);
        
        // Stream.empty()
        Stream<String> emptyStream = Stream.empty();
        System.out.println("Empty stream count: " + emptyStream.count());
        
        // Stream.generate() - infinite stream
        Stream<Double> randomStream = Stream.generate(Math::random);
        System.out.println("5 random numbers:");
        randomStream.limit(5).forEach(System.out::println);
        
        // Stream.iterate() - infinite stream
        Stream<Integer> numbersStream = Stream.iterate(0, n -> n + 2);
        System.out.println("First 10 even numbers:");
        numbersStream.limit(10).forEach(System.out::println);
        
        // Stream.iterate() with predicate (Java 9+)
        Stream<Integer> limitedStream = Stream.iterate(1, n -> n <= 100, n -> n * 2);
        System.out.println("Powers of 2 up to 100:");
        limitedStream.forEach(System.out::println);
        
        // IntStream, LongStream, DoubleStream
        IntStream intStream = IntStream.range(1, 6);  // 1, 2, 3, 4, 5
        System.out.println("IntStream range:");
        intStream.forEach(System.out::println);
        
        IntStream intStreamClosed = IntStream.rangeClosed(1, 5);  // 1, 2, 3, 4, 5
        System.out.println("IntStream rangeClosed:");
        intStreamClosed.forEach(System.out::println);
        
        // Random number streams
        Random random = new Random();
        Stream<Integer> randomInts = random.ints(5, 1, 10).boxed();
        System.out.println("5 random integers between 1-10:");
        randomInts.forEach(System.out::println);
        
        // Stream from String
        IntStream charsStream = "Hello".chars();
        System.out.println("Characters in 'Hello':");
        charsStream.forEach(c -> System.out.print((char)c + " "));
        System.out.println();
        
        // Stream from file lines (requires exception handling)
        try {
            // Creates a temporary file for demonstration
            Path tempFile = Files.createTempFile("demo", ".txt");
            Files.write(tempFile, Arrays.asList("Line 1", "Line 2", "Line 3"));
            
            Stream<String> linesStream = Files.lines(tempFile);
            System.out.println("Lines from file:");
            linesStream.forEach(System.out::println);
            
            // Clean up
            Files.deleteIfExists(tempFile);
        } catch (Exception e) {
            System.out.println("File operation error: " + e.getMessage());
        }
    }
}
```

---

# Intermediate Operations

Intermediate operations are lazy and return a stream.

## Filter, Map, and Sorted

```java
import java.util.*;
import java.util.stream.*;

public class IntermediateOperations {
    
    static class Person {
        private String name;
        private int age;
        private String city;
        private double salary;
        
        public Person(String name, int age, String city, double salary) {
            this.name = name;
            this.age = age;
            this.city = city;
            this.salary = salary;
        }
        
        // Getters
        public String getName() { return name; }
        public int getAge() { return age; }
        public String getCity() { return city; }
        public double getSalary() { return salary; }
        
        @Override
        public String toString() {
            return String.format("Person{name='%s', age=%d, city='%s', salary=%.2f}", 
                               name, age, city, salary);
        }
    }
    
    public static void main(String[] args) {
        List<Person> people = Arrays.asList(
            new Person("Alice", 25, "New York", 75000),
            new Person("Bob", 30, "London", 65000),
            new Person("Charlie", 35, "New York", 85000),
            new Person("Diana", 28, "London", 70000),
            new Person("Eve", 32, "Paris", 80000)
        );
        
        System.out.println("Original list:");
        people.forEach(System.out::println);
        
        // Filter - people older than 30
        System.out.println("\nPeople older than 30:");
        people.stream()
              .filter(person -> person.getAge() > 30)
              .forEach(System.out::println);
        
        // Map - extract names
        System.out.println("\nNames only:");
        people.stream()
              .map(Person::getName)
              .forEach(System.out::println);
        
        // Map - transform to uppercase names
        System.out.println("\nUppercase names:");
        people.stream()
              .map(Person::getName)
              .map(String::toUpperCase)
              .forEach(System.out::println);
        
        // Sorted - by age
        System.out.println("\nSorted by age:");
        people.stream()
              .sorted(Comparator.comparing(Person::getAge))
              .forEach(System.out::println);
        
        // Sorted - by salary (descending)
        System.out.println("\nSorted by salary (descending):");
        people.stream()
              .sorted(Comparator.comparing(Person::getSalary).reversed())
              .forEach(System.out::println);
        
        // Complex chain - filter, map, and sort
        System.out.println("\nNew York people, names only, sorted:");
        people.stream()
              .filter(person -> "New York".equals(person.getCity()))
              .map(Person::getName)
              .sorted()
              .forEach(System.out::println);
    }
}
```

---

# More Intermediate Operations

## Distinct, Limit, Skip, and FlatMap

```java
import java.util.*;
import java.util.stream.*;

public class MoreIntermediateOperations {
    public static void main(String[] args) {
        // Distinct
        List<Integer> numbers = Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 5);
        System.out.println("Original: " + numbers);
        System.out.println("Distinct:");
        numbers.stream()
               .distinct()
               .forEach(System.out::println);
        
        // Limit
        System.out.println("\nFirst 3 distinct numbers:");
        numbers.stream()
               .distinct()
               .limit(3)
               .forEach(System.out::println);
        
        // Skip
        System.out.println("\nSkip first 2 distinct numbers:");
        numbers.stream()
               .distinct()
               .skip(2)
               .forEach(System.out::println);
        
        // FlatMap - flatten nested collections
        List<List<String>> nestedList = Arrays.asList(
            Arrays.asList("Java", "Python"),
            Arrays.asList("JavaScript", "C++"),
            Arrays.asList("Ruby", "Go")
        );
        
        System.out.println("\nNested list:");
        nestedList.forEach(System.out::println);
        
        System.out.println("Flattened:");
        nestedList.stream()
                  .flatMap(Collection::stream)
                  .forEach(System.out::println);
        
        // FlatMap with arrays
        String[] words = {"Hello World", "Java Streams", "Functional Programming"};
        System.out.println("\nAll words from sentences:");
        Arrays.stream(words)
              .flatMap(sentence -> Arrays.stream(sentence.split(" ")))
              .forEach(System.out::println);
        
        // FlatMap with Optional
        List<Optional<String>> optionals = Arrays.asList(
            Optional.of("Alice"),
            Optional.empty(),
            Optional.of("Bob"),
            Optional.empty(),
            Optional.of("Charlie")
        );
        
        System.out.println("\nNon-empty optionals:");
        optionals.stream()
                 .flatMap(Optional::stream)  // Java 9+ feature
                 .forEach(System.out::println);
        
        // Alternative for Java 8
        System.out.println("Non-empty optionals (Java 8 compatible):");
        optionals.stream()
                 .filter(Optional::isPresent)
                 .map(Optional::get)
                 .forEach(System.out::println);
        
        // Complex example: processing orders
        List<Order> orders = Arrays.asList(
            new Order("Order1", Arrays.asList(
                new Product("Laptop", 999.99),
                new Product("Mouse", 29.99)
            )),
            new Order("Order2", Arrays.asList(
                new Product("Keyboard", 79.99),
                new Product("Monitor", 299.99)
            ))
        );
        
        System.out.println("\nAll products from all orders:");
        orders.stream()
              .flatMap(order -> order.getProducts().stream())
              .forEach(System.out::println);
        
        System.out.println("\nTotal value of all products:");
        double total = orders.stream()
                            .flatMap(order -> order.getProducts().stream())
                            .mapToDouble(Product::getPrice)
                            .sum();
        System.out.println("$" + total);
    }
    
    static class Order {
        private String id;
        private List<Product> products;
        
        public Order(String id, List<Product> products) {
            this.id = id;
            this.products = products;
        }
        
        public String getId() { return id; }
        public List<Product> getProducts() { return products; }
    }
    
    static class Product {
        private String name;
        private double price;
        
        public Product(String name, double price) {
            this.name = name;
            this.price = price;
        }
        
        public String getName() { return name; }
        public double getPrice() { return price; }
        
        @Override
        public String toString() {
            return String.format("Product{name='%s', price=%.2f}", name, price);
        }
    }
}
```

---

# Terminal Operations

Terminal operations consume the stream and produce a result.

## Basic Terminal Operations

```java
import java.util.*;
import java.util.stream.*;

public class TerminalOperations {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // forEach
        System.out.println("All numbers:");
        numbers.stream().forEach(System.out::println);
        
        // count
        long count = numbers.stream()
                           .filter(n -> n % 2 == 0)
                           .count();
        System.out.println("Count of even numbers: " + count);
        
        // collect to List
        List<Integer> evenNumbers = numbers.stream()
                                          .filter(n -> n % 2 == 0)
                                          .collect(Collectors.toList());
        System.out.println("Even numbers: " + evenNumbers);
        
        // collect to Set
        Set<Integer> oddNumbers = numbers.stream()
                                        .filter(n -> n % 2 == 1)
                                        .collect(Collectors.toSet());
        System.out.println("Odd numbers: " + oddNumbers);
        
        // toArray
        Integer[] array = numbers.stream()
                                .filter(n -> n > 5)
                                .toArray(Integer[]::new);
        System.out.println("Numbers > 5: " + Arrays.toString(array));
        
        // reduce - sum
        Optional<Integer> sum = numbers.stream().reduce((a, b) -> a + b);
        System.out.println("Sum: " + sum.orElse(0));
        
        // reduce with identity
        Integer sumWithIdentity = numbers.stream().reduce(0, (a, b) -> a + b);
        System.out.println("Sum with identity: " + sumWithIdentity);
        
        // reduce - product
        Integer product = numbers.stream().reduce(1, (a, b) -> a * b);
        System.out.println("Product: " + product);
        
        // reduce - find maximum
        Optional<Integer> max = numbers.stream().reduce(Integer::max);
        System.out.println("Maximum: " + max.orElse(0));
        
        // min and max methods
        Optional<Integer> min = numbers.stream().min(Integer::compareTo);
        Optional<Integer> max2 = numbers.stream().max(Integer::compareTo);
        System.out.println("Min: " + min.orElse(0) + ", Max: " + max2.orElse(0));
        
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date");
        
        // findFirst
        Optional<String> firstLongWord = words.stream()
                                            .filter(word -> word.length() > 5)
                                            .findFirst();
        System.out.println("First long word: " + firstLongWord.orElse("none"));
        
        // findAny
        Optional<String> anyLongWord = words.stream()
                                          .filter(word -> word.length() > 5)
                                          .findAny();
        System.out.println("Any long word: " + anyLongWord.orElse("none"));
        
        // anyMatch, allMatch, noneMatch
        boolean anyLong = words.stream().anyMatch(word -> word.length() > 5);
        boolean allShort = words.stream().allMatch(word -> word.length() < 10);
        boolean noneEmpty = words.stream().noneMatch(String::isEmpty);
        
        System.out.println("Any long word: " + anyLong);
        System.out.println("All short words: " + allShort);
        System.out.println("No empty words: " + noneEmpty);
    }
}
```

---

# Advanced Terminal Operations

## Working with Primitive Streams

```java
import java.util.*;
import java.util.stream.*;

public class PrimitiveStreams {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        // mapToInt, mapToLong, mapToDouble
        IntStream intStream = numbers.stream().mapToInt(Integer::intValue);
        
        // Statistical operations on IntStream
        IntSummaryStatistics stats = numbers.stream()
                                           .mapToInt(Integer::intValue)
                                           .summaryStatistics();
        
        System.out.println("Statistics for numbers 1-10:");
        System.out.println("Count: " + stats.getCount());
        System.out.println("Sum: " + stats.getSum());
        System.out.println("Min: " + stats.getMin());
        System.out.println("Max: " + stats.getMax());
        System.out.println("Average: " + stats.getAverage());
        
        // Sum, average, min, max on primitive streams
        int sum = numbers.stream().mapToInt(Integer::intValue).sum();
        OptionalDouble average = numbers.stream().mapToInt(Integer::intValue).average();
        OptionalInt min = numbers.stream().mapToInt(Integer::intValue).min();
        OptionalInt max = numbers.stream().mapToInt(Integer::intValue).max();
        
        System.out.println("\nDirect operations:");
        System.out.println("Sum: " + sum);
        System.out.println("Average: " + average.orElse(0));
        System.out.println("Min: " + min.orElse(0));
        System.out.println("Max: " + max.orElse(0));
        
        // Working with doubles
        List<Double> prices = Arrays.asList(19.99, 29.99, 39.99, 49.99, 59.99);
        
        DoubleSummaryStatistics priceStats = prices.stream()
                                                  .mapToDouble(Double::doubleValue)
                                                  .summaryStatistics();
        
        System.out.println("\nPrice statistics:");
        System.out.println("Count: " + priceStats.getCount());
        System.out.println("Sum: $" + String.format("%.2f", priceStats.getSum()));
        System.out.println("Average: $" + String.format("%.2f", priceStats.getAverage()));
        System.out.println("Min: $" + String.format("%.2f", priceStats.getMin()));
        System.out.println("Max: $" + String.format("%.2f", priceStats.getMax()));
        
        // Range operations
        System.out.println("\nSquares of numbers 1-10:");
        IntStream.rangeClosed(1, 10)
                 .map(n -> n * n)
                 .forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        // Generate Fibonacci sequence
        System.out.println("\nFirst 10 Fibonacci numbers:");
        Stream.iterate(new int[]{0, 1}, fib -> new int[]{fib[1], fib[0] + fib[1]})
              .limit(10)
              .mapToInt(fib -> fib[0])
              .forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        // Working with random numbers
        System.out.println("\n5 random numbers between 1-100:");
        new Random().ints(5, 1, 101)
                    .forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        // Box primitive stream back to object stream
        List<Integer> boxedNumbers = IntStream.rangeClosed(1, 5)
                                            .boxed()
                                            .collect(Collectors.toList());
        System.out.println("\nBoxed numbers: " + boxedNumbers);
    }
}
```

---

# Collectors

Collectors provide a way to accumulate stream elements into collections or other results.

## Basic Collectors

```java
import java.util.*;
import java.util.stream.*;

public class BasicCollectors {
    
    static class Employee {
        private String name;
        private String department;
        private double salary;
        private int age;
        
        public Employee(String name, String department, double salary, int age) {
            this.name = name;
            this.department = department;
            this.salary = salary;
            this.age = age;
        }
        
        // Getters
        public String getName() { return name; }
        public String getDepartment() { return department; }
        public double getSalary() { return salary; }
        public int getAge() { return age; }
        
        @Override
        public String toString() {
            return String.format("Employee{name='%s', dept='%s', salary=%.2f, age=%d}", 
                               name, department, salary, age);
        }
    }
    
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", "Engineering", 75000, 25),
            new Employee("Bob", "Engineering", 80000, 30),
            new Employee("Charlie", "Sales", 65000, 35),
            new Employee("Diana", "Sales", 70000, 28),
            new Employee("Eve", "Marketing", 72000, 32),
            new Employee("Frank", "Engineering", 85000, 29)
        );
        
        System.out.println("All employees:");
        employees.forEach(System.out::println);
        
        // Collect to List
        List<String> names = employees.stream()
                                    .map(Employee::getName)
                                    .collect(Collectors.toList());
        System.out.println("\nNames: " + names);
        
        // Collect to Set
        Set<String> departments = employees.stream()
                                         .map(Employee::getDepartment)
                                         .collect(Collectors.toSet());
        System.out.println("Departments: " + departments);
        
        // Collect to specific collection type
        LinkedList<String> linkedNames = employees.stream()
                                                .map(Employee::getName)
                                                .collect(Collectors.toCollection(LinkedList::new));
        System.out.println("LinkedList names: " + linkedNames);
        
        // Collect to array
        String[] nameArray = employees.stream()
                                    .map(Employee::getName)
                                    .toArray(String[]::new);
        System.out.println("Name array: " + Arrays.toString(nameArray));
        
        // Joining
        String allNames = employees.stream()
                                 .map(Employee::getName)
                                 .collect(Collectors.joining(", "));
        System.out.println("All names joined: " + allNames);
        
        String namesWithPrefix = employees.stream()
                                        .map(Employee::getName)
                                        .collect(Collectors.joining(", ", "Employees: [", "]"));
        System.out.println("Names with prefix/suffix: " + namesWithPrefix);
        
        // Counting
        long count = employees.stream()
                            .filter(emp -> emp.getSalary() > 70000)
                            .collect(Collectors.counting());
        System.out.println("High salary employees count: " + count);
        
        // Summarizing
        DoubleSummaryStatistics salaryStats = employees.stream()
                                                      .collect(Collectors.summarizingDouble(Employee::getSalary));
        System.out.println("\nSalary statistics:");
        System.out.println("Count: " + salaryStats.getCount());
        System.out.println("Sum: $" + String.format("%.2f", salaryStats.getSum()));
        System.out.println("Average: $" + String.format("%.2f", salaryStats.getAverage()));
        System.out.println("Min: $" + String.format("%.2f", salaryStats.getMin()));
        System.out.println("Max: $" + String.format("%.2f", salaryStats.getMax()));
        
        // Averaging
        OptionalDouble averageSalary = employees.stream()
                                              .mapToDouble(Employee::getSalary)
                                              .average();
        System.out.println("Average salary: $" + 
                          String.format("%.2f", averageSalary.orElse(0)));
        
        // Min and Max with Collectors
        Optional<Employee> youngestEmployee = employees.stream()
                                                     .collect(Collectors.minBy(Comparator.comparing(Employee::getAge)));
        Optional<Employee> highestPaid = employees.stream()
                                                .collect(Collectors.maxBy(Comparator.comparing(Employee::getSalary)));
        
        System.out.println("Youngest employee: " + youngestEmployee.orElse(null));
        System.out.println("Highest paid employee: " + highestPaid.orElse(null));
    }
}
```

---

# Advanced Collectors

## Grouping and Partitioning

```java
import java.util.*;
import java.util.stream.*;

public class AdvancedCollectors {
    
    static class Employee {
        private String name;
        private String department;
        private double salary;
        private int age;
        
        public Employee(String name, String department, double salary, int age) {
            this.name = name;
            this.department = department;
            this.salary = salary;
            this.age = age;
        }
        
        public String getName() { return name; }
        public String getDepartment() { return department; }
        public double getSalary() { return salary; }
        public int getAge() { return age; }
        
        @Override
        public String toString() {
            return String.format("Employee{name='%s', dept='%s', salary=%.2f, age=%d}", 
                               name, department, salary, age);
        }
    }
    
    public static void main(String[] args) {
        List<Employee> employees = Arrays.asList(
            new Employee("Alice", "Engineering", 75000, 25),
            new Employee("Bob", "Engineering", 80000, 30),
            new Employee("Charlie", "Sales", 65000, 35),
            new Employee("Diana", "Sales", 70000, 28),
            new Employee("Eve", "Marketing", 72000, 32),
            new Employee("Frank", "Engineering", 85000, 29),
            new Employee("Grace", "Marketing", 68000, 26),
            new Employee("Henry", "Sales", 73000, 31)
        );
        
        // Group by department
        Map<String, List<Employee>> byDepartment = employees.stream()
                                                           .collect(Collectors.groupingBy(Employee::getDepartment));
        
        System.out.println("Employees by department:");
        byDepartment.forEach((dept, empList) -> {
            System.out.println(dept + ":");
            empList.forEach(emp -> System.out.println("  " + emp));
        });
        
        // Group by salary range
        Map<String, List<Employee>> bySalaryRange = employees.stream()
                                                            .collect(Collectors.groupingBy(emp -> {
                                                                double salary = emp.getSalary();
                                                                if (salary < 70000) return "Low";
                                                                else if (salary < 80000) return "Medium";
                                                                else return "High";
                                                            }));
        
        System.out.println("\nEmployees by salary range:");
        bySalaryRange.forEach((range, empList) -> {
            System.out.println(range + " salary:");
            empList.forEach(emp -> System.out.println("  " + emp));
        });
        
        // Count by department
        Map<String, Long> countByDepartment = employees.stream()
                                                      .collect(Collectors.groupingBy(
                                                          Employee::getDepartment,
                                                          Collectors.counting()
                                                      ));
        
        System.out.println("\nEmployee count by department:");
        countByDepartment.forEach((dept, count) -> 
            System.out.println(dept + ": " + count));
        
        // Average salary by department
        Map<String, Double> avgSalaryByDept = employees.stream()
                                                      .collect(Collectors.groupingBy(
                                                          Employee::getDepartment,
                                                          Collectors.averagingDouble(Employee::getSalary)
                                                      ));
        
        System.out.println("\nAverage salary by department:");
        avgSalaryByDept.forEach((dept, avgSalary) -> 
            System.out.println(dept + ": $" + String.format("%.2f", avgSalary)));
        
        // Sum salary by department
        Map<String, Double> totalSalaryByDept = employees.stream()
                                                        .collect(Collectors.groupingBy(
                                                            Employee::getDepartment,
                                                            Collectors.summingDouble(Employee::getSalary)
                                                        ));
        
        System.out.println("\nTotal salary by department:");
        totalSalaryByDept.forEach((dept, total) -> 
            System.out.println(dept + ": $" + String.format("%.2f", total)));
        
        // Partitioning by condition
        Map<Boolean, List<Employee>> partitionByAge = employees.stream()
                                                              .collect(Collectors.partitioningBy(emp -> emp.getAge() >= 30));
        
        System.out.println("\nEmployees partitioned by age >= 30:");
        System.out.println("Age >= 30:");
        partitionByAge.get(true).forEach(emp -> System.out.println("  " + emp));
        System.out.println("Age < 30:");
        partitionByAge.get(false).forEach(emp -> System.out.println("  " + emp));
        
        // Partition and count
        Map<Boolean, Long> partitionCount = employees.stream()
                                                   .collect(Collectors.partitioningBy(
                                                       emp -> emp.getSalary() > 70000,
                                                       Collectors.counting()
                                                   ));
        
        System.out.println("\nEmployee count by salary > 70000:");
        System.out.println("High salary (>70k): " + partitionCount.get(true));
        System.out.println("Low salary (<=70k): " + partitionCount.get(false));
        
        // Nested grouping - by department then by age group
        Map<String, Map<String, List<Employee>>> nestedGrouping = employees.stream()
                .collect(Collectors.groupingBy(
                    Employee::getDepartment,
                    Collectors.groupingBy(emp -> emp.getAge() < 30 ? "Young" : "Senior")
                ));
        
        System.out.println("\nNested grouping (Department -> Age Group):");
        nestedGrouping.forEach((dept, ageGroups) -> {
            System.out.println(dept + ":");
            ageGroups.forEach((ageGroup, empList) -> {
                System.out.println("  " + ageGroup + ":");
                empList.forEach(emp -> System.out.println("    " + emp));
            });
        });
    }
}
```

---

# Custom Collectors

Creating your own collectors for specific use cases.

```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class CustomCollectors {
    
    // Custom collector to collect to a specific string format
    public static Collector<String, ?, String> toFormattedString(String delimiter, String prefix, String suffix) {
        return Collector.of(
            StringBuilder::new,                    // supplier
            (sb, str) -> sb.append(str).append(delimiter),  // accumulator
            (sb1, sb2) -> sb1.append(sb2),        // combiner
            sb -> {                               // finisher
                if (sb.length() > 0) {
                    sb.setLength(sb.length() - delimiter.length()); // remove last delimiter
                }
                return prefix + sb.toString() + suffix;
            }
        );
    }
    
    // Custom collector to collect statistics
    public static <T> Collector<T, ?, Statistics<T>> toStatistics(Function<T, Double> mapper) {
        return Collector.of(
            Statistics::new,                      // supplier
            (stats, item) -> stats.add(mapper.apply(item)),  // accumulator
            Statistics::combine,                  // combiner
            Function.identity()                   // finisher
        );
    }
    
    // Custom collector to collect to immutable list
    public static <T> Collector<T, ?, List<T>> toImmutableList() {
        return Collector.of(
            ArrayList::new,                       // supplier
            ArrayList::add,                       // accumulator
            (list1, list2) -> { list1.addAll(list2); return list1; },  // combiner
            Collections::unmodifiableList         // finisher
        );
    }
    
    // Custom collector to collect unique elements by a key function
    public static <T, K> Collector<T, ?, List<T>> uniqueBy(Function<T, K> keyExtractor) {
        return Collector.of(
            () -> new LinkedHashMap<K, T>(),      // supplier
            (map, item) -> map.putIfAbsent(keyExtractor.apply(item), item),  // accumulator
            (map1, map2) -> { map2.forEach(map1::putIfAbsent); return map1; },  // combiner
            map -> new ArrayList<>(map.values())  // finisher
        );
    }
    
    static class Statistics<T> {
        private long count = 0;
        private double sum = 0;
        private double min = Double.MAX_VALUE;
        private double max = Double.MIN_VALUE;
        
        public void add(double value) {
            count++;
            sum += value;
            min = Math.min(min, value);
            max = Math.max(max, value);
        }
        
        public Statistics<T> combine(Statistics<T> other) {
            count += other.count;
            sum += other.sum;
            min = Math.min(min, other.min);
            max = Math.max(max, other.max);
            return this;
        }
        
        public long getCount() { return count; }
        public double getSum() { return sum; }
        public double getAverage() { return count > 0 ? sum / count : 0; }
        public double getMin() { return min; }
        public double getMax() { return max; }
        
        @Override
        public String toString() {
            return String.format("Statistics{count=%d, sum=%.2f, avg=%.2f, min=%.2f, max=%.2f}", 
                               count, sum, getAverage(), min, max);
        }
    }
    
    static class Product {
        private String name;
        private String category;
        private double price;
        
        public Product(String name, String category, double price) {
            this.name = name;
            this.category = category;
            this.price = price;
        }
        
        public String getName() { return name; }
        public String getCategory() { return category; }
        public double getPrice() { return price; }
        
        @Override
        public String toString() {
            return String.format("Product{name='%s', category='%s', price=%.2f}", name, category, price);
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Product)) return false;
            Product product = (Product) o;
            return Objects.equals(name, product.name) && Objects.equals(category, product.category);
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(name, category);
        }
    }
    
    public static void main(String[] args) {
        List<String> words = Arrays.asList("Java", "Python", "JavaScript", "Ruby", "Go");
        
        // Using custom formatted string collector
        String formatted = words.stream()
                                .collect(toFormattedString(", ", "Languages: [", "]"));
        System.out.println("Formatted string: " + formatted);
        
        List<Product> products = Arrays.asList(
            new Product("Laptop", "Electronics", 999.99),
            new Product("Mouse", "Electronics", 29.99),
            new Product("Keyboard", "Electronics", 79.99),
            new Product("Desk", "Furniture", 299.99),
            new Product("Chair", "Furniture", 199.99),
            new Product("Laptop", "Electronics", 1299.99),  // Duplicate name/category
            new Product("Monitor", "Electronics", 349.99)
        );
        
        // Using custom statistics collector
        Statistics<Product> priceStats = products.stream()
                                               .collect(toStatistics(Product::getPrice));
        System.out.println("Price statistics: " + priceStats);
        
        // Using immutable list collector
        List<String> immutableCategories = products.stream()
                                                  .map(Product::getCategory)
                                                  .distinct()
                                                  .collect(toImmutableList());
        System.out.println("Immutable categories: " + immutableCategories);
        
        // Try to modify (will throw UnsupportedOperationException)
        try {
            immutableCategories.add("New Category");
        } catch (UnsupportedOperationException e) {
            System.out.println("Cannot modify immutable list: " + e.getMessage());
        }
        
        // Using unique by collector
        List<Product> uniqueProducts = products.stream()
                                             .collect(uniqueBy(p -> p.getName() + p.getCategory()));
        System.out.println("\nUnique products (by name and category):");
        uniqueProducts.forEach(System.out::println);
        
        // Complex custom collector - most expensive product by category
        Map<String, Optional<Product>> mostExpensiveByCategory = products.stream()
                .collect(Collectors.groupingBy(
                    Product::getCategory,
                    Collector.of(
                        () -> Optional.<Product>empty(),
                        (opt, product) -> opt.map(p -> p.getPrice() > product.getPrice() ? p : product)
                                           .or(() -> Optional.of(product)),
                        (opt1, opt2) -> opt1.flatMap(p1 -> opt2.map(p2 -> p1.getPrice() > p2.getPrice() ? p1 : p2))
                                          .or(() -> opt1.or(() -> opt2))
                    )
                ));
        
        System.out.println("\nMost expensive product by category:");
        mostExpensiveByCategory.forEach((category, product) -> 
            System.out.println(category + ": " + product.orElse(null)));
    }
}
```

---

# Parallel Streams

Parallel streams can improve performance for CPU-intensive operations on large datasets.

```java
import java.util.*;
import java.util.stream.*;
import java.time.Instant;
import java.time.Duration;

public class ParallelStreams {
    
    public static void measureTime(String description, Runnable operation) {
        Instant start = Instant.now();
        operation.run();
        Instant end = Instant.now();
        Duration duration = Duration.between(start, end);
        System.out.println(description + ": " + duration.toMillis() + "ms");
    }
    
    // CPU-intensive operation for demonstration
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
    
    public static void main(String[] args) {
        // Create a large dataset
        List<Integer> numbers = IntStream.rangeClosed(1, 100000)
                                       .boxed()
                                       .collect(Collectors.toList());
        
        System.out.println("Processing " + numbers.size() + " numbers\n");
        
        // Sequential processing
        measureTime("Sequential sum", () -> {
            long sum = numbers.stream()
                            .mapToLong(Integer::longValue)
                            .sum();
        });
        
        // Parallel processing
        measureTime("Parallel sum", () -> {
            long sum = numbers.parallelStream()
                            .mapToLong(Integer::longValue)
                            .sum();
        });
        
        // More CPU-intensive operation - finding prime numbers
        List<Integer> testNumbers = IntStream.rangeClosed(1, 10000)
                                           .boxed()
                                           .collect(Collectors.toList());
        
        System.out.println("\nFinding prime numbers up to 10000:");
        
        measureTime("Sequential prime check", () -> {
            List<Integer> primes = testNumbers.stream()
                                            .filter(ParallelStreams::isPrime)
                                            .collect(Collectors.toList());
            System.out.println("  Found " + primes.size() + " primes");
        });
        
        measureTime("Parallel prime check", () -> {
            List<Integer> primes = testNumbers.parallelStream()
                                            .filter(ParallelStreams::isPrime)
                                            .collect(Collectors.toList());
            System.out.println("  Found " + primes.size() + " primes");
        });
        
        // Demonstrating parallel processing characteristics
        System.out.println("\nParallel processing characteristics:");
        
        // Check available processors
        int processors = Runtime.getRuntime().availableProcessors();
        System.out.println("Available processors: " + processors);
        
        // Show which threads are used in parallel processing
        Set<String> threadNames = new HashSet<>();
        numbers.parallelStream()
               .limit(20)
               .forEach(n -> threadNames.add(Thread.currentThread().getName()));
        
        System.out.println("Threads used in parallel processing:");
        threadNames.forEach(name -> System.out.println("  " + name));
        
        // Order considerations in parallel streams
        System.out.println("\nOrder considerations:");
        
        List<Integer> smallNumbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        
        System.out.println("Sequential processing (ordered):");
        smallNumbers.stream()
                   .map(n -> n * 2)
                   .forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        System.out.println("Parallel processing (potentially unordered):");
        smallNumbers.parallelStream()
                   .map(n -> n * 2)
                   .forEach(n -> System.out.print(n + " "));
        System.out.println();
        
        System.out.println("Parallel processing with forEachOrdered (ordered):");
        smallNumbers.parallelStream()
                   .map(n -> n * 2)
                   .forEachOrdered(n -> System.out.print(n + " "));
        System.out.println();
        
        // When parallel streams might not help
        System.out.println("\nWhen parallel streams might not be beneficial:");
        
        List<String> words = Arrays.asList("Java", "Python", "JavaScript", "C++", "Ruby");
        
        measureTime("Sequential simple operation", () -> {
            List<String> upper = words.stream()
                                    .map(String::toUpperCase)
                                    .collect(Collectors.toList());
        });
        
        measureTime("Parallel simple operation", () -> {
            List<String> upper = words.parallelStream()
                                    .map(String::toUpperCase)
                                    .collect(Collectors.toList());
        });
        
        // Reduce operations in parallel
        System.out.println("\nReduce operations:");
        
        Integer sequentialSum = numbers.stream()
                                     .limit(1000)
                                     .reduce(0, Integer::sum);
        
        Integer parallelSum = numbers.parallelStream()
                                   .limit(1000)
                                   .reduce(0, Integer::sum);
        
        System.out.println("Sequential sum: " + sequentialSum);
        System.out.println("Parallel sum: " + parallelSum);
        
        // Parallel reduce with combiner
        Integer parallelSumWithCombiner = numbers.parallelStream()
                                                .limit(1000)
                                                .reduce(0, 
                                                       Integer::sum,    // accumulator
                                                       Integer::sum);   // combiner
        
        System.out.println("Parallel sum with combiner: " + parallelSumWithCombiner);
    }
}
```

---

# Stream Performance and Best Practices

```java
import java.util.*;
import java.util.stream.*;
import java.time.Instant;
import java.time.Duration;

public class StreamPerformance {
    
    public static void measureTime(String description, Runnable operation) {
        Instant start = Instant.now();
        operation.run();
        Instant end = Instant.now();
        Duration duration = Duration.between(start, end);
        System.out.println(description + ": " + duration.toMillis() + "ms");
    }
    
    public static void main(String[] args) {
        List<Integer> largeList = IntStream.rangeClosed(1, 1_000_000)
                                         .boxed()
                                         .collect(Collectors.toList());
        
        System.out.println("Performance comparison on " + largeList.size() + " elements:\n");
        
        // 1. Stream vs Traditional Loop
        measureTime("Traditional for-each loop", () -> {
            List<Integer> result = new ArrayList<>();
            for (Integer n : largeList) {
                if (n % 2 == 0) {
                    result.add(n * n);
                }
            }
        });
        
        measureTime("Stream operations", () -> {
            List<Integer> result = largeList.stream()
                                          .filter(n -> n % 2 == 0)
                                          .map(n -> n * n)
                                          .collect(Collectors.toList());
        });
        
        measureTime("Parallel stream", () -> {
            List<Integer> result = largeList.parallelStream()
                                          .filter(n -> n % 2 == 0)
                                          .map(n -> n * n)
                                          .collect(Collectors.toList());
        });
        
        // 2. Short-circuiting operations
        System.out.println("\nShort-circuiting benefits:");
        
        measureTime("findFirst (short-circuit)", () -> {
            Optional<Integer> result = largeList.stream()
                                               .filter(n -> n > 500_000)
                                               .findFirst();
        });
        
        measureTime("collect all (no short-circuit)", () -> {
            List<Integer> result = largeList.stream()
                                          .filter(n -> n > 500_000)
                                          .collect(Collectors.toList());
        });
        
        // 3. Primitive streams vs boxed streams
        System.out.println("\nPrimitive vs Boxed streams:");
        
        measureTime("IntStream (primitive)", () -> {
            long sum = IntStream.rangeClosed(1, 1_000_000)
                              .filter(n -> n % 2 == 0)
                              .sum();
        });
        
        measureTime("Stream<Integer> (boxed)", () -> {
            Integer sum = IntStream.rangeClosed(1, 1_000_000)
                                 .boxed()
                                 .filter(n -> n % 2 == 0)
                                 .reduce(0, Integer::sum);
        });
        
        // 4. Lazy evaluation demonstration
        System.out.println("\nLazy evaluation:");
        
        System.out.println("Creating stream with side effects:");
        Stream<Integer> stream = Arrays.asList(1, 2, 3, 4, 5).stream()
            .peek(n -> System.out.println("Processing: " + n))
            .filter(n -> n % 2 == 0)
            .peek(n -> System.out.println("Filtered: " + n))
            .map(n -> n * n)
            .peek(n -> System.out.println("Mapped: " + n));
        
        System.out.println("Stream created, but no operations executed yet");
        
        System.out.println("Now executing terminal operation:");
        List<Integer> result = stream.collect(Collectors.toList());
        System.out.println("Result: " + result);
        
        // 5. Best practices
        System.out.println("\nBest Practices:");
        
        // Avoid side effects in lambda expressions
        List<String> words = Arrays.asList("Java", "Python", "JavaScript", "Ruby");
        
        // Bad: side effects
        List<String> sideEffectList = new ArrayList<>();
        words.stream()
             .filter(word -> word.length() > 4)
             .forEach(sideEffectList::add); // Side effect - modifying external state
        
        // Good: functional approach
        List<String> functionalResult = words.stream()
                                           .filter(word -> word.length() > 4)
                                           .collect(Collectors.toList());
        
        System.out.println("Side effect result: " + sideEffectList);
        System.out.println("Functional result: " + functionalResult);
        
        // Keep lambda expressions simple
        List<String> complexWords = Arrays.asList("hello", "world", "java", "stream");
        
        // Bad: complex lambda
        List<String> complexResult = complexWords.stream()
            .filter(word -> {
                boolean startsWithVowel = "aeiouAEIOU".indexOf(word.charAt(0)) != -1;
                boolean longerThan4 = word.length() > 4;
                boolean containsA = word.contains("a");
                return startsWithVowel || (longerThan4 && containsA);
            })
            .collect(Collectors.toList());
        
        // Better: extract to method
        List<String> betterResult = complexWords.stream()
                                              .filter(StreamPerformance::isComplexMatch)
                                              .collect(Collectors.toList());
        
        System.out.println("Complex filter result: " + betterResult);
        
        // Use appropriate collectors
        System.out.println("\nCollector performance:");
        
        measureTime("Collect to ArrayList", () -> {
            List<Integer> result_list = largeList.stream()
                                          .filter(n -> n % 100 == 0)
                                          .collect(Collectors.toList());
        });
        
        measureTime("Collect to specific collection", () -> {
            ArrayList<Integer> result_arraylist = largeList.stream()
                                               .filter(n -> n % 100 == 0)
                                               .collect(Collectors.toCollection(ArrayList::new));
        });
        
        measureTime("Collect to array", () -> {
            Integer[] resultArray = largeList.stream()
                                           .filter(n -> n % 100 == 0)
                                           .toArray(Integer[]::new);
        });
    }
    
    private static boolean isComplexMatch(String word) {
        boolean startsWithVowel = "aeiouAEIOU".indexOf(word.charAt(0)) != -1;
        boolean longerThan4 = word.length() > 4;
        boolean containsA = word.contains("a");
        return startsWithVowel || (longerThan4 && containsA);
    }
    
    // Guidelines for when to use parallel streams
    public static void parallelStreamGuidelines() {
        System.out.println("\nParallel Stream Guidelines:");
        System.out.println("Use parallel streams when:");
        System.out.println("1. Large amount of data (>10,000 elements typically)");
        System.out.println("2. CPU-intensive operations");
        System.out.println("3. Operations are stateless and don't depend on order");
        System.out.println("4. No shared mutable state");
        
        System.out.println("\nAvoid parallel streams when:");
        System.out.println("1. Small datasets");
        System.out.println("2. I/O bound operations");
        System.out.println("3. Operations have side effects");
        System.out.println("4. Order matters and can't use forEachOrdered");
    }
}
```

---

# Hands-on Exercise 1: Student Management System

Create a comprehensive student management system using Stream API:

```java
import java.util.*;
import java.util.stream.*;

// Student class
class Student {
    private String name;
    private int age;
    private String major;
    private double gpa;
    private List<String> courses;
    
    public Student(String name, int age, String major, double gpa, List<String> courses) {
        this.name = name;
        this.age = age;
        this.major = major;
        this.gpa = gpa;
        this.courses = courses;
    }
    
    // Getters
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getMajor() { return major; }
    public double getGpa() { return gpa; }
    public List<String> getCourses() { return courses; }
    
    @Override
    public String toString() {
        return String.format("Student{name='%s', age=%d, major='%s', gpa=%.2f}", name, age, major, gpa);
    }
}

public class StudentManagementSystem {
    
    public static void main(String[] args) {
        List<Student> students = Arrays.asList(
            new Student("Alice", 20, "Computer Science", 3.8, Arrays.asList("Java", "Database", "Algorithms")),
            new Student("Bob", 21, "Computer Science", 3.2, Arrays.asList("Java", "Web Development")),
            new Student("Charlie", 22, "Mathematics", 3.9, Arrays.asList("Calculus", "Statistics", "Linear Algebra")),
            new Student("Diana", 19, "Physics", 3.7, Arrays.asList("Mechanics", "Thermodynamics")),
            new Student("Eve", 23, "Computer Science", 3.5, Arrays.asList("Database", "Machine Learning", "AI")),
            new Student("Frank", 20, "Mathematics", 3.6, Arrays.asList("Calculus", "Discrete Math"))
        );
        
        // TODO: Implement the following using Stream API:
        
        // 1. Find all Computer Science students with GPA > 3.5
        System.out.println("1. CS students with GPA > 3.5:");
        // Your implementation here
        
        // 2. Get average GPA by major
        System.out.println("\n2. Average GPA by major:");
        // Your implementation here
        
        // 3. Find the oldest student in each major
        System.out.println("\n3. Oldest student in each major:");
        // Your implementation here
        
        // 4. Get all unique courses being taken by students
        System.out.println("\n4. All unique courses:");
        // Your implementation here
        
        // 5. Count students by age group (18-20, 21-23, 24+)
        System.out.println("\n5. Students by age group:");
        // Your implementation here
        
        // 6. Find students taking more than 2 courses
        System.out.println("\n6. Students taking more than 2 courses:");
        // Your implementation here
        
        // 7. Get top 3 students by GPA
        System.out.println("\n7. Top 3 students by GPA:");
        // Your implementation here
        
        // 8. Create a summary report
        System.out.println("\n8. Summary report:");
        // Your implementation here
    }
}
```

---

# Hands-on Exercise 2: E-commerce Data Analysis

Create an e-commerce data analysis system:

```java
import java.util.*;
import java.util.stream.*;
import java.time.LocalDate;

class Product {
    private String id;
    private String name;
    private String category;
    private double price;
    
    public Product(String id, String name, String category, double price) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
    }
    
    // Getters
    public String getId() { return id; }
    public String getName() { return name; }
    public String getCategory() { return category; }
    public double getPrice() { return price; }
    
    @Override
    public String toString() {
        return String.format("Product{id='%s', name='%s', category='%s', price=%.2f}", id, name, category, price);
    }
}

class Order {
    private String orderId;
    private String customerId;
    private LocalDate orderDate;
    private List<OrderItem> items;
    
    public Order(String orderId, String customerId, LocalDate orderDate, List<OrderItem> items) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.orderDate = orderDate;
        this.items = items;
    }
    
    public String getOrderId() { return orderId; }
    public String getCustomerId() { return customerId; }
    public LocalDate getOrderDate() { return orderDate; }
    public List<OrderItem> getItems() { return items; }
    
    public double getTotalAmount() {
        return items.stream().mapToDouble(OrderItem::getSubtotal).sum();
    }
}

class OrderItem {
    private Product product;
    private int quantity;
    
    public OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
    }
    
    public Product getProduct() { return product; }
    public int getQuantity() { return quantity; }
    public double getSubtotal() { return product.getPrice() * quantity; }
}

public class ECommerceAnalysis {
    
    public static void main(String[] args) {
        // Sample data setup
        List<Product> products = Arrays.asList(
            new Product("P1", "Laptop", "Electronics", 999.99),
            new Product("P2", "Mouse", "Electronics", 29.99),
            new Product("P3", "Keyboard", "Electronics", 79.99),
            new Product("P4", "Monitor", "Electronics", 299.99),
            new Product("P5", "Chair", "Furniture", 199.99),
            new Product("P6", "Desk", "Furniture", 399.99),
            new Product("P7", "Book", "Books", 19.99),
            new Product("P8", "Pen", "Stationery", 4.99)
        );
        
        List<Order> orders = Arrays.asList(
            new Order("O1", "C1", LocalDate.of(2024, 1, 15), Arrays.asList(
                new OrderItem(products.get(0), 1), new OrderItem(products.get(1), 2)
            )),
            new Order("O2", "C2", LocalDate.of(2024, 1, 20), Arrays.asList(
                new OrderItem(products.get(2), 1), new OrderItem(products.get(3), 1)
            )),
            new Order("O3", "C1", LocalDate.of(2024, 2, 5), Arrays.asList(
                new OrderItem(products.get(4), 1), new OrderItem(products.get(5), 1)
            ))
        );
        
        // TODO: Implement the following analyses:
        
        // 1. Total revenue by category
        System.out.println("1. Total revenue by category:");
        // Your implementation here
        
        // 2. Most popular products (by quantity sold)
        System.out.println("\n2. Most popular products:");
        // Your implementation here
        
        // 3. Average order value by customer
        System.out.println("\n3. Average order value by customer:");
        // Your implementation here
        
        // 4. Monthly sales summary
        System.out.println("\n4. Monthly sales summary:");
        // Your implementation here
        
        // 5. Products never ordered
        System.out.println("\n5. Products never ordered:");
        // Your implementation here
    }
}
```

---

# Exercise Solutions: Student Management System

```java
public class StudentManagementSystemSolution {
    
    public static void main(String[] args) {
        // ... (same student data as above)
        
        // 1. CS students with GPA > 3.5
        List<Student> csHighGpa = students.stream()
            .filter(s -> "Computer Science".equals(s.getMajor()))
            .filter(s -> s.getGpa() > 3.5)
            .collect(Collectors.toList());
        csHighGpa.forEach(System.out::println);
        
        // 2. Average GPA by major
        Map<String, Double> avgGpaByMajor = students.stream()
            .collect(Collectors.groupingBy(
                Student::getMajor,
                Collectors.averagingDouble(Student::getGpa)
            ));
        avgGpaByMajor.forEach((major, avg) -> 
            System.out.println(major + ": " + String.format("%.2f", avg)));
        
        // 3. Oldest student in each major
        Map<String, Optional<Student>> oldestByMajor = students.stream()
            .collect(Collectors.groupingBy(
                Student::getMajor,
                Collectors.maxBy(Comparator.comparing(Student::getAge))
            ));
        oldestByMajor.forEach((major, student) -> 
            System.out.println(major + ": " + student.orElse(null)));
        
        // 4. All unique courses
        Set<String> uniqueCourses = students.stream()
            .flatMap(s -> s.getCourses().stream())
            .collect(Collectors.toSet());
        System.out.println(uniqueCourses);
        
        // 5. Students by age group
        Map<String, Long> studentsByAgeGroup = students.stream()
            .collect(Collectors.groupingBy(
                s -> {
                    int age = s.getAge();
                    if (age <= 20) return "18-20";
                    else if (age <= 23) return "21-23";
                    else return "24+";
                },
                Collectors.counting()
            ));
        studentsByAgeGroup.forEach((group, count) -> 
            System.out.println(group + ": " + count));
        
        // 6. Students taking more than 2 courses
        List<Student> activeStudents = students.stream()
            .filter(s -> s.getCourses().size() > 2)
            .collect(Collectors.toList());
        activeStudents.forEach(System.out::println);
        
        // 7. Top 3 students by GPA
        List<Student> top3Students = students.stream()
            .sorted(Comparator.comparing(Student::getGpa).reversed())
            .limit(3)
            .collect(Collectors.toList());
        top3Students.forEach(System.out::println);
        
        // 8. Summary report
        DoubleSummaryStatistics gpaStats = students.stream()
            .mapToDouble(Student::getGpa)
            .summaryStatistics();
        
        System.out.println("Total students: " + students.size());
        System.out.println("Average GPA: " + String.format("%.2f", gpaStats.getAverage()));
        System.out.println("Highest GPA: " + gpaStats.getMax());
        System.out.println("Lowest GPA: " + gpaStats.getMin());
        System.out.println("Total unique courses: " + uniqueCourses.size());
    }
}
```

---

# Summary

## Key Concepts Covered

1. **Stream Creation**: Various ways to create streams from different data sources
2. **Intermediate Operations**: filter, map, sorted, distinct, limit, skip, flatMap
3. **Terminal Operations**: collect, forEach, reduce, find operations, match operations
4. **Collectors**: Built-in collectors for common aggregation operations
5. **Custom Collectors**: Creating specialized collectors for specific use cases
6. **Parallel Streams**: Leveraging multiple cores for performance
7. **Performance Considerations**: When and how to optimize stream operations

## Benefits of Stream API

- **Functional Style**: More expressive and readable code
- **Lazy Evaluation**: Operations are optimized and executed only when needed
- **Composability**: Operations can be easily chained and combined
- **Parallelization**: Easy to leverage multiple cores
- **Integration**: Works seamlessly with collections and other Java APIs

## Best Practices

- Keep lambda expressions simple and readable
- Avoid side effects in stream operations
- Use appropriate collectors for better performance
- Consider parallel streams for CPU-intensive operations on large datasets
- Prefer primitive streams for numerical operations

---

# Next Lecture Preview

## Lecture 41: JavaFX Basics and GUI Programming

- Introduction to JavaFX
- Scene Graph and Application Structure
- Creating User Interfaces with FXML
- Event Handling and Controls
- Layouts and Styling with CSS
- Building Desktop Applications

## Preparation

- Ensure JavaFX is available in your development environment
- Review event-driven programming concepts
- Practice with lambda expressions for event handling

---

# Thank You!

## Questions and Discussion

- How do streams improve code readability and maintainability?
- When would you choose parallel streams over sequential streams?
- What are the trade-offs between streams and traditional loops?

## Resources for Further Learning

- Oracle Stream API Documentation
- Java 8 in Action by Raoul-Gabriel Urma
- Practice with real-world datasets and stream operations

**Next: JavaFX and GUI Application Development**