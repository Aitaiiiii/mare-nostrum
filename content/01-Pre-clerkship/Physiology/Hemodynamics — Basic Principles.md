---
title: "Hemodynamics — Basic Principles"
aliases: ["Hemodynamics — Basic Principles", "Hemodynamics"]
stage: Pre-clerkship
specialty: "Physiology"
related: ["[[Physiology (Map)]]", "[[Cardiology (Map)]]"]
type: "Discrete entity"
guidelines: ["ACC/AHA", "ESC"]
review_status: "New"
tags: []
created: 2026-07-21
notion_id: 3a4224ab-ad81-81b9-a251-ff4305d7320d
source: notion-migration
updated: 2026-09-14
---

# Hemodynamics — Basic Principles

หน้านี้เป็น **hub ของ invasive hemodynamics ในห้องสวนหัวใจ** ครอบคลุม Swan-Ganz, การวัด cardiac output (Fick / thermodilution), การคำนวณ resistance, shunt (Qp:Qs), valve area (Gorlin), pressure waveforms และ PV loops. สำหรับ mechanical circulatory support ดูรายละเอียดที่ [[MCS (Mechanical Circulatory Support)]]; สำหรับ coronary physiology (FFR/iFR) ดู [[Coronary Blood Flow & Ischemia]]

> ⚠️ **หมายเหตุความปลอดภัยของสูตร (formula sanity):** ค่าคงที่ในสูตร hemodynamics เป็นตัวกำหนดผลลัพธ์โดยตรง ค่าคงที่ผิดทำให้ valve area ผิดแบบเงียบ ๆ สูตรในหน้านี้ทุกตัว **ตรวจสอบกับแหล่งอ้างอิงแล้ว** (ดู 🔍 Verification status ท้ายหน้า) และได้ **แก้ค่าคงที่ที่คลาดเคลื่อนจากต้นฉบับ** ไว้แล้ว (Gorlin aortic = 44.3 ไม่ใช่ 44.5; mitral = 37.7 ไม่ใช่ 38; stroke work = 0.0136 ไม่ใช่ 0.0144)
> 

## 1. 🎈 Swan-Ganz (Pulmonary Artery Catheter, PAC)

**ข้อบ่งชี้ (ไม่ทำ routine — ไม่มี mortality benefit):** ประเมิน hemodynamic ที่ไม่แน่นอน, cardiogenic shock ระยะสั้น, ประเมินก่อน heart transplant / MCS, refractory/recurrent HF, ช่วย wean inotrope

**Contraindications:** severe coagulopathy/thrombocytopenia, TV/PV mechanical prosthesis, pacemaker lead ที่เพิ่งใส่, LBBB (เสี่ยง complete heart block เพราะ catheter อาจกด RBB — เตรียม pacing)

**ระยะทางโดยประมาณจากตำแหน่งใส่ (แต่ละช่วง < 15 cm):** ผ่านลำดับ IJV, RA, RV, PA จนถึง PCWP ตามลำดับ; ปลาย catheter ควรอยู่ **West zone 3** (ครึ่งล่างของปอด) เพื่อให้ PCWP สะท้อน LAP จริง

| Parameter | ค่าปกติ |
| --- | --- |
| RA (mean) | 0–6 mmHg |
| RV | 24/0–6 mmHg |
| PA | 24/8–12 (mean < 20) mmHg |
| PCWP (mean) | < 12 mmHg |
| Cardiac index (CI) | 2.5–4.0 L/min/m² |
| SVR | 800–1200 dyne·s·cm⁻⁵ |
| PVR | < 3 Wood units (< 240 dyne·s·cm⁻⁵) |

**PCWP ↔ LVEDP:** ปกติ PCWP ≈ LVEDP (วัด PCWP ที่ **จุดเริ่ม QRS หรือกึ่งกลางของ a-wave / c-wave**). ปกติ mean PCWP ต่ำกว่า PA diastolic ~1–3 mmHg

- **PCWP > LVEDP:** MS, mitral annular calcification, MR, PE, LA myxoma, cor triatriatum
- **PAEDP < PCWP (ผิดปกติ):** decreased LV compliance, สูง LVEDP, AR
- **Severe MR:** mean PCWP อาจ > PA diastolic (giant v wave)
- **Pulmonary HTN:** mean PCWP ต่ำกว่า PA diastolic ≥ 3 mmHg

**Invasive exercise hemodynamics:** เมื่อ resting PCWP ปกติแต่ยังสงสัย HFpEF ให้ต่อด้วย supine cycle exercise ผ่าน PAC เดิม เกณฑ์วินิจฉัยคือ **peak exercise PCWP ≥25 mmHg** ในท่า supine (ท่านั่ง/upright ใช้ ≥20 mmHg) ต่างจาก resting cutoff **≥15 mmHg** ที่ใช้วินิจฉัยได้เลยเมื่อค่าสูงอยู่แล้วโดยไม่ต้องออกกำลัง (รายละเอียด phenotype ดูหน้า HFpEF)

**PEEP effect:** ทุก ๆ PEEP ที่เพิ่ม 5 mmHg → PCWP อ่านสูงขึ้นเทียม ~2–3 mmHg

**Damping:** overdamped = คลื่นแบน (air bubble/clot/kink); underdamped = ring artifact/overshoot

## 2. 🌊 Pressure Waveforms (RA/CVP · PCWP · a-c-v)

**RA/CVP:** prominent **a wave** (atrial contraction); **PCWP:** prominent **v wave** (LA filling). LA เทียบ PCWP: v wave ของ PCWP มา **ช้ากว่า** (delay จากการส่งผ่านปอด)

**ความสัมพันธ์กับ ECG:** a wave ตามหลัง P ~80 ms (ราว R wave); c wave = valve bulging ต้น systole (= LVEDP บน monitor); v wave ~ T wave; x descent = atrial relaxation; y descent = ventricular filling หลัง AV valve เปิด

| สิ่งที่เห็น | สาเหตุ |
| --- | --- |
| Large a wave | ↑RA resistance (TS, tricuspid atresia, RA myxoma) หรือ ↓RV compliance (PHT, PS, acute PE, RV infarct) |
| Cannon a wave | AV dissociation (atrium บีบใส่ปิด TV) — complete heart block, VT |
| Absent a wave | AF |
| Giant v wave (> 10 mmHg) | ขวา (CVP): TR, ASD; ซ้าย (PCWP): MR, MS, VSD, LV failure |
| Rapid/deep y descent | Constrictive pericarditis, RCM |
| Blunted y descent | Tamponade, TS, atrial myxoma |

## 3. 💉 Cardiac Output — Fick & Thermodilution

**Fick principle** (แม่นในภาวะ high-output; ต้อง steady state):

```
CO (L/min) = VO₂ / [ Hb × 1.34 × 10 × (SaO₂ − SvO₂) ]
```

- VO₂ = oxygen consumption (mL/min) — วัดตรง หรือประมาณจาก nomogram (~3 mL/kg หรือ 125 mL/min/m²)
- 1.34–1.36 mL O₂/g Hb (oxygen-carrying capacity; แหล่งอ้างอิงใช้ต่างกันเล็กน้อย); ×10 แปลงหน่วย Hb g/dL → g/L
- SaO₂, SvO₂ = สัดส่วน (เช่น 0.95); **SvO₂ ใช้ mixed venous จาก PA**
- High CO → AV O₂ difference แคบ; Low CO → AV O₂ difference กว้าง

**Thermodilution:** CO แปรผกผันกับพื้นที่ใต้กราฟ (AUC) ของ temperature curve

- **Underestimate (อ่านต่ำกว่าจริง):** severe TR/PR, severe AR
- **Overestimate / ไม่น่าเชื่อถือ:** low-output state, severe MR, L→R หรือ R→L shunt, AF/irregular HR
- **ความแม่นภายใต้เงื่อนไขอุดมคติ:** Fick ~10%, TD 5–20%; TD แม่นกว่าใน low-output ถ้าไม่มี TR/shunt

**Mixed venous saturation (โดย echo/สูตร):** SvO₂ = (3×SVC + IVC)/4. ปกติ IVC O₂sat > SVC O₂sat (ไตได้เลือดมากแต่สกัด O₂ น้อย); Low CO → ↑extraction → **low SvO₂**; sepsis/cyanide poisoning → เซลล์สกัด O₂ ไม่ได้ → **high SvO₂**

## 4. 🔁 Resistance (PVR · SVR)

```
SVR (Wood units) = (MAP − RAP) / CO
PVR (Wood units) = (mPAP − PCWP) / CO
Wood units × 80 = dyne·s·cm⁻⁵
```

- PVR ปกติ < 3 Wood units; **PVRi = PVR × BSA** (คูณ ไม่ใช่หาร)
- SVR ปกติ 800–1200 dyne·s·cm⁻⁵

## 5. 🕳️ Shunt Detection (Qp:Qs & O₂ step-up)

```
Qp/Qs = (SaO₂ − SvO₂) / (PvO₂ − PaO₂)
```

โดย SaO₂ = systemic arterial (aorta), SvO₂ = mixed venous, PvO₂ = pulmonary vein, PaO₂ = pulmonary artery

- **Qp:Qs > 1.5** = significant L→R shunt (พิจารณาปิด); **< 1.0** = R→L shunt
- **O₂ step-up ที่มีนัยสำคัญเมื่อ Qp:Qs > 1.3**

**7-5-5-7 rule (O₂ saturation step-up thresholds):**

| ระดับ | Δ%Sat | Min Qp:Qs | DDx |
| --- | --- | --- | --- |
| Atrial (SVC/IVC→RA) | ≥ 7% | 1.5–1.9 | ASD, PAPVR, VSD+TR, ruptured sinus of Valsalva, coronary fistula to RA, Gerbode defect |
| Ventricular (RA→RV) | ≥ 5% | 1.3–1.5 | VSD, PDA+PR, coronary fistula to RV |
| Great vessel (RV→PA) | ≥ 5% | 1.3 | Aortopulmonary window, aberrant coronary, PDA |
| Any level (SVC→PA) | ≥ 7% | 1.3 | ทั้งหมดข้างต้น |

## 6. 🫀 Valve Area — Gorlin, Hakki, Continuity, PHT

**Gorlin (ค่าคงที่ต่างกันตามลิ้น — ตรวจสอบแล้ว):**

```
AVA (cm²) = CO(mL/min) / [ 44.3 × SEP(s/beat) × HR × √(mean gradient) ]
MVA (cm²) = CO(mL/min) / [ 37.7 × DFP(s/beat) × HR × √(mean gradient) ]
```

- Valve flow = CO / (SEP × HR) สำหรับ aortic; = CO / (DFP × HR) สำหรับ mitral
- SEP = systolic ejection period (aortic opening → dicrotic notch); DFP = diastolic filling period
- 🔴 **ต้นฉบับใช้ 44.5 (aortic) และ 38 (mitral) — ผิด**; ค่าคงที่ที่ถูกต้องคือ **44.3** และ **37.7**

**Hakki (simplified — ประมาณเร็ว):** `Valve area ≈ CO(L/min) / √(peak-to-peak หรือ mean gradient)` — แม่นน้อยกว่า Gorlin โดยเฉพาะเมื่อ HR ผิดปกติมาก (ไม่คิด SEP/DFP)

**Continuity equation (echo):** `AVA = 0.785 × D²_LVOT × (VTI_LVOT / VTI_AV)`; Dimensionless index = VTI_LVOT / VTI_AV; SV = 0.785 × D²_LVOT × VTI_LVOT

**Bernoulli:** `ΔP = 4v²`; ถ้า proximal velocity > 1 m/s → `ΔP = 4(v²_distal − v²_proximal)`

**Pressure half-time:** `MVA (MS) = 220/PHT`; `TVA (TS) = 190/PHT`; `PHT (ms) = 0.29 × deceleration time`

**Stroke work (ตรวจสอบแล้ว):** `SW (g·m/beat) = SV × (MAP − PCWP) × 0.0136`; SWI = SW/BSA (ปกติ ~50–62 g·m/m²/beat)

- 🔴 ต้นฉบับใช้ 0.0144 — ค่าคงที่ที่ถูกต้องคือ **0.0136** (แปลง mmHg·mL → g·m)

**Coronary flow reserve** = peak hyperemic velocity / baseline velocity; **FFR** = mean distal pressure / mean aortic pressure (ดูรายละเอียด cutoff ที่หน้า FFR)

## 7. 💧 Fluid Responsiveness

**Positive-pressure ventilation cutoffs:**

- **SVV > 13%**; **PPV > 11%** (TV ≥ 7 mL/kg) หรือ **> 8%** (TV < 7 mL/kg); PPV = (PPmax − PPmin)/[(PPmax+PPmin)/2] × 100
- **IVC distensibility > 15%** (วัด 1 cm จาก hepatic vein junction)
- **Spontaneous breathing:** IVC collapsibility index > 40%

**Fluid challenge / passive leg raise (PLR):** responsive = CO ↑ ≥ 15% หลังให้ colloid 500 mL/15 นาที (thermodilution); PLR (นั่ง 45° → นอนราบ ยกขา 45°) + CO monitor, cutoff **CO ↑10% (intubated) / 12% (spontaneous)** — จำกัดใน ↑intra-abdominal pressure/severe hypovolemia. LV dysfunction ใช้ crystalloid > 200 mL/15–30 นาที. Fluid responsiveness ≠ hypovolemia

## 8. 🔀 PV Loops (Pressure-Volume)

**Mechanical circulatory support:**

| Device | Afterload | Contractility | Preload |
| --- | --- | --- | --- |
| IABP | ↓ | เท่าเดิม | เท่าเดิม |
| LVAD | เท่าเดิม | เท่าเดิม (เสีย isovolumic periods → loop เป็นรูปสามเหลี่ยม) | ↓ (unloading) |
| VA-ECMO | ↑ | เท่าเดิม | ↓ |
| Impella | ↓ wall stress/afterload | เท่าเดิม | ↓ LV volume |

**Disease-state loops:** HOCM = เลื่อนไป volume เล็ก pressure สูง (outflow obstruction); Tamponade = คล้าย MS แต่ pressure ต่ำ (↓preload); ASD = คล้าย MS แต่ ↓LV systolic pressure; PDA = ↑SV, ↓afterload/LV systolic pressure (คล้าย MR แต่ isovolumic contraction ปกติ); TOF = ช่วง isovolumic contraction กลับมี volume ลดลง (สัมพันธ์กับ R→L shunt fraction)

**Intervention:** CRT = เลื่อนซ้าย + ↑contractility; post-MitraClip / post-TAVI = เปลี่ยน Ees line

## 9. 📉 Valvular & Pericardial Waveform Patterns

**AS / HOCM:**

- Doppler mean gradient ≈ cath mean; Doppler peak gradient ≈ **peak instantaneous** cath; cath **peak-to-peak < peak instantaneous**
- **Carabello's sign** (AVA < 0.6 cm²): เมื่อดึง catheter จาก LV → aorta, aortic pressure ↑ > 5 mmHg (catheter เดิมกีดขวางรู valve แคบ)
- **Brockenbrough–Braunwald–Morrow sign (HOCM):** หลัง PVC → ↑LVOT gradient แต่ **aortic pulse pressure ลดลง** (ต่างจาก valvular AS ที่ pulse pressure เพิ่ม); arterial waveform **spike-and-dome**, early-peaking
- Post-PVC ใน AS: ↑pulse pressure, ↑gradient; arterial upstroke ช้า (pulsus parvus et tardus)

**MS:** gradient คร่อม diastole; พื้นที่ระหว่าง PCWP กับ LVEDP diastolic curve = mean gradient; หลัง PBMV ที่เกิด severe MR → hypotension + ↓pulse pressure

**RV infarct:** RAP/PCWP > 0.8 (หรือ CVP/PCWP ≥ 0.67); RA prominent y; Kussmaul's

**Constrictive vs Restrictive vs Tamponade vs RV infarct:**

| Parameter | Constrictive | Restrictive (RCM) |
| --- | --- | --- |
| EDP equalization (LVEDP−RVEDP) | ≤ 5 mmHg | > 5 mmHg |
| PA systolic | < 55 mmHg | > 55 mmHg |
| RVEDP / RVSP | > 1/3 | ≤ 1/3 |
| Dip-plateau (square-root sign) | มี (> 7 mmHg) | อาจมี (> 7 mmHg) |
| Ventricular interdependence (inspiration) | RV↑/LV↓ discordance | concordant (RV↓/LV↓) |
| Kussmaul's sign | มี | respiratory variation ปกติ |
- **Constrictive:** deep X + deep Y (W-shape, pressure สูง); square-root sign; RV–LV **discordance** ตอนหายใจเข้า (สำคัญที่สุด)
- **Restrictive:** blunt X, deep Y; RV–LV **concordance**
- **Tamponade:** deep X, blunt Y (M/square); pulsus paradoxus บ่อย; RA/RV diastolic collapse
- **Effusive-constrictive:** tracing เปลี่ยนจาก tamponade → constrictive หลังเจาะน้ำ
- **DDx ของ LVEDP−RVEDP < 5 mmHg:** RCM, tamponade, severe TR, decompensated L-HF, RV infarct, acute MR

**Hemodynamic pattern table (Table 52-10):**

| ภาวะ | RA | RV | PA | PCW | CI |
| --- | --- | --- | --- | --- | --- |
| Normal | 0–6 | 25/0–6 | 25/0–12 | 6–12 | ≥ 2.5 |
| AMI ไม่มี LVF | 0–6 | 25/0–6 | 30/12–18 | ≤ 18 | ≥ 2.5 |
| AMI + LVF | — | 25–40/0–6 | 30–40/18–25 | > 18 | < 2.0 |
| Biventricular failure | > 6 | 50–60/>6 | 50–60/25 | 18–25 | < 2.0 |
| RV infarct | 12–20 | 30/12–20 | 30/12 | ≤ 12 | < 2.0 |
| Tamponade | 12–16 | 25/12–16 | 25/12–16 | 12–16 | < 2.0 |
| PE (acute) | 12–20 | 50–60/— | 50–60 | ≤ 12 | < 2.0 |

(RV infarct: RAP/PCWP > 0.8; tamponade = diastolic equalization ของทุกห้อง)

## 10. 🩹 IABP & Miscellaneous

- **Shock on IABP:** hypotension + low pulse pressure; **augmented pressure = aortic diastolic peak** (ไม่ใช่ systolic peak)
- **PDA:** pullback Ao→PA; PDA+PHT+AS → LV→Ao→PDA→PA→RV pullback
- CVP = RA end-diastolic (zone A/B); RVSP = PASP ถ้าไม่มี PS

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **ค่าคงที่ Gorlin ผิด = valve area ผิดแบบเงียบ ๆ** — aortic **44.3**, mitral **37.7** (อย่าใช้ 44.5/38); ตรวจ SEP/DFP ให้ตรงลิ้น
> 

> - **Gorlin ไม่น่าเชื่อถือใน low-flow state** (CO ต่ำ, LVEF ต่ำ) — under-estimate area ได้ → ใช้ dobutamine challenge หรือ CT calcium score ยืนยัน low-flow low-gradient AS
> 

> - **อย่าลืม PEEP ทำให้ PCWP อ่านสูงเทียม** (~2–3 mmHg ต่อ PEEP 5); อ่าน PCWP ที่ **end-expiration** เสมอ
> 

> - **PAC ไม่ได้ลด mortality** (ESCAPE trial, JAMA 2005, n=433: 6-month mortality และ days-alive-out-of-hospital ไม่ต่างจาก clinical assessment อย่างเดียว, adverse event จาก catheter สูงกว่า) ใช้เมื่อ hemodynamic ไม่ชัดเจน ไม่ใช่ routine
> 

> - **Thermodilution ห้ามเชื่อใน severe TR / shunt / low-output** — ใช้ Fick แทน
> 

> - **LBBB + จะใส่ PAC** → เตรียม pacing (เสี่ยง complete heart block ชั่วคราว)
> 

## 🎯 High-Yield Recall

- **Fick:** CO = VO₂ / (Hb × 1.34 × 10 × (SaO₂−SvO₂)); high CO → narrow AV O₂ diff
- **Gorlin:** AVA = CO / (44.3 × SEP × HR × √mean grad); MVA ใช้ **37.7** + DFP
- **Hakki:** valve area ≈ CO / √gradient (quick, ไม่คิด SEP)
- **Resistance:** Wood units × 80 = dyne·s·cm⁻⁵; PVR = (mPAP−PCWP)/CO
- **Qp:Qs = (SaO₂−SvO₂)/(PvO₂−PaO₂)**; step-up rule **7-5-5-7**; Qp:Qs > 1.5 = ปิด
- **Carabello** (AVA<0.6): aortic pressure ↑>5 หลัง pullback; **Brockenbrough** (HOCM): post-PVC pulse pressure **ลด**
- **Constrictive vs Restrictive:** equalization ≤5 vs >5; PASP <55 vs >55; RV–LV **discordance = constrictive**
- **RV infarct:** RAP/PCWP > 0.8; **Tamponade:** blunt Y; **Constriction:** deep Y (square-root)
- 🔍 Verification status
    
    **✅ Searched & verified (27 ก.ค. 2026):**
    
    - **Gorlin constant:** aortic **44.3**, mitral **37.7** — ยืนยัน (wikidoc/JSCAI/omnicalculator). ⚠️ ต้นฉบับ SNC6 ใช้ 44.5 (aortic) และ 38 (mitral) ในหลาย part → **แก้เป็น 44.3/37.7 แล้ว**
    - **Fick:** CO = VO₂/(Hb×1.34×10×(SaO₂−SvO₂)); 1.34–1.36 mL O₂/g Hb ใช้ต่างกันตามแหล่ง — ✅ (StatPearls)
    - **Qp:Qs = (SaO₂−SvO₂)/(PvO₂−PaO₂)** — ✅ (ต้นฉบับพิมพ์ denominator ผิดเป็น pulm vein−pulm vein → แก้แล้ว)
    - **Stroke work constant 0.0136** (SV×(MAP−PCWP)×0.0136) — ✅ (LVSWI refs); ต้นฉบับใช้ 0.0144 → แก้แล้ว
    - FFR ≤0.80 / iFR ≤0.89 — ✅ (ใช้ที่หน้า FFR)
    
    **✅ Searched & verified (29 ก.ค. 2026, revision audit):**
    
    - **ESCAPE trial (JAMA 2005, n=433):** PAC-guided therapy ไม่ลด 6-month mortality หรือเพิ่ม days-alive-out-of-hospital เทียบกับ clinical assessment อย่างเดียว และมี adverse event จาก catheter สูงกว่า — ยืนยัน claim เดิมถูกต้องและตรงกับ trial ที่อ้างจริง
    - **Invasive exercise PCWP ≥25 mmHg (supine) / ≥20 mmHg (upright)** สำหรับวินิจฉัย HFpEF เมื่อ resting PCWP ปกติ — ✅ เพิ่มเป็นเนื้อหาใหม่รอบนี้ สอดคล้องกับเกณฑ์ gold standard invasive testing
    - **PPV/SVV fluid-responsiveness thresholds:** meta-analysis 2024 (69 studies, n=2711 fluid challenges) ยืนยัน pooled threshold PPV ~11.5% (95%CI 10.5–12.4%, AUC 0.87), SVV ~12.1% (95%CI 10.9–13.3%, AUC 0.87) — สอดคล้องกับค่าที่ใช้ในหน้านี้ (PPV 11%/8%, SVV 13%)
    
    **⚠️ From source/textbook, not independently re-verified:**
    
    - 7-5-5-7 step-up thresholds, Table 52-10 hemodynamic patterns, PHT constants (220/190), fluid responsiveness cutoffs (SVV13/PPV11-8/IVC15/PLR10-12) — เป็นค่าคลาสสิกจากตำรา cath (Kern/Grossman) ผลเป็นที่ยอมรับ
    - Carabello 0.6 cm² / >5 mmHg, RAP/PCWP>0.8 RV infarct — textbook values
    
    **🔴 ข้อควรระวังทางคลินิก:** Gorlin under-estimate ใน low-flow; Hakki ไม่แม่นเมื่อ HR สุดขั้ว — ยืนยันด้วย imaging เสมอ

## 🔗 Related maps
- [[Physiology (Map)]]
- [[Cardiology (Map)]]

