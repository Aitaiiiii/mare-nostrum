---
title: "Temporary Pacing"
aliases: ["Temporary Pacing"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Arrhythmia & EP"
type: "Discrete entity"
review_status: "New"
tags: []
created: 2026-07-21
notion_id: 3a4224ab-ad81-81ab-92b8-eb91f934f42c
source: notion-migration
---

# Temporary Pacing

> **Digest output** — สังเคราะห์จาก SNC7 (Short Notes Cardiology) ร่วมกับ live search (28 ก.ค. 2026) เพื่อ verify การตั้งค่าที่ใช้จริง
> 

> 
> 

> **Companion pages:** [Bradycardia — Approach & AV Block](Bradycardia%20%E2%80%94%20Approach%20&%20AV%20Block%203a4224abad8181878188db03c0dd5078.md) (ข้อบ่งชี้ทางคลินิก) · [Device Indications — Pacemaker, ICD & CRT](Device%20Indications%20%E2%80%94%20Pacemaker,%20ICD%20&%20CRT%203a4224abad818144a28de9340f0c0287.md) · [Pacing Modes & ICD Therapies](Pacing%20Modes%20&%20ICD%20Therapies%20%E2%80%94%20Programming%20Basics%203a4224abad8181c1b02fcf7897d537b0.md) (troubleshooting เชิงลึก/permanent device)
> 

Temporary pacing คือ**สะพานเชื่อม (bridge)** ระหว่างภาวะ bradyarrhythmia ที่คุกคามชีวิตกับการรักษาที่ชัดเจน (permanent pacemaker หรือการแก้ reversible cause) เลือกใช้ **transvenous** เมื่อมีเวลาเตรียมและต้องการความเสถียรกว่า หรือ **transcutaneous** เมื่อต้องการเริ่มทันทีในสถานการณ์ฉุกเฉิน

# 🎯 ข้อบ่งชี้

- **Bradycardia ที่ไม่ตอบสนองต่อ atropine/drug therapy**
- **Complete (3rd degree) AV block**
- **Mobitz II** ที่ hemodynamically unstable หรือรอผ่าตัด/หัตถการ
- **Overdrive pacing** (ระงับ tachyarrhythmia บางชนิด)
- **Bridge ก่อน permanent pacemaker** หรือระหว่างรอแก้ reversible cause (ดู T-DIE ในเพจ Bradycardia)
- **Perioperative bridging** ในผู้ป่วย pacemaker-dependent ที่ต้องปิดการทำงานชั่วคราว

# 1️⃣ Transvenous Temporary Pacing

## ตำแหน่งใส่สาย

**Right internal jugular vein หรือ subclavian vein เป็นตำแหน่งที่นิยม** เหนือกว่า **femoral vein** เพราะ femoral เพิ่มความเสี่ยง **DVT/PE** และยึดสายให้มั่นคงระยะยาวได้ยากกว่าเมื่อผู้ป่วยต้องนอนติดเตียงนาน

## เทคนิคและการตั้งค่า

สอดสาย pacing catheter ปลาย balloon ผ่าน introducer sheath โดยพองบอลลูนหลังปลายสายพ้น sheath (**~10 ซม.**) แล้วปล่อยให้กระแสเลือดพาไปเข้า RV ยืนยันตำแหน่งด้วย intracardiac ECG ผ่าน **V1 lead** (การสัมผัส endocardium ทำให้เกิด injury current pattern เปลี่ยนไป) เมื่อยืนยันตำแหน่งแล้วจึงยุบบอลลูน

| การตั้งค่า | ค่าที่ใช้ | หลักการ |
| --- | --- | --- |
| **Mode** | **VVI (demand)** | pace เฉพาะเมื่อไม่มี intrinsic beat มา inhibit |
| **Rate** | **ต่ำกว่า intrinsic rate 10–20 bpm** | ให้จังหวะเองของหัวใจ inhibit การ pace เมื่อมี — ป้องกัน competitive pacing |
| **Output (capture threshold)** | ลด output ลงทีละน้อยจนกระทั่ง **capture หาย = threshold** แล้วตั้ง output จริงที่ **~2–3 เท่าของ threshold** (safety margin) | เผื่อ threshold ที่อาจเปลี่ยนแปลงจาก edema/fibrosis รอบปลายสาย |
| **Sensitivity** | เพิ่มค่า sensitivity (ตัวเลข mV ลดลง) จนกระทั่ง **QRS ของผู้ป่วยเองตรวจจับไม่ได้ = sensing threshold** แล้วตั้งค่าจริงที่ **น้อยกว่าครึ่งหนึ่งของ threshold นี้** (ช่วงปกติทั่วไป **~2–5 mV**) | ป้องกัน undersensing โดยไม่ oversensitive จน false-sense สัญญาณรบกวน |

# 2️⃣ Transcutaneous (External) Pacing

## ตำแหน่งแปะ pad

**AP position** — pad สีดำ (negative) ด้านหน้าอกบริเวณ apex (ใกล้ตำแหน่ง V3) และ pad สีแดง (positive) ด้านหลังระหว่างกระดูกสะบักซ้ายกับกระดูกสันหลัง

| การตั้งค่า | ค่าที่ใช้ |
| --- | --- |
| **Mode** | **Demand (synchronous)** |
| **Rate** | ตั้งสูงกว่า intrinsic rhythm **>30 bpm** |
| **mA เริ่มต้น** | **70 mA** แล้วเพิ่มทีละขั้นจนเห็น capture บนจอ (ช่วง capture ปกติทั่วไป **50–100 mA**) |
| **หาก capture ไม่ขึ้นที่ 120–130 mA** | **ย้ายตำแหน่ง pad ใหม่** แล้วเริ่มกระบวนการซ้ำ |
| **เมื่อ capture แล้ว** | ตั้ง mA สุดท้ายที่ **threshold + 5–10 mA** |

**การยืนยัน capture ต้องทำ 2 ระดับเสมอ**: (1) **electrical capture** — pacing spike ตามด้วย QRS กว้าง + T wave กว้าง บน monitor และ (2) **mechanical capture** — pulse คลำได้หรือ arterial line/SpO₂ waveform ตามจังหวะที่ pace เนื่องจาก skeletal muscle artifact จาก pad สามารถเลียนแบบ electrical capture ได้โดยไม่มีการบีบตัวของหัวใจจริง ผู้ป่วยที่รู้สึกตัวมักเจ็บปวดจาก skeletal muscle stimulation จึงควรพิจารณา **analgesia/sedation** ร่วมด้วย

# ⚠️ Troubleshooting & Complications

| ปัญหา | สาเหตุ | แนวทางแก้ |
| --- | --- | --- |
| **Failure to pace (output failure)** — ไม่มี spike | สาย/connection หลุด, แบตเตอรี่หมด, oversensing inhibit การ pace | ตรวจวงจรทั้งหมด → เพิ่ม output ถึงสูงสุด (**20mA atrial/25mA ventricular**) → สลับเป็น asynchronous (**AOO/VOO**) → เตรียม transcutaneous backup |
| **Failure to capture** — มี spike แต่ไม่มี QRS ตาม | เชิงกล (สายเลื่อน, fibrosis ที่ปลายสาย-endocardium interface, MI, electrolyte imbalance, หลัง defibrillation), ยา (**flecainide, sotalol, beta-blocker, lidocaine, verapamil**) | แก้ปัจจัยกระตุ้น → เพิ่ม output → สลับขั้ว bipolar หรือแปลงเป็น unipolar |
| **Oversensing** | P/T wave ขนาดใหญ่, myopotential, EMI ถูกแปลผลผิดเป็น intrinsic beat → inhibit การ pace เกินจำเป็น | ลด sensitivity (เพิ่มค่า mV) หรือสลับเป็น asynchronous |
| **Undersensing (failure to sense)** | spike ตกลงบน native beat — เสี่ยง R-on-T | เพิ่ม sensitivity (ลดค่า mV) |
| **Crosstalk** (dual chamber) | atrial spike ถูก ventricular channel sense ผิดเป็น intrinsic → inhibit V pacing | ลด sensitivity/output ของช่องที่รบกวน |
| **Lead displacement dysrhythmia** | สายลอยใน RV กระตุ้น ectopy/VT สลับกับ failure to capture | CXR ยืนยันตำแหน่ง; QRS morphology เปลี่ยนจาก LBBB→RBBB pattern บ่งชี้สายทะลุ septum ไป LV |

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> 
> 

> - **ใช้ femoral vein เมื่อหลีกเลี่ยงได้** — เพิ่มความเสี่ยง DVT/PE และยึดสายมั่นคงยากกว่าเมื่อต้อง bridge นาน
> 

> - **ยืนยัน capture ด้วย electrical เพียงอย่างเดียว** — skeletal muscle artifact เลียนแบบ spike-QRS ได้ ต้องยืนยัน mechanical capture (pulse/arterial waveform) เสมอ
> 

> - **Transcutaneous pacing โดยไม่ให้ analgesia/sedation** ในผู้ป่วยรู้สึกตัว — เจ็บปวดจน patient ขยับ/หลุด pad ได้
> 

> - **มองข้ามยาที่ทำให้ failure to capture** (flecainide, sotalol, beta-blocker, lidocaine, verapamil) — ต้องซักประวัติยาก่อนด่วนสรุปว่าเป็นปัญหาเชิงกล
> 

# 🎯 High-Yield Recall

- Site: **Rt IJV/subclavian > femoral** (DVT/PE risk)
- Transvenous **VVI**: rate ต่ำกว่า intrinsic **10–20 bpm** · output **~2–3× threshold** · sensitivity **<½ ของ sensing threshold** (ปกติ ~2–5 mV)
- Transcutaneous: **AP pads · demand mode · rate >30bpm เหนือ intrinsic · เริ่ม 70mA** → เพิ่มจนกระทั่ง capture (ปกติ 50–100mA; ย้าย pad ถ้าไม่ capture ที่ 120–130mA) → ตั้งสุดท้าย **threshold+5–10mA**
- Capture ต้องยืนยันทั้ง **electrical (spike+wide QRS) และ mechanical (pulse/arterial waveform)**
- Failure to capture ddx: เชิงกล (dislodge/fibrosis/MI/electrolyte/post-defib) หรือยา (**flecainide, sotalol, BB, lidocaine, verapamil**)

> 🇹🇭 **Thai availability**: Temporary pacing catheter, external pulse generator และ transcutaneous pacing pads (มักรวมกับเครื่อง defibrillator) เป็นอุปกรณ์มาตรฐานใน ICU/CCU/cath lab ของโรงพยาบาลรัฐและเอกชนขนาดใหญ่ทั่วไทย — ไม่ใช่ปัญหาด้านการเข้าถึง
> 
- 🔍 Verification status
    
    **✅ Searched & verified (28 ก.ค. 2026)**
    
    - Transcutaneous pacing settings (AP pad position, demand mode, rate >30bpm เหนือ intrinsic, mA เริ่ม 70, resite ถ้าไม่ capture ที่ 120–130mA, final mA = threshold+5–10) — LITFL "Transcutaneous Pacing" (Nickson, rev. 2020)
    - Troubleshooting mechanisms (failure to pace/capture, oversensing, undersensing, crosstalk, lead displacement dysrhythmia, drug-induced failure to capture) — LITFL "Temporary Pacemaker Troubleshooting" (rev. เม.ย. 2023)
    - Transvenous rate (10–20bpm below intrinsic), output (1.5–3× threshold safety margin), sensitivity (<½ threshold) principles — cross-checked LITFL/EMRA/derangedphysiology, สอดคล้องกัน
    
    **⚠️ From source (SNC7), not independently re-verified this pass**
    
    - รายละเอียดเทคนิคสอดสาย balloon-tip เฉพาะจุด (ระยะ 10cm, alligator clip + V1 monitoring pattern เฉพาะ)
    - ตัวเลข sensitivity default ต่อ chamber ที่เจาะจงมาก (1mV atrial/2.5mV ventricular) — ใช้ช่วงกว้างกว่า (~2–5mV) แทนเพื่อความปลอดภัย
    
    **🔴 Flagged uncertain**
    
    - ไม่มี
