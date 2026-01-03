---
author:
- Milav Dabgar
date: Month Day, Year
title: Subject Name (SUBJECT001) - Sample Term Solution
---

# Question 1(a) \[3 marks\] {#question-1a-3-marks .unnumbered}

**Write a Java program to find the maximum of three numbers.**

::: solutionbox
To find the **maximum** of three numbers, we use **conditional
statements** (if-else) to compare values. The program takes three
numbers as input and returns the "largest value" among them.

#### Java Program:

``` {.java language="Java" caption="Find Maximum of Three Numbers"}
public class MaxOfThree {
    public static void main(String[] args) {
        int a = 25, b = 40, c = 15;
        int max;
        
        // Compare first two numbers
        if (a > b) {
            max = a;
        } else {
            max = b;
        }
        
        // Compare result with third number
        if (c > max) {
            max = c;
        }
        
        System.out.println("Maximum number is: " + max);
    }
}
```

#### Output:

    Maximum number is: 40

#### Key Points:

- **Logic**: First compare `a` and `b`, store larger in `max`

- **Second Comparison**: Compare `max` with `c` to get final maximum

- **Alternative**: Can use `Math.max(a, Math.max(b, c))` for concise
  code
:::

::: mnemonicbox
["MAX: Compare in pairs, update Maximum At
eXamination"]{style="color: mnemoniccolor"}
:::

# Question 1(b) \[4 marks\] {#question-1b-4-marks .unnumbered}

**Calculate the cutoff frequency of an RC low-pass filter with
$R = 1.5\,k\Omega$ and $C = 100\,nF$. Also find the output voltage if
input is 10V at cutoff frequency.**

::: solutionbox
#### Given Data:

- Resistance: $R = 1.5\,k\Omega = 1500\,\Omega$

- Capacitance: $C = 100\,nF = 100 \times 10^{-9}\,F$

- Input Voltage: $V_{in} = 10\,V$

#### Step 1: Calculate Cutoff Frequency

The **cutoff frequency** formula for RC low-pass filter is:
$$f_c = \frac{1}{2\pi RC}$$

Substituting values:
$$f_c = \frac{1}{2\pi \times 1500 \times 100 \times 10^{-9}}$$
$$f_c = \frac{1}{2\pi \times 1.5 \times 10^{-4}}$$
$$f_c = \frac{1}{9.42 \times 10^{-4}} = 1061.57\,Hz \approx 1.06\,kHz$$

#### Step 2: Calculate Output Voltage at Cutoff

At cutoff frequency, output voltage is **0.707 times** (or
$\frac{1}{\sqrt{2}}$) the input voltage:
$$V_{out} = 0.707 \times V_{in} = 0.707 \times 10 = 7.07\,V$$

#### Results:

- **Cutoff Frequency**: $f_c = 1.06\,kHz$

- **Output Voltage**: $V_{out} = 7.07\,V$ at cutoff

- **Attenuation**: $-3\,dB$ at cutoff frequency

- **Phase Shift**: $-45^\circ$ at cutoff frequency
:::

::: mnemonicbox
["RC-Formula: fc = 1/(2$\pi$ RC), Vout = 0.707 Vin at
fc"]{style="color: mnemoniccolor"}
:::

# Question 1(c) \[7 marks\] {#question-1c-7-marks .unnumbered}

**Compare active and passive electronic components with suitable
examples.**

::: solutionbox
Electronic components are classified into **active** and **passive**
categories based on their ability to control or amplify electrical
energy.

  **Characteristic**   **Active Components**                                                 **Passive Components**
  -------------------- --------------------------------------------------------------------- ------------------------------------------------
  Energy Source        Require external power source                                         Do not require external power
  Control Ability      Can control/amplify current flow                                      Cannot amplify, only regulate
  Directionality       Usually unidirectional                                                Bidirectional
  Power Gain           Provide power gain ($>1$)                                             Power gain is always $\leq 1$
  Examples             Transistors (BJT, FET), Diodes (LED, Zener), ICs (Op-Amp, 555), SCR   Resistors, Capacitors, Inductors, Transformers
  Function             Amplification, switching, oscillation, rectification                  Resistance, capacitance, inductance, filtering
  Linearity            Can be linear or non-linear                                           Generally linear

  : Active vs Passive Components Comparison

#### Active Components in Detail:

- **Transistors**: Used for amplification and switching. BJT uses
  current control, FET uses voltage control.

- **Diodes**: Allow current in one direction. LED emits light, Zener
  regulates voltage.

- **ICs**: Integrated circuits like `555 timer` (oscillator), op-amps
  (amplifier).

- **Power Requirement**: All active components need DC bias/supply to
  operate.

#### Passive Components in Detail:

- **Resistors**: Oppose current flow, dissipate power as heat. Value in
  $\Omega$.

- **Capacitors**: Store energy in electric field. Value in Farads (F),
  blocks DC, passes AC.

- **Inductors**: Store energy in magnetic field. Value in Henry (H),
  opposes AC changes.

- **Transformers**: Transfer energy between circuits via magnetic
  coupling.

#### Key Distinction:

The fundamental difference is that active components can "inject power"
into a circuit (amplification), while passive components can only
"absorb or store" energy, never increase it.
:::

::: mnemonicbox
["ACTIVE = Amplify, Control, Transform; PASSIVE = Resist, Store,
Filter"]{style="color: mnemoniccolor"}
:::

# Question 1(c OR) \[7 marks\] {#question-1c-or-7-marks .unnumbered}

**Draw and explain the working of a half-wave rectifier circuit with
input and output waveforms.**

::: solutionbox
A **half-wave rectifier** converts AC voltage to pulsating DC by
allowing only one half-cycle (positive or negative) of the input AC
waveform to pass through.

#### Circuit Diagram:

<figure data-latex-placement="H">
<div class="circuitikz">
<p>(0,0) to[sV, l=<span
class="math inline"><em>V</em><sub><em>i</em><em>n</em></sub></span>]
(0,2); (0,2) to[short] (2,2);</p>
<p>(2,2) to[D*, l=<span class="math inline"><em>D</em></span>]
(4,2);</p>
<p>(4,2) to[short] (5,2); (5,2) to[R, l=<span
class="math inline"><em>R</em><sub><em>L</em></sub></span>] (5,0); (5,0)
to[short] (0,0);</p>
<p>(4.5,2) to[short, *-] (4.5,2.5); at (4.5,2.7) <span><span
class="math inline"><em>V</em><sub><em>o</em><em>u</em><em>t</em></sub></span></span>;
(4.5,0) to[short, *-] (4.5,-0.5); at (4.5,-0.5) ;</p>
</div>
<figcaption>Half-Wave Rectifier Circuit</figcaption>
</figure>

#### Working Principle:

1.  **Positive Half-Cycle**: When input AC is positive, diode is
    forward-biased (conducts). Current flows through load resistor
    $R_L$, producing output voltage.

2.  **Negative Half-Cycle**: When input AC is negative, diode is
    reverse-biased (blocks). No current flows, output voltage is zero.

3.  **Result**: Only positive half-cycles appear at output, creating
    pulsating DC.

#### Waveform Representation:

<figure data-latex-placement="H">

<figcaption>Input and Output Waveforms</figcaption>
</figure>

#### Key Parameters:

- **Efficiency**: $\eta = 40.6\%$ (theoretical maximum)

- **Ripple Factor**: $r = 1.21$ (high ripple content)

- **Peak Inverse Voltage (PIV)**: $PIV = V_m$ (maximum reverse voltage
  across diode)

- **DC Output**: $V_{DC} = \frac{V_m}{\pi} = 0.318 V_m$ where $V_m$ is
  peak AC voltage

#### Applications:

Half-wave rectifiers are used in low-power applications like battery
charging, signal demodulation, and voltage multipliers. They are "not
suitable" for high-power applications due to poor efficiency.
:::

::: mnemonicbox
["HWR: Half-Wave = Half output, 40.6% efficiency, PIV =
Vm"]{style="color: mnemoniccolor"}
:::
