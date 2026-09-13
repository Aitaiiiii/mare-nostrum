---
title: "Echocardiography Signs, Formulas & Eponyms (Doppler Quantification, Named Signs & Parameters)"
aliases: ["Echocardiography Signs, Formulas & Eponyms (Doppler Quantification, Named Signs & Parameters)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "ECG & Cardiac Imaging"
type: "Workflow"
guidelines: ["ACC/AHA", "ESC"]
review_status: "New"
tags: [workflow]
created: 2026-07-21
notion_id: 3a4224ab-ad81-816c-a76d-f871f0d93b6e
source: notion-migration
---

# Echocardiography Signs, Formulas & Eponyms (Doppler Quantification, Named Signs & Parameters)

> หน้านี้เป็นเพจที่ 4 ของ eponym/reference series — คู่กับ [ECG & Electrophysiology Eponyms (Medical Eponym Reference — Anatomy, Signs, Scores, Criteria, Syndromes)](ECG%20&%20Electrophysiology%20Eponyms%20(Medical%20Eponym%20Re%203a4224abad8181f1ba1ec23df0d2a1c8.md), [Cardiovascular Physical Examination Eponyms (Signs, Murmurs, Pulses & Grading Scales)](Cardiovascular%20Physical%20Examination%20Eponyms%20(Signs%203a4224abad8181b2b576c4ecae388473.md) และ [Cardiac Surgery & Intervention Procedures (CVT / Cardiac Surgery / Structural — Eponymous & Common Names)](Cardiac%20Surgery%20&%20Intervention%20Procedures%20(CVT%20Car%203a4224abad8181fbb42ddbc52c12554b.md) — รวบรวม **ชื่อ formula, sign, pattern และ parameter ทาง echocardiography** ทั้ง eponym และชื่อ common จัดหมวด: Formulas/Doppler → Named signs → M-mode signs → Chamber/function parameters → Named anatomy → Modalities/artifacts
> 

> ⚙️ routing: quantification ของโรคเฉพาะอยู่ที่เพจโรคนั้นๆ — PHT/continuity ของ MS → [MS (Mitral Stenosis) — Rheumatic Pathophysiology, Auscultation & PMBC Decision](MS%20(Mitral%20Stenosis)%20%E2%80%94%20Rheumatic%20Pathophysiology,%20%203a0224abad8181f2a1cdcfe5edaa93c1.md) · respiratory Doppler variation → [Cardiac Tamponade](Cardiac%20Tamponade%2038a224abad8181c88c29ef4c4d355967.md) · diastolic function (E/e′, LAVi) → [HFpEF (Heart Failure with Preserved Ejection Fraction)](HFpEF%20(Heart%20Failure%20with%20Preserved%20Ejection%20Fract%20387224abad8181e4b79ce5d452a2c835.md) · valve severity → [Valvular Heart Disease (Murmur Approach, Severity & Timing of Intervention)](Valvular%20Heart%20Disease%20(Murmur%20Approach,%20Severity%20%2038e224abad818191b576c7d3825a91e1.md)
> 

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **ทุก formula มีเงื่อนไข validity** — อย่าใช้ค่าที่ได้โดยไม่ดูเงื่อนไข: **PHT (220/PHT)** ใช้ไม่ได้ใน significant AR/หลัง valvuloplasty ทันที; **simplified Bernoulli (4V²)** ต้องเติม V1 เมื่อ V1>1.5 หรือ V2>3 m/s; **continuity** ใช้ไม่ได้เมื่อมี significant AR
> 

> - **eponym signs ของ emergency**: **McConnell (acute PE)**, **D-shape (RV pressure/volume overload)** — อย่ามองข้าม; เป็นเบาะแสดงภาวะ RV ที่คุกคาม
> 

> - normal cutoff เช่น TAPSE, E/e′ **ขึ้นกับ guideline ปี** — 2025 ASE เปลี่ยนบางตัวเป็น graded range; เช็กฉบับล่าสุดก่อนอ้าง
> 

---

# 🧮 1. Core Formulas & Doppler Quantification

> ⚠️ **FORMULAS ARE NUMBERS** — ทุกสมการ verify ค่าคงที่/เงื่อนไขแล้ว (search 21 ก.ค. 2026); หน่วยต้องตรงตาม (velocity m/s, area cm²)
> 

| Formula | สมการ | เงื่อนไข/ข้อจำกัด |
| --- | --- | --- |
| **Simplified (modified) Bernoulli** | **ΔP = 4V²** (ΔP mmHg, V peak velocity m/s) | ละเลย V1 ได้เมื่อ V1<1 m/s; **ถ้า V1>1.5 หรือ V2>3 m/s ต้องใช้ ΔP = 4(V2²−V1²)**; ไม่คิด pressure recovery |
| **Continuity equation (AVA)** | **AVA = (CSA_LVOT × VTI_LVOT) / VTI_AV** โดย CSA_LVOT = π×(D/2)² | conservation of mass; **ใช้ไม่ได้เมื่อมี significant AR/subvalvular obstruction**; error หลักมาจากการวัด LVOT diameter (เข้ากำลังสองเพราะ D ถูกยกกำลังสอง) |
| **PISA (EROA)** | **EROA = 2πr² × V_aliasing / V_peak** ; **RegVol = EROA × VTI_regurgitant** | เลื่อน Nyquist ไปทาง jet เพื่อวัด r; สมมติ hemispheric shell — error ถ้า orifice ไม่กลม/eccentric jet |
| **Pressure half-time (MVA, Hatle)** | **MVA = 220 / PHT** (220 = empirical constant ของ Hatle 1979) | PHT = เวลาจาก Vmax → Vmax/1.4; **overestimate severity ใน diastolic dysfunction, underestimate เมื่อมี AR**; ไม่ reliable ทันทีหลัง PMBC → [MS (Mitral Stenosis) — Rheumatic Pathophysiology, Auscultation & PMBC Decision](MS%20(Mitral%20Stenosis)%20%E2%80%94%20Rheumatic%20Pathophysiology,%20%203a0224abad8181f2a1cdcfe5edaa93c1.md) |
| **RVSP / PASP** | **RVSP = 4×(TR Vmax)² + RA pressure** (≈ PASP ถ้าไม่มี RVOT obstruction) | RA pressure ประเมินจาก IVC size/collapsibility |
| **Stroke volume (Doppler)** | **SV = CSA_LVOT × VTI_LVOT** ; CO = SV × HR | พื้นฐานของ continuity |
| **Gorlin formula (cath, gold standard)** | AVA = CO / (SEP × HR × 44.3 × √mean gradient) | invasive; **Hakki simplification: AVA ≈ CO / √gradient** (จากค่า HR×SEP×44.3 ≈ 1000) |
| **Teichholz (LV volume)** | คำนวณ LV volume จาก M-mode linear dimension | ⚠️ **ไม่แม่นเมื่อมี regional wall motion abnormality** — ASE แนะนำ Simpson แทน |
| **Simpson biplane (MOD)** | EF จาก disk summation ของ 4CH+2CH | method of choice สำหรับ EF เมื่อมี RWMA |

---

# 🩻 2. Named 2D / Doppler Signs & Patterns

- **SAM (Systolic Anterior Motion)** — anterior mitral leaflet ถูกดูดเข้าหา septum ในช่วง systole ทำให้เกิด **dynamic LVOT obstruction + posteriorly-directed MR** ใน **HOCM** กลไกคือ **Venturi/drag effect** จาก high-velocity flow ผ่าน LVOT ที่แคบ — common name; เป็นภาพจำของ HOCM
- **McConnell's sign** — ใน **acute PE / acute RV pressure overload**: **RV free wall akinesia แต่ apex ยัง contract ปกติ (apical sparing ของ RV)** — ค่อนข้าง specific ต่อ acute RV strain (แยกจาก chronic PH) ตั้งชื่อตาม Michael **McConnell**
- **D-sign / D-shaped septum** — ใน parasternal short axis, interventricular septum แบนทำให้ LV เป็นรูปตัว D: **systolic flattening = RV pressure overload** (เช่น PH), **diastolic flattening = RV volume overload** (เช่น ASD, severe TR) — common name; เป็นเครื่องมือแยก pressure vs volume overload
- **60/60 sign** — ใน acute PE: **PASP <60 mmHg + RV outflow acceleration time <60 ms** บ่งชี้ acute RV afterload สูงเฉียบพลัน — common name
- **Cherry-on-top / apical sparing ("bull's-eye") pattern** — บน **GLS bull's-eye map**: apical strain preserved ขณะที่ basal/mid ถูกกด — signature ของ **cardiac amyloidosis** (relative apical longitudinal strain) — common name
- **Lambl's excrescences** — เส้นใย fibrous เล็กๆ ที่ขอบ aortic valve (มัก incidental) — อาจสับสนกับ vegetation/fibroelastoma ตั้งชื่อตาม Vilém Dušan **Lambl** (Czech)
- **Coanda effect** — jet ของ MR ที่ eccentric ไหลเลียบผนัง LA ทำให้ **ดู jet เล็กกว่าความจริง** → ประเมิน MR ต่ำกว่าจริง — physical effect (ชื่อ Henri **Coandă**, Romanian)
- **Venturi effect** — high-velocity flow สร้าง low-pressure ดูด leaflet — กลไกเบื้องหลัง SAM — physical (Giovanni **Venturi**)
- **B-lines / lung comet** — ใน lung ultrasound (POCUS): vertical reverberation artifact บ่งชี้ **interstitial edema/EVLW** — common name (ไม่ใช่ echo แต่คู่กับ cardiac POCUS)
- **Spontaneous echo contrast (SEC, "smoke")** — swirling echodensity ใน LA/LAA จาก low-flow + rouleaux — บ่งชี้ **stasis + thrombus risk** (เช่น AF, MS) — common name

> McConnell (RV apex สู้) กับ apical sparing amyloid (LV apex สู้) เป็น "apex ที่รอด" คนละบริบท — อย่าสับสน
> 

---

# 📈 3. M-mode Signs & Patterns

M-mode ("ice-pick") ความละเอียดเวลาสูง จับ motion เร็วๆ ได้ดี — signs คลาสสิกหลายอันเป็นภาพจากยุคก่อน 2D แต่ยังใช้จริง

- **EPSS (E-point Septal Separation)** — ระยะห่างระหว่าง anterior mitral leaflet E-point กับ septum; **เพิ่มขึ้น (>7 mm) = LV systolic dysfunction/ลด EF** (mitral เปิดไม่สุดเพราะ SV ต่ำ) — common name; ใช้ประเมิน EF เร็วๆ ข้างเตียง
- **B-bump (B-notch)** ของ mitral valve — notch บน closure ของ anterior leaflet บ่งชี้ **elevated LVEDP** (mitral ปิดล่าช้าเพราะ LA-LV pressure crossover) — common name
- **Fluttering ของ anterior mitral leaflet** — diastolic fluttering จาก **AR jet** กระทบ leaflet (คู่ echo ของ Austin Flint murmur) — common name
- **Premature/early closure ของ mitral valve** — ใน **acute severe AR**: LV pressure พุ่งเร็วจน mitral ปิดก่อน QRS — เป็น danger sign ของ acute AR — common name
- **Mid-systolic notching / "flying W" ของ pulmonic valve** — บ่งชี้ **pulmonary hypertension** (RV afterload สูง ทำ pulmonic valve ปิดเร็วกลางคลื่น) — common name
- **Boxcar / "box" appearance** — mitral valve M-mode ที่แบนราบใน **rheumatic MS** (leaflet แข็ง เคลื่อนน้อย, EF slope ลด) — common name
- **Systolic anterior motion บน M-mode** — SAM เห็นเป็น anterior movement ของ mitral ในช่วง systole (ยืนยัน HOCM) — common name

---

# 📐 4. Chamber & Function Parameters (with cutoffs)

> normal cutoff อ้าง **ASE/EACVI Chamber Quantification 2015** และ **ASE Diastolic Function 2016 (+ 2025 update)** — search 21 ก.ค. 2026; ASE ไม่อยู่ใน guideline list จึงระบุในเนื้อ
> 

| Parameter | ความหมาย | Cutoff |
| --- | --- | --- |
| **LVEF (Simpson biplane)** | systolic function | ปกติ ♂ 52–72% / ♀ 54–74%; reduced <50% (HFrEF ≤40%) |
| **TAPSE** | RV longitudinal systolic function (M-mode lateral tricuspid annulus) | **<17 mm = RV dysfunction** (2015 ASE); 2025 ASE ใช้ graded range |
| **RV S′ (tissue Doppler)** | RV basal systolic velocity | <9.5 cm/s บ่งชี้ RV dysfunction |
| **E/e′ (average)** | LV filling pressure surrogate | **>14 = elevated** (2016 ASE); **<7 = normal**; 7–14 → ใช้ SRIVR หรือ TR velocity (>2.8 m/s) ช่วย (2025 update) |
| **e′ (septal / lateral)** | myocardial relaxation | septal e′ <7, lateral e′ <10 cm/s = impaired relaxation |
| **LAVi (LA volume index)** | chronicity ของ filling pressure สูง | >34 mL/m² = enlarged |
| **Deceleration time (DT) ของ E** | filling pattern | สั้น <150 ms = restrictive/grade 3 diastolic dysfunction |
| **TR Vmax** | ประเมิน PASP | >2.8 m/s บ่งชี้ elevated PA pressure/filling pressure |
| **LV GLS (global longitudinal strain)** | subclinical systolic function | ปกติ negative กว่า **−20%** (เช่น −22%); less negative = impaired |
| **FAC (RV fractional area change)** | RV global systolic | <35% = RV dysfunction |
| **IVC diameter/collapse** | RA pressure estimate | <2.1 cm + collapse >50% → RAP ~3 mmHg |

> ค่าเหล่านี้เปลี่ยนตาม guideline edition — โดยเฉพาะ **2025 ASE** ปรับ TAPSE/diastolic algorithm; ดู [HFpEF (Heart Failure with Preserved Ejection Fraction)](HFpEF%20(Heart%20Failure%20with%20Preserved%20Ejection%20Fract%20387224abad8181e4b79ce5d452a2c835.md) สำหรับ diastolic function algorithm ฉบับเต็ม
> 

---

# 🫀 5. Named Anatomy & Normal Variants (seen on echo)

structure ที่มักเจอแล้วต้องแยกจาก pathology (thrombus/vegetation/mass)

- **Chiari network** — reticular remnant ของ right valve of sinus venosus ใน RA (ต่อจาก IVC/coronary sinus) — normal variant, อย่าเข้าใจผิดเป็น thrombus/vegetation ตั้งชื่อตาม Hans **Chiari** (Austrian pathologist)
- **Eustachian valve** — flap ที่ IVC-RA junction (นำเลือดไป foramen ovale ในทารก) — normal; ถ้าเด่นมากเรียก prominent Eustachian valve ตั้งชื่อตาม Bartolomeo **Eustachi**
- **Thebesian valve** — flap เล็กที่ coronary sinus ostium ตั้งชื่อตาม Adam Christian **Thebesius**
- **Moderator band** — muscular band ข้าม RV apex (มี right bundle branch วิ่งผ่าน) — landmark ยืนยันว่าเป็น morphologic RV — common name
- **Crista terminalis** — ridge ใน RA (รอยต่อ smooth/trabeculated) — อาจดูเหมือน mass — common name
- **Coumadin ridge (warfarin ridge / "Q-tip")** — ridge ระหว่าง LAA กับ left upper pulmonary vein ใน LA — normal, อย่าเข้าใจผิดเป็น thrombus — common name
- **Lipomatous hypertrophy ของ interatrial septum** — ไขมันสะสมที่ septum (เว้น fossa ovalis → "dumbbell") — normal variant — common name
- **Lambl's excrescences** — (ดูหมวด 2) valvular strand ที่ aortic valve

---

# 🫦 5B. Disease-Specific Named Signs & Scores (Valve Morphology & Doppler Patterns)

กลุ่มนี้เป็น named sign/score ที่ผูกกับ pathology เฉพาะเจาะจง — รายละเอียดของโรคนั้นดูที่เพจโรคเฉพาะ ที่นี่รวบรวมเฉพาะส่วนที่เป็น "ชื่อ"/"pattern" ที่จำเป็นต้องรู้เพื่อไม่ให้ซ้ำกับเพจโรคเฉพาะ

**Rheumatic Mitral Stenosis:**

- **Hockey-stick sign** — PSLA/PLAX: anterior mitral leaflet **doming** ขณะ diastole (tip ของ leaflet เคลื่อนไหวน้อยกว่า base เพราะ tip fusion) — เกิดจาก commissural fusion + leaflet tip แข็ง (✅ verified 28 ก.ค. 2026)
- **Fish-mouth (buttonhole) appearance** — PSAX ที่ระดับ mitral valve: valve orifice เป็นรูป funnel/ปากปลา จาก commissural fusion — ใช้ดู planimetry MVA (✅ verified)
- **Wilkins (Wilkins-Block) score** — 16-point echo score ทำนายความสำเร็จของ **percutaneous mitral balloon valvuloplasty (PMBC)**: 4 องค์ประกอบ — **leaflet mobility, leaflet thickening, subvalvular thickening, calcification** (แต่ละข้อให้ 1-4 คะแนน รวม 4-16); **≤ɒ8 คะแนน = favorable anatomy** (PMBC สำเร็จสูง), 9-11 = intermediate, **>11 = poor candidate** (สูงต่อ complication) — ดู [MS (Mitral Stenosis) — Rheumatic Pathophysiology, Auscultation & PMBC Decision](MS%20(Mitral%20Stenosis)%20%E2%80%94%20Rheumatic%20Pathophysiology,%20%203a0224abad8181f2a1cdcfe5edaa93c1.md) สำหรับ decision algorithm เต็ม (✅ verified)

**HOCM (Doppler patterns):**

- **Dagger-shaped CW Doppler** — LVOT flow velocity ขึ้นช้าใน early systole แล้วเร่งขึ้นอย่างฉับพลันใน late systole (peak ช้า) — สะท้อน dynamic LVOT obstruction จาก SAM ที่เพิ่มขึ้นเรื่อยๆ (✅ verified)
- **Lobster-claw sign (PW Doppler)** — bifid systolic flow profile (mid-systolic dip) พบใน **mid-ventricular obstruction** หรือ **apical HCM ที่มี apical aneurysm** — สะท้อนการตกของ ejection velocity กลาง systole จาก severe mid-cavity narrowing (✅ verified)

**Ebstein's Anomaly:**

- **FREST features** — mnemonic สำหรับ anterior tricuspid leaflet ใน Ebstein: **F**enestration, **R**edundant, **E**longated, **S**ail-like, **T**ethering — แต่ละ feature พบใน literature standard (redundant/dysplastic leaflet, sail-like anterior leaflet, tethering ของ chordae) — ⚠️ สืบค้นแล้วไม่พบชื่อ acronym "FREST" เป็น formal classification ใน literature — ใช้เป็น mnemonic ช่วยจำ feature ไม่ใช่ validated score

**Endomyocardial Fibrosis (EMF):**

- **Merlon sign** — basal ventricle **hypercontraction** ต่อต้านกับ apex ที่ obliterated/immobile (ชื่อเปรียบกับ merlon = ส่วนทึบของ battlement ที่สูง-ต่ำสลับ) มักเห็นคู่กับ **square root sign** บน M-mode ของ septum/posterior wall (✅ verified)

**Ruptured Sinus of Valsalva:**

- **Windsock (deformity) sign** — elongated tubular/windsock-shaped structure โบกจาก ruptured sinus สู่ RVOT/RV เห็นชัดที่สุดทาง TEE (พบใน TTE ได้เช่นกัน) (✅ verified)

**Sinus Venosus ASD:**

- **Teardrop sign** — รูปร่างหยดน้ำของหลอดเลือดที่ TEE ระดับ RPA จาก **anomalous connection ของ right upper pulmonary vein เข้า SVC** — pathognomonic ของ sinus venosus ASD with PAPVR (⚠️ concept ยืนยันได้ แต่ชื่อ "teardrop sign" เฉพาะเจาะจงยังไม่พบใน primary literature ที่สืบได้จาก session นี้ — flag ตรวจสอบก่อนใช้ cite)

**Constrictive Pericarditis (diastolic function patterns):**

- **Annulus reversus** — lateral mitral annulus e' **ต่ำกว่า** medial e' (กลับทิศทางจาก normal physiology ที่ lateral e' สูงกว่า) — เกิดจาก pericardial tethering ที่ด้าน lateral wall มากกว่า septal (ซึ่ง septal ยัง "หลุด" จาก pericardium ผ่าน septal shift)
- **Annulus paradoxus** — E/e' ratio **ต่ำ** (ดูเหมือน filling pressure ปกติ) แต่ PCWP **สูง** จริง — เพราะ medial e' สูงผิดปกติจาก exaggerated early diastolic septal motion (constraint effect) ไม่ใช่ preserved myocardial relaxation จริง

---

# 🔬 6. Modalities, Views & Artifacts

- **TTE / TEE** — Transthoracic / Transesophageal echo — common
- **3D / 4D echo** — volumetric — common
- **Speckle-tracking echocardiography (STE)** — วัด strain/GLS จาก speckle pattern — common
- **Tissue Doppler imaging (TDI)** — วัด myocardial velocity (e′, s′, a′) — common
- **Contrast echo (agitated saline "bubble study")** — ตรวจ intracardiac/pulmonary shunt (PFO/ASD) — common
- **Stress echo (exercise/dobutamine)** — ประเมิน ischemia/viability/low-flow low-gradient AS — common
- **Nyquist limit** — aliasing velocity limit ของ color/PW Doppler — ปรับเพื่อทำ PISA/ดู flow — common (ชื่อ Harry **Nyquist**)
- **Doppler effect** — พื้นฐานการวัด velocity — ตั้งชื่อตาม Christian **Doppler** (Austrian physicist, 1803–1853)
- **Reverberation / mirror / side-lobe / acoustic shadowing** — artifacts ที่ต้องรู้จักเพื่อไม่ตีความ mass/structure ผิด — common
- **Foreshortening** — apical view ที่ตัด apex สั้นเกิน ทำให้ EF/volume ผิด — common pitfall

---

# 🎯 High-Yield Recall

- **Formula ต้องจำ + validity**: **Bernoulli ΔP=4V²** (เติม V1 ถ้า V1>1.5/V2>3) · **Continuity AVA=(CSA×VTI_LVOT)/VTI_AV** (พังถ้ามี AR) · **PISA EROA=2πr²·Val/Vpeak** · **MVA=220/PHT** (Hatle; พังใน AR/diastolic dysfunction) · **RVSP=4(TR Vmax)²+RAP**
- **Emergency signs**: **McConnell** (RV free-wall akinesia + apex รอด = acute PE) · **D-sign** (systolic=pressure overload, diastolic=volume overload) · **60/60 sign** (acute PE)
- **Disease signatures**: **SAM** = HOCM (Venturi) · **apical sparing/cherry-on-top GLS** = amyloid · **premature MV closure** = acute severe AR · **flying W pulmonic** = PH
- **M-mode**: **EPSS >7 mm** = ลด EF · **B-bump** = สูง LVEDP · **MV fluttering** = AR (echo คู่ของ Austin Flint)
- **Cutoff**: **TAPSE <17 mm**, **E/e′ >14** elevated / <7 normal, **LAVi >34**, **GLS ปกติ < −20%**, **DT <150 ms** = restrictive
- **อย่าเข้าใจผิดเป็น mass**: Chiari network, Eustachian valve, Coumadin ridge, moderator band, lipomatous septum
- **Disease-specific named signs**: rheumatic MS — **hockey-stick** (PLAX doming) + **fish-mouth** (PSAX orifice) + **Wilkins score** (≤8 favorable / >11 poor PMBC candidate) · HOCM — **dagger-shaped CW** + **lobster-claw PW** (mid-cavity/apical obstruction) · Ebstein — **FREST** (mnemonic, ไม่ใช่ validated score) · EMF — **Merlon sign** (basal hypercontraction+apex obliteration) · ruptured sinus of Valsalva — **windsock sign** · constrictive pericarditis — **annulus reversus/paradoxus**
- 🔍 Verification status
    
    **✅ Searched & verified (21 ก.ค. 2026)**
    
    - Simplified Bernoulli ΔP=4V² + V1 correction (V1>1.5/V2>3 m/s) — ASE "Equations You Should Know", Thoracic Key, [echocardiografie.nl](http://echocardiografie.nl) (JASE 2009)
    - Continuity AVA = (CSA_LVOT×VTI_LVOT)/VTI_AV — StatPearls, CAVALIER study
    - PISA EROA = 2πr²×V_aliasing/V_peak — [echocardiographer.org](http://echocardiographer.org), ASE Tighe review
    - Pressure half-time MVA = 220/PHT (Hatle 1979 empirical constant; PHT = Vmax→Vmax/1.4; overestimate ใน diastolic dysfunction / underestimate ใน AR) — Hatle Circulation 1979, johnsonfrancis, 123sonography, PubMed
    - TAPSE <17 mm (2015 ASE Chamber Quant; 2025 graded); RV S′ <9.5 — onlinejase, cardioserv 2025
    - E/e′ >14 elevated / <7 normal, SRIVR & TR velocity >2.8 pathway (2016 + 2025 ASE) — Guideline Central 2025
    - LV GLS ปกติ < −20%, apical sparing = amyloid signature — JACC Imaging, EHJ-CI
    
    **⚠️ From standard reference / general knowledge, not individually re-verified this session**
    
    - Gorlin/Hakki, Teichholz vs Simpson caveat — standard echo/cath knowledge
    - ชื่อบุคคล (Hatle, Doppler, Coandă, Venturi, Nyquist, McConnell, Chiari, Eustachi, Thebesius, Lambl) — ความรู้มาตรฐาน ยังไม่ search รายคน
    - M-mode signs (EPSS >7 mm, B-bump, flying W, boxcar) — standard, threshold EPSS อาจต่างเล็กน้อยตามแหล่ง (5–7 mm)
    - Chamber cutoffs อื่น (LAVi 34, DT 150, FAC 35%, IVC/RAP) — ASE reference values มาตรฐาน, ไม่ได้ re-search รายค่า
    
    **🔴 Flagged / ระวัง**
    
    - **2025 ASE** ปรับ TAPSE เป็น graded severity + diastolic algorithm ใหม่ — ตัวเลข single-cutoff ในตารางเป็นของ 2015/2016 edition; re-check ฉบับล่าสุดก่อนใช้ report จริง
    - EPSS cutoff (5 vs 7 mm) และ GLS normal (−18 ถึง −22% ตาม vendor) มี inter-vendor/inter-guideline variation
    - normal EF range ต่างกันเล็กน้อยตาม guideline/gender — ใช้ค่าอ้างอิงของ lab ตัวเอง
    
    **✅ Searched & verified (28 ก.ค. 2026, เพิ่มเติม):**
    
    - Wilkins score 4 components (mobility/thickening/subvalvular/calcification), 4-16 คะแนน, ≤8 favorable / >11 poor — Healio, [johnsonfrancis.org](http://johnsonfrancis.org), JACC:Asia 2026, [appcardio.com](http://appcardio.com)
    - Hockey-stick sign (PLAX AML doming) + fish-mouth appearance (PSAX orifice) ใน rheumatic MS — [cardiologyoutlines.com](http://cardiologyoutlines.com), radiologykey, journal of echocardiography
    - Dagger-shaped CW Doppler + lobster-claw PW Doppler ใน HOCM (mid-cavity/apical obstruction) — JACC Case Reports, ESC Council Cardiovascular Genomics, Polish Heart Journal
    - Merlon sign (basal hypercontraction + apex obliteration, คู่กับ square root sign) ใน EMF — [johnsonfrancis.org](http://johnsonfrancis.org)
    - Windsock deformity ใน ruptured sinus of Valsalva (TEE/TTE) — PMC, PubMed (case reports)
    
    **⚠️ From literature-consistent description, not fully re-verified:**
    
    - FREST mnemonic สำหรับ Ebstein — แต่ละ feature (fenestration/redundant/elongated/sail-like/tethering) ตรงกับ standard literature แต่ไม่พบ acronym "FREST" เป็น formal named score
    - Annulus reversus/annulus paradoxus (constrictive pericarditis) — เป็นคำศัพท์มาตรฐานใน echo/cath literature เรื่อง constrictive pericarditis ไม่ได้ re-search เฉพาะเจาะจง session นี้
    
    **🔴 Flagged uncertain:**
    
    - **Teardrop sign** (sinus venosus ASD/PAPVR) — ยืนยันได้เฉพาะ concept (RUPV anomalous connection → teardrop-shaped color flow ที่ RPA level บน TEE) แต่ไม่พบการระบุชื่อ "teardrop sign" โดยตรงใน primary source ที่สืบได้ — ใช้ด้วยความระมัดระวัง
