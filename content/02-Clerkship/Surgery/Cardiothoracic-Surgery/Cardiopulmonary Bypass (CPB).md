---
title: "Cardiopulmonary Bypass (CPB) — Circuit & Physiology (CVT)"
aliases: ["Cardiopulmonary Bypass (CPB) — Circuit & Physiology (CVT)", "Cardiopulmonary Bypass (CPB)"]
stage: Clerkship
rotation: "Surgery"
specialty: "Cardiothoracic Surgery"
type: "Discrete entity"
guidelines: ["EACTS", "STS"]
review_status: "New"
tags: []
created: 2026-08-04
notion_id: 3b2224ab-ad81-815f-b29f-d63dfdeec96e
source: notion-migration
updated: 2026-09-14
---

# Cardiopulmonary Bypass (CPB) — Circuit & Physiology (CVT)

<aside>
🫀

**Short Note in CVT — A1 · CPB & Perioperative core (SNC-CVT Template C: perioperative/physiology).** เพจนี้คือ principle + physiology ของ cardiopulmonary bypass ที่เป็นฐานของทุก open-heart operation. Myocardial protection/cardioplegia → A2 · deep hypothermia + cerebral protection → A3 · vasoplegia + post-CPB coagulopathy → A4 · MCS (รวม VA-ECMO ซึ่งเป็น CPB ดัดแปลง) → A5 และ [[MCS (Mechanical Circulatory Support)]].

</aside>

**Contents**

- Principle & physiology — ทำอะไร
- Circuit components (ไล่ตาม blood path)
- Pump & oxygenator options
- Conduct of CPB — anticoagulation, flow, temp targets
- Systemic effects & pitfalls
- Key numbers

## 1. ⚙️ Principle & physiology

**Cardiopulmonary bypass (CPB)** ทำหน้าที่ heart และ lung ชั่วคราว โดยดึง venous blood ออกจากร่างกายก่อนเข้า heart นำไป oxygenate นอกร่างกายแล้ว pump กลับเข้า arterial system ทำให้ surgeon มี bloodless, motionless field ขณะที่ systemic perfusion ยังดำเนินต่อ

เป้าหมายเชิงสรีรวิทยาที่ CPB ต้องทำให้ได้พร้อมกันมี 4 ข้อ: 

(1) รักษา tissue oxygen delivery ให้เพียงพอขณะ native circulation หยุด 

(2) ควบคุม gas exchange ผ่าน membrane oxygenator 

(3) ควบคุม temperature ผ่าน heat exchanger 

(4) กัน clot ใน circuit ด้วย systemic anticoagulation ทั้งสี่ข้อนี้เดินพร้อมกันตลอดเวลาที่อยู่บน pump

## 2. 🔀 Circuit components (ไล่ตาม blood path)

blood เดินเป็นวงจากตัวผู้ป่วย → circuit → กลับเข้าตัวผู้ป่วย เรียงตามลำดับ:

![image.png](Cardiopulmonary%20Bypass%20(CPB)%20%E2%80%94%20Circuit%20&%20Physiolog/image.png)

| Component | หน้าที่ |
| --- | --- |
| **Venous cannula** | ดึง deoxygenated blood ออกจาก RA (RA canular/ 2 stage) — เช่นใน CABG ที่จะไม่เปิด heart หรือ bicaval (SVC+IVC) ด้วย gravity siphon หรือ vacuum-assisted drainage |
| **Venous reservoir** | พัก blood + เป็น buffer volume; **open** (มี blood-air interface, capacity มาก, จัดการ air ง่าย) vs **closed** (sterile กว่า แต่ capacity น้อย เสี่ยง air embolism ต้องระวัง) |
| **Main pump** | สร้าง arterial flow — roller หรือ centrifugal (ดูหัวข้อถัดไป) |
| **Membrane oxygenator** | gas exchange — blood ไหลด้านหนึ่งของ hollow fiber, gas (O₂ + sweep) อีกด้าน — ทำหน้าที่ lung |
| **Heat exchanger** | มัก integrate กับ oxygenator; น้ำอุณหภูมิควบคุมไหลคนละ compartment กับ blood — cool/rewarm |
| **Arterial line filter / bubble trap** | ดัก gaseous + particulate microemboli ก่อนเลือดกลับเข้าตัว |
| **Arterial cannula** | คืน oxygenated blood สู่ aorta (หรือ axillary/femoral) — จุด return |

นอก blood path หลักยังมี **cardiotomy suction** (ดูด blood จาก surgical field กลับ reservoir), **vent** (decompress LV กัน distension), และ **cardioplegia delivery line** (→ A2) โดย cardiotomy suction เป็นแหล่ง contact activation + hemolysis + microemboli ที่สำคัญ เพราะ blood สัมผัสทั้ง air และ tissue factor จาก wound

## 3. 🔁 Pump & oxygenator options

**Roller vs centrifugal pump** — decision ที่ส่งผลต่อ hemolysis และ safety:

![Screenshot 2569-08-04 at 15.40.40.png](Cardiopulmonary%20Bypass%20(CPB)%20%E2%80%94%20Circuit%20&%20Physiolog/Screenshot_2569-08-04_at_15.40.40.png)

|  | Roller pump | Centrifugal pump |
| --- | --- | --- |
| **กลไก** | occlusive — บีบ tubing เป็นจังหวะ, flow คงที่ (ไม่ขึ้นกับ afterload) | non-occlusive — ปั่น impeller, flow ขึ้นกับ afterload (preload/afterload-dependent) |
| **ข้อดี** | flow แม่นยำ, ต้นทุนต่ำ | hemolysis น้อยกว่า, ถ้า air เข้าจะ deprime ตัวเอง (ไม่ปั๊ม air เข้าคน) |
| **ข้อเสีย** | ถ้า outflow occlude → สร้าง pressure สูงจน tubing แตก; ปั๊ม air ได้ถ้า reservoir แห้ง | ต้องมี flow meter (ดู flow ตรงๆ ไม่ได้จาก RPM), ราคาสูงกว่า |

**Oxygenator** ปัจจุบันเป็น membrane (hollow-fiber) เกือบทั้งหมด แทน bubble oxygenator รุ่นเก่า เพราะ bubble oxygenator มี direct blood-gas interface ที่ทำให้ protein denaturation และ gaseous embolism มากกว่า

## 4. 🧪 Conduct of CPB — anticoagulation, flow, temp targets

### Anticoagulation (ขั้นตอนที่ safety-critical ที่สุด)

<aside>
🚨

**ห้ามเริ่ม CPB ก่อนได้ ACT ถึง target** — เลือดที่สัมผัส synthetic surface โดยไม่ anticoagulate เต็มที่ → clot ใน circuit → catastrophic thromboembolism

</aside>

- **Heparin (unfractionated) bolus ~300–400 U/kg IV** ก่อน cannulation (บางตำราใช้ 3 mg/kg ≈ 300 U/kg)
- **Target ACT >480 วินาที ก่อนเริ่ม CPB** (สถาบันส่วนใหญ่ใช้ช่วง 400–500 วินาที); ลดลงได้ถึง ~300 วินาทีถ้าใช้ heparin-coated (biocompatible) circuit
- **Reversal ด้วย protamine** หลัง wean off CPB (~1 mg protamine ต่อ 100 U heparin) — ระวัง protamine reaction (hypotension, pulmonary hypertension, anaphylaxis)
- กรณี **heparin resistance** (มักจาก AT III deficiency) → ACT ไม่ขึ้นถึง target → เติม AT III หรือ FFP

### Flow & pressure targets

- **Pump flow index 2.2–2.4 L/min/m²** ที่ normothermia (เทียบ cardiac index ปกติ); ลดได้เมื่อ hypothermia เพราะ metabolic demand ลด (Q₁₀ effect)
- **MAP 60–80 mmHg** — CPB ให้ non-pulsatile flow จึงคุมด้วย flow เป็นหลัก, MAP ต่ำเกินไปใช้ vasopressor (norepinephrine/phenylephrine), MAP สูงไปใช้ vasodilator
- **Hematocrit 25–30%** — hemodilution จาก priming volume; ต่ำกว่านี้เสี่ยง tissue hypoxia, สูงเกินเสี่ยง viscosity/transfusion
- ติดตาม adequacy ด้วย **SvO₂ (>70%), lactate, urine output, NIRS** (cerebral oximetry)

### Temperature

- ส่วนใหญ่ทำที่ **mild-moderate hypothermia (32–36°C)** หรือ normothermia เพื่อลด metabolic demand ขณะ arrest
- **Deep hypothermia (≤20°C, นิยาม 2024)** สงวนไว้เฉพาะเมื่อต้องทำ circulatory arrest (aortic arch work) → รายละเอียดที่ A3

## 5. ⚠️ Systemic effects & pitfalls

**Post-perfusion SIRS** — ผลกระทบทาง physiology ที่สำคัญที่สุดของ CPB blood สัมผัส nonendothelial synthetic surface (tubing, oxygenator, reservoir) ทำให้เกิด contact activation ของ complement, kallikrein-kinin, coagulation-fibrinolytic cascade ร่วมกับ neutrophil activation ต่อเนื่องไปจนเกิด cytokine storm (IL-6, IL-8, TNF-α) ส่งผลให้เกิด capillary leak, vasoplegia และ organ dysfunction ซึ่งร่วมกับ ischemia-reperfusion injury และ surgical trauma ในผู้ป่วยส่วนน้อย subclinical และ resolve เอง แต่ในราย extreme พัฒนาเป็น MODS ได้ (vasoplegia รายละเอียด → A4)

**Hemodilution & fluid shift** — priming volume ของ circuit (~1.5–2 L crystalloid) เจือก blood volume ทำให้ Hct ตก, oncotic pressure ลด → tissue edema; ทางแก้คือ retrograde autologous priming (RAP) หรือ minimize circuit

**Non-pulsatile flow** — CPB มาตรฐานให้ continuous non-pulsatile flow อาจกระทบ microcirculation และ baroreceptor แต่ผลลัพธ์ทางคลินิกเทียบ pulsatile ยังถกเถียง

<aside>
🚨

**STRICT AVOIDANCE / RED FLAGS**

- **ห้ามเริ่ม CPB ก่อน ACT >480** — clot ใน circuit คือ catastrophe; ตรวจ ACT ซ้ำก่อนเสมอถ้าสงสัย heparin resistance
- **ระวัง air embolism** — โดยเฉพาะ closed reservoir ที่ capacity น้อย หรือ centrifugal pump ที่ deprime; air เข้า arterial line → cerebral air embolism
- **ห้าม clamp arterial outflow ขณะ roller pump ยังเดิน** — สร้าง pressure สูงจน tubing แตก/disconnect
- **Protamine reaction** — ให้ช้าๆ ระวัง hypotension/pulmonary vasoconstriction โดยเฉพาะคนที่เคยได้ protamine (NPH insulin, prior exposure, fish allergy)
</aside>

<aside>
🎯

**High-Yield Recall**

- **Blood path:** venous cannula → reservoir → pump → membrane oxygenator + heat exchanger → arterial filter → aortic cannula
- **Heparin ~300–400 U/kg → ACT >480s ก่อนเริ่ม CPB** (safety-critical); reverse ด้วย protamine ~1 mg / 100 U heparin
- **Flow index 2.2–2.4 L/min/m² · MAP 60–80 mmHg · Hct 25–30%** ที่ normothermia
- **Roller** = occlusive, flow คงที่, เสี่ยง overpressure/air; **centrifugal** = afterload-dependent, hemolysis น้อย, ไม่ปั๊ม air
- **SIRS** = contact activation (complement/cytokine/coagulation) → capillary leak/vasoplegia; extreme → MODS
- **Deep hypothermia ≤20°C** (นิยาม 2024) → A3; myocardial protection → A2
</aside>

- 🔍 Verification status
    
    **✅ Searched & verified (web, 4 ส.ค. 2026):**
    
    - Heparin bolus ~300–400 U/kg (3 mg/kg); ACT >480s ก่อนเริ่ม CPB (institutional 400–500), ลด ~300s ถ้า heparin-coated circuit (AATS TSRA primer; JCVA 2020; BL Lifesciences)
    - Pump flow index 2.2–2.4 L/min/m² standard (สูงได้ 2.9); MAP 60–80 mmHg; Hct 25–30%; temp 33–36°C (Anesthesiology RCT PMC12416890)
    - Circuit components + open vs closed reservoir + roller vs centrifugal + membrane oxygenator (OpenAnesthesia; ScienceDirect CPB equipment)
    - SIRS mechanism: contact activation → complement/kallikrein/cytokine/coagulation cascade + neutrophil; >25% มี feature; extreme → MODS (PubMed 17462274; PMC10875393)
    
    **⚠️ From source/textbook, ไม่ได้ re-verify effect size:**
    
    - Priming volume ~1.5–2 L, protamine ratio ~1 mg/100 U heparin เป็นค่ามาตรฐานตำรา
    - Q₁₀ effect / non-pulsatile flow physiology เป็น concept-level
    
    **🔴 Flagged uncertain:**
    
    - ACT target ไม่มี high-level evidence กำหนดตายตัว — >480 เป็น convention, สถาบันต่างกัน 400–500; device-dependent (kaolin vs celite activator)
    - Pulsatile vs non-pulsatile clinical outcome ยังไม่ชัด

LV vent

- drain เลือดที่กลับเข้า left system (มี bronchial system ที่ไปเลี้ยงปอดกลับมาอยู่)
- RSPV, Ao root ที่ใช้ drain

![image.png](Cardiopulmonary%20Bypass%20(CPB)%20%E2%80%94%20Circuit%20&%20Physiolog/image%201.png)
