---
title: "Pacing Modes & ICD Therapies — Programming Basics"
aliases: ["Pacing Modes & ICD Therapies — Programming Basics", "Pacing Modes & ICD Therapies"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Arrhythmia & EP"
type: "Discrete entity"
review_status: "New"
tags: []
created: 2026-07-21
notion_id: 3a4224ab-ad81-81c1-b02f-cf7897d537b0
source: notion-migration
---

# Pacing Modes & ICD Therapies — Programming Basics

> **Digest output** — สังเคราะห์จาก SNC7 (Short Notes Cardiology) ร่วมกับ live search (28 ก.ค. 2026)
> 

> 
> 

> **Companion pages:** [Bradycardia — Approach & AV Block](Bradycardia%20%E2%80%94%20Approach%20&%20AV%20Block%203a4224abad8181878188db03c0dd5078.md) · [Device Indications — Pacemaker, ICD & CRT](Device%20Indications%20%E2%80%94%20Pacemaker,%20ICD%20&%20CRT%203a4224abad818144a28de9340f0c0287.md) · [Temporary Pacing](Temporary%20Pacing%203a4224abad8181ab92b8eb91f934f42c.md) · [Devices for Monitoring & Managing Heart Failure](Devices%20for%20Monitoring%20&%20Managing%20Heart%20Failure%20(I%2039e224abad818178b091e882a171896d.md) (ICD/CRT device profiles — ไม่ซ้ำเนื้อหาที่นี่)
> 

เพจนี้ครอบคลุม**การโปรแกรมและตรวจสอบ permanent pacemaker/ICD** — โค้ด, timing cycle, ค่าปกติ, การ troubleshoot, magnet response, และการจัดการรอบผ่าตัด/MRI

# 1️⃣ NBG Pacemaker Code

รหัส 5 ตำแหน่งอธิบายพฤติกรรมของเครื่อง:

| ตำแหน่ง | ความหมาย | ตัวเลือก |
| --- | --- | --- |
| **I** | Chamber ที่ **pace** | O=none, A=atrium, V=ventricle, D=dual |
| **II** | Chamber ที่ **sense** | O, A, V, D |
| **III** | **Response ต่อการ sense** | **O**=none, **T**=triggered (pace ทันทีที่ sense), **I**=inhibited (ไม่ pace เมื่อ sense), D=dual |
| **IV** | **Rate adaptive** (sensor-driven) | R หรือไม่มี |
| **V** | **Multisite pacing** | O, A, V, D |

# 2️⃣ Pacing Modes — กลไก

- **VVI** — pace/sense เฉพาะ ventricle, inhibited เมื่อ sense native QRS — เกิด **AV dissociation** เพราะไม่ synchronize กับ atrium
- **AAI** — pace/sense เฉพาะ atrium — ใช้เมื่อ AV conduction ปกติ (SND ล้วน)
- **DDD** — pace/sense ทั้งสองห้อง, response ทั้ง triggered และ inhibited — เมื่อ sense P wave จะรอ **AV interval** แล้ว pace ventricle (P-synchronous); AV interval ที่ sensed P มักสั้นกว่า paced AV ประมาณ **20–30 ms** เพราะ sensed P เกิดช้ากว่าจุดเริ่มจริงของ atrial depolarization
- **DDI** — **non-tracking**: sense P wave แต่ไม่ triggers V pacing ตาม P — ถ้า atrium pace (Ap) จะตามด้วย V pace ที่ fixed interval, ถ้า atrium sense (As) จะ V pace ที่ lower rate limit เท่านั้น (ไม่ track rate ของ atrium) — ใช้เมื่อต้องการเลี่ยง tracking atrial arrhythmia
- **DVI** — pace ทั้งสองห้องแต่ **sense เฉพาะ ventricle**, fixed VA interval
- **VDD** — เหมือน DDD แต่**ไม่มี atrial pacing** (sense atrium ได้ pace ventricle ได้เท่านั้น) — ใช้เมื่อ SA node ทำงานปกติแต่มี AV block
- **DOO/VOO/AOO** — **Asynchronous** — pace ตาม fixed rate โดยไม่สนใจ intrinsic P/QRS เลย — ใช้เฉพาะสถานการณ์ที่กลัว oversensing (magnet mode, MRI, electrocautery)

# 3️⃣ Timing Cycles

- **Blanking period** — ช่วงที่เครื่อง**ไม่รับรู้สัญญาณเลย** (ป้องกัน crosstalk/afterpotential)
- **Refractory period** — ช่วงที่เครื่อง**รับรู้สัญญาณแต่ไม่ตอบสนอง** (ไม่ retrigger timing cycle)
- **TARP (Total Atrial Refractory Period)** = sensed AV interval + **PVARP**
- **PVARP (Post-Ventricular Atrial Refractory Period)** — ป้องกัน atrial lead sense **retrograde P wave** หลัง V pace (ป้องกัน pacemaker-mediated tachycardia)
- **VRP (Ventricular Refractory Period)** — ป้องกัน V lead oversense **T wave**
- **Dynamic/rate-adaptive AV delay** — ที่ HR สูงขึ้น AV interval จะสั้นลงอัตโนมัติ เลียนแบบสรีรวิทยาปกติ

## Upper Rate Behavior (dual-chamber เท่านั้น)

| สถานการณ์ | เงื่อนไข | ผล |
| --- | --- | --- |
| **1:1 tracking ปกติ** | Atrial rate ≤ MTR (Maximum Tracking Rate) | ปกติ |
| **Wenckebach-like behavior** | TARP > Atrial rate > MTR | AV interval ค่อยๆ ยืดจนตกจังหวะ (คล้าย Wenckebach) — แก้โดยเพิ่ม MTR หรือลด PVARP (ไม่เช่นนั้นเสี่ยง 2:1 block และ PMT) |
| **2:1 block** | Atrial rate > TARP | ทุก P ที่ 2 ตกใน refractory จึงไม่ tracked — แก้โดยลด TARP (ลด PVARP/AV interval, ใช้ rate-adaptive AV) |

# 4️⃣ ค่าปกติของอุปกรณ์

| พารามิเตอร์ | ช่วงปกติ | หมายเหตุ |
| --- | --- | --- |
| **Lead impedance** | **~200–2,000 โอห์ม** (ค่าทั่วไปที่ implant มักอยู่ที่ 500–800 โอห์ม) | นอกช่วงนี้บ่งชี้ปัญหาสาย (fracture=สูงผิดปกติ, insulation break=ต่ำผิดปกติ) |
| **Capture threshold** | มักต่ำที่ implant | ตั้ง output จริงที่ **2–3 เท่าของ threshold** เป็น safety margin |
| **Sensing amplitude ที่แนะนำ** | **≥5 mV** สำหรับ pacing/sensing lead ทั่วไป | ตั้ง sensitivity จริงที่ **~1/2–1/3 ของ P/R wave amplitude** ที่วัดได้ |
| **BOL / EOL(EOS) / ERI** | Beginning of Life / End of Life(Service) / Elective Replacement Indicator | ERI มักบ่งชี้เหลืออายุแบตเตอรี่ **ประมาณ 3 เดือน** — ต้องนัดเปลี่ยนเครื่องก่อนถึง EOL |

**Far-field sensing** — เครื่องรับรู้สัญญาณไฟฟ้าจากห้องหัวใจที่ไม่ใช่ห้องที่ lead นั้นอยู่ (เช่น V lead sense สัญญาณจาก atrium) ทำให้เกิด oversensing ผิดที่

# 5️⃣ Malfunction & Troubleshooting

| ปัญหาบน ECG | กลไกที่เป็นไปได้ |
| --- | --- |
| **Rate ช้าลง** | Failure to capture · failure to pace (**สงสัย oversensing ไว้ก่อนเสมอจนกว่าจะพิสูจน์เป็นอย่างอื่น**) · functional/true undersensing · hysteresis |
| **Rate เร็วขึ้น** | Normal response ต่อ physiologic demand · atrial arrhythmia ที่ถูก track · **PMT (pacemaker-mediated tachycardia)** · sensor-induced tachycardia |
| **Rate ปกติแต่ P/QRS ไม่ตามทุก spike** | Failure to capture — threshold ปกติ (battery depletion, functional noncapture จาก pseudofusion) vs threshold เพิ่มขึ้น (lead dislodge/perforation, exit block, metabolic/drug/MI ที่ทำให้ electrode-myocardium interface เสีย) |

## Etiology vs CXR/Impedance/Threshold

| สาเหตุ | CXR | Impedance | Threshold |
| --- | --- | --- | --- |
| **Lead dislodgement** (early=unstable, late=**Twiddler's syndrome**) | ผิดปกติ/ปกติ | ปกติ/เพิ่มขึ้น | เพิ่มขึ้น |
| **Progressive fibrosis/MI/metabolic/ยา** | ปกติ | ปกติ | เพิ่มขึ้น |
| **Insulation failure** | ปกติ (บางครั้งเห็น conductor ผิดปกติ) | **ลดลง** | เพิ่มขึ้น |
| **Conductor fracture/loose screw** | ผิดปกติ | **เพิ่มขึ้น** | เพิ่มขึ้น |
| **Battery depletion** | ปกติ | ปกติ | เพิ่มขึ้น/ปกติ |

**Crosstalk** — atrial pacing spike ถูก ventricular channel sense ผิดเป็น intrinsic V activity → inhibit V pacing (V standstill) — ป้องกันด้วย bipolar lead, ลด A output, ลด V sensitivity, ยืด **PAVB (post-atrial ventricular blanking)**, เปิด **VSP (ventricular safety pacing — fixed pace ที่ ~110ms หลัง A pace เพื่อกันการถูก inhibit เกินจำเป็น)**

**Pacemaker-mediated tachycardia (PMT / endless-loop tachycardia)** — เกิดใน DDD/VDD จาก retrograde VA conduction: V pace → retrograde P → atrial lead sense ผิดเป็น native P → trigger V pace ใหม่ → วนซ้ำ — แก้ด้วยยืด **PVARP** หรือใช้ magnet mode ตัดวงจร

**Pacemaker syndrome** — เกิดจากเสีย **AV synchrony** (VVI ที่ไม่มี atrial kick, หรือ AAI ที่ PR ยืดจน atrial contraction ชนกับ closed AV valve) หรือเสีย **interventricular synchrony** (DDD ที่มี % V pacing สูงทำให้เกิด dyssynchrony แบบ LBBB) — อาการอ่อนเพลีย เวียนศีรษะ ใจสั่น ร่วมกับ **SBP ลดลง >20 mmHg** เมื่อเปลี่ยนจาก native rhythm เป็น paced rhythm

# 6️⃣ ระบุตำแหน่ง Ventricular pacing จาก ECG morphology

| ตำแหน่ง | QRS | Axis | V1 | aVL |
| --- | --- | --- | --- | --- |
| **RV pacing** | กว้าง | Left axis | Negative | Positive |
| **LV pacing** | กว้าง | Right axis | Positive | Negative |
| **LV septal pacing** | กว้าง | Left axis | Positive | Positive |
| **BiV pacing** | แคบกว่า | Northwest axis | Positive | Negative |
| **His bundle pacing** | แคบ (ใกล้ intrinsic) | ปกติ | — | — |

# 7️⃣ Perioperative CIED Management

อิงหลักการจาก **2020 ASA Practice Advisory on Perioperative Management of CIEDs** (Anesthesiology 2020;132(2):225-252) ต่อยอดจาก 2011 HRS/ASA consensus:

1. ประเมินความเสี่ยง **EMI** — คุกคามหาก source อยู่**เหนือสะดือ**และ**ใกล้กว่า 15 ซม.**จากตัวเครื่อง (เช่น monopolar electrocautery)
2. ประเมิน **pacing dependency**
3. **Pacemaker**: ถ้า dependent + เสี่ยง EMI → reprogram เป็น **asynchronous mode** หรือใช้ magnet; ถ้าไม่ dependent → เตรียม magnet ไว้ให้พร้อมโดยไม่ต้อง reprogram ล่วงหน้า
4. **ICD**: **ปิด tachyarrhythmia detection/therapy** เสมอเมื่อมีความเสี่ยง EMI (ป้องกัน inappropriate shock จาก EMI) — ถ้า pacing-dependent ต้อง reprogram เป็น asynchronous ร่วมด้วย — ต้องมี **external defibrillator/pacing พร้อมใช้ตลอดการผ่าตัด**
5. หลังผ่าตัด: **interrogate device และคืนค่าโปรแกรมเดิม** เสมอ
6. **อุปกรณ์ CRT ควรปรึกษา CIED team เฉพาะทาง** เนื่องจากการปิด biventricular pacing แม้ชั่วคราวอาจทำให้ HF แย่ลง

**การตรวจสอบเครื่อง (PLSTO mnemonic)**: **P**atient data · **L**ead impedance · **S**ensing (ลด backup pacing rate ลงจนเห็น intrinsic rhythm) · **T**hreshold (เพิ่ม output เหนือ intrinsic แล้วค่อยลดจนเสีย capture) · **O**bservation (บันทึกเหตุการณ์)

**หลัง external defibrillation**: ต้อง **ตรวจสอบ pacemaker ซ้ำเสมอ** เพราะ cardioversion/defibrillation อาจทำให้เกิด **power-on-reset** กลับไปที่ค่า default (มักเป็น VVI) — วาง pad แบบ AP และให้ห่างจากตัวเครื่อง **>8–10 ซม.**

# 8️⃣ Magnet Response

**หลักการทั่วไป (ยืนยันแล้ว)**: Pacemaker เมื่อวาง magnet จะเปลี่ยนเป็น **asynchronous mode** (DDD→DOO, VVI→VOO, AAI→AOO) ที่ rate คงที่เฉพาะรุ่น/ยี่ห้อ พร้อมระงับ rate response ชั่วคราว — ICD เมื่อวาง magnet จะ**ระงับการตรวจจับ/รักษา tachyarrhythmia** (shock/ATP) แต่**การ pace ยังทำงานต่อ** — Boston Scientific และ Abbott/St. Jude อนุญาตให้ปรับแต่งพฤติกรรมนี้ได้ (reprogrammable), ส่วน Medtronic ตอบสนองช้ากว่าเล็กน้อย (~1.5 นาทีหลัง interrogation ตามการศึกษาเปรียบเทียบข้ามยี่ห้อ)

⚠️ **ตัวเลข magnet rate เฉพาะยี่ห้อ/รุ่นเปลี่ยนแปลงได้ตามรุ่นและ battery status — ต้องยืนยันกับบัตรประจำเครื่อง (device ID card) หรือระบบ interrogation จริงเสมอ ห้ามอ้างอิงจากความจำเพียงอย่างเดียว** ตัวเลขจาก source draft (Medtronic DOO/VOO ~85bpm ERI ~65bpm; Boston DOO/VOO ~100bpm ERI ~85bpm; St. Jude DOO/VOO ~98–100bpm ERI <85bpm) **ยังไม่ได้ยืนยันอิสระในรอบนี้** — ใช้เป็นแนวทางคร่าวๆ เท่านั้น

# 9️⃣ MRI & CIED

อิงหลักการจาก **2017 HRS Expert Consensus Statement on MRI and Radiation Exposure in Patients with CIEDs**:

- อุปกรณ์ **MRI-conditional** ต้องโปรแกรมเข้าสู่ **"MRI mode"** ก่อนสแกน: pacing-dependent patient → **asynchronous mode (DOO/VOO)**; non-dependent → พิจารณา asynchronous หรือ inhibited mode ก็ได้; **ปิด tachyarrhythmia detection/therapy ของ ICD เสมอ**
- หลังสแกน: **interrogate ซ้ำและคืนค่าโปรแกรมเดิมเสมอ**
- ความเสี่ยงหลัก: **RF-induced lead-tip heating**, EMI ทำให้ oversensing/inhibition, asynchronous pacing ที่อาจกระตุ้น AT/VT หากตกใน vulnerable period
- ต้องตรวจสอบ **MRI-compatibility ของทั้งเครื่องและสายที่ฝัง** (บางกรณี lead compatible แต่ generator ไม่ หรือมี abandoned lead ซึ่งเป็นข้อห้ามสัมพัทธ์) ก่อนทุกครั้ง — ควรทำในศูนย์ที่มีทีม cardiology และ continuous monitoring พร้อม

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> 
> 

> - **สงสัย oversensing ไว้ก่อนเสมอ** เมื่อพบ "failure to pace" ที่ rate ช้าลงกะทันหัน — อย่ารีบสรุปว่าแบตเตอรี่หมด
> 

> - **ไม่ interrogate/restore ค่าเดิมหลังผ่าตัดหรือหลัง external defibrillation** — เสี่ยง device ค้างอยู่ใน asynchronous mode หรือ power-on-reset กลับเป็น VVI โดยไม่รู้ตัว
> 

> - **อ้างอิง magnet rate เฉพาะยี่ห้อจากความจำ** — ต้องเช็คกับบัตรเครื่องหรือ interrogation จริงเสมอ เพราะเปลี่ยนตามรุ่น/battery status
> 

> - **MRI โดยไม่ตรวจสอบ compatibility ของทั้งเครื่องและสาย** หรือไม่มีทีม cardiology monitoring พร้อม
> 

# 🎯 High-Yield Recall

- **NBG code**: Pace/Sense/Response(O,T,I)/Rate-adaptive/Multisite
- **DDI = non-tracking** · **DDD = P-synchronous** · **VDD = DDD ไม่มี atrial pacing** · **DOO/VOO/AOO = asynchronous**
- **TARP = sensed AV + PVARP**; Wenckebach-like เมื่อ **TARP>Arate>MTR**; 2:1 block เมื่อ **Arate>TARP**
- Lead impedance ปกติ **~200–2,000 โอห์ม**; output ตั้งที่ **2–3× threshold**; sensing ที่แนะนำ **≥5mV**
- **Crosstalk → V standstill** (แก้ด้วย bipolar/ลด A output/ยืด PAVB/เปิด VSP); **PMT** แก้ด้วยยืด PVARP
- **Pacemaker syndrome** = เสีย AV/interventricular synchrony → SBP ลด >20mmHg เมื่อเปลี่ยนเป็น paced rhythm
- Perioperative: **EMI เสี่ยงถ้า source เหนือสะดือ+<15ซม.**; pacemaker-dependent+ICD → **ปิด tachytherapy เสมอ + เตรียม external defib**
- MRI: pacing-dependent → **DOO/VOO** + ปิด tachytherapy ICD เสมอ, interrogate ก่อน-หลังทุกครั้ง

> 🇹🇭 **Thai availability**: Permanent pacemaker/ICD/CRT ทุกยี่ห้อหลัก (Medtronic, Boston Scientific, Abbott/St. Jude, Biotronik) มีจำหน่ายและฝังได้ในโรงพยาบาลตติยภูมิทั่วไทย; MRI-conditional device เพิ่มมากขึ้นแต่ยังไม่ใช่ทุกรุ่น — ต้องตรวจสอบ compatibility เฉพาะเครื่องก่อนส่งสแกนเสมอ
> 
- 🔍 Verification status
    
    **✅ Searched & verified (28 ก.ค. 2026)**
    
    - Lead impedance normal range (~200–2,000 โอห์ม, typical 300–1,200/500–800 ที่ implant), capture threshold safety margin (2–3×), sensing amplitude แนะนำ (≥5mV, ตั้งที่ ~1/2–1/3 ของ amplitude ที่วัดได้) — [droracle.ai](http://droracle.ai) cross-referenced กับ standard EP teaching
    - Perioperative CIED algorithm หลักการ (EMI risk เหนือสะดือ/<15cm, pacing dependency check, ICD tachytherapy suspension, restore หลังผ่าตัด) — 2020 ASA Practice Advisory (Anesthesiology 2020;132(2):225-252), ต่อยอด 2011 HRS/ASA consensus
    - MRI-conditional programming หลักการ (asynchronous mode สำหรับ pacing-dependent, ปิด tachytherapy, restore หลังสแกน, RF heating risk) — 2017 HRS Expert Consensus Statement on MRI and CIEDs
    - Magnet response หลักการทั่วไป (pacemaker→asynchronous, ICD→suspend tachytherapy only, Boston/Abbott reprogrammable, Medtronic delayed response) — cross-referenced multiple sources (Boston Scientific clinical documents, comparative magnet-response studies)
    
    **⚠️ From source (SNC7), not re-verified independently this pass**
    
    - Timing cycle numeric details (DDD sensed-vs-paced AV interval 20–30ms, VSP fixed ~110ms) — standard EP teaching, ไม่ใช่ guideline-graded number
    - ECG morphology table สำหรับระบุตำแหน่ง pacing site — standard EP teaching
    - PLSTO mnemonic และ external defib pad distance (>8–10cm) — practice-based, ไม่พบ primary guideline citation เฉพาะเจาะจงในรอบค้นนี้
    
    **🔴 Flagged uncertain**
    
    - ตัวเลข magnet rate เฉพาะยี่ห้อ/รุ่น (Medtronic 85/65bpm, Boston 100/85bpm, St. Jude 98-100bpm) จาก source draft — **ไม่ได้ยืนยันอิสระ** ต้องเช็คกับบัตรเครื่องจริงก่อนใช้ทางคลินิกเสมอ
