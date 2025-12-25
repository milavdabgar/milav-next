---
theme: default
background: https://source.unsplash.com/1024x768/?threads,management
title: Thread Creation and Management
info: |
  ## Java Programming (4343203)
  
  Lecture 31: Thread Creation and Management
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about creating threads in Java, thread management techniques, thread pools, and best practices for multithreaded programming.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Thread Creation and Management
## Lecture 31

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

- 🧵 **Create threads** using different methods in Java
- 🏗️ **Understand** Thread class vs Runnable interface
- 🔧 **Manage thread lifecycle** - start, pause, stop, interrupt
- 📋 **Implement thread pools** for efficient resource management
- ⚡ **Apply thread synchronization** techniques
- 🎯 **Handle thread exceptions** and error scenarios
- 🔄 **Use ExecutorService** for advanced thread management
- 💡 **Follow best practices** for multithreaded applications

</v-clicks>

---
layout: default
---

# Thread Creation Methods

<div class="grid grid-cols-2 gap-6">

<div>

## Method 1: Extending Thread Class

### Basic Thread Extension
```java
public class MyThread extends Thread {
    private String threadName;
    
    public MyThread(String name) {
        this.threadName = name;
        System.out.println("Creating thread: " + threadName);
    }
    
    @Override
    public void run() {
        System.out.println("Thread " + threadName + " is running");
        
        try {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Thread " + threadName + 
                                 " - Count: " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            System.out.println("Thread " + threadName + 
                             " was interrupted");
        }
        
        System.out.println("Thread " + threadName + " completed");
    }
}

// Usage
public class ThreadExtensionExample {
    public static void main(String[] args) {
        MyThread thread1 = new MyThread("Worker-1");
        MyThread thread2 = new MyThread("Worker-2");
        
        // Start threads
        thread1.start();
        thread2.start();
        
        // Wait for completion
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted");
        }
        
        System.out.println("All threads completed");
    }
}
```

### Advantages & Disadvantages
**Advantages:**
- Simple and straightforward
- Direct access to Thread methods
- Easy to understand

**Disadvantages:**
- Single inheritance limitation
- Tight coupling with Thread class
- Less flexible design

</div>

<div>

## Method 2: Implementing Runnable Interface

### Runnable Implementation
```java
public class MyTask implements Runnable {
    private String taskName;
    
    public MyTask(String name) {
        this.taskName = name;
        System.out.println("Creating task: " + taskName);
    }
    
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println("Task " + taskName + 
                         " is running on thread: " + threadName);
        
        try {
            for (int i = 1; i <= 5; i++) {
                System.out.println("Task " + taskName + 
                                 " - Step: " + i);
                
                // Simulate work
                performWork(i);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println("Task " + taskName + 
                             " was interrupted");
            Thread.currentThread().interrupt();
        }
        
        System.out.println("Task " + taskName + " completed");
    }
    
    private void performWork(int step) {
        // Simulate CPU-intensive work
        double result = 0;
        for (int i = 0; i < 1000000; i++) {
            result += Math.sin(i) * Math.cos(step);
        }
    }
}

// Usage
public class RunnableInterfaceExample {
    public static void main(String[] args) {
        // Create tasks
        MyTask task1 = new MyTask("DataProcessor");
        MyTask task2 = new MyTask("ReportGenerator");
        MyTask task3 = new MyTask("EmailSender");
        
        // Create threads with tasks
        Thread thread1 = new Thread(task1, "Thread-1");
        Thread thread2 = new Thread(task2, "Thread-2");
        Thread thread3 = new Thread(task3, "Thread-3");
        
        // Start threads
        thread1.start();
        thread2.start();
        thread3.start();
        
        // Monitor threads
        while (thread1.isAlive() || thread2.isAlive() || thread3.isAlive()) {
            System.out.println("Active threads: " + 
                             Thread.activeCount());
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        
        System.out.println("All tasks completed");
    }
}
```

### Advantages & Disadvantages
**Advantages:**
- Implements interface - can extend other classes
- Separation of task and thread
- More flexible and reusable
- Better OOP design

**Disadvantages:**
- Slightly more complex setup
- Need to create Thread objects separately

</div>

</div>

---
layout: default
---

# Thread Management Lifecycle

<div class="grid grid-cols-2 gap-6">

<div>

## Thread Lifecycle Management

### Starting Threads
```java
public class ThreadLifecycleDemo {
    public static void main(String[] args) {
        Thread worker = new Thread(new WorkerTask("BackgroundWorker"));
        
        // Check initial state
        System.out.println("Initial state: " + worker.getState());
        
        // Start thread
        worker.start();
        System.out.println("After start(): " + worker.getState());
        
        // Monitor thread execution
        monitorThread(worker);
    }
    
    private static void monitorThread(Thread thread) {
        Thread monitor = new Thread(() -> {
            while (thread.isAlive()) {
                System.out.printf("Thread state: %s, Alive: %s%n", 
                                thread.getState(), thread.isAlive());
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    break;
                }
            }
            System.out.println("Final state: " + thread.getState());
        });
        
        monitor.setDaemon(true); // Dies with main thread
        monitor.start();
    }
    
    static class WorkerTask implements Runnable {
        private String name;
        
        public WorkerTask(String name) {
            this.name = name;
        }
        
        @Override
        public void run() {
            try {
                System.out.println(name + " starting work");
                
                // Phase 1: Initial work
                Thread.sleep(2000);
                System.out.println(name + " completed phase 1");
                
                // Phase 2: Heavy computation
                performHeavyComputation();
                System.out.println(name + " completed phase 2");
                
                // Phase 3: Cleanup
                Thread.sleep(1000);
                System.out.println(name + " cleanup completed");
                
            } catch (InterruptedException e) {
                System.out.println(name + " was interrupted during work");
                Thread.currentThread().interrupt();
            }
        }
        
        private void performHeavyComputation() throws InterruptedException {
            for (int i = 0; i < 10; i++) {
                // Check for interruption
                if (Thread.currentThread().isInterrupted()) {
                    throw new InterruptedException("Work interrupted");
                }
                
                // Simulate computation
                Thread.sleep(200);
                System.out.println(name + " - computation step: " + (i + 1));
            }
        }
    }
}
```

</div>

<div>

## Thread Interruption and Cleanup

### Proper Thread Interruption
```java
public class ThreadInterruptionExample {
    public static void main(String[] args) {
        Thread longRunningTask = new Thread(new LongRunningTask());
        
        longRunningTask.start();
        
        // Let it run for 5 seconds
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        // Request interruption
        System.out.println("Requesting thread interruption...");
        longRunningTask.interrupt();
        
        // Wait for graceful shutdown
        try {
            longRunningTask.join(2000); // Wait max 2 seconds
            if (longRunningTask.isAlive()) {
                System.out.println("Thread didn't stop gracefully");
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    static class LongRunningTask implements Runnable {
        @Override
        public void run() {
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    // Do some work
                    performWork();
                    
                    // Check for interruption periodically
                    if (Thread.currentThread().isInterrupted()) {
                        System.out.println("Interruption detected during work");
                        break;
                    }
                    
                    // Sleep with interruption check
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted during sleep");
                Thread.currentThread().interrupt();
            } finally {
                // Cleanup resources
                cleanup();
            }
        }
        
        private void performWork() {
            System.out.println("Performing work on thread: " + 
                             Thread.currentThread().getName());
        }
        
        private void cleanup() {
            System.out.println("Cleaning up resources...");
            // Close files, database connections, etc.
        }
    }
}
```

### Daemon Threads
```java
public class DaemonThreadExample {
    public static void main(String[] args) {
        Thread userThread = new Thread(() -> {
            for (int i = 1; i <= 5; i++) {
                System.out.println("User thread: " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        
        Thread daemonThread = new Thread(() -> {
            while (true) {
                System.out.println("Daemon thread running...");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    break;
                }
            }
        });
        
        // Set as daemon thread
        daemonThread.setDaemon(true);
        
        System.out.println("User thread daemon status: " + 
                          userThread.isDaemon());
        System.out.println("Daemon thread daemon status: " + 
                          daemonThread.isDaemon());
        
        userThread.start();
        daemonThread.start();
        
        try {
            userThread.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        System.out.println("Main thread ending - daemon thread will stop");
    }
}
```

</div>

</div>

---
layout: default
---

# Thread Pools and ExecutorService

<div class="grid grid-cols-2 gap-6">

<div>

## ExecutorService Basics

### Fixed Thread Pool
```java
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

public class FixedThreadPoolExample {
    public static void main(String[] args) {
        // Create fixed thread pool
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        AtomicInteger taskCounter = new AtomicInteger(0);
        
        // Submit multiple tasks
        for (int i = 1; i <= 10; i++) {
            final int taskId = i;
            
            executor.submit(() -> {
                String threadName = Thread.currentThread().getName();
                int taskNumber = taskCounter.incrementAndGet();
                
                System.out.println("Task " + taskId + 
                                 " (execution #" + taskNumber + 
                                 ") started on " + threadName);
                
                try {
                    // Simulate work
                    Thread.sleep(2000 + (int)(Math.random() * 1000));
                    
                    // Simulate different outcomes
                    if (Math.random() < 0.2) {
                        throw new RuntimeException("Task " + taskId + " failed");
                    }
                    
                    System.out.println("Task " + taskId + " completed on " + threadName);
                    
                } catch (InterruptedException e) {
                    System.out.println("Task " + taskId + " interrupted");
                    Thread.currentThread().interrupt();
                } catch (RuntimeException e) {
                    System.err.println("Error in task " + taskId + ": " + e.getMessage());
                }
            });
        }
        
        // Shutdown executor
        executor.shutdown();
        
        try {
            // Wait for all tasks to complete
            if (!executor.awaitTermination(30, TimeUnit.SECONDS)) {
                System.out.println("Tasks didn't complete within 30 seconds");
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
        
        System.out.println("All tasks completed, total executions: " + 
                          taskCounter.get());
    }
}
```

### Cached Thread Pool
```java
public class CachedThreadPoolExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        
        // Submit burst of tasks
        System.out.println("Submitting burst of short tasks...");
        for (int i = 1; i <= 20; i++) {
            final int taskId = i;
            
            executor.submit(() -> {
                System.out.println("Quick task " + taskId + 
                                 " on " + Thread.currentThread().getName());
                try {
                    Thread.sleep(100); // Short task
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        // Wait a bit
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        // Submit another burst after some threads may have been recycled
        System.out.println("Submitting second burst...");
        for (int i = 21; i <= 30; i++) {
            final int taskId = i;
            
            executor.submit(() -> {
                System.out.println("Second wave task " + taskId + 
                                 " on " + Thread.currentThread().getName());
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }
        
        executor.shutdown();
        try {
            executor.awaitTermination(10, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
```

</div>

<div>

## Advanced Thread Pool Usage

### Custom ThreadPoolExecutor
```java
import java.util.concurrent.*;

public class CustomThreadPoolExample {
    public static void main(String[] args) {
        // Create custom thread pool
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2,           // corePoolSize
            5,           // maximumPoolSize  
            60,          // keepAliveTime
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10), // workQueue capacity
            new CustomThreadFactory(),     // threadFactory
            new CustomRejectedExecutionHandler() // rejectionHandler
        );
        
        // Monitor thread pool
        Thread monitor = createMonitor(executor);
        monitor.start();
        
        // Submit more tasks than queue can handle
        for (int i = 1; i <= 20; i++) {
            final int taskId = i;
            
            try {
                executor.submit(new ComputationTask(taskId));
                System.out.println("Submitted task " + taskId);
            } catch (RejectedExecutionException e) {
                System.err.println("Task " + taskId + " rejected: " + e.getMessage());
            }
            
            // Small delay between submissions
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        
        // Graceful shutdown
        executor.shutdown();
        try {
            if (!executor.awaitTermination(30, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
        
        monitor.interrupt();
    }
    
    static class ComputationTask implements Runnable {
        private final int taskId;
        
        public ComputationTask(int taskId) {
            this.taskId = taskId;
        }
        
        @Override
        public void run() {
            System.out.println("Task " + taskId + 
                             " started on " + Thread.currentThread().getName());
            
            try {
                // Simulate computation
                Thread.sleep(3000 + (int)(Math.random() * 2000));
                
                // Simulate result calculation
                double result = performComputation();
                
                System.out.println("Task " + taskId + 
                                 " completed with result: " + String.format("%.2f", result));
                
            } catch (InterruptedException e) {
                System.out.println("Task " + taskId + " was interrupted");
                Thread.currentThread().interrupt();
            }
        }
        
        private double performComputation() {
            double result = 0;
            for (int i = 0; i < 1000000; i++) {
                result += Math.sin(i) * Math.cos(taskId);
            }
            return result;
        }
    }
    
    static class CustomThreadFactory implements ThreadFactory {
        private final AtomicInteger threadNumber = new AtomicInteger(1);
        
        @Override
        public Thread newThread(Runnable r) {
            Thread thread = new Thread(r, "CustomWorker-" + threadNumber.getAndIncrement());
            thread.setDaemon(false);
            thread.setPriority(Thread.NORM_PRIORITY);
            
            System.out.println("Created new thread: " + thread.getName());
            return thread;
        }
    }
    
    static class CustomRejectedExecutionHandler implements RejectedExecutionHandler {
        @Override
        public void rejectedExecution(Runnable r, ThreadPoolExecutor executor) {
            System.err.println("Task rejected. Active: " + executor.getActiveCount() + 
                             ", Queue size: " + executor.getQueue().size());
            
            // Try to run in caller thread as fallback
            if (!executor.isShutdown()) {
                System.out.println("Running rejected task in caller thread");
                r.run();
            }
        }
    }
    
    static Thread createMonitor(ThreadPoolExecutor executor) {
        return new Thread(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                System.out.printf("Pool Stats - Active: %d, Pool Size: %d, Queue Size: %d, Completed: %d%n",
                                executor.getActiveCount(),
                                executor.getPoolSize(),
                                executor.getQueue().size(),
                                executor.getCompletedTaskCount());
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    break;
                }
            }
        });
    }
}
```

</div>

</div>

---
layout: default
---

# Thread Synchronization

<div class="grid grid-cols-2 gap-6">

<div>

## Synchronized Methods and Blocks

### Synchronized Methods
```java
public class BankAccount {
    private double balance;
    private final String accountNumber;
    
    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }
    
    // Synchronized method
    public synchronized void deposit(double amount) {
        if (amount > 0) {
            System.out.println("Depositing " + amount + 
                             " to account " + accountNumber);
            balance += amount;
            System.out.println("New balance: " + balance);
        }
    }
    
    // Synchronized method
    public synchronized boolean withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            System.out.println("Withdrawing " + amount + 
                             " from account " + accountNumber);
            balance -= amount;
            System.out.println("New balance: " + balance);
            return true;
        }
        return false;
    }
    
    // Synchronized method
    public synchronized double getBalance() {
        return balance;
    }
    
    // Synchronized method
    public synchronized void transfer(BankAccount toAccount, double amount) {
        if (this.withdraw(amount)) {
            toAccount.deposit(amount);
            System.out.println("Transferred " + amount + 
                             " from " + this.accountNumber + 
                             " to " + toAccount.accountNumber);
        } else {
            System.out.println("Transfer failed - insufficient funds");
        }
    }
}

public class BankingSimulation {
    public static void main(String[] args) throws InterruptedException {
        BankAccount account1 = new BankAccount("ACC001", 1000);
        BankAccount account2 = new BankAccount("ACC002", 500);
        
        // Create multiple threads for concurrent operations
        Thread[] operations = new Thread[10];
        
        for (int i = 0; i < 10; i++) {
            final int operationId = i;
            
            operations[i] = new Thread(() -> {
                for (int j = 0; j < 5; j++) {
                    switch (operationId % 4) {
                        case 0:
                            account1.deposit(50);
                            break;
                        case 1:
                            account1.withdraw(30);
                            break;
                        case 2:
                            account2.deposit(25);
                            break;
                        case 3:
                            account1.transfer(account2, 20);
                            break;
                    }
                    
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                }
            });
        }
        
        // Start all operations
        for (Thread op : operations) {
            op.start();
        }
        
        // Wait for completion
        for (Thread op : operations) {
            op.join();
        }
        
        // Final balances
        System.out.println("\nFinal Balances:");
        System.out.println("Account 1: " + account1.getBalance());
        System.out.println("Account 2: " + account2.getBalance());
    }
}
```

</div>

<div>

## Thread Communication with wait/notify

### Producer-Consumer with wait/notify
```java
import java.util.LinkedList;
import java.util.Queue;

public class ProducerConsumerWaitNotify {
    private static final int BUFFER_SIZE = 5;
    private final Queue<Integer> buffer = new LinkedList<>();
    private final Object lock = new Object();
    
    public static void main(String[] args) {
        ProducerConsumerWaitNotify pc = new ProducerConsumerWaitNotify();
        
        // Create producer threads
        Thread producer1 = new Thread(pc.new Producer(1), "Producer-1");
        Thread producer2 = new Thread(pc.new Producer(2), "Producer-2");
        
        // Create consumer threads
        Thread consumer1 = new Thread(pc.new Consumer(1), "Consumer-1");
        Thread consumer2 = new Thread(pc.new Consumer(2), "Consumer-2");
        Thread consumer3 = new Thread(pc.new Consumer(3), "Consumer-3");
        
        // Start all threads
        producer1.start();
        producer2.start();
        consumer1.start();
        consumer2.start();
        consumer3.start();
        
        // Let them run for 10 seconds
        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        // Interrupt all threads
        producer1.interrupt();
        producer2.interrupt();
        consumer1.interrupt();
        consumer2.interrupt();
        consumer3.interrupt();
        
        System.out.println("Simulation ended");
    }
    
    class Producer implements Runnable {
        private final int producerId;
        
        public Producer(int producerId) {
            this.producerId = producerId;
        }
        
        @Override
        public void run() {
            int itemNumber = 1;
            
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    produce(producerId * 1000 + itemNumber++);
                    Thread.sleep(1000 + (int)(Math.random() * 1000));
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Producer " + producerId + " stopped");
            }
        }
        
        private void produce(int item) throws InterruptedException {
            synchronized (lock) {
                // Wait while buffer is full
                while (buffer.size() >= BUFFER_SIZE) {
                    System.out.println("Producer " + producerId + 
                                     " waiting - buffer full");
                    lock.wait();
                }
                
                buffer.offer(item);
                System.out.println("Producer " + producerId + 
                                 " produced: " + item + 
                                 " (buffer size: " + buffer.size() + ")");
                
                // Notify consumers
                lock.notifyAll();
            }
        }
    }
    
    class Consumer implements Runnable {
        private final int consumerId;
        
        public Consumer(int consumerId) {
            this.consumerId = consumerId;
        }
        
        @Override
        public void run() {
            try {
                while (!Thread.currentThread().isInterrupted()) {
                    int item = consume();
                    processItem(item);
                    Thread.sleep(1500 + (int)(Math.random() * 1000));
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Consumer " + consumerId + " stopped");
            }
        }
        
        private int consume() throws InterruptedException {
            synchronized (lock) {
                // Wait while buffer is empty
                while (buffer.isEmpty()) {
                    System.out.println("Consumer " + consumerId + 
                                     " waiting - buffer empty");
                    lock.wait();
                }
                
                int item = buffer.poll();
                System.out.println("Consumer " + consumerId + 
                                 " consumed: " + item + 
                                 " (buffer size: " + buffer.size() + ")");
                
                // Notify producers
                lock.notifyAll();
                
                return item;
            }
        }
        
        private void processItem(int item) throws InterruptedException {
            System.out.println("Consumer " + consumerId + 
                             " processing item: " + item);
            Thread.sleep(500); // Simulate processing time
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise: Task Scheduler

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build Thread-based Task Scheduler
Create a comprehensive task scheduler that can manage different types of tasks:

```java
// TODO: Implement Task interface
public interface Task {
    String getName();
    TaskType getType();
    Priority getPriority();
    void execute() throws Exception;
    boolean canRetry();
    int getMaxRetries();
}

// TODO: Implement different task types
public enum TaskType {
    CPU_INTENSIVE,
    IO_BOUND,
    DATABASE_OPERATION,
    NETWORK_REQUEST,
    FILE_PROCESSING
}

public enum Priority {
    LOW(1), MEDIUM(5), HIGH(10), CRITICAL(15);
    
    private final int value;
    Priority(int value) { this.value = value; }
    public int getValue() { return value; }
}

// TODO: Implement concrete tasks
public class DataProcessingTask implements Task {
    // Implement CPU-intensive task
}

public class FileDownloadTask implements Task {
    // Implement I/O bound task  
}

public class DatabaseBackupTask implements Task {
    // Implement database operation task
}

// TODO: Implement Task Scheduler
public class TaskScheduler {
    private final Map<TaskType, ExecutorService> executors;
    private final PriorityQueue<ScheduledTask> taskQueue;
    private final CompletionService<TaskResult> completionService;
    
    public TaskScheduler() {
        // Initialize different thread pools for different task types
    }
    
    public void scheduleTask(Task task, long delayMs) {
        // Schedule task for future execution
    }
    
    public void submitTask(Task task) {
        // Submit task for immediate execution
    }
    
    public void start() {
        // Start the scheduler
    }
    
    public void shutdown() {
        // Graceful shutdown
    }
}

// TODO: Implement main application
public class TaskSchedulerDemo {
    public static void main(String[] args) {
        // Create scheduler
        // Add various tasks
        // Monitor execution
        // Handle results and failures
    }
}
```

**Requirements:**
- Support different task types with appropriate thread pools
- Implement priority-based task execution
- Handle task failures with retry mechanism
- Provide execution statistics and monitoring
- Support scheduled/delayed task execution
- Implement graceful shutdown

</div>

<div>

## Solution Framework

```java
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.time.LocalDateTime;

public interface Task {
    String getName();
    TaskType getType();
    Priority getPriority();
    void execute() throws Exception;
    boolean canRetry();
    int getMaxRetries();
}

public class DataProcessingTask implements Task {
    private final String name;
    private final int dataSize;
    private int retryCount = 0;
    
    public DataProcessingTask(String name, int dataSize) {
        this.name = name;
        this.dataSize = dataSize;
    }
    
    @Override
    public void execute() throws Exception {
        System.out.println("Processing " + dataSize + " records in " + name);
        
        // Simulate CPU-intensive work
        long sum = 0;
        for (int i = 0; i < dataSize * 100000; i++) {
            sum += i;
        }
        
        // Simulate potential failure
        if (Math.random() < 0.2) {
            throw new RuntimeException("Data processing failed");
        }
        
        Thread.sleep(1000);
        System.out.println("Completed " + name + ", processed sum: " + sum);
    }
    
    @Override
    public String getName() { return name; }
    
    @Override
    public TaskType getType() { return TaskType.CPU_INTENSIVE; }
    
    @Override
    public Priority getPriority() { return Priority.MEDIUM; }
    
    @Override
    public boolean canRetry() { return retryCount < 2; }
    
    @Override
    public int getMaxRetries() { return 2; }
}

public class TaskScheduler {
    private final Map<TaskType, ExecutorService> executors;
    private final ScheduledExecutorService scheduler;
    private final AtomicInteger totalTasks = new AtomicInteger(0);
    private final AtomicInteger completedTasks = new AtomicInteger(0);
    private final AtomicInteger failedTasks = new AtomicInteger(0);
    private volatile boolean isRunning = false;
    
    public TaskScheduler() {
        this.executors = new HashMap<>();
        
        // Different thread pools for different task types
        executors.put(TaskType.CPU_INTENSIVE, 
                     Executors.newFixedThreadPool(2));
        executors.put(TaskType.IO_BOUND, 
                     Executors.newFixedThreadPool(5));
        executors.put(TaskType.DATABASE_OPERATION, 
                     Executors.newFixedThreadPool(3));
        executors.put(TaskType.NETWORK_REQUEST, 
                     Executors.newCachedThreadPool());
        executors.put(TaskType.FILE_PROCESSING, 
                     Executors.newFixedThreadPool(2));
        
        this.scheduler = Executors.newScheduledThreadPool(2);
        
        // Start statistics monitor
        startMonitoring();
    }
    
    public void scheduleTask(Task task, long delayMs) {
        totalTasks.incrementAndGet();
        
        scheduler.schedule(() -> {
            submitTask(task);
        }, delayMs, TimeUnit.MILLISECONDS);
        
        System.out.println("Scheduled " + task.getName() + 
                         " to run in " + delayMs + "ms");
    }
    
    public Future<?> submitTask(Task task) {
        ExecutorService executor = executors.get(task.getType());
        
        return executor.submit(() -> {
            executeTaskWithRetry(task);
        });
    }
    
    private void executeTaskWithRetry(Task task) {
        int attempts = 0;
        
        while (attempts <= task.getMaxRetries()) {
            try {
                System.out.println("Executing " + task.getName() + 
                                 " (attempt " + (attempts + 1) + ")");
                
                long startTime = System.currentTimeMillis();
                task.execute();
                long executionTime = System.currentTimeMillis() - startTime;
                
                completedTasks.incrementAndGet();
                System.out.println("Task " + task.getName() + 
                                 " completed in " + executionTime + "ms");
                return;
                
            } catch (Exception e) {
                attempts++;
                System.err.println("Task " + task.getName() + 
                                 " failed (attempt " + attempts + "): " + e.getMessage());
                
                if (attempts > task.getMaxRetries() || !task.canRetry()) {
                    failedTasks.incrementAndGet();
                    System.err.println("Task " + task.getName() + " permanently failed");
                    return;
                }
                
                // Wait before retry
                try {
                    Thread.sleep(1000 * attempts);
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                    return;
                }
            }
        }
    }
    
    public void start() {
        isRunning = true;
        System.out.println("Task Scheduler started at " + LocalDateTime.now());
    }
    
    private void startMonitoring() {
        scheduler.scheduleAtFixedRate(() -> {
            if (isRunning) {
                System.out.println("\n=== SCHEDULER STATISTICS ===");
                System.out.println("Total tasks: " + totalTasks.get());
                System.out.println("Completed: " + completedTasks.get());
                System.out.println("Failed: " + failedTasks.get());
                System.out.println("Success rate: " + 
                    String.format("%.1f%%", 
                        (completedTasks.get() * 100.0) / Math.max(1, totalTasks.get())));
                System.out.println("============================\n");
            }
        }, 5, 5, TimeUnit.SECONDS);
    }
    
    public void shutdown() {
        isRunning = false;
        scheduler.shutdown();
        
        for (ExecutorService executor : executors.values()) {
            executor.shutdown();
            
            try {
                if (!executor.awaitTermination(30, TimeUnit.SECONDS)) {
                    executor.shutdownNow();
                }
            } catch (InterruptedException e) {
                executor.shutdownNow();
                Thread.currentThread().interrupt();
            }
        }
        
        System.out.println("Task Scheduler shutdown completed");
    }
}
```

</div>

</div>

---
layout: default
---

# Best Practices and Guidelines

<div class="grid grid-cols-2 gap-6">

<div>

## Thread Creation Best Practices

### 1. Choose the Right Approach
```java
public class ThreadCreationGuidelines {
    
    // BAD: Creating too many threads
    public void badApproach() {
        for (int i = 0; i < 1000; i++) {
            new Thread(() -> {
                // Some work
                performTask();
            }).start();
        }
    }
    
    // GOOD: Use thread pool
    public void goodApproach() {
        ExecutorService executor = Executors.newFixedThreadPool(
            Runtime.getRuntime().availableProcessors());
        
        for (int i = 0; i < 1000; i++) {
            executor.submit(() -> {
                performTask();
            });
        }
        
        executor.shutdown();
    }
    
    // GOOD: Prefer Runnable over Thread extension
    class TaskRunner implements Runnable {
        private final String taskName;
        
        public TaskRunner(String taskName) {
            this.taskName = taskName;
        }
        
        @Override
        public void run() {
            performTask();
        }
        
        // Can extend other classes if needed
    }
    
    private void performTask() {
        // Simulate work
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```

### 2. Handle Interruptions Properly
```java
public class InterruptionHandling {
    
    // GOOD: Proper interruption handling
    public void interruptibleTask() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                // Do some work
                performWorkStep();
                
                // Check for interruption periodically
                if (Thread.currentThread().isInterrupted()) {
                    System.out.println("Task interrupted");
                    break;
                }
            }
        } catch (InterruptedException e) {
            // Restore interrupted status
            Thread.currentThread().interrupt();
            System.out.println("Task interrupted during sleep");
        } finally {
            // Cleanup resources
            cleanup();
        }
    }
    
    private void performWorkStep() throws InterruptedException {
        // Simulate work that can be interrupted
        Thread.sleep(100);
    }
    
    private void cleanup() {
        System.out.println("Cleaning up resources");
    }
}
```

</div>

<div>

## Thread Safety Guidelines

### 3. Synchronization Best Practices
```java
public class SynchronizationGuidelines {
    private final Object lock = new Object();
    private int counter = 0;
    
    // GOOD: Minimize synchronized blocks
    public void incrementCounter() {
        synchronized (lock) {
            counter++; // Only critical section is synchronized
        }
    }
    
    // BAD: Synchronizing entire method when not needed
    public synchronized void badSynchronizedMethod() {
        System.out.println("Starting method"); // Non-critical
        
        synchronized (lock) {
            counter++; // Only this needs synchronization
        }
        
        System.out.println("Method completed"); // Non-critical
    }
    
    // GOOD: Use concurrent collections
    private final Map<String, Integer> concurrentMap = 
        new ConcurrentHashMap<>();
    
    public void updateMap(String key, Integer value) {
        // No synchronization needed - ConcurrentHashMap is thread-safe
        concurrentMap.put(key, value);
    }
    
    // GOOD: Use atomic operations
    private final AtomicInteger atomicCounter = new AtomicInteger(0);
    
    public void incrementAtomic() {
        // No synchronization needed - atomic operation
        atomicCounter.incrementAndGet();
    }
}
```

### 4. Exception Handling in Threads
```java
public class ThreadExceptionHandling {
    
    public static void main(String[] args) {
        // Set uncaught exception handler for all threads
        Thread.setDefaultUncaughtExceptionHandler(
            (thread, exception) -> {
                System.err.println("Uncaught exception in thread " + 
                                 thread.getName() + ": " + exception.getMessage());
                exception.printStackTrace();
            });
        
        // Create thread with exception handling
        Thread workerThread = new Thread(new SafeWorker());
        
        // Set specific exception handler for this thread
        workerThread.setUncaughtExceptionHandler(
            (thread, exception) -> {
                System.err.println("Worker thread failed: " + exception.getMessage());
                // Could restart thread, log error, etc.
            });
        
        workerThread.start();
    }
    
    static class SafeWorker implements Runnable {
        @Override
        public void run() {
            try {
                // Perform work
                performRiskyOperation();
            } catch (Exception e) {
                // Handle expected exceptions
                System.err.println("Handled exception: " + e.getMessage());
            }
        }
        
        private void performRiskyOperation() throws Exception {
            if (Math.random() < 0.3) {
                throw new RuntimeException("Random failure");
            }
            System.out.println("Work completed successfully");
        }
    }
}
```

### 5. Resource Management
```java
public class ResourceManagement {
    
    // GOOD: Use try-with-resources for ExecutorService
    public void properResourceManagement() {
        try (ExecutorService executor = Executors.newFixedThreadPool(4)) {
            // Submit tasks
            for (int i = 0; i < 10; i++) {
                executor.submit(this::performTask);
            }
            
            // ExecutorService will be shut down automatically
        }
    }
    
    // Alternative: Manual resource management
    public void manualResourceManagement() {
        ExecutorService executor = Executors.newFixedThreadPool(4);
        
        try {
            // Submit tasks
            for (int i = 0; i < 10; i++) {
                executor.submit(this::performTask);
            }
        } finally {
            // Ensure proper shutdown
            executor.shutdown();
            
            try {
                if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                    executor.shutdownNow();
                }
            } catch (InterruptedException e) {
                executor.shutdownNow();
                Thread.currentThread().interrupt();
            }
        }
    }
    
    private void performTask() {
        System.out.println("Task executed by " + 
                          Thread.currentThread().getName());
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

- 🧵 **Thread Creation**: Multiple approaches - Thread class vs Runnable interface
- 🏗️ **Thread Management**: Lifecycle, states, and proper shutdown
- 🔧 **Thread Pools**: ExecutorService, fixed pools, cached pools, custom pools
- 📋 **Synchronization**: synchronized methods/blocks, wait/notify pattern
- ⚡ **Best Practices**: Resource management, exception handling, interruption
- 🎯 **Real Applications**: Banking systems, task schedulers, concurrent processing
- 🔄 **Advanced Features**: Custom thread factories, rejection handlers

</v-clicks>

## Thread Creation Comparison

| Aspect | Thread Extension | Runnable Interface |
|--------|-----------------|-------------------|
| Inheritance | Single inheritance limitation | Can extend other classes |
| Flexibility | Less flexible | More flexible |
| Reusability | Tightly coupled to Thread | Better separation of concerns |
| Best Practice | Generally avoided | Recommended approach |

## Thread Pool Types

### Fixed Thread Pool
- **Use case**: Known workload, consistent resource usage
- **Pros**: Predictable resource usage, stable performance
- **Cons**: May not utilize all available resources

### Cached Thread Pool  
- **Use case**: Varying workload, short-lived tasks
- **Pros**: Adapts to workload, reuses idle threads
- **Cons**: Can create too many threads under load

### Custom Thread Pool
- **Use case**: Specific requirements, fine-tuned control
- **Pros**: Maximum control, optimized for specific needs
- **Cons**: More complex setup and management

</div>

<div>

## Key Concepts Recap

<v-clicks>

- **Thread Lifecycle**: NEW → RUNNABLE → BLOCKED/WAITING → TERMINATED
- **Thread Safety**: Ensuring correct behavior in concurrent environment
- **Race Conditions**: Avoided through proper synchronization
- **Deadlocks**: Prevented through careful lock ordering
- **Resource Management**: Proper cleanup and shutdown procedures
- **Exception Handling**: Managing errors in multithreaded environment
- **Performance**: Balancing parallelism with overhead

</v-clicks>

## Synchronization Mechanisms

### synchronized keyword
```java
synchronized (lock) {
    // Critical section
    sharedResource.modify();
}
```

### wait/notify pattern
```java
synchronized (lock) {
    while (condition) {
        lock.wait();
    }
    // Process
    lock.notifyAll();
}
```

### Thread-safe collections
```java
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
BlockingQueue<Task> queue = new LinkedBlockingQueue<>();
```

## Best Practices Summary

1. **Prefer Runnable over Thread extension**
2. **Use thread pools instead of creating individual threads**
3. **Handle interruptions properly**
4. **Minimize synchronization scope**
5. **Use concurrent collections when appropriate**
6. **Always clean up resources**
7. **Handle exceptions in threads**
8. **Monitor thread pool metrics**

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Thread Creation and Management Complete

**Lecture 31 Successfully Completed!**  
You now understand how to create and manage threads effectively in Java

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready for advanced concurrency patterns! <carbon:arrow-right class="inline"/>
  </span>
</div>