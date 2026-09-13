---
title: "Arrhythmia Order Set"
type: "Standing Order"
specialty: "Cardiology"
ward: ["Medicine"]
tags: [workflow]
notion_id: 38a224ab-ad81-81e4-b3dc-e6106c676ff8
source: notion-migration
---

# Arrhythmia Order Set

> ⚠️ **SAFETY** | Reference สำหรับการศึกษาและ clinical reasoning เท่านั้น ปรับตาม local ACLS protocol, cardiac monitoring capability, และ attending physician ทุกครั้ง — cardioversion/defibrillation ต้องมี qualified personnel + resuscitation equipment พร้อม
> 

---

> [!question]- What to review
>
> - **Hemodynamic stability FIRST**: SBP <90, AMS, ischemic chest pain, acute pulmonary edema → **unstable** → cardioversion/defibrillation ทันที ไม่รอยา
> - **ECG 12-lead STAT**: QRS width (<0.12s = narrow / ≥0.12s = wide), regularity, PR interval, QTc, delta wave, AV dissociation, fusion/capture beats
> - **Vital signs**: HR, BP, SpO2, RR, GCS; continuous cardiac monitoring
> - **ประวัติ**: onset, duration, palpitation, presyncope/syncope, chest pain; ยา (digoxin, antiarrhythmic, QT-prolonging drugs, beta-blocker, CCB)
> - **❌ ห้ามใช้ AV nodal blockers** (adenosine, beta-blocker, CCB, digoxin) ถ้าสงสัย WPW + AF irregular wide complex
> - **Lab STAT**: K, Mg, Ca, glucose, Cr, TFT, troponin; reversible causes (5H5T)
> - **Defibrillator on standby เสมอ**
>
> ---
>

# 🔴 UNSTABLE — ทุก Tachyarrhythmia

*(SBP <90, shock, AMS, acute pulmonary edema, ischemic chest pain)*

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG 12-lead STAT; continuous monitoring; IV access × 2
> - [ ] Electrolytes, Cr, glucose, troponin STAT; ABG; SpO2
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] O2 maintain SpO2 ≥94%
> - [ ] **Sedation** (ถ้า conscious): Midazolam 1–2 mg IV + Fentanyl 1–2 mcg/kg IV; หรือ Ketamine 0.5–1 mg/kg IV ถ้า hypotensive
> - [ ] **Synchronized DCCV**: narrow regular (SVT/AFl) 50–100 J → narrow irregular (AF) 120–200 J → wide regular (VT) 100–200 J; escalate ทุก attempt
> - [ ] **Unsynchronized defibrillation** (VF/pVT/wide irregular polymorphic): **200 J biphasic** (360 J monophasic); เริ่ม ACLS ทันที
> - [ ] ❌ ห้าม adenosine/verapamil/diltiazem ใน wide irregular หรือสงสัย WPW+AF
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] ECG ซ้ำหลัง cardioversion ทันที; troponin serial q3–6h
> - [ ] K, Mg q4–6h; repeat 12-lead ECG
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] แก้ underlying (hypoK, hypoMg, ischemia) ทันที
> - [ ] Antiarrhythmic maintenance ตาม rhythm ที่ restore (ดูแต่ละ section ด้านล่าง)
> - [ ] ปรึกษา cardiology/electrophysiology
>
> ---
>

# Ⅰ. NARROW COMPLEX TACHYCARDIA (QRS <0.12s)

---

## 🔵 SVT — Narrow Regular (AVNRT / AVRT)

*(HR 150–250; regular; narrow QRS; P wave retrograde/ซ่อน)*

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG 12-lead; auscultate carotid bilateral (bruit → ห้าม carotid massage); electrolytes STAT
> - [ ] IV access proximal (antecubital/central — adenosine ต้องใกล้หัวใจ); defibrillator standby
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Step 1 — Vagal maneuvers**: Modified Valsalva (เป่าลม syringe 10 mL × 15 sec → นอนราบ ยกขา 45° × 15 sec); Carotid sinus massage ถ้าไม่มี bruit
> - [ ] **Step 2 — Adenosine**: 6 mg IV rapid push (1–3 sec) + NSS 20 mL flush rapid; ถ้าไม่ convert → 12 mg × 1–2 doses; onset 10–20 sec; แจ้งผู้ป่วย: flushing, chest tightness, brief asystole — ❌ ห้าม WPW+AF, 2nd/3rd AV block
> - [ ] **Step 3 — AV nodal blocker** (ถ้า adenosine ไม่ได้ผล/recur): EF ปกติ: Verapamil 5 mg IV over 2 min → repeat 5–10 mg ทุก 15–30 min (max 20 mg); หรือ Diltiazem 0.25 mg/kg IV over 2 min → repeat 0.35 mg/kg — EF ลด/HFrEF: Amiodarone 150 mg IV over 10 min
> - [ ] **Step 4 — Cardioversion** ถ้าไม่ convert: Synchronized 50–100 J (sedation ก่อน)
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] ECG ซ้ำหลัง SR restore; Holter outpatient; electrolytes q6–8h
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] Rate control maintenance: Diltiazem ER 120–360 mg PO OD หรือ Metoprolol succinate 25–100 mg PO OD
> - [ ] ถ้า recurrent/symptomatic SVT (structurally normal): Refer electrophysiology สำหรับ catheter ablation (first-line preferred; AHA 2023)
> - [ ] แก้ underlying: thyrotoxicosis, caffeine, electrolyte imbalance
>
> ---
>

## 🔵 Atrial Fibrillation / Atrial Flutter with RVR

*(AF: irregular irregular; AFl: regular ~150 bpm sawtooth P wave)*

**Key decision**: Duration ≥24h หรือ unknown → ห้าม cardiovert โดยไม่มี OAC ≥3 สัปดาห์ หรือ TEE-guided (ESC 2024: threshold ลดจาก 48h → 24h)

**CHA₂DS₂-VA score** (ESC 2024; ตัด sex): ≥2 → OAC indicated

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG + rhythm strip (AF vs AFl vs MAT); Electrolytes, Cr, TFT, CBC, coag, troponin STAT
> - [ ] Bedside echo ถ้า unstable; formal echo ใน 24–48h (LV function, valvular disease)
> - [ ] CHA₂DS₂-VA score; HAS-BLED score
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Anticoagulation** (AF ≥24h หรือ unknown): UFH bolus 60–80 units/kg IV → infusion 12–18 units/kg/h (target PTT 60–100); หรือ Enoxaparin 1 mg/kg SC q12h (CrCl ≥30)
> - [ ] **Rate control** (stable; target HR <110 acutely): EF ปกติ: Metoprolol 2.5–5 mg IV q5 min × 3 (max 15 mg); หรือ Diltiazem 0.25 mg/kg IV over 2 min → 0.35 mg/kg → drip 5–15 mg/h — HFrEF/EF ลด: Digoxin 0.25–0.5 mg IV → 0.125 mg q6h × 3; หรือ Amiodarone 150 mg IV over 10 min → drip 1 mg/min × 6h → 0.5 mg/min × 18h — ❌ ห้าม diltiazem/beta-blocker ใน HFrEF decompensated; ❌ ห้าม verapamil/diltiazem ใน WPW
> - [ ] **Rhythm control** (duration <24h + stable; ถ้า TEE-guided หรือ anticoagulated): DCCV 120–200 J biphasic — No SHD: Flecainide 2 mg/kg IV over 10 min หรือ Propafenone 2 mg/kg IV — SHD/HFrEF: Amiodarone 150 mg IV → drip
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] Rhythm strip q2–4h; ECG ซ้ำหลัง cardioversion; electrolytes q6–8h; INR/anti-Xa
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Long-term OAC**: CHA₂DS₂-VA ≥2 → Apixaban 5 mg PO BID หรือ Rivaroxaban 20 mg PO OD with meal (DOAC preferred; AHA 2023, ESC 2024); Warfarin ถ้า mechanical valve/rheumatic MS
> - [ ] **Long-term rate control**: Bisoprolol 2.5–10 mg PO OD หรือ Diltiazem ER 120–360 mg OD
> - [ ] **Long-term rhythm control**: Amiodarone 200 mg PO OD (SHD); Flecainide/Propafenone (no SHD); Dronedarone 400 mg PO BID (paroxysmal; ❌ ห้ามใน HFrEF)
> - [ ] Ablation: ESC 2024 first-line ใน paroxysmal AF suitable patients → ปรึกษา electrophysiology
> - [ ] AF-CARE comorbidity management: HTN, OSA, obesity, alcohol, thyrotoxicosis (ESC 2024)
>
> ---
>

# Ⅱ. WIDE COMPLEX TACHYCARDIA (QRS ≥0.12s)

---

## 🔴 Stable VT — Monomorphic Wide Regular

**กฎ**: Treat as VT until proven otherwise — AV dissociation/fusion beats/capture beats = pathognomonic

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG 12-lead (Brugada/Vereckei criteria); Electrolytes, troponin, Cr STAT
> - [ ] Echo (LV function — เลือกยาตาม EF); continuous monitoring; defibrillator standby
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Procainamide 10 mg/kg IV over 20 min** (max 17 mg/kg; rate ≤50 mg/min) — preferred first-line (AHA Class IIa; PROCAMIO 2017); หยุดถ้า hypotension, QRS widening >50%, QTc >500 ms — ❌ ห้ามถ้า QTc ↑ baseline, torsades, SLE
> - [ ] **Amiodarone 150 mg IV over 10 min** → infusion 1 mg/min × 6h → 0.5 mg/min × 18h (max 2.2 g/24h) — alternative ถ้า LV dysfunction/procainamide ไม่มี (AHA Class IIb)
> - [ ] **Sotalol 100 mg IV over 5 min** — alternative; ❌ ห้ามถ้า QTc ↑ หรือ hypoK
> - [ ] ❌ ห้าม verapamil/diltiazem (hemodynamic collapse); ❌ ห้าม lidocaine (inferior)
> - [ ] ถ้าไม่ตอบสนอง/deteriorate: Synchronized DCCV 100–200 J (sedation ก่อน)
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] ECG ซ้ำ; Serial troponin; Echo formal; Electrolytes q6h
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] แก้ underlying: ischemia → cath lab, electrolyte, drug toxicity
> - [ ] Maintenance: Amiodarone 200 mg PO OD (SHD); Sotalol ถ้า QTc ปกติ
> - [ ] Beta-blocker ใน post-MI VT: Metoprolol succinate 25–200 mg PO OD
> - [ ] ปรึกษา electrophysiology: VT ablation หรือ ICD (ESC 2022 Class IIa ถ้า recurrent/SHD)
>
> ---
>

## 🔴 Torsades de Pointes (Polymorphic VT + Prolonged QTc)

*(QRS amplitude alternates/twisting; triggered by long-short coupling; QTc >500 ms)*

**❌ ห้าม amiodarone / procainamide / sotalol / quinidine ทั้งหมด — ยืด QTc ให้แย่ลง**

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG + QTc serial (Bazett); K, Mg, Ca STAT; drug levels (amiodarone, sotalol, haloperidol, quinolone, methadone); TFT
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Pulseless/VF**: Unsynchronized defibrillation 200 J ก่อน
> - [ ] **MgSO4 2 g IV over 1–2 min** → infusion 1–2 g/h × 4–6h (ไม่รอ Mg level)
> - [ ] **แก้ hypoK ทันที**: target K ≥4.5 mEq/L (KCl IV per hypoK protocol)
> - [ ] **หยุด QT-prolonging drugs ทันที**: class Ia/III AAD, antipsychotics, macrolides, fluoroquinolones, methadone
> - [ ] **เพิ่ม HR เพื่อ shorten QTc** (TdP เกิดที่ HR ต่ำ): Isoproterenol 2–10 mcg/min IV (titrate HR 80–100; acquired TdP; ❌ ห้ามใน congenital LQTS) — หรือ Transcutaneous/Transvenous pacing 80–100 bpm (overdrive pacing; เลือกถ้า bradycardia-dependent TdP)
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] K, Mg q4–6h; QTc monitoring q4h
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] หยุด QT-prolonging drugs ตลอด admission
> - [ ] Congenital LQTS (LQT1/2/3): Beta-blocker (nadolol), ICD → ปรึกษา electrophysiology
>
> ---
>

## 🔴 AF with WPW — Wide Irregular Tachycardia (Pre-excited AF)

*(Irregular, wide/bizarre QRS, HR อาจสูง 200–300 → ชีวิตอันตราย)*

**❌ ห้าม adenosine / beta-blocker / CCB / digoxin / amiodarone IV — block AV node → force conduction ผ่าน AP → HR สูงมาก → VF**

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG 12-lead STAT; defibrillator standby ตลอด; continuous monitoring; electrolytes STAT
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Unstable**: Unsynchronized defibrillation 200 J (VF/pulseless); Synchronized DCCV ถ้า pulse + unstable
> - [ ] **Stable**: Procainamide 10 mg/kg IV over 20 min (slows accessory pathway; preferred) — หรือ Ibutilide 1 mg IV over 10 min
> - [ ] ถ้าไม่ตอบสนอง: Synchronized DCCV
>

## Order for Continue

> [!example]+ 💊 Medication
>
> - [ ] ปรึกษา electrophysiology สำหรับ accessory pathway catheter ablation (curative; urgent)
>
> ---
>

# Ⅲ. BRADYARRHYTHMIAS

---

## 🔵 Symptomatic Bradycardia / AV Block

**Symptoms**: syncope/presyncope, dyspnea, chest pain, hypotension, AMS → ต้องรักษา

**AV block**: 1st (PR >200) → benign; 2nd Mobitz I (Wenckebach) → usually benign; **2nd Mobitz II + 3rd degree (CHB)** → unstable → pacing ทันที

## Order for One Day

> [!example]+ 🔬 Investigation
>
> - [ ] ECG 12-lead STAT (identify: sinus brady vs AV block type vs junctional escape)
> - [ ] Electrolytes (K, Ca, Mg), drug levels (digoxin, beta-blocker, CCB), TFT, troponin STAT
> - [ ] Continuous cardiac monitoring; SpO2; IV access × 2; portable CXR
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] **Atropine 0.5 mg IV** q3–5 min; max total **3 mg** (AHA ACLS; Class IIa) — onset immediate; SA node/AV node — ❌ ineffective ใน Mobitz II/CHB (block below His-Purkinje) — ❌ ห้ามใน heart transplant (paradoxical response)
> - [ ] **Mobitz II / CHB**: ข้าม atropine → Transcutaneous Pacing ทันที
> - [ ] **Bridge pharmacologic** (ระหว่าง pacing): Dopamine 2–10 mcg/kg/min IV drip — หรือ Epinephrine 2–10 mcg/min IV drip (profound brady + hypotension) — Isoproterenol 2–10 mcg/min IV (pure β; CHB ก่อนปัก TVP; ระวัง ischemia)
> - [ ] **Transcutaneous Pacing (TCP)**: Rate 60–80 bpm; เพิ่ม mA จน electrical + mechanical capture; Sedation ก่อน (Midazolam 1–2 mg IV + Fentanyl 1–2 mcg/kg IV — TCP เจ็บปวดมาก)
>

## Order for Continue

> [!example]+ 🔬 Investigation
>
> - [ ] Continuous monitoring; Serial ECG; Electrolytes q6–8h
> - [ ] Digoxin level; Echo ถ้ายังไม่ได้ทำ
>
> ---
>

> [!example]+ 💊 Medication
>
> - [ ] หยุดยาที่ทำให้ bradycardia: beta-blocker, CCB, digoxin, amiodarone
> - [ ] แก้ underlying: ACS (cath lab), hyperK, hypothyroidism, hypothermia, Lyme disease
> - [ ] **Transvenous Pacing (TVP)**: bridge จาก TCP; ปรึกษา cardiology ถ้า persistent high-degree AV block
> - [ ] **Permanent Pacemaker (PPM)**: ปรึกษา electrophysiology — indication: Mobitz II, CHB, symptomatic SSS
>
> ---
>

# ⚡ Cardioversion / Defibrillation Energy Summary

| Rhythm | Mode | Energy (Biphasic) |
| --- | --- | --- |
| SVT (narrow regular) | Synchronized | 50–100 J |
| AF (narrow irregular) | Synchronized | 120–200 J |
| Atrial flutter | Synchronized | 50–100 J |
| VT monomorphic (wide regular) | Synchronized | 100–200 J |
| VF / pVT / wide irregular polymorphic | **Unsynchronized** | **200 J** (360 J monophasic) |

> ⚠️ Reference only — ปรับตาม local protocol, ACLS certification, และ attending physician ทุกครั้ง
>
