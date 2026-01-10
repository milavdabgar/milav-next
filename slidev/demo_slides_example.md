---
theme: default
title: Python Programming Fundamentals Demo
info: |
  ## Demo Slides Example
  
  This is a practical example showing how to use the generic slide template
  for AI generation. These slides demonstrate perfect v-click synchronization
  with speaker notes [click] markers.
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Python Programming Fundamentals
## The Deep Dive

**Exploring Core Concepts & Building Blocks**  
Algorithms • Flow Charts • Operators • Data Types

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
Dr. James: Welcome to the Deep Dive. We're here to pull out the key info you need from different sources. That's right. And today we're looking at a summer 2023 exam solution guide. It's all about the basics of Python programming.

Sarah: Yep, the fundamentals.

Dr. James: So whether this is maybe your first time seeing this stuff or you need a refresher, or maybe you just want things clear before you actually start coding, our aim is to, you know, make these technical ideas understandable, maybe even interesting. Hopefully.

Sarah: And this guide, it hits definitions, rules, code examples, pretty comprehensive for fundamentals.
-->

---
layout: default
---

# What is an Algorithm?

<div class="grid grid-cols-2 gap-8">

<div>

## 🧠 **Core Definition**

<v-click at="1">

- **Step-by-step procedure**
- Solves problems in **finite sequence**

</v-click>

</div>

<div v-click at="2">

## 💡 **Recipe Analogy**

**"Like a recipe. Exactly like a recipe!"**

- Clear, unambiguous steps
- Finite and well-defined
- Set of **instructions** → **specific result**

</div>

</div>

<div v-click="3" class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
<strong>🎯 Remember:</strong> Algorithms are the logic behind pretty much all software!
</div>

<!--
Dr. James: Okay, let's dive in. First concept, algorithms. Sounds maybe a bit formal, but what is an algorithm really?

[click] Sarah: Well, at its heart, it's just a step-by-step procedure. It's a way to solve a problem in a specific finite sequence of steps.

[click] Sarah: Like a recipe. Exactly like a recipe. That's a great analogy. For computers, it's the set of instructions to get a certain result.

[click] Sarah: And honestly, algorithms are the logic behind pretty much all software.

Dr. James: Makes sense. And then
-->

---
layout: default
---

# Algorithm Advantages: C-E-R-V-C

<div class="grid grid-cols-3 gap-6">

<div v-click="1" class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl">

## 🎯 **C - Clarity**

- **Totally unambiguous** instructions
- No confusion for programmer/machine
- Crystal clear steps

</div>

<div v-click="2" class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl">

## ⚡ **E - Efficiency**

- Smart **resource usage**
- Optimized **time & memory**
- Think: sorting huge data sets
- **Speed matters!**

</div>

<div v-click="3" class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl">

## 🔄 **R - Reusability**

- Build once, **adapt later**
- Reuse parts for similar problems
- **Saves a lot of work**

</div>

</div>

<!--
Dr. James: And the material gives this mnemonic, C or VC, to remember the advantages. What's that about?

Sarah: Ah, yes.

Sarah: C or ER or VC.

Sarah: Okay, so C is for clarity.

[click] Sarah: Let's start with C - for clarity. The instructions need to be totally unambiguous. No confusion for the programmer or the machine.

[click] Sarah: Right. E is efficiency. Good algorithms, they try to use resources, well, time, memory. Think about sorting huge amounts of data. Yeah, you want that fast. Exactly. Efficiency matters.

[click] Sarah: R is reusability. Often, you build an algorithm for one thing, but you can adapt it or reuse parts for similar problems later. Saves a lot of work.
-->

---
layout: center
class: text-center
---

# Flow Charts: Visual Algorithms

<div class="grid grid-cols-2 gap-12 mt-8">

<div class="text-left">

## 🎨 **What Are Flow Charts?**

<v-click at="1">

- **Visual algorithms**
- Standard symbols + arrows
- Show **sequence & decisions**
- Display **flow of logic**

</v-click>

</div>

<div class="text-left">

## 💡 **Why Use Them?**

<v-click at="2">

- **Much more graphical**
- Grasp **overall structure quickly**
- Like looking at a **map** instead of reading directions
- **Visual thinking**

</v-click>

</div>

</div>

<div v-click="3" class="mt-12 text-2xl font-bold text-blue-600">
"Sometimes easier to grasp the overall structure quickly" 
</div>

<!--
[click] Sarah: Flow charts are basically visual algorithms. Instead of just text, you use standard symbols and arrows to show the sequence, the decisions, the flow of logic.

[click] Dr. James: More graphical.

[click] Sarah: Yeah, much more graphical. Sometimes easier to grasp the overall structure quickly, like looking at a map instead of reading directions.

Sarah: Got it.
-->

---
layout: center
class: text-center
---

# Flow Chart Example: Simple Interest

<div class="mt-8">

<div class="flex justify-center items-center space-x-4">

<div v-click="1" class="bg-green-100 p-4 rounded-full">
<strong>START</strong>
</div>

<div v-click="1" class="text-2xl">→</div>

<div v-click="2" class="bg-blue-100 p-4 rounded-lg">
<strong>Input</strong><br/>
<code class="text-sm">P, R, T</code><br/>
(Principal, Rate, Time)
</div>

<div v-click="2" class="text-2xl">→</div>

<div v-click="3" class="bg-purple-100 p-4 rounded-lg">
<strong>Process</strong><br/>
<code class="text-sm">SI = P×R×T/100</code>
</div>

</div>

<div class="flex justify-center items-center space-x-4 mt-6">

<div v-click="3" class="text-2xl">→</div>

<div v-click="4" class="bg-yellow-100 p-4 rounded-lg">
<strong>Output</strong><br/>
<code class="text-sm">Display SI</code>
</div>

<div v-click="4" class="text-2xl">→</div>

<div v-click="5" class="bg-red-100 p-4 rounded-full">
<strong>END</strong>
</div>

</div>

</div>

<div v-click="6" class="mt-8 text-lg text-blue-600">
**"Very clear path: Get numbers → Do math → Show answer"**
</div>

<!--
[click] Sarah: So you'd start with a start oval, then an arrow to a parallelogram, input PRT, principal rate time.

Dr. James: The inputs.

Dr. James: Right.

[click] Sarah: Then an arrow to a rectangle for the calculation. SI equals PRT 100. That's the process.

Dr. James: The formula.

Sarah: Yep.

[click] Dr. James: Arrow again to another parallelogram, output SI, show the result.

[click] Dr. James: And finally, an arrow to an end oval.

Sarah: So if I wanted to figure out interest on, say, a quick loan.

[click] Dr. James: Exactly. It maps out those exact steps, get the numbers, do the math, show the answer. Very clear.
-->

---
layout: default
---

# Python Assignment Operators

<div class="grid grid-cols-2 gap-8">

<div>

## 📝 **What Are They?**

<v-click at="1">

- How you **give values** to variables
- Basic one: **equal sign** (`=`)
- Python has **shorthand operators**
- Combine **math + assignment**

</v-click>

</div>

<div>

## 💡 **Why Use Them?**

<v-click at="2">

- **Shortcuts** for common operations
- Make code **shorter**
- Often **easier to read**
- Especially when **updating same variable**

</v-click>

</div>

</div>

<div v-click="3" class="mt-8">

## 🔧 **Example**

<div class="bg-gray-100 p-4 rounded-lg font-mono">
<div>Instead of: <code>x = x + 5</code></div>
<div>You can write: <code>x += 5</code></div>
</div>

</div>

<!--
Sarah: Okay. Solid foundation for problem solving. Let's shift into Python itself. Assignment operators. What are these?

[click] Dr. James: Assignment operators are how you give values to variables in Python. The basic one is just the equal sign. Simple enough.

[click] Dr. James: But Python has these shorthand operators too. Like instead of XX plus 5, you can just write X plus up to 5. Combines the math and the assignment. Ah, shortcuts.

Yeah. They make code shorter, often a bit easier to read, especially if you're updating the same variable a lot.
-->

---
layout: center
class: text-center
---

# Summary: Python Fundamentals Mastered

<div class="grid grid-cols-2 gap-12 mt-8">

<div class="text-left">

## 🎯 **What We Covered**

<v-click at="1">- **Algorithms**: Step-by-step procedures</v-click>
<v-click at="2">- **Flow Charts**: Visual problem solving</v-click>
<v-click at="3">- **Assignment Operators**: Efficient coding</v-click>
<v-click at="4">- **Data Types**: Foundation of variables</v-click>

</div>

<div class="text-left">

## 💡 **Key Insights**

<v-click at="5">- **Planning first** is crucial</v-click>
<v-click at="6">- **Visual thinking** helps understanding</v-click>
<v-click at="7">- **Efficiency matters** in code</v-click>
<v-click at="8">- **Types are fundamental** even when dynamic</v-click>

</div>

</div>

<!-- Final statement doesn't have [click] marker, so no v-click needed -->
<div class="mt-12">

## 🚀 **Ready for Next Steps**

<div class="text-xl text-blue-600">
**You now have solid foundations for Python programming!**
</div>

</div>

<!--
[click] Dr. James: So let's wrap up what we've covered today. Algorithms as step-by-step procedures.

[click] Sarah: Flow charts for visual problem solving.

[click] Dr. James: Assignment operators for efficient coding.

[click] Sarah: And data types as the foundation of variables.

[click] Dr. James: Planning first is crucial.

[click] Sarah: Visual thinking helps understanding.

[click] Dr. James: Efficiency matters in code.

[click] Sarah: And types are fundamental, even when dynamic.

Dr. James: These concepts give you solid foundations for Python programming! You're ready for the next steps.
-->