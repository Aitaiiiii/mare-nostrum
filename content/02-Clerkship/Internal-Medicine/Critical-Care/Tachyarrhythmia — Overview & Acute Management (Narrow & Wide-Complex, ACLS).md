---
title: "Tachyarrhythmia — Overview & Acute Management (Narrow & Wide-Complex, ACLS)"
aliases: ["Tachyarrhythmia — Overview & Acute Management (Narrow & Wide-Complex, ACLS)", "Tachyarrhythmia"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
type: "Workflow"
guidelines: ["ACC/AHA", "ESC"]
review_status: "New"
tags: [critical-care, workflow, acc-aha, esc]
created: 2026-07-05
notion_id: 394224ab-ad81-813a-bc0b-f54e9f9129e3
source: notion-migration
---

# Tachyarrhythmia — Overview & Acute Management (Narrow & Wide-Complex, ACLS)

> **Source:** 2025 AHA Guidelines for CPR & ECC — Part 9 Adult ALS (Wigginton JG et al., *Circulation* 2025;152(16_suppl_2):S538–S577) + 2015 ACC/AHA/HRS SVT guideline (evidence update). Fellowship-level acute-management monograph. Companion to board-review page ⚡ *Arrhythmia (AF Anticoagulation, VT, AV Block, PVC & Inherited Syndromes)*.
> 

---

## 1. 🧬 Etiology & Molecular Pathophysiology

Tachyarrhythmia เกิดจาก mechanism พื้นฐานสามกลุ่มที่แยกกันชัดเจนในระดับ cellular electrophysiology และการเข้าใจ mechanism นี้เป็นตัวกำหนดทั้ง diagnosis และ therapeutic response โดยตรง

**Reentry** เป็น mechanism ที่พบบ่อยที่สุดของ sustained tachyarrhythmia เกิดขึ้นเมื่อมี circuit ที่มี two functional pathways ที่มี conduction velocity และ refractoriness ต่างกัน (unidirectional block + slow conduction) ส่งผลให้ impulse สามารถวนกลับมา re-excite tissue ที่พ้น refractory period แล้วได้อย่างต่อเนื่อง กลไกนี้อธิบาย AVNRT, AVRT, typical atrial flutter (cavotricuspid isthmus–dependent macroreentry) และ scar-related monomorphic VT เนื่องจาก circuit มีลักษณะ anatomically หรือ functionally fixed จึงทำให้ arrhythmia มักเป็น regular และ terminable ด้วย interventions ที่ block ส่วนใดส่วนหนึ่งของ circuit เช่น AV nodal blockade หรือ synchronized cardioversion

**Enhanced/abnormal automaticity** เกิดจากการที่ cell เพิ่ม phase 4 diastolic depolarization slope ผ่าน funny current (**I_f**) และ altered Ca²⁺/K⁺ handling ทำให้เกิด ectopic focus ที่ยิง impulse เร็วกว่า sinus node กลไกนี้อธิบาย focal atrial tachycardia, MAT และ automatic junctional tachycardia และเนื่องจากไม่มี reentry circuit ที่แน่นอน จึงทำให้ arrhythmia กลุ่มนี้มักไม่ตอบสนองต่อ cardioversion และ adenosine อาจเพียง suppress ชั่วคราวแล้วกลับมาใหม่

**Triggered activity** เกิดจาก afterdepolarizations สองชนิด คือ early afterdepolarization (**EAD**) ที่เกิดช่วง phase 2/3 จาก reactivation ของ L-type Ca²⁺ current ในภาวะ prolonged repolarization (long QT) ซึ่งเป็น substrate ของ torsades de pointes และ delayed afterdepolarization (**DAD**) ที่เกิดจาก intracellular Ca²⁺ overload กระตุ้น Na⁺/Ca²⁺ exchanger (transient inward current) ซึ่งอธิบาย digoxin toxicity arrhythmia และ catecholaminergic VT

---

## 2. 🩺 Clinical Phenotypes & Advanced Nuances

การจำแนกหน้างานที่ 2025 AHA guidelines ใช้ อาศัย **QRS duration** และ **regularity** เป็นแกนหลัก และมีการเปลี่ยน terminology สำคัญที่ควรทราบ

**Terminology update (2025 AHA):** guideline เลิกใช้คำว่า "SVT" แบบ imprecise แล้วเปลี่ยนมาใช้ **narrow-complex tachycardia (NCT)** ครอบคลุม sinus tachycardia, atrial flutter, AVNRT, AVRT และ atrial tachycardia อื่น ๆ โดยระบุว่าคำว่า supraventricular tachycardia เคยถูกใช้อย่างไม่แม่นยำ และใช้ **wide-complex tachycardia (WCT)** สำหรับ QRS ≥ 0.12 sec

- **Narrow-complex (QRS < 0.12 sec)** — origin อยู่เหนือ ventricle ทำให้ depolarization เดินผ่าน His-Purkinje system ตามปกติ QRS จึงแคบ; regular NCT บ่งชี้ AVNRT/AVRT/AT/flutter, ส่วน irregular NCT บ่งชี้ AF, atrial flutter with variable block หรือ MAT
- **Wide-complex (QRS ≥ 0.12 sec)** — VT มักแสดงเป็น wide-complex เนื่องจาก impulse กำเนิดใน ventricular myocardium จึง bypass His-Purkinje system และเดินผ่าน slow myocyte-to-myocyte conduction ทำให้ depolarization ล่าช้าและ QRS กว้าง; principle หน้างานคือ **treat WCT as VT until proven otherwise** เพราะ VT พบบ่อยกว่าและอันตรายกว่า SVT with aberrancy
- **Pitfall:** narrow complex ไม่ได้ rule out VT เสมอไป — fascicular VT ที่ origin ใกล้ conduction system นำเสนอเป็น narrow complex tachycardia ได้ และในทางกลับกัน SVT with pre-existing BBB หรือ rate-dependent aberrancy ก็ทำให้ NCT กลายเป็น wide complex ได้

---

## 3. 🩻 Advanced Diagnostics & Formal Criteria

หน้างานที่สำคัญที่สุดคือการประเมิน **hemodynamic stability** เพราะเป็น branch point แรกของ algorithm สัญญาณของ instability ที่ guideline ใช้ ได้แก่ hypotension, acutely altered mental status, signs of shock, ischemic chest discomfort และ acute heart failure

เกณฑ์ rate: tachycardia นิยามที่ HR > 100 bpm แต่ในภาวะเฉียบพลัน rate ≥ 150 bpm มักบ่งชี้ tachyarrhythmia ที่มีนัยสำคัญทางคลินิกและต้องประเมินเร่งด่วน — ถ้า HR < 150 และผู้ป่วย unstable ควรมองหาสาเหตุอื่นของ shock ที่ทำให้เกิด compensatory sinus tachycardia มากกว่าจะเชื่อว่า arrhythmia เป็นต้นเหตุ

**Adenosine เป็น diagnostic tool:** ใน regular tachycardia การตอบสนองต่อ adenosine ช่วยแยก mechanism ได้ — การที่ tachycardia terminate อย่างฉับพลันบ่งชี้ AVNRT/AVRT (AV node เป็นส่วนหนึ่งของ circuit), การที่ tachycardia ดำเนินต่อพร้อม transient AV block แทบจะ diagnostic ของ atrial tachycardia หรือ atrial flutter และ exclude AVRT

---

## 4. 💊 Management & Pharmacodynamics

**(2025 AHA Guidelines for CPR & ECC — Part 9 Adult ALS, *Circulation* 2025)**

Branch point คือ stability เสมอ

**► Unstable (ทุกชนิด) — Synchronized cardioversion**

- Unstable NCT → synchronized cardioversion (**COR 1**)
- Unstable WCT → presumed VT → synchronized cardioversion
- Polymorphic/torsades → sync ไม่ได้ (ไม่มี R wave ให้ sync) → treat as **unsynchronized defibrillation** เหมือน VF
- Energy (biphasic, 2025): narrow regular **50–100 J**, AF หรือ wide-complex **120–200 J** แล้ว escalate ถ้าไม่สำเร็จ; sedate ผู้ป่วยที่รู้สึกตัวก่อน

**► Stable regular NCT**

- **Vagal maneuvers** — first line (**COR 1**, LOE B-R). Modified Valsalva (Valsalva + passive leg raise) efficacy ดีกว่า standard; standard Valsalva terminate NCT ได้ 20–30% และ modified เพิ่มได้ถึง 50%. MOA: เพิ่ม vagal tone → hyperpolarize AV node → block reentry circuit ที่ผ่าน AV node
- **Adenosine** — first-line drug (**COR 1**). Dose: **6 mg rapid IV push + NS flush** → **12 mg** ถ้าไม่ได้ผล. MOA: activate **A1 receptor** → เปิด **I_KACh** (G-protein–coupled K⁺ channel) → hyperpolarize + suppress Ca²⁺-dependent AV nodal conduction → transient complete AV block. Half-life < 10 sec. ระวัง severe asthma (bronchospasm)
- **Nondihydropyridine CCB / beta-blocker** — diltiazem, verapamil, metoprolol เมื่อ vagal + adenosine ไม่ได้ผล. MOA: block L-type Ca²⁺ channel (CCB) หรือ β1 blockade → ลด AV nodal conduction velocity และเพิ่ม refractoriness
- Stable NCT ที่ persist แม้ให้ vagal + drug → synchronized cardioversion (**COR 1**, LOE B-NR)

**► Stable regular monomorphic WCT**

- IV amiodarone, procainamide หรือ sotalol อาจพิจารณา (**COR 2b**)
- ใน stable regular monomorphic WCT อาจพิจารณา IV adenosine เพื่อ treatment/diagnosis หากยังไม่ทราบ etiology (**COR 2b**)
- **ข้อห้ามสำคัญ (COR 3: Harm):** ห้าม verapamil/diltiazem ใน WCT; ห้าม adenosine ใน unstable, irregularly irregular หรือ polymorphic WCT — ใน pre-excited AF (WPW + AF) การ block AV node จะเร่ง conduction ผ่าน accessory pathway ทำให้เกิด VF ได้

**► Irregular tachyarrhythmia** (AF/AFL with variable block, MAT) — rate control + address underlying cause

---

## 5. 📚 Landmark Trials & Literature

- **Wigginton JG et al. Part 9: Adult Advanced Life Support. 2025 AHA Guidelines for CPR & ECC.** *Circulation.* 2025;152(16_suppl_2):S538–S577 — guideline ปัจจุบันที่ให้ terminology NCT/WCT และ COR/LOE ปัจจุบัน
- **REVERT trial (Appelboam A et al., *Lancet* 2015)** — RCT ยืนยันว่า modified Valsalva (postural modification) เพิ่ม cardioversion rate ของ SVT อย่างมีนัยสำคัญเทียบกับ standard Valsalva (~43% vs 17%)
- **Page RL et al. 2015 ACC/AHA/HRS Guideline for Management of Adult Patients with SVT.** *Circulation.* 2015 — foundational document
- **PROCAMIO trial (Ortiz M et al., *Eur Heart J* 2017)** — RCT เทียบ IV procainamide vs amiodarone ใน stable WCT: procainamide มี major cardiac adverse events น้อยกว่าและ termination rate สูงกว่า

---

> ⚠️ Reference เพื่อการศึกษา — energy setting และ drug choice หน้างานจริงต้องปรับตาม local protocol และปรึกษา attending/EP เสมอ โดยเฉพาะ WCT ที่ diagnosis ไม่ชัด
> 

---

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **ห้าม adenosine หรือ AV nodal blocker (verapamil/diltiazem/beta-blocker/digoxin)** ใน unstable, irregularly irregular, หรือ polymorphic WCT — เสี่ยง degenerate เป็น VF โดยเฉพาะ pre-excited AF (WPW)
> 

> - **อย่าตัด VT ทิ้งเพียงเพราะ QRS แคบ** — fascicular VT นำเสนอเป็น narrow-complex ได้; ในทางกลับกัน SVT + aberrancy/pre-existing BBB ทำให้ NCT กลายเป็น WCT ได้เช่นกัน
> 

> - **Unstable patient → synchronized cardioversion ทันที** ไม่ต้องรอวินิจฉัย mechanism ให้ชัดเจนก่อน
> 

> - **Polymorphic VT/torsades ไม่สามารถ synchronize ได้** (ไม่มี R wave ที่ชัดเจน) → ต้อง unsynchronized defibrillation เหมือน VF
> 

# 🎯 High-Yield Recall

- **2025 AHA เปลี่ยน terminology**: SVT → **narrow-complex tachycardia (NCT)**; wide-complex tachycardia (WCT) ≥0.12 sec = **treat as VT until proven otherwise**
- **Branch point แรกเสมอคือ hemodynamic stability** — unstable (ทุกชนิด) → synchronized cardioversion; polymorphic/torsades → defibrillation
- **Stable regular NCT**: vagal maneuver (modified Valsalva) → adenosine 6→12 mg IV → CCB/beta-blocker → cardioversion
- **Stable regular monomorphic WCT**: IV procainamide/amiodarone/sotalol (COR 2b); adenosine อาจช่วย diagnosis/treatment ได้ (COR 2b) แต่ห้ามใน unstable/irregular/polymorphic
- **Adenosine เป็นทั้ง diagnostic และ therapeutic tool** — termination ฉับพลัน = AVNRT/AVRT; ดำเนินต่อพร้อม transient AV block = AT/flutter

> 🇹🇭 **Thai availability:** adenosine และ amiodarone มีทั่วไปในรพ.ระดับตติยภูมิ/ทุติยภูมิส่วนใหญ่; **IV procainamide หายากและมักไม่ stock [ในหลายรพ.ไทย](http://ในหลายรพ.ไทย)** (ต้องประสานเภสัชกรรม/เตรียมล่วงหน้า) — ในทางปฏิบัติจึงมักเลือก amiodarone แม้ PROCAMIO trial จะสนับสนุน procainamide มากกว่า; sotalol มีจำกัดเฉพาะบางสถาบัน
> 

> 🔍 **Verification status**
> 

> ✅ Searched & verified (28 ก.ค. 2026): 2025 AHA ACLS terminology (NCT/WCT), adenosine/vagal maneuver first-line, energy settings, PROCAMIO/REVERT trial results
> 

> ⚠️ From source, not re-verified: exact Thai hospital-level procainamide stocking (ทราบจากความรู้ทั่วไปทางคลินิก ไม่ได้ verify เป็นรายสถาบัน) — 🔴 ผู้ใช้ควรตรวจสอบกับเภสัชกรรมของตนเอง
>
