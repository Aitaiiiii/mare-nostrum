---
title: "Basic Electrophysiology"
aliases: ["Basic Electrophysiology"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Arrhythmia & EP"
type: "Discrete entity"
review_status: "New"
tags: [cardiology, arrhythmia-ep, discrete-entity]
created: 2026-07-21
notion_id: 3a4224ab-ad81-816a-9415-ed172d684d18
source: notion-migration
---

# Basic Electrophysiology

> Foundational cellular/cardiac EP · companion: [[Tachyarrhythmia — Overview & Acute Management (Narrow & Wide-Complex, ACLS)]] · [[VT - Wide-Complex Tachycardia (Ventricular Tachycardia, WCT Differentiation & Management)|VT / Wide-Complex Tachycardia (Ventricular Tachycardia, WCT Differentiation & Management)]] · [[SVT — AVNRT - AVRT - Focal AT|SVT — AVNRT / AVRT / Focal AT]] · [[Antiarrhythmic Drugs]] — *populated 28 ก.ค. 2026 จาก digest SNC4 + verification*
> 

# 🧬 Cellular Electrophysiology & Ion Channels

หัวใจมี cell สองกลุ่มหลักที่มี electrophysiologic property ต่างกันโดยพื้นฐาน คือ **non-pacemaker (working myocardium)** และ **pacemaker cell (SA/AV node)** ซึ่งความต่างนี้อธิบายทั้ง normal conduction sequence และกลไกของ arrhythmia แทบทั้งหมด

**Non-pacemaker cell (atrial/ventricular myocyte, Purkinje fiber)** มี **resting membrane potential (RMP) ประมาณ -85 ถึง -90 mV** ที่คงที่ (stable) เนื่องจาก **IK1 (inward rectifier K⁺ current)** เปิดตลอดเวลาใน phase 4 ทำให้ maintain RMP ใกล้ K⁺ equilibrium potential Action potential ของ cell กลุ่มนี้มี 5 phases:

- **Phase 0 (rapid depolarization)** — Na⁺ influx ผ่าน fast Na⁺ channel (**INa**) ที่เปิดเมื่อ membrane potential ถึง threshold ทำให้เกิด upstroke ที่ชันมาก ส่งผลโดยตรงต่อ **conduction velocity** ของเนื้อเยื่อนั้น — ยิ่ง INa แรงเท่าไหร่ conduction ก็ยิ่งเร็ว (นี่คือเหตุผลที่ class I AAD ที่ block INa ทำให้ conduction ช้าลงและ QRS กว้างขึ้น)
- **Phase 1 (early rapid repolarization)** — K⁺ efflux ผ่าน **Ito (transient outward current)** ทำให้เกิด notch เล็กน้อย สอดคล้องกับ **J point** บน surface ECG; Ito เด่นที่ RV epicardium มากกว่า endocardium ซึ่งเป็นพื้นฐานของ transmural gradient ใน **Brugada syndrome**
- **Phase 2 (plateau)** — Ca²⁺ influx ผ่าน **L-type Ca²⁺ channel (ICaL)** สมดุลกับ K⁺ efflux ทำให้ membrane potential คงที่ชั่วขณะ สอดคล้องกับ **ST segment**; phase นี้เป็นช่วงที่ Ca²⁺ entry กระตุ้น excitation-contraction coupling
- **Phase 3 (repolarization)** — K⁺ efflux ผ่าน **IKr (rapid) และ IKs (slow) delayed rectifier** ทำให้ membrane potential กลับสู่ RMP สอดคล้องกับ **QT interval**; ยาที่ block IKr (เช่น sotalol, dofetilide, macrolide, antipsychotic) ทำให้ QT ยืดและเสี่ยง torsades
- **Phase 4 (resting)** — maintained โดย **IK1**; ใน ischemia ที่ ATP ลดลง **IKATP channel เปิด** (activated โดย ATP depletion) ทำให้ K⁺ efflux เพิ่มขึ้นและ AP duration สั้นลง ซึ่งเป็นกลไกหนึ่งของ ischemia-induced arrhythmia

**Pacemaker cell (SA node, AV node)** มีคุณสมบัติต่างจาก working myocardium อย่างสิ้นเชิง เนื่องจากไม่มี true resting potential — **maximum diastolic potential ประมาณ -50 ถึง -65 mV** (less negative กว่า non-pacemaker มาก) ทำให้ fast Na⁺ channel อยู่ในสภาวะ inactivated ตลอดเวลา ส่งผลให้ pacemaker cell ไม่มี phase 1/2 (ไม่มี plateau) และใช้ mechanism ต่างไปโดยสิ้นเชิง:

- **Phase 0** — เกิดจาก Ca²⁺ influx ผ่าน **L-type Ca²⁺ channel (ICaL)** แทนที่ Na⁺ channel (เนื่องจาก Na⁺ channel inactivated) ทำให้ upstroke ชันน้อยกว่าและ conduction velocity ช้ากว่า non-pacemaker cell มาก
- **Phase 3** — K⁺ efflux ตามปกติ
- **Phase 4 (spontaneous diastolic depolarization)** — เป็น hallmark ของ pacemaker cell เกิดจาก **funny current (If)** ที่ไหลผ่าน **HCN channel (hyperpolarization-activated cyclic nucleotide-gated channel)** ทำให้ Na⁺ ไหลเข้าช้าๆ ร่วมกับ **T-type Ca²⁺ current (ICaT)** และ IK ที่ค่อยๆ ลดลง ทำให้ membrane depolarize ขึ้นเรื่อยๆ จนถึง threshold โดยอัตโนมัติ — **ความชันของ phase 4 กำหนดอัตราการเต้นของหัวใจโดยตรง** (sympathetic stimulation เพิ่มความชัน → HR เพิ่ม; vagal stimulation ลดความชัน → HR ลด); **ivabradine block If โดยเฉพาะ** ใช้รักษา inappropriate sinus tachycardia (Class IIa)

| Feature | Non-pacemaker (atrial/ventricular myocyte) | Pacemaker (SA/AV node) |
| --- | --- | --- |
| RMP | -85 ถึง -90 mV (stable) | -50 ถึง -65 mV (unstable, MDP) |
| Phase 0 current | INa (fast, Na⁺) | ICaL (slow, Ca²⁺) |
| Phase 1/2 (plateau) | มี (Ito, ICaL) | ไม่มี |
| Phase 4 | Resting (IK1) | Spontaneous depolarization (If, ICaT) |
| Conduction velocity | เร็ว (myocardium/Purkinje) | ช้า (โดยเฉพาะ AV node) |

---

# ⚡ Conduction System & Conduction Velocity

การนำไฟฟ้าในหัวใจเดินทางผ่านเนื้อเยื่อที่มี conduction velocity ต่างกันมาก ซึ่งความต่างนี้ถูกออกแบบเพื่อให้เกิด sequential contraction ที่เหมาะสม:

- **AV node** — ช้าที่สุดในระบบ (~0.02–0.05 m/s) เนื่องจากอาศัย ICaL เป็นหลักและมี cell-to-cell coupling ต่ำ ทำให้เกิด **physiologic AV delay** ที่จำเป็นสำหรับให้ atrial contraction เสร็จสมบูรณ์ก่อน ventricular systole; นอกจากนี้ AV node ยังมีคุณสมบัติ **decremental conduction** คือยิ่ง input rate เร็วขึ้น conduction velocity ยิ่งช้าลง (ป้องกันไม่ให้ rapid atrial rate เช่น atrial flutter ผ่านลง ventricle แบบ 1:1) ซึ่งเป็นพื้นฐานของ Wenckebach phenomenon
- **Atrial/ventricular myocardium** — ปานกลาง (~0.3–1 m/s)
- **His bundle** — เร็ว (~2 m/s)
- **Purkinje fiber** — เร็วที่สุด (~2–4 m/s) เนื่องจากมี cell ขนาดใหญ่ gap junction หนาแน่น และ INa แรง ทำให้ ventricle ทั้งหมด depolarize เกือบพร้อมกัน (synchronous contraction)

**Safety factor of conduction** คือ margin ระหว่างกระแสที่ cell ต้นทางสร้างได้ (source) กับกระแสขั้นต่ำที่ cell ปลายทางต้องการเพื่อ depolarize (sink) — ในภาวะ fibrosis, ischemia หรือ Na channel blocker toxicity safety factor จะลดลง ทำให้เกิด **conduction block** หรือ **decremental/discontinuous conduction** ซึ่งเป็น substrate สำคัญของ reentry

---

# 🔁 Refractory Periods & Excitability

- **Absolute refractory period (ARP)** — ตั้งแต่ phase 0 ถึงกลาง phase 3 ที่ Na⁺ channel ส่วนใหญ่ยังอยู่ใน inactivated state ไม่ว่า stimulus จะแรงเพียงใดก็ไม่สามารถกระตุ้นให้เกิด AP ใหม่ได้
- **Relative refractory period (RRP)** — ช่วงปลาย phase 3 ที่ Na⁺ channel เริ่ม recover บางส่วน stimulus ที่แรงกว่าปกติสามารถกระตุ้น AP ใหม่ได้ แต่ AP นั้นมักมี upstroke ช้ากว่าปกติ (slow conduction) ซึ่งเป็น substrate ของ **aberrancy** (เช่น Ashman phenomenon ที่ long-short cycle ทำให้ beat ถัดมา conduct ผ่าน bundle branch ที่ยังอยู่ใน relative refractory)
- **Supernormal period** — ช่วงแคบๆ ใกล้ปลาย phase 3 ที่ threshold ต่ำกว่าปกติชั่วขณะ ทำให้ excitability สูงกว่าปกติเล็กน้อย (พบใน some AV block phenomena)
- **Effective refractory period (ERP)** — คำที่ใช้ใน EP study หมายถึง longest S1-S2 interval ที่ S2 ไม่สามารถ propagate ผ่านเนื้อเยื่อได้ (ใช้ประเมิน AV node, atrial, ventricular ERP ในการทำ EP study)

**Wavelength concept:** wavelength ของ reentry circuit = **refractory period × conduction velocity** — เนื้อเยื่อที่มี wavelength สั้น (refractory period สั้น + conduction ช้า) สามารถรองรับ reentry circuit ขนาดเล็กได้หลายวง ซึ่งอธิบายว่าทำไม atrial tissue ที่มี remodeling (AF) จึงเกิด multiple wavelet reentry ได้ง่าย ในขณะที่การให้ยาที่ยืด refractory period (class III) จะเพิ่ม wavelength และทำให้ reentry circuit ไม่สามารถ sustain ได้ (antiarrhythmic mechanism)

---

# 🌀 Mechanisms of Arrhythmia

ทุก arrhythmia เกิดจาก mechanism พื้นฐานสามกลุ่มเท่านั้น:

**1. Automaticity** — การที่ cell สร้าง spontaneous impulse ได้เอง แบ่งเป็น **normal automaticity** (SA node ปกติมี phase 4 slope ชันที่สุดจึงเป็น dominant pacemaker ผ่าน overdrive suppression ของ subsidiary pacemaker เช่น AV junction/Purkinje) และ **abnormal automaticity** (เกิดจาก partial depolarization ของ non-pacemaker cell เช่นในภาวะ ischemia/hypokalemia ทำให้ RMP ลดลงมาใกล้ threshold จน Na⁺ channel inactivate และ cell ต้องพึ่ง Ca²⁺-mediated slow response คล้าย pacemaker cell — อธิบาย accelerated idioventricular rhythm, some atrial tachycardia)

**2. Reentry** — mechanism ที่พบบ่อยที่สุดของ sustained tachyarrhythmia ต้องการองค์ประกอบครบ 4 อย่าง: (1) **two distinct pathways** ที่มี conduction velocity/refractoriness ต่างกัน, (2) **unidirectional block** ในทางหนึ่ง, (3) **slow conduction** ในอีกทางเพื่อให้เวลาที่ pathway แรก recover excitability, (4) **excitable gap** — เนื้อเยื่อที่ recover แล้วรอ re-excitation แบ่งเป็น **anatomic reentry** (fixed circuit เช่น typical atrial flutter รอบ CTI, AVNRT รอบ AV node) และ **functional reentry** (ไม่มี fixed anatomic pathway เช่น VF, some AF) — reentry อธิบาย AVNRT, AVRT, typical flutter, scar-related monomorphic VT

**3. Triggered activity** — เกิดจาก **afterdepolarization** ที่แทรกในหรือหลัง AP ปกติ แบ่งเป็นสองชนิด:

- **Early afterdepolarization (EAD)** — เกิดช่วง phase 2/3 จาก reactivation ของ ICaL ในภาวะที่ AP duration ยืดออกผิดปกติ (long QT) เมื่อ EAD มี amplitude มากพอจะกระตุ้น full AP ใหม่ได้ — เป็น substrate ของ **torsades de pointes**; ปัจจัยกระตุ้น: hypokalemia, class Ia/III AAD, bradycardia (bradycardia-dependent, R-on-T phenomenon)
- **Delayed afterdepolarization (DAD)** — เกิดช่วง phase 4 หลัง AP สมบูรณ์แล้ว จาก **intracellular Ca²⁺ overload** ที่กระตุ้น **Na⁺/Ca²⁺ exchanger (NCX)** ให้เกิด transient inward current — พบใน **digoxin toxicity** (Na⁺/K⁺ ATPase inhibition → intracellular Na⁺/Ca²⁺ สูงขึ้น), **catecholaminergic polymorphic VT (CPVT)** (RyR2/CASQ2 mutation ทำให้ SR ปล่อย Ca²⁺ผิดปกติขณะ adrenergic surge), และ idiopathic outflow tract VT/PVC (cAMP-mediated)

| Mechanism | Phase | Ion event | ตัวอย่างทางคลินิก |
| --- | --- | --- | --- |
| Reentry | - | Circuit-dependent | AVNRT, AVRT, typical flutter, scar VT |
| Abnormal automaticity | Phase 4 (partial depol.) | ↓RMP, Ca-mediated | AIVR, focal AT, ischemia-related VT |
| EAD (triggered) | Phase 2/3 | ICaL reactivation | Torsades de pointes (long QT) |
| DAD (triggered) | Phase 4 (post-AP) | Ca overload → NCX | Digoxin toxicity, CPVT, idiopathic VT |

---

# 🩻 Clinical Correlates & EP Study Applications

Concept พื้นฐานเหล่านี้เป็นรากฐานของการอ่าน EP study และเลือก antiarrhythmic drug:

- **Use-dependence** (class I AAD) — ยาจับ Na⁺ channel ใน active/inactivated state ได้ดีกว่า resting state ทำให้ออกฤทธิ์แรงขึ้นเมื่อ heart rate เร็ว (ดี — block VT ที่ rate สูง); **reverse use-dependence** (class III) — ยืด refractory period มากขึ้นเมื่อ HR ช้าลง (เสี่ยง proarrhythmia ใน bradycardia)
- **Decremental conduction ของ AV node** เป็นพื้นฐานของ adenosine/vagal maneuver ในการ terminate AVNRT/AVRT (block ที่ AV node ซึ่งเป็นส่วนหนึ่งของ circuit)
- **Entrainment mapping** ใน EP study อาศัยหลัก pacing เร็วกว่า tachycardia cycle length เล็กน้อยเพื่อ capture excitable gap ของ reentry circuit — ใช้ยืนยัน reentry mechanism และระบุ critical isthmus สำหรับ ablation

> 🚨 **STRICT AVOIDANCE / RED FLAGS (ข้อสอบ/คลินิก)**
> 

> - **อย่าสับสน pacemaker cell กับ non-pacemaker cell** — pacemaker phase 0 = Ca²⁺-mediated (ช้า), non-pacemaker phase 0 = Na⁺-mediated (เร็ว) — คำถามข้อสอบชอบสลับ
> 

> - **EAD ≠ DAD** — EAD เกิดระหว่าง repolarization (phase 2/3, สัมพันธ์กับ long QT/bradycardia), DAD เกิดหลัง repolarization สมบูรณ์ (phase 4, สัมพันธ์กับ Ca overload/digoxin/catecholamine) — กลไกและ trigger ต่างกันโดยสิ้นเชิง
> 

> - **Reentry ต้องมีครบ 4 องค์ประกอบ** (two pathway, unidirectional block, slow conduction, excitable gap) — ขาดองค์ประกอบใดไม่เกิด sustained reentry
> 

> - **Decremental conduction ของ AV node เป็น protective mechanism ปกติ ไม่ใช่พยาธิสภาพ** — อย่าตีความ PR ยาวขึ้นเมื่อ atrial rate เร็วขึ้นว่าผิดปกติเสมอไป
> 

# 🎯 High-Yield Recall

- **Non-pacemaker cell**: RMP -85~-90mV, phase 0 = INa (fast), มี plateau (phase 1-2), phase 4 = resting (IK1)
- **Pacemaker cell**: MDP -50~-65mV, phase 0 = ICaL (slow), ไม่มี plateau, phase 4 = spontaneous depolarization (If/HCN + ICaT) — ivabradine blocks If
- **Conduction velocity**: AV node ช้าที่สุด (0.02-0.05 m/s, decremental) < atrial/ventricular myocardium < His bundle < **Purkinje fiber เร็วที่สุด (2-4 m/s)**
- **3 mechanisms of arrhythmia**: automaticity (normal/abnormal), reentry (ต้องการ 2 pathway + unidirectional block + slow conduction + excitable gap), triggered activity (EAD=phase2/3/long QT/TdP; DAD=phase4/Ca overload/digoxin-CPVT)
- **Wavelength = refractory period × conduction velocity** — class III AAD ยืด wavelength เพื่อยับยั้ง reentry
- **Use-dependence (class I) vs reverse use-dependence (class III)** กำหนดความเสี่ยง proarrhythmia ที่ HR ต่างกัน

> 🇹🇭 **Thai availability:** หน้านี้เป็น conceptual physiology ไม่มียาโดยตรง; ยาที่เกี่ยวข้องกับ concept นี้ — **ivabradine (If blocker)** มีใช้ในไทยแต่ indication หลักคือ HFrEF/inappropriate sinus tach (ต้องขอผ่านผู้เชี่ยวชาญบางกรณี); class I/III AAD ดูรายละเอียดใน [[Antiarrhythmic Drugs]]
> 

> 🔍 **Verification status**
> 

> ✅ Searched & verified (28 ก.ค. 2026): resting membrane potential values, ion current assignments (INa/ICaL/Ito/IKr/IKs/IK1/If), conduction velocity ranges ทุกส่วนของ conduction system (AV node/His/Purkinje/myocardium) — cross-checked กับ CV Physiology, StatPearls, Comprehensive Physiology
> 

> ⚠️ From source, not re-verified: exact numeric RMP ranges อาจแตกต่างเล็กน้อยตาม textbook (ใช้ range ที่ widely-cited); supernormal period clinical significance เป็น classic teaching point ไม่ได้ re-verify เชิงลึก
>
