---
theme: default
background: https://source.unsplash.com/1024x768/?custom,design
title: Custom Exceptions
info: |
  ## Java Programming (4343203)
  
  Lecture 29: Custom Exceptions
  
  Diploma in ICT - Semester IV
  Gujarat Technological University

  Learn about creating custom exceptions, exception hierarchy design, best practices, and building domain-specific exception handling systems.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Custom Exceptions
## Lecture 29

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

- 🏗️ **Create** custom exception classes with proper inheritance
- 🎯 **Design** meaningful exception hierarchies for applications
- 📋 **Implement** both checked and unchecked custom exceptions
- ⚡ **Apply** best practices for exception class design
- 🔧 **Build** domain-specific exception handling systems
- 🎭 **Use** custom exceptions for business logic validation
- 💡 **Understand** when to create custom vs use built-in exceptions

</v-clicks>

---
layout: default
---

# Why Create Custom Exceptions?

<div class="grid grid-cols-2 gap-6">

<div>

## Built-in Exceptions vs Custom Exceptions

### Built-in Exceptions
```java
// Using generic built-in exceptions
public class BankAccount {
    private double balance;
    
    public void withdraw(double amount) {
        if (amount <= 0) {
            // Generic exception - not very descriptive
            throw new IllegalArgumentException("Invalid amount");
        }
        
        if (amount > balance) {
            // Generic exception - doesn't convey business meaning
            throw new RuntimeException("Not enough money");
        }
        
        balance -= amount;
    }
}

// Problems with generic exceptions:
// 1. Not descriptive of business domain
// 2. Hard to handle different error types specifically
// 3. No additional context or data
// 4. Generic error messages
```

### Custom Exceptions
```java
// Using custom business-specific exceptions
public class BankAccount {
    private double balance;
    
    public void withdraw(double amount) throws WithdrawalException {
        if (amount <= 0) {
            // Specific exception with business context
            throw new InvalidAmountException(
                "Withdrawal amount must be positive: " + amount);
        }
        
        if (amount > balance) {
            // Business-specific exception with detailed info
            throw new InsufficientFundsException(
                "Cannot withdraw " + amount + ", available balance: " + balance,
                amount, balance);
        }
        
        balance -= amount;
    }
}

// Benefits of custom exceptions:
// 1. Clear business domain meaning
// 2. Specific handling for different scenarios  
// 3. Additional context and data
// 4. Better error reporting and debugging
```

</div>

<div>

## When to Create Custom Exceptions

### ✅ **Create Custom Exceptions When:**

<v-clicks>

- **Business Domain Specificity**: Exception represents a specific business rule violation
- **Additional Context**: Need to include domain-specific data with the exception
- **Specific Handling**: Different error scenarios need different handling logic  
- **Better Documentation**: Exception name clearly conveys what went wrong
- **Error Recovery**: Need specific information to potentially recover from error

</v-clicks>

### ❌ **Don't Create Custom Exceptions When:**

<v-clicks>

- **Generic Errors**: Standard Java exceptions already cover the scenario well
- **Simple Cases**: No additional context or specific handling needed
- **Over-Engineering**: Creating too many similar exceptions without clear benefit
- **Maintenance Overhead**: Custom exceptions add complexity without value

</v-clicks>

## Custom Exception Benefits

### For Developers
- **Clear Intent**: Exception names explain what went wrong
- **Easier Debugging**: Specific exceptions point to exact problems
- **Better Testing**: Can test for specific exception types
- **Maintainability**: Changes localized to specific exception types

### For Applications  
- **Precise Error Handling**: Different exceptions = different recovery strategies
- **Better User Experience**: Domain-specific error messages
- **Monitoring & Logging**: Can track specific error patterns
- **API Design**: Clear exception contracts for method consumers

### Real-world Example
```java
// E-commerce order processing
try {
    orderService.processOrder(order);
} catch (InvalidCustomerException e) {
    // Redirect to customer registration
    redirectToRegistration();
} catch (InsufficientInventoryException e) {
    // Show alternative products
    showAlternatives(e.getUnavailableItems());
} catch (PaymentDeclinedException e) {
    // Ask for different payment method
    requestDifferentPayment(e.getDeclineReason());
} catch (ShippingUnavailableException e) {
    // Offer different shipping options
    showShippingOptions(e.getAvailableOptions());
}
```

</div>

</div>

---
layout: default
---

# Creating Basic Custom Exceptions

<div class="grid grid-cols-2 gap-6">

<div>

## Simple Custom Exception
```java
// Basic custom exception class
public class AccountException extends Exception {
    
    // Default constructor
    public AccountException() {
        super();
    }
    
    // Constructor with message
    public AccountException(String message) {
        super(message);
    }
    
    // Constructor with message and cause
    public AccountException(String message, Throwable cause) {
        super(message, cause);
    }
    
    // Constructor with cause only
    public AccountException(Throwable cause) {
        super(cause);
    }
}

// Usage example
public class BankAccount {
    private String accountNumber;
    private double balance;
    
    public void withdraw(double amount) throws AccountException {
        if (amount <= 0) {
            throw new AccountException("Withdrawal amount must be positive");
        }
        
        if (amount > balance) {
            throw new AccountException(
                "Insufficient funds: requested=" + amount + ", available=" + balance);
        }
        
        balance -= amount;
        System.out.println("Withdrawal successful. New balance: " + balance);
    }
}
```

## Custom Unchecked Exception
```java
// Runtime exception - doesn't need to be declared
public class InvalidConfigurationException extends RuntimeException {
    
    public InvalidConfigurationException() {
        super();
    }
    
    public InvalidConfigurationException(String message) {
        super(message);
    }
    
    public InvalidConfigurationException(String message, Throwable cause) {
        super(message, cause);
    }
    
    public InvalidConfigurationException(Throwable cause) {
        super(cause);
    }
}

// Usage - no need to declare in throws clause
public class ConfigurationManager {
    public void loadConfiguration(String filename) {
        if (filename == null || filename.isEmpty()) {
            // Runtime exception - optional to declare
            throw new InvalidConfigurationException(
                "Configuration filename cannot be null or empty");
        }
        
        try {
            // Load configuration logic
            Properties props = new Properties();
            props.load(new FileInputStream(filename));
            
            // Validate required properties
            if (!props.containsKey("database.url")) {
                throw new InvalidConfigurationException(
                    "Required property 'database.url' not found in " + filename);
            }
            
        } catch (IOException e) {
            throw new InvalidConfigurationException(
                "Failed to load configuration from " + filename, e);
        }
    }
}
```

</div>

<div>

## Custom Exception with Additional Data
```java
// Exception with additional context information
public class InsufficientFundsException extends Exception {
    private double requestedAmount;
    private double availableBalance;
    private String accountNumber;
    
    public InsufficientFundsException(double requestedAmount, 
                                     double availableBalance, 
                                     String accountNumber) {
        super("Insufficient funds: requested=" + requestedAmount + 
              ", available=" + availableBalance + 
              ", account=" + accountNumber);
        
        this.requestedAmount = requestedAmount;
        this.availableBalance = availableBalance;
        this.accountNumber = accountNumber;
    }
    
    // Getters for additional context
    public double getRequestedAmount() { 
        return requestedAmount; 
    }
    
    public double getAvailableBalance() { 
        return availableBalance; 
    }
    
    public String getAccountNumber() { 
        return accountNumber; 
    }
    
    public double getShortfall() {
        return requestedAmount - availableBalance;
    }
}

// Usage with specific error handling
public class ATMService {
    public void processWithdrawal(String accountNumber, double amount) {
        try {
            BankAccount account = getAccount(accountNumber);
            account.withdraw(amount);
            
        } catch (InsufficientFundsException e) {
            // Use additional exception data for specific handling
            System.err.println("Withdrawal failed:");
            System.err.println("  Account: " + e.getAccountNumber());
            System.err.println("  Requested: $" + e.getRequestedAmount());
            System.err.println("  Available: $" + e.getAvailableBalance());
            System.err.println("  Shortfall: $" + e.getShortfall());
            
            // Offer alternative options
            if (e.getShortfall() < 50) {
                System.out.println("Consider withdrawing $" + e.getAvailableBalance());
            }
        }
    }
}
```

## Exception with Validation Details
```java
// Exception for validation errors with detailed information
public class ValidationException extends Exception {
    private String fieldName;
    private Object invalidValue;
    private String validationRule;
    private List<String> validationErrors;
    
    // Single field validation error
    public ValidationException(String fieldName, Object invalidValue, 
                              String validationRule) {
        super("Validation failed for field '" + fieldName + "': " + validationRule);
        this.fieldName = fieldName;
        this.invalidValue = invalidValue;
        this.validationRule = validationRule;
        this.validationErrors = Arrays.asList(getMessage());
    }
    
    // Multiple validation errors
    public ValidationException(List<String> validationErrors) {
        super("Validation failed: " + String.join("; ", validationErrors));
        this.validationErrors = new ArrayList<>(validationErrors);
    }
    
    // Getters
    public String getFieldName() { return fieldName; }
    public Object getInvalidValue() { return invalidValue; }
    public String getValidationRule() { return validationRule; }
    public List<String> getValidationErrors() { return validationErrors; }
}
```

</div>

</div>

---
layout: default
---

# Exception Hierarchy Design

<div class="grid grid-cols-2 gap-6">

<div>

## Building Exception Hierarchies
A well-designed exception hierarchy allows for both specific and general exception handling:

```java
// Base application exception
public abstract class ApplicationException extends Exception {
    private String errorCode;
    private LocalDateTime timestamp;
    
    public ApplicationException(String message) {
        super(message);
        this.timestamp = LocalDateTime.now();
    }
    
    public ApplicationException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
        this.timestamp = LocalDateTime.now();
    }
    
    public ApplicationException(String message, Throwable cause) {
        super(message, cause);
        this.timestamp = LocalDateTime.now();
    }
    
    public String getErrorCode() { return errorCode; }
    public LocalDateTime getTimestamp() { return timestamp; }
}

// Business layer exceptions
public abstract class BusinessException extends ApplicationException {
    public BusinessException(String message) {
        super(message);
    }
    
    public BusinessException(String message, String errorCode) {
        super(message, errorCode);
    }
    
    public BusinessException(String message, Throwable cause) {
        super(message, cause);
    }
}

// System layer exceptions
public abstract class SystemException extends ApplicationException {
    public SystemException(String message) {
        super(message);
    }
    
    public SystemException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Specific business exceptions
public class UserNotFoundException extends BusinessException {
    private String userId;
    
    public UserNotFoundException(String userId) {
        super("User not found: " + userId, "USER_NOT_FOUND");
        this.userId = userId;
    }
    
    public String getUserId() { return userId; }
}

public class InvalidCredentialsException extends BusinessException {
    private String username;
    private int attemptCount;
    
    public InvalidCredentialsException(String username, int attemptCount) {
        super("Invalid credentials for user: " + username, "INVALID_CREDENTIALS");
        this.username = username;
        this.attemptCount = attemptCount;
    }
    
    public String getUsername() { return username; }
    public int getAttemptCount() { return attemptCount; }
}
```

</div>

<div>

## Hierarchical Exception Handling
```java
// System exceptions
public class DatabaseException extends SystemException {
    private String operation;
    private String tableName;
    
    public DatabaseException(String operation, String tableName, 
                           String message, Throwable cause) {
        super("Database operation failed: " + operation + 
              " on table " + tableName + " - " + message, cause);
        this.operation = operation;
        this.tableName = tableName;
    }
    
    public String getOperation() { return operation; }
    public String getTableName() { return tableName; }
}

public class NetworkException extends SystemException {
    private String host;
    private int port;
    
    public NetworkException(String host, int port, String message, Throwable cause) {
        super("Network error connecting to " + host + ":" + port + " - " + message, cause);
        this.host = host;
        this.port = port;
    }
    
    public String getHost() { return host; }
    public int getPort() { return port; }
}

// Service layer using hierarchical handling
public class UserService {
    public User authenticateUser(String username, String password) 
            throws BusinessException, SystemException {
        
        try {
            // Check if user exists
            User user = userRepository.findByUsername(username);
            if (user == null) {
                throw new UserNotFoundException(username);
            }
            
            // Validate password
            if (!passwordEncoder.matches(password, user.getHashedPassword())) {
                int attempts = getFailedAttempts(username) + 1;
                recordFailedAttempt(username, attempts);
                throw new InvalidCredentialsException(username, attempts);
            }
            
            // Clear failed attempts on success
            clearFailedAttempts(username);
            
            return user;
            
        } catch (BusinessException e) {
            // Re-throw business exceptions as-is
            throw e;
            
        } catch (DatabaseException e) {
            // Convert database exception to system exception
            throw new SystemException("Authentication service temporarily unavailable", e);
            
        } catch (Exception e) {
            // Convert unexpected exceptions
            throw new SystemException("Unexpected error during authentication", e);
        }
    }
}

// Controller layer with hierarchical exception handling
@RestController
public class AuthController {
    @PostMapping("/authenticate")
    public ResponseEntity<?> authenticate(@RequestBody LoginRequest request) {
        try {
            User user = userService.authenticateUser(request.getUsername(), request.getPassword());
            String token = jwtService.generateToken(user);
            return ResponseEntity.ok(new AuthResponse(token, user.getId()));
            
        } catch (UserNotFoundException e) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
                .body(new ErrorResponse(e.getErrorCode(), "Invalid username or password"));
                
        } catch (InvalidCredentialsException e) {
            ErrorResponse response = new ErrorResponse(e.getErrorCode(), "Invalid username or password");
            
            // Add lockout warning after multiple attempts
            if (e.getAttemptCount() >= 3) {
                response.setWarning("Account will be locked after 5 failed attempts");
            }
            
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(response);
            
        } catch (BusinessException e) {
            // Handle other business exceptions generically
            return ResponseEntity.badRequest()
                .body(new ErrorResponse(e.getErrorCode(), e.getMessage()));
                
        } catch (SystemException e) {
            // Log system exceptions for monitoring
            logger.error("System error during authentication", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(new ErrorResponse("SYSTEM_ERROR", "Service temporarily unavailable"));
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Domain-Specific Exception Design

<div class="grid grid-cols-2 gap-6">

<div>

## E-commerce Domain Exceptions
```java
// Base e-commerce exception
public abstract class EcommerceException extends Exception {
    private String orderId;
    private String customerId;
    
    public EcommerceException(String message) {
        super(message);
    }
    
    public EcommerceException(String message, String orderId, String customerId) {
        super(message);
        this.orderId = orderId;
        this.customerId = customerId;
    }
    
    public String getOrderId() { return orderId; }
    public String getCustomerId() { return customerId; }
}

// Inventory related exceptions
public class InsufficientInventoryException extends EcommerceException {
    private String productId;
    private int requestedQuantity;
    private int availableQuantity;
    
    public InsufficientInventoryException(String productId, 
                                        int requestedQuantity, 
                                        int availableQuantity) {
        super("Insufficient inventory for product " + productId + 
              ": requested=" + requestedQuantity + 
              ", available=" + availableQuantity);
        this.productId = productId;
        this.requestedQuantity = requestedQuantity;
        this.availableQuantity = availableQuantity;
    }
    
    public String getProductId() { return productId; }
    public int getRequestedQuantity() { return requestedQuantity; }
    public int getAvailableQuantity() { return availableQuantity; }
    public int getShortfall() { return requestedQuantity - availableQuantity; }
}

// Payment related exceptions
public abstract class PaymentException extends EcommerceException {
    private String transactionId;
    private BigDecimal amount;
    
    public PaymentException(String message, String transactionId, BigDecimal amount) {
        super(message);
        this.transactionId = transactionId;
        this.amount = amount;
    }
    
    public String getTransactionId() { return transactionId; }
    public BigDecimal getAmount() { return amount; }
}

public class PaymentDeclinedException extends PaymentException {
    private String declineReason;
    private String declineCode;
    
    public PaymentDeclinedException(String transactionId, BigDecimal amount,
                                  String declineReason, String declineCode) {
        super("Payment declined: " + declineReason, transactionId, amount);
        this.declineReason = declineReason;
        this.declineCode = declineCode;
    }
    
    public String getDeclineReason() { return declineReason; }
    public String getDeclineCode() { return declineCode; }
    
    public boolean isRetryable() {
        // Some decline codes indicate retryable errors
        return "INSUFFICIENT_FUNDS".equals(declineCode) || 
               "TEMPORARY_HOLD".equals(declineCode);
    }
}

public class PaymentTimeoutException extends PaymentException {
    private int timeoutSeconds;
    
    public PaymentTimeoutException(String transactionId, BigDecimal amount, int timeoutSeconds) {
        super("Payment timed out after " + timeoutSeconds + " seconds", transactionId, amount);
        this.timeoutSeconds = timeoutSeconds;
    }
    
    public int getTimeoutSeconds() { return timeoutSeconds; }
}
```

</div>

<div>

## Medical Domain Exceptions  
```java
// Base medical system exception
public abstract class MedicalException extends Exception {
    private String patientId;
    private String facilityId;
    private LocalDateTime occurredAt;
    
    public MedicalException(String message, String patientId, String facilityId) {
        super(message);
        this.patientId = patientId;
        this.facilityId = facilityId;
        this.occurredAt = LocalDateTime.now();
    }
    
    public String getPatientId() { return patientId; }
    public String getFacilityId() { return facilityId; }
    public LocalDateTime getOccurredAt() { return occurredAt; }
}

// Patient related exceptions
public class PatientNotFoundException extends MedicalException {
    public PatientNotFoundException(String patientId, String facilityId) {
        super("Patient not found: " + patientId, patientId, facilityId);
    }
}

public class PatientRecordLockedException extends MedicalException {
    private String lockedByUserId;
    private LocalDateTime lockedSince;
    
    public PatientRecordLockedException(String patientId, String facilityId,
                                      String lockedByUserId, LocalDateTime lockedSince) {
        super("Patient record is currently locked by another user", patientId, facilityId);
        this.lockedByUserId = lockedByUserId;
        this.lockedSince = lockedSince;
    }
    
    public String getLockedByUserId() { return lockedByUserId; }
    public LocalDateTime getLockedSince() { return lockedSince; }
}

// Prescription related exceptions
public class DrugInteractionException extends MedicalException {
    private String drugId1;
    private String drugId2;
    private String interactionType;
    private String severity;
    
    public DrugInteractionException(String patientId, String facilityId,
                                  String drugId1, String drugId2,
                                  String interactionType, String severity) {
        super("Drug interaction detected: " + drugId1 + " and " + drugId2 +
              " - " + interactionType + " (Severity: " + severity + ")",
              patientId, facilityId);
        this.drugId1 = drugId1;
        this.drugId2 = drugId2;
        this.interactionType = interactionType;
        this.severity = severity;
    }
    
    public String getDrugId1() { return drugId1; }
    public String getDrugId2() { return drugId2; }
    public String getInteractionType() { return interactionType; }
    public String getSeverity() { return severity; }
    
    public boolean isCritical() {
        return "CRITICAL".equalsIgnoreCase(severity) || "SEVERE".equalsIgnoreCase(severity);
    }
}

public class AllergicReactionException extends MedicalException {
    private String allergen;
    private String reactionType;
    private List<String> symptoms;
    
    public AllergicReactionException(String patientId, String facilityId,
                                   String allergen, String reactionType,
                                   List<String> symptoms) {
        super("Allergic reaction alert: Patient allergic to " + allergen +
              " - Reaction type: " + reactionType,
              patientId, facilityId);
        this.allergen = allergen;
        this.reactionType = reactionType;
        this.symptoms = new ArrayList<>(symptoms);
    }
    
    public String getAllergen() { return allergen; }
    public String getReactionType() { return reactionType; }
    public List<String> getSymptoms() { return symptoms; }
}

// Usage in medical service
@Service
public class PrescriptionService {
    public void prescribeMedication(String patientId, String drugId, String dosage)
            throws MedicalException {
        
        try {
            // Get patient info
            Patient patient = patientRepository.findById(patientId);
            if (patient == null) {
                throw new PatientNotFoundException(patientId, getCurrentFacilityId());
            }
            
            // Check for allergies
            List<String> allergies = patient.getAllergies();
            Drug drug = drugRepository.findById(drugId);
            
            if (allergies.contains(drug.getActiveIngredient())) {
                throw new AllergicReactionException(
                    patientId, getCurrentFacilityId(),
                    drug.getActiveIngredient(), "MEDICATION",
                    Arrays.asList("Potential allergic reaction to prescribed medication"));
            }
            
            // Check for drug interactions
            List<String> currentMedications = getCurrentMedications(patientId);
            for (String currentDrug : currentMedications) {
                DrugInteraction interaction = checkInteraction(drugId, currentDrug);
                if (interaction != null && interaction.getSeverity().equals("CRITICAL")) {
                    throw new DrugInteractionException(
                        patientId, getCurrentFacilityId(),
                        drugId, currentDrug,
                        interaction.getType(), interaction.getSeverity());
                }
            }
            
            // Create prescription
            Prescription prescription = new Prescription(patientId, drugId, dosage);
            prescriptionRepository.save(prescription);
            
        } catch (MedicalException e) {
            // Log medical exceptions for compliance tracking
            medicalAuditLogger.logMedicalException(e);
            throw e;
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Exception Chaining and Context

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Chaining with Context
```java
// Data access layer exception with context
public class DataAccessException extends Exception {
    private String operation;
    private String entity;
    private Map<String, Object> parameters;
    
    public DataAccessException(String operation, String entity, 
                              String message, Throwable cause) {
        super("Data access failed: " + operation + " on " + entity + " - " + message, cause);
        this.operation = operation;
        this.entity = entity;
        this.parameters = new HashMap<>();
    }
    
    public DataAccessException addParameter(String key, Object value) {
        parameters.put(key, value);
        return this;
    }
    
    public String getOperation() { return operation; }
    public String getEntity() { return entity; }
    public Map<String, Object> getParameters() { return parameters; }
}

// Service layer exception that chains data access exceptions
public class OrderProcessingException extends Exception {
    private String orderId;
    private String processingStage;
    private Map<String, Object> orderContext;
    
    public OrderProcessingException(String orderId, String processingStage, 
                                  String message, Throwable cause) {
        super("Order processing failed at stage '" + processingStage + 
              "' for order " + orderId + ": " + message, cause);
        this.orderId = orderId;
        this.processingStage = processingStage;
        this.orderContext = new HashMap<>();
    }
    
    public OrderProcessingException addContext(String key, Object value) {
        orderContext.put(key, value);
        return this;
    }
    
    public String getOrderId() { return orderId; }
    public String getProcessingStage() { return processingStage; }
    public Map<String, Object> getOrderContext() { return orderContext; }
    
    // Method to get the full exception chain
    public List<Throwable> getExceptionChain() {
        List<Throwable> chain = new ArrayList<>();
        Throwable current = this;
        while (current != null) {
            chain.add(current);
            current = current.getCause();
        }
        return chain;
    }
}

// Repository implementation with exception chaining
@Repository
public class OrderRepository {
    public Order saveOrder(Order order) throws DataAccessException {
        try {
            // Database save operation
            return entityManager.merge(order);
            
        } catch (PersistenceException e) {
            throw new DataAccessException("INSERT", "Order", 
                "Failed to save order to database", e)
                .addParameter("orderId", order.getId())
                .addParameter("customerId", order.getCustomerId())
                .addParameter("totalAmount", order.getTotalAmount());
                
        } catch (Exception e) {
            throw new DataAccessException("INSERT", "Order",
                "Unexpected error during order save", e)
                .addParameter("orderId", order.getId());
        }
    }
}
```

</div>

<div>

## Context-Aware Exception Handling
```java
// Service that chains exceptions with context
@Service
public class OrderService {
    
    public void processOrder(Order order) throws OrderProcessingException {
        String orderId = order.getId();
        
        try {
            // Stage 1: Validate order
            validateOrder(order);
            
            // Stage 2: Reserve inventory
            reserveInventory(order);
            
            // Stage 3: Process payment
            processPayment(order);
            
            // Stage 4: Save order
            Order savedOrder = orderRepository.saveOrder(order);
            
            // Stage 5: Send confirmation
            sendOrderConfirmation(savedOrder);
            
        } catch (ValidationException e) {
            throw new OrderProcessingException(orderId, "VALIDATION",
                "Order validation failed", e)
                .addContext("customerId", order.getCustomerId())
                .addContext("itemCount", order.getItems().size());
                
        } catch (InventoryException e) {
            throw new OrderProcessingException(orderId, "INVENTORY",
                "Inventory reservation failed", e)
                .addContext("unavailableItems", e.getUnavailableItems());
                
        } catch (PaymentException e) {
            throw new OrderProcessingException(orderId, "PAYMENT",
                "Payment processing failed", e)
                .addContext("paymentMethod", order.getPaymentMethod())
                .addContext("amount", order.getTotalAmount());
                
        } catch (DataAccessException e) {
            throw new OrderProcessingException(orderId, "PERSISTENCE",
                "Order save failed", e)
                .addContext("operation", e.getOperation())
                .addContext("entity", e.getEntity());
                
        } catch (Exception e) {
            throw new OrderProcessingException(orderId, "UNKNOWN",
                "Unexpected error during order processing", e);
        }
    }
}

// Controller with comprehensive exception handling
@RestController
public class OrderController {
    
    @PostMapping("/orders")
    public ResponseEntity<?> createOrder(@RequestBody Order order) {
        try {
            orderService.processOrder(order);
            return ResponseEntity.ok("Order processed successfully");
            
        } catch (OrderProcessingException e) {
            // Log the full exception chain for debugging
            logExceptionChain(e);
            
            // Return user-friendly error based on processing stage
            return handleOrderProcessingError(e);
        }
    }
    
    private ResponseEntity<?> handleOrderProcessingError(OrderProcessingException e) {
        ErrorResponse response = new ErrorResponse();
        
        switch (e.getProcessingStage()) {
            case "VALIDATION":
                response.setCode("VALIDATION_ERROR");
                response.setMessage("Please check your order details");
                response.setUserMessage("There was an issue with your order. Please review and try again.");
                break;
                
            case "INVENTORY":
                response.setCode("INVENTORY_ERROR");
                response.setMessage("Some items are no longer available");
                response.setUserMessage("Sorry, some items in your cart are out of stock.");
                // Add available alternatives from context
                break;
                
            case "PAYMENT":
                response.setCode("PAYMENT_ERROR");
                response.setMessage("Payment could not be processed");
                response.setUserMessage("There was an issue processing your payment. Please try a different payment method.");
                break;
                
            case "PERSISTENCE":
                response.setCode("SYSTEM_ERROR");
                response.setMessage("Order could not be saved");
                response.setUserMessage("We're experiencing technical difficulties. Please try again in a few moments.");
                break;
                
            default:
                response.setCode("UNKNOWN_ERROR");
                response.setMessage("An unexpected error occurred");
                response.setUserMessage("Something went wrong. Our team has been notified.");
        }
        
        response.setOrderId(e.getOrderId());
        response.setTimestamp(LocalDateTime.now());
        
        return ResponseEntity.badRequest().body(response);
    }
    
    private void logExceptionChain(OrderProcessingException e) {
        logger.error("Order processing failed for order: {}", e.getOrderId());
        
        List<Throwable> chain = e.getExceptionChain();
        for (int i = 0; i < chain.size(); i++) {
            Throwable exception = chain.get(i);
            logger.error("  Exception level {}: {} - {}", 
                        i, exception.getClass().getSimpleName(), exception.getMessage());
        }
        
        // Log context information
        logger.error("Order context: {}", e.getOrderContext());
        logger.error("Processing stage: {}", e.getProcessingStage());
    }
}
```

</div>

</div>

---
layout: default
---

# Advanced Exception Features

<div class="grid grid-cols-2 gap-6">

<div>

## Exceptions with Recovery Information
```java
// Exception that provides recovery options
public class ServiceUnavailableException extends Exception {
    private String serviceName;
    private LocalDateTime estimatedRecoveryTime;
    private List<String> alternativeServices;
    private String fallbackUrl;
    
    public ServiceUnavailableException(String serviceName, 
                                     LocalDateTime estimatedRecoveryTime,
                                     List<String> alternativeServices) {
        super("Service unavailable: " + serviceName + 
              ". Estimated recovery: " + estimatedRecoveryTime);
        this.serviceName = serviceName;
        this.estimatedRecoveryTime = estimatedRecoveryTime;
        this.alternativeServices = new ArrayList<>(alternativeServices);
    }
    
    public String getServiceName() { return serviceName; }
    public LocalDateTime getEstimatedRecoveryTime() { return estimatedRecoveryTime; }
    public List<String> getAlternativeServices() { return alternativeServices; }
    public String getFallbackUrl() { return fallbackUrl; }
    
    public boolean hasAlternatives() {
        return alternativeServices != null && !alternativeServices.isEmpty();
    }
    
    public Duration getEstimatedDowntime() {
        return Duration.between(LocalDateTime.now(), estimatedRecoveryTime);
    }
}

// Exception with retry information
public class TemporaryFailureException extends Exception {
    private int maxRetries;
    private Duration retryDelay;
    private String retryStrategy;
    
    public TemporaryFailureException(String message, int maxRetries, 
                                   Duration retryDelay, String retryStrategy) {
        super(message + " (Retryable: " + maxRetries + " attempts)");
        this.maxRetries = maxRetries;
        this.retryDelay = retryDelay;
        this.retryStrategy = retryStrategy;
    }
    
    public int getMaxRetries() { return maxRetries; }
    public Duration getRetryDelay() { return retryDelay; }
    public String getRetryStrategy() { return retryStrategy; }
    
    public boolean shouldRetry(int currentAttempt) {
        return currentAttempt < maxRetries;
    }
    
    public Duration getDelayForAttempt(int attempt) {
        switch (retryStrategy.toLowerCase()) {
            case "exponential":
                return retryDelay.multipliedBy((long) Math.pow(2, attempt));
            case "linear":
                return retryDelay.multipliedBy(attempt + 1);
            default:
                return retryDelay;
        }
    }
}

// Service with automatic retry logic
@Service
public class ExternalApiService {
    
    public String callExternalService(String endpoint) 
            throws ServiceUnavailableException, TemporaryFailureException {
        
        int attempts = 0;
        TemporaryFailureException lastException = null;
        
        while (attempts < 3) {
            try {
                return performApiCall(endpoint);
                
            } catch (ConnectException e) {
                lastException = new TemporaryFailureException(
                    "Connection failed to " + endpoint,
                    3, Duration.ofSeconds(2), "exponential");
                    
                if (lastException.shouldRetry(attempts)) {
                    try {
                        Thread.sleep(lastException.getDelayForAttempt(attempts).toMillis());
                    } catch (InterruptedException ie) {
                        Thread.currentThread().interrupt();
                        break;
                    }
                    attempts++;
                } else {
                    break;
                }
                
            } catch (ServiceMaintenanceException e) {
                throw new ServiceUnavailableException(
                    "External API", e.getMaintenanceEnd(),
                    Arrays.asList("backup-api.example.com", "cached-service"));
            }
        }
        
        throw lastException;
    }
}
```

</div>

<div>

## Internationalized Exception Messages
```java
// Exception with internationalization support
public class LocalizedValidationException extends Exception {
    private String messageKey;
    private Object[] messageParameters;
    private Locale locale;
    
    public LocalizedValidationException(String messageKey, Locale locale, Object... parameters) {
        super(getLocalizedMessage(messageKey, locale, parameters));
        this.messageKey = messageKey;
        this.locale = locale;
        this.messageParameters = parameters;
    }
    
    public String getMessageKey() { return messageKey; }
    public Object[] getMessageParameters() { return messageParameters; }
    public Locale getLocale() { return locale; }
    
    public String getLocalizedMessage(Locale targetLocale) {
        return getLocalizedMessage(messageKey, targetLocale, messageParameters);
    }
    
    private static String getLocalizedMessage(String key, Locale locale, Object[] params) {
        try {
            ResourceBundle bundle = ResourceBundle.getBundle("messages", locale);
            String pattern = bundle.getString(key);
            return MessageFormat.format(pattern, params);
        } catch (MissingResourceException e) {
            return key + ": " + Arrays.toString(params);
        }
    }
}

// Exception with contextual help
public class ValidationExceptionWithHelp extends Exception {
    private String fieldName;
    private Object invalidValue;
    private String helpText;
    private String documentationUrl;
    private List<String> suggestedValues;
    
    public ValidationExceptionWithHelp(String fieldName, Object invalidValue, 
                                      String message, String helpText) {
        super(message);
        this.fieldName = fieldName;
        this.invalidValue = invalidValue;
        this.helpText = helpText;
        this.suggestedValues = new ArrayList<>();
    }
    
    public ValidationExceptionWithHelp withDocumentationUrl(String url) {
        this.documentationUrl = url;
        return this;
    }
    
    public ValidationExceptionWithHelp withSuggestedValues(List<String> values) {
        this.suggestedValues = new ArrayList<>(values);
        return this;
    }
    
    // Getters
    public String getFieldName() { return fieldName; }
    public Object getInvalidValue() { return invalidValue; }
    public String getHelpText() { return helpText; }
    public String getDocumentationUrl() { return documentationUrl; }
    public List<String> getSuggestedValues() { return suggestedValues; }
    
    public String getDetailedHelp() {
        StringBuilder help = new StringBuilder();
        help.append("Field: ").append(fieldName).append("\n");
        help.append("Invalid value: ").append(invalidValue).append("\n");
        help.append("Error: ").append(getMessage()).append("\n");
        
        if (helpText != null) {
            help.append("Help: ").append(helpText).append("\n");
        }
        
        if (!suggestedValues.isEmpty()) {
            help.append("Suggested values: ").append(String.join(", ", suggestedValues)).append("\n");
        }
        
        if (documentationUrl != null) {
            help.append("Documentation: ").append(documentationUrl).append("\n");
        }
        
        return help.toString();
    }
}

// Usage in validation service
@Service
public class ValidationService {
    
    public void validateCountryCode(String countryCode) throws ValidationExceptionWithHelp {
        if (countryCode == null || countryCode.trim().isEmpty()) {
            throw new ValidationExceptionWithHelp(
                "countryCode", countryCode,
                "Country code cannot be empty",
                "Country code must be a valid ISO 3166-1 alpha-2 code (2 letters)"
            ).withSuggestedValues(Arrays.asList("US", "CA", "GB", "DE", "FR"))
             .withDocumentationUrl("https://api.example.com/docs/country-codes");
        }
        
        if (countryCode.length() != 2) {
            throw new ValidationExceptionWithHelp(
                "countryCode", countryCode,
                "Country code must be exactly 2 characters long",
                "Use the ISO 3166-1 alpha-2 standard for country codes"
            ).withSuggestedValues(getValidCountryCodes())
             .withDocumentationUrl("https://api.example.com/docs/country-codes");
        }
        
        if (!isValidCountryCode(countryCode)) {
            List<String> similar = findSimilarCountryCodes(countryCode);
            throw new ValidationExceptionWithHelp(
                "countryCode", countryCode,
                "Invalid country code: " + countryCode,
                "Country code not found in ISO 3166-1 alpha-2 standard"
            ).withSuggestedValues(similar)
             .withDocumentationUrl("https://api.example.com/docs/country-codes");
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 1: Library Management System

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Build Library Exception System
Create a comprehensive exception hierarchy for a library management system:

```java
// TODO: Design base exception hierarchy
public abstract class LibraryException extends Exception {
    // Add common fields: library branch, timestamp, operation
    // Add constructors with proper chaining
    // Add utility methods for logging and reporting
}

// TODO: Create domain-specific exceptions
public class BookException extends LibraryException {
    // Book-related exceptions
}

public class MemberException extends LibraryException {
    // Member-related exceptions
}

public class TransactionException extends LibraryException {
    // Borrowing/returning transaction exceptions
}

// TODO: Create specific exception types
public class BookNotFoundException extends BookException {
    private String isbn;
    private String title;
    // Add methods to suggest similar books
}

public class BookAlreadyBorrowedException extends BookException {
    private String borrowerId;
    private LocalDate borrowDate;
    private LocalDate dueDate;
    // Add method to check if overdue
}

public class MemberSuspendedException extends MemberException {
    private String suspensionReason;
    private LocalDate suspensionStart;
    private LocalDate suspensionEnd;
    private List<String> reinstatementRequirements;
    // Add method to check if suspension is active
}

public class OverdueBooksException extends TransactionException {
    private List<OverdueBook> overdueBooks;
    private BigDecimal totalFines;
    // Add methods to calculate penalties
}

// TODO: Create supporting classes
public class OverdueBook {
    private String isbn;
    private String title;
    private LocalDate dueDate;
    private int daysOverdue;
    private BigDecimal fineAmount;
}

// TODO: Implement library service with exception handling
public class LibraryService {
    public void borrowBook(String memberId, String isbn) throws LibraryException;
    public void returnBook(String memberId, String isbn) throws LibraryException;
    public void renewBook(String memberId, String isbn) throws LibraryException;
    public void addMember(Member member) throws LibraryException;
    public void suspendMember(String memberId, String reason) throws LibraryException;
}
```

**Requirements:**
- Create meaningful exception hierarchy
- Include domain-specific context in exceptions
- Provide recovery information where possible
- Support different handling strategies for different exception types
- Include validation with helpful error messages

</div>

<div>

## Solution Framework

```java
// Base library exception
public abstract class LibraryException extends Exception {
    private String libraryBranch;
    private LocalDateTime timestamp;
    private String operation;
    private String userId;
    
    public LibraryException(String message, String operation, String libraryBranch) {
        super(message);
        this.operation = operation;
        this.libraryBranch = libraryBranch;
        this.timestamp = LocalDateTime.now();
    }
    
    public LibraryException(String message, String operation, String libraryBranch, Throwable cause) {
        super(message, cause);
        this.operation = operation;
        this.libraryBranch = libraryBranch;
        this.timestamp = LocalDateTime.now();
    }
    
    // Getters and utility methods
    public String getLibraryBranch() { return libraryBranch; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public String getOperation() { return operation; }
    public String getUserId() { return userId; }
    
    public LibraryException setUserId(String userId) {
        this.userId = userId;
        return this;
    }
}

// Specific exception implementations
public class BookNotFoundException extends BookException {
    private String isbn;
    private String searchTerm;
    private List<Book> suggestedBooks;
    
    public BookNotFoundException(String isbn, String libraryBranch) {
        super("Book not found: " + isbn, "SEARCH", libraryBranch);
        this.isbn = isbn;
        this.suggestedBooks = new ArrayList<>();
    }
    
    public BookNotFoundException withSearchTerm(String searchTerm) {
        this.searchTerm = searchTerm;
        return this;
    }
    
    public BookNotFoundException withSuggestions(List<Book> suggestions) {
        this.suggestedBooks = new ArrayList<>(suggestions);
        return this;
    }
    
    public String getIsbn() { return isbn; }
    public String getSearchTerm() { return searchTerm; }
    public List<Book> getSuggestedBooks() { return suggestedBooks; }
    
    public boolean hasSuggestions() {
        return suggestedBooks != null && !suggestedBooks.isEmpty();
    }
}

public class MemberSuspendedException extends MemberException {
    private String memberId;
    private String suspensionReason;
    private LocalDate suspensionStart;
    private LocalDate suspensionEnd;
    private List<String> reinstatementRequirements;
    
    public MemberSuspendedException(String memberId, String suspensionReason,
                                   LocalDate suspensionStart, LocalDate suspensionEnd,
                                   String libraryBranch) {
        super("Member suspended: " + memberId + " - " + suspensionReason, 
              "MEMBER_CHECK", libraryBranch);
        this.memberId = memberId;
        this.suspensionReason = suspensionReason;
        this.suspensionStart = suspensionStart;
        this.suspensionEnd = suspensionEnd;
        this.reinstatementRequirements = new ArrayList<>();
    }
    
    public boolean isCurrentlySuspended() {
        LocalDate now = LocalDate.now();
        return now.isAfter(suspensionStart) && now.isBefore(suspensionEnd);
    }
    
    public long getDaysRemaining() {
        return ChronoUnit.DAYS.between(LocalDate.now(), suspensionEnd);
    }
    
    // Getters...
    public String getMemberId() { return memberId; }
    public String getSuspensionReason() { return suspensionReason; }
    public List<String> getReinstatementRequirements() { return reinstatementRequirements; }
}

// Service implementation
@Service
public class LibraryService {
    
    public void borrowBook(String memberId, String isbn) throws LibraryException {
        try {
            // Check member status
            Member member = getMember(memberId);
            validateMemberStatus(member);
            
            // Check book availability
            Book book = getBook(isbn);
            validateBookAvailability(book);
            
            // Check borrowing limits
            validateBorrowingLimits(member);
            
            // Create borrowing record
            BorrowingTransaction transaction = createBorrowingTransaction(member, book);
            transactionRepository.save(transaction);
            
            // Update book status
            book.setStatus(BookStatus.BORROWED);
            bookRepository.save(book);
            
        } catch (MemberSuspendedException e) {
            // Add specific context for suspension
            throw e.setUserId(memberId);
            
        } catch (BookNotFoundException e) {
            // Add suggestions for alternative books
            List<Book> suggestions = findSimilarBooks(isbn);
            throw e.withSuggestions(suggestions).setUserId(memberId);
            
        } catch (Exception e) {
            throw new LibraryException("Book borrowing failed", "BORROW", getCurrentBranch(), e)
                .setUserId(memberId);
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Hands-on Exercise 2: Online Banking System

<div class="grid grid-cols-2 gap-6">

<div>

## Task: Design Banking Exception System  
Create a comprehensive exception hierarchy for online banking:

```java
// TODO: Create base banking exception hierarchy
public abstract class BankingException extends Exception {
    // Add: account number, transaction id, amount, timestamp
    // Add: error codes for different systems integration
    // Add: methods for compliance logging
}

// TODO: Account-related exceptions
public class AccountException extends BankingException {
    // Base for all account-related issues
}

public class AccountNotFoundException extends AccountException {
    // Include: search criteria used, suggested account numbers
}

public class AccountClosedException extends AccountException {
    // Include: closure date, reason, contact information for reopening
}

public class AccountFrozenException extends AccountException {
    // Include: freeze reason, who froze it, how to unfreeze
}

// TODO: Transaction-related exceptions
public class TransactionException extends BankingException {
    // Base for all transaction issues
}

public class InsufficientFundsException extends TransactionException {
    // Include: requested amount, available amount, overdraft options
}

public class DailyLimitExceededException extends TransactionException {
    // Include: current day total, limit amount, time until reset
}

public class InvalidTransactionException extends TransactionException {
    // Include: validation failures, corrective actions
}

// TODO: Security-related exceptions
public class SecurityException extends BankingException {
    // Base for security violations
}

public class AuthenticationFailedException extends SecurityException {
    // Include: attempt count, lockout information, recovery options
}

public class AuthorizationException extends SecurityException {
    // Include: required permissions, how to obtain access
}

// TODO: System-related exceptions
public class SystemException extends BankingException {
    // Include: affected services, estimated recovery time, alternatives
}

// TODO: Implement banking service
public class BankingService {
    public void transfer(String fromAccount, String toAccount, BigDecimal amount) 
            throws BankingException;
    
    public void withdraw(String accountNumber, BigDecimal amount) 
            throws BankingException;
    
    public void deposit(String accountNumber, BigDecimal amount) 
            throws BankingException;
    
    public AccountBalance getBalance(String accountNumber) 
            throws BankingException;
}
```

**Requirements:**
- Design for regulatory compliance (logging, audit trails)
- Include recovery and alternative action information
- Support multiple error languages/locales  
- Provide detailed context for fraud detection
- Handle both online and batch processing scenarios

</div>

<div>

## Solution Implementation

```java
// Base banking exception with compliance features
public abstract class BankingException extends Exception {
    private String accountNumber;
    private String transactionId;
    private BigDecimal amount;
    private LocalDateTime timestamp;
    private String errorCode;
    private String regulatoryCode;
    private Map<String, Object> auditData;
    
    public BankingException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
        this.timestamp = LocalDateTime.now();
        this.auditData = new HashMap<>();
        this.transactionId = generateTransactionId();
    }
    
    // Builder-style methods for adding context
    public BankingException withAccount(String accountNumber) {
        this.accountNumber = accountNumber;
        addAuditData("accountNumber", accountNumber);
        return this;
    }
    
    public BankingException withAmount(BigDecimal amount) {
        this.amount = amount;
        addAuditData("amount", amount);
        return this;
    }
    
    public BankingException withRegulatoryCode(String regulatoryCode) {
        this.regulatoryCode = regulatoryCode;
        return this;
    }
    
    public BankingException addAuditData(String key, Object value) {
        auditData.put(key, value);
        return this;
    }
    
    // Compliance logging
    public void logForCompliance() {
        ComplianceLogger.log(this);
    }
    
    // Getters...
    public String getTransactionId() { return transactionId; }
    public String getErrorCode() { return errorCode; }
    public Map<String, Object> getAuditData() { return auditData; }
}

// Specific banking exceptions
public class InsufficientFundsException extends TransactionException {
    private BigDecimal requestedAmount;
    private BigDecimal availableBalance;
    private BigDecimal overdraftLimit;
    private List<OverdraftOption> overdraftOptions;
    
    public InsufficientFundsException(BigDecimal requested, BigDecimal available, BigDecimal overdraftLimit) {
        super("Insufficient funds: requested=" + requested + ", available=" + available, "INSUFFICIENT_FUNDS");
        this.requestedAmount = requested;
        this.availableBalance = available;
        this.overdraftLimit = overdraftLimit;
        this.overdraftOptions = new ArrayList<>();
    }
    
    public InsufficientFundsException withOverdraftOptions(List<OverdraftOption> options) {
        this.overdraftOptions = new ArrayList<>(options);
        return this;
    }
    
    public BigDecimal getShortfall() {
        return requestedAmount.subtract(availableBalance);
    }
    
    public boolean hasOverdraftAvailable() {
        return overdraftLimit != null && 
               availableBalance.add(overdraftLimit).compareTo(requestedAmount) >= 0;
    }
    
    public BigDecimal getMaximumWithdrawal() {
        return availableBalance.add(overdraftLimit != null ? overdraftLimit : BigDecimal.ZERO);
    }
    
    // Getters...
}

public class AuthenticationFailedException extends SecurityException {
    private String username;
    private int attemptCount;
    private int maxAttempts;
    private Duration lockoutDuration;
    private LocalDateTime lockoutUntil;
    private List<String> recoveryOptions;
    
    public AuthenticationFailedException(String username, int attemptCount, int maxAttempts) {
        super("Authentication failed for user: " + username, "AUTH_FAILED");
        this.username = username;
        this.attemptCount = attemptCount;
        this.maxAttempts = maxAttempts;
        this.recoveryOptions = new ArrayList<>();
        
        // Calculate lockout if max attempts reached
        if (attemptCount >= maxAttempts) {
            this.lockoutDuration = calculateLockoutDuration(attemptCount);
            this.lockoutUntil = LocalDateTime.now().plus(lockoutDuration);
        }
    }
    
    public boolean isAccountLocked() {
        return lockoutUntil != null && LocalDateTime.now().isBefore(lockoutUntil);
    }
    
    public Duration getTimeUntilUnlock() {
        if (lockoutUntil == null) return Duration.ZERO;
        return Duration.between(LocalDateTime.now(), lockoutUntil);
    }
    
    public AuthenticationFailedException withRecoveryOptions(List<String> options) {
        this.recoveryOptions = new ArrayList<>(options);
        return this;
    }
    
    private Duration calculateLockoutDuration(int attempts) {
        // Exponential backoff: 15 mins, 30 mins, 1 hour, 2 hours...
        long minutes = 15 * (long) Math.pow(2, Math.min(attempts - maxAttempts, 4));
        return Duration.ofMinutes(minutes);
    }
}

// Banking service with comprehensive exception handling
@Service
public class BankingService {
    
    public void transfer(String fromAccount, String toAccount, BigDecimal amount) 
            throws BankingException {
        
        String transactionId = generateTransactionId();
        
        try {
            // Validate accounts
            Account from = validateAndGetAccount(fromAccount);
            Account to = validateAndGetAccount(toAccount);
            
            // Security checks
            validateTransactionSecurity(from, to, amount);
            
            // Business rule checks
            validateTransactionLimits(from, amount);
            validateSufficientFunds(from, amount);
            
            // Perform transfer
            performTransfer(from, to, amount, transactionId);
            
        } catch (BankingException e) {
            // Add transaction context and log
            e.withAccount(fromAccount)
             .withAmount(amount)
             .addAuditData("toAccount", toAccount)
             .addAuditData("transactionId", transactionId);
            
            e.logForCompliance();
            throw e;
            
        } catch (Exception e) {
            // Convert unexpected exceptions
            SystemException systemException = new SystemException(
                "Transfer failed due to system error", "SYSTEM_ERROR", e)
                .withAccount(fromAccount)
                .withAmount(amount)
                .addAuditData("toAccount", toAccount);
            
            systemException.logForCompliance();
            throw systemException;
        }
    }
    
    private void validateSufficientFunds(Account account, BigDecimal amount) 
            throws InsufficientFundsException {
        
        BigDecimal available = account.getAvailableBalance();
        
        if (available.compareTo(amount) < 0) {
            OverdraftLimit overdraft = getOverdraftLimit(account);
            List<OverdraftOption> options = getOverdraftOptions(account);
            
            throw new InsufficientFundsException(amount, available, 
                    overdraft != null ? overdraft.getLimit() : BigDecimal.ZERO)
                .withOverdraftOptions(options)
                .withRegulatoryCode("REG_E_OVERDRAFT");
        }
    }
}
```

</div>

</div>

---
layout: default
---

# Best Practices for Custom Exceptions

<div class="grid grid-cols-2 gap-6">

<div>

## Exception Design Guidelines

### 1. **Naming Conventions**
```java
// GOOD: Descriptive names that clearly indicate the problem
public class InsufficientFundsException extends Exception { }
public class UserAlreadyExistsException extends Exception { }
public class EmailDeliveryFailedException extends Exception { }

// BAD: Generic or unclear names
public class BadException extends Exception { }
public class ErrorException extends Exception { }
public class FailException extends Exception { }
```

### 2. **Constructor Patterns**
```java
// Standard constructor pattern for custom exceptions
public class CustomBusinessException extends Exception {
    
    // 1. Default constructor
    public CustomBusinessException() {
        super();
    }
    
    // 2. Message constructor
    public CustomBusinessException(String message) {
        super(message);
    }
    
    // 3. Cause constructor
    public CustomBusinessException(Throwable cause) {
        super(cause);
    }
    
    // 4. Message and cause constructor
    public CustomBusinessException(String message, Throwable cause) {
        super(message, cause);
    }
    
    // 5. All-args constructor with suppression and stack trace control
    public CustomBusinessException(String message, Throwable cause,
                                  boolean enableSuppression,
                                  boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
```

### 3. **Adding Context Information**
```java
public class OrderProcessingException extends Exception {
    private final String orderId;
    private final String customerId;
    private final OrderStatus currentStatus;
    private final String processingStage;
    
    public OrderProcessingException(String orderId, String customerId, 
                                  OrderStatus currentStatus, String processingStage,
                                  String message) {
        super(buildMessage(orderId, processingStage, message));
        this.orderId = orderId;
        this.customerId = customerId;
        this.currentStatus = currentStatus;
        this.processingStage = processingStage;
    }
    
    private static String buildMessage(String orderId, String stage, String message) {
        return String.format("Order processing failed at stage '%s' for order %s: %s",
                           stage, orderId, message);
    }
    
    // Getters (make fields final and provide only getters)
    public String getOrderId() { return orderId; }
    public String getCustomerId() { return customerId; }
    public OrderStatus getCurrentStatus() { return currentStatus; }
    public String getProcessingStage() { return processingStage; }
}
```

</div>

<div>

### 4. **Exception Hierarchies**
```java
// Create logical hierarchies that support both specific and general handling
public abstract class ApplicationException extends Exception {
    private final String errorCode;
    private final LocalDateTime timestamp;
    
    protected ApplicationException(String message, String errorCode) {
        super(message);
        this.errorCode = errorCode;
        this.timestamp = LocalDateTime.now();
    }
    
    public String getErrorCode() { return errorCode; }
    public LocalDateTime getTimestamp() { return timestamp; }
}

// Separate business vs system exceptions
public abstract class BusinessException extends ApplicationException {
    protected BusinessException(String message, String errorCode) {
        super(message, errorCode);
    }
}

public abstract class SystemException extends ApplicationException {
    protected SystemException(String message, String errorCode) {
        super(message, errorCode);
    }
    
    protected SystemException(String message, String errorCode, Throwable cause) {
        super(message, cause);
        this.errorCode = errorCode;
    }
}

// Specific implementations
public class ValidationException extends BusinessException {
    public ValidationException(String message) {
        super(message, "VALIDATION_ERROR");
    }
}

public class DatabaseException extends SystemException {
    public DatabaseException(String message, Throwable cause) {
        super(message, "DATABASE_ERROR", cause);
    }
}
```

### 5. **Testing Custom Exceptions**
```java
@Test
public void testInsufficientFundsException() {
    // Test exception creation
    BigDecimal requested = new BigDecimal("100.00");
    BigDecimal available = new BigDecimal("50.00");
    BigDecimal overdraft = new BigDecimal("25.00");
    
    InsufficientFundsException exception = new InsufficientFundsException(
        requested, available, overdraft);
    
    // Test exception properties
    assertEquals(requested, exception.getRequestedAmount());
    assertEquals(available, exception.getAvailableBalance());
    assertEquals(new BigDecimal("50.00"), exception.getShortfall());
    assertFalse(exception.hasOverdraftAvailable());
    
    // Test message content
    assertTrue(exception.getMessage().contains("requested=100.00"));
    assertTrue(exception.getMessage().contains("available=50.00"));
    
    // Test with overdraft available
    BigDecimal largeOverdraft = new BigDecimal("100.00");
    InsufficientFundsException exceptionWithOverdraft = 
        new InsufficientFundsException(requested, available, largeOverdraft);
    
    assertTrue(exceptionWithOverdraft.hasOverdraftAvailable());
    assertEquals(new BigDecimal("150.00"), exceptionWithOverdraft.getMaximumWithdrawal());
}

@Test
public void testExceptionChaining() {
    SQLException originalException = new SQLException("Connection failed");
    
    DatabaseException chainedException = new DatabaseException(
        "Failed to save user", originalException);
    
    assertEquals("Failed to save user", chainedException.getMessage());
    assertEquals(originalException, chainedException.getCause());
    assertEquals("DATABASE_ERROR", chainedException.getErrorCode());
    assertNotNull(chainedException.getTimestamp());
}

@Test
public void testExceptionInService() {
    // Test that service methods throw appropriate exceptions
    BankingService service = new BankingService();
    
    assertThrows(AccountNotFoundException.class, () -> {
        service.getBalance("INVALID_ACCOUNT");
    });
    
    assertThrows(InsufficientFundsException.class, () -> {
        service.withdraw("123456", new BigDecimal("1000000"));
    });
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

- 🏗️ **Custom Exception Creation**: Building exceptions specific to business domains
- 🎯 **Exception Hierarchies**: Designing logical inheritance structures
- 📋 **Context Information**: Adding relevant data to exceptions for better debugging
- ⚡ **Exception Chaining**: Preserving original exception information
- 🔧 **Recovery Information**: Including data to help with error recovery
- 🎭 **Advanced Features**: Internationalization, retry logic, and contextual help
- 💡 **Best Practices**: Naming, constructors, testing, and design patterns

</v-clicks>

## Custom Exception Benefits

### Development Benefits
- **Clear Intent**: Exception names convey exactly what went wrong
- **Better Debugging**: Specific context makes problems easier to trace
- **Maintainability**: Changes can be localized to specific exception types
- **Testing**: Can test for specific error conditions
- **Documentation**: Exception types serve as API documentation

### Runtime Benefits  
- **Precise Error Handling**: Different exceptions enable different recovery strategies
- **User Experience**: Domain-specific errors translate to better user messages
- **Monitoring**: Can track specific error patterns and trends
- **Compliance**: Audit trails and regulatory reporting requirements

</div>

<div>

## Design Principles Recap

<v-clicks>

- **Domain-Specific**: Create exceptions that reflect your business domain
- **Meaningful Names**: Exception class names should clearly indicate the problem
- **Rich Context**: Include relevant data that helps with debugging and recovery
- **Proper Inheritance**: Design hierarchies that support both specific and general handling
- **Consistent Constructors**: Follow standard patterns for exception constructors
- **Immutable Data**: Make exception data fields final and provide only getters
- **Chain Appropriately**: Preserve original exception information when converting
- **Test Thoroughly**: Write comprehensive tests for custom exception behavior

</v-clicks>

## When to Create Custom Exceptions

### ✅ **Create Custom When:**
- Business domain needs specific error types
- Need to include additional context data
- Different errors require different handling strategies
- Want to provide recovery or alternative action information
- Need to meet regulatory or compliance requirements

### ❌ **Don't Create Custom When:**
- Built-in Java exceptions already cover the scenario well
- No additional context or specific handling is needed
- Would create too many similar exceptions without clear benefit
- Adds unnecessary complexity to the codebase

## Real-world Impact

### Without Custom Exceptions
- Generic error messages that don't help users
- Difficult debugging with limited context
- Hard to implement different recovery strategies
- Poor user experience with technical error messages

### With Well-Designed Custom Exceptions
- Clear, domain-specific error reporting
- Rich context for effective debugging
- Targeted error handling and recovery
- Professional user experience with meaningful messages

</div>

</div>

---
layout: center
class: text-center
---

# Thank You!
## Custom Exceptions Complete

**Lecture 29 Successfully Completed!**  
You can now design and implement domain-specific exception systems

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Ready to build robust, professional applications! <carbon:arrow-right class="inline"/>
  </span>
</div>