# EE546 Homework 1

| name       | Student ID |
| ---------- | ---------- |
| XIA Yuejun | 25059117G  |



## Question 1:

### 1):

Given:


$$
\begin{align}
 Electromotive force (EMF): &E = 3.7 V \\
 Ohmic resistance: &R_Ω = 50 mΩ = 0.05 Ω \\
 Polarization resistance: &R_f = 30 mΩ = 0.03 Ω \\
 
 \end{align}
$$

$$
R_{i} = R_Ω + R_f = 0.05 + 0.03 = 0.08 Ω
$$



#### 1.When discharge current I = 2 A:


$$
\begin{align}
U_{cc} &= E-IR_{i} \\
&=3.7 - 2 × 0.08 = 3.7 - 0.16 = 3.54 V
\end{align}
$$



#### 2.When discharge current I = 6 A:

$$
\begin{align}
U_{cc} &= E-IR_{i} \\ 
&= 3.7 - 6 × 0.08 = 3.7 - 0.48 = 3.22 V
\end{align}
$$



#### 3. Comparison and explanation:

- When current increases from 2A to 6A, the operating voltage decreases from 3.54V to 3.22V, a drop of 0.32V

- Reason: Higher external load current results in greater voltage drop across the internal resistance, leading to reduced output voltage

  

---

### 2) 

#### Primary batteries (non-rechargeable):

1. Zinc–carbon
2. Alkaline Battery
3. Li-Metal Battery 

#### Secondary batteries (rechargeable):

1. Ni-Cd Battery
2. Ni-Fe Battery
3. Ni-MH Battery
4. Lead Acid Battery
5.  Lithium-Ion Battery

**Energy density comparison**:

- Primary batteries typically have higher specific energy density because they don't need to consider reversibility, allowing for more active materials and optimized chemical reactions.

---

### 3) 

Given:

- Bus voltage: 800 V
- Total energy capacity: 96 kWh
- Single cell(Rated voltage,Rated capacity): 3.7 V, 3 Ah

#### 1. Series and parallel configuration calculation:

$$
Series number  : 
N_s = 800 V /3.7 V = 216.2 ≈ 217 cells
\\
Parallel number\ \ N_p \ \: = (96 kWh / 800 V)/3Ah  = 120 Ah /3Ah = 120 Ah / 3 Ah = 40 
$$



#### 2. 2C discharge time:


$$
\begin{align}
t_{discharge \ time} &=\frac{Total \ \ capacity}{2C \ \ discharge \ \ current} \\
& = 120 Ah / (2*120)A \\
&= 0.5 hours = 30 minutes

\end{align}
$$


#### 3. Maximum power at 1C discharge:


$$
\begin{align}
P_{maximum} &=V_{bus \ \ voltage} \cdot (1C \ \ discharge \ \ current) \\
& = 800 V × 120 A = 96 kW
\end{align}
$$

---

## Question 2: 

### 1) 

#### 1. Four electrode materials(EDLC):

- Activated carbon:activated carbon has very large specific surface area.
- Carbon nanotubes : tubular nanostructure, high conductivity, stable framework.
- Carbon Aerogel: highly porous and lightweight, specific surface area 100–1000 m²/g, performance can be enhanced through surface modification.
- Carbon nanofiber: graphitized structure, can be composited with other materials to enhance electrochemical performance

Properties to a large A: 

- Unique molecular structure ,porous structure.



#### 2. Electric double layer distance(EDL):

The electrical double layer distance *d* is on the order of the ionic radius,  Typical values range from 31 pm to over 200 pm .[ionic_radius_from_wiki][1]

---

### 2) 

#### 1. CV curve :

Ideal capacitor: Rectangular shape for CV curve.

Reasons for practical deviations:

1. Capacitor with resistivity lead to a diamond shape.
2. Due to influence of redox reactions,cause peaks  in cv curve .

#### 2. Specific capacitance :


$$
mass : \ \ m = 40 g,\\ 
 voltage window: \Delta U = 2.5 V,\\ 
 integrated charge: \Delta Q = 300 C
$$

$$
\begin{align}
C_{s}& = ΔQ/(m × ΔU)  \\
&= 300 C / (40 g × 2.5 V) = 3 F/g
\end{align}
$$

---

### 3)

#### 1. ESR :


$$
current :\ \ I = 3 A \\

voltage\ \  drop: \Delta V = 0.15 V
$$

$$
\begin{align}
ESR:R_s &= \Delta V /(2I)  
= 0.15 V / (2 × 3) A = 0.025 Ω = 25 mΩ
\end{align}
$$


#### 2.  Effects of smaller ESR  on  supercapacitor performance:

**Maximum power density analysis**:

- Power: P = U²/(4 × ESR) (maximum power when load resistance equals internal resistance)

$$
P = \frac{U²}{(4\cdot R_s)}
$$



- Lower ESR means:
  - Lower power loss .
  - Higher operating voltage .
  - Faster charge-discharge response.
  - Achieving higher  power output under high current conditions.

---

[1]: https://en.wikipedia.org/wiki/Ionic_radius
