---
author:
- Milav Dabgar
date: મહિના દિવસ, વર્ષ
lang: gu
title: Subject Name (SUBJECT001) - Sample Term Solution
---

## Question 1

### Question 1(અ) \[3 marks\]

**ત્રણ numbers માંથી maximum શોધવા માટે Java program લખો.**

#### Solution

ત્રણ numbers માંથી **maximum** શોધવા માટે, અમે values ની સરખામણી કરવા માટે
**conditional statements** (if-else) નો ઉપયોગ કરીએ છીએ. Program ત્રણ
numbers input તરીકે લે છે અને તેમાંથી “સૌથી મોટી value” પરત કરે છે.

##### Java Program:

``` java
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

##### Output:

    Maximum number is: 40

##### મુખ્ય મુદ્દાઓ:

- **Logic**: પ્રથમ `a` અને `b` ની સરખામણી કરો, મોટી value ને `max` માં store
  કરો

- **બીજી સરખામણી**: અંતિમ maximum મેળવવા માટે `max` ને `c` સાથે સરખાવો

- **વૈકલ્પિક**: Concise code માટે `Math.max(a, Math.max(b, c))` નો ઉપયોગ
  કરી શકાય

> *MAX: જોડીમાં સરખાવો, પરીક્ષણે મહત્તમ અપડેટ કરો*

### Question 1(બ) \[4 marks\]

**RC low-pass filter નું cutoff frequency શોધો જ્યાં $`R = 1.5\,k\Omega`$ અને
$`C = 100\,nF`$ છે. તેમજ cutoff frequency પર જો input 10V હોય તો output
voltage શોધો.**

#### Solution

##### આપેલ માહિતી:

- Resistance: $`R = 1.5\,k\Omega = 1500\,\Omega`$

- Capacitance: $`C = 100\,nF = 100 \times 10^{-9}\,F`$

- Input Voltage: $`V_{in} = 10\,V`$

##### પગલું 1: Cutoff Frequency ની ગણતરી

RC low-pass filter માટે **cutoff frequency** નો formula છે:
``` math
f_c = \frac{1}{2\pi RC}
```

મૂલ્યો મૂકીએ:
``` math
f_c = \frac{1}{2\pi \times 1500 \times 100 \times 10^{-9}}
```
``` math
f_c = \frac{1}{2\pi \times 1.5 \times 10^{-4}}
```
``` math
f_c = \frac{1}{9.42 \times 10^{-4}} = 1061.57\,Hz \approx 1.06\,kHz
```

##### પગલું 2: Cutoff પર Output Voltage

Cutoff frequency પર, output voltage એ input voltage ના **0.707 ગણા**
(અથવા $`\frac{1}{\sqrt{2}}`$) હોય છે:
``` math
V_{out} = 0.707 \times V_{in} = 0.707 \times 10 = 7.07\,V
```

##### પરિણામો:

- **Cutoff Frequency**: $`f_c = 1.06\,kHz`$

- **Output Voltage**: $`V_{out} = 7.07\,V`$ cutoff પર

- **Attenuation**: $`-3\,dB`$ cutoff frequency પર

- **Phase Shift**: $`-45^\circ`$ cutoff frequency પર

> *RC-Formula: fc = 1/(2$`\pi`$ RC), Vout = 0.707 Vin at fc*

### Question 1(ક) \[7 marks\]

**Active અને passive electronic components ની યોગ્ય ઉદાહરણો સાથે તુલના
કરો.**

#### Solution

Electronic components ને **active** અને **passive** કેટેગરીમાં વર્ગીકૃત કરવામાં
આવે છે જે તેમની electrical energy ને control અથવા amplify કરવાની ક્ષમતા પર
આધારિત છે.

| **લાક્ષણિકતા** | **Active Components** | **Passive Components** |
|:---|:---|:---|
| Energy Source | બાહ્ય power source જરૂરી | બાહ્ય power જરૂરી નથી |
| Control Ability | Current flow ને control/amplify કરી શકે | Amplify નહીં, ફક્ત regulate કરે |
| Directionality | સામાન્ય રીતે unidirectional | Bidirectional |
| Power Gain | Power gain આપે ($`>1`$) | Power gain હંમેશા $`\leq 1`$ |
| ઉદાહરણો | Transistors (BJT, FET), Diodes (LED, Zener), ICs (Op-Amp, 555), SCR | Resistors, Capacitors, Inductors, Transformers |
| કાર્ય | Amplification, switching, oscillation, rectification | Resistance, capacitance, inductance, filtering |
| Linearity | Linear અથવા non-linear હોઈ શકે | સામાન્ય રીતે linear |

Active vs Passive Components Comparison

##### Active Components વિગતવાર:

- **Transistors**: Amplification અને switching માટે વપરાય છે. BJT current
  control વાપરે, FET voltage control વાપરે છે.

- **Diodes**: એક દિશામાં current ને પસાર થવા દે છે. LED પ્રકાશ બહાર કાઢે,
  Zener voltage regulate કરે છે.

- **ICs**: Integrated circuits જેવા કે `555 timer` (oscillator), op-amps
  (amplifier).

- **Power Requirement**: બધા active components ને ચાલુ થવા માટે DC
  bias/supply જરૂરી.

##### Passive Components વિગતવાર:

- **Resistors**: Current flow નો વિરોધ કરે, power ને heat તરીકે dissipate
  કરે. મૂલ્ય $`\Omega`$ માં.

- **Capacitors**: Electric field માં energy સંગ્રહ કરે. મૂલ્ય Farads (F) માં,
  DC block કરે, AC પસાર કરે.

- **Inductors**: Magnetic field માં energy સંગ્રહ કરે. મૂલ્ય Henry (H) માં, AC
  ફેરફારોનો વિરોધ કરે.

- **Transformers**: Magnetic coupling દ્વારા circuits વચ્ચે energy transfer
  કરે.

##### મુખ્ય તફાવત:

મૂળભૂત તફાવત એ છે કે active components circuit માં “power inject” કરી શકે
(amplification), જ્યારે passive components ફક્ત energy “absorb અથવા store”
કરી શકે, તેને ક્યારેય વધારી શકતા નથી.

> *ACTIVE = Amplify, Control, Transform; PASSIVE = Resist, Store,
> Filter*

### Question 1(ક OR) \[7 marks\]

**Half-wave rectifier circuit ને input અને output waveforms સાથે દોરો અને તેનું
કાર્ય સમજાવો.**

#### Solution

**Half-wave rectifier** AC voltage ને pulsating DC માં રૂપાંતરિત કરે છે input
AC waveform ના ફક્ત એક half-cycle (positive અથવા negative) ને પસાર થવા
દઈને.

##### Circuit Diagram:

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

##### કાર્ય સિદ્ધાંત:

1.  **Positive Half-Cycle**: જ્યારે input AC positive હોય, diode
    forward-biased (conduct) થાય છે. Current load resistor $`R_L`$ માંથી
    વહે છે, output voltage ઉત્પન્ન કરે છે.

2.  **Negative Half-Cycle**: જ્યારે input AC negative હોય, diode
    reverse-biased (block) થાય છે. કોઈ current વહેતું નથી, output voltage
    શૂન્ય હોય છે.

3.  **પરિણામ**: Output પર ફક્ત positive half-cycles દેખાય છે, pulsating DC
    બનાવે છે.

##### Waveform Representation:

<figure data-latex-placement="H">

<figcaption>Input and Output Waveforms</figcaption>
</figure>

##### મુખ્ય પરિમાણો:

- **Efficiency**: $`\eta = 40.6\%`$ (સૈદ્ધાંતિક મહત્તમ)

- **Ripple Factor**: $`r = 1.21`$ (ઉચ્ચ ripple content)

- **Peak Inverse Voltage (PIV)**: $`PIV = V_m`$ (diode પર મહત્તમ reverse
  voltage)

- **DC Output**: $`V_{DC} = \frac{V_m}{\pi} = 0.318 V_m`$ જ્યાં $`V_m`$ એ
  peak AC voltage છે

##### એપ્લિકેશન્સ:

Half-wave rectifiers નો ઉપયોગ low-power applications માં થાય છે જેવા કે
battery charging, signal demodulation, અને voltage multipliers. તેઓ poor
efficiency ને કારણે high-power applications માટે *યોગ્ય નથી*.

> *HWR: Half-Wave = અડધું output, 40.6% efficiency, PIV = Vm*
