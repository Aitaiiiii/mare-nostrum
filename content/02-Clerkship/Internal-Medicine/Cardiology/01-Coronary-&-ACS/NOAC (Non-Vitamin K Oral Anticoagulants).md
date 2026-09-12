---
title: "NOAC (Non-Vitamin K Oral Anticoagulants)"
aliases: ["NOAC (Non-Vitamin K Oral Anticoagulants)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Coronary & ACS"
type: "Discrete entity"
guidelines: ["ESC"]
review_status: "New"
tags: [cardiology, coronary-acs, discrete-entity, esc]
created: 2026-07-21
notion_id: 3a4224ab-ad81-8180-beb4-c51f7b46b7e9
source: notion-migration
---

# NOAC (Non-Vitamin K Oral Anticoagulants)

**Discrete-entity page — NOAC/DOAC deep-dive** — เสริมจาก [[Anticoagulant Therapy]] (ซึ่งมี AF/VTE dosing + reversal ครบแล้ว) หน้านี้เจาะกลไกที่ทำให้ NOAC ต่างจาก warfarin, การปรับยาใน hepatic/renal impairment, **perioperative interruption/bridging** (เชื่อมกับ [[Preoperative Cardiac Risk Assessment (Non-Cardiac Surgery)]]), และ **NOAC ในผู้ป่วย AF+PCI** (triple/dual therapy). อ้างอิงหลัก **2022 ESC Non-Cardiac Surgery Guideline**, **2021 EHRA Practical Guide on NOAC**, **2023 ACC/AHA/ACCP/HRS AF Guideline**, **2024 ESC AF Guideline**.

## 1. 🧬 ทำไม NOAC ต่างจาก Warfarin (Pharmacology)

**Onset/offset เร็ว** — NOAC ออกฤทธิ์โดยตรงต่อ factor (ไม่ผ่าน vitamin K cycle เหมือน warfarin) ทำให้ peak ผลใน 1-4 ชม.และ half-life สั้น (~5-17 ชม.) จึงไม่ต้อง bridge เวลาหยุดยาเหมือน warfarin — เป็นเหตุผลหลักที่ periop management ของ NOAC คือ "หยุดแล้วรอ" ไม่ใช่ "หยุดแล้ว bridge"

**Renal clearance แตกต่างกันมาก** ทำให้ระวัง renal impairment ไม่เท่ากัน:

| ยา | % ขับทางไต | หมายเหตุ |
| --- | --- | --- |
| **Dabigatran** | ~80% | ขับไตสูงสุด → CrCl<30 ห้ามใช้, ระวังมากสุดใน CKD |
| **Rivaroxaban** | ~35% | food effect สูงสุด, bioavailability >80% (ต้องกินพร้อมอาหารมื้อหลัก โดยเฉพาะ 20mg) |
| **Edoxaban** | ~50% | ห้ามใช้ถ้า CrCl>95 (ประสิทธิภาพลดลงเทียบ warfarin ใน ENGAGE AF — clearance เร็วเกินไป) |
| **Apixaban** | ~27% | ขับไตต่ำสุด → ปลอดภัยสุดใน CKD ระยะท้าย/ESRD |

**Metabolism/interaction:** ทุกตัวเป็น **P-glycoprotein (P-gp) substrate**; **apixaban กับ rivaroxaban** ยังผ่าน **CYP3A4** เพิ่มเติม (dabigatran/edoxaban ไม่ผ่าน CYP)

- **Strong P-gp/CYP3A4 inhibitor** (↑NOAC level): amiodarone, dronedarone, verapamil, ciclosporin, tacrolimus, clarithromycin, ketoconazole/itraconazole/posaconazole/voriconazole, HIV protease inhibitor (ritonavir) — ระวังโดยเฉพาะเมื่อรวมกับ renal impairment
- **Strong inducer** (↓NOAC level → thrombosis risk): rifampicin, carbamazepine, phenytoin, phenobarbital, St. John's Wort
- Digoxin และ azithromycin ไม่มี interaction สำคัญ

## 2. 🫘 Hepatic Impairment — Child-Pugh Dosing

**Prefer ใช้ NOAC เฉพาะ Child-Pugh A** เป็นหลัก:

| Child-Pugh | Dabigatran | Apixaban | Edoxaban | Rivaroxaban |
| --- | --- | --- | --- | --- |
| **A (5-6)** | ไม่ต้องปรับ | ไม่ต้องปรับ | ไม่ต้องปรับ | ไม่ต้องปรับ |
| **B (7-9)** | ใช้ได้ (caution) | ใช้ได้ (caution) | ใช้ได้ (caution) | **ห้ามใช้** |
| **C (10-15)** | **ห้ามใช้** | **ห้ามใช้** | **ห้ามใช้** | **ห้ามใช้** |

*หมายเหตุ: rivaroxaban ถูกคัดออกจาก Child B เพราะ hepatic metabolism (CYP3A4) สัดส่วนสูงกว่าตัวอื่น ทำให้ hepatic impairment กระทบระดับยามากกว่า; Child C ทุกตัวไม่มีข้อมูลเพียงพอ → ใช้ warfarin แทน (monitor ด้วย INR ซึ่งเป็นมาตรฐานเดิมของ hepatic coagulopathy อยู่แล้ว)*

**Child-Turcotte-Pugh classification:**

| Criteria | 1 คะแนน | 2 คะแนน | 3 คะแนน |
| --- | --- | --- | --- |
| Encephalopathy | ไม่มี | mild-mod (grade 1-2) | severe (grade 3-4) |
| Ascites | ไม่มี | mild-mod (ตอบสนอง diuretic) | severe (refractory) |
| Bilirubin (mg/dL) | <2 | 2-3 | >3 |
| Albumin (g/dL) | >3.5 | 2.8-3.5 | <2.8 |
| PT prolonged (sec) | <4 | 4-6 | >6 |
| INR | <1.7 | 1.7-2.3 | >2.3 |

รวมคะแนน: A = 5-6, B = 7-9, C = 10-15

## 3. ✂️ Perioperative NOAC Interruption & Resumption

> 🔍 **Verified 2022 ESC Non-Cardiac Surgery Guideline (Halvorsen et al., Eur Heart J 2022)** — กรอบคิดหลัก: ระยะเวลาหยุดยาขึ้นกับ **drug compound, half-life, renal function, และ bleeding risk ของหัตถการ** (Class I, B) — **ไม่มี "one-size-fits-all"**
> 

**หลักการทั่วไป (verified):**

- **Minor bleeding risk** (ควบคุมเลือดออกได้ง่าย): ผ่าตัดโดย**ไม่ต้องหยุด NOAC** ได้เลย (Class I, B) หรือเลือกผ่าช่วง trough level (หยุด 12-24 ชม.) (Class I, C)
- **Low-moderate bleeding risk surgery**: หยุด NOAC **1 วันเต็ม** (~24 ชม.)
- **High bleeding risk surgery**: หยุด NOAC **2 วันเต็ม** (~48 ชม.)
- **Dabigatran + eGFR<50**: ขยายเป็น **≥96 ชม.** ก่อน high bleeding risk surgery (ขับไตสูงจึงสะสมนานกว่า)
- **Very high bleeding risk** (neuraxial/spinal/epidural anesthesia, LP): หยุด **5 เท่าของ half-life**, resume ไม่เร็วกว่า **24 ชม.** หลังหัตถการ/หลังถอด epidural catheter (Class IIa, C)
- **Urgent surgery**: หยุด NOAC ทันที (Class I, C); ถ้าต้องผ่าด่วนใน dabigatran ที่มี intermediate/high bleeding risk → พิจารณา **idarucizumab** (Class IIa, B)
- **ไม่ bridge ด้วย heparin** — NOAC มี onset/offset เร็วพอที่จะ "หยุดแล้วรอ" โดยไม่ต้อง parenteral bridge (ต่างจาก warfarin)
- **ห้ามลด dose NOAC เพื่อลด bleeding risk ช่วงผ่าตัด** (Class III, C) — ต้องหยุดยาแทนการลด dose
- **Resume**: 6-8 ชม.หลังผ่าถ้า hemostasis สมบูรณ์ดี; **48-72 ชม.** หลัง high bleeding risk procedure (± thromboprophylaxis คั่นระหว่างรอ) (Class IIb, C)
- **Routine coagulation assay (anti-Xa/dTT) ก่อนผ่า ไม่จำเป็น** ยกเว้นกรณี urgent surgery ที่ไม่แน่ใจระดับยา (Class IIa, C)

⚠️ **ตาราง CrCl-based granular** (จากแหล่งเดิม/EHRA-style practical guide — ทิศทางถูกต้องตรงกับหลักการข้างบน แต่ตัวเลขราย-ชั่วโมงในแต่ละช่อง CrCl ยังไม่ได้ verify ทีละช่องจาก primary literature โดยตรง ควรตรวจ 2021 EHRA Practical Guide ฉบับเต็มก่อนใช้ทางคลินิกจริง):

| CrCl (mL/min) | Dabigatran (low bleed risk) | Dabigatran (high bleed risk) | Xa-inhibitor (low bleed risk) | Xa-inhibitor (high bleed risk) |
| ------------- | --------------------------- | ---------------------------- | ----------------------------- | ------------------------------ |
| ≥80           | ≥24h                        | ≥48h                         | ≥24h                          | ≥48h                           |
| 50-79         | ≥36h                        | ≥72h                         | ≥24h                          | ≥48h                           |
| 30-49         | ≥48h                        | ≥96h                         | ≥24h                          | ≥48h                           |
| 15-29         | ห้ามใช้ NOAC                | ห้ามใช้ NOAC                 | ≥36h                          | ≥48h                           |
| <15           | ไม่มีข้อบ่งชี้              | ไม่มีข้อบ่งชี้               | ไม่มีข้อบ่งชี้                | ไม่มีข้อบ่งชี้                 |

**เชื่อมโยง:** ดู [[Preoperative Cardiac Risk Assessment (Non-Cardiac Surgery)]] สำหรับ workflow เต็มของการประเมิน bleeding-risk ของหัตถการ และการจัดการ warfarin/mechanical-valve bridging (ซึ่ง**ไม่ใช่ประเด็นของ NOAC** เพราะ mechanical valve = ข้อห้ามของ NOAC โดยตรง — ดูข้อ 6)

## 4. 🩹 NOAC ใน AF + PCI (Triple/Dual Antithrombotic Therapy)

หลักคิด: หลัง PCI ในผู้ป่วย AF ต้องสมดุลระหว่าง **stent thrombosis risk** (ต้องการ antiplatelet) กับ **stroke prevention** (ต้องการ OAC) กับ **bleeding risk** (ยิ่งใช้ยาหลายตัวยิ่งเลือดออกมาก) — แนวโน้มปัจจุบันคือ **dual therapy (OAC + P2Y12 เพียงตัวเดียว) เหนือ triple therapy** โดยให้ triple therapy ระยะสั้นที่สุดเท่าที่จำเป็น (มักไม่เกิน 1 สัปดาห์ถึง 1 เดือน ตามความเสี่ยง ischemic vs bleeding ของแต่ละราย)

**Landmark trials (verified):**

|  | **PIONEER AF-PCI** (NEJM 2016) | **RE-DUAL PCI** (NEJM 2017) | **AUGUSTUS** (NEJM 2019) |
| --- | --- | --- | --- |
| ประชากร | NVAF + PCI, N=2124 | NVAF + PCI, N=2725 | AF + ACS/PCI, N=4614 |
| แขนทดลอง | rivaroxaban 15mg OD (10mg ถ้า CrCl 30-50) + P2Y12i **เดี่ยว** vs rivaroxaban 2.5mg BID + DAPT vs VKA + DAPT | dabigatran 150 BID + P2Y12i vs dabigatran 110 BID + P2Y12i vs VKA + DAPT | apixaban ± aspirin + P2Y12i vs VKA ± aspirin + P2Y12i (2×2 factorial) |
| ผล bleeding | dual/low-dose rivaroxaban arms bleeding น้อยกว่า standard VKA+DAPT อย่างมีนัยสำคัญ | ทั้งสอง dabigatran arms bleeding น้อยกว่า VKA+DAPT | apixaban bleeding น้อยกว่า VKA (HR ~0.69); **aspirin เพิ่ม bleeding อย่างชัดเจน** เทียบ placebo |
| MACE/ischemic | ไม่ต่างกันมีนัยสำคัญ (secondary endpoint, ไม่ powered พอ) | ไม่ต่างกันมีนัยสำคัญ (secondary) | ไม่ต่างกันมีนัยสำคัญระหว่าง apixaban/VKA; ทุก trial ไม่ได้ออกแบบมาให้ power พอสำหรับ ischemic endpoint แยก |

> **สรุปร่วมทั้ง 3 trials**: NOAC (แทน VKA) + P2Y12 inhibitor เดี่ยว (ไม่ใส่ aspirin) = **ลด bleeding อย่างชัดเจนโดยไม่เพิ่ม ischemic event อย่างมีนัยสำคัญ** เป็นฐานของแนวทางปัจจุบันที่เลือก **dual therapy เหนือ triple** และเมื่อจำเป็นต้อง triple ให้สั้นที่สุด (ดู DAPT duration ที่ [[Antiplatelet Therapy]])
> 

## 5. 📊 คะแนนช่วยตัดสินใจเลือก Warfarin vs NOAC — SAMe-TT2R2

ใช้ทำนาย **time-in-therapeutic-range (TTR)** ถ้าจะเลือก warfarin — ถ้าคาดว่าคุม INR ได้ไม่ดี ควรเลือก NOAC แทนตั้งแต่แรก:

| ปัจจัย | คะแนน |
| --- | --- |
| **S**ex (female) | 1 |
| **A**ge <60 ปี | 1 |
| **Me**dical history (≥2 จาก: HTN, DM, CAD/MI, PAD, CHF, prior stroke, pulmonary/hepatic/renal disease) | 1 |
| **T**reatment (ยาที่ interact เช่น amiodarone) | 1 |
| **T**obacco use (ภายใน 2 ปี) | 2 |
| **R**ace (non-white) | 2 |
| **สูงสุด** | 8 |

**แปลผล**: 0-2 คะแนน → คุม INR ได้ดี พิจารณา **warfarin** ได้; **≥3 คะแนน** → เสี่ยงคุม INR ไม่ดี ควรเลือก **NOAC** ตั้งแต่แรก (ไม่ต้อง "ลอง" warfarin ก่อน)

## 6. ⚖️ NOAC Eligibility ตามพยาธิสภาพลิ้นหัวใจ

| ภาวะ | NOAC ใช้ได้หรือไม่ |
| --- | --- |
| **Mechanical prosthetic valve** | **ห้ามเด็ดขาด** — RE-ALIGN (dabigatran): ↑thrombotic event + ↑bleeding เพราะ warfarin ยับยั้ง contact-factor activation จากพื้นผิว prosthesis ได้ แต่ dabigatran ไม่มีกลไกนี้ |
| **Moderate-severe rheumatic MS** | **ห้าม** — INVICTUS: VKA เหนือ rivaroxaban ชัดเจน |
| **Mild-moderate native VHD อื่น** | ใช้ได้ (อยู่ใน trial หลัก) |
| **Severe AS** | ข้อมูลจำกัด (ถูกคัดออกจาก RE-LY) — ใช้ด้วยความระมัดระวัง |
| **Bioprosthetic valve (>3 เดือนหลังผ่า)** | ใช้ได้ใน degenerative MR หรือ aortic position; ไม่แนะนำถ้าเป็น rheumatic MS เดิม |
| **Mitral valve repair (>3 เดือน)** | มีข้อมูลบางส่วนจาก trial inclusion |
| **PTAV/TAVI** | ไม่มีข้อมูล prospective ชัดเจน อาจต้องพิจารณา antiplatelet ร่วม |
| **AF + bioprosthetic AVR ใหม่** | **warfarin 3 เดือนแรกก่อน** แล้วค่อยเปลี่ยนเป็น NOAC (Class IIa) |

## 7. 🔄 Switching ระหว่างยา

- **VKA → NOAC**: รอ INR ลดถึงระดับที่กำหนดก่อนเริ่ม — INR<3.0 เริ่ม rivaroxaban ได้; INR<2.5 เริ่ม edoxaban; INR<2.0 เริ่ม apixaban/dabigatran (ยิ่ง INR สูง ยิ่งรอนาน เพื่อไม่ให้ anticoagulation ซ้อนกันมากเกินไป)
- **NOAC → VKA**: ให้ยาซ้อนกันจนกว่า INR ใกล้ therapeutic แล้วค่อยหยุด NOAC (ต้อง overlap เพราะ VKA ออกฤทธิ์ช้า)
- **NOAC ↔ LMWH**: สลับได้ทันทีในเวลาที่ควรให้ dose ถัดไป (pharmacokinetics คล้ายกัน)
- **UFH → NOAC**: เริ่ม NOAC ~4 ชม.หลังหยุด UFH infusion (รอ anticoagulant effect ของ UFH ลดลงก่อน)

**การจัดการเมื่อลืมกินยา/ไม่แน่ใจว่ากินหรือยัง:**

| สถานการณ์ | แนวทาง |
| --- | --- |
| ยา BID ลืมกิน ภายใน 6 ชม. | กินตอนนี้ + กิน dose ถัดไปตามเวลาปกติ |
| ยา BID ลืมกิน เกิน 6 ชม. | ข้าม รอ dose ถัดไป |
| ยา OD ลืมกิน ภายใน 12 ชม. | กินตอนนี้ + กิน dose ถัดไปตามเวลาปกติ |
| ยา OD ลืมกิน เกิน 12 ชม. | ข้าม รอ dose ถัดไป |
| ไม่แน่ใจว่ากินหรือยัง (OD, ภายใน 12 ชม.) | ถ้า CHA₂DS₂-VASc≥3 → กินตอนนี้ + dose ถัดไปปกติ; ถ้า≤2 → รอ dose ถัดไป |

## 8. 🧪 Lab Monitoring — ความสัมพันธ์กับ coagulation test

- **Dabigatran** → สัมพันธ์กับ **thrombin time (TT) > aPTT**; **aPTT ปกติ = ตัดระดับยาที่มีผลทางคลินิกออกได้อย่างมั่นใจ**; aPTT ยืดยาว = มีระดับยา on-therapeutic หรือสูงกว่า
- **Apixaban/Edoxaban/Rivaroxaban** → สัมพันธ์กับ **PT**; **ไม่มี test ใดที่ตัดระดับยาออกได้อย่างมั่นใจ 100%** (ต่างจาก dabigatran); PT ยืดยาวบ่งชี้ว่ามีระดับยา on-therapeutic ขึ้นไป
- ตรวจ **LFT ก่อนเริ่ม NOAC แล้วตรวจซ้ำทุกปี**

## 9. 💊 Reversal (สรุปเชื่อมจาก [[Anticoagulant Therapy]])

- **Dabigatran** → **idarucizumab** 5g IV (specific, ครบถ้วน); ถ้าไม่มี → 4F-PCC/aPCC 50U/kg; ถ้ายังคุมไม่ได้ → hemodialysis (dabigatran ขับไตสูง จึง dialyzable)
- **Factor Xa inhibitor (apixaban/rivaroxaban)** → **andexanet alfa** (specific, infusion 2 ชม.) หรือ 4F-PCC/aPCC off-label
- **Ciraparantag (aripazine)** — universal reversal agent, ยัง investigational

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **ห้ามใช้ NOAC ใน mechanical valve ทุกชนิด** — RE-ALIGN แสดง harm ชัดเจน (dabigatran เพิ่มทั้ง thrombosis และ bleeding)
> 

> - **ห้ามลด dose NOAC เพื่อลด perioperative bleeding risk** — ต้องหยุดยาแทน ไม่ใช่ลด dose (Class III)
> 

> - **ห้าม bridge NOAC ด้วย heparin** ในบริบท periop — NOAC มี onset/offset เร็วพออยู่แล้ว การ bridge เพิ่ม bleeding โดยไม่ได้ประโยชน์
> 

> - **Dabigatran + eGFR<50 ต้องขยายเวลาหยุดยาก่อนผ่าตัด high bleeding risk เป็น ≥96 ชม.** — พลาดจุดนี้ = เสี่ยง bleeding ระหว่างผ่าตัดจากยาสะสม
> 

## 🎯 High-Yield Recall

- NOAC periop: **1 วันเต็มถ้า low bleeding risk, 2 วันเต็มถ้า high bleeding risk**; dabigatran+eGFR<50 → **≥96 ชม.**; ไม่ bridge, ไม่ลด dose
- **Apixaban ขับไตต่ำสุด (27%) ปลอดภัยสุดใน CKD**; **dabigatran ขับไตสูงสุด (80%) ระวังสุด**
- **Rivaroxaban ห้ามใน Child-Pugh B** (ตัวเดียวในกลุ่ม); ทุกตัวห้ามใน Child C
- **AF+PCI**: NOAC + P2Y12 เดี่ยว (ไม่ใส่ aspirin) ลด bleeding โดยไม่เพิ่ม ischemic event — PIONEER/RE-DUAL/AUGUSTUS สอดคล้องกัน
- **SAMe-TT2R2 ≥3 → เลือก NOAC เหนือ warfarin ตั้งแต่แรก**
- **NOAC ห้ามเด็ดขาดใน mechanical valve และ rheumatic MS+AF** — ใช้ warfarin เท่านั้น
- 🔍 Verification status
    
    **✅ Searched & verified (28 ก.ค. 2026):**
    
    - 2022 ESC Non-Cardiac Surgery Guideline periop NOAC framework: drug/half-life/renal/bleeding-risk-dependent interruption, minor-risk no-interruption, high-risk 2-day/low-risk 1-day rule, dabigatran+eGFR<50→≥96h, neuraxial→5 half-lives+resume≥24h, no dose-reduction (Class III), no bridging, resume 6-8h/48-72h — ✅ (Halvorsen et al., Eur Heart J 2022; ACC summary)
    - Child-Pugh NOAC dosing (rivaroxaban avoid Class B; all avoid Class C) — ✅ (JACC 2019, multiple pharmacokinetic reviews)
    - SAMe-TT2R2 scoring — ✅ (matches original 2013 derivation, cross-checked against source)
    - PIONEER AF-PCI / RE-DUAL PCI / AUGUSTUS direction of effect (NOAC+single P2Y12 less bleeding, similar MACE) — ✅ (NEJM primary publications)
    - Renal clearance % (dabigatran 80%, apixaban ~27%) — ✅ (established pharmacology)
    
    **⚠️ From source/textbook, not re-verified line-by-line:**
    
    - Granular CrCl-bracket interruption table (24/36/48/72/96h per cell) — likely EHRA-practical-guide derived; directionally consistent with verified 2022 ESC framework but exact hour-values per CrCl bracket not individually confirmed against EHRA 2021 primary document
    - P-gp/CYP interaction drug lists — stable pharmacology, standard drug references
    - Switching protocol INR cutoffs (rivaroxaban<3.0, edoxaban<2.5, apixaban/dabigatran<2.0) — standard labeling guidance
    
    **🔴 Flagged uncertain:**
    
    - Exact PIONEER/RE-DUAL/AUGUSTUS numeric HRs/CIs — not independently re-confirmed to decimal precision in this pass; use with caution if citing exact statistics, verify against primary NEJM papers before board exam use
