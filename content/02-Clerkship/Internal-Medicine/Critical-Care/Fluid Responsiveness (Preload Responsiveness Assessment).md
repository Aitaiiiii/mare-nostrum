---
title: "Fluid Responsiveness (Preload Responsiveness Assessment)"
aliases: ["Fluid Responsiveness (Preload Responsiveness Assessment)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
type: "Workflow"
review_status: "New"
tags: [critical-care, workflow]
created: 2026-06-23
notion_id: 388224ab-ad81-81ac-812a-e3bff09e3cd1
source: notion-migration
---

# Fluid Responsiveness (Preload Responsiveness Assessment)

## 🧬 Etiology & Molecular Pathophysiology

หัวใจของการประเมิน fluid responsiveness คือการทำความเข้าใจ **Frank-Starling relationship** ในบริบทของหัวใจที่กำลัง fail ในระดับ physiological: เมื่อ left ventricular end-diastolic volume (LVEDV) เพิ่มขึ้น cardiac sarcomere จะถูก stretch ส่งผลให้เกิดการเพิ่ม calcium sensitivity ของ troponin C ผ่าน length-dependent activation mechanism ซึ่งทำให้ stroke volume (SV) เพิ่มตาม — นี่คือ ascending limb ของ Starling curve ซึ่งเป็นบริบทที่ผู้ป่วย "ตอบสนองต่อ fluid" ได้

ปัญหาสำคัญคือ preload ไม่ได้สัมพันธ์ linear กับ filling pressure เช่น CVP หรือ PAOP เพราะ ventricular compliance นั้นแปรผันอย่างมากระหว่าง patient ที่แตกต่างกันและในผู้ป่วยรายเดิมตามเวลา ดังนั้น CVP จึงไม่สามารถทำนาย fluid responsiveness ได้น่าเชื่อถือ (AUC เพียง 0.77)

**กลไกการเกิด dynamic parameters**: ในผู้ป่วยที่ใส่เครื่อง mechanical ventilation แบบ mandatory mode การ insufflation ของปอดในช่วง inspiration จะเพิ่ม intrathoracic pressure ส่งผลให้ venous return ลดลงชั่วคราว เนื่องจาก transmural pressure ของ vena cava และ right atrium ลดลง ทำให้ RV preload ลดลง ส่งผล (หลังจาก pulmonary transit time ~2-3 heartbeats) ให้ LV SV ลดลงด้วย **Pulse Pressure Variation (PPV)** เกิดจาก respiratory-induced cyclic variation ของ SV ซึ่งสะท้อนออกมาเป็น variation ของ arterial pulse pressure เนื่องจาก pulse pressure ≈ SV / arterial compliance ผู้ป่วยที่อยู่บน steep ascending limb ของ Starling curve จะมี PPV/SVV สูง เพราะ cyclic change ใน preload มีผลต่อ SV มาก

นิยามมาตรฐาน: **fluid responsive = CO เพิ่มขึ้น ≥ 10-15%** หลังได้รับ fluid bolus โดย prevalence ของ fluid responsiveness ในผู้ป่วย ICU อยู่ที่ประมาณ **50%** (Messina et al., Critical Care 2024, n = 69 studies, 3,185 fluid challenges)

---

## 🩺 Clinical Phenotypes & Advanced Nuances

ผู้ป่วยทุกรายที่มี acute circulatory failure (MAP < 65 mmHg, lactate > 2 mmol/L, mottling, oliguria < 0.5 mL/kg/h, vasopressor escalation) ต้องถูกประเมินก่อน fluid challenge เสมอ

**Nuance สำคัญ — "Fluid Responsive แต่ไม่ควรให้ fluid"**: ผู้ป่วย ARDS ที่มี VExUS grade 3 (severe venous congestion) อาจ fluid responsive ตาม PPV แต่การให้ fluid จะยิ่งเพิ่ม pulmonary edema ผ่าน hydrostatic mechanism ดังนั้นต้องถามว่า "ควรให้หรือไม่?" ไม่ใช่แค่ "responsive หรือเปล่า?"

**Grey Zone ของ dynamic parameters**: ผู้ป่วย 15-20% มีค่า PPV/SVV อยู่ใน grey zone (PPV 9-13%, SVV 10-14%) ซึ่งต้องใช้ functional hemodynamic test อื่นเพิ่มเติม

**Limitations ของ PPV/SVV**:

- **Arrhythmia** (AF, frequent ectopics): RR interval irregular ทำให้ PPV/SVV invalid
- **Spontaneous breathing**: intrathoracic pressure change ไม่สม่ำเสมอ → ใช้ PLR แทน
- **Low Vt < 7 mL/kg PBW** (ARDS lung-protective): PPV false negative สูง → ใช้ TVC
- **Increased IAP** (abdominal compartment): PPV false positive
- **RV failure / Acute cor pulmonale**: D-sign on echo, TAPSE ลด, RV/LV > 0.9 → contraindication ต่อ aggressive fluid

---

## 🩻 Advanced Diagnostics & Formal Criteria

### Static vs Dynamic Parameters

| Parameter | Threshold | AUC | ข้อจำกัดหลัก |
| --- | --- | --- | --- |
| CVP | < 8 mmHg | 0.56–0.77 | Compliance-dependent; ควร abandon |
| PAOP | < 12 mmHg | ~0.55 | Invasive; compliance-dependent |
| IVC distensibility (MV) | > 18% | 0.80–0.90 | Mandatory mode + Vt ≥ 8 mL/kg |
| **PPV** | **≥ 11.5–12%** | **0.87** | MV mandatory + no arrhythmia + Vt ≥ 8 mL/kg |
| **SVV** | **≥ 12.1–13%** | **0.87** | เดียวกับ PPV; ต้องการ CO monitor |
| PVI (pleth) | ≥ 13.8% | 0.88 | Vasoconstriction ลด accuracy |
| ΔIVC (spont.) | > 40–50% collapsibility | ~0.80 | Operator-dependent |

*(Messina et al., Critical Care 2024)*

### Functional Hemodynamic Tests

**1. Passive Leg Raise (PLR) — Gold Standard**

- วิธี: semi-recumbent 45° → lower trunk flat + ยก leg 45° พร้อมกัน (~300 mL auto-bolus, 60–90 วินาที)
- Threshold: **ΔVTI aortic ≥ 10–15%** หรือ **ΔCO ≥ 10%**
- AUROC 0.95, sensitivity 85%, specificity 91% (Monnet meta-analysis, ICM 2016)
- ข้อดี: ใช้ได้กับ spontaneous breathing, arrhythmia, low Vt
- ข้อห้าม: elevated ICP; ต้องวัด CO จริง (ΔPP จาก PLR sensitivity ต่ำ = 56%)

**2. End-Expiratory Occlusion Test (EEXO)**

- วิธี: หยุด ventilator cycle ที่ end-expiration **15 วินาที** → venous return เพิ่มชั่วคราว
- Threshold: **ΔCO ≥ 5%** หรือ **ΔPP ≥ 5%**
- Sensitivity 85%, specificity 88% (Gavelli et al., Ann Intensive Care 2020)
- ดีใน low Vt/ARDS; ต้องการ deep sedation; ต้องทน 15-sec pause

**3. Tidal Volume Challenge (TVC)**

- วิธี: เพิ่ม Vt ชั่วคราว 6 → 8 mL/kg IBW นาน 1–3 นาที → วัด ΔPPV
- Threshold: **ΔPPV ≥ 3.5%** (absolute increase)
- Sensitivity 87%, specificity 84% (Myatra et al., Crit Care Med 2017)
- แก้ปัญหา false negative ของ PPV ใน ARDS

**4. Mini-Fluid Challenge**

- วิธี: ให้ **100 mL ใน 1 นาที** → วัด ΔCO/ΔVTI
- Threshold: **ΔCO ≥ 5%** หรือ **ΔVTI ≥ 10%**

### VExUS Score (Venous Excess Ultrasound)

| Grade | IVC | Hepatic Vein | Portal Vein | Renal Vein | ความหมาย |
| --- | --- | --- | --- | --- | --- |
| 0 | < 2 cm | ปกติ | ปกติ | ปกติ | No congestion |
| 1 | ≥ 2 cm | ปกติ หรือ 1 abnormal | — | — | Mild congestion |
| 2 | ≥ 2 cm | 1 abnormal ≠ severe | — | — | Moderate congestion |
| **3** | ≥ 2 cm | ≥ 1 severely abnormal | Pulsatile portal flow | Discontinuous renal flow | **Severe — withhold fluid** |

VExUS grade 3 สัมพันธ์กับ AKI และ worse outcomes (Andrei et al., Crit Care 2023; multicenter sepsis cohort, Ann Intensive Care 2025)

---

## 💊 Management & Pharmacodynamics

### ROSE Framework (Malbrain et al.)

- **R — Resuscitation (Salvage)**: restore perfusion pressure ฉุกเฉิน
- **O — Optimization**: guided fluid therapy ด้วย dynamic parameters
- **S — Stabilization**: งดให้ fluid ที่ไม่จำเป็น
- **E — Evacuation (De-escalation)**: active fluid removal

### Decision Algorithm

MV mandatory + ไม่มี arrhythmia + Vt ≥ 8 mL/kg → ใช้ PPV/SVV (PPV ≥ 12%: responsive; 9–12%: grey zone → ทำ EEXO หรือ PLR)

Spontaneous breathing / arrhythmia / อื่นๆ → PLR (ΔCO ≥ 10%: responsive)

ARDS + low Vt + MV mandatory → TVC เพิ่มเติม (ΔPPV ≥ 3.5%)

ทุกกรณี: ตรวจ VExUS — Grade 3 → พิจารณา withhold fluid แม้ responsive

### Fluid Challenge Technique

- **Balanced crystalloid (Plasmalyte, LR) 250–500 mL ใน 15–30 นาที**
- SSC 2021 (SCCM/ESICM): 30 mL/kg ภายใน 3 ชั่วโมงแรก (contested; individualized preferred หลัง initial)
- วัด ΔCO ทันที; ΔCO < 10–15% → หยุด
- Balanced crystalloid ดีกว่า NSS (SMART, JAMA 2018; SALT-ED, NEJM 2018) เนื่องจาก hyperchloremic acidosis จาก NSS เพิ่ม risk AKI

### Contraindications to Fluid

- VExUS grade 3
- New bilateral crepitations / worsening P:F ratio หลัง fluid
- RV failure / acute cor pulmonale (D-sign, TAPSE ลด, RV/LV > 0.9)
- Post-24–48 hr stabilization phase ใน ARDS

### De-escalation

- หลัง 24–48 ชั่วโมง: target **neutral-to-negative fluid balance**
- **Furosemide**: inhibit Na-K-2Cl cotransporter ที่ thick ascending limb → natriuresis
- Refractory → ultrafiltration ผ่าน CRRT

---

## 📚 Landmark Trials & Literature

| Trial | ปี | ผล | ความสำคัญ |
| --- | --- | --- | --- |
| ARISE / ProCESS / ProMISe | 2014–2015 | EGDT = usual care | ล้มล้าง CVP-guided fluid therapy |
| **CLASSIC** (NEJM) | 2022 | Restrictive vs standard: mortality ไม่ต่าง (42.3% vs 42.1%) | สนับสนุน restrictive/individualized approach |
| **SMART** (JAMA) | 2018 | Balanced crystalloid ลด MAKE30 (14.3% vs 15.4%, p=0.04) | Basis ของ balanced crystalloid recommendation |
| **SALT-ED** (NEJM) | 2018 | Balanced crystalloid ลด MAKE30 ใน ED | สนับสนุน SMART |
| **FACTT** (NEJM) | 2006 | Conservative fluid ลด ventilator days (11 vs 14 วัน, p<0.001) | "De-resuscitate" ใน ARDS |
| Monnet PLR meta-analysis (ICM) | 2016 | AUROC 0.95, sens 85%, spec 91% | Gold standard evidence สำหรับ PLR |
| Gavelli EEXO meta-analysis (Ann Intensive Care) | 2020 | Pooled sens 85%, spec 88% | EEXO validation |
| Myatra TVC (Crit Care Med) | 2017 | ΔPPV ≥ 3.5%: sens 87%, spec 84% | TVC สำหรับ ARDS/low Vt |
| **Messina et al.** (Critical Care) | 2024 | PPV AUC 0.87, SVV AUC 0.87, CVP AUC 0.77 | ยืนยัน abandonment ของ CVP; updated thresholds |

---

## 🛏️ PLR — Step-by-Step Bedside Guide

### ก่อนเริ่ม — Check Contraindications

- Elevated ICP / head injury
- Head-of-bed ต้องอยู่สูงตลอด (ICP monitoring, tracheostomy ที่มีปัญหา)
- Intraabdominal hypertension รุนแรง (IAP > 20 mmHg)
- Bilateral lower limb amputation
- Massive lower limb edema / compartment syndrome
- MAP < 50 → resuscitate ก่อน

### เตรียมของ

- **Echo (แนะนำ)**: cardiac probe + apical 5-chamber view สำหรับ LVOT VTI
- **EtCO₂**: อ่านจาก ventilator/monitor — ใช้ได้เฉพาะ MV + hemodynamics คงที่
- **Arterial line-based CO**: PiCCO, FloTrac, Vigileo — อ่าน CO/SV real-time

### Step 1 — ตั้งท่าเริ่มต้น

ผู้ป่วยนอนหงาย **head-of-bed 45°** ขาราบ → รอ hemodynamics stable **2–3 นาที** → **บันทึก baseline CO/VTI/MAP/HR**

> ⚠️ ท่าเริ่มต้นต้องเป็น 45° เท่านั้น — ถ้าเริ่มจาก supine flat จะได้ auto-bolus น้อยกว่ามาก เพราะ splanchnic reservoir mobilize ได้น้อยกว่า
> 

### Step 2 — เปลี่ยนเป็นท่า PLR (ทำพร้อมกันทั้งสอง movement)

1. Lower trunk → **ลงราบ 0°**
2. Leg → **ยกขึ้น 45°**

> ✅ **ใช้เตียง ICU ปรับอัตโนมัติเสมอ** — ห้ามให้ผู้ตรวจยก leg เองเพราะ muscle contraction จาก active lifting confound ค่า
> 

> ✅ ทำ **พร้อมกัน** — ทำทีละขั้นทำให้ effect ไม่ครบ
> 

### Step 3 — วัด Peak Response

รอ **60 วินาที** หลังเปลี่ยนท่า → วัด CO/VTI ที่ **นาทีที่ 1** (peak ~60–90 วินาที; effect ลดหลัง 2–3 นาที)

**Echo (LVOT VTI)**:

- Apical 5-chamber → PW Doppler ที่ LVOT ใต้ aortic valve ~5 mm
- Trace waveform **3 consecutive beats** → average
- บันทึก VTI_PLR

**EtCO₂**:

- อ่านค่า peak ใน 1 นาทีแรก → บันทึก EtCO₂_PLR

### Step 4 — คำนวณ % Change

ΔVTI = (VTI_PLR − VTI_baseline) / VTI_baseline × 100

ตัวอย่าง: Baseline 18 cm → PLR 21 cm → ΔVTI = +16.7% → Fluid Responsive ✅

### Step 5 — กลับท่าเดิม + Reversibility Check

กลับ semi-recumbent 45° ทันที → รอ 2–3 นาที → CO/VTI ควรกลับ baseline (ถ้าไม่กลับ = มี confounding factor)

---

### Interpretation

| ผล | ความหมาย | ทำต่อ |
| --- | --- | --- |
| **ΔVTI/ΔCO ≥ 10–15%** | Fluid Responsive | พิจารณา fluid challenge 250–500 mL |
| **ΔVTI/ΔCO < 10%** | Non-responsive | หา cause อื่น ไม่ให้ fluid เพิ่ม |
| **ΔEtCO₂ ≥ 5%** | Responsive (surrogate) | ใช้ถ้าไม่มี echo/CO monitor |

> ⚠️ Responsive ≠ ควรให้ fluid — ต้องดู VExUS + clinical congestion ก่อนตัดสินใจเสมอ
> 

---

### Common Mistakes

| ความผิดพลาด | ผล |
| --- | --- |
| เริ่มจาก supine flat (ไม่ใช่ 45°) | Auto-bolus น้อย → false negative |
| ผู้ตรวจยก leg เอง | Muscle contraction confound → false positive |
| วัด ΔPP แทน ΔCO/ΔVTI | Sensitivity เพียง 56% → ไม่น่าเชื่อถือ |
| วัดช้าเกิน (> 2 นาที) | Effect หายแล้ว → false negative |
| ผู้ป่วย cough/agitate ระหว่างทำ | Confound ค่า |

---

### Quick Reference

```
1. Check CI (ICP? IAP?)
2. Head-of-bed 45° → วัด Baseline VTI (3 beats)
3. Trunk flat + Leg 45° พร้อมกัน (ใช้เตียง!)
4. รอ 60 วินาที → วัด PLR VTI (3 beats)
5. ΔVTI ≥ 10–15% = Responsive / < 10% = Non-responsive
6. กลับท่า 45° ทันที
7. ดู VExUS ก่อนให้ fluid
```
