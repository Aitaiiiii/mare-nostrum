---
title: "MV Waveform & PVA (Waveform Interpretation, Patient-Ventilator Asynchrony & Troubleshooting)"
aliases: ["MV Waveform & PVA (Waveform Interpretation, Patient-Ventilator Asynchrony & Troubleshooting)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
also_relevant: ["Critical Care medicine", "Chest Medicine"]
type: "Workflow"
guidelines: ["ATS/ERS"]
review_status: "New"
tags: [critical-care, workflow, ats-ers]
created: 2026-06-26
notion_id: 38b224ab-ad81-813e-994e-e12097c571d3
source: notion-migration
---

# MV Waveform & PVA (Waveform Interpretation, Patient-Ventilator Asynchrony & Troubleshooting)

# 🧬 1. Physiological Foundation — Equation of Motion & Respiratory Mechanics

ความสัมพันธ์ระหว่าง pressure, volume และ flow ใน respiratory system ทั้งหมดถูกควบคุมโดย Equation of Motion ซึ่งเป็น foundation ของการวิเคราะห์ waveform และ troubleshooting ทุกอย่างบน ventilator:

**P_vent + P_mus = (V_T / C_rs) + (R_rs × V̇) + PEEP_total**

โดยที่ P_vent = pressure จาก ventilator, P_mus = pressure จาก respiratory muscles ผู้ป่วย, V_T/C_rs = elastic load, R_rs × V̇ = resistive load และ PEEP_total รวม auto-PEEP เสมอ

ใน **passive patient** (P_mus = 0) ventilator รับ load ทั้งหมด ทำให้ waveform สะท้อน respiratory mechanics ผู้ป่วยโดยตรง ในขณะที่ **active effort** waveform ถูกบิดเบือนโดย P_mus ทำให้ต้องใช้ esophageal pressure (Pes) เป็น surrogate ของ P_mus

## Compliance, Resistance & Time Constant

**Static Compliance** — คำนวณจาก inspiratory hold:

- C_rs = V_T / (Pplat − PEEP) — Normal 50–100 mL/cmH₂O
- ลดใน ARDS, pulmonary edema, pneumonia, fibrosis, abdominal HT
- ใน VCV: compliance ↓ → Pplat ↑ (PIP-Pplat gradient เดิม — resistance ไม่เปลี่ยน)

**Resistance** — คำนวณจาก:

- R_rs = (PIP − Pplat) / V̇_insp — Normal < 10 cmH₂O/L/s
- สูงใน bronchospasm, secretions, ETT biting, kinked circuit
- ใน VCV: resistance ↑ → PIP ↑ แต่ Pplat เดิม → **PIP-Pplat gap กว้างขึ้น = diagnostic clue**

**Time Constant (τ = R × C)** — กุญแจสู่ flow waveform ใน PCV:

- τ คือเวลาที่ alveolus fill/empty ถึง 63% ของ equilibrium; complete fill/empty ต้องการ 3–5τ
- Obstructive disease (↑R → ↑τ): ต้องการ I-time นานขึ้น + RR ช้าลง ป้องกัน auto-PEEP
- ใน PCV flow-time scalar: exponential decelerating pattern; flow ยังไม่ถึง zero = Ti สั้นเกิน

**Driving Pressure (ΔP = Pplat − PEEP = V_T / C_rs)**:

- สะท้อน stress ต่อ functional lung ดีกว่า V_T absolute — normalize ด้วย compliance แทน "baby lung" size ใน ARDS
- Threshold เชื่อมกับ ARDS mortality: **ΔP > 15 cmH₂O** (Amato et al. 2015, NEJM)

**Transpulmonary Pressure (PL = Paw − Pes)**:

- True distending pressure ของปอด — set PEEP ให้ end-expiratory PL ≥ 0 (ป้องกัน collapse); end-inspiratory PL < 20–25 cmH₂O (ป้องกัน overdistension)
- มีประโยชน์เฉพาะใน obese, high IAP, severe ARDS ที่ chest wall mechanics มีบทบาทมาก

## Mechanical Power (MP) — The Emerging VILI Metric

MP = total energy delivered ต่อ respiratory system ต่อหน่วยเวลา เป็น integrative metric ของ VILI risk ทุก variable:

**MP ≈ 0.098 × RR × V_T × (ΔP + PEEP + ½ × R_rs × V̇)**

Simplified bedside ใน VCV: **MP ≈ 0.098 × RR × V_T × (PIP − ½ΔP)**

- Normal: < 12–17 J/min
- Threshold เชื่อมกับ mortality: **> 17 J/min** (Gattinoni 2016 ICM; Costa 2021 AJRCCM)
- MP integrates RR, VT, ΔP, PEEP, flow ทุกตัวเป็น single VILI risk metric
- 2025 data (PNAS): alveolar recruitment energy อาจเป็น component ที่ injurious ที่สุด แม้ magnitude น้อยกว่า tissue deformation

**Bedside application**: ถ้า MP สูงเกิน 17 J/min ให้ตรวจ component ไหน drive ขึ้น — RR? VT? ΔP? PEEP? — แล้วแก้ตัวนั้นก่อน

---

# 🩺 2. Ventilator Modes & Waveform Phenotypes — Advanced Modes

*หมายเหตุ: Fundamental modes (VCV, PCV, PSV, SIMV) และ 4-Phase Framework ครอบคลุมในหน้า Mechanical Ventilation (Fundamentals, Modes & Monitoring) แยกต่างหาก — page นี้เน้น advanced modes + waveform interpretation ขั้นสูง*

## TTC Framework Revisited

ทุก mechanical breath classify ตาม 3 axes ที่เป็นอิสระ:

| Axis | Ventilator-controlled | Patient-controlled |
| --- | --- | --- |
| **Trigger** | Time (mandatory) | Flow หรือ Pressure effort |
| **Target** | Volume หรือ Pressure | Patient effort (PAV/NAVA) |
| **Cycle** | Volume, Time, Flow% | Flow%, Time |

## Waveform Signatures ตาม Mode

**VCV waveform pattern**: square flow → pressure trapezoidal ramp

- PIP ↑, Pplat เดิม → resistance ↑
- PIP ↑, Pplat ↑ → compliance ↓
- **Scooping** ของ pressure-time → flow starvation (patient demand > set flow)

**PCV waveform pattern**: constant pressure → decelerating exponential flow

- Decelerating flow ถึง zero = Ti เพียงพอสำหรับ τ
- Decelerating flow truncated ไม่ถึง zero = Ti สั้นเกิน → อาจ air-trap
- **Overshoot spike** ที่ early inspiration = rise time เร็วเกินไป

**PSV waveform pattern**: patient trigger + flow cycle (Esense)

- Cycling threshold สูง (40–45%) → terminate เร็ว → COPD ป้องกัน air trap
- Cycling threshold ต่ำ (5–15%) → terminate ช้า → ARDS ป้องกัน premature cycling

## Advanced Modes

**PRVC / VC+ / APV (Dual-Control Mode)**

- Pressure-limited + volume-targeted: ventilator adjust pressure breath-to-breath เพื่อ achieve target V_T แบบ closed-loop
- Advantage: lower peak pressure + VT consistency (best of VCV + PCV)
- **Pitfall — PRVC runaway**: ใน high drive patients เมื่อ compliance ดีขึ้นอย่างรวดเร็ว ventilator ลด pressure → แต่ patient effort เพิ่ม → VT overshoot → P-SILI risk

**PAV+ (Proportional Assist Ventilation)**

- Formula: P_vent = k_f × V̇(t) + k_v × V(t)
- k_f = flow assist coefficient (ลด resistive work); k_v = volume assist coefficient (ลด elastic work)
- Ventilator ประเมิน R และ C แบบ real-time ทุก breath ผ่าน least-squares fitting algorithm
- Patient control ทั้ง depth และ timing ของ breath — most physiologic mode
- **Contraindication**: respiratory depression, neuromuscular weakness, apnea

**NAVA (Neurally Adjusted Ventilatory Assist)**

- P_vent = NAVA_level (cmH₂O/μV) × EAdi (μV)
- Trigger และ control pressure ตาม electrical activity ของ diaphragm ผ่าน EAdi catheter (nasogastric)
- Key advantage: **bypass auto-PEEP threshold load** เพราะ trigger ที่ neural signal ไม่ใช่ airway pressure/flow
- ลด PVA โดยเฉพาะ ineffective trigger ที่เกิดจาก auto-PEEP
- NAVA level titration: เพิ่มทีละ 0.5 cmH₂O/μV จนถึง threshold ที่ ventilator "follows" patient effort อย่างสมบูรณ์
- **Contraindication**: absent diaphragmatic function, NMBA, cardiac/esophageal pacemaker, ไม่สามารถใส่ EAdi catheter

**APRV (Airway Pressure Release Ventilation)**

- Bilevel CPAP + inverse I:E ratio: maintain P_high (T_high 4–6 วินาที) → release ไปที่ P_low สั้น (T_low 0.4–0.8 วินาที)
- Cycling parameter: **T_low ตั้งให้ flow ถึง 75% ของ peak expiratory flow** ก่อน next P_high
- ผู้ป่วย breathe spontaneously ตลอดเวลา โดยเฉพาะใน T_high phase
- Mechanism ป้องกัน VILI: sustained P_high ป้องกัน alveolar collapse → ลด atelectrauma จาก cyclic opening/closing
- ⚠️ ใน patients ที่มี high respiratory drive → vigorous effort ใน T_low phase → large V_T swings → P-SILI risk
- Evidence: ยังไม่ convincing เมื่อเทียบกับ standard lung-protective approach; ESICM 2024 ไม่แนะนำ first-line ใน ARDS

**ASV (Adaptive Support Ventilation)**

- Closed-loop: ventilator คำนวณ optimal RR + V_T combination โดย minimize WOB ตาม Otis equation พร้อมรักษา target minute ventilation
- Set: IBW + target MV% (80–90% weaning; 120–150% high metabolic demand) + PEEP + FiO₂ + Paw limit
- Benefit: post-operative weaning, chronic respiratory failure with preserved drive, early recovery phase
- **Contraindication**: very low VT target, severe ARDS, severe metabolic acidosis, severe TBI, obese/restrictive lung ที่ต้องการ VT ต่ำมาก

| Mode | Target | Trigger | Cycle | Advantage | Limitation |
| --- | --- | --- | --- | --- | --- |
| VCV/AC | Volume | Time/Patient | Volume | VT guarantee | High Ppeak, flow starvation |
| PCV/AC | Pressure | Time/Patient | Time | Lower Ppeak, dec. flow | VT variability |
| PSV | Pressure | Patient | Flow% | Synchrony ดี | Cycling asynchrony |
| PRVC/VC+ | Vol+Press | Time/Patient | Volume | Best of both | PRVC runaway |
| PAV+ | Proportional | Patient | Patient | Most physiologic | Weak/no drive CI |
| NAVA | EAdi-based | EAdi | EAdi | Bypass auto-PEEP | EAdi catheter required |
| APRV | Bilevel CPAP | — | Time | Recruit + spontaneous | P-SILI ถ้า high drive |
| ASV | Closed-loop | Auto/Patient | Auto | Auto-weaning | CI ใน restrictive/obese/ARDS |

## P-V Loop และ F-V Loop

**Pressure-Volume Loop**:

- Area inside loop = work of breathing (WOB) รวม
- Inner loop width = airway resistance component (dynamic WOB)
- Outer loop (hysteresis) = tissue resistance + surfactant component
- **Beak sign** ที่ upper right = overdistension (UIP exceeded) → ลด VT/PEEP
- Loop shift leftward หลัง recruitment = ↑ compliance

**Flow-Volume Loop**:

- Shape ของ expiratory curve บอก airway mechanics
- Notch/scalloping บน expiratory flow curve = variable upper airway obstruction
- Early steep drop ใน expiration = high resistance (bronchospasm, secretions)

---

# 🩻 3. Patient-Ventilator Asynchrony — Classification, Waveform Recognition & Advanced Monitoring

## PVA Overview & Clinical Significance

PVA = mismatch ระหว่าง patient's neural respiratory effort กับ ventilator-delivered breath ซึ่ง organize ตาม phase ของ respiratory cycle ที่ mismatch เกิดขึ้น

- Prevalence: **~25%** ของ mechanically ventilated patients
- **Asynchrony Index (AI) ≥ 10%** เชื่อมกับ longer MV duration (+3.29 วัน) และ ICU LOS (+3.65 วัน) จาก systematic review 2024 (n=2,672)
- **AI = (asynchronous breaths / total breath attempts) × 100%**

## Phase 1: Trigger Asynchrony

### Ineffective Triggering (Missed Trigger)

**Waveform**: pressure scalar deflect ลงเล็กน้อย หรือ flow scalar มี small transient perturbation ใน expiratory phase แต่ไม่มี breath ตามมา

**กลไก**:

- Ventilator factors: trigger sensitivity ไม่เหมาะสม
- Patient factors: **dynamic hyperinflation/auto-PEEP** (ต้องการ effort overcome auto-PEEP ก่อน → ไม่ถึง trigger threshold), respiratory muscle weakness, excessive PSV

**Management**:

- ปรับ trigger sensitivity → **flow trigger preferred** กว่า pressure trigger
- ใน obstructive: extrinsic PEEP ≈ 80% auto-PEEP เพื่อ counterbalance inspiratory threshold load
- ลด PSV level ถ้า over-assisted

### Autotriggering

**Waveform**: breaths เกิดโดยไม่มี patient effort นำหน้า — pressure scalar ไม่มี inspiratory dip, flow scalar ไม่มี perturbation ก่อน trigger

**กลไก**: cardiac oscillations, circuit water condensation, air leak, trigger sensitivity สูงเกิน

**Cheyne-Stokes Respiration** — cause ของ autotriggering ที่สำคัญใน HF/CNS injury:

- Crescendo-decrescendo pattern + central apnea → autotriggering ใน apnea phase
- Preferred modes: AC (VC หรือ PC) หรือ SIMV/PSV ที่มี low mandatory rate
- ลด trigger sensitivity; ลด MV เป้า → permissive hypercapnia (PaCO₂ ~40–45 mmHg)
- **หลีกเลี่ยง** PAV/PRVC/Volume Support → อาจ worsen periodic breathing

### Double Triggering

**Waveform**: 2 consecutive mechanical breaths ภายใน single inspiratory effort — breath ที่สองเกิดทันทีหลัง breath แรก มี VT เล็กกว่า → **breath stacking** → delivered V_T รวม ≈ 2× normal → **P-SILI risk สูง**

**กลไก**: Ti ของ ventilator สั้นกว่า neural Ti → ventilator cycle ออก แต่ neural effort ยังอยู่ → trigger breath ที่สอง พบบ่อยใน high drive: ARDS, fever, metabolic acidosis, pain

**Management**:

- VCV: ลด peak flow rate (ยืด Ti) หรือเปลี่ยนเป็น decelerating flow
- PCV: เพิ่ม Ti ให้ตรงกับ patient neural Ti
- Refractory → เพิ่ม sedation

### Reverse Triggering (RT) — 2025 Update

**Waveform**: diaphragm contraction เกิด **หลัง** passive insufflation เริ่มแล้ว

- Pes trace: negative deflection ใน mid-to-late inspiration
- Airway pressure: secondary deflection หรือ "double notch" ใน late inspiration
- ใน passive patient: pressure waveform deformation ที่ unexplained

**กลไก** (2 proposed pathways):

1. **Entrainment**: respiratory rhythm ของ brainstem (pre-Bötzinger complex) ถูก entrain กับ periodic mechanical insufflation ผ่าน Hering-Breuer reflex
2. **Local pulmonary reflexes**: ไม่ผ่าน central rhythm generator

**Prevalence**: **30–55%** ของ sedated patients ใน controlled ventilation (AJRCCM 2023 review); มักเกิดใน transition phase จาก fully passive → assisted

**2025 RT Phenotype Classification (J Mech Vent Dec 2025)**:

- **Early RT**: EAdi/effort เริ่มใน early inspiration → flow mismatch
- **Mid-cycle RT**: effort peak ตรงกับ mechanical peak flow
- **Late / Post-cycle RT**: effort ต่อเนื่องเข้า exhalation → breath stacking → **P-SILI risk สูงสุด**

⚠️ **2025 First Case Report (AJRCCM Nov 2025)**: RT ระหว่าง NIV ในผู้ป่วย bilateral diaphragmatic dysfunction — RT ไม่ได้จำกัดอยู่ใน invasive ventilation อีกต่อไป

**Management**:

- ลด RR → ยืด Ti → ปรับ entrainment pattern
- Deep sedation (RASS –3 to –4)
- ถ้า RT เป็น sign ของ recovering drive (high frequency + improving oxygenation) → พิจารณา transition ไปสู่ assisted mode
- NMBA เป็น last resort

## Phase 2: Flow Asynchrony

### Flow Starvation (Insufficient Flow)

**Waveform**: **"scooping / concave deformity"** ของ inspiratory pressure-time scalar ใน VCV — ปกติควรเป็น linear ramp แต่ถูก "pulled down" โดย patient effort; Pes trace แสดง large negative swing

**กลไก**: Patient neural demand > set peak flow ใน VCV → patient ต้อง fight ventilator → ↑ WOB มาก

**Management**: ↑ peak flow (40 → 60–80 L/min) หรือเปลี่ยนเป็น PCV/PSV

### Flow Overshoot

**Waveform**: **spike** ที่ early inspiration ใน PCV/PSV — pressure สูงเกิน target ชั่วคราว; flow-time scalar แสดง peak สูงผิดปกติ

**กลไก**: Rise time เร็วเกินไป → early pressure overshoot ก่อน lung inflate sufficiently

**Management**: ยืด rise time (เพิ่ม msec)

### Increased Airway Resistance Pattern

**Waveform**: ใน flow-time scalar (expiratory): **prolonged expiratory time** ก่อน flow return ถึง zero baseline — ถ้า RR เร็วเกินไปสำหรับ τ → **auto-PEEP** (flow ไม่ถึง zero ก่อน next breath)

ใน VCV pressure-time: PIP ↑ ขณะ Pplat เดิม (↑ PIP-Pplat gradient)

**Auto-PEEP detection**: **expiratory hold maneuver** → pressure ที่สูงกว่า set PEEP = auto-PEEP

### Air Leak Pattern

**Waveform**: inspiratory volume > expiratory volume บน volume-time scalar; flow scalar ไม่ return ถึง baseline; pressure ไม่ถึง target ใน PCV

**กลไก**: ETT cuff leak, bronchopleural fistula, circuit disconnection

## Phase 3: Cycling / Termination Asynchrony

### Premature Cycling

**Waveform**: ventilator cycle ออกก่อน patient neural Ti สิ้นสุด → **double hump** บน pressure-time scalar หรือ patient effort ต่อเนื่องเข้า early expiratory phase

**กลไก**:

- Ventilator: Ti สั้นเกินไป
- Patient: restrictive mechanics (fibrosis) → flow drop เร็วมาก → cycling criterion ใน PSV ถึงเร็ว

**Management**:

- VCV: ลด peak flow / ↑ VT → ยืด Ti
- PCV: ↑ Ti
- PSV: ลด cycling threshold criterion (เช่น 25% → 10–15%) โดยเฉพาะ restrictive

### Delayed (Prolonged) Cycling

**Waveform**: ventilator ยัง inflate หลัง patient neural effort สิ้นสุด → patient exhale แต่ ventilator ยัง deliver → **spike** ที่ end of inspiration ใน pressure-time scalar; expiratory flow kick ใน late inspiration

**กลไก**: obstructive mechanics → flow drop ช้า → cycling criterion ใน PSV (% peak flow) ถึงช้า → Ti ยาว

**Management**: ↑ cycling threshold criterion ใน PSV (เช่น 25% → 40–45%)

## PVA Summary Table

| Type | Phase | Waveform Signature | Main Cause | Management |
| --- | --- | --- | --- | --- |
| Ineffective trigger | Trigger | Dip ไม่มี breath ตาม | Auto-PEEP, over-sedation | Flow trigger; extrinsic PEEP = 80% auto-PEEP |
| Autotriggering | Trigger | Breath ไม่มี dip นำหน้า | Leak, cardiogenic osc. | ↑ threshold; ตรวจ circuit |
| Double triggering | Trigger | 2 breaths ใน 1 effort | Ti < neural Ti | ↑ Ti; ลด flow VCV |
| Reverse triggering | Trigger | Effort หลัง insufflation | Deep sedation + entrainment | ↑ Ti; sedation; NMBA |
| Flow starvation | Flow | Pressure scooping | Set flow < demand | ↑ flow / เปลี่ยน PCV |
| Flow overshoot | Flow | Early pressure spike | Rise time เร็วเกิน | ↑ rise time |
| ↑ Resistance | Flow | Prolonged expiratory flow | Bronchospasm, secretion | Bronchodilator, suction |
| Air leak | Flow | Insp > exp volume | Cuff leak, BPF | ตรวจ cuff, circuit |
| Premature cycling | Cycling | Double hump | Ti < neural Ti; restrictive | ↑ Ti; ↓ cycling threshold PSV |
| Delayed cycling | Cycling | End-insp spike | Obstructive; low cycling% | ↑ cycling threshold PSV |

## Advanced Monitoring Beyond Waveform

**Esophageal Pressure (Pes)** — Gold standard สำหรับ respiratory effort assessment:

- **ΔPes** (inspiratory swing) = effort marker; normal 5–10 cmH₂O; > 15 cmH₂O = high effort / P-SILI risk
- **Transpulmonary Pressure (PL) = Paw − Pes**: set PEEP ให้ end-expiratory PL ≥ 0 (ป้องกัน collapse); end-inspiratory PL < 20–25 cmH₂O (ป้องกัน overdistension)
- Confirm autotriggering vs weak effort: ไม่มี Pes deflection = autotriggering แน่นอน
- Identify RT ได้ชัดเจนกว่า airway waveform คนเดียว

**P0.1 (Airway Occlusion Pressure at 100ms)** — Central respiratory drive:

- Measure โดยไม่ขึ้นกับ respiratory mechanics; อ่านได้จาก ventilator หลายรุ่นโดยตรง
- P0.1 > 3.5–4 cmH₂O → high drive → P-SILI risk → พิจารณา ↑ sedation
- P0.1 < 0.5 cmH₂O → low drive → ↑ respiratory muscle atrophy risk
- Guide PSV titration ใน weaning: target P0.1 1.5–3.5 cmH₂O

**EAdi (Electrical Activity of Diaphragm)**:

- ใน NAVA patients: EAdi trace ให้ข้อมูล direct ที่สุดเกี่ยวกับ timing + magnitude ของ neural effort
- ตรวจ RT ได้ชัดเจนที่สุด — negative EAdi deflection ตาม mechanical insufflation
- EAdi ยังใช้ใน non-NAVA patients เป็น monitoring tool โดยไม่ต้อง activate NAVA mode

---

# 💊 4. Management & Troubleshooting — Algorithms & Clinical Application

## Alarm Troubleshooting Algorithm

### High Airway Pressure Alarm — DOPES Framework

เมื่อ PIP สูงขึ้นกะทันหัน: **disconnect + bag manually 100% O₂ ก่อน** ถ้าไม่แน่ใจ

- **D — Dislodged ETT**: ETT หลุด, เลื่อนเข้า mainstem bronchus → ฟัง bilateral BS, CXR
- **O — Obstructed ETT**: secretions, biting, kinking, mucus plug, bronchospasm → suction, auscultation
- **P — Pneumothorax**: ↓ BS unilaterally + ↑ PIP + ↓ BP + ↑ HR → bedside US / emergency needle decompression
- **E — Equipment**: circuit kink, water trap, ventilator malfunction
- **S — Stacked breaths / auto-PEEP**: obstructive physiology → disconnect + assess manual resistance

**Physiological Differentiation ด้วย Inspiratory Hold**:

| Pattern | PIP | Pplat | PIP-Pplat | ΔP | Interpretation |
| --- | --- | --- | --- | --- | --- |
| ↑ Resistance only | ↑ | Normal | **↑** | Normal | Bronchospasm, secretion, biting ETT |
| ↓ Compliance only | ↑ | ↑ | Normal | **↑** | PTX, pulm edema, ARDS↓, abdominal HT |
| Mixed | ↑ | ↑ | ↑ | ↑ | ARDS + mucus plug |
| Auto-PEEP | ↑ | ↑ | ↑ (partial) | — | Obstructive → expiratory hold maneuver |

### Low Tidal Volume Alarm

Air leak (ETT cuff, bronchopleural fistula, circuit disconnect), compliance ลดมากใน PCV mode, trigger น้อยลงใน PSV, auto-PEEP สูงใน obstruction → manual bagging ก่อน systematic check

### Low Airway Pressure Alarm

Circuit disconnection, ETT extubation, ETT cuff deflation, large air leak → manual bagging → systematic check circuit ทั้งหมด

## PVA Management — Tiered Approach

**Tier 1: Ventilator Adjustment (First-line)**

- Ineffective trigger → ปรับ sensitivity (flow preferred) + extrinsic PEEP ≈ auto-PEEP × 0.8
- Double triggering → ยืด Ti (VCV: ↓ flow; PCV: ↑ Ti)
- Flow starvation → ↑ peak flow หรือเปลี่ยน VCV → PCV/PSV
- Premature cycling → ↓ cycling threshold % ใน PSV; ↑ Ti
- Delayed cycling → ↑ cycling threshold % ใน PSV

**Tier 2: Sedation Optimization**

- RASS 0 to –1 (light sedation): stable patients กำลัง wean
- RASS –2 to –3 (moderate): high drive / double triggering / RT ที่ไม่ตอบสนอง Tier 1
- RASS –4 to –5 (deep/NMBA): refractory PVA / P-SILI risk / severe ARDS acute phase
- Preferred: **propofol** (titratable, short-acting) + **fentanyl/morphine** (analgesia-first; SCCM PADIS 2018)
- หลีกเลี่ยง benzodiazepines ใน ICU (delirium risk)

**Tier 3: NMBA (ATS 2024 — conditional recommendation)**

- พิจารณา **cisatracurium** ใน severe ARDS (P/F < 100, < 48h) — conditional recommendation, low certainty
- MOA: benzylisoquinoline NMBA ออกฤทธิ์ผ่าน competitive ACh receptor blockade ที่ neuromuscular junction; Hofmann elimination → ไม่ขึ้นกับ renal/hepatic function
- Dosing: bolus 0.2 mg/kg IV → infusion 0.18–0.3 mg/kg/h (titrate to TOF 1–2/4)
- Primary benefit มาจาก prevention ของ PVA (RT, double triggering) → ลด P-SILI มากกว่า NMBA per se
- Monitor: TOF monitoring ทุก 4–6h; ระวัง prolonged weakness

**Tier 4: Mode Change**

- High drive + ineffective trigger → **NAVA** (bypass auto-PEEP issue)
- Variable mechanics + poor synchrony → **PAV+**
- Refractory RT ใน ARDS → ลด rate ใน controlled mode หรือ transition ถ้า lung function พร้อม

## Liberation Strategy (AARC 2024)

**Daily Readiness Screening**:

- P/F ≥ 150–200 mmHg, FiO₂ ≤ 0.4–0.5, PEEP ≤ 5–8 cmH₂O
- Stable hemodynamics, no agitation, adequate cough/secretion clearance

**SBT Method**: preferred **low-level PSV (5–8 cmH₂O)** หรือ T-piece เป็นเวลา 30–120 นาที

**RSBI (f/V_T)** — เป็นเพียง monitoring parameter ระหว่าง SBT ไม่ใช่ gatekeeper ก่อน (AARC 2024) — รายละเอียดสูตร, threshold, D-RSBI และ evidence → [ETT Weaning](ETT%20Weaning%20(Liberation%20from%20Mechanical%20Ventilatio%2038a224abad8181ecae71dab7682b2710.md)

- ไม่แนะนำ SIMV สำหรับ weaning
- Cuff leak test ใน prolonged intubation >1 สัปดาห์, female, large ETT (เทียบกับ IBW)

## P-SILI Framework — Patient Self-Inflicted Lung Injury

P-SILI เกิดจาก high respiratory drive ส่งผลให้ diaphragm effort สร้าง large negative pleural pressure swing → เพิ่ม transpulmonary pressure → lung stress/strain นอกเหนือจาก ventilator-delivered volume

**Clinical markers ที่บ่งชี้ P-SILI risk**:

- ΔPes > 15 cmH₂O (หรือ > 8–10 cmH₂O ใน ARDS)
- P0.1 > 3.5–4 cmH₂O
- Double triggering หรือ RT ที่บ่อยครั้ง (ด้าน late phenotype)
- Clinical: paradoxical chest wall motion, excessive accessory muscle use

**Management spectrum**:

- Mild: ↑ support level (PSV ↑), analgesia optimization
- Moderate: ↑ sedation depth (RASS –2 to –3), consider mode change
- Severe: deep sedation (RASS –4 to –5) ± cisatracurium 48h

---

# 📚 5. Landmark Trials & Literature

## Foundation of Lung-Protective Ventilation

**ARDSNet ARMA (2000, NEJM)** — 861 patients; VT 6 mL/kg IBW + Pplat ≤ 30 cmH₂O vs VT 12 mL/kg IBW; mortality 31.0% vs 39.8% (P=0.007); ↑ ventilator-free days (12 vs 10 วัน); กำหนด standard of care lung-protective ventilation ที่ยังใช้อยู่ถึงปัจจุบัน

**Amato et al. — Driving Pressure (2015, NEJM)** — Retrospective mediation analysis, n=3,562 จาก 9 RCTs; **ΔP** เป็น ventilatory variable ที่ predict ARDS survival ได้ดีที่สุด; ΔP ↓ ทุก 1 SD → survival ↑ (HR 0.32, 95% CI 0.28–0.37) แม้ adjust สำหรับ VT และ PEEP แล้ว; เปลี่ยน paradigm → ΔP-guided ventilation

**LUNG SAFE Study (Laffey et al., 2016, JAMA)** — 29,144 patients, 50 ประเทศ; ARDS 40% ไม่ได้รับการ recognized; lung-protective ventilation ถูก under-use; mortality 34.9%; เป็น basis สำหรับ quality improvement initiatives ทั่วโลก

**LOV-S Trial (2022, NEJM)** — Staircase RM + high PEEP vs low PEEP ใน moderate-severe ARDS; ต้อง stop early เพราะ ↑ mortality (55.3% vs 49.3%); **aggressive high-pressure RM ไม่แนะนำ**

## NMBA Debate: ACURASYS vs ROSE

**ACURASYS Trial (Papazian et al., 2010, NEJM)** — 340 patients, severe ARDS (P/F < 150); cisatracurium 48h vs placebo; 90-day mortality ลดลง (31.6% vs 40.7%, adjusted HR 0.68, P=0.04); ↓ barotrauma; ไม่เพิ่ม ICU-acquired weakness

**ROSE Trial (2019, NEJM)** — 1,006 patients, moderate-severe ARDS; early NMBA 48h (deep sedation control) vs light sedation (RASS 0 to –1) โดยไม่ routine NMBA; ผล 90-day mortality ไม่ต่างกัน (42.5% vs 42.8%, P=0.93)

**Reconciliation (Slutsky & Park, 2019–2020)**: ความแตกต่างของ ACURASYS vs ROSE อธิบายได้ด้วย sedation depth ใน control arm — ROSE มี light sedation control (ลด PVA ด้วย sedation เอง) ขณะที่ ACURASYS ใช้ deep sedation ใน control ทั้งสองกลุ่ม ดังนั้น benefit ของ NMBA ใน ACURASYS อาจมาจาก prevention ของ PVA/RT มากกว่า NMBA per se

**ATS 2024 Guidelines**: NMBA ยังคง conditional recommendation สำหรับ early severe ARDS (P/F < 100, < 48h) แต่ require individualized assessment

## Mechanical Power Evidence

**Gattinoni et al. (2016, Intensive Care Med)** — Seminal paper introduce MP concept; experimental pigs threshold ที่ 12 J/min เริ่ม induce VILI; provide formula สำหรับ bedside calculation

**Costa et al. (2021, AJRCCM) — ALVEOLI/LOVS/ExPress/ACURASYS reanalysis** — n=1,705 จาก 4 RCTs; MP เชื่อมกับ 28-day mortality (adjusted OR 1.08 per 1 J/min, P<0.001) แม้หลัง control สำหรับ VT, PEEP, RR และ ΔP → MP add independent information

**2025 Systematic Review (ScienceDirect 2025)** — ยืนยัน MP > 17 J/min เชื่อมกับ worse outcomes; VentCoach pilot trial (2025) แสดง feasibility ของ MP-guided protocol แต่ต้องการ larger RCT

**PNAS 2025** — Recruitment energy (alveolar opening) อาจเป็น component ที่ injurious ที่สุดของ MP แม้ magnitude น้อยกว่า tissue deformation — ชี้นัยต่อ recruitment maneuver design

## PVA Outcome Evidence

**Thille et al. (2006, Intensive Care Med)** — Classical study กำหนด AI ≥ 10% เป็น significant PVA threshold; พบใน 24% ของ patients; AI สัมพันธ์กับ longer MV duration

**PVA Systematic Review & Meta-analysis (2024)** — 19 studies, n=2,672; overall PVA + ineffective triggering + double triggering เชื่อมกับ MV duration ยาวขึ้น (mean diff 3.29 วัน) และ ICU LOS ยาวขึ้น (mean diff 3.65 วัน)

**Rietveld et al. (2025, ICM Exp) — AI-based PVA Detection** — Review 13 studies, >5.8 million breaths; ML algorithms มี sensitivity 80–95% สำหรับ specific PVA types ใน controlled settings; generalizability ยัง limited เนื่องจาก heterogeneous training sets

**Docci et al. (2025, Curr Opin Crit Care)** — "Does PVA really matter?" — critical review challenge causation vs association; เสนอว่า association ระหว่าง PVA กับ outcome อาจ confound โดย disease severity → need สำหรับ interventional RCT ที่ treat PVA as primary endpoint ยังคงอยู่

## Advanced Mode Trials

**NAVA Meta-analysis (Vaschetto 2019, Crit Care)** — Pooled analysis 9 RCTs (n=373); NAVA ลด AI อย่างมีนัยสำคัญ, ลด Ppeak, ลด sedation; ไม่ต่างกัน MV duration และ mortality; limitation: small heterogeneous trials

**PAV+ Trials (Xirouchaki 2008, 2014)** — 2 RCTs; PAV+ vs PSV ใน partial ventilatory support; ลด PVA, ↑ comfort, ↓ sedation requirement; ไม่ต่างกัน primary endpoint MV duration

**APRV vs Conventional** — ไม่มี large RCT แสดง mortality benefit; ESICM 2024 ไม่แนะนำ APRV เป็น first-line ใน ARDS

**Reverse Triggering Review (AJRCCM 2023)** — Prevalence 30–55% ใน sedated patients; RT frequency สูงอาจเป็น marker ของ improving neural drive มากกว่า indicator ของ need for deeper sedation; management ขึ้นกับ phenotype และ clinical context

---

> **หมายเหตุ**: Page นี้เป็น companion ของ **Mechanical Ventilation (Fundamentals, Modes & Monitoring)** ซึ่งครอบคลุม basic modes, 4-Phase Framework, initial settings และ DOPES overview ไว้แล้ว — ดูประกอบเสมอ
>
