---
theme: default
background: https://source.unsplash.com/1024x768/?java,programming
class: text-center
highlighter: shiki
lineNumbers: true
drawings:
  persist: false
transition: slide-left
title: Java Programming - Lecture 41
mdc: true
---

# Java Programming
## Lecture 41: JavaFX Basics and GUI Programming
### GTU Diploma in Computer Engineering

---
layout: two-cols
---

# Learning Objectives

After this lecture, you will be able to:

- Understand JavaFX architecture and components
- Create basic JavaFX applications
- Work with scenes, stages, and nodes
- Handle user events and interactions
- Use common JavaFX controls and layouts
- Style applications with CSS
- Build responsive user interfaces
- Create data-driven applications with TableView

::right::

# Lecture Overview

1. **Introduction to JavaFX**
2. **JavaFX Application Structure**
3. **Scene Graph and Nodes**
4. **Common Controls**
5. **Layout Managers**
6. **Event Handling**
7. **CSS Styling**
8. **TableView and Data Binding**
9. **FXML and Scene Builder**
10. **Hands-on Exercises**

---

# What is JavaFX?

JavaFX is a modern UI toolkit for building rich desktop applications in Java.

## Key Features

1. **Rich UI Controls**: Extensive set of built-in controls
2. **CSS Styling**: Web-like styling capabilities
3. **FXML**: XML-based markup for UI design
4. **Scene Graph**: Hierarchical representation of UI components
5. **Hardware Acceleration**: GPU-accelerated graphics
6. **Media Support**: Audio and video playback
7. **Web Integration**: WebView component for HTML content

## JavaFX vs Swing

```java
// Swing approach
import javax.swing.*;
import java.awt.*;

public class SwingExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Swing Example");
        JButton button = new JButton("Click me");
        button.addActionListener(e -> 
            JOptionPane.showMessageDialog(frame, "Button clicked!"));
        
        frame.add(button);
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

// JavaFX approach
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class JavaFXExample extends Application {
    @Override
    public void start(Stage primaryStage) {
        Button button = new Button("Click me");
        button.setOnAction(e -> {
            Alert alert = new Alert(Alert.AlertType.INFORMATION, "Button clicked!");
            alert.showAndWait();
        });
        
        VBox root = new VBox(button);
        Scene scene = new Scene(root, 300, 200);
        
        primaryStage.setTitle("JavaFX Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# JavaFX Application Structure

Every JavaFX application follows a specific structure.

## Basic Application Template

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class BasicJavaFXApp extends Application {
    
    @Override
    public void start(Stage primaryStage) throws Exception {
        // Create the root node
        StackPane root = new StackPane();
        
        // Add components to the root
        Label label = new Label("Hello, JavaFX!");
        root.getChildren().add(label);
        
        // Create the scene
        Scene scene = new Scene(root, 400, 300);
        
        // Set up the primary stage
        primaryStage.setTitle("My JavaFX Application");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    @Override
    public void init() throws Exception {
        // Called before start() - initialize application
        System.out.println("Application initializing...");
    }
    
    @Override
    public void stop() throws Exception {
        // Called when application is closing - cleanup resources
        System.out.println("Application stopping...");
    }
    
    public static void main(String[] args) {
        launch(args); // Launches the JavaFX application
    }
}
```

## Application Lifecycle

```java
import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class LifecycleDemo extends Application {
    
    private TextArea logArea;
    
    @Override
    public void init() throws Exception {
        log("init() called - Application thread: " + Thread.currentThread().getName());
        // Initialize non-UI components here
        // This runs on the launcher thread, NOT the JavaFX Application Thread
    }
    
    @Override
    public void start(Stage primaryStage) throws Exception {
        log("start() called - JavaFX Application Thread: " + Thread.currentThread().getName());
        
        logArea = new TextArea();
        logArea.setEditable(false);
        logArea.setPrefRowCount(10);
        
        Button exitButton = new Button("Exit Application");
        exitButton.setOnAction(e -> {
            log("Exit button clicked");
            Platform.exit(); // Proper way to exit JavaFX application
        });
        
        VBox root = new VBox(10);
        root.getChildren().addAll(
            new Label("Application Lifecycle Demo"),
            logArea,
            exitButton
        );
        
        Scene scene = new Scene(root, 500, 400);
        primaryStage.setTitle("JavaFX Lifecycle");
        primaryStage.setScene(scene);
        primaryStage.show();
        
        log("Application started successfully");
    }
    
    @Override
    public void stop() throws Exception {
        log("stop() called - Application is shutting down");
        // Cleanup resources here
        // Save application state, close connections, etc.
    }
    
    private void log(String message) {
        String logMessage = System.currentTimeMillis() + ": " + message;
        System.out.println(logMessage);
        
        if (logArea != null) {
            Platform.runLater(() -> {
                logArea.appendText(logMessage + "\n");
            });
        }
    }
    
    public static void main(String[] args) {
        System.out.println("main() called - Main thread: " + Thread.currentThread().getName());
        launch(args);
        System.out.println("main() finished - Application has terminated");
    }
}
```

---

# Scene Graph and Nodes

JavaFX uses a scene graph - a hierarchical tree of nodes.

## Understanding the Hierarchy

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class SceneGraphDemo extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        // Stage (Window)
        //   └── Scene
        //       └── Root Node (Parent)
        //           ├── Child Node 1
        //           ├── Child Node 2
        //           └── Child Node 3 (Parent)
        //               ├── Grandchild 1
        //               └── Grandchild 2
        
        // Create leaf nodes (no children)
        Button button1 = new Button("Button 1");
        Button button2 = new Button("Button 2");
        Label label = new Label("This is a label");
        TextField textField = new TextField("Enter text here");
        
        // Create parent nodes that contain other nodes
        HBox buttonBox = new HBox(10); // Horizontal layout with 10px spacing
        buttonBox.getChildren().addAll(button1, button2);
        
        VBox inputBox = new VBox(5); // Vertical layout with 5px spacing
        inputBox.getChildren().addAll(label, textField);
        
        // Create root node
        VBox root = new VBox(20); // Main container
        root.getChildren().addAll(
            new Label("Scene Graph Hierarchy Demo"),
            buttonBox,
            inputBox,
            createInfoButton()
        );
        
        // Set some styling
        root.setStyle("-fx-padding: 20; -fx-alignment: center;");
        buttonBox.setStyle("-fx-alignment: center;");
        inputBox.setStyle("-fx-alignment: center;");
        
        Scene scene = new Scene(root, 400, 300);
        primaryStage.setTitle("Scene Graph Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
        
        // Demonstrate node traversal
        demonstrateNodeTraversal(root);
    }
    
    private Button createInfoButton() {
        Button infoButton = new Button("Show Scene Graph Info");
        infoButton.setOnAction(e -> {
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("Scene Graph Information");
            alert.setHeaderText("Current Scene Graph Structure");
            alert.setContentText(
                "Stage\n" +
                "└── Scene\n" +
                "    └── VBox (root)\n" +
                "        ├── Label\n" +
                "        ├── HBox\n" +
                "        │   ├── Button 1\n" +
                "        │   └── Button 2\n" +
                "        ├── VBox\n" +
                "        │   ├── Label\n" +
                "        │   └── TextField\n" +
                "        └── Button (Info)"
            );
            alert.showAndWait();
        });
        return infoButton;
    }
    
    private void demonstrateNodeTraversal(VBox root) {
        System.out.println("Traversing scene graph:");
        traverseNode(root, 0);
    }
    
    private void traverseNode(Object node, int depth) {
        String indent = "  ".repeat(depth);
        System.out.println(indent + node.getClass().getSimpleName());
        
        if (node instanceof Parent) {
            Parent parent = (Parent) node;
            for (Object child : parent.getChildrenUnmodifiable()) {
                traverseNode(child, depth + 1);
            }
        }
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Common JavaFX Controls

JavaFX provides a rich set of built-in controls.

## Basic Controls

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class BasicControlsDemo extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        VBox root = new VBox(10);
        root.setStyle("-fx-padding: 20;");
        
        // Label
        Label titleLabel = new Label("JavaFX Controls Demo");
        titleLabel.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
        
        // Button
        Button actionButton = new Button("Click Me!");
        actionButton.setOnAction(e -> showAlert("Button clicked!"));
        
        // TextField
        TextField textField = new TextField();
        textField.setPromptText("Enter your name");
        
        // TextArea
        TextArea textArea = new TextArea();
        textArea.setPromptText("Enter multiple lines of text here...");
        textArea.setPrefRowCount(3);
        
        // CheckBox
        CheckBox checkBox1 = new CheckBox("Option 1");
        CheckBox checkBox2 = new CheckBox("Option 2");
        checkBox2.setSelected(true); // Pre-selected
        
        // RadioButtons (grouped)
        ToggleGroup radioGroup = new ToggleGroup();
        RadioButton radio1 = new RadioButton("Choice A");
        RadioButton radio2 = new RadioButton("Choice B");
        RadioButton radio3 = new RadioButton("Choice C");
        radio1.setToggleGroup(radioGroup);
        radio2.setToggleGroup(radioGroup);
        radio3.setToggleGroup(radioGroup);
        radio2.setSelected(true); // Pre-selected
        
        // ComboBox (Dropdown)
        ComboBox<String> comboBox = new ComboBox<>();
        comboBox.getItems().addAll("Java", "Python", "JavaScript", "C++", "Ruby");
        comboBox.setPromptText("Select a language");
        
        // ListView
        ListView<String> listView = new ListView<>();
        listView.getItems().addAll("Item 1", "Item 2", "Item 3", "Item 4", "Item 5");
        listView.setPrefHeight(100);
        
        // Slider
        Slider slider = new Slider(0, 100, 50);
        slider.setShowTickLabels(true);
        slider.setShowTickMarks(true);
        slider.setMajorTickUnit(25);
        
        Label sliderLabel = new Label("Value: 50");
        slider.valueProperty().addListener((obs, oldVal, newVal) -> 
            sliderLabel.setText("Value: " + Math.round(newVal.doubleValue())));
        
        // ProgressBar
        ProgressBar progressBar = new ProgressBar(0.6);
        
        // ProgressIndicator
        ProgressIndicator progressIndicator = new ProgressIndicator(0.75);
        
        // Button to demonstrate interactions
        Button demoButton = new Button("Show Current Values");
        demoButton.setOnAction(e -> showCurrentValues(textField, textArea, checkBox1, checkBox2, 
                                                     radioGroup, comboBox, listView, slider));
        
        // Add all controls to the root
        root.getChildren().addAll(
            titleLabel,
            new Separator(),
            new Label("Text Input:"),
            textField,
            textArea,
            new Separator(),
            new Label("Selection Controls:"),
            checkBox1,
            checkBox2,
            new Label("Radio Buttons:"),
            radio1, radio2, radio3,
            new Label("Dropdown:"),
            comboBox,
            new Label("List:"),
            listView,
            new Separator(),
            new Label("Value Controls:"),
            new Label("Slider:"),
            slider,
            sliderLabel,
            new Label("Progress Controls:"),
            progressBar,
            progressIndicator,
            new Separator(),
            actionButton,
            demoButton
        );
        
        Scene scene = new Scene(new ScrollPane(root), 400, 600);
        primaryStage.setTitle("JavaFX Controls Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    private void showAlert(String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Information");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
    
    private void showCurrentValues(TextField textField, TextArea textArea, 
                                 CheckBox checkBox1, CheckBox checkBox2,
                                 ToggleGroup radioGroup, ComboBox<String> comboBox,
                                 ListView<String> listView, Slider slider) {
        StringBuilder sb = new StringBuilder();
        sb.append("Current Values:\n\n");
        
        sb.append("TextField: ").append(textField.getText()).append("\n");
        sb.append("TextArea: ").append(textArea.getText().replaceAll("\n", " ")).append("\n\n");
        
        sb.append("CheckBox 1: ").append(checkBox1.isSelected()).append("\n");
        sb.append("CheckBox 2: ").append(checkBox2.isSelected()).append("\n\n");
        
        RadioButton selectedRadio = (RadioButton) radioGroup.getSelectedToggle();
        sb.append("Selected Radio: ").append(selectedRadio != null ? selectedRadio.getText() : "None").append("\n\n");
        
        sb.append("ComboBox: ").append(comboBox.getValue()).append("\n");
        sb.append("ListView Selection: ").append(listView.getSelectionModel().getSelectedItem()).append("\n\n");
        
        sb.append("Slider: ").append(Math.round(slider.getValue())).append("\n");
        
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Current Values");
        alert.setHeaderText("Form Data");
        alert.setContentText(sb.toString());
        alert.showAndWait();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Layout Managers

Layout managers control how components are arranged in containers.

## Common Layout Managers

```java
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class LayoutDemo extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        TabPane tabPane = new TabPane();
        
        // VBox Layout
        Tab vboxTab = new Tab("VBox");
        vboxTab.setContent(createVBoxDemo());
        
        // HBox Layout
        Tab hboxTab = new Tab("HBox");
        hboxTab.setContent(createHBoxDemo());
        
        // BorderPane Layout
        Tab borderPaneTab = new Tab("BorderPane");
        borderPaneTab.setContent(createBorderPaneDemo());
        
        // GridPane Layout
        Tab gridPaneTab = new Tab("GridPane");
        gridPaneTab.setContent(createGridPaneDemo());
        
        // StackPane Layout
        Tab stackPaneTab = new Tab("StackPane");
        stackPaneTab.setContent(createStackPaneDemo());
        
        // FlowPane Layout
        Tab flowPaneTab = new Tab("FlowPane");
        flowPaneTab.setContent(createFlowPaneDemo());
        
        tabPane.getTabs().addAll(vboxTab, hboxTab, borderPaneTab, 
                                gridPaneTab, stackPaneTab, flowPaneTab);
        
        Scene scene = new Scene(tabPane, 600, 500);
        primaryStage.setTitle("JavaFX Layout Managers");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    private VBox createVBoxDemo() {
        VBox vbox = new VBox(10);
        vbox.setPadding(new Insets(20));
        vbox.setAlignment(Pos.CENTER);
        
        Label title = new Label("VBox Layout - Vertical Stack");
        title.setStyle("-fx-font-weight: bold;");
        
        Button btn1 = new Button("Button 1");
        Button btn2 = new Button("Button 2 (Longer)");
        Button btn3 = new Button("Button 3");
        
        // Demonstrate VBox properties
        VBox.setVgrow(btn2, Priority.ALWAYS); // Button 2 will grow vertically
        
        vbox.getChildren().addAll(title, btn1, btn2, btn3);
        return vbox;
    }
    
    private HBox createHBoxDemo() {
        VBox container = new VBox(20);
        container.setPadding(new Insets(20));
        
        Label title = new Label("HBox Layout - Horizontal Stack");
        title.setStyle("-fx-font-weight: bold;");
        
        HBox hbox = new HBox(10);
        hbox.setAlignment(Pos.CENTER);
        
        Button btn1 = new Button("Button 1");
        Button btn2 = new Button("Button 2");
        Button btn3 = new Button("Button 3");
        
        // Demonstrate HBox properties
        HBox.setHgrow(btn2, Priority.ALWAYS); // Button 2 will grow horizontally
        btn2.setMaxWidth(Double.MAX_VALUE);
        
        hbox.getChildren().addAll(btn1, btn2, btn3);
        container.getChildren().addAll(title, hbox);
        return container;
    }
    
    private VBox createBorderPaneDemo() {
        VBox container = new VBox(10);
        container.setPadding(new Insets(20));
        
        Label title = new Label("BorderPane Layout - Five Regions");
        title.setStyle("-fx-font-weight: bold;");
        
        BorderPane borderPane = new BorderPane();
        borderPane.setPrefSize(300, 200);
        
        // Add components to different regions
        borderPane.setTop(new Label("TOP"));
        borderPane.setBottom(new Label("BOTTOM"));
        borderPane.setLeft(new Label("LEFT"));
        borderPane.setRight(new Label("RIGHT"));
        borderPane.setCenter(new Label("CENTER"));
        
        // Style the regions
        borderPane.getTop().setStyle("-fx-background-color: lightblue; -fx-padding: 10;");
        borderPane.getBottom().setStyle("-fx-background-color: lightgreen; -fx-padding: 10;");
        borderPane.getLeft().setStyle("-fx-background-color: lightcoral; -fx-padding: 10;");
        borderPane.getRight().setStyle("-fx-background-color: lightyellow; -fx-padding: 10;");
        borderPane.getCenter().setStyle("-fx-background-color: lightgray; -fx-padding: 10;");
        
        container.getChildren().addAll(title, borderPane);
        return container;
    }
    
    private VBox createGridPaneDemo() {
        VBox container = new VBox(10);
        container.setPadding(new Insets(20));
        
        Label title = new Label("GridPane Layout - Grid Structure");
        title.setStyle("-fx-font-weight: bold;");
        
        GridPane gridPane = new GridPane();
        gridPane.setHgap(10);
        gridPane.setVgap(10);
        gridPane.setPadding(new Insets(10));
        
        // Add components to specific grid positions
        gridPane.add(new Label("Name:"), 0, 0);
        gridPane.add(new TextField(), 1, 0);
        
        gridPane.add(new Label("Email:"), 0, 1);
        gridPane.add(new TextField(), 1, 1);
        
        gridPane.add(new Label("Password:"), 0, 2);
        gridPane.add(new PasswordField(), 1, 2);
        
        Button submitBtn = new Button("Submit");
        gridPane.add(submitBtn, 0, 3, 2, 1); // Span 2 columns
        
        // Make text fields grow
        ColumnConstraints col1 = new ColumnConstraints();
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHgrow(Priority.ALWAYS);
        gridPane.getColumnConstraints().addAll(col1, col2);
        
        container.getChildren().addAll(title, gridPane);
        return container;
    }
    
    private VBox createStackPaneDemo() {
        VBox container = new VBox(10);
        container.setPadding(new Insets(20));
        
        Label title = new Label("StackPane Layout - Stacked Components");
        title.setStyle("-fx-font-weight: bold;");
        
        StackPane stackPane = new StackPane();
        stackPane.setPrefSize(200, 150);
        
        // Create layered components
        Label background = new Label("Background Layer");
        background.setStyle("-fx-background-color: lightblue; -fx-font-size: 16px;");
        background.setPrefSize(180, 130);
        
        Label foreground = new Label("Foreground Layer");
        foreground.setStyle("-fx-background-color: rgba(255, 255, 255, 0.8); " +
                          "-fx-border-color: black; -fx-padding: 10;");
        
        stackPane.getChildren().addAll(background, foreground);
        
        container.getChildren().addAll(title, stackPane);
        return container;
    }
    
    private VBox createFlowPaneDemo() {
        VBox container = new VBox(10);
        container.setPadding(new Insets(20));
        
        Label title = new Label("FlowPane Layout - Flowing Components");
        title.setStyle("-fx-font-weight: bold;");
        
        FlowPane flowPane = new FlowPane();
        flowPane.setHgap(10);
        flowPane.setVgap(10);
        flowPane.setPrefWrapLength(250); // Wrap after 250 pixels
        
        // Add various sized buttons
        for (int i = 1; i <= 12; i++) {
            Button btn = new Button("Button " + i);
            if (i % 3 == 0) {
                btn.setPrefWidth(80);
            } else if (i % 2 == 0) {
                btn.setPrefWidth(60);
            }
            flowPane.getChildren().add(btn);
        }
        
        container.getChildren().addAll(title, flowPane);
        return container;
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Event Handling

JavaFX provides multiple ways to handle user events.

## Event Handling Mechanisms

```java
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.KeyEvent;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class EventHandlingDemo extends Application {
    
    private TextArea logArea;
    
    @Override
    public void start(Stage primaryStage) {
        VBox root = new VBox(10);
        root.setStyle("-fx-padding: 20;");
        
        // Log area to show events
        logArea = new TextArea();
        logArea.setPrefRowCount(10);
        logArea.setEditable(false);
        
        // 1. Lambda expression event handling
        Button lambdaButton = new Button("Lambda Event Handler");
        lambdaButton.setOnAction(e -> log("Lambda button clicked!"));
        
        // 2. Method reference event handling
        Button methodRefButton = new Button("Method Reference Handler");
        methodRefButton.setOnAction(this::handleMethodRefButton);
        
        // 3. Anonymous class event handling
        Button anonymousButton = new Button("Anonymous Class Handler");
        anonymousButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                log("Anonymous class button clicked!");
            }
        });
        
        // 4. Multiple event types on same control
        Button multiEventButton = new Button("Multi-Event Button");
        
        // Mouse events
        multiEventButton.setOnMouseEntered(e -> log("Mouse entered button"));
        multiEventButton.setOnMouseExited(e -> log("Mouse exited button"));
        multiEventButton.setOnMousePressed(e -> log("Mouse pressed on button"));
        multiEventButton.setOnMouseReleased(e -> log("Mouse released on button"));
        
        // Action event
        multiEventButton.setOnAction(e -> log("Multi-event button clicked!"));
        
        // 5. TextField with key events
        TextField textField = new TextField();
        textField.setPromptText("Type here to see key events");
        
        textField.setOnKeyPressed(e -> log("Key pressed: " + e.getCode()));
        textField.setOnKeyReleased(e -> log("Key released: " + e.getCode()));
        textField.setOnKeyTyped(e -> log("Key typed: '" + e.getCharacter() + "'"));
        
        // Text change listener
        textField.textProperty().addListener((obs, oldText, newText) -> 
            log("Text changed from '" + oldText + "' to '" + newText + "'"));
        
        // 6. CheckBox with change listener
        CheckBox checkBox = new CheckBox("Check me");
        checkBox.selectedProperty().addListener((obs, wasSelected, isSelected) -> 
            log("CheckBox " + (isSelected ? "checked" : "unchecked")));
        
        // 7. Slider with value change listener
        Slider slider = new Slider(0, 100, 50);
        slider.setShowTickLabels(true);
        slider.setShowTickMarks(true);
        
        Label sliderValueLabel = new Label("Value: 50");
        slider.valueProperty().addListener((obs, oldVal, newVal) -> {
            int value = newVal.intValue();
            sliderValueLabel.setText("Value: " + value);
            log("Slider value changed to: " + value);
        });
        
        // 8. ComboBox selection event
        ComboBox<String> comboBox = new ComboBox<>();
        comboBox.getItems().addAll("Option 1", "Option 2", "Option 3");
        comboBox.setPromptText("Select an option");
        
        comboBox.setOnAction(e -> log("ComboBox selection: " + comboBox.getValue()));
        
        // 9. Custom event handling with event filters
        Button filterButton = new Button("Event Filter Demo");
        
        // Add event filter (runs before event handlers)
        filterButton.addEventFilter(MouseEvent.MOUSE_CLICKED, e -> {
            log("Event filter: Mouse click intercepted");
            if (e.isControlDown()) {
                log("Ctrl+Click detected - consuming event");
                e.consume(); // Prevent further processing
            }
        });
        
        // Regular event handler
        filterButton.setOnMouseClicked(e -> log("Event handler: Button clicked"));
        
        // Clear log button
        Button clearButton = new Button("Clear Log");
        clearButton.setOnAction(e -> logArea.clear());
        
        root.getChildren().addAll(
            new Label("Event Handling Demo - Check the log area below:"),
            lambdaButton,
            methodRefButton,
            anonymousButton,
            multiEventButton,
            new Separator(),
            new Label("TextField (with key events):"),
            textField,
            checkBox,
            new Label("Slider (with value change listener):"),
            slider,
            sliderValueLabel,
            new Label("ComboBox (with selection event):"),
            comboBox,
            new Separator(),
            filterButton,
            new Label("(Try Ctrl+Click on the filter button)"),
            new Separator(),
            clearButton,
            new Label("Event Log:"),
            logArea
        );
        
        Scene scene = new Scene(new ScrollPane(root), 500, 700);
        primaryStage.setTitle("Event Handling Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
        
        log("Application started - ready for events!");
    }
    
    private void handleMethodRefButton(ActionEvent event) {
        log("Method reference button clicked!");
    }
    
    private void log(String message) {
        logArea.appendText("[" + System.currentTimeMillis() % 10000 + "] " + message + "\n");
        logArea.setScrollTop(Double.MAX_VALUE); // Scroll to bottom
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# CSS Styling

JavaFX supports CSS for styling applications.

## CSS Styling Examples

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class CSSStyleDemo extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        VBox root = new VBox(20);
        root.setStyle("-fx-padding: 30; -fx-background-color: #f0f0f0;");
        
        // Title with inline CSS
        Label title = new Label("JavaFX CSS Styling Demo");
        title.setStyle("-fx-font-size: 24px; " +
                      "-fx-font-weight: bold; " +
                      "-fx-text-fill: #2c3e50; " +
                      "-fx-alignment: center;");
        
        // Styled buttons
        Button primaryButton = new Button("Primary Button");
        primaryButton.setStyle(
            "-fx-background-color: #3498db; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 14px; " +
            "-fx-padding: 10 20; " +
            "-fx-background-radius: 5; " +
            "-fx-cursor: hand;"
        );
        
        Button successButton = new Button("Success Button");
        successButton.setStyle(
            "-fx-background-color: #27ae60; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 14px; " +
            "-fx-padding: 10 20; " +
            "-fx-background-radius: 5; " +
            "-fx-cursor: hand;"
        );
        
        Button warningButton = new Button("Warning Button");
        warningButton.setStyle(
            "-fx-background-color: #f39c12; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 14px; " +
            "-fx-padding: 10 20; " +
            "-fx-background-radius: 5; " +
            "-fx-cursor: hand;"
        );
        
        Button dangerButton = new Button("Danger Button");
        dangerButton.setStyle(
            "-fx-background-color: #e74c3c; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 14px; " +
            "-fx-padding: 10 20; " +
            "-fx-background-radius: 5; " +
            "-fx-cursor: hand;"
        );
        
        // Styled text field
        TextField styledTextField = new TextField();
        styledTextField.setPromptText("Styled text field");
        styledTextField.setStyle(
            "-fx-background-color: white; " +
            "-fx-border-color: #bdc3c7; " +
            "-fx-border-width: 2; " +
            "-fx-border-radius: 5; " +
            "-fx-padding: 10; " +
            "-fx-font-size: 14px;"
        );
        
        // Focus styling
        styledTextField.focusedProperty().addListener((obs, wasFocused, isFocused) -> {
            if (isFocused) {
                styledTextField.setStyle(
                    "-fx-background-color: white; " +
                    "-fx-border-color: #3498db; " +
                    "-fx-border-width: 2; " +
                    "-fx-border-radius: 5; " +
                    "-fx-padding: 10; " +
                    "-fx-font-size: 14px;"
                );
            } else {
                styledTextField.setStyle(
                    "-fx-background-color: white; " +
                    "-fx-border-color: #bdc3c7; " +
                    "-fx-border-width: 2; " +
                    "-fx-border-radius: 5; " +
                    "-fx-padding: 10; " +
                    "-fx-font-size: 14px;"
                );
            }
        });
        
        // Styled text area
        TextArea styledTextArea = new TextArea();
        styledTextArea.setPromptText("Styled text area with custom styling");
        styledTextArea.setPrefRowCount(4);
        styledTextArea.setStyle(
            "-fx-background-color: #ecf0f1; " +
            "-fx-control-inner-background: #ecf0f1; " +
            "-fx-border-color: #95a5a6; " +
            "-fx-border-width: 2; " +
            "-fx-border-radius: 5; " +
            "-fx-font-family: 'Courier New'; " +
            "-fx-font-size: 12px;"
        );
        
        // CSS with hover effects using pseudoclasses
        Button hoverButton = new Button("Hover Effect Button");
        hoverButton.setStyle(
            "-fx-background-color: #9b59b6; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 14px; " +
            "-fx-padding: 15 25; " +
            "-fx-background-radius: 25; " +
            "-fx-cursor: hand; " +
            "-fx-effect: dropshadow(gaussian, rgba(0,0,0,0.3), 10, 0.5, 0.0, 1.0);"
        );
        
        // Hover effects using mouse events (since inline CSS can't handle :hover)
        hoverButton.setOnMouseEntered(e -> {
            hoverButton.setStyle(
                "-fx-background-color: #8e44ad; " +
                "-fx-text-fill: white; " +
                "-fx-font-size: 14px; " +
                "-fx-padding: 15 25; " +
                "-fx-background-radius: 25; " +
                "-fx-cursor: hand; " +
                "-fx-scale-x: 1.05; " +
                "-fx-scale-y: 1.05; " +
                "-fx-effect: dropshadow(gaussian, rgba(0,0,0,0.5), 15, 0.5, 0.0, 2.0);"
            );
        });
        
        hoverButton.setOnMouseExited(e -> {
            hoverButton.setStyle(
                "-fx-background-color: #9b59b6; " +
                "-fx-text-fill: white; " +
                "-fx-font-size: 14px; " +
                "-fx-padding: 15 25; " +
                "-fx-background-radius: 25; " +
                "-fx-cursor: hand; " +
                "-fx-scale-x: 1.0; " +
                "-fx-scale-y: 1.0; " +
                "-fx-effect: dropshadow(gaussian, rgba(0,0,0,0.3), 10, 0.5, 0.0, 1.0);"
            );
        });
        
        // Theme toggle button
        Button themeButton = new Button("Toggle Dark Theme");
        themeButton.setStyle(
            "-fx-background-color: #34495e; " +
            "-fx-text-fill: white; " +
            "-fx-font-size: 12px; " +
            "-fx-padding: 8 15; " +
            "-fx-background-radius: 3;"
        );
        
        boolean[] isDarkTheme = {false};
        themeButton.setOnAction(e -> {
            if (!isDarkTheme[0]) {
                // Apply dark theme
                root.setStyle("-fx-padding: 30; -fx-background-color: #2c3e50;");
                title.setStyle("-fx-font-size: 24px; -fx-font-weight: bold; -fx-text-fill: #ecf0f1;");
                themeButton.setText("Toggle Light Theme");
                isDarkTheme[0] = true;
            } else {
                // Apply light theme
                root.setStyle("-fx-padding: 30; -fx-background-color: #f0f0f0;");
                title.setStyle("-fx-font-size: 24px; -fx-font-weight: bold; -fx-text-fill: #2c3e50;");
                themeButton.setText("Toggle Dark Theme");
                isDarkTheme[0] = false;
            }
        });
        
        root.getChildren().addAll(
            title,
            new Separator(),
            primaryButton,
            successButton,
            warningButton,
            dangerButton,
            new Separator(),
            new Label("Styled Input Controls:"),
            styledTextField,
            styledTextArea,
            new Separator(),
            hoverButton,
            new Separator(),
            themeButton
        );
        
        Scene scene = new Scene(root, 400, 600);
        primaryStage.setTitle("CSS Styling Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# TableView and Data Binding

TableView is used for displaying tabular data with sorting and editing capabilities.

```java
import javafx.application.Application;
import javafx.beans.property.*;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.converter.IntegerStringConverter;

public class TableViewDemo extends Application {
    
    // Person model class with JavaFX properties
    public static class Person {
        private final StringProperty name;
        private final IntegerProperty age;
        private final StringProperty email;
        private final BooleanProperty active;
        
        public Person(String name, int age, String email, boolean active) {
            this.name = new SimpleStringProperty(name);
            this.age = new SimpleIntegerProperty(age);
            this.email = new SimpleStringProperty(email);
            this.active = new SimpleBooleanProperty(active);
        }
        
        // Property getters (required for TableView binding)
        public StringProperty nameProperty() { return name; }
        public IntegerProperty ageProperty() { return age; }
        public StringProperty emailProperty() { return email; }
        public BooleanProperty activeProperty() { return active; }
        
        // Value getters and setters
        public String getName() { return name.get(); }
        public void setName(String name) { this.name.set(name); }
        
        public int getAge() { return age.get(); }
        public void setAge(int age) { this.age.set(age); }
        
        public String getEmail() { return email.get(); }
        public void setEmail(String email) { this.email.set(email); }
        
        public boolean isActive() { return active.get(); }
        public void setActive(boolean active) { this.active.set(active); }
    }
    
    private TableView<Person> tableView;
    private ObservableList<Person> data;
    
    @Override
    public void start(Stage primaryStage) {
        VBox root = new VBox(10);
        root.setStyle("-fx-padding: 20;");
        
        // Create sample data
        data = FXCollections.observableArrayList(
            new Person("Alice Johnson", 25, "alice@example.com", true),
            new Person("Bob Smith", 30, "bob@example.com", true),
            new Person("Charlie Brown", 35, "charlie@example.com", false),
            new Person("Diana Prince", 28, "diana@example.com", true),
            new Person("Eve Wilson", 32, "eve@example.com", false)
        );
        
        // Create TableView
        tableView = new TableView<>();
        tableView.setEditable(true); // Enable editing
        
        // Create columns
        TableColumn<Person, String> nameColumn = new TableColumn<>("Name");
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        nameColumn.setCellFactory(TextFieldTableCell.forTableColumn());
        nameColumn.setOnEditCommit(event -> {
            event.getRowValue().setName(event.getNewValue());
            showAlert("Name updated to: " + event.getNewValue());
        });
        nameColumn.setPrefWidth(150);
        
        TableColumn<Person, Integer> ageColumn = new TableColumn<>("Age");
        ageColumn.setCellValueFactory(new PropertyValueFactory<>("age"));
        ageColumn.setCellFactory(TextFieldTableCell.forTableColumn(new IntegerStringConverter()));
        ageColumn.setOnEditCommit(event -> {
            event.getRowValue().setAge(event.getNewValue());
            showAlert("Age updated to: " + event.getNewValue());
        });
        ageColumn.setPrefWidth(80);
        
        TableColumn<Person, String> emailColumn = new TableColumn<>("Email");
        emailColumn.setCellValueFactory(new PropertyValueFactory<>("email"));
        emailColumn.setCellFactory(TextFieldTableCell.forTableColumn());
        emailColumn.setOnEditCommit(event -> {
            event.getRowValue().setEmail(event.getNewValue());
            showAlert("Email updated to: " + event.getNewValue());
        });
        emailColumn.setPrefWidth(200);
        
        TableColumn<Person, Boolean> activeColumn = new TableColumn<>("Active");
        activeColumn.setCellValueFactory(new PropertyValueFactory<>("active"));
        activeColumn.setCellFactory(col -> new TableCell<Person, Boolean>() {
            private final CheckBox checkBox = new CheckBox();
            
            {
                checkBox.setOnAction(e -> {
                    Person person = getTableRow().getItem();
                    if (person != null) {
                        person.setActive(checkBox.isSelected());
                        showAlert(person.getName() + " is now " + 
                                (checkBox.isSelected() ? "active" : "inactive"));
                    }
                });
            }
            
            @Override
            protected void updateItem(Boolean item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setGraphic(null);
                } else {
                    checkBox.setSelected(item);
                    setGraphic(checkBox);
                }
            }
        });
        activeColumn.setPrefWidth(80);
        
        // Add columns to table
        tableView.getColumns().addAll(nameColumn, ageColumn, emailColumn, activeColumn);
        
        // Set data
        tableView.setItems(data);
        
        // Create control buttons
        HBox buttonBox = new HBox(10);
        
        Button addButton = new Button("Add Person");
        addButton.setOnAction(e -> addPerson());
        
        Button removeButton = new Button("Remove Selected");
        removeButton.setOnAction(e -> removeSelectedPerson());
        
        Button showSelectionButton = new Button("Show Selection");
        showSelectionButton.setOnAction(e -> showSelectedPerson());
        
        Button clearSelectionButton = new Button("Clear Selection");
        clearSelectionButton.setOnAction(e -> tableView.getSelectionModel().clearSelection());
        
        Button sortByNameButton = new Button("Sort by Name");
        sortByNameButton.setOnAction(e -> {
            nameColumn.setSortType(TableColumn.SortType.ASCENDING);
            tableView.getSortOrder().clear();
            tableView.getSortOrder().add(nameColumn);
        });
        
        buttonBox.getChildren().addAll(addButton, removeButton, showSelectionButton, 
                                      clearSelectionButton, sortByNameButton);
        
        // Statistics label
        Label statsLabel = new Label();
        updateStatsLabel(statsLabel);
        
        // Listen for data changes to update statistics
        data.addListener((javafx.collections.ListChangeListener<Person>) change -> 
            updateStatsLabel(statsLabel));
        
        // Selection listener
        tableView.getSelectionModel().selectedItemProperty().addListener(
            (obs, oldSelection, newSelection) -> {
                if (newSelection != null) {
                    System.out.println("Selected: " + newSelection.getName());
                }
            });
        
        root.getChildren().addAll(
            new Label("TableView Demo - Double-click cells to edit"),
            tableView,
            buttonBox,
            new Separator(),
            statsLabel
        );
        
        Scene scene = new Scene(root, 600, 500);
        primaryStage.setTitle("JavaFX TableView Demo");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    private void addPerson() {
        // Create a dialog to get person details
        Dialog<Person> dialog = new Dialog<>();
        dialog.setTitle("Add New Person");
        dialog.setHeaderText("Enter person details:");
        
        // Create form fields
        TextField nameField = new TextField();
        nameField.setPromptText("Name");
        TextField ageField = new TextField();
        ageField.setPromptText("Age");
        TextField emailField = new TextField();
        emailField.setPromptText("Email");
        CheckBox activeCheckBox = new CheckBox("Active");
        activeCheckBox.setSelected(true);
        
        VBox form = new VBox(10);
        form.getChildren().addAll(
            new Label("Name:"), nameField,
            new Label("Age:"), ageField,
            new Label("Email:"), emailField,
            activeCheckBox
        );
        
        dialog.getDialogPane().setContent(form);
        dialog.getDialogPane().getButtonTypes().addAll(ButtonType.OK, ButtonType.CANCEL);
        
        dialog.setResultConverter(buttonType -> {
            if (buttonType == ButtonType.OK) {
                try {
                    String name = nameField.getText().trim();
                    int age = Integer.parseInt(ageField.getText().trim());
                    String email = emailField.getText().trim();
                    boolean active = activeCheckBox.isSelected();
                    
                    if (!name.isEmpty() && !email.isEmpty()) {
                        return new Person(name, age, email, active);
                    }
                } catch (NumberFormatException e) {
                    showAlert("Invalid age format");
                }
            }
            return null;
        });
        
        dialog.showAndWait().ifPresent(person -> {
            data.add(person);
            showAlert("Added: " + person.getName());
        });
    }
    
    private void removeSelectedPerson() {
        Person selected = tableView.getSelectionModel().getSelectedItem();
        if (selected != null) {
            data.remove(selected);
            showAlert("Removed: " + selected.getName());
        } else {
            showAlert("No person selected");
        }
    }
    
    private void showSelectedPerson() {
        Person selected = tableView.getSelectionModel().getSelectedItem();
        if (selected != null) {
            String info = String.format("Selected Person:\nName: %s\nAge: %d\nEmail: %s\nActive: %s",
                                      selected.getName(), selected.getAge(), 
                                      selected.getEmail(), selected.isActive());
            showAlert(info);
        } else {
            showAlert("No person selected");
        }
    }
    
    private void updateStatsLabel(Label statsLabel) {
        long activeCount = data.stream().mapToLong(p -> p.isActive() ? 1 : 0).sum();
        double averageAge = data.stream().mapToInt(Person::getAge).average().orElse(0);
        
        statsLabel.setText(String.format("Total: %d | Active: %d | Average Age: %.1f", 
                                        data.size(), activeCount, averageAge));
    }
    
    private void showAlert(String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Information");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# FXML and Scene Builder

FXML allows you to separate UI design from application logic.

## FXML Example

First, create an FXML file (LoginForm.fxml):

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.*?>
<?import javafx.scene.layout.*?>

<VBox xmlns="http://javafx.com/javafx/11.0.1" xmlns:fx="http://javafx.com/fxml/1" fx:controller="LoginController">
   <children>
      <Label text="Login Form" style="-fx-font-size: 18px; -fx-font-weight: bold;">
         <VBox.margin>
            <Insets bottom="20.0" />
         </VBox.margin>
      </Label>
      
      <GridPane hgap="10.0" vgap="10.0">
         <columnConstraints>
            <ColumnConstraints minWidth="80.0" />
            <ColumnConstraints hgrow="ALWAYS" />
         </columnConstraints>
         
         <children>
            <Label text="Username:" />
            <TextField fx:id="usernameField" promptText="Enter username" GridPane.columnIndex="1" />
            
            <Label text="Password:" GridPane.rowIndex="1" />
            <PasswordField fx:id="passwordField" promptText="Enter password" GridPane.columnIndex="1" GridPane.rowIndex="1" />
            
            <CheckBox fx:id="rememberMeCheckBox" text="Remember me" GridPane.columnIndex="1" GridPane.rowIndex="2" />
         </children>
         
         <VBox.margin>
            <Insets bottom="20.0" />
         </VBox.margin>
      </GridPane>
      
      <HBox spacing="10.0" alignment="CENTER">
         <children>
            <Button fx:id="loginButton" text="Login" onAction="#handleLogin" prefWidth="80.0" />
            <Button fx:id="cancelButton" text="Cancel" onAction="#handleCancel" prefWidth="80.0" />
         </children>
      </HBox>
      
      <Label fx:id="statusLabel" text="" style="-fx-text-fill: red;">
         <VBox.margin>
            <Insets top="10.0" />
         </VBox.margin>
      </Label>
   </children>
   
   <padding>
      <Insets bottom="30.0" left="30.0" right="30.0" top="30.0" />
   </padding>
</VBox>
```

Now, the controller class:

```java
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.event.ActionEvent;
import java.net.URL;
import java.util.ResourceBundle;

public class LoginController implements Initializable {
    
    @FXML
    private TextField usernameField;
    
    @FXML
    private PasswordField passwordField;
    
    @FXML
    private CheckBox rememberMeCheckBox;
    
    @FXML
    private Button loginButton;
    
    @FXML
    private Button cancelButton;
    
    @FXML
    private Label statusLabel;
    
    @Override
    public void initialize(URL location, ResourceBundle resources) {
        // Initialize the controller
        System.out.println("LoginController initialized");
        
        // Add listeners
        usernameField.textProperty().addListener((obs, oldText, newText) -> {
            clearStatus();
            updateLoginButtonState();
        });
        
        passwordField.textProperty().addListener((obs, oldText, newText) -> {
            clearStatus();
            updateLoginButtonState();
        });
        
        updateLoginButtonState();
    }
    
    @FXML
    private void handleLogin(ActionEvent event) {
        String username = usernameField.getText().trim();
        String password = passwordField.getText();
        boolean rememberMe = rememberMeCheckBox.isSelected();
        
        if (username.isEmpty() || password.isEmpty()) {
            showStatus("Please enter both username and password", "error");
            return;
        }
        
        // Simple validation (in real app, this would be more secure)
        if ("admin".equals(username) && "password".equals(password)) {
            showStatus("Login successful!", "success");
            System.out.println("Remember me: " + rememberMe);
            
            // Close the login window or navigate to main application
            loginButton.getScene().getWindow().hide();
        } else {
            showStatus("Invalid username or password", "error");
        }
    }
    
    @FXML
    private void handleCancel(ActionEvent event) {
        // Clear fields
        usernameField.clear();
        passwordField.clear();
        rememberMeCheckBox.setSelected(false);
        clearStatus();
        
        // Or close the window
        // cancelButton.getScene().getWindow().hide();
    }
    
    private void showStatus(String message, String type) {
        statusLabel.setText(message);
        if ("error".equals(type)) {
            statusLabel.setStyle("-fx-text-fill: red;");
        } else if ("success".equals(type)) {
            statusLabel.setStyle("-fx-text-fill: green;");
        }
    }
    
    private void clearStatus() {
        statusLabel.setText("");
    }
    
    private void updateLoginButtonState() {
        boolean isValid = !usernameField.getText().trim().isEmpty() && 
                         !passwordField.getText().isEmpty();
        loginButton.setDisable(!isValid);
    }
}
```

Main application class to load FXML:

```java
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class FXMLDemo extends Application {
    
    @Override
    public void start(Stage primaryStage) throws Exception {
        // Load FXML file
        FXMLLoader loader = new FXMLLoader(getClass().getResource("/LoginForm.fxml"));
        Parent root = loader.load();
        
        // Get controller if needed
        LoginController controller = loader.getController();
        
        Scene scene = new Scene(root);
        primaryStage.setTitle("FXML Login Demo");
        primaryStage.setScene(scene);
        primaryStage.setResizable(false);
        primaryStage.show();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Hands-on Exercise 1: Student Registration Form

Create a comprehensive student registration form using JavaFX:

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class StudentRegistrationForm extends Application {
    
    // TODO: Create a student registration form with the following fields:
    // - Personal Information: Name, Age, Gender (RadioButtons), Date of Birth (DatePicker)
    // - Contact Information: Email, Phone, Address (TextArea)
    // - Academic Information: Course (ComboBox), Year (ComboBox), GPA (Slider)
    // - Additional: Interests (CheckBoxes), Comments (TextArea)
    // - Buttons: Register, Clear, Cancel
    
    @Override
    public void start(Stage primaryStage) {
        // TODO: Implement the registration form
        // Use appropriate layout managers (GridPane recommended)
        // Add validation for required fields
        // Show confirmation dialog when registration is successful
        // Implement clear functionality to reset all fields
        
        primaryStage.setTitle("Student Registration Form");
        primaryStage.show();
    }
    
    // TODO: Add validation methods
    // TODO: Add event handlers for buttons
    // TODO: Add a method to collect and display form data
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Hands-on Exercise 2: Simple Calculator

Create a functional calculator application:

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class SimpleCalculator extends Application {
    
    // TODO: Create a calculator with:
    // - Display area (TextField, read-only)
    // - Number buttons (0-9)
    // - Operation buttons (+, -, *, /, =)
    // - Clear button (C), Clear All (CA)
    // - Decimal point button
    
    private TextField display;
    private double currentValue = 0;
    private String currentOperation = "";
    private boolean operationPressed = false;
    
    @Override
    public void start(Stage primaryStage) {
        // TODO: Create the calculator UI
        // Use GridPane for button layout
        // Style buttons for better appearance
        // Implement calculation logic
        
        primaryStage.setTitle("Simple Calculator");
        primaryStage.show();
    }
    
    // TODO: Implement button event handlers
    // TODO: Implement calculation logic
    // TODO: Handle edge cases (division by zero, etc.)
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Exercise Solutions: Student Registration Form

```java
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import java.time.LocalDate;

public class StudentRegistrationFormSolution extends Application {
    
    private TextField nameField;
    private Spinner<Integer> ageSpinner;
    private ToggleGroup genderGroup;
    private DatePicker dobPicker;
    private TextField emailField;
    private TextField phoneField;
    private TextArea addressArea;
    private ComboBox<String> courseCombo;
    private ComboBox<String> yearCombo;
    private Slider gpaSlider;
    private Label gpaLabel;
    private CheckBox sportsCheckBox;
    private CheckBox musicCheckBox;
    private CheckBox readingCheckBox;
    private TextArea commentsArea;
    
    @Override
    public void start(Stage primaryStage) {
        VBox root = new VBox(20);
        root.setPadding(new Insets(20));
        
        // Title
        Label titleLabel = new Label("Student Registration Form");
        titleLabel.setStyle("-fx-font-size: 20px; -fx-font-weight: bold;");
        
        // Create form sections
        VBox personalSection = createPersonalSection();
        VBox contactSection = createContactSection();
        VBox academicSection = createAcademicSection();
        VBox additionalSection = createAdditionalSection();
        HBox buttonSection = createButtonSection();
        
        root.getChildren().addAll(titleLabel, personalSection, contactSection, 
                                 academicSection, additionalSection, buttonSection);
        
        Scene scene = new Scene(new ScrollPane(root), 500, 700);
        primaryStage.setTitle("Student Registration");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    private VBox createPersonalSection() {
        VBox section = new VBox(10);
        section.getChildren().add(new Label("Personal Information:"));
        section.setStyle("-fx-border-color: lightgray; -fx-border-width: 1; -fx-padding: 10;");
        
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        
        // Name
        grid.add(new Label("Name:"), 0, 0);
        nameField = new TextField();
        grid.add(nameField, 1, 0);
        
        // Age
        grid.add(new Label("Age:"), 0, 1);
        ageSpinner = new Spinner<>(16, 100, 18);
        grid.add(ageSpinner, 1, 1);
        
        // Gender
        grid.add(new Label("Gender:"), 0, 2);
        genderGroup = new ToggleGroup();
        RadioButton maleRadio = new RadioButton("Male");
        RadioButton femaleRadio = new RadioButton("Female");
        maleRadio.setToggleGroup(genderGroup);
        femaleRadio.setToggleGroup(genderGroup);
        HBox genderBox = new HBox(10, maleRadio, femaleRadio);
        grid.add(genderBox, 1, 2);
        
        // Date of Birth
        grid.add(new Label("Date of Birth:"), 0, 3);
        dobPicker = new DatePicker();
        grid.add(dobPicker, 1, 3);
        
        section.getChildren().add(grid);
        return section;
    }
    
    private VBox createContactSection() {
        VBox section = new VBox(10);
        section.getChildren().add(new Label("Contact Information:"));
        section.setStyle("-fx-border-color: lightgray; -fx-border-width: 1; -fx-padding: 10;");
        
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        
        // Email
        grid.add(new Label("Email:"), 0, 0);
        emailField = new TextField();
        grid.add(emailField, 1, 0);
        
        // Phone
        grid.add(new Label("Phone:"), 0, 1);
        phoneField = new TextField();
        grid.add(phoneField, 1, 1);
        
        // Address
        grid.add(new Label("Address:"), 0, 2);
        addressArea = new TextArea();
        addressArea.setPrefRowCount(3);
        grid.add(addressArea, 1, 2);
        
        // Make second column grow
        ColumnConstraints col1 = new ColumnConstraints();
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHgrow(Priority.ALWAYS);
        grid.getColumnConstraints().addAll(col1, col2);
        
        section.getChildren().add(grid);
        return section;
    }
    
    private VBox createAcademicSection() {
        VBox section = new VBox(10);
        section.getChildren().add(new Label("Academic Information:"));
        section.setStyle("-fx-border-color: lightgray; -fx-border-width: 1; -fx-padding: 10;");
        
        GridPane grid = new GridPane();
        grid.setHgap(10);
        grid.setVgap(10);
        
        // Course
        grid.add(new Label("Course:"), 0, 0);
        courseCombo = new ComboBox<>();
        courseCombo.getItems().addAll("Computer Science", "Information Technology", 
                                     "Electronics", "Mechanical", "Civil");
        grid.add(courseCombo, 1, 0);
        
        // Year
        grid.add(new Label("Year:"), 0, 1);
        yearCombo = new ComboBox<>();
        yearCombo.getItems().addAll("1st Year", "2nd Year", "3rd Year");
        grid.add(yearCombo, 1, 1);
        
        // GPA
        grid.add(new Label("GPA:"), 0, 2);
        gpaSlider = new Slider(0, 10, 7);
        gpaSlider.setShowTickLabels(true);
        gpaSlider.setShowTickMarks(true);
        gpaSlider.setMajorTickUnit(2);
        gpaLabel = new Label("7.0");
        gpaSlider.valueProperty().addListener((obs, oldVal, newVal) -> 
            gpaLabel.setText(String.format("%.1f", newVal.doubleValue())));
        
        VBox gpaBox = new VBox(5, gpaSlider, gpaLabel);
        grid.add(gpaBox, 1, 2);
        
        ColumnConstraints col1 = new ColumnConstraints();
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHgrow(Priority.ALWAYS);
        grid.getColumnConstraints().addAll(col1, col2);
        
        section.getChildren().add(grid);
        return section;
    }
    
    private VBox createAdditionalSection() {
        VBox section = new VBox(10);
        section.getChildren().add(new Label("Additional Information:"));
        section.setStyle("-fx-border-color: lightgray; -fx-border-width: 1; -fx-padding: 10;");
        
        // Interests
        Label interestsLabel = new Label("Interests:");
        sportsCheckBox = new CheckBox("Sports");
        musicCheckBox = new CheckBox("Music");
        readingCheckBox = new CheckBox("Reading");
        HBox interestsBox = new HBox(10, sportsCheckBox, musicCheckBox, readingCheckBox);
        
        // Comments
        Label commentsLabel = new Label("Comments:");
        commentsArea = new TextArea();
        commentsArea.setPrefRowCount(3);
        commentsArea.setPromptText("Any additional information...");
        
        section.getChildren().addAll(interestsLabel, interestsBox, commentsLabel, commentsArea);
        return section;
    }
    
    private HBox createButtonSection() {
        HBox buttonBox = new HBox(10);
        buttonBox.setStyle("-fx-alignment: center;");
        
        Button registerButton = new Button("Register");
        registerButton.setOnAction(e -> handleRegister());
        
        Button clearButton = new Button("Clear");
        clearButton.setOnAction(e -> handleClear());
        
        Button cancelButton = new Button("Cancel");
        cancelButton.setOnAction(e -> handleCancel());
        
        buttonBox.getChildren().addAll(registerButton, clearButton, cancelButton);
        return buttonBox;
    }
    
    private void handleRegister() {
        if (!validateForm()) {
            return;
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append("Registration Successful!\n\n");
        sb.append("Name: ").append(nameField.getText()).append("\n");
        sb.append("Age: ").append(ageSpinner.getValue()).append("\n");
        
        RadioButton selectedGender = (RadioButton) genderGroup.getSelectedToggle();
        if (selectedGender != null) {
            sb.append("Gender: ").append(selectedGender.getText()).append("\n");
        }
        
        if (dobPicker.getValue() != null) {
            sb.append("Date of Birth: ").append(dobPicker.getValue()).append("\n");
        }
        
        sb.append("Email: ").append(emailField.getText()).append("\n");
        sb.append("Phone: ").append(phoneField.getText()).append("\n");
        sb.append("Course: ").append(courseCombo.getValue()).append("\n");
        sb.append("Year: ").append(yearCombo.getValue()).append("\n");
        sb.append("GPA: ").append(String.format("%.1f", gpaSlider.getValue())).append("\n");
        
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Registration Successful");
        alert.setHeaderText("Student Registered");
        alert.setContentText(sb.toString());
        alert.showAndWait();
    }
    
    private boolean validateForm() {
        if (nameField.getText().trim().isEmpty()) {
            showError("Name is required");
            return false;
        }
        
        if (emailField.getText().trim().isEmpty()) {
            showError("Email is required");
            return false;
        }
        
        if (courseCombo.getValue() == null) {
            showError("Please select a course");
            return false;
        }
        
        if (yearCombo.getValue() == null) {
            showError("Please select a year");
            return false;
        }
        
        return true;
    }
    
    private void showError(String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Validation Error");
        alert.setHeaderText("Please correct the following error:");
        alert.setContentText(message);
        alert.showAndWait();
    }
    
    private void handleClear() {
        nameField.clear();
        ageSpinner.getValueFactory().setValue(18);
        genderGroup.selectToggle(null);
        dobPicker.setValue(null);
        emailField.clear();
        phoneField.clear();
        addressArea.clear();
        courseCombo.setValue(null);
        yearCombo.setValue(null);
        gpaSlider.setValue(7);
        sportsCheckBox.setSelected(false);
        musicCheckBox.setSelected(false);
        readingCheckBox.setSelected(false);
        commentsArea.clear();
    }
    
    private void handleCancel() {
        Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
        alert.setTitle("Confirm Exit");
        alert.setHeaderText("Are you sure you want to exit?");
        alert.setContentText("All unsaved data will be lost.");
        
        alert.showAndWait().ifPresent(response -> {
            if (response == ButtonType.OK) {
                System.exit(0);
            }
        });
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
```

---

# Summary

## Key Concepts Covered

1. **JavaFX Architecture**: Stage, Scene, Scene Graph, and Nodes
2. **Application Structure**: Application lifecycle and proper initialization
3. **UI Controls**: Buttons, text fields, lists, tables, and specialized controls
4. **Layout Managers**: VBox, HBox, BorderPane, GridPane, StackPane, FlowPane
5. **Event Handling**: Action events, mouse events, key events, and property listeners
6. **CSS Styling**: Inline styles and external stylesheets
7. **Data Binding**: TableView with observable properties
8. **FXML**: Separating UI design from application logic

## Benefits of JavaFX

- **Modern UI**: Rich, responsive user interfaces
- **CSS Styling**: Web-like styling capabilities
- **Data Binding**: Automatic UI updates with property changes
- **FXML Support**: Designer-developer workflow separation
- **Cross-platform**: Runs on Windows, macOS, and Linux

## Best Practices

- Use appropriate layout managers for responsive design
- Separate UI logic from business logic
- Use data binding for dynamic UI updates
- Apply consistent styling throughout the application
- Handle user input validation properly
- Use FXML for complex UI designs

---

# Next Lecture Preview

## Lecture 42: Final Review and Project Integration

- Review of all major Java concepts covered
- Best practices for Java development
- Project planning and architecture
- Integration of different Java technologies
- Preparation for real-world development
- Career guidance and next steps

## Preparation

- Review previous lectures and practice exercises
- Think about potential project ideas
- Prepare questions about Java development practices

---

# Thank You!

## Questions and Discussion

- How does JavaFX compare to other UI frameworks you've used?
- What are the advantages of using FXML vs pure Java code for UI design?
- How can you make JavaFX applications more responsive and user-friendly?

## Resources for Further Learning

- Oracle JavaFX Documentation
- JavaFX Scene Builder for visual UI design
- OpenJFX community and resources
- Practice building complete desktop applications

**Next: Final Review and Project Integration**