---
title: "Inotropes & Vasopressors — Infusion Reference (conc / rate / titration)"
type: "Standing Order"
specialty: "Cardiology"
ward: ["Medicine"]
also_relevant: ["Cardiology", "Critical Care medicine"]
tags: [workflow]
notion_id: 3b2224ab-ad81-8191-8c21-f957ff8c3bca
source: notion-migration
---

# Inotropes & Vasopressors — Infusion Reference (conc / rate / titration)

<aside>
⚠️

**Salt vs base trap** — norepinephrine/epinephrine ที่ label เป็น **tartrate/bitartrate** มี base concentration ประมาณครึ่งหนึ่งของ label total เพราะรวมมวล counterion เข้าไปด้วย (2024 SCCM/ESICM position paper) การ chart dose โดยไม่ระบุ salt form ทำให้ dose คลาดเคลื่อนได้ถึง ~50% ต้องระบุ form + unit ให้ชัดในทุก order

</aside>

<aside>
📋

Concentration ที่ให้เป็นค่ามาตรฐานสากล (ASHP/Stanford/institutional protocols) ทุกสถาบันมี premix ต่างกัน ต้อง cross-check กับ pharmacy และ pump library soft/hard limits ก่อนสั่งจริง ตัวเลข titration เป็น general guide สำหรับ provider-driven titration

</aside>

---

## 1. Norepinephrine (Levophed) — first-line vasopressor

- **Norepinephrine 4 mg + D5W 250 mL IV = 16 mcg/mL** (double strength 8 mg/250 mL = 32 mcg/mL สำหรับ fluid restriction)
    
    ↳ *เจือจางใน D5W เพราะ norepinephrine ถูก oxidation ทำลายฤทธิ์ใน saline solution แม้ทางปฏิบัติหลายที่ผสมใน NSS ได้ในระยะสั้น*
    
- **Start 0.05 mcg/kg/min IV** (non-WBD เริ่ม 5 mcg/min) — rate 10 ml/hr
- **Titrate ↑ 0.05 mcg/kg/min q5min** จนได้ MAP ≥65 mmHg
- **Range 0.05–0.5 mcg/kg/min; soft ceiling ~1 mcg/kg/min**
    
    ↳ *เมื่อ dose ถึงช่วง 0.25–0.5 mcg/kg/min ควรเริ่มมองหา second agent (vasopressin) แทนการดัน norepinephrine เดี่ยวขึ้นไปเรื่อย ๆ เนื่องจากผลข้างเคียงเพิ่มขึ้นโดยที่ประโยชน์ต่อ MAP เริ่มลดลง*
    
- **Access:** central line เป็นหลัก; peripheral ได้ระยะสั้น (<48 hr, low dose) ที่ conc เจือจาง 64 mcg/mL
- 🇹🇭 มีทุก รพ.

![[inotropes-vasopressors-infusion-referenc-img-7618.jpeg]]

![[inotropes-vasopressors-infusion-referenc-img-7619.jpeg]]

<aside>
🚨

**Extravasation** → phentolamine 5–10 mg เจือจางฉีดรอบบริเวณที่รั่วทันที ป้องกัน tissue necrosis จาก local vasoconstriction

</aside>

---

## 2. Vasopressin — fixed-dose adjunct (ไม่ titrate)

- **Vasopressin 20 units + NSS/D5W 100 mL IV = 0.2 unit/mL**
- **Fixed dose 0.03 unit/min IV คงที่** — เพิ่มเข้าไปเมื่อ norepinephrine ถึง 0.25–0.5 mcg/kg/min (SSC 2021)
    
    ↳ *ให้เป็น catecholamine-sparing adjunct เพื่อลดขนาด norepinephrine ไม่ใช่ให้เพื่อไล่ MAP จึงไม่ต้อง titrate ตาม BP เหมือน catecholamine การเพิ่ม vasopressin ลดอุบัติการณ์ atrial fibrillation เมื่อใช้คู่ norepinephrine*
    
- **ไม่ต้อง titrate** — septic shock ไม่ควรเกิน 0.03–0.04 unit/min; vasoplegia หลัง cardiac surgery ใช้ได้ถึง 0.1 unit/min
- **Wean:** ระวัง rebound hypotension เมื่อถอน ให้ค่อย ๆ ลดตาม protocol
- 🇹🇭 มีในไทยแต่ราคาสูง บางสถาบัน stock จำกัด

<aside>
🚨

Dose >0.04 unit/min เพิ่มความเสี่ยง **digital / mesenteric ischemia** ชัดเจนโดยไม่มีประโยชน์เพิ่ม — ห้ามดัน dose เกินช่วงนี้เพื่อไล่ MAP

</aside>

---

## 3. Epinephrine (Adrenaline) — third-line vasopressor / anaphylaxis / cardiogenic

- **Epinephrine 4 mg + D5W 250 mL IV = 16 mcg/mL** (บางที่ทำ 2 mg/250 mL = 8 mcg/mL)
    
    ↳ *ASHP แนะนำจงใจตั้ง concentration ให้ต่างจาก norepinephrine เพื่อลดความสับสนระหว่างสองตัวที่หน้าตา order คล้ายกัน*
    
- **Start 0.01–0.05 mcg/kg/min IV**
- **Titrate ↑ 0.02–0.05 mcg/kg/min q10–15min** ตาม MAP และ perfusion
- **Range 0.01–0.5 mcg/kg/min** (refractory ใช้ได้ถึง ~3)
- **Access:** central line
- 🇹🇭 มีทุก รพ. (ampoule 1 mg/mL)

<aside>
🚨

กระตุ้น β2-mediated glycolysis ทำให้ **lactate สูงขึ้น** ได้โดยไม่ได้แปลว่า perfusion แย่ลง อย่าไล่ dose ตาม lactate เพียงอย่างเดียว และทำให้ HR เร็ว/arrhythmia มากกว่า norepinephrine

</aside>

---

## 4. Dopamine — เลี่ยงใน septic shock, ใช้เมื่อไม่มี NE หรือมี bradycardia

- **Dopamine 400 mg + D5W 250 mL IV = 1,600 mcg/mL** (double 800 mg/250 mL = 3,200 mcg/mL)
- **Start 5 mcg/kg/min IV**
- **Titrate ↑ 1–2.5 mcg/kg/min q5–10min**
- **Range 2–20 mcg/kg/min**
    
    ↳ *ฤทธิ์ขึ้นกับขนาด: ขนาดต่ำออกฤทธิ์ dopaminergic ขนาดกลางออกฤทธิ์ β1 และขนาดสูงกว่า 10 mcg/kg/min ออกฤทธิ์ α1 เป็นหลัก so-called renal-dose dopamine ไม่มีประโยชน์ต่อการปกป้องไต*
    
- **Access:** central line only
- 🇹🇭 มีทุก รพ.

<aside>
🚨

SSC 2021 แนะนำ **against dopamine** เป็น first-line ใน septic shock เพราะเพิ่ม arrhythmia และ mortality เทียบกับ norepinephrine (meta-analysis RR 0.89 favoring NE) — ใช้เฉพาะเมื่อไม่มี norepinephrine หรือในผู้ป่วยที่มี bradycardia ร่วม

</aside>

---

## 5. Dobutamine — inotrope หลักใน low cardiac output

- **Dobutamine 500 mg + D5W 250 mL IV = 2,000 mcg/mL (2 mg/mL)**
- **Start 2.5 mcg/kg/min IV**
- **Titrate ↑ 2.5 mcg/kg/min q10min** ตาม cardiac index และ perfusion
- **Range 2.5–20 mcg/kg/min** (max 40 ในบาง protocol)
- **Goal:** cardiac index >2.5; ลด/หยุดเมื่อ HR >120 หรือเกิด ventricular arrhythmia
- 🇹🇭 มีทุก รพ.

<aside>
🚨

β2-mediated vasodilatation ทำให้เกิด **hypotension** ได้โดยเฉพาะเมื่อ volume ไม่พอ และในผู้ป่วยที่ได้ β-blocker อยู่ dobutamine จะถูก block ต้องใช้ dose สูงขึ้นหรือเปลี่ยนไปใช้ milrinone แทน

</aside>

---

## 6. Milrinone — inodilator (PDE-3 inhibitor)

- **Milrinone 20 mg + D5W/NSS 100 mL IV = 200 mcg/mL**
- **Loading (optional):** 50 mcg/kg IV over 10–20 min
    
    ↳ *ทางปฏิบัติมักข้าม loading dose เพราะทำให้เกิด hypotension ชัดเจนจาก vasodilatation เฉียบพลัน*
    
- **Maintenance 0.125–0.75 mcg/kg/min IV** (max 1.5)
- **ไม่ต้อง titrate ถี่** — ปรับตาม cardiac output และ BP; onset ช้ากว่า catecholamine
    
    ↳ *ขับทางไต 83% ในรูปไม่เปลี่ยนแปลง half-life ยาวประมาณ 2.5 ชั่วโมง จึงสะสมในผู้ป่วย renal impairment ต้องลดขนาดตาม eGFR*
    
- 🇹🇭 มีในไทยแต่ราคาสูง

<aside>
🚨

Vasodilatation ร่วมกับ half-life ยาว → **hypotension ที่แก้ยาก** เพราะถอนยาแล้วฤทธิ์ยังคงอยู่นาน ระวังเป็นพิเศษใน CKD/AKI ที่ยาสะสม

</aside>

---

## 7. Phenylephrine — pure α1, ใช้เมื่อ tachyarrhythmia ห้าม β

- **Phenylephrine 50 mg + NSS 250 mL IV = 200 mcg/mL** (bedside push 100 mcg/mL)
- **Infusion 0.2–1 mcg/kg/min IV**, titrate ตาม MAP (range ถึง 5 ในบาง protocol)
- **Bolus 50–200 mcg IV push** สำหรับ transient hypotension เช่นช่วง peri-intubation
    
    ↳ *เป็น pure vasoconstrictor ที่ไม่กระตุ้น β จึงเหมาะเมื่อ norepinephrine ทำให้ HR เร็วเกินไป หรือมี atrial fibrillation with rapid ventricular response*
    
- 🇹🇭 มีทุก รพ.

<aside>
🚨

**Reflex bradycardia** จาก pure α1 vasoconstriction และลด cardiac output ในผู้ป่วยที่ pump อ่อนอยู่แล้ว จึงไม่ควรใช้เป็น pressor หลักใน cardiogenic shock

</aside>

---

## 8. Angiotensin II (Giapreza) — refractory vasodilatory shock (rescue)

- **เจือจางเป็น 5,000 ng/mL** ใน NSS (หรือ 10,000 ng/mL เมื่อ fluid restrict)
- **Start 20 ng/kg/min IV**
- **Titrate ↑ q5min ในช่วง 3 ชั่วโมงแรก, max 80 ng/kg/min** ใน 3 ชั่วโมงแรก จากนั้น maintenance ไม่เกิน 40 ng/kg/min
    
    ↳ *ใช้ใน distributive shock ที่ยังต้องการ norepinephrine >0.2 mcg/kg/min (ATHOS-3) ประโยชน์ต่อ survival เด่นใน subgroup ที่ต้อง renal replacement therapy หรือมี renin สูง*
    
- 🇹🇭 **ยังไม่มีจำหน่ายในไทย** (FDA approved ธ.ค. 2017)

<aside>
🚨

เพิ่มความเสี่ยง **thrombosis / DVT** ชัดเจน — ต้องให้ DVT prophylaxis ตลอดระยะเวลาที่ใช้ยา

</aside>

---

## 🎯 High-Yield Recall

- **Norepinephrine** first-line ทุก shock; 16 mcg/mL, start 0.05 mcg/kg/min, spare ด้วย vasopressin ที่ NE 0.25–0.5
- **Vasopressin** fixed 0.03 unit/min ไม่ titrate; เป็น adjunct ไม่ใช่ rescue เดี่ยว
- **Salt vs base**: tartrate/bitartrate = ครึ่งหนึ่งของ base — ระบุ form เสมอ
- **Dopamine** เลี่ยงใน sepsis (arrhythmia + mortality); renal-dose ไร้ประโยชน์
- **Dobutamine** ถูก β-blocker บัง → เปลี่ยน milrinone; **milrinone** สะสมใน renal impairment, half-life ยาว
- **Phenylephrine** → reflex bradycardia + ลด CO; **Angiotensin II** → DVT risk, ยังไม่มีในไทย

---

- 🔍 Verification status
    
    **✅ Searched & verified (04 ส.ค. 2026):**
    
    - Norepinephrine conc 16 mcg/mL, start/titration, salt-vs-base issue — ASHP standard concentrations + 2024 SCCM/ESICM position paper
    - Vasopressin 0.03 unit/min fixed, add-on ที่ NE 0.25–0.5 — Surviving Sepsis Campaign 2021
    - Dopamine against first-line ใน sepsis (RR 0.89) — SSC 2021 + meta-analysis
    - Dobutamine/dopamine/epinephrine/phenylephrine conc + titration — ASHP + institutional titration tables (Augusta, Ventura, Stanford)
    - Milrinone 0.125–0.75 mcg/kg/min, renal accumulation — pulmccm review 2026
    - Angiotensin II 20 ng/kg/min start, max 80 (3 hr) — ATHOS-3 / Giapreza labeling
    
    **⚠️ Institution-dependent (ต้อง cross-check):**
    
    - Premix concentrations และ double-strength variants ต่างกันแต่ละ รพ.
    - Pump library soft/hard limits
    - Peripheral vs central line policy

<aside>
⚠️

สำหรับใช้เป็น reference / teaching ต้องปรับตาม premix, nursing protocol และ attending ของสถาบันก่อนสั่งจริง

</aside>
