---
theme: default
background: https://source.unsplash.com/1024x768/?implementation,structure
title: Interface Implementation
info: |
  ## Java Programming (4343203)
  
  Lecture 24: Interface Implementation
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about implementing multiple interfaces, resolving method conflicts, interface hierarchies, composition patterns, and advanced implementation strategies.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Interface Implementation
## Lecture 24

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

- 🔧 **Implement** multiple interfaces in a single class effectively
- ⚔️ **Resolve** method name conflicts between interfaces
- 🏗️ **Design** interface hierarchies and inheritance relationships
- 🎯 **Apply** composition and delegation patterns with interfaces
- ⚡ **Handle** default method conflicts and resolution strategies
- 📝 **Create** flexible architectures using interface implementation
- 🛠️ **Practice** advanced implementation patterns and techniques

</v-clicks>

---
layout: default
---

# Multiple Interface Implementation

<div class="grid grid-cols-2 gap-6">

<div>

## Basic Multiple Implementation
```java
public interface Drawable {
    void draw();
    
    default void prepare() {
        System.out.println("Preparing to draw");
    }
}

public interface Movable {
    void move(int x, int y);
    
    default void prepare() {
        System.out.println("Preparing to move");
    }
}

public interface Scalable {
    void scale(double factor);
}

// Implementing multiple interfaces
public class GameObject implements Drawable, Movable, Scalable {
    private int x, y;
    private double size = 1.0;
    private String name;
    
    public GameObject(String name) {
        this.name = name;
        this.x = 0;
        this.y = 0;
    }
    
    // Must resolve default method conflict
    @Override
    public void prepare() {
        System.out.println("Preparing " + name + " for operation");
        // Can call specific interface methods if needed
        // Drawable.super.prepare();
        // Movable.super.prepare();
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
        if (factor > 0) {
            this.size *= factor;
            System.out.println(name + " scaled by factor " + factor);
        }
    }
}
```

</div>

<div>

## Using Multiple Interface References
```java
public class GameDemo {
    public static void main(String[] args) {
        GameObject player = new GameObject("Player");
        
        // Can be referenced by any implemented interface
        Drawable drawable = player;
        Movable movable = player;
        Scalable scalable = player;
        
        // Using through different interface references
        drawable.prepare();
        drawable.draw();
        
        movable.prepare();  // Same object, different interface view
        movable.move(10, 20);
        
        scalable.scale(1.5);
        
        // Using as concrete class
        player.draw();  // Shows updated position and size
    }
}
```

### Output:
```
Preparing Player for operation
Drawing Player at (0,0) with size 1.0
Preparing Player for operation
Player moved to (10,20)
Player scaled by factor 1.5
Drawing Player at (10,20) with size 1.5
```

## Benefits of Multiple Implementation
- **Behavioral Composition**: Combine different capabilities
- **Polymorphic Usage**: Use object through different interface views
- **Flexible Design**: Easy to extend with new interfaces
- **Code Reuse**: Share implementations across similar classes

</div>

</div>

---
layout: default
---

# Resolving Default Method Conflicts

<div class="grid grid-cols-2 gap-6">

<div>

## Diamond Problem with Default Methods
```java
public interface A {
    default void method() {
        System.out.println("A's implementation");
    }
    
    default String getInfo() {
        return "Interface A";
    }
}

public interface B {
    default void method() {
        System.out.println("B's implementation");
    }
    
    default String getDetails() {
        return "Interface B";
    }
}

public interface C extends A, B {
    // Must resolve the conflict
    @Override
    default void method() {
        System.out.println("C's resolution:");
        A.super.method();  // Call A's version
        B.super.method();  // Call B's version
        System.out.println("Combined in C");
    }
}
```

## Implementation Class Resolution
```java
public class DiamondResolver implements A, B {
    @Override
    public void method() {
        // Strategy 1: Choose one interface
        A.super.method();
        
        // Strategy 2: Combine both
        // System.out.println("Combining A and B:");
        // A.super.method();
        // B.super.method();
        
        // Strategy 3: Completely new implementation
        // System.out.println("Custom implementation");
    }
    
    // Can use other default methods without conflict
    public void displayInfo() {
        System.out.println(getInfo());     // From A
        System.out.println(getDetails());  // From B
    }
}
```

</div>

<div>

## Complex Hierarchy Resolution
```java
public interface Vehicle {
    default void start() {
        System.out.println("Vehicle starting...");
    }
    
    default void stop() {
        System.out.println("Vehicle stopping...");
    }
}

public interface Electric {
    default void start() {
        System.out.println("Electric system starting...");
    }
    
    default void charge() {
        System.out.println("Charging battery...");
    }
}

public interface Autonomous {
    default void start() {
        System.out.println("Autonomous system starting...");
    }
    
    default void enableAutoPilot() {
        System.out.println("Auto-pilot enabled");
    }
}

public class ElectricAutonomousCar 
    implements Vehicle, Electric, Autonomous {
    
    @Override
    public void start() {
        System.out.println("Starting Electric Autonomous Car:");
        Vehicle.super.start();     // Base vehicle start
        Electric.super.start();    // Electric system start
        Autonomous.super.start();  // Autonomous system start
        System.out.println("All systems ready!");
    }
    
    // Other methods inherited without conflict
    public void performOperations() {
        charge();           // From Electric
        enableAutoPilot();  // From Autonomous
        stop();            // From Vehicle (no conflict)
    }
}
```

### Resolution Strategies
1. **Explicit Selection**: Choose one interface's implementation
2. **Combination**: Call multiple interface implementations
3. **Custom Implementation**: Provide completely new logic
4. **Hierarchical**: Use super interface calls strategically

</div>

</div>

---
layout: default
---

# Interface Hierarchies and Inheritance

<div class="grid grid-cols-2 gap-6">

<div>

## Interface Inheritance Chain
```java
// Base interface
public interface Animal {
    void makeSound();
    
    default void breathe() {
        System.out.println("Breathing...");
    }
    
    default String getCategory() {
        return "Animal";
    }
}

// Extending interface
public interface Mammal extends Animal {
    void giveMilk();
    
    @Override
    default String getCategory() {
        return "Mammal";
    }
    
    default void regulateTemperature() {
        System.out.println("Regulating body temperature");
    }
}

// Further extending
public interface Carnivore extends Mammal {
    void hunt();
    
    @Override
    default String getCategory() {
        return "Carnivorous Mammal";
    }
    
    default void eatMeat() {
        System.out.println("Eating meat");
    }
}

// Multiple inheritance in interfaces
public interface Domesticated {
    void obeyCommands();
    
    default void showAffection() {
        System.out.println("Showing affection to humans");
    }
}
```

</div>

<div>

## Implementing Interface Hierarchy
```java
public class Dog implements Carnivore, Domesticated {
    private String name;
    private String breed;
    
    public Dog(String name, String breed) {
        this.name = name;
        this.breed = breed;
    }
    
    // Implementing Animal methods
    @Override
    public void makeSound() {
        System.out.println(name + " says Woof!");
    }
    
    // Implementing Mammal methods
    @Override
    public void giveMilk() {
        System.out.println(name + " is nursing puppies");
    }
    
    // Implementing Carnivore methods
    @Override
    public void hunt() {
        System.out.println(name + " is hunting for prey");
    }
    
    // Implementing Domesticated methods
    @Override
    public void obeyCommands() {
        System.out.println(name + " is obeying commands");
    }
    
    // Override default methods if needed
    @Override
    public void showAffection() {
        System.out.println(name + " is wagging tail and being friendly");
    }
    
    // Can access all inherited default methods
    public void performAllBehaviors() {
        makeSound();              // Abstract method implementation
        breathe();               // From Animal (default)
        regulateTemperature();   // From Mammal (default)
        eatMeat();              // From Carnivore (default)
        showAffection();        // Overridden default
        System.out.println("Category: " + getCategory()); // From Carnivore
    }
}
```

## Usage Example
```java
public class AnimalDemo {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy", "Golden Retriever");
        
        // Can be referenced by any interface in hierarchy
        Animal animal = dog;
        Mammal mammal = dog;
        Carnivore carnivore = dog;
        Domesticated pet = dog;
        
        // Different interface views
        animal.makeSound();
        mammal.giveMilk();
        carnivore.hunt();
        pet.obeyCommands();
        
        dog.performAllBehaviors();
    }
}
```

</div>

</div>

---
layout: default
---

# Composition and Delegation Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Composition with Interfaces
```java
// Service interfaces
public interface DatabaseService {
    void saveData(String data);
    String loadData(String key);
    
    default void backup() {
        System.out.println("Backing up database");
    }
}

public interface CacheService {
    void cache(String key, String value);
    String getFromCache(String key);
    void clearCache();
    
    default void warmup() {
        System.out.println("Warming up cache");
    }
}

public interface LoggingService {
    void log(String message);
    void logError(String error);
    
    default void logInfo(String info) {
        log("INFO: " + info);
    }
}

// Composite service using composition
public class DataManager implements DatabaseService, CacheService, LoggingService {
    // Composition - delegate to specialized implementations
    private final DatabaseService database;
    private final CacheService cache;
    private final LoggingService logger;
    
    public DataManager(DatabaseService database, 
                      CacheService cache, 
                      LoggingService logger) {
        this.database = database;
        this.cache = cache;
        this.logger = logger;
    }
    
    // DatabaseService implementation - delegation
    @Override
    public void saveData(String data) {
        logInfo("Saving data: " + data);
        database.saveData(data);
        cache.cache(data, data); // Also cache it
    }
    
    @Override
    public String loadData(String key) {
        logInfo("Loading data for key: " + key);
        
        // Try cache first
        String cachedData = cache.getFromCache(key);
        if (cachedData != null) {
            logInfo("Data found in cache");
            return cachedData;
        }
        
        // Load from database
        String data = database.loadData(key);
        if (data != null) {
            cache.cache(key, data); // Cache for next time
        }
        return data;
    }
    
    // CacheService implementation - delegation
    @Override
    public void cache(String key, String value) {
        cache.cache(key, value);
    }
    
    @Override
    public String getFromCache(String key) {
        return cache.getFromCache(key);
    }
    
    @Override
    public void clearCache() {
        logInfo("Clearing cache");
        cache.clearCache();
    }
    
    // LoggingService implementation - delegation
    @Override
    public void log(String message) {
        logger.log(message);
    }
    
    @Override
    public void logError(String error) {
        logger.logError(error);
    }
}
```

</div>

<div>

## Dynamic Delegation Pattern
```java
public interface Processor {
    void process(String data);
    String getProcessorType();
}

public class FastProcessor implements Processor {
    @Override
    public void process(String data) {
        System.out.println("Fast processing: " + data);
    }
    
    @Override
    public String getProcessorType() { return "Fast"; }
}

public class SecureProcessor implements Processor {
    @Override
    public void process(String data) {
        System.out.println("Secure processing: " + encrypt(data));
    }
    
    private String encrypt(String data) {
        return "encrypted(" + data + ")";
    }
    
    @Override
    public String getProcessorType() { return "Secure"; }
}

// Adaptive processor that delegates based on conditions
public class AdaptiveProcessor implements Processor {
    private Processor fastProcessor = new FastProcessor();
    private Processor secureProcessor = new SecureProcessor();
    private boolean securityMode = false;
    
    public void enableSecurity(boolean enabled) {
        this.securityMode = enabled;
    }
    
    @Override
    public void process(String data) {
        Processor delegate = securityMode ? secureProcessor : fastProcessor;
        System.out.println("Delegating to " + delegate.getProcessorType() + " processor");
        delegate.process(data);
    }
    
    @Override
    public String getProcessorType() {
        return "Adaptive(" + 
               (securityMode ? secureProcessor.getProcessorType() : 
                              fastProcessor.getProcessorType()) + ")";
    }
}

// Usage
public class ProcessorDemo {
    public static void main(String[] args) {
        AdaptiveProcessor processor = new AdaptiveProcessor();
        
        System.out.println("Normal mode:");
        processor.process("sensitive data");
        
        System.out.println("\nSecure mode:");
        processor.enableSecurity(true);
        processor.process("sensitive data");
        
        System.out.println("Type: " + processor.getProcessorType());
    }
}
```

</div>

</div>

---
layout: default
---

# Practical Example: Plugin Architecture

<div class="grid grid-cols-2 gap-6">

<div>

## Plugin Interface Hierarchy
```java
// Base plugin interface
public interface Plugin {
    String getName();
    String getVersion();
    void initialize();
    void shutdown();
    
    default boolean isEnabled() {
        return true;
    }
    
    default String getDescription() {
        return "Plugin: " + getName() + " v" + getVersion();
    }
}

// Configurable plugin
public interface ConfigurablePlugin extends Plugin {
    void configure(Properties config);
    Properties getConfiguration();
    
    default void resetConfiguration() {
        configure(new Properties());
    }
}

// Service provider plugin
public interface ServicePlugin extends ConfigurablePlugin {
    void startService();
    void stopService();
    boolean isServiceRunning();
    
    default void restartService() {
        if (isServiceRunning()) {
            stopService();
        }
        startService();
    }
}

// UI plugin
public interface UIPlugin extends Plugin {
    void createUI();
    void destroyUI();
    void showUI(boolean visible);
    
    default void toggleUI() {
        showUI(!isUIVisible());
    }
    
    boolean isUIVisible();
}

// Event handling capability
public interface EventHandlerPlugin {
    void handleEvent(String eventType, Object eventData);
    String[] getSupportedEvents();
    
    default boolean canHandle(String eventType) {
        String[] supported = getSupportedEvents();
        for (String type : supported) {
            if (type.equals(eventType)) {
                return true;
            }
        }
        return false;
    }
}
```

</div>

<div>

## Concrete Plugin Implementation
```java
// Database backup plugin
public class DatabaseBackupPlugin 
    implements ServicePlugin, EventHandlerPlugin {
    
    private String name = "DB Backup";
    private String version = "1.0";
    private Properties config = new Properties();
    private boolean serviceRunning = false;
    private boolean initialized = false;
    
    @Override
    public String getName() { return name; }
    
    @Override
    public String getVersion() { return version; }
    
    @Override
    public void initialize() {
        System.out.println("Initializing " + getDescription());
        // Set default configuration
        config.setProperty("backup.interval", "3600"); // 1 hour
        config.setProperty("backup.location", "/backups");
        initialized = true;
    }
    
    @Override
    public void shutdown() {
        if (serviceRunning) {
            stopService();
        }
        System.out.println("Shutting down " + getName());
        initialized = false;
    }
    
    @Override
    public void configure(Properties config) {
        this.config.putAll(config);
        System.out.println("Plugin configured with " + config.size() + " properties");
    }
    
    @Override
    public Properties getConfiguration() {
        return new Properties(config); // Return copy
    }
    
    @Override
    public void startService() {
        if (!initialized) {
            throw new IllegalStateException("Plugin not initialized");
        }
        if (!serviceRunning) {
            serviceRunning = true;
            String interval = config.getProperty("backup.interval", "3600");
            System.out.println("Backup service started with interval: " + interval + "s");
        }
    }
    
    @Override
    public void stopService() {
        if (serviceRunning) {
            serviceRunning = false;
            System.out.println("Backup service stopped");
        }
    }
    
    @Override
    public boolean isServiceRunning() {
        return serviceRunning;
    }
    
    @Override
    public void handleEvent(String eventType, Object eventData) {
        if ("data.changed".equals(eventType)) {
            System.out.println("Data changed event received, triggering backup");
            performBackup();
        } else if ("system.shutdown".equals(eventType)) {
            System.out.println("System shutdown event, performing final backup");
            performBackup();
        }
    }
    
    @Override
    public String[] getSupportedEvents() {
        return new String[]{"data.changed", "system.shutdown"};
    }
    
    private void performBackup() {
        String location = config.getProperty("backup.location");
        System.out.println("Performing backup to: " + location);
    }
    
    @Override
    public boolean isEnabled() {
        return initialized && Boolean.parseBoolean(
            config.getProperty("enabled", "true"));
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Media Processing System

<div class="grid grid-cols-2 gap-6">

<div>

## Task
Create a media processing system with multiple interface implementations:

## Media Processing Interfaces
```java
// Base media interface
public interface Media {
    String getFileName();
    long getFileSize();
    String getFormat();
    
    default String getDisplayName() {
        return getFileName() + " (" + getFormat() + ")";
    }
}

// Playable media
public interface Playable extends Media {
    void play();
    void pause();
    void stop();
    boolean isPlaying();
    
    default void togglePlayback() {
        if (isPlaying()) {
            pause();
        } else {
            play();
        }
    }
}

// Editable media
public interface Editable {
    void cut(int startTime, int endTime);
    void copy(int startTime, int endTime);
    void paste(int position);
    void undo();
    
    default void trim(int startTime, int endTime) {
        cut(0, startTime);
        cut(endTime, getDuration());
    }
    
    int getDuration();
}

// Convertible media
public interface Convertible {
    boolean convertTo(String format);
    String[] getSupportedFormats();
    
    default boolean canConvertTo(String format) {
        String[] formats = getSupportedFormats();
        for (String f : formats) {
            if (f.equalsIgnoreCase(format)) {
                return true;
            }
        }
        return false;
    }
}

// Streamable media
public interface Streamable {
    void startStream(String url);
    void stopStream();
    boolean isStreaming();
    int getViewerCount();
    
    default String getStreamStatus() {
        return isStreaming() ? 
            "Streaming to " + getViewerCount() + " viewers" : 
            "Not streaming";
    }
}
```

</div>

<div>

## Implementation Classes
```java
// Video file implementation
public class VideoFile implements Playable, Editable, Convertible, Streamable {
    private String fileName;
    private long fileSize;
    private String format;
    private int duration;
    private boolean playing = false;
    private boolean streaming = false;
    private int viewerCount = 0;
    
    public VideoFile(String fileName, long fileSize, 
                    String format, int duration) {
        this.fileName = fileName;
        this.fileSize = fileSize;
        this.format = format;
        this.duration = duration;
    }
    
    // Media interface implementation
    @Override
    public String getFileName() { return fileName; }
    
    @Override
    public long getFileSize() { return fileSize; }
    
    @Override
    public String getFormat() { return format; }
    
    // Playable interface implementation
    @Override
    public void play() {
        if (!playing) {
            playing = true;
            System.out.println("Playing video: " + getDisplayName());
        }
    }
    
    @Override
    public void pause() {
        if (playing) {
            playing = false;
            System.out.println("Paused video: " + fileName);
        }
    }
    
    @Override
    public void stop() {
        playing = false;
        System.out.println("Stopped video: " + fileName);
    }
    
    @Override
    public boolean isPlaying() { return playing; }
    
    // Editable interface implementation
    @Override
    public void cut(int startTime, int endTime) {
        System.out.println("Cutting video from " + startTime + "s to " + endTime + "s");
        duration = duration - (endTime - startTime);
    }
    
    @Override
    public void copy(int startTime, int endTime) {
        System.out.println("Copying video segment from " + startTime + "s to " + endTime + "s");
    }
    
    @Override
    public void paste(int position) {
        System.out.println("Pasting video segment at " + position + "s");
    }
    
    @Override
    public void undo() {
        System.out.println("Undoing last edit operation");
    }
    
    @Override
    public int getDuration() { return duration; }
    
    // Convertible interface implementation
    @Override
    public boolean convertTo(String targetFormat) {
        if (canConvertTo(targetFormat)) {
            System.out.println("Converting " + fileName + " from " + 
                             format + " to " + targetFormat);
            this.format = targetFormat;
            return true;
        }
        return false;
    }
    
    @Override
    public String[] getSupportedFormats() {
        return new String[]{"mp4", "avi", "mov", "mkv"};
    }
    
    // Streamable interface implementation
    @Override
    public void startStream(String url) {
        if (!streaming) {
            streaming = true;
            viewerCount = 0;
            System.out.println("Started streaming " + fileName + " to " + url);
        }
    }
    
    @Override
    public void stopStream() {
        if (streaming) {
            streaming = false;
            System.out.println("Stopped streaming " + fileName);
            viewerCount = 0;
        }
    }
    
    @Override
    public boolean isStreaming() { return streaming; }
    
    @Override
    public int getViewerCount() { return viewerCount; }
    
    public void simulateViewers(int count) {
        if (streaming) {
            viewerCount = count;
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Smart Home System

<div class="grid grid-cols-2 gap-6">

<div>

## Smart Home Interfaces
```java
// Base device interface
public interface SmartDevice {
    String getDeviceId();
    String getDeviceName();
    boolean isOnline();
    void connect();
    void disconnect();
    
    default String getStatus() {
        return getDeviceName() + " (" + getDeviceId() + "): " + 
               (isOnline() ? "Online" : "Offline");
    }
}

// Controllable device
public interface Controllable extends SmartDevice {
    void turnOn();
    void turnOff();
    boolean isOn();
    
    default void toggle() {
        if (isOn()) {
            turnOff();
        } else {
            turnOn();
        }
    }
}

// Dimmable device
public interface Dimmable extends Controllable {
    void setBrightness(int level); // 0-100
    int getBrightness();
    
    default void dim() {
        setBrightness(Math.max(0, getBrightness() - 20));
    }
    
    default void brighten() {
        setBrightness(Math.min(100, getBrightness() + 20));
    }
}

// Thermostat control
public interface TemperatureControllable extends Controllable {
    void setTemperature(double temperature);
    double getCurrentTemperature();
    double getTargetTemperature();
    
    default void increaseTemperature(double delta) {
        setTemperature(getTargetTemperature() + delta);
    }
    
    default void decreaseTemperature(double delta) {
        setTemperature(getTargetTemperature() - delta);
    }
}

// Security device
public interface SecurityDevice extends SmartDevice {
    void arm();
    void disarm();
    boolean isArmed();
    void triggerAlarm();
    
    default void handleSecurityEvent(String eventType) {
        if (isArmed() && ("motion".equals(eventType) || 
                         "breach".equals(eventType))) {
            triggerAlarm();
        }
    }
}

// Monitoring capability
public interface Monitorable {
    String[] getAvailableMetrics();
    double getMetricValue(String metricName);
    void startMonitoring();
    void stopMonitoring();
    
    default void displayMetrics() {
        System.out.println("Device Metrics:");
        for (String metric : getAvailableMetrics()) {
            System.out.println("  " + metric + ": " + getMetricValue(metric));
        }
    }
}
```

</div>

<div>

## Smart Device Implementations
```java
// Smart light implementation
public class SmartLight implements Dimmable, Monitorable {
    private String deviceId;
    private String deviceName;
    private boolean online = false;
    private boolean on = false;
    private int brightness = 100;
    private double powerConsumption = 0.0;
    
    public SmartLight(String deviceId, String deviceName) {
        this.deviceId = deviceId;
        this.deviceName = deviceName;
    }
    
    // SmartDevice implementation
    @Override
    public String getDeviceId() { return deviceId; }
    
    @Override
    public String getDeviceName() { return deviceName; }
    
    @Override
    public boolean isOnline() { return online; }
    
    @Override
    public void connect() {
        online = true;
        System.out.println(deviceName + " connected to network");
    }
    
    @Override
    public void disconnect() {
        online = false;
        on = false;
        System.out.println(deviceName + " disconnected from network");
    }
    
    // Controllable implementation
    @Override
    public void turnOn() {
        if (online) {
            on = true;
            powerConsumption = (brightness / 100.0) * 10; // 10W max
            System.out.println(deviceName + " turned on at " + brightness + "% brightness");
        }
    }
    
    @Override
    public void turnOff() {
        on = false;
        powerConsumption = 0.0;
        System.out.println(deviceName + " turned off");
    }
    
    @Override
    public boolean isOn() { return on; }
    
    // Dimmable implementation
    @Override
    public void setBrightness(int level) {
        if (level < 0) level = 0;
        if (level > 100) level = 100;
        brightness = level;
        
        if (on) {
            powerConsumption = (brightness / 100.0) * 10;
            System.out.println(deviceName + " brightness set to " + brightness + "%");
        }
    }
    
    @Override
    public int getBrightness() { return brightness; }
    
    // Monitorable implementation
    @Override
    public String[] getAvailableMetrics() {
        return new String[]{"power_consumption", "brightness_level", "online_status"};
    }
    
    @Override
    public double getMetricValue(String metricName) {
        switch (metricName) {
            case "power_consumption": return powerConsumption;
            case "brightness_level": return brightness;
            case "online_status": return online ? 1.0 : 0.0;
            default: return 0.0;
        }
    }
    
    @Override
    public void startMonitoring() {
        System.out.println("Started monitoring " + deviceName);
    }
    
    @Override
    public void stopMonitoring() {
        System.out.println("Stopped monitoring " + deviceName);
    }
}

// Smart thermostat implementation
public class SmartThermostat implements TemperatureControllable, Monitorable {
    private String deviceId;
    private String deviceName;
    private boolean online = false;
    private boolean on = false;
    private double currentTemperature = 20.0;
    private double targetTemperature = 22.0;
    private double powerConsumption = 0.0;
    
    public SmartThermostat(String deviceId, String deviceName) {
        this.deviceId = deviceId;
        this.deviceName = deviceName;
    }
    
    @Override
    public String getDeviceId() { return deviceId; }
    
    @Override
    public String getDeviceName() { return deviceName; }
    
    @Override
    public boolean isOnline() { return online; }
    
    @Override
    public void connect() {
        online = true;
        System.out.println(deviceName + " connected to network");
    }
    
    @Override
    public void disconnect() {
        online = false;
        on = false;
        System.out.println(deviceName + " disconnected");
    }
    
    @Override
    public void turnOn() {
        if (online) {
            on = true;
            powerConsumption = 500.0; // 500W
            System.out.println(deviceName + " turned on, target: " + targetTemperature + "°C");
        }
    }
    
    @Override
    public void turnOff() {
        on = false;
        powerConsumption = 0.0;
        System.out.println(deviceName + " turned off");
    }
    
    @Override
    public boolean isOn() { return on; }
    
    @Override
    public void setTemperature(double temperature) {
        this.targetTemperature = temperature;
        if (on) {
            System.out.println(deviceName + " target temperature set to " + temperature + "°C");
            // Simulate temperature adjustment
            adjustCurrentTemperature();
        }
    }
    
    @Override
    public double getCurrentTemperature() { return currentTemperature; }
    
    @Override
    public double getTargetTemperature() { return targetTemperature; }
    
    private void adjustCurrentTemperature() {
        // Simulate gradual temperature change
        if (currentTemperature < targetTemperature) {
            currentTemperature = Math.min(targetTemperature, currentTemperature + 0.5);
        } else if (currentTemperature > targetTemperature) {
            currentTemperature = Math.max(targetTemperature, currentTemperature - 0.5);
        }
    }
    
    @Override
    public String[] getAvailableMetrics() {
        return new String[]{"current_temperature", "target_temperature", "power_consumption"};
    }
    
    @Override
    public double getMetricValue(String metricName) {
        switch (metricName) {
            case "current_temperature": return currentTemperature;
            case "target_temperature": return targetTemperature;
            case "power_consumption": return powerConsumption;
            default: return 0.0;
        }
    }
    
    @Override
    public void startMonitoring() {
        System.out.println("Started monitoring " + deviceName);
    }
    
    @Override
    public void stopMonitoring() {
        System.out.println("Stopped monitoring " + deviceName);
    }
}
```

</div>

</div>

---
layout: default
---

# Interface Implementation Best Practices

<div class="grid grid-cols-2 gap-6">

<div>

## Design Guidelines

### 1. Favor Composition over Inheritance
```java
// GOOD: Composition approach
public interface Logger {
    void log(String message);
}

public interface DatabaseConnector {
    void connect();
    void execute(String query);
}

public class UserService {
    private final Logger logger;
    private final DatabaseConnector db;
    
    public UserService(Logger logger, DatabaseConnector db) {
        this.logger = logger;
        this.db = db;
    }
    
    public void createUser(String username) {
        logger.log("Creating user: " + username);
        db.execute("INSERT INTO users...");
    }
}

// Rather than complex inheritance hierarchy
```

### 2. Keep Interfaces Focused
```java
// GOOD: Single Responsibility
public interface UserReader {
    User findById(String id);
    List<User> findAll();
}

public interface UserWriter {
    void save(User user);
    void delete(String id);
}

// BAD: Mixed responsibilities
public interface UserManager {
    User findById(String id);
    void save(User user);
    void sendEmail(String to, String message);
    void generateReport();
}
```

</div>

<div>

### 3. Use Default Methods Wisely
```java
public interface Calculator {
    // Core operations - must be implemented
    double add(double a, double b);
    double subtract(double a, double b);
    
    // Convenience methods - default implementations
    default double addAll(double... numbers) {
        double result = 0;
        for (double num : numbers) {
            result = add(result, num);
        }
        return result;
    }
    
    default double square(double number) {
        return add(number, number); // Reuse existing method
    }
}
```

### 4. Handle Method Conflicts Explicitly
```java
public interface A {
    default String getValue() { return "A"; }
}

public interface B {
    default String getValue() { return "B"; }
}

public class Implementation implements A, B {
    @Override
    public String getValue() {
        // Explicit resolution with business logic
        return "Combined: " + A.super.getValue() + "-" + B.super.getValue();
    }
}
```

### 5. Document Interface Contracts
```java
/**
 * Processes payment transactions with validation and logging.
 * 
 * Implementations must ensure:
 * - Thread safety for concurrent processing
 * - Proper validation of payment amounts
 * - Comprehensive error logging
 * - Transaction rollback on failures
 */
public interface PaymentProcessor {
    /**
     * Processes a payment transaction.
     * 
     * @param amount payment amount (must be positive)
     * @param currency currency code (ISO 4217)
     * @return transaction result with success status
     * @throws IllegalArgumentException if amount <= 0 or currency is invalid
     * @throws PaymentException if processing fails
     */
    PaymentResult processPayment(BigDecimal amount, String currency) 
        throws PaymentException;
}
```

</div>

</div>

---
layout: default
---

# Advanced Implementation Patterns

<div class="grid grid-cols-2 gap-6">

<div>

## Adapter Pattern with Interfaces
```java
// Third-party library interface
public interface ExternalPaymentGateway {
    boolean processTransaction(String cardNumber, double amount);
    String getLastError();
}

// Our standard interface
public interface PaymentService {
    PaymentResult processPayment(PaymentRequest request);
}

// Adapter implementation
public class PaymentGatewayAdapter implements PaymentService {
    private final ExternalPaymentGateway gateway;
    
    public PaymentGatewayAdapter(ExternalPaymentGateway gateway) {
        this.gateway = gateway;
    }
    
    @Override
    public PaymentResult processPayment(PaymentRequest request) {
        boolean success = gateway.processTransaction(
            request.getCardNumber(), 
            request.getAmount()
        );
        
        if (success) {
            return new PaymentResult(true, "Transaction completed");
        } else {
            return new PaymentResult(false, gateway.getLastError());
        }
    }
}
```

## Proxy Pattern with Interfaces
```java
// Service interface
public interface DataService {
    String getData(String key);
    void saveData(String key, String data);
}

// Actual service implementation
public class DatabaseService implements DataService {
    @Override
    public String getData(String key) {
        System.out.println("Loading data from database: " + key);
        // Simulate database access
        return "data_" + key;
    }
    
    @Override
    public void saveData(String key, String data) {
        System.out.println("Saving to database: " + key + " = " + data);
        // Simulate database save
    }
}

// Caching proxy
public class CachingDataServiceProxy implements DataService {
    private final DataService realService;
    private final Map<String, String> cache = new HashMap<>();
    
    public CachingDataServiceProxy(DataService realService) {
        this.realService = realService;
    }
    
    @Override
    public String getData(String key) {
        if (cache.containsKey(key)) {
            System.out.println("Cache hit for: " + key);
            return cache.get(key);
        }
        
        System.out.println("Cache miss for: " + key);
        String data = realService.getData(key);
        cache.put(key, data);
        return data;
    }
    
    @Override
    public void saveData(String key, String data) {
        realService.saveData(key, data);
        cache.put(key, data); // Update cache
    }
}
```

</div>

<div>

## Chain of Responsibility with Interfaces
```java
// Handler interface
public interface RequestHandler {
    void setNext(RequestHandler next);
    void handle(Request request);
    
    default boolean canHandle(Request request) {
        return false;
    }
}

// Base handler implementation
public abstract class AbstractRequestHandler implements RequestHandler {
    private RequestHandler next;
    
    @Override
    public void setNext(RequestHandler next) {
        this.next = next;
    }
    
    @Override
    public void handle(Request request) {
        if (canHandle(request)) {
            processRequest(request);
        } else if (next != null) {
            next.handle(request);
        } else {
            System.out.println("No handler found for request: " + request.getType());
        }
    }
    
    protected abstract void processRequest(Request request);
}

// Specific handlers
public class AuthenticationHandler extends AbstractRequestHandler {
    @Override
    public boolean canHandle(Request request) {
        return "AUTH".equals(request.getType());
    }
    
    @Override
    protected void processRequest(Request request) {
        System.out.println("Processing authentication request");
    }
}

public class DataHandler extends AbstractRequestHandler {
    @Override
    public boolean canHandle(Request request) {
        return "DATA".equals(request.getType());
    }
    
    @Override
    protected void processRequest(Request request) {
        System.out.println("Processing data request");
    }
}

// Usage
public class ChainDemo {
    public static void main(String[] args) {
        RequestHandler authHandler = new AuthenticationHandler();
        RequestHandler dataHandler = new DataHandler();
        
        authHandler.setNext(dataHandler);
        
        authHandler.handle(new Request("AUTH"));
        authHandler.handle(new Request("DATA"));
        authHandler.handle(new Request("UNKNOWN"));
    }
}
```

## Command Pattern with Functional Interfaces
```java
@FunctionalInterface
public interface Command {
    void execute();
    
    default Command andThen(Command after) {
        return () -> {
            this.execute();
            after.execute();
        };
    }
}

// Command invoker
public class RemoteControl {
    private Command command;
    
    public void setCommand(Command command) {
        this.command = command;
    }
    
    public void pressButton() {
        if (command != null) {
            command.execute();
        }
    }
}

// Usage with lambdas
public class CommandDemo {
    public static void main(String[] args) {
        RemoteControl remote = new RemoteControl();
        
        // Lambda commands
        Command lightOn = () -> System.out.println("Light turned on");
        Command fanOn = () -> System.out.println("Fan turned on");
        Command musicOn = () -> System.out.println("Music started");
        
        // Composite command
        Command eveningMode = lightOn.andThen(fanOn).andThen(musicOn);
        
        remote.setCommand(eveningMode);
        remote.pressButton();
    }
}
```

</div>

</div>

---
layout: default
---

# Testing Interface Implementations

<div class="grid grid-cols-2 gap-6">

<div>

## Mock Implementation for Testing
```java
// Service interface
public interface EmailService {
    boolean sendEmail(String to, String subject, String body);
    int getEmailsSentToday();
}

// Mock implementation for testing
public class MockEmailService implements EmailService {
    private List<Email> sentEmails = new ArrayList<>();
    private boolean shouldFail = false;
    
    @Override
    public boolean sendEmail(String to, String subject, String body) {
        if (shouldFail) {
            return false;
        }
        
        sentEmails.add(new Email(to, subject, body));
        System.out.println("Mock: Email sent to " + to);
        return true;
    }
    
    @Override
    public int getEmailsSentToday() {
        return sentEmails.size();
    }
    
    // Test helper methods
    public void setShouldFail(boolean shouldFail) {
        this.shouldFail = shouldFail;
    }
    
    public List<Email> getSentEmails() {
        return new ArrayList<>(sentEmails);
    }
    
    public void clear() {
        sentEmails.clear();
    }
    
    public Email getLastSentEmail() {
        return sentEmails.isEmpty() ? null : 
               sentEmails.get(sentEmails.size() - 1);
    }
}

// Test class
public class UserServiceTest {
    private MockEmailService mockEmailService;
    private UserService userService;
    
    @Before
    public void setUp() {
        mockEmailService = new MockEmailService();
        userService = new UserService(mockEmailService);
    }
    
    @Test
    public void testUserRegistration() {
        // Test successful registration
        boolean result = userService.registerUser("john@example.com", "John");
        
        assertTrue(result);
        assertEquals(1, mockEmailService.getEmailsSentToday());
        
        Email sentEmail = mockEmailService.getLastSentEmail();
        assertEquals("john@example.com", sentEmail.getTo());
        assertTrue(sentEmail.getSubject().contains("Welcome"));
    }
    
    @Test
    public void testRegistrationWithEmailFailure() {
        mockEmailService.setShouldFail(true);
        
        boolean result = userService.registerUser("john@example.com", "John");
        
        // Should handle email failure gracefully
        assertTrue(result); // User still registered
        assertEquals(0, mockEmailService.getSentEmails().size());
    }
}
```

</div>

<div>

## Interface Contract Testing
```java
// Contract test for all PaymentProcessor implementations
public abstract class PaymentProcessorContractTest {
    protected abstract PaymentProcessor createPaymentProcessor();
    
    @Test
    public void testValidPayment() {
        PaymentProcessor processor = createPaymentProcessor();
        PaymentResult result = processor.processPayment(
            new PaymentRequest("1234567890123456", 100.00, "USD"));
        
        assertNotNull(result);
        // All implementations should handle valid payments
    }
    
    @Test
    public void testInvalidAmount() {
        PaymentProcessor processor = createPaymentProcessor();
        
        assertThrows(IllegalArgumentException.class, () -> {
            processor.processPayment(
                new PaymentRequest("1234567890123456", -10.00, "USD"));
        });
    }
    
    @Test
    public void testNullRequest() {
        PaymentProcessor processor = createPaymentProcessor();
        
        assertThrows(IllegalArgumentException.class, () -> {
            processor.processPayment(null);
        });
    }
}

// Specific implementation tests
public class CreditCardProcessorTest extends PaymentProcessorContractTest {
    @Override
    protected PaymentProcessor createPaymentProcessor() {
        return new CreditCardProcessor();
    }
    
    @Test
    public void testCreditCardSpecificFeatures() {
        CreditCardProcessor processor = new CreditCardProcessor();
        // Test credit card specific functionality
    }
}

public class PayPalProcessorTest extends PaymentProcessorContractTest {
    @Override
    protected PaymentProcessor createPaymentProcessor() {
        return new PayPalProcessor();
    }
    
    @Test
    public void testPayPalSpecificFeatures() {
        PayPalProcessor processor = new PayPalProcessor();
        // Test PayPal specific functionality
    }
}
```

## Integration Testing with Interfaces
```java
// Integration test with multiple interface implementations
@TestMethodOrder(OrderAnnotation.class)
public class ECommerceIntegrationTest {
    private PaymentProcessor paymentProcessor;
    private OrderService orderService;
    private EmailService emailService;
    
    @BeforeEach
    public void setUp() {
        // Use real implementations for integration test
        paymentProcessor = new CreditCardProcessor();
        emailService = new SMTPEmailService();
        orderService = new OrderService(paymentProcessor, emailService);
    }
    
    @Test
    @Order(1)
    public void testCompleteOrderFlow() {
        Order order = new Order("ORD-001", 299.99, "user@example.com");
        
        OrderResult result = orderService.processOrder(order);
        
        assertTrue(result.isSuccess());
        assertEquals("ORD-001", result.getOrderId());
    }
    
    @Test
    @Order(2)
    public void testOrderWithPaymentFailure() {
        // Create order with invalid payment details
        Order order = new Order("ORD-002", -100.00, "user@example.com");
        
        OrderResult result = orderService.processOrder(order);
        
        assertFalse(result.isSuccess());
        assertNotNull(result.getErrorMessage());
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

- 🔧 **Multiple Implementation**: Implementing multiple interfaces in single classes
- ⚔️ **Conflict Resolution**: Resolving default method conflicts explicitly
- 🏗️ **Interface Hierarchies**: Creating and using interface inheritance chains
- 🎯 **Composition Patterns**: Using delegation and composition with interfaces
- ⚡ **Advanced Patterns**: Adapter, Proxy, Chain of Responsibility, Command patterns
- 📝 **Best Practices**: Design guidelines and testing strategies
- 🛠️ **Real Applications**: Plugin systems, smart home, media processing

</v-clicks>

</div>

<div>

## Implementation Strategies

### Multiple Interface Benefits
- **Behavioral Composition**: Combine different capabilities
- **Flexible Design**: Easy to extend and modify
- **Polymorphic Usage**: Multiple interface views
- **Testing**: Mock implementations and contract testing

### Resolution Strategies
```java
// Explicit resolution of conflicts
@Override
public void conflictingMethod() {
    InterfaceA.super.conflictingMethod();
    InterfaceB.super.conflictingMethod();
    // Custom logic
}
```

## Best Practices Recap

<v-clicks>

- Keep interfaces focused and cohesive
- Use composition over complex inheritance
- Resolve method conflicts explicitly
- Document interface contracts clearly
- Test interface implementations thoroughly
- Use appropriate design patterns
- Consider performance implications
- Plan for interface evolution

</v-clicks>

## Next Lecture Preview
**Lecture 25: Polymorphism**
- Runtime polymorphism concepts
- Method dispatch and binding
- Polymorphic behavior patterns
- Advanced polymorphism applications

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!

## Questions and Discussion

**Next Lecture**: Polymorphism  
**Topic**: Runtime polymorphism, method dispatch, polymorphic behavior

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Master interface implementation patterns! <carbon:arrow-right class="inline"/>
  </span>
</div>