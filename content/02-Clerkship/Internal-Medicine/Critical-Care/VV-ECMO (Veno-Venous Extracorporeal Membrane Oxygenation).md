---
title: "VV-ECMO (Veno-Venous Extracorporeal Membrane Oxygenation)"
aliases: ["VV-ECMO (Veno-Venous Extracorporeal Membrane Oxygenation)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
type: "Discrete entity"
guidelines: ["ATS/ERS", "SSC/SCCM"]
review_status: "New"
tags: []
created: 2026-08-05
notion_id: 3b3224ab-ad81-8149-8451-c524edcea2d9
source: notion-migration
---

# VV-ECMO (Veno-Venous Extracorporeal Membrane Oxygenation)

> [!info]
> 

> Governing bodies: **ELSO 2021** (VV-ECMO adult respiratory guideline) เป็น consensus หลัก; **ATS 2024** และ **ESICM 2023** ให้คำแนะนำเชิง guideline. ELSO ไม่อยู่ใน Guidelines property list จึงระบุในเนื้อหาแทน.
> 

## Overview — what VV-ECMO does and does not do

VV-ECMO เป็น extracorporeal life support ที่ทำหน้าที่ทดแทน **gas exchange** ของปอด โดยดึงเลือด deoxygenated ออกจาก venous system ผ่าน membrane oxygenator แล้วคืนกลับเข้า venous system เช่นเดิม ตำแหน่งที่คืนเลือดคือ venous side จึงไม่มีการเพิ่ม forward flow ให้ระบบไหลเวียน ผู้ป่วยต้องมี native cardiac output ที่เพียงพอด้วยตัวเอง หลักการนี้แยก VV-ECMO ออกจาก VA-ECMO อย่างชัดเจน VA คืนเลือดเข้า artery จึงให้ทั้ง gas exchange และ hemodynamic support ส่วน VV ให้เฉพาะ gas exchange อย่างเดียว

ประโยชน์เชิงกลไกที่แท้จริงของ VV-ECMO ไม่ได้อยู่ที่การเพิ่มออกซิเจนเพียงอย่างเดียว แต่อยู่ที่การเปิดโอกาสให้ตั้ง ventilator แบบ **ultra-lung-protective** ได้ เมื่อ circuit รับภาระ gas exchange ไปแล้ว จึงลด tidal volume, plateau pressure และ driving pressure ลงจนถึงระดับที่หยุด ventilator-induced lung injury (VILI) ได้ ปอดจึงได้ rest และมีเวลาให้ lung injury หายเอง ตรง ๆ เลยคือ ECMO ไม่ได้รักษา ARDS มันซื้อเวลาและตัด VILI ออกไปจากสมการ

ดูภาพรวม circulatory MCS (IABP, Impella, VA-ECMO) ที่ [[MCS (Mechanical Circulatory Support) — Durable LVAD & Temporary MCS (IABP · Impella · VA-ECMO)]]; ดูโรคหลักที่เป็น indication ที่ [[ARDS (Acute Respiratory Distress Syndrome)]]

## 1. ⚙️ Mechanism & gas-exchange physiology

**Circuit path**: venous drainage cannula → centrifugal pump → membrane oxygenator (mixes sweep gas) → return cannula → venous system

การควบคุม gas exchange ใน VV-ECMO แยกออกเป็นสองแกนอิสระ ซึ่งเป็น concept หลักที่ต้อง internalize:

- **Oxygenation** คุมด้วย **ECMO blood flow (pump flow)** เป็นหลัก ยิ่ง flow สูง สัดส่วนของ cardiac output ที่ผ่าน oxygenator ยิ่งมาก arterial oxygenation จึงดีขึ้น การเพิ่ม FiO₂ ของ sweep gas (FdO₂) ช่วยได้ระดับหนึ่งแต่ถึง ceiling เร็ว เพราะเลือดที่ผ่าน membrane อิ่มตัวเกือบ 100% อยู่แล้ว ปัจจัยจำกัดคือ **สัดส่วน ECMO flow ต่อ cardiac output** ไม่ใช่ FdO₂
- **CO₂ removal** คุมด้วย **sweep gas flow** (gas ที่ไหลผ่านอีกฝั่งของ membrane) CO₂ diffuse ผ่าน membrane ได้เร็วกว่า O₂ มาก การ clear CO₂ จึงมีประสิทธิภาพสูงแม้ใช้ blood flow ต่ำ ปรับ sweep ขึ้นเพื่อล้าง CO₂ ออกมากขึ้นโดยไม่กระทบ oxygenation

ความเป็นอิสระของสองแกนนี้อธิบายว่าทำไม low-flow extracorporeal CO₂ removal (ECCO₂R) จึงจัดการ hypercapnia ได้ด้วย flow เพียง 0.5–1.5 L/min ในขณะที่ full VV-ECMO ต้องการ flow 3–6 L/min เพื่อแก้ hypoxemia

**Determinants ของ arterial oxygenation ระหว่าง VV-ECMO** ได้แก่ ECMO flow, ปริมาณ recirculation, native lung function ที่เหลืออยู่, hemoglobin และ cardiac output ที่สูงขึ้น (เช่น sepsis, hyperdynamic state) กลับทำให้ arterial saturation ต่ำลงได้ เพราะสัดส่วน blood ที่ผ่าน oxygenator ลดลงเมื่อเทียบกับ total venous return ประเด็นนี้ขัด intuition ของหลายคน high cardiac output ไม่ได้ช่วย oxygenation ใน VV-ECMO แต่ทำให้แย่ลง

## 2. 🔄 Recirculation — the defining inefficiency of VV-ECMO

Recirculation คือปัญหาเฉพาะตัวของ VV-ECMO ที่ไม่มีใน VA-ECMO และเป็นสาเหตุอันดับต้น ๆ ของ refractory hypoxemia บน circuit ที่ทำงานปกติ

**นิยาม**: recirculation fraction (Rf) คือสัดส่วนของเลือด oxygenated ที่เพิ่งคืนออกจาก return cannula แล้วถูกดูดกลับเข้า drainage cannula ทันที โดยไม่ทันผ่าน tricuspid valve ไปสู่ pulmonary artery และ systemic circulation เลือดส่วนนี้วนอยู่ใน circuit เปล่า ๆ ไม่ได้ทำ gas exchange ให้ผู้ป่วยจริง

**ผลเชิงกลไก**: เมื่อ Rf สูงขึ้น **effective ECMO flow** (flow ที่ทำ gas exchange ให้ผู้ป่วยจริง) ลดลง แม้ pump แสดง flow ตัวเลขสูงเท่าเดิม ผู้ป่วยจึง desaturate ทั้งที่ console บอกว่า flow ปกติ ลักษณะเด่นที่ชี้ recirculation คือ **preoxygenator (drainage-side) saturation สูงผิดปกติ** เพราะเลือดที่ดูดกลับมี oxygenated blood ปนอยู่มาก ปกติ preoxygenator saturation ควรอยู่ราว **70–80%** ถ้าขึ้นไปใกล้เคียง postoxygenator saturation ให้สงสัย recirculation ทันที

**ตัวกำหนด recirculation**:

| ปัจจัย | ทิศทางที่เพิ่ม recirculation | กลไก |
| --- | --- | --- |
| **ระยะห่าง drainage–return port** | ยิ่งใกล้กันยิ่งเพิ่ม | inflow jet ถูกดูดกลับก่อนกระจาย |
| **Cannula tip position** | port หันเข้าหากัน / return jet ไม่ชี้เข้า tricuspid valve | เลือด oxygenated วิ่งตรงเข้าปาก drainage |
| **ECMO flow เทียบ cardiac output** | flow สูงเมื่อ CO ต่ำ | flow เกินกว่าที่ venous return จะป้อนได้ ดูดเลือดตัวเองกลับ |
| **Cardiac output ต่ำ / hypovolemia** | เพิ่ม | venous return ไม่พอ pump ดึงเลือด return กลับแทน |
| **Cannula configuration** | femoral-femoral เสี่ยงกว่า | ports อยู่ใน IVC เดียวกัน ใกล้กัน |
| **RAP สูง / RA anatomy** | เพิ่ม | เปลี่ยน flow dynamic รอบ port |

**ตัวเลข Rf ตาม configuration** (วัดด้วย ultrasound dilution และ computational model): bicaval dual-lumen cannula ที่วางตำแหน่งถูกต้องให้ **Rf < 7%** และในเคสที่วางเหมาะสมวัดได้ต่ำถึง **~2%** ส่วน conventional single-stage cannula ที่วางไม่ดีวัดได้สูงถึง **~38%** การเปลี่ยนไปใช้ multistage cannula ที่ออกแบบ side-hole กระจายตัวลด Rf ลงเหลือราว **19% เทียบกับ conventional 38%** ตัวเลขเหล่านี้ตอกย้ำว่า cannula design และ position มีผลต่อประสิทธิภาพจริงมากกว่าที่ตัวเลข pump flow บอก

**Cannulation strategies กับ recirculation**:

- **Dual-lumen bicaval cannula** (เช่น Avalon, Crescent) — ใส่ทาง right IJ ผ่าน SVC-RA-IVC, drainage ports อยู่ที่ SVC และ IVC ส่วน return port ชี้เข้า tricuspid valve ให้ recirculation ต่ำสุดและช่วย mobilization ได้ แต่ต้องวางตำแหน่งแม่นยำใต้ echo/fluoroscopy การหมุน (rotation) หรือความลึกที่คลาดเคลื่อนทำให้ return jet เลื่อนออกจาก tricuspid แล้ว Rf พุ่งขึ้นทันที
- **Femoro-jugular** (drainage femoral IVC → return IJ/SVC) — configuration มาตรฐานสำหรับ two-cannula ระยะห่างของ ports มากพอ recirculation ต่ำ เป็น default ของหลายศูนย์
- **Femoro-femoral** (ทั้ง drainage และ return ใน IVC) — เสี่ยง recirculation สูงสุดเพราะ ports อยู่ใกล้กันใน vessel เดียว ต้องเว้นระยะ tip ให้ห่างและ monitor ใกล้ชิด

**การประเมินและแก้ไข recirculation ข้างเตียง**:

- สงสัยเมื่อ SpO₂ ผู้ป่วยต่ำทั้งที่ pump flow เพียงพอ ร่วมกับ preoxygenator saturation สูงผิดปกติ (เลือด drainage สีแดงสด)
- ยืนยันตำแหน่ง cannula ด้วย echocardiography (TTE/TEE) หรือ CXR ประเมิน return jet ว่าชี้เข้า tricuspid หรือไม่
- วัด Rf เชิงปริมาณด้วย **ultrasound dilution technique** ถ้ามีเครื่อง
- แก้ไข: reposition cannula, ปรับ tip depth, ลด ECMO flow ให้สมดุลกับ venous return, แก้ hypovolemia เพื่อเพิ่ม venous return, พิจารณาเปลี่ยน configuration ถ้า recirculation ดื้อ

> [!danger] 🚨 STRICT AVOIDANCE / RED FLAGS
> 

> - **อย่าตีความว่า desaturation บน VV-ECMO = oxygenator failure เสมอ** ตรวจ recirculation (preoxygenator saturation สูง) และ high cardiac output state ก่อนเปลี่ยน oxygenator
> 

> - **อย่าเร่ง ECMO flow สูงเกินกว่า venous return จะป้อนได้** จะยิ่งเพิ่ม recirculation และเกิด drainage-line chatter/suck-down แทนที่จะแก้ hypoxemia
> 

> - **VV-ECMO ไม่ให้ hemodynamic support** ผู้ป่วย shock ที่ต้องการ circulatory support ต้องพิจารณา VA หรือ VAV ไม่ใช่ VV
> 

> - **ระวัง air entrainment ที่ negative drainage pressure สูงเกิน** และ pump-related hemolysis
> 

## 3. 🎯 Indications & patient selection

VV-ECMO พิจารณาใน severe respiratory failure ที่ **potentially reversible** และ refractory ต่อ conventional therapy ที่ optimize เต็มที่แล้ว (รวม lung-protective ventilation, prone positioning, neuromuscular blockade)

| Indication | Threshold ที่ใช้อ้างอิง | ที่มา |
| --- | --- | --- |
| **Refractory hypoxemia** | PaO₂/FiO₂ **< 80 mmHg** (หรือ < 50 นานกว่า 3 ชม.) despite optimization | EOLIA entry criteria |
| **Severe hypoxemia (composite)** | **Murray/Lung Injury Score ≥ 3** | CESAR entry criteria |
| **Refractory hypercapnia** | **pH < 7.25** with PaCO₂ ≥ 60 mmHg นานกว่า 6 ชม. despite optimal vent | ELSO 2021 |
| **Uncompensated respiratory acidosis** | plateau pressure สูงเกินทนได้ทั้งที่ตั้ง protective vent แล้ว | ELSO 2021 |

**Bridging indications อื่น ๆ** ได้แก่ bridge to lung transplantation, primary graft dysfunction หลัง lung transplant, severe air leak syndrome และ status asthmaticus ที่ดื้อการรักษา (ดู [[Lung Transplantation — Indication, PGD & CLAD (CVT)]])

**Contraindications**:

- **Irreversible lung disease** ที่ไม่มี transplant pathway (VV-ECMO ไม่มีจุดจบ)
- **Severe multiorgan failure** ที่ทำให้ futile
- **Contraindication ต่อ anticoagulation** ที่รุนแรง เช่น major uncontrolled bleeding, recent hemorrhagic stroke
- **Prolonged mechanical ventilation** ด้วย high pressure (มักใช้ **> 7 วัน** เป็น relative cutoff จาก trial exclusion เพราะบ่งชี้ irreversibility)
- **Advanced age + comorbidity** ที่ prognosis แย่ (CESAR จำกัด ≤ 65 ปี, EOLIA ไม่กำหนด upper age)
- **Severe immunosuppression / underlying condition** ที่ survival ต่ำมาก

การตัดสินใจต้องผ่าน **reversibility และ futility assessment** ร่วมกับทีม ECMO ที่มีประสบการณ์ scoring เช่น **RESP score** และ **PRESERVE score** ช่วยประเมิน prognosis แต่ไม่ทดแทน clinical judgment ของ multidisciplinary team

## 4. 💊 Management on VV-ECMO

**Ventilator lung rest settings** (หลัง cannulation gas exchange โอนไป circuit แล้ว): เป้าคือ minimize VILI ค่าที่ใช้เป็น historical standard คือ PCV mode, **plateau pressure ≤ 20–24 cmH₂O**, **PEEP ~10 cmH₂O**, **RR ~10/min**, **FiO₂ 0.3**, I:E 1:1 โดยยอมให้ tidal volume ต่ำมาก (อาจ < 4 mL/kg PBW หรือต่ำกว่า) ในเคส poor compliance การตั้งค่าที่ optimal ยัง not well-defined และเป็นประเด็นวิจัยต่อเนื่อง การศึกษา ultra-protective 48 ชม. ไม่ลด biotrauma และมี trend mortality สูงขึ้น จึงยังไม่แนะนำให้กด setting สุดโต่งเป็น routine

**Anticoagulation**: unfractionated heparin เป็น default titrate ตาม aPTT หรือ anti-Xa; ELSO แนะนำ balance ระหว่าง circuit thrombosis กับ bleeding เป็นรายผู้ป่วย เป้า target ต่ำกว่าเมื่อ bleeding risk สูง

**Flow & sweep titration**: ตั้ง blood flow ให้พอ maintain SaO₂ target (มัก accept ~88–92% ใน VV-ECMO ถ้า tissue oxygenation ยังพอ) และปรับ sweep ตาม PaCO₂ โดยลด PaCO₂ อย่างช้า ๆ ในผู้ป่วยที่ chronic hypercapnia เพื่อเลี่ยง rapid alkalosis และ cerebral injury

**Fluid & general care**: conservative fluid strategy สัมพันธ์กับ outcome ที่ดีกว่า (positive fluid balance สัมพันธ์กับ mortality สูงขึ้น) ร่วมกับ early mobilization/rehabilitation ตาม ELSO 2024 guideline, sedation ให้น้อยที่สุดเท่าที่ปลอดภัย, และ nutrition, VAP prevention ตามปกติ

**Weaning**: เมื่อ native lung ฟื้น ทดสอบด้วยการลด **sweep gas flow** ลงจนถึง off (sweep trial) โดยคง blood flow ไว้ แล้วประเมิน gas exchange ของ native lung ที่ ventilator setting ที่ยอมรับได้ ถ้า PaO₂/FiO₂ และ PaCO₂ ยังดีที่ sweep = 0 นานพอ จึง decannulate หลักการคือ oxygenation คุมด้วย blood flow ส่วน weaning ทดสอบผ่าน sweep

**Complications ที่ต้องเฝ้าระวัง**: bleeding (พบบ่อยสุด โดยเฉพาะ cannula site และ intracranial), hemolysis, circuit/oxygenator thrombosis, cannula-associated infection, HIT และ neurologic injury การติดตาม D-dimer, plasma free Hb และ transmembrane pressure gradient ช่วยจับ oxygenator failure ก่อน decompensate

> [!warning] 🇹🇭 Thai availability
> 

> VV-ECMO มีเฉพาะใน ECMO-capable centers (โรงพยาบาลมหาวิทยาลัยและศูนย์ใหญ่ เช่น รามาธิบดี ศิริราช จุฬาฯ) ไม่ได้มีทุกโรงพยาบาล ต้อง refer ล่วงหน้าเมื่อผู้ป่วยเข้าเกณฑ์ ก่อนถึงจุดที่ transfer ไม่ได้ (heparin, cannula, circuit consumables มีในศูนย์เหล่านี้)
> 

## 5. 📚 Landmark Trials & Evidence

- **CESAR (Lancet 2009)** — randomise 180 ราย UK ให้ transfer ไปศูนย์ ECMO เทียบกับ conventional care ที่ รพ.ต้นทาง กลุ่ม referral มี survival without severe disability ที่ 6 เดือนดีกว่า แต่มีเพียง ~76% ของกลุ่ม transfer ที่ได้ ECMO จริง และ conventional arm ไม่ได้ standardize ventilation จึงตีความเป็นประโยชน์ของ ECMO-capable center care มากกว่าตัว ECMO เอง entry ใช้ Murray score ≥ 3, อายุ ≤ 65 ปี, ventilate < 7 วัน
- **EOLIA (NEJM 2018)** — RCT ที่ใหญ่และดีที่สุด randomise 249 รายที่ very severe ARDS ให้ early VV-ECMO เทียบ conventional + rescue ECMO หยุดก่อนกำหนดที่ interim analysis ด้วย futility rule **60-day mortality 35% (ECMO) vs 46% (control), RR 0.76 (95% CI 0.55–1.04), p = 0.09** ไม่ถึง significance แบบ frequentist จุดวิจารณ์สำคัญคือ **crossover 28%** ในกลุ่ม control ที่ได้ rescue ECMO (mortality ของกลุ่ม crossover สูงถึง 57% เพราะ sicker และเริ่มช้า) ทำให้ mortality gap แคบลง Bayesian reanalysis (Goligher, JAMA 2018) พบ probability ของ benefit สูง (~88% แม้ใช้ skeptical prior) การตีความจึงเลื่อนไปเป็นคำถามของ early ECMO strategy มากกว่า ECMO ได้ผลหรือไม่
- **Post-hoc RPSFT analysis** — ปรับ crossover แล้ว HR ~0.51 (95% CI 0.24–1.02, p = 0.055) สนับสนุนทิศทางประโยชน์

**Guideline stance ปัจจุบัน**: ELSO 2021 (VV-ECMO adult respiratory guideline) เป็น consensus หลักด้าน patient selection และ management; ATS 2024 และ ESICM 2023 ต่างแนะนำให้พิจารณา VV-ECMO ใน severe ARDS ที่ refractory ต่อ conventional therapy ในศูนย์ที่มีประสบการณ์ โดยมี grading ของ evidence และ eligibility criteria ต่างกันในรายละเอียด ทั้งคู่วางตำแหน่ง ECMO เป็น escalation หลัง evidence-based conventional strategy (รวม prone positioning) ไม่ใช่ first-line

## 🎯 High-Yield Recall

- **หลักการ**: VV-ECMO = gas exchange support เท่านั้น ไม่มี hemodynamic support ต้องมี native cardiac output พอ; ประโยชน์จริงคือเปิดทางให้ lung rest (ตัด VILI)
- **สองแกนอิสระ**: oxygenation คุมด้วย **blood flow**, CO₂ removal คุมด้วย **sweep gas flow**
- **Recirculation**: เลือด oxygenated ถูกดูดกลับก่อนถึง tricuspid valve → ลด effective flow; เบาะแส = **preoxygenator saturation สูงผิดปกติ** ทั้งที่ SpO₂ ผู้ป่วยต่ำ; bicaval DLC วางถูก Rf **< 7%** vs conventional วางแย่ ~38%
- **High cardiac output ทำให้ oxygenation แย่ลง** ใน VV-ECMO (ขัด intuition)
- **Indication**: P/F **< 80**, Murray **≥ 3**, หรือ pH **< 7.25** ที่ refractory; ต้อง reversible + ผ่านทีม ECMO
- **Weaning** ทดสอบด้วย **sweep = 0** (คง blood flow), ไม่ใช่ลด flow
- **Trials**: EOLIA (35% vs 46%, p=0.09, crossover 28%, Bayesian ชี้ benefit) + CESAR (center-effect); guideline (ELSO 2021, ATS 2024, ESICM 2023) = escalation หลัง conventional + proning ในศูนย์เชี่ยวชาญ

> [!info] 🔍 Verification status
> 

> ✅ Searched & verified (5 ส.ค. 2026): EOLIA numbers (35% vs 46%, RR 0.76, CI 0.55–1.04, p=0.09, crossover 28%, RPSFT HR 0.51); recirculation fraction (DLC <7%, ~2% optimal, conventional ~38%, multistage 19%); ELSO 2021 vent lung-rest settings; ATS 2024 / ESICM 2023 guideline stance; indication thresholds (P/F<80, Murray≥3, pH<7.25); preoxygenator sat 70–80%.
> 

> ⚠️ From source/textbook: RESP/PRESERVE score เป็น prognostic tool (ไม่ได้ verify component ในรอบนี้); Thai center list (institutional knowledge).
> 

> 🔴 Flagged: optimal ventilator strategy บน ECMO ยัง not well-defined (active research).
>
