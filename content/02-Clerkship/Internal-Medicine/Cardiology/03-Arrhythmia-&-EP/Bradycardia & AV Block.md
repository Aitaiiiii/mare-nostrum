---
title: "Bradycardia — Approach & AV Block"
aliases: ["Bradycardia — Approach & AV Block", "Bradycardia"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Arrhythmia & EP"
type: "Workflow"
review_status: "New"
tags: [workflow]
created: 2026-07-21
notion_id: 3a4224ab-ad81-8187-8188-db03c0dd5078
source: notion-migration
related: ["[[Arrhythmia Order Set]]"]
sources: ["2026-09/20260903-1401-line-2bebe353"]
updated: 2026-09-14
---

# Bradycardia — Approach & AV Block

> Workflow (Hub) · companion: [[Device Indications (PPM, ICD, CRT)]] · [[Temporary Pacing]] · [[Basic Electrophysiology]] — *populated 26 ก.ค. 2026 จาก digest SNC4*
> 

# 📐 Definition & mechanism

เกณฑ์ HR ที่ใช้เรียก bradycardia มีสองชุด และยังใช้ปนกันอยู่

- เกณฑ์ดั้งเดิม — HR **<60 bpm** ในผู้ใหญ่ที่ไม่ใช่นักกีฬาที่ฝึกหนัก
- 2018 ACC/AHA/HRS — HR **<50 bpm** โดยให้ 50-100 bpm เป็นช่วงปกติ (ผู้ป่วยส่วนน้อยที่มีอาการตั้งแต่ HR ยังไม่ต่ำกว่า 50)

ตัวเลข HR อย่างเดียวจึงยังไม่พอให้รักษา การตัดสินใจอิงอาการที่สัมพันธ์กับ HR ต่ำเป็นหลัก

กลไกของ bradycardia มีสองแบบ

- Impulse initiation — SA node ปล่อย impulse ช้าลงจาก phase 4 depolarization หรือ autonomic tone
  สาเหตุคือ intrinsic SA node disease, autonomic, ยา และ metabolic → sinus node dysfunction (section 1)
- Impulse conduction — impulse เกิดขึ้นแล้วแต่ไปไม่ถึง ventricle ตำแหน่ง block มีสามระดับ
  - SA exit block (อยู่ใน section 1 เพราะนับเป็นส่วนหนึ่งของ SND)
  - AV nodal block
  - Infranodal (His-Purkinje) block

  สาเหตุคือ fibrosis, intrinsic AV node disease, autonomic, ยา และ metabolic

ตำแหน่ง block เป็นตัวกำหนด escape rhythm การตอบสนองต่อ atropine และความจำเป็นของ pacemaker (ตารางใน section 2)

# 🚨 Reversible causes ก่อนเสมอ (T-DIE)

ก่อนสรุปว่าต้อง pacemaker ถาวร ต้องคัดกรองสาเหตุที่แก้ไขได้:

- **T** — Thyroid (hypothyroid) / Hypothermia
- **D** — Drug (digoxin, beta-blocker, non-DHP CCB, clonidine, ivabradine)
- **I** — Infarction/Ischemia (โดยเฉพาะ inferior STEMI → vagal/AV nodal)
- **E** — Electrolyte (**hyperkalemia**), + hypervagotonia, OSA, infection (Lyme, Chagas), infiltrative (amyloid, sarcoid)
- **Inherited conduction disease ที่พบบ่อยสุด = SCN5A**

# 🩺 1. Sinus Node Dysfunction (SND / Sick Sinus)

- **SA exit block:** 2nd type I (P-P สั้นลง), type II (pause = 2× P-P); 3rd = sinus arrest
- **Chronotropic incompetence:** HR ไม่ถึง 80% ของ age-predicted max ขณะออกแรง
- **Carotid sinus hypersensitivity:** sinus pause > 3 วินาที เมื่อ massage
- **Tachy-brady syndrome**; reversible: OSA (nocturnal bradycardia), athletic training

# 🩺 2. AV Block — แยก intranodal vs infranodal (สำคัญต่อการพยากรณ์)

|  | Mobitz I (intranodal) | Mobitz II (infranodal) |
| --- | --- | --- |
| PR ก่อน block | **progressive prolongation** (Wenckebach) | **fixed** แล้วตกทันที |
| QRS | narrow | มัก BBB (wide) |
| Baseline PR | ยาว (>300 ms) | สั้น (<160 ms) |
| Escape | >50 bpm (junctional) | <40 bpm (ventricular) |
| Response to atropine/exercise | ดีขึ้น | **แย่ลง** |
| Pacemaker | มัก reversible | **ต้อง pacemaker** |
- **1st degree:** PR > 200 ms
- **Complete (3rd degree):** AV dissociation, escape rhythm; cannon A wave
- **Paroxysmal AV block:** adenosine-sensitive, vagal (atrial slowing + PR prolong ก่อน block), intrinsic, bradycardia/pause-dependent (phase 4)

# 💊 Management

- **Acute symptomatic:** **atropine 0.5–1 mg IV** (ได้ผลน้อยใน infranodal); ถ้าไม่ตอบ → **transcutaneous/transvenous pacing**, +/− dopamine/isoproterenol infusion
- **Drug-induced (specific antidote):** beta-blocker OD → **IV glucagon** + high-dose insulin-euglycemia (IIa); CCB OD → **IV calcium** + high-dose insulin (IIa)
- **Permanent pacemaker** เมื่อ: symptomatic SND, acquired **Mobitz II / complete AV block** (แม้ asymptomatic), high-grade AV block ที่ไม่ reversible
- Echo ประเมิน structural cause (LBBB → Class I)

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **Mobitz II / complete AV block + wide escape = ห้ามรอ** → temporary pacing แล้ว permanent pacemaker (atropine อาจไม่ช่วยและทำให้แย่ลงใน infranodal)
> 

> - **แก้ reversible cause (T-DIE) ก่อนฝัง pacemaker ถาวร** — hyperkalemia/drug/ischemia/hypothyroid หายได้
> 

> - inferior STEMI + AV block มัก vagal/transient; anterior STEMI + AV block = สัญญาณ extensive infarct (แย่)
> 

# 🎯 High-Yield Recall

- **T-DIE reversible เสมอ**; inherited conduction disease = **SCN5A**
- **Mobitz I = intranodal (narrow, PR↑, escape >50, atropine ดีขึ้น)**; **Mobitz II = infranodal (BBB, PR fixed, escape <40, ต้อง PPM)**
- **Atropine ได้ผลใน AV nodal ไม่ใช่ infranodal**; BB OD → glucagon, CCB OD → calcium + insulin
- **Mobitz II / complete AV block → permanent pacemaker** แม้ asymptomatic

> 🇹🇭 **Thai availability:** atropine, glucagon, calcium gluconate, isoproterenol, temporary/permanent pacemaker มีในไทย
> 

> 🔍 **Verification status**
> 

> ✅ 14 ก.ย. 2026 — เกณฑ์ HR <50 bpm และช่วงปกติ 50-100 bpm ตาม 2018 ACC/AHA/HRS bradycardia guideline (ยังเป็นฉบับล่าสุด ไม่พบ update) · เกณฑ์ดั้งเดิม <60 bpm · จาก slide ในแหล่ง `2026-09/20260903-1401-line-2bebe353`
> 

> ⚠️ From source extraction (stable EP/conduction teaching), not individually re-verified: intranodal/infranodal clue thresholds, glucagon/calcium antidote class · กรอบกลไก initiation/conduction และรายการสาเหตุใน Definition & mechanism (มาจาก slide)
> 

> 🔴 หากจะ promote → cross-check pacemaker indications กับ 2021 ESC pacing guideline (เพจ Device Indications)
>
