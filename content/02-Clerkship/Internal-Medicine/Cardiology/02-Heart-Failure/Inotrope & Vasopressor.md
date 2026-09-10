---
title: "Inotrope & Vasopressor"
aliases: ["Inotrope & Vasopressor"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Heart Failure"
type: "Discrete entity"
review_status: "Reviewing"
tags: [cardiology, heart-failure, discrete-entity]
created: 2026-07-21
notion_id: 3a4224ab-ad81-8134-8fb1-fb991549c417
source: notion-migration
---

# Inotrope & Vasopressor

> Companion: [[ADHF (Acute Decompensated Heart Failure)]] · [[MCS (Mechanical Circulatory Support)]] · [[Sepsis (Sepsis-3)]] · [[HCM (Hypertrophic Cardiomyopathy)]] · [[Pulmonary Hypertension (2022 ESC-ERS)|Pulmonary Hypertension (2022 ESC/ERS)]] — *populated 26 ก.ค. 2026 จาก digest SNC3; revised 29 ก.ค. 2026 (เพิ่ม DOREMI/OptimaCC/ATHOS-3, section adverse effects, และยาที่เดิมอยู่ในตารางแต่ไม่มีเนื้อหา; digest 31 ก.ค. 2026 เพิ่ม neurogenic / hemorrhagic / anaphylactic shock ใน Clinical Selection). ⚠️ dose = mcg/kg/min (มาตรฐาน); อัตรา mL/hr ขึ้นกับ dilution ของแต่ละสถาบัน ให้ตั้ง order ตาม local protocol*
> 

# Framing — Three Mechanistic Families

ยากลุ่มนี้แยกตามเป้าหมาย hemodynamic คือ **vasopressor** เพิ่ม systemic vascular resistance (SVR) เพื่อรักษา perfusion pressure ส่วน **inotrope** เพิ่ม contractility เพื่อเพิ่ม cardiac output และ **inodilator** ทำทั้งสองอย่างพร้อมลด afterload

ในเชิงกลไกระดับเซลล์แยกได้ 3 กลุ่มที่มีผลต่างกันเรื่อง myocardial oxygen cost

- **cAMP/Ca²⁺-dependent** (catecholamine ทุกตัว, PDE3 inhibitor) เพิ่ม cytosolic Ca²⁺ จึงเพิ่มทั้ง contractility และ arrhythmia risk พร้อม O₂ consumption
- **Ca²⁺ sensitizer** (levosimendan) เพิ่มการตอบสนองของ myofilament ต่อ Ca²⁺ ที่มีอยู่เดิม โดยไม่เพิ่ม Ca²⁺ load
- **Non-adrenergic vasopressor** (vasopressin, angiotensin II) ออกฤทธิ์ผ่าน receptor คนละระบบ จึงยังทำงานได้เมื่อ adrenergic receptor ถูก desensitize

การแยกนี้กำหนดว่าเมื่อผู้ป่วยไม่ตอบสนองต่อ catecholamine จะ escalate ไปทางไหน

# 🧪 Receptor Pharmacodynamics & Dosing

| Drug | Dose (mcg/kg/min unless noted) | Receptor / กลไก | Net hemodynamic |
| --- | --- | --- | --- |
| **Dopamine** | 0.5–2 (dopaminergic) / 5–10 (β1) / >10 (α1) | dose-dependent: D→β1→α1 | ↑CO, ↑SVR (dose สูง), ↑PVR |
| **Dobutamine** | 2.5–20 | **β1 >> β2** (inodilator) | ↑CO, ↓SVR |
| **Norepinephrine** | 0.02–1 | **α1 >> β1** | ↑↑SVR, ↑CO เล็กน้อย |
| **Epinephrine** | 0.01–0.5 | β1 = β2 (low) → α1 (high) | ↑↑CO, ↑SVR, ↑lactate |
| **Phenylephrine** | 0.1–10 | **pure α1** | ↑↑SVR, ↓CO (reflex brady) |
| **Vasopressin** | 0.01–0.04 U/min (มัก fixed 0.03) | **V1 receptor** (non-adrenergic) | ↑SVR, ไม่มีผล inotropic |
| **Angiotensin II** | เริ่ม 20 ng/kg/min | **AT1 receptor** | ↑↑SVR |
| **Isoproterenol** | 2–10 mcg/min (ไม่อิงน้ำหนัก) | **β1 + β2** (chronotrope) | ↑↑HR, ↓SVR |
| **Milrinone** | 0.375–0.75 (renal impairment ลดถึง 0.125; ± load 50 mcg/kg over 10 min) | **PDE3 inhibitor** → ↑cAMP | ↑CO, ↓SVR, ↓PVR |
| **Levosimendan** | 0.05–0.2 (± load 6–12 mcg/kg over 10 min) | **Ca²⁺ sensitizer**  • K-ATP opener | ↑CO, ↓SVR, ↓PVR |

**หมายเหตุ dose ที่ต้องระวัง**

- ช่อง dopaminergic ของ dopamine เดิมนิยมเรียกว่า "renal dose" ซึ่งเป็นความเชื่อที่ถูกหักล้างไปแล้ว RCT ของ ANZICS (n=324, ผู้ป่วย SIRS ที่มี early renal dysfunction) พบว่า peak creatinine ไม่ต่างจาก placebo (245 vs 249 µmol/L, p=0.8) จึงไม่ควรสั่งเพื่อหวังผลปกป้องไต
- **2021 ESC** ระบุ norepinephrine ที่ช่วง 0.2–1.0 mcg/kg/min ซึ่งสูงกว่าที่ใช้จริงข้างเตียง ทางปฏิบัติมักเริ่มที่ 0.02–0.05 แล้ว titrate ขึ้นตาม MAP
- **Vasopressin** ให้แบบ fixed dose ไม่ titrate ตาม response และไม่ควรเกิน 0.04 U/min เนื่องจากเสี่ยง digital และ mesenteric ischemia

# ⚙️ Mechanisms & Clinical Properties

## Catecholamines

**Dobutamine** กระตุ้น β1 มากกว่า β2 จึงเพิ่ม contractility พร้อมขยายหลอดเลือดเล็กน้อย ทำให้เหมาะกับผู้ป่วยที่ cardiac output ต่ำแต่ความดันยังพอไปได้ ข้อจำกัดที่สำคัญคือ **tolerance** ซึ่งเกิดจาก β-receptor downregulation และ GRK-mediated desensitization โดยการศึกษาแบบ continuous infusion พบว่า hemodynamic response ที่ 72 ชั่วโมงเหลือ **66%** ของ response ที่ 2 ชั่วโมง และที่ 96 ชั่วโมงเหลือ **57%** ทางปฏิบัติจึงต้องเพิ่ม dose ตามเวลาที่ผ่านไป และควรวางแผน exit strategy ตั้งแต่ต้นแทนที่จะ infuse ยาวไปเรื่อย ๆ

**Norepinephrine** เป็น vasopressor หลักในทุกชนิดของ shock ที่มี cardiac origin เนื่องจากฤทธิ์ α1 เด่นชัดโดยยังมี β1 พอที่จะไม่ลด cardiac output ลง ต่างจาก phenylephrine ที่ไม่มี β1 เลย

**Epinephrine** กระตุ้น β1 และ β2 ที่ dose ต่ำ แล้วเปลี่ยนเป็น α1 เด่นที่ dose สูง ทำให้ได้ทั้ง inotropy และ vasoconstriction จากยาตัวเดียว ข้อเสียคือเพิ่ม myocardial O₂ demand, เร่ง glycolysis จน lactate สูงขึ้นแม้ perfusion จะดีขึ้น ซึ่งรบกวนการใช้ lactate เป็น marker ติดตาม และเพิ่มอัตรา refractory shock

**Phenylephrine** เป็น pure α1 agonist ที่ไม่มีฤทธิ์ chronotropic หรือ inotropic เลย ในผู้ป่วยที่ cardiac output ต่ำอยู่แล้วยาตัวนี้จะเพิ่ม afterload จน CO ลดลงต่อ จึงไม่เหมาะกับ cardiogenic shock ทั่วไป แต่กลับเป็นตัวเลือกแรกในภาวะที่ต้องการเพิ่ม afterload โดยห้ามกระตุ้น contractility คือ **dynamic LVOT obstruction** ใน HOCM เนื่องจากการกระตุ้น β จะเพิ่ม contractility และลด LV volume จนทำให้ obstruction แย่ลง ตามคำแนะนำใน 2017 AHA scientific statement เรื่อง contemporary management of cardiogenic shock

**Isoproterenol** เป็น non-selective β agonist ที่เพิ่ม heart rate เด่นและลด SVR ปัจจุบันเหลือที่ใช้อยู่ 3 สถานการณ์เฉพาะ

- **Bradycardia / high-grade AV block** เป็น bridge ก่อนใส่ temporary pacing ที่ **2–10 mcg/min**
- **Acquired torsades de pointes** โดยเร่ง heart rate ให้ถึงประมาณ **100 bpm** เพื่อย่น QT interval และตัด pause-dependent trigger ที่ **2–10 mcg/min**
- **Brugada electrical storm** โดยให้ bolus **1–2 mcg** ตามด้วย infusion **0.15–0.3 mcg/min** นาน 24 ชั่วโมง กลไกคือเพิ่ม L-type calcium current จนชดเชย transmural dispersion of repolarization ที่ RVOT

ข้อห้ามที่ต้องแยกให้ชัดคือ **congenital long QT syndrome** ซึ่ง isoproterenol จะยืด QT ต่อและกระตุ้น arrhythmia แทนที่จะระงับ

## Non-catecholamine inodilators

**Milrinone** ยับยั้ง phosphodiesterase-3 ทำให้ cAMP สะสมภายใน cardiomyocyte โดยไม่ต้องผ่าน β-receptor จึงยังออกฤทธิ์ในผู้ป่วยที่ได้รับ chronic beta-blocker นอกจากฤทธิ์ inotrope ยาลดทั้ง PCWP, SVR และ **pulmonary vascular resistance (PVR)** ซึ่งทำให้เป็นตัวเลือกที่สมเหตุสมผลใน RV failure ที่ต้องการเพิ่ม RV contractility พร้อมลด RV afterload ไปด้วยกัน ในบางสถาบันใช้รูปแบบ inhaled milrinone เพื่อให้ได้ pulmonary selectivity โดยเลี่ยง systemic hypotension ยา clearance ผ่านไตเป็นหลัก จึงต้องลด dose ใน CKD และต้องระวังว่าเมื่อหยุดยาแล้ว hypotension หรือ arrhythmia อาจคงอยู่ต่ออีกระยะ onset ประมาณ 10 นาที duration ประมาณ 5 ชั่วโมงในผู้ที่ไตปกติ

**Levosimendan** จับ **troponin C** แบบ calcium-dependent คือจับตอน systole ที่ Ca²⁺ สูง และปล่อยตอน diastole ที่ Ca²⁺ ต่ำ ทำให้เพิ่ม inotropy โดยยังคง lusitropy ไว้ และไม่เพิ่ม O₂ consumption หรือ Ca²⁺ load แขน vasodilator มาจากการเปิด **K-ATP channel** ทั้งใน systemic, coronary และ pulmonary circulation รวมถึง mitochondrial K-ATP ที่ให้ผล cardioprotection คล้าย ischemic preconditioning

จุดที่กำหนดวิธีใช้จริงคือ **active metabolite OR-1896** ซึ่งมี elimination half-life **70–80 ชั่วโมง** และขึ้นถึงระดับสูงสุดประมาณ 2–3 วันหลังหยุด infusion ทำให้ hemodynamic effect คงอยู่ราว **7–9 วัน** จากการให้ยาเพียง 24 ชั่วโมง ผลข้างเคียงที่เกิดขึ้นจึงอาจตามมาหลังผู้ป่วยออกจาก ICU ไปแล้ว

เนื่องจากกลไกไม่ผ่าน β-receptor หรือ cAMP pathway ซึ่งเป็นเส้นทางที่ถูก block ใน **CCB/BB toxicity** ยาจึงน่าสนใจในกลุ่มนี้ ข้อควรระวังคือฤทธิ์ vasodilator จะซ้ำเติม vasoplegic shock ที่ SVR ต่ำอยู่แล้ว ทางปฏิบัติจึงงด loading bolus เมื่อความดันไม่นิ่ง ใช้เดี่ยวเฉพาะเมื่อ **SBP >90 mmHg** และต่ำกว่านั้นต้องให้ร่วมกับ vasopressor

## Non-adrenergic vasopressors

**Vasopressin** ออกฤทธิ์ผ่าน V1 receptor บน vascular smooth muscle ซึ่งเป็นระบบที่แยกจาก adrenergic receptor ประโยชน์ทางคลินิกมาจาก 2 กลไก

1. ใน vasodilatory shock ที่ยืดเยื้อ endogenous vasopressin store จะถูกใช้จนพร่อง เกิด **relative vasopressin deficiency** การให้ทดแทนจึงคืน vascular tone และลด catecholamine requirement
2. **V1 receptor sensitivity ไม่เปลี่ยนตาม pH** ต่างจาก adrenergic receptor ที่ desensitize ในภาวะ acidosis ทำให้ vasopressin ยังได้ผลในผู้ป่วยที่ catecholamine เริ่มไม่ตอบสนอง

ตาม Surviving Sepsis Campaign แนะนำให้เพิ่ม vasopressin เมื่อ norepinephrine ขึ้นถึงประมาณ **0.25–0.5 mcg/kg/min** ยาไม่มีฤทธิ์ inotropic จึงไม่ช่วยเรื่อง cardiac output

**Angiotensin II** ออกฤทธิ์ผ่าน AT1 receptor เป็นทางเลือกใน catecholamine-refractory vasodilatory shock โดยยกระดับ MAP ได้เร็วภายใน 30 นาที ข้อจำกัดที่ต้องชั่งน้ำหนักคืออัตรา thrombotic event สูงกว่า placebo (**13% vs 5%** ส่วนใหญ่เป็น DVT) จึงต้องคู่กับ thromboprophylaxis

# 🎯 Clinical Selection by Scenario

- **Cardiogenic shock ทั่วไป** — norepinephrine เป็น vasopressor ตัวแรก ร่วมกับ dobutamine หรือ milrinone เป็น inotrope เมื่อยังมี hypoperfusion หลังความดันขึ้นแล้ว; inotrope ได้ Class IIb ตาม **2021 ESC HF guideline** เฉพาะกรณีที่มี peripheral hypoperfusion จาก low cardiac output; **2024 ISHLT consensus** ระบุ norepinephrine เป็น vasopressor ที่แนะนำและไม่สนับสนุน dopamine
- **เลือก dobutamine หรือ milrinone** — DOREMI แสดงว่าผลลัพธ์ทางคลินิกไม่ต่างกัน การเลือกจึงอิง profile ของผู้ป่วย: milrinone เมื่อมี PH/RV failure หรือ tachyarrhythmia เป็นข้อกังวล; dobutamine เมื่อมี renal impairment หรือความดันเปราะบาง เพราะ titrate กลับได้เร็วกว่า
- **RV failure / acute PH** — norepinephrine เพื่อรักษา aortic root pressure ให้ RV coronary perfusion ยังไปได้ ร่วมกับ milrinone หรือ dobutamine เพื่อลด PVR; หลีกเลี่ยง dopamine และ epinephrine ที่เพิ่ม PVR
- **Dynamic LVOT obstruction (HOCM, post-TAVR, Takotsubo บางราย)** — phenylephrine เป็นตัวเลือกแรก ร่วมกับ volume loading และพิจารณา beta-blocker; ห้ามให้ inotrope
- **Septic / vasoplegic shock** — norepinephrine → vasopressin → epinephrine → angiotensin II (ดู [[Sepsis (Sepsis-3)]])
- **Bradycardia, acquired TdP, Brugada storm** — isoproterenol ตาม dose เฉพาะโรคด้านบน
- **CCB/BB toxicity** — high-dose insulin euglycemia therapy เป็นหลัก โดย levosimendan หรือ milrinone เป็น adjunct เพราะเลี่ยงเส้นทางที่ถูกพิษ block
- **Advanced HF (EF <35%, NYHA III–IV, admit ซ้ำบ่อย)** — inotrope แบบ intermittent หรือ continuous ใช้เป็น bridge ไป transplant/LVAD หรือเป็น palliative therapy โดยต้องคุยเรื่องเป้าหมายการรักษาให้ชัดก่อนเริ่ม
- **Neurogenic shock (acute spinal cord injury)** — เกิดจากการสูญเสีย supraspinal sympathetic outflow ทำให้ vascular tone ตกร่วมกับ bradycardia พบเมื่อ lesion อยู่เหนือ T6 เนื่องจาก cardiac sympathetic innervation ออกจากไขสันหลังระดับ T1–T4; **norepinephrine เป็น first-line** เพราะมีทั้ง α1 (แก้ hypotension) และ β1 (พยุง heart rate) จึงจัดการทั้งสองปัญหาพร้อมกัน ให้หลัง judicious fluid resuscitation เพราะปัญหาหลักคือ vasodilation จึงระวัง volume overload; เป้า **MAP 85–90 mmHg นาน 7 วัน** เพื่อรักษา spinal cord perfusion; phenylephrine (pure α1) และ dopamine สัมพันธ์กับ complication rate สูงกว่าจาก reflex bradycardia และ arrhythmia จึงไม่ใช่ first choice; ใช้ atropine สำหรับ symptomatic bradycardia
- **Hemorrhagic / hypovolemic shock** — hemorrhage control และ blood/fluid resuscitation คือการรักษาหลัก vasopressor ไม่ทดแทนการให้เลือด; หลักฐาน observational ชี้ว่า early หรือ high-dose vasopressor สัมพันธ์กับ mortality สูงขึ้น (บางชุดข้อมูลพบ risk เพิ่มราว 2 เท่าใน 12 ชม.แรก) จึงเริ่มต่อเมื่อไม่ตอบสนองต่อ resuscitation และใช้เป็น bridge สู่ hemorrhage control เท่านั้น โดยเลือก norepinephrine เมื่อจำเป็น; ยังเป็นประเด็น controversial เพราะ European trauma guideline แนะนำ NE พยุง MAP ระหว่างคุมเลือด ขณะที่ North American practice มัก discourage; low-dose vasopressin (AVERT-Shock) ลด blood product requirement ได้แต่ยังเป็นหลักฐานจำกัด
- **Anaphylactic shock** — **IM epinephrine เป็น first-line** ฉีดที่ anterolateral thigh ขนาด **0.01 mg/kg (max 0.3 mg ในเด็ก, 0.5 mg ในผู้ใหญ่)** ซ้ำได้ทุก 5–15 นาที; ฤทธิ์ α1 เพิ่ม BP และลด airway edema ส่วน β2 ให้ bronchodilation จึงครอบคลุมทุกกลไกจากยาตัวเดียว; IV epinephrine infusion (1–10 mcg/min หรือ 0.01–0.1 mcg/kg/min) สงวนไว้สำหรับ refractory anaphylaxis หลังได้ IM ครบ ≥2 ครั้ง หรือใน perioperative setting; ให้ IV crystalloid ควบคู่เพราะมี distributive vasodilation ร่วมกับ capillary leak; ผู้ป่วยที่ใช้ beta-blocker และ refractory ให้ glucagon 1–5 mg IV; ไม่มี guideline แนะนำ vasopressor ตัวอื่นเป็น first-line

# ⚠️ Adverse Effects & Practical Cautions

| Problem | ยาที่เกี่ยวข้อง | กลไก / ตัวเลข | การจัดการ |
| --- | --- | --- | --- |
| **Tachyarrhythmia** | catecholamine ทุกตัว, PDE3i | ↑cytosolic Ca²⁺ → triggered activity; milrinone: sustained VT/VF **1–3%**, SVT **~4%** | ลด dose, แก้ K⁺/Mg²⁺, เปลี่ยนไป levosimendan/vasopressin |
| **Extravasation necrosis** | norepinephrine, epinephrine, dopamine, phenylephrine | α1-mediated local vasoconstriction | **Phentolamine 5–10 mg ใน NSS 10 mL** ฉีด infiltrate รอบตำแหน่ง ภายใน 12 ชม.; ประคบอุ่น ห้ามประคบเย็น |
| **Digital / mesenteric ischemia** | vasopressin, high-dose NE | V1/α1 vasoconstriction ที่ end-artery | ตรวจปลายมือปลายเท้าทุกเวร, ไม่ใช้ vasopressin เกิน 0.04 U/min |
| **Dose-dependent hypotension** | milrinone (**2.9%**), levosimendan, dobutamine | vasodilation จาก PDE3/K-ATP | งด loading bolus, ให้คู่ vasopressor |
| **ฤทธิ์คงค้างหลังหยุดยา** | milrinone (renal clearance), levosimendan (OR-1896) | half-life ยาว | ระวังใน CKD; levosimendan เฝ้าระวังต่อ 7–9 วัน |
| **Thrombocytopenia** | milrinone | reversible, **0.4%** | ตรวจ CBC เมื่อใช้ยาว |
| **Tolerance** | dobutamine | β-receptor downregulation, 72 ชม. เหลือ 66% | เพิ่ม dose หรือสลับไป PDE3i |
| **Lactate สูงลวง** | epinephrine | เร่ง aerobic glycolysis | อย่าใช้ lactate เดี่ยวเป็น marker perfusion ระหว่างให้ยา |
| **Thrombotic event** | angiotensin II | **13% vs 5%** vs placebo | ให้ VTE prophylaxis ควบคู่ |

# 📚 Landmark Trials

- **SOAP II (2010)** — dopamine vs norepinephrine ใน shock ทุกชนิด (n=1,679): 28-day mortality โดยรวมไม่ต่างกัน (52.5% vs 48.5%, p=0.10) แต่ arrhythmia สูงกว่าชัดเจนใน dopamine (24.1% vs 12.4%, p<0.001); prespecified subgroup cardiogenic shock พบ mortality สูงกว่าใน dopamine (p=0.03) โดย **interaction test ไม่ significant (p=0.87)** ผล subgroup นี้จึงเป็น hypothesis-generating ส่วนที่แข็งจริงคือข้อมูล arrhythmia
- **OptimaCC (2018)** — epinephrine vs norepinephrine ใน cardiogenic shock หลัง AMI (n=57): cardiac index และ arterial pressure ใกล้เคียงกัน แต่ epinephrine เพิ่ม heart rate, lactate และ refractory shock จน DSMB สั่งหยุดการศึกษาก่อนกำหนด
- **DOREMI (2021)** — milrinone vs dobutamine ใน cardiogenic shock (n=192): primary composite เกิด 49% vs 54% (RR 0.90, 95% CI 0.69–1.19, p=0.47) ไม่ต่างกันทั้ง safety outcome และ surrogate marker; subgroup analysis พบว่า baseline beta-blocker use **ไม่ลดทอนการตอบสนองต่อ dobutamine** ซึ่งขัดกับเหตุผลเชิงทฤษฎีที่มักใช้เลือก milrinone ในผู้ป่วยกลุ่มนี้
- **SURVIVE (2007)** — levosimendan vs dobutamine ใน ADHF: 180-day mortality 26% vs 28% (HR 0.91, 95% CI 0.74–1.13, p=0.40)
- **REVIVE II (2005/2013)** — levosimendan vs placebo: clinical status ที่ 5 วันดีขึ้น (p=0.015) ลดวันนอนเฉลี่ย 1.9 วัน (7.0 vs 8.9) แต่ไม่ลด mortality และเพิ่ม hypotension (50% vs 36%), VT (25% vs 17%), AF (8% vs 2%)
- **LEVO-CTS · CHEETAH · LICORN** — levosimendan รอบ cardiac surgery ให้ผล neutral หรือ inconclusive ทั้ง 3 การศึกษา สวนทางกับ meta-analysis ขนาดเล็กก่อนหน้าที่เคยชี้ว่าได้ประโยชน์
- **OPTIME-CHF (2002)** — milrinone 48 ชม. ใน ADHF (n=951): ไม่มีประโยชน์โดยรวม เพิ่ม sustained hypotension และ atrial arrhythmia; วิเคราะห์ตาม etiology พบผลแย่ลงในกลุ่ม ischemic และ neutral ถึงดีขึ้นในกลุ่ม non-ischemic
- **ANZICS low-dose dopamine (2000)** — dopamine 2 mcg/kg/min vs placebo ในผู้ป่วย SIRS ที่มี early renal dysfunction (n=324): peak creatinine ไม่ต่างกัน (245 vs 249 µmol/L, p=0.8) เป็นหลักฐานที่ปิดแนวคิด renal-dose dopamine
- **ATHOS-3 (2017)** — angiotensin II ใน catecholamine-refractory distributive shock (n=321): บรรลุ MAP response ตาม primary endpoint แต่เพิ่ม thrombotic event (13% vs 5%)
- **ADHERE registry** — inotrope สัมพันธ์กับ in-hospital mortality สูงกว่า vasodilator ในผู้ป่วย ADHF ที่ไม่ได้อยู่ใน shock

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **ห้ามให้ inotrope แบบ routine ในผู้ป่วยที่ cardiac output ต่ำแต่ไม่มี hypoperfusion** เพิ่ม arrhythmia และ mortality (OPTIME-CHF, ADHERE); ข้อบ่งชี้คือ hypoperfusion จริงเท่านั้น
> 

> - **ห้ามให้ inotrope ใน dynamic LVOT obstruction** การเพิ่ม contractility ทำให้ obstruction แย่ลงจนความดันตกซ้ำ; ใช้ phenylephrine ร่วมกับ volume แทน
> 

> - **ห้ามใช้ isoproterenol ใน congenital long QT** ยืด QT ต่อและกระตุ้น arrhythmia (ต่างจาก acquired TdP ที่ใช้ได้)
> 

> - **ห้ามผสม catecholamine กับ sodium bicarbonate ในสายเดียวกัน** ด่างทำให้ยา inactivate
> 

# 🎯 High-Yield Recall

- **Norepinephrine = first-line vasopressor** ทั้ง cardiogenic และ septic shock; หลักฐานที่แข็งที่สุดคือ arrhythmia ต่ำกว่า dopamine (SOAP II) และ refractory shock ต่ำกว่า epinephrine (OptimaCC)
- **Dobutamine vs milrinone ผลลัพธ์เท่ากัน** (DOREMI) เลือกจาก PVR, ไต และความมั่นคงของความดัน
- **"Renal-dose dopamine" ไม่มีอยู่จริง** (ANZICS 2000)
- **Levosimendan** = Ca²⁺ sensitizer, ไม่เพิ่ม O₂ demand, mortality neutral (SURVIVE); OR-1896 ทำให้ฤทธิ์อยู่ต่อ **7–9 วัน**
- **Phenylephrine ใน LVOT obstruction, isoproterenol ใน Brugada storm** เป็น 2 สถานการณ์ที่ยาซึ่งปกติเลี่ยงกลับกลายเป็นตัวเลือกแรก
- **Extravasation → phentolamine 5–10 mg ใน NSS 10 mL ภายใน 12 ชม.**
- **Distributive / hypovolemic scenarios:** neurogenic shock (lesion เหนือ T6) → NE first-line (dual α/β แก้ทั้ง hypotension และ bradycardia); anaphylaxis → **IM epinephrine 0.01 mg/kg** first-line; hemorrhagic shock → เลือด/คุมเลือดก่อน เพราะ early pressor สัมพันธ์ mortality

> 🇹🇭 **Thai availability:** dopamine, dobutamine, norepinephrine, epinephrine, isoproterenol, milrinone มีทั่วไป; **levosimendan** มีในไทย ราคาสูง มักจำกัดที่ รพ.ตติยภูมิ (ยังไม่ได้รับอนุมัติจาก FDA สหรัฐฯ ณ ก.ค. 2026 อยู่ระหว่าง Phase 3 สำหรับ PH-HFpEF); vasopressin และ phenylephrine มีจำกัดบางแห่ง; **angiotensin II (Giapreza) ไม่มีจำหน่ายในไทย**
> 

> 🔍 **Verification status**
> 

> ✅ Searched & verified (29 ก.ค. 2026): SOAP II (รวม interaction p=0.87), OptimaCC, DOREMI + beta-blocker subgroup, SURVIVE, REVIVE II, OPTIME-CHF, LEVO-CTS/CHEETAH/LICORN, ANZICS dopamine, ATHOS-3, ADHERE; milrinone dosing + AE rates; dobutamine tolerance 66%/72h; levosimendan OR-1896 half-life 70–80 h; phenylephrine ใน LVOT obstruction (2017 AHA statement); isoproterenol dosing 3 ข้อบ่งชี้; vasopressin V1 pH-independence; phentolamine dosing; 2021 ESC Class IIb; 2024 ISHLT consensus; levosimendan FDA status; **(31 ก.ค. 2026 digest)** neurogenic shock pressor selection — NE first-line, phenylephrine/dopamine complication signal (2023 StatPearls, 2025 JCM review); early vasopressor ใน hemorrhagic shock สัมพันธ์ mortality (observational, controversial vs European trauma guideline; AVERT-Shock vasopressin); anaphylaxis IM epinephrine 0.01 mg/kg first-line + IV infusion เฉพาะ refractory (2023 AAAAI/ACAAI practice parameter)
> 

> ⚠️ From source extraction ไม่ได้ re-verify รอบนี้: dose range ของ dopamine, norepinephrine, epinephrine (standard textbook values); **mL/hr rates omitted** (dilution-dependent ต้องตาม local protocol)
> 

> 🔴 Corrected รอบนี้: (1) เดิมอ้าง **ROSE-AHF** เป็นหลักฐาน harm ของ routine inotrope ซึ่งผิด ROSE-AHF ทดสอบ low-dose dopamine/nesiritide เสริม diuretic ใน ADHF ที่มี renal dysfunction → แก้เป็น ADHERE registry (2) เดิมเขียนว่า NE ลด mortality กว่า dopamine ซึ่ง overclaim จาก subgroup ที่ interaction ไม่ significant (3) milrinone dose เดิม 0.125–0.75 → มาตรฐานคือ 0.375–0.75 โดย 0.125 สงวนไว้สำหรับ renal impairment (4) vasopressin range เดิม 0.02–0.04 → 0.01–0.04 U/min
>
