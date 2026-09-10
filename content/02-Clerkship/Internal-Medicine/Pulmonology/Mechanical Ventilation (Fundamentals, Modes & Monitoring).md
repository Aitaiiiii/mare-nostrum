---
title: "Mechanical Ventilation (Fundamentals, Modes & Monitoring)"
aliases: ["Mechanical Ventilation (Fundamentals, Modes & Monitoring)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Pulmonology"
also_relevant: ["Chest Medicine", "Critical Care medicine"]
type: "Disease"
guidelines: ["ATS/ERS"]
review_status: "New"
tags: [pulmonology, disease, ats-ers, critical-care]
created: 2026-06-26
notion_id: 38b224ab-ad81-816d-88f8-f13f24e44e21
source: notion-migration
---

# Mechanical Ventilation (Fundamentals, Modes & Monitoring)

# 🧬 1. Etiology & Molecular Pathophysiology

MV ใช้แรงดันบวกจากภายนอก (positive pressure) เพื่อขับอากาศเข้าปอดแทนแรงดันลบตามธรรมชาติ ความเข้าใจ respiratory mechanics เป็นรากฐานของทุก clinical decision

## Fundamental Respiratory Mechanics

**Compliance (C = ΔV/ΔP)**: Static compliance: **Crs = VT / (Pplat − PEEP)**; ปกติ 50–100 mL/cmH₂O; ARDS <40; ลดใน stiff lungs (ARDS, pulmonary edema, fibrosis) หรือ stiff chest wall (obesity, abdominal compartment syndrome); Dynamic compliance (Cdyn) = VT/(Ppeak−PEEP) < Crs เสมอ

**Resistance (Raw = (Ppeak − Pplat) / Flow)**: ปกติ <5 cmH₂O/L/s; สูงใน bronchospasm, secretions, small ETT

**Time Constant (τ = R × C)**: บอกความเร็วในการ fill/empty alveolus — obstruction: τ ยาว → ต้องการ expiration นานกว่า → ถ้าสั้นเกิน → **auto-PEEP + dynamic hyperinflation** — ARDS: heterogeneous τ → pendelluft + stress concentration = VILI mechanism

**Driving Pressure (ΔP = Pplat − PEEP = VT/Crs)**: สะท้อน strain ของ aerated lung unit; **Amato et al. 2015**: ΔP เป็น strongest predictor ของ ARDS mortality เหนือ Pplat/VT/PEEP; **target <15 cmH₂O**

**Transpulmonary Pressure (PL = Paw − Ppl)**: true distending pressure ของปอด; Ppl วัดจาก esophageal pressure; มีประโยชน์ใน obese/high IAP

**Mechanical Power (MP)**: total energy/min delivered ต่อปอด (J/min) — **Gattinoni simplified formula (VCV only)**: **MP = 0.098 × RR × Vt × [Ppeak − (Pplat − PEEP)/2]** — ค่าคง **0.098** แปลง cmH₂O·L → Joule **ขาดไม่ได้**; สูตรนี้ valid เฉพาะ **VCV ที่ constant flow** — ใน **PCV** ใช้ **Becher formula: 0.098 × RR × Vt × (ΔP_insp + PEEP)** แทน เนื่องจาก decelerating flow ทำให้ P-V loop ต่างกัน; **>17 J/min = poor outcome**; LDPV protocol targeting ΔP + MP (2024, n=3,468) ลด ICU mortality 47.7% → 41.1%

## VILI Mechanisms

- **Volutrauma**: high VT → stretch → integrin → NF-κB → IL-8/IL-6/TNF-α → VALI
- **Barotrauma**: high Pplat → overdistension → alveolar rupture → PTX, pneumomediastinum
- **Atelectrauma**: cyclic opening-closing (low PEEP) → shear → surfactant dysfunction
- **Biotrauma**: cytokine spillover → systemic → MODS — สาเหตุหลักของ MV mortality
- **P-SILI**: vigorous spontaneous effort → large negative Ppl → transpulmonary pressure spike → heterogeneous injury; rationale สำหรับ deep sedation ± NMB ใน severe ARDS

---

# 🩺 2. Clinical Phenotypes & Advanced Nuances

## Indications for Invasive MV

- **Hypoxemic failure**: PaO₂ <60 mmHg ที่ไม่ตอบสนองต่อ O₂/NIV/HFNC (V/Q mismatch, shunt, diffusion impairment)
- **Hypercapnic failure**: PaCO₂ ↑ + pH <7.25 + exhausted muscles; COPD: NIV first; severe asthma: พิจารณา early intubation ถ้า fatigue
- **Airway protection**: GCS ≤8, massive hemoptysis, facial/airway trauma

## Ventilator Modes Taxonomy

| Mode | Trigger | Control | Key Feature |
| --- | --- | --- | --- |
| **VC-AC** | Patient/time | Volume | Guaranteed VT; risk respiratory alkalosis; flow starvation |
| **PC-AC** | Patient/time | Pressure | Decelerating flow; VT varies with compliance; better synchrony |
| **PRVC/VC+** | Patient/time | Hybrid | Pressure-limited + volume-targeted; ซ่อน high drive |
| **PSV** | Patient only | Pressure | Weaning; cycle-off ปัญหาใน COPD (delayed) และ ARDS (premature) |
| **SIMV** | Mixed | Mixed | ไม่แนะนำสำหรับ weaning; inferior to PSV |
| **CPAP** | Patient | — | No mandatory breaths; NIV/ETT post-extubation |
| **APRV** | Time | Pressure | บาง evidence; ไม่ first-line ARDS (ESICM 2024) |

## Ventilator Modes Taxonomy

| Mode | Trigger | Control | Key Feature |
| --- | --- | --- | --- |
| **VC-AC** | Patient/time | Volume | Guaranteed VT; risk respiratory alkalosis; flow starvation |
| **PC-AC** | Patient/time | Pressure | Decelerating flow; VT varies with compliance; better synchrony |
| **PRVC/VC+** | Patient/time | Hybrid | Pressure-limited + volume-targeted; ซ่อน high drive |
| **PSV** | Patient only | Pressure | Weaning; cycle-off ปัญหาใน COPD (delayed) และ ARDS (premature) |
| **SIMV** | Mixed | Mixed | ไม่แนะนำสำหรับ weaning; inferior to PSV |
| **CPAP** | Patient | — | No mandatory breaths; NIV/ETT post-extubation |
| **APRV** | Time | Pressure | บาง evidence; ไม่ first-line ARDS (ESICM 2024) |

## 🔄 4-Phase Breath Physiology (Trigger → Limit → Cycle → Baseline)

ทุก ventilated breath ดำเนินตาม  4 phase เสมอ — การเข้าใจ phase แต่ละอันทำให้ order ventilator ได้อย่างเป็นระบบ และวิเคราะห์ waveform ได้ครบทุก mode (Chatburn taxonomy)

### Phase 1 — Trigger

สิ่งที่ “เริ่ม” inspiration: ventilator ตรวจจับสัญญาณจากผู้ป่วยหรือจากนาฬิกาแล้วเปิดเปลือย demand valve

- **Flow trigger** (preferred): ventilator ส่ง bias flow ต่อเนื่องไว้ใน circuit (~1–2 L/min); เมื่อผู้ป่วย inhale → เบียง flow drop จาก bias → trigger; **ข้อดี**: WOB น้อย, responsive กว่า, auto-trigger น้อยกว่า pressure sense; **ข้อเสีย**: auto-trigger ถ้า circuit leak หรือ water in tubing
- **Pressure trigger**: ผู้ป่วย inhale → pressure drop ≥2 cmH₂O จาก PEEP → trigger; ใช้ถ้า flow sense auto-trigger จาก circuit leak/cardiogenic oscillation; WOB สูงกว่าเล็กน้อย
- **Time trigger** (mandatory): ventilator เริ่มตาม set RR — backup ถ้าผู้ป่วยไม่ trigger เอง; patient trigger ทับได้เสมอ
- **ระวัง**: trigger sensitivity **สูงเกิน (over-sensitive)** → auto-trigger → alkalosis + patient-ventilator asynchrony; **ต่ำเกิน (under-sensitive)** → missed trigger → เพิ่ม WOB + fatigue + asynchrony

### Phase 2 — Control / Limit

สิ่งที่ “ควบคุม” inspiration — ventilator รักษาตัวแปรใดตัวหนึ่งให้คงที่ตลอด breath (ตัวแปรอื่นสามารถเปลี่ยนแปรเป็น “limited” ได้)

- **VCV — limit = flow** (constant flow — “square wave”): ventilator ให้ flow คงที่ตลอด; pressure ขึ้นตาม compliance + resistance; **Ppeak ≠ alveolar pressure** (ต้องทำ inspiratory hold เพื่อวัด Pplat); **Ramp/Rise time** = ความชันการขึ้นถึง set flow → สั้น = square wave → ยาว = decelerating-like; ปรับตาม patient demand
- **PCV — limit = pressure**: ventilator ให้ pressure คงที่ตลอด breath; **⚠️ IP = pressure above PEEP ไม่ใช่จาก zero** (Ppeak = IP + PEEP); flow เป็น decelerating (เพราะ alveolar pressure ค่อยๆ เพิ่มขึ้น → pressure gradient ลดลง); VT เปลี่ยนตาม compliance + resistance → ต้อง monitor VT เสมอ
- **PSV — limit = pressure support** (above PEEP): patient สามารถหายใจได้เองตาม demand; VT และ flow ขึ้นอยู่กับ effort + compliance

**Waveform signature ตาม limit type**:

- VCV: pressure-time ”ramp up” (slope ขึ้นเป็นเส้นตรง); flow-time ”square”; ถ้า bump ตอนต้น = สูง resistance
- PCV: pressure-time ”rectangle” (ขึ้นเร็วแล้วคงที่); flow-time ”decelerating”; ถ้า flow ไม่ถึง zero = Ti สั้นเกิน (อาจ air-trap)
- PSV: pressure-time ”rectangle” คล้าย PCV; flow-time decelerating และจะลงถึง Esense แล้วตัด

### Phase 3 — Cycle

สิ่งที่ “จบ” inspiration → เปลี่ยนเป็น expiration: ventilator ปิด demand valve → passive expiration

- **Time cycling (PCV/PC-AC)**: จบที่ Ti เสมอ — ถ้า Ti ยาวเกินไป → ผู้ป่วยเริ่ม exhale ก่อนที่ ventilator จะ cycle → ผู้ป่วยทน inspiration ทั้งที่อยาก exhale → เย็น + ทนไม่ได้ (air-hunger)
- **Volume cycling (VCV)**: จบเมื่อถึง set VT — **⚠️ ถ้าใส่ Inspiratory Pause → cycling เปลี่ยนเป็น time ทันที—** ventilator hold pressure หลัง deliver VT → วัด Pplat ได้; implement ต่างกันตามรุ่น:
    - Pause (sec) = ต่อหลังจาก Ti → total insp time เพิ่มขึ้น
    - Pause (%) = กินเวลาใน Ti ไปเลย → delivery time ลดลง; ต้องดู manual รุ่นนั้นๆ
- **Flow cycling (PSV — Esense)**: flow ลดลงถึง % ที่ตั้งของ peak flow → cycle-off — เป็น physiological ที่สุดใน normal breathing

| Esense (%) | Terminate | เหมาะใน | Clinical problem ถ้า wrong |
| --- | --- | --- | --- |
| สูง 40–45% | เร็ว | COPD / high compliance | ต่ำเกิน → air trap, delayed cycle, double-trigger |
| Default ~25% | Standard | Most patients | — |
| ต่ำ 5–15% | ช้า | ARDS / low compliance | สูงเกิน → premature cycle, double-trigger, shallow VT |

### Phase 4 — Baseline (PEEP)

ความดันที่ maintain ไว้ในขณะ expiration — มี physiological effect สำคัญ

- **Extrinsic PEEP (set PEEP)**: รักษา FRC → ลด atelectasis; เปิด alveoli ที่ collapsed → เพิ่ม V/Q matching; ลด O₂ requirement (เพิ่ม oxygenation เลี่ยงพอย FiO₂ ได้); ใน COPD ช่วย counterbalance auto-PEEP → ลด WOB trigger
- **Auto-PEEP (intrinsic PEEP / PEEPi)**: gas trapped เพราะ expiratory time ไม่พอ → alveolar pressure > airway pressure ตอนสิ้น expiration; ผล: (1) เพิ่ม inspiratory threshold load → ผู้ป่วยต้อง overcome PEEPi ก่อนจะ trigger → missed trigger; (2) dynamic hyperinflation → เพิ่ม intrathoracic pressure → ลด venous return → hemodynamic collapse; (3) barotrauma
- **วัด auto-PEEP**: expiratory hold maneuver → equilibrated pressure = total PEEP; หรือดู flow-time curve (ถ้า flow ไม่กลับ zero ก่อน next breath → auto-PEEP)
- **แก้ auto-PEEP**: ลด RR, เพิ่ม inspiratory flow rate (ให้ expiratory time ยาวขึ้น), ตั้ง applied PEEP = 80% PEEPi

### Workflow: Order Vent ตาม 4-Phase

> **คิดตามลำดับนี้ทุกครั้งที่ order ventilator**
> 

> 1. **Trigger**: Flow sense (default) → ปรับ threshold ถ้า auto-trigger; เปลี่ยนเป็น pressure ถ้า leak
> 

> 2. **Limit/Control**: เลือก PCV (ตั้ง IP above PEEP + Ti) หรือ VCV (ตั้ง VT + flow rate + ramp time); PSV = ตั้ง PS level
> 

> 3. **Cycle**: Ti (PCV); VT ± pause และตรวจ pause type sec vs % (VCV); Esense (PSV)
> 

> 4. **Baseline**: PEEP
> 

> 5. **Universal**: FiO₂ + **alarm** (VT min/max, RR max, Ppeak max, MV min/max, apnea backup)
> 

## Disease-Specific Phenotypes

**ARDS**: VT 4–6 mL/kg PBW; Pplat <30; ΔP <15; high PEEP; prone ≥16h ใน severe — ดู ARDS monograph

**Obstructive (COPD/asthma)**: RR 8–12; Flow 80–100 L/min; I:E 1:3–4; applied PEEP = 80% PEEPi; permissive hypercapnia (pH >7.20); hemodynamic collapse หลัง intubation = auto-PEEP → disconnect + bag

**Neuromuscular**: VT 8 mL/kg; RR 12–16; maintain partial ventilatory support เพื่อป้องกัน diaphragm atrophy

---

# 🩻 3. Advanced Diagnostics & Formal Criteria

## Post-Intubation Assessment

- ABG ใน 30 นาที; CXR (ETT tip 2–4 cm เหนือ carina; T4–T5 level); EtCO₂ waveform confirmation

## Ventilator Mechanics

**Inspiratory hold → Pplat** (hold 0.5–1.5 sec; flow = 0): target <30 cmH₂O

- **Crs = VT / (Pplat − PEEP)** — normal 50–100; ARDS <40
- **Raw = (Ppeak − Pplat) / Flow** — normal <5 cmH₂O/L/s
- **ΔP = Pplat − PEEP** — target <15 cmH₂O

**Expiratory hold → auto-PEEP (PEEPi)**: total PEEP = set PEEP + PEEPi; applied PEEP = 80% PEEPi ใน COPD

**P0.1 (100ms occlusion pressure)**: respiratory drive; >3.5–4.0 cmH₂O = high drive → P-SILI risk; <0.5 = needs full support; guide PSV titration ใน weaning

## Waveform Interpretation

- VC pressure-time: steep slope = low compliance; initial bump = high resistance
- Flow-time: ไม่กลับ zero ก่อน next breath = auto-PEEP
- Double triggering: patient triggers 2nd breath ขณะยัง expiring → ลด inspiratory time / เพิ่ม flow rate

## Oxygenation Monitoring

| Parameter | Formula | Target |
| --- | --- | --- |
| P/F ratio | PaO₂/FiO₂ | ≥300 normal; <300 = ARDS |
| S/F ratio | SpO₂/FiO₂ | 235 ≈ P/F 200; 315 ≈ P/F 300 |
| OI | Pmean×FiO₂×100/PaO₂ | >16 severe (ECMO consideration) |

**Oxygenation target 2024**: SpO₂ 92–96%; PaO₂ 55–80 mmHg; liberal vs conservative: no mortality difference (meta-analysis 13 RCTs 2024); avoid hyperoxia (SpO₂ >99% + high FiO₂ → ROS + resorption atelectasis)

## ARDSNet FiO₂/PEEP Table

| FiO₂ | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Low PEEP** | 5 | 5–8 | 8–10 | 10 | 10–12 | 14 | 14–18 | 18–24 |
| **High PEEP** | 5 | 8–10 | 10–12 | 14 | 14–16 | 18 | 18–22 | 22–24 |

---

# 💊 4. Management & Pharmacodynamics

## IBW (Devine Formula)

- **Male**: PBW = 50 + 0.91 × (Height cm − 152.4)
- **Female**: PBW = 45.5 + 0.91 × (Height cm − 152.4)

## Standard Initial Settings

| Parameter | Initial Value | Rationale |
| --- | --- | --- |
| Mode | VC-AC | Guaranteed VT; familiar |
| VT | 6–8 mL/kg PBW | 4–6 ใน ARDS |
| RR | 16–20 /min | Adjust ตาม pH/PaCO₂; สูงถึง 35 ใน ARDS |
| FiO₂ | 1.0 → wean ≤0.6 | Target SpO₂ 92–96% |
| PEEP | 5–8 cmH₂O | 10–20 ใน ARDS |
| Flow rate | 60 L/min | 80–100 ใน COPD/asthma |
| I:E ratio | 1:2 | 1:3–4 ใน obstruction |
| Trigger | Flow −2 L/min | Pressure −2 ถ้าไม่มี auto-PEEP |

## Lung-Protective Strategy (ทุก MV patients)

- VT ≤8 mL/kg PBW (4–6 ใน ARDS)
- Pplat <30 cmH₂O
- **ΔP <15 cmH₂O** (primary target post-Amato 2015)
- PEEP ≥5 cmH₂O (prevent atelectrauma)
- Permissive hypercapnia (pH >7.20) ถ้าจำเป็น

## Sedation (PADIS 2018)

- **Analgesia-first**: fentanyl/morphine IV; target RASS −1 ถึง 0
- Propofol/dexmedetomidine ≯ midazolam; daily awakening + daily SBT standard of care
- Deep sedation + NMB: severe ARDS (P-SILI prevention), prone, severe asynchrony; ไม่ routine หลัง ROSE trial (NEJM 2019)

## VAP Prevention Bundle

- HOB 30–45°; oral chlorhexidine daily
- Minimize sedation; daily awakening + daily SBT
- Cuff pressure 20–30 cmH₂O; circuit change เฉพาะเมื่อ visibly soiled
- Early EN; stress ulcer prophylaxis

## Troubleshooting Acute Deterioration — DOPES

**ถ้าไม่แน่ใจ → disconnect + bag manually 100% O₂ ก่อนเสมอ**

- **D** — Dislodged ETT
- **O** — Obstructed ETT
- **P** — Pneumothorax
- **E** — Equipment failure
- **S** — Stacked breaths / auto-PEEP / high PEEP hemodynamic

---

# 📚 5. Landmark Trials & Literature

**ARDSNet / NHLBI Network (NEJM 2000)** — 861 patients; VT 6 vs 12 mL/kg PBW; mortality 31% vs 39.8% (p=0.007; 22% relative RR reduction); ลด plasma IL-6 ยืนยัน biotrauma; กำหนด standard care lung-protective ventilation

**Amato et al. (NEJM 2015)** — Post-hoc mediation analysis, 9 RCTs (n=3,562); ΔP strongest predictor ของ ARDS mortality เหนือ Pplat/VT/PEEP; shift paradigm → ΔP-targeted ventilation

**PROSEVA (Guerin et al., NEJM 2013)** — Prone ≥16h ใน severe ARDS (P/F <150); 28-day mortality 16% vs 32.8%; NNT=6 — standard of care ใน severe ARDS

**LOV-S trial (NEJM 2022)** — Staircase RM + high PEEP vs low PEEP ใน moderate-severe ARDS; ต้อง stop early เพราะ ↑ mortality (55.3% vs 49.3%); **aggressive high-pressure RM ไม่แนะนำ**

**ACURASYS (NEJM 2010)** — Cisatracurium 48h ใน moderate-severe ARDS; ลด 90-day mortality (HR 0.68); reduce VILI markers

**ROSE trial (NEJM 2019)** — Cisatracurium vs light sedation; ไม่มีความแตกต่าง 90-day mortality; NMB ยังมีบทบาทใน P-SILI/asynchrony แต่ไม่ routine ทุก ARDS

**LUNG SAFE study (JAMA 2016)** — 29,144 patients, 50 countries; 40% ARDS ไม่ได้รับ lung-protective VT; mortality 34.9%; implementation gap ขนาดใหญ่ใน real world

**Mechanical Power Studies (2019–2024)** — MP >17 J/min เป็น independent predictor ของ mortality; LDPV protocol targeting ΔP + MP (2024, n=3,468) ลด ICU mortality 47.7% → 41.1% — *สูตร ดู section 1 (Gattinoni simplified, VCV only)*

**AARC 2024 Liberation Guidelines** — ดู ETT Weaning monograph ใน Notion สำหรับรายละเอียด

---

# 🔧 Ventilator Waveform & 4-Phase Framework

> จากโน้ต ICU Round 25 Jun — framework สำหรับทำความเข้าใจ + order ventilator ทุก mode
> 

## 4-Phase Framework (Trigger → Limit → Cycle → Baseline)

ทุก ventilated breath ผ่าน 4 phase ตามลำดับนี้เสมอ — เมื่อเข้าใจ framework นี้สามารถ order ventilator และวิเคราะห์ waveform ได้ทุก mode อย่างเป็นระบบ (Chatburn taxonomy)

---

**Phase 1 — Trigger**: อะไร "เริ่ม" inspiration?

- **Patient trigger — Flow sense**: ventilator detect baseline circuit flow drop (threshold ~1–2 L/min) → preferred; sensitive กว่า pressure sense; auto-triggering น้อยกว่า
- **Patient trigger — Pressure sense**: pressure drop ≥2 cmH₂O จาก PEEP → ใช้ถ้า flow trigger auto-trigger บ่อย (leak หรือ cardiogenic oscillation); work of breathing สูงกว่าเล็กน้อย
- **Time trigger**: ventilator เริ่มตาม set RR โดยอัตโนมัติ (mandatory breath); ถ้าผู้ป่วย trigger เองก่อน = patient trigger override

---

**Phase 2 — Control / Limit**: อะไร "ควบคุม" inspiration (ไม่ให้เกินค่าที่ตั้ง)?

- **PCV — limit = pressure**: Inspiratory Pressure (IP) คือ pressure **above PEEP** ไม่ใช่จาก zero → Ppeak = IP + PEEP (เช่น IP 15 + PEEP 8 = Ppeak 23 cmH₂O); ต้องดูกราฟ pressure-time ยืนยันเสมอ เพราะบางรุ่นแสดงผลต่างกัน
- **VCV — limit = flow** (บางรุ่น limit ด้วย VT หรือ Ti เพิ่มเติม); **Ramp time / Rise time / Slope** = ความชันที่ขึ้นถึง limit flow → สั้น = เร็ว (square wave pattern) → ยาว = ค่อยๆ ขึ้น (decelerating-like); ปรับตาม patient demand เพื่อลด asynchrony
- **PSV — limit = pressure support level** (above PEEP; patient determines flow/VT)

---

**Phase 3 — Cycle**: อะไร "จบ" inspiration → เปลี่ยนเป็น expiration?

- **PCV cycling = time**: จบที่ Ti ที่ตั้งไว้เสมอ
- **VCV cycling = volume**: จบเมื่อถึง set VT — **⚠️ ข้อยกเว้นสำคัญ: ถ้าใส่ Inspiratory Pause จะเปลี่ยน cycling เป็น time ทันที** แทนที่จะจบที่ volume → ventilator hold pressure หลังจากส่ง VT แล้ว; implement ต่างกันตามรุ่น:
    - **Pause = วินาที (sec)**: pause ต่อจากหลังจากครบ Ti; total inspiratory time = Ti + pause
    - **Pause = เปอร์เซ็นต์ (%)**: กินเวลาใน Ti ไปเลย; Ti ไม่เพิ่ม แต่ actual delivery time ลดลง → ต้องตรวจสอบ manual ของ ventilator รุ่นนั้นๆ
- **PSV cycling = flow (Esense)**: เมื่อ inspiratory flow ลดลงถึง % ที่ตั้งของ peak inspiratory flow → cycle-off

| Esense | Behavior | ใช้ใน |
| --- | --- | --- |
| สูง 40–45% | Terminate เร็ว | COPD/high compliance (ป้องกัน air trap + delayed cycle) |
| Default ~25% | Standard | Most patients |
| ต่ำ 5–15% | Terminate ช้า | ARDS/low compliance (ป้องกัน premature cycle + double-trigger) |

---

**Phase 4 — Baseline**: ความดันที่ค้างไว้ระหว่าง expiration = **PEEP**

---

## Workflow: Order Ventilator ตาม 4-Phase

เมื่อสั่ง order ให้คิดตามลำดับนี้:

1. **Trigger**: Flow sense (default); ปรับ threshold ถ้า auto-trigger / ใช้ pressure sense ถ้า circuit leak
2. **Limit/Control**: เลือก mode (PCV vs VCV) → ตั้ง IP (PCV) หรือ VT + flow + ramp (VCV); PSV = ตั้ง pressure support level
3. **Cycle**: ตั้ง Ti (PCV); ตั้ง VT ± pause (VCV); ตั้ง Esense (PSV)
4. **Baseline**: ตั้ง PEEP
5. **Universal**: ตั้ง FiO₂ + **alarm** ทุกครั้ง (VT min/max, RR max, Ppeak max, MV min/max, apnea time)
