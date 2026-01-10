---
theme: default
title: Generic Slide Template for AI Generation
info: |
  ## Generic Slide Template for AI Generation
  
  Use this template structure when generating slides from timestamped transcripts.
  
  CRITICAL RULES:
  1. Number of v-click attributes MUST equal number of [click] markers in speaker notes
  2. First statement in speaker notes has NO [click] marker (visible when slide appears)
  3. Each subsequent [click] corresponds to next v-click number in sequence
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# [EXTRACT MAIN TOPIC FROM TRANSCRIPT]
## [EXTRACT SUBTITLE FROM FIRST SPEAKER STATEMENTS]

**[EXTRACT KEY DESCRIPTIVE PHRASES]**  
[Use bullet points or descriptive text from opening dialogue]

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
[FIRST SPEAKER STATEMENT - NO [click] MARKER]: [Extract opening statement that introduces the topic]

[MORE SPEAKER DIALOGUE WITHOUT [click] IF NEEDED]: [Additional context or setup statements]

[FINAL SPEAKER STATEMENT BEFORE SLIDE TRANSITION]: [Last statement that leads to next slide]
-->

---
layout: default
---

# [EXTRACT SLIDE TITLE FROM TRANSCRIPT]

## Layout Option 1: Two-Column Grid

<div class="grid grid-cols-2 gap-8">

<div>

## [ICON] **[EXTRACT SECTION TITLE]**

<v-click at="1">

- **[EXTRACT KEY POINT 1]**
- [EXTRACT KEY POINT 2]
- [EXTRACT KEY POINT 3]

</v-click>

</div>

<div>

## [ICON] **[EXTRACT SECTION TITLE]**

<v-click at="2">

**"[EXTRACT MEMORABLE QUOTE FROM TRANSCRIPT]"**

- [EXTRACT SUPPORTING POINT 1]
- [EXTRACT SUPPORTING POINT 2]
- [EXTRACT SUPPORTING POINT 3]

</v-click>

</div>

</div>

<div v-click="3" class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
<strong>[ICON] [EXTRACT INSIGHT TYPE]:</strong> [EXTRACT KEY TAKEAWAY FROM DIALOGUE]
</div>

<!--
[FIRST SPEAKER STATEMENT - NO [click] MARKER]: [Extract statement that introduces this slide's content]

[click] [SPEAKER NAME]: [Extract dialogue that corresponds to v-click="1" content]

[click] [SPEAKER NAME]: [Extract dialogue that corresponds to v-click="2" content]

[click] [SPEAKER NAME]: [Extract dialogue that corresponds to v-click="3" content]

[OPTIONAL CLOSING STATEMENT WITHOUT [click]]: [Transition to next topic if present]
-->

---
layout: default
---

# [EXTRACT SLIDE TITLE]

## Layout Option 2: Three-Column Grid with Cards

<div class="grid grid-cols-3 gap-6">

<div v-click="1" class="bg-gradient-to-br from-blue-50 to-blue-100 p-6 rounded-xl">

## [ICON] **[EXTRACT POINT 1 TITLE]**

- **[EXTRACT KEY DETAIL]**
- [EXTRACT SUPPORTING DETAIL]
- [EXTRACT ADDITIONAL DETAIL]

</div>

<div v-click="2" class="bg-gradient-to-br from-green-50 to-green-100 p-6 rounded-xl">

## [ICON] **[EXTRACT POINT 2 TITLE]**

- [EXTRACT KEY DETAIL]
- **[EXTRACT EMPHASIZED DETAIL]**
- [EXTRACT EXAMPLE OR ANALOGY]
- **[EXTRACT STRONG POINT]**

</div>

<div v-click="3" class="bg-gradient-to-br from-purple-50 to-purple-100 p-6 rounded-xl">

## [ICON] **[EXTRACT POINT 3 TITLE]**

- [EXTRACT BENEFIT 1]
- [EXTRACT BENEFIT 2]
- **[EXTRACT MEMORABLE PHRASE]**

</div>

</div>

<div v-click="4" class="mt-8 p-4 bg-gradient-to-r from-indigo-50 to-cyan-50 rounded-lg">
<strong>[ICON] [EXTRACT SUMMARY TYPE]:</strong> [EXTRACT CLOSING INSIGHT OR MNEMONIC]
</div>

<!--
[FIRST SPEAKER STATEMENT - NO [click] MARKER]: [Extract opening context for this slide]

[click] [SPEAKER NAME]: [Extract dialogue for first point - corresponds to v-click="1"]

[click] [SPEAKER NAME]: [Extract dialogue for second point - corresponds to v-click="2"]

[click] [SPEAKER NAME]: [Extract dialogue for third point - corresponds to v-click="3"]

[click] [SPEAKER NAME]: [Extract dialogue for summary/closing - corresponds to v-click="4"]
-->

---
layout: center
class: text-center
---

# [EXTRACT SLIDE TITLE]

## Layout Option 3: Center Layout with Side-by-Side Content

<div class="grid grid-cols-2 gap-12 mt-8">

<div class="text-left">

## [ICON] **[EXTRACT SECTION TITLE]**

<v-click at="1">

- **[EXTRACT KEY POINT]**
- [EXTRACT DETAIL]
- [EXTRACT EXAMPLE]
- [EXTRACT ADDITIONAL INFO]

</v-click>

</div>

<div class="text-left">

## [ICON] **[EXTRACT SECTION TITLE]**

<v-click at="2">

- **[EXTRACT DIFFERENT ASPECT]**
- [EXTRACT COMPARISON]
- [EXTRACT METAPHOR OR ANALOGY]
- **[EXTRACT KEY INSIGHT]**

</v-click>

</div>

</div>

<div v-click="3" class="mt-12 text-2xl font-bold text-blue-600">
"[EXTRACT MEMORABLE QUOTE FROM TRANSCRIPT]"
</div>

<!--
[click] [SPEAKER NAME]: [Extract dialogue for first section - corresponds to v-click="1"]

[click] [SPEAKER NAME]: [Extract dialogue for second section - corresponds to v-click="2"]

[click] [SPEAKER NAME]: [Extract memorable quote or key insight - corresponds to v-click="3"]

[OPTIONAL CLOSING]: [Transition statement]
-->

---
layout: center
class: text-center
---

# [EXTRACT SLIDE TITLE]: [EXTRACT SPECIFIC EXAMPLE]

## Layout Option 4: Visual Flow/Process Diagram

<div class="mt-8">

<div class="flex justify-center items-center space-x-4">

<div v-click="1" class="bg-green-100 p-4 rounded-full">
<strong>[EXTRACT STEP 1]</strong>
</div>

<div v-click="1" class="text-2xl">→</div>

<div v-click="2" class="bg-blue-100 p-4 rounded-lg">
<strong>[EXTRACT STEP 2]</strong><br/>
<code class="text-sm">[EXTRACT DETAIL/CODE]</code><br/>
([EXTRACT EXPLANATION])
</div>

<div v-click="2" class="text-2xl">→</div>

<div v-click="3" class="bg-purple-100 p-4 rounded-lg">
<strong>[EXTRACT STEP 3]</strong><br/>
<code class="text-sm">[EXTRACT FORMULA/PROCESS]</code>
</div>

</div>

<div class="flex justify-center items-center space-x-4 mt-6">

<div v-click="3" class="text-2xl">→</div>

<div v-click="4" class="bg-yellow-100 p-4 rounded-lg">
<strong>[EXTRACT STEP 4]</strong><br/>
<code class="text-sm">[EXTRACT OUTPUT]</code>
</div>

<div v-click="4" class="text-2xl">→</div>

<div v-click="5" class="bg-red-100 p-4 rounded-full">
<strong>[EXTRACT FINAL STEP]</strong>
</div>

</div>

</div>

<div v-click="6" class="mt-8 text-lg text-blue-600">
**"[EXTRACT SUMMARY QUOTE FROM DIALOGUE]"**
</div>

<!--
[click] [SPEAKER NAME]: [Extract dialogue for first step - corresponds to v-click="1"]

[click] [SPEAKER NAME]: [Extract dialogue for second step - corresponds to v-click="2"]

[click] [SPEAKER NAME]: [Extract dialogue for third step - corresponds to v-click="3"]

[click] [SPEAKER NAME]: [Extract dialogue for fourth step - corresponds to v-click="4"]

[click] [SPEAKER NAME]: [Extract dialogue for final step - corresponds to v-click="5"]

[click] [SPEAKER NAME]: [Extract summary or closing statement - corresponds to v-click="6"]
-->

---
layout: default
---

# [EXTRACT SLIDE TITLE]

## Layout Option 5: Code Example with Explanation

<div class="grid grid-cols-2 gap-8">

<div>

## [ICON] **[EXTRACT CONCEPT TITLE]**

<v-click at="1">

- [EXTRACT EXPLANATION 1]
- [EXTRACT EXPLANATION 2]
- [EXTRACT KEY BENEFIT]
- [EXTRACT USE CASE]

</v-click>

</div>

<div>

## [ICON] **[EXTRACT PRACTICAL TITLE]**

<v-click at="2">

- **[EXTRACT PRACTICAL BENEFIT]**
- [EXTRACT WHEN TO USE]
- [EXTRACT COMPARISON]
- [EXTRACT EFFICIENCY NOTE]

</v-click>

</div>

</div>

<div v-click="3" class="mt-8">

## [ICON] **[EXTRACT EXAMPLE TITLE]**

<div class="bg-gray-100 p-4 rounded-lg font-mono">
<div>[EXTRACT COMPARISON TEXT]: <code>[EXTRACT CODE EXAMPLE 1]</code></div>
<div>[EXTRACT BETTER WAY TEXT]: <code>[EXTRACT CODE EXAMPLE 2]</code></div>
</div>

</div>

<!--
[FIRST SPEAKER STATEMENT]: [Extract introductory context]

[click] [SPEAKER NAME]: [Extract explanation corresponding to first section - v-click="1"]

[click] [SPEAKER NAME]: [Extract practical application info - v-click="2"]

[OPTIONAL FINAL STATEMENT]: [Wrap up or transition]
-->

---
layout: center
class: text-center
---

# [EXTRACT SUMMARY TITLE]

## Layout Option 6: Summary/Conclusion Slide

<div class="grid grid-cols-2 gap-12 mt-8">

<div class="text-left">

## [ICON] **[EXTRACT SUMMARY SECTION 1]**

<v-click at="1">- **[EXTRACT TOPIC 1]**: [EXTRACT DESCRIPTION]</v-click>
<v-click at="2">- **[EXTRACT TOPIC 2]**: [EXTRACT DESCRIPTION]</v-click>
<v-click at="3">- **[EXTRACT TOPIC 3]**: [EXTRACT DESCRIPTION]</v-click>
<v-click at="4">- **[EXTRACT TOPIC 4]**: [EXTRACT DESCRIPTION]</v-click>

</div>

<div class="text-left">

## [ICON] **[EXTRACT SUMMARY SECTION 2]**

<v-click at="5">- **[EXTRACT INSIGHT 1]** [EXTRACT DETAILS]</v-click>
<v-click at="6">- **[EXTRACT INSIGHT 2]** [EXTRACT DETAILS]</v-click>
<v-click at="7">- **[EXTRACT INSIGHT 3]** [EXTRACT DETAILS]</v-click>
<v-click at="8">- **[EXTRACT INSIGHT 4]** [EXTRACT DETAILS]</v-click>

</div>

</div>

<!-- Final statement doesn't have [click] marker, so no v-click needed -->
<div class="mt-12">

## [ICON] **[EXTRACT CONCLUSION TITLE]**

<div class="text-xl text-blue-600">
**[EXTRACT FINAL ENCOURAGING STATEMENT]**
</div>

</div>

<!--
[click] [SPEAKER NAME]: [Extract first summary point - v-click="1"]

[click] [SPEAKER NAME]: [Extract second summary point - v-click="2"]

[click] [SPEAKER NAME]: [Extract third summary point - v-click="3"]

[click] [SPEAKER NAME]: [Extract fourth summary point - v-click="4"]

[click] [SPEAKER NAME]: [Extract first insight - v-click="5"]

[click] [SPEAKER NAME]: [Extract second insight - v-click="6"]

[click] [SPEAKER NAME]: [Extract third insight - v-click="7"]

[click] [SPEAKER NAME]: [Extract fourth insight - v-click="8"]

[SPEAKER NAME]: [Extract final statement without [click] - no v-click needed]
-->