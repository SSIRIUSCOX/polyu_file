# EE546 Homework Solutions - Batteries and Supercapacitors

### Question 1: Batteries (50%)

### 1) Battery Voltage Calculation

Given parameters:

- Electromotive force (EMF): E = 3.7 V
- Ohmic resistance: R_Ω = 50 mΩ = 0.05 Ω
- Polarization resistance: R_f = 30 mΩ = 0.03 Ω
- Total internal resistance: R_internal = R_Ω + R_f = 0.05 + 0.03 = 0.08 Ω

Operating voltage formula: U_cc = E - I × R_internal

#### i. When discharge current I = 2 A:

U_cc = 3.7 - 2 × 0.08 = 3.7 - 0.16 = **3.54 V**

#### ii. When discharge current I = 6 A:

U_cc = 3.7 - 6 × 0.08 = 3.7 - 0.48 = **3.22 V**

#### iii. Comparison and explanation:

- When current increases from 2A to 6A, the operating voltage decreases from 3.54V to 3.22V, a drop of 0.32V
- **Reason**: Higher external load current results in greater voltage drop across the internal resistance, leading to reduced output voltage
- This follows Ohm's law, where voltage drop across internal resistance is proportional to current

### 2) Battery Types

#### Primary batteries (non-rechargeable):

1. **Alkaline Zinc-Manganese Battery** (Alkaline Zn-MnO₂)
2. **Lithium Primary Battery** (Lithium primary, Li-MnO₂, Li-SOCl₂)
3. **Zinc-Air Battery** (Zn-Air)

#### Secondary batteries (rechargeable):

1. **Lithium-ion Battery** (Li-ion)
2. **Lithium Iron Phosphate Battery** (LiFePO₄)
3. **Nickel-Metal Hydride Battery** (Ni-MH)
4. **Lead-Acid Battery** (Lead-acid)
5. **Sodium-ion Battery** (Na-ion)

**Energy density comparison**:

- **Primary batteries** typically have higher specific energy density because they don't need to consider reversibility, allowing for more active materials and optimized chemical reactions

### 3) Electric Vehicle Battery System Design

Given parameters:

- Bus voltage: 800 V
- Total energy capacity: 96 kWh
- Single cell: 3.7 V, 3 Ah

#### i. Series and parallel configuration calculation:

**Series number** N_s: N_s = 800 V ÷ 3.7 V = **216.2 ≈ 217 cells** (round up to ensure sufficient voltage)

**Parallel number** N_p: Total capacity: 96 kWh ÷ 800 V = 120 Ah N_p = 120 Ah ÷ 3 Ah = **40 parallel groups**

#### ii. 2C discharge time:

- Total capacity: 120 Ah
- 2C discharge current: 120 × 2 = 240 A
- Discharge time: 120 Ah ÷ 240 A = **0.5 hours = 30 minutes**

#### iii. Maximum power at 1C discharge:

- 1C discharge current: 120 A
- Maximum power: 800 V × 120 A = **96 kW**

## Question 2: Supercapacitors (50%)

### 1) Electric Double Layer Capacitor (EDLC)

#### i. Four electrode materials:

1. **Activated Carbon** - High specific surface area (1000-2000 m²/g) and abundant microporous structure
2. **Graphene** - Theoretical specific surface area up to 2630 m²/g, single-layer carbon atom structure
3. **Carbon Nanotubes** - Unique tubular structure providing large surface area and good conductivity
4. **Carbide-Derived Carbon (CDC)** - Controllable pore size distribution, high specific surface area

| Electrode Material    | Key Properties for Increased Surface Area                    |
| --------------------- | ------------------------------------------------------------ |
| **Activated Carbon**  | Extremely high specific surface area (>1000 m²/g), porous structure, low cost, good conductivity |
| **Carbon Nanotubes**  | One-dimensional nanostructure, strong conductivity, good thermal stability, microporous but slightly lower specific surface area than activated carbon |
| **Carbon Aerogel**    | Highly porous and lightweight, specific surface area 100–1000 m²/g, performance can be enhanced through surface modification |
| **Carbon Nanofibers** | Graphitized structure, high mechanical strength, can be composited with other materials to enhance electrochemical performance |

**Properties contributing to large surface area**:

- Porous structure (micropores, mesopores)
- Nanoscale size effects
- High specific surface area
- Good electrolyte wettability

#### ii. Electric double layer distance:

According to the Helmholtz model, the electric double layer distance d ≈ **0.5-1 nm** (distance of several molecular diameters)

### 2) Cyclic Voltammetry (CV) Testing

#### i. CV curve characteristics:

**Ideal capacitor**: Rectangular CV curve, current proportional to scan rate, independent of voltage

**Reasons for practical deviations**:

1. **Equivalent Series Resistance (ESR)**: Causes curve tilting and IR voltage drop
2. **Pseudocapacitive behavior**: Fast redox reactions produce peaks and nonlinear response

#### ii. Specific capacitance calculation:

Given: mass m = 40 g, voltage window ΔU = 2.5 V, integrated charge ΔQ = 300 C

Specific capacitance formula: C_specific = ΔQ/(m × ΔU) C_specific = 300 C ÷ (40 g × 2.5 V) = **3 F/g**

### 3) Galvanostatic Charge-Discharge (GCD) Testing

#### i. Equivalent series resistance calculation:

Given: current I = 3 A, voltage drop ΔV = 0.15 V

ESR = ΔV ÷ (2I) = 0.15 V ÷ (2 × 3) A = **0.025 Ω = 25 mΩ**

#### ii. ESR impact on power density:

**Maximum power density analysis**:

- Power: P = U²/(4 × ESR) (maximum power when load resistance equals internal resistance)
- Lower ESR means:
  - Lower power loss (I²R loss)
  - Higher operating voltage (reduced IR drop)
  - Faster charge-discharge response
  - Higher power density and energy efficiency

**Conclusion**: Lower ESR results in superior power performance of supercapacitors, especially in high-power applications.