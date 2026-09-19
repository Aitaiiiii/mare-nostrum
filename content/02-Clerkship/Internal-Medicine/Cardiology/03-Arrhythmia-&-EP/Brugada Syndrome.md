---
title: "Brugada Syndrome"
aliases: ["Brugada Syndrome"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Cardiology"
subspecialty: "Arrhythmia & EP"
type: "Disease"
guidelines: ["ESC"]
review_status: "New"
tags: []
created: 2026-07-21
notion_id: 3a4224ab-ad81-8129-b61c-e6eafd27548e
source: notion-migration
updated: 2026-09-14
---

# Brugada Syndrome

# ⚡ Brugada Syndrome (BrS)

> **Retrofit เป็น fellowship-depth monograph (Shape A) เมื่อ 12 ส.ค. 2026** ขยายจาก digest เดิม (26 ก.ค. 2026) พร้อม live search ทั้งหน้า
> 

> 
> 

> 🔴 **แก้ claim ที่ผิดจากเวอร์ชันเดิม** เดิมเขียนว่า type 1 ECG เพียงอย่างเดียวไม่พอวินิจฉัยตาม 2022 ESC ข้อเท็จจริงคือ **spontaneous type 1 เพียงอย่างเดียววินิจฉัยได้** ส่วนที่ต้องมี clinical factor ร่วมคือ **induced type 1** (drug หรือ fever) รายละเอียดใน section 3
> 

> 
> 

> **Companion pages:** [[SCD (Sudden Cardiac Death)]] · [[Device Indications (PPM, ICD, CRT)]] · [[Early Repolarization Syndrome]] · [[Short QT Syndrome]] · [[ECG & EP Eponyms]]
> 

## 1. 🧬 Etiology & Molecular Pathophysiology

**Brugada syndrome (BrS)** เป็น inherited arrhythmia syndrome ที่ทำให้เกิด polymorphic VT และ VF ในหัวใจที่ไม่มี structural heart disease ชัดเจน โดยมีบริเวณที่เป็นต้นตอคือ **right ventricular outflow tract (RVOT) epicardium** ระดับ ion current กลไกรวมคือ **inward current (I_Na, I_Ca) ลดลงเทียบกับ outward current (I_to) ที่มากเกิน** ในช่วงต้นของ action potential

### Repolarization vs depolarization hypothesis

สองสมมติฐานนี้ยังแข่งกันอธิบายโรค และการเลือกเชื่อข้างใดมีผลต่อการตีความว่า ablation ควรทำที่ไหน

|  | **Repolarization hypothesis** | **Depolarization hypothesis** |
| --- | --- | --- |
| กลไก | I_to ที่หนาแน่นใน RVOT epicardium ร่วมกับ I_Na ที่ลดลง ทำให้ phase 1 ลึกและ action potential dome หายไปเฉพาะ epicardium เกิด **transmural voltage gradient** กับ endocardium | conduction delay และ activation ที่ล่าช้าใน RVOT ทำให้ activation gradient ระหว่าง RVOT กับ RV ที่เหลือ |
| ต้นเหตุ ST elevation | dispersion of repolarization | delayed activation ของ RVOT |
| กลไกจุดชนวน VF | **phase 2 reentry** จากบริเวณที่ dome หายไปไปยังบริเวณที่ยังมี | reentry รอบบริเวณ slow conduction |
| หลักฐานสนับสนุน | สัตว์ทดลอง wedge preparation, ผลของ I_to blocker (quinidine) ที่ทำให้ ECG กลับปกติ | **late fractionated electrogram** ที่ RVOT epicardium ในผู้ป่วยจริง และการ ablate บริเวณนั้นทำให้ type 1 หายไปพร้อมลด VF |

กรอบที่ประนีประนอมสองฝ่ายคือ **reduced RVOT conduction reserve** โดยถือว่าปลายทางร่วมของทุกกลไกคือ RVOT ที่ conduction สำรองน้อยผิดปกติ ซึ่งอธิบายได้ทั้งกรณีที่ substrate เป็น functional ล้วนและกรณีที่พบ **subepicardial fibrosis** กับ connexin-43 ที่ลดลงจากชิ้นเนื้อ ผู้ป่วยจำนวนหนึ่งจึงมี structural component ที่ตรวจไม่พบด้วย echo ทั่วไป

### Modulators ที่เปลี่ยน phenotype แบบวันต่อวัน

- **Fever** ทำให้ Nav1.5 ที่มี mutation inactivate เร็วขึ้นตามอุณหภูมิ เกิด type 1 และ VF ขณะไข้ได้ในคนที่ ECG ปกติมาก่อน
- **Vagal tone สูง / bradycardia** ช่วง sleep และหลังมื้ออาหารใหญ่ ลด I_Ca และยืด diastole จึงเพิ่ม transmural dispersion อธิบายว่าเหตุการณ์กระจุกตัวช่วงกลางคืน
- **Testosterone** เป็นคำอธิบายหลักของ male predominance เพราะเพิ่ม I_to และลด I_Ca
- **Hypokalemia** และ Na-channel blocker ทุกชนิด รวม cocaine กับ alcohol ปริมาณมาก ทำหน้าที่เป็น unmasker ทางเภสัชวิทยา

### Genetics

- **SCN5A** เป็นยีนเดียวที่มีหลักฐานระดับ definitive สำหรับ BrS ยีนอื่นที่เคยรายงาน (SCN1B, KCNE3, CACNA1C ฯลฯ) ส่วนใหญ่ถูกลดระดับหลักฐานลงในการ curate ยุคหลัง
- Diagnostic yield ของ SCN5A rare coding variant อยู่ราว **20% ในเชื้อสายยุโรป** แต่เพียงราว **5% ในผู้ป่วยไทย** ความชุกที่สูงกว่าในเอเชียตะวันออกเฉียงใต้จึงอธิบายด้วย ultrarare SCN5A variant ไม่ได้
- **โมเดล oligogenic/polygenic** GWAS ชี้ตำแหน่ง **SCN5A-SCN10A** และ **HEY2** เป็น common variant ที่รวมกันเป็น polygenic risk ทำให้ penetrance ในครอบครัวเดียวกันต่างกันมาก
- ปัจจัยจำเพาะประชากรไทยสองตัวที่ยืนยันแล้ว
    1. **SCN5A p.Arg965Cys** low-frequency coding variant พบราว **6.5% ของผู้ป่วย BrS ไทย**
    2. **RE5 noncoding enhancer variant** ใน SCN5A intron พบ **3.9% ของผู้ป่วย** case-control **OR 45.2** ทำลาย Mef2 binding site และลด Nav1.5 sodium current density ลง **30%** ใน hiPSC-CM โดยผู้ที่มี variant นี้ phenotype รุนแรง มี cardiac arrest ถึง **89%**
- Genetic testing SCN5A ใน proband เป็น **Class I ตาม 2022 ESC** ประโยชน์หลักคือ cascade screening ในครอบครัว ผลลบไม่ตัดโรคทิ้ง และผลบวกเพียงลำพังไม่วินิจฉัยโรค (Shanghai score ให้เพียง 0.5 คะแนน)

### Epidemiology

- ความชุกโดยประมาณในไทยและเอเชียตะวันออกเฉียงใต้ราว **1 ใน 1,000** เทียบกับราว **1 ใน 2,000** ในภูมิภาคอื่น
- **M:F ประมาณ 8:1** อายุที่มาแสดงอาการเฉลี่ยราว 40 ปี
- BrS คือคำอธิบายหลักของ **sudden unexplained nocturnal death syndrome (SUNDS)** ที่คนไทยเรียก **โรคใหลตาย (Lai Tai)** อัตราตายจาก SUDS ในชายอีสาน อายุ 20–49 ปี อยู่ที่ **25.9 ต่อ 100,000 person-years** และพบ family history ของ SUDS ใน **40.3%** ของ index case
- การเสียชีวิตมี seasonality ชัดเจน โดยราว **38% เกิดช่วงมีนาคมถึงพฤษภาคม**

## 2. 🩺 Clinical Phenotypes & Advanced Nuances

ผู้ป่วยสองในสามไม่มีอาการเมื่อวินิจฉัย รูปแบบการมาพบแพทย์กำหนดความเสี่ยงมากกว่าตัว ECG เพียงลำพัง จึงต้องแยก phenotype ให้ชัดก่อนตัดสินใจเรื่อง ICD

| Phenotype | ลักษณะเด่น | นัยทางคลินิก |
| --- | --- | --- |
| **Aborted cardiac arrest** | VF ขณะหลับหรือพัก มัก resuscitate ได้เพราะมีคนพบ | เสี่ยงสูงสุด event rate **7.7%/ปี** ICD เป็น Class I |
| **Arrhythmic syncope** | หมดสติแบบไม่มี prodrome ท่านอน หรือมี **nocturnal agonal respiration** ที่ญาติเล่าว่าหายใจครืดคราดตอนกลางคืน | ต้องแยกจาก vasovagal ให้ได้ เพราะ syncope ที่ไม่ใช่ arrhythmic ไม่เพิ่มความเสี่ยง |
| **Spontaneous type 1 ที่ไม่มีอาการ** | เจอจากการตรวจสุขภาพหรือ cascade screening | event rate **0.81–1.18%/ปี** อยู่ในโซนที่ตัดสินใจยากที่สุด |
| **Drug/fever-induced type 1 ที่ไม่มีอาการ** | ECG ปกติที่ baseline | event rate **0.21–0.30%/ปี** ใกล้ประชากรทั่วไป |
| **BrS/ER overlap** | type 1 ใน V1–V2 ร่วมกับ augmented J wave ใน inferior lead | ตอบสนองต่อ ablation แย่กว่า ใน BRAVE 3 ใน 5 รายที่ยังมี VF หลัง ablate เป็นกลุ่มนี้ |
| **SCN5A-positive with conduction disease** | PR และ QRS ยาวขึ้น มี fragmented QRS | substrate มักกว้างกว่า สัมพันธ์กับ VF recurrence (HR 2.22 ใน cohort ablation) |
| **Pediatric BrS** | phenotype โผล่ตอนไข้เป็นหลัก | ไข้เป็น trigger ที่พบมากกว่าผู้ใหญ่ชัดเจน การคุมไข้จึงเป็นแกนการดูแล |

**Atrial involvement** ไม่ใช่เรื่องบังเอิญ ผู้ป่วย BrS มี AF และ atrial flutter มากกว่าประชากรทั่วไป เพราะ Na-channel dysfunction กระทบ atrium ด้วย ประเด็นสำคัญคือการรักษา AF ในคนกลุ่มนี้ถูกจำกัดทันที เนื่องจาก class IC และ class IA บางตัวเป็นยาที่ห้ามใช้ และ AF ที่นำมาสู่ ICD ที่ตั้ง detection ต่ำจะกลายเป็น inappropriate shock

**Brugada phenocopy ที่ต้อง exclude ก่อนติดป้ายว่าเป็นโรค** กลุ่มนี้ให้ ECG หน้าตาเหมือนกันแต่ต้นเหตุต่างและรักษาต่างกันหมด

- **RVOT ischemia** โดยเฉพาะ occlusion ของ conus branch หรือ proximal LAD
- **ARVC** ที่มี RVOT abnormality และ epsilon wave
- **Acute pulmonary embolism**, mediastinal mass หรือ pectus excavatum ที่กด RVOT
- **Hyperkalemia**, hypothermia, hypercalcemia
- **Drug toxicity** จาก TCA, cocaine, Na-channel blocker overdose
- ช่วงหลัง cardiac arrest หรือ post-cardioversion ที่ ECG ยังไม่คงที่

## 3. 🩻 Advanced Diagnostics & Formal Criteria

### Type 1 pattern

- **Type 1 (coved) เท่านั้นที่ diagnostic** เกณฑ์คือ J-point/ST elevation **≥2 mm** รูป coved ลงต่อเนื่องเข้าสู่ negative T wave ใน **≥1 lead ของ V1–V2** โดยอ่านได้ทั้งตำแหน่งมาตรฐานและ **high position ที่ 2nd–3rd intercostal space**
- **Type 2 (saddleback)** ไม่ diagnostic ใช้เป็นตัวคัดคนที่ควรทำ provocation test มี morphologic criteria (β angle, base of triangle) ที่ช่วยทำนายผล challenge แต่ค่าตัดยังต่างกันตามการศึกษา
- ECG มี **dynamic variation** สูง การได้ ECG ปกติครั้งเดียวไม่ตัดโรคทิ้ง เครื่องมือที่ช่วยจับ spontaneous type 1 คือ 12-lead ambulatory monitoring, การทำ ECG ซ้ำขณะไข้ และ ECG ช่วง early recovery หลัง exercise ซึ่งเป็นช่วง vagal rebound

### 2022 ESC diagnostic & workup recommendations

- **Spontaneous type 1 pattern** ในผู้ที่ไม่มีโรคหัวใจอื่น วินิจฉัย BrS ได้เลย
- **Induced type 1** จาก sodium channel blocker หรือ fever ต้องมีอย่างน้อยหนึ่งข้อร่วม จึง**ควรพิจารณา**วินิจฉัย (**Class IIa**)
    - arrhythmic syncope หรือ nocturnal agonal respiration
    - family history ของ BrS
    - family history ของ sudden death อายุ **น้อยกว่า 45 ปี** ที่ autopsy negative และสถานการณ์ชวนสงสัย BrS
- **Induced type 1 ที่ไม่มีข้อร่วมเลย** อาจพิจารณาวินิจฉัย (**Class IIb**) กลุ่มนี้ปฏิบัติจริงมักเรียกว่า **Brugada ECG pattern** แล้วติดตามแทนการติดป้ายโรค
- **Genetic testing SCN5A ใน proband** (**Class I**)
- **Implantable loop recorder** ในผู้ป่วย BrS ที่มี unexplained syncope (**Class IIa**)
- **PES** อาจพิจารณาใน asymptomatic ที่มี spontaneous type 1 (**Class IIb**)
- **Sodium channel blocker test ไม่แนะนำ**ในผู้ที่เคยมี type 1 pattern มาก่อน

### Sodium channel blocker provocation test

- **Ajmaline 1 mg/kg IV (max 100 mg) ใน 5 นาที** sensitivity สูงสุดในกลุ่มยาทั้งหมด ข้อจำกัดคือเข้าถึงยากในหลายประเทศรวมทั้งไทย
- **Flecainide 2 mg/kg IV (max 150 mg) ใน 10 นาที** ทางเลือกที่ใช้แพร่หลายในยุโรป
- **Procainamide 10 mg/kg IV** ใน 10 นาที ตามโปรโตคอลเดิม บางศูนย์ยืดเป็น 20–30 นาที เป็น agent หลักในอเมริกาเหนือ และให้ผลบวกน้อยกว่า ajmaline อย่างมีนัย
- **Oral flecainide 200–400 mg** ใช้เป็นทางเลือกเมื่อไม่มี IV agent โดยต้อง monitor ต่อเนื่อง
- **หยุด infusion ทันที**เมื่อเกิด type 1 pattern, QRS ยาวขึ้นถึง **≥130% ของ baseline**, มี PVC หรือ ventricular arrhythmia, หรือมี side effect ชัดเจน
- ทำในที่ที่มีอุปกรณ์ resuscitation และ isoproterenol พร้อมใช้ **false positive rate รายงานไว้ที่ 4–27%** จึงห้ามตีความผลบวกแยกจากบริบททางคลินิก

### Shanghai score

ใช้เมื่อภาพรวมไม่ชัด โดยเลือกคะแนนสูงสุดได้เพียงหนึ่งข้อในแต่ละหมวด

| หมวด | องค์ประกอบ | คะแนน |
| --- | --- | --- |
| **ECG** | spontaneous type 1 (standard หรือ high lead) | 3.5 |
|  | fever-induced type 1 | 3 |
|  | type 2/3 ที่เปลี่ยนเป็น type 1 หลัง sodium channel blocker | 2 |
| **Clinical history** | unexplained cardiac arrest หรือ documented VF/PMVT | 3 |
|  | nocturnal agonal respiration | 2 |
|  | suspected arrhythmic syncope | 2 |
|  | syncope กลไกไม่ชัด | 1 |
|  | AF/atrial flutter อายุน้อยกว่า 30 ปี โดยไม่มีสาเหตุอื่น | 0.5 |
| **Family history** | first/second-degree relative ที่เป็น definite BrS | 2 |
|  | SCD ที่ชวนสงสัยในญาติ (ขณะไข้ กลางคืน หรือได้ยาที่กระตุ้น) | 1 |
|  | unexplained SCD อายุน้อยกว่า 45 ปี ในญาติที่ autopsy negative | 0.5 |
| **Genetic** | probable pathogenic variant ในยีนที่สัมพันธ์กับ BrS | 0.5 |

การแปลผล **≥3.5 = probable/definite BrS** · **2–3 = possible BrS** · **น้อยกว่า 2 = non-diagnostic** ในการ validate ที่ญี่ปุ่นพบว่าอัตรา lethal arrhythmic event ต่อ 10 ปีไล่ขึ้นตามคะแนนจาก **0%** ในกลุ่มคะแนนต่ำสุด ไปถึง **32.5%** ในกลุ่ม ≥5.5 คะแนน ข้อจำกัดที่ต้องรู้คือ score นี้ออกแบบมาเพื่อ**วินิจฉัย** ไม่ได้ออกแบบมาเป็น prognostic tool การนำมาใช้ทำนายเหตุการณ์จึงเป็นการยืมเครื่องมือ

## 4. 💊 Risk Stratification & Management

### Annual arrhythmic event rate

ตัวเลขชุดนี้เป็นฐานของการตัดสินใจทั้งหมด เพราะต้องเทียบกับ complication rate ของ ICD ที่ผู้ป่วยจะแบกตลอดชีวิต

| กลุ่ม | Event rate ต่อปี |
| --- | --- |
| **Aborted SCD** | **7.7%** |
| **Syncope + spontaneous type 1** | **2.3–3.7%** |
| **Syncope (รวมทุกแบบ)** | **1.9%** |
| **Syncope + drug-induced type 1** | **1.0–2.0%** |
| **Asymptomatic + spontaneous type 1** | **0.8–1.2%** |
| **Asymptomatic (รวมทุกแบบ)** | **0.5%** |
| **Asymptomatic + drug-induced type 1** | **0.2–0.3%** |

ฝั่งความเสี่ยงของอุปกรณ์ meta-analysis ผู้ป่วย BrS ที่ใส่ ICD 1,539 ราย พบ **inappropriate shock 3.3% ต่อปี** และ complication อื่น เช่น lead malfunction กับ device infection อีก **4.5% ต่อปี** ในผู้ป่วยอายุน้อยที่จะอยู่กับอุปกรณ์อีกหลายสิบปี ตัวเลขสองชุดนี้จึงชนกันเต็มที่ในกลุ่ม asymptomatic

### ECG และ clinical modifier

- **Fragmented QRS** เป็น marker ที่ข้อมูลสม่ำเสมอที่สุดในกลุ่ม noninvasive
- **aVR sign**, significant S wave ใน lead I, early repolarization ใน peripheral lead, QTc ยาว และ AF สัมพันธ์กับ event ใน cohort หลายชุด
- **Substrate size** จาก electroanatomical mapping ทำนาย VF recurrence (HR 1.13 ต่อหน่วยพื้นที่) ร่วมกับ aborted cardiac arrest (HR 2.98) และ SCN5A variant (HR 2.22)
- **Family history ของ SCD เพียงอย่างเดียวไม่ใช่ predictor ที่ดี** ทั้งใน FINGER registry และ cohort หลังจากนั้น ข้อนี้ขัดกับสัญชาตญาณและเป็นจุดที่มักตัดสินใจเกินจำเป็น

### Risk score และข้อจำกัด

- **Sieira score** ทำงานดีที่สุดในการเปรียบเทียบแบบ head-to-head (AUC ราว 0.80 ใน multi-centre cohort, pooled AUC 0.71) รองมาคือ **Shanghai score** (AUC 0.63–0.71) และ **BRUGADA-RISK**
- ทั้งสาม score ให้ discrimination ระดับปานกลางใกล้เคียงกัน (AUC ราว 0.75) โดยมี **PPV ต่ำมากราว 3%** แต่ **NPV สูงถึง 99.8%** ประโยชน์จริงจึงอยู่ที่การยืนยันว่าใครความเสี่ยงต่ำ ไม่ใช่การชี้ว่าใครควรได้ ICD
- ในกลุ่ม intermediate risk ซึ่งเป็นกลุ่มที่ต้องการเครื่องมือมากที่สุด cohort ขนาดใหญ่ที่สุดสรุปว่า score เหล่านี้แยกความเสี่ยงไม่ได้ ทางปฏิบัติจึงยังต้องอาศัยประสบการณ์และการตัดสินใจร่วมกับผู้ป่วย
- **PES/programmed stimulation** ยังถกเถียง PRELUDE registry ไม่พบว่า inducibility ทำนาย event ปัจจุบันเหลือสถานะ Class IIb เฉพาะ asymptomatic ที่มี spontaneous type 1

### Lifestyle & preventive measures (แกนหลักในทุกราย)

- **ลดไข้เชิงรุกทันที** ด้วย antipyretic และให้ผู้ป่วยถือคำสั่งนี้ติดตัว รวมถึงมาตรวจ ECG เมื่อมีไข้สูง
- **หลีกเลี่ยงยาตามรายการใน [brugadadrugs.org](http://brugadadrugs.org)** กลุ่มที่ห้ามชัดเจนคือ class IA และ IC antiarrhythmic (flecainide, propafenone, procainamide), TCA, lithium, cocaine, และ propofol ในบางบริบท
- คุม **hypokalemia** เลี่ยง alcohol ปริมาณมากและมื้ออาหารหนักก่อนนอน
- **Cascade screening ในครอบครัว** ด้วย ECG ± genetic testing และสอน CPR กับการเข้าถึง AED
- แนะนำหลีกเลี่ยงยาที่ใช้บ่อยในไทยโดยไม่รู้ว่าเป็นกลุ่มเสี่ยง เช่น ยาแก้แพ้และ antiemetic บางตัว ให้ตรวจรายการทุกครั้งก่อนสั่งยาใหม่

### ICD

- **Aborted cardiac arrest หรือ documented sustained VT** เป็น **Class I**
- **Spontaneous type 1 ร่วมกับ arrhythmic syncope** เป็น **Class IIa**
- **Asymptomatic** ไม่มีข้อบ่งชี้ ICD ให้ติดตามและใช้ ILR เมื่อมี unexplained syncope
- ตั้ง detection zone สูงและใช้ long detection interval เพื่อลด inappropriate shock จาก AF และ sinus tachycardia

### Quinidine

กลไกคือ block **I_to** ซึ่งกู้ action potential dome ที่ epicardium กลับมา ทำให้ transmural dispersion ลดลงและ ECG กลับเข้าใกล้ปกติ ผลนี้เกิดแม้ quinidine เป็น Na-channel blocker ในตัวเอง

- **ขนาดสูงเดิม ≥1 g/วัน** (mean 1,483 mg ในการศึกษาต้นแบบ) ป้องกัน VF re-induction ได้ **88%** แต่มี side effect **36%** ส่วนใหญ่เป็น diarrhea และ hepatotoxicity ทำให้หยุดยาถึงราวหนึ่งในสาม
- **ขนาดต่ำ ≤600 mg/วัน** มีประสิทธิผลราว **85%** และ tolerability ดีกว่าชัดเจน จึงเป็นแนวที่นิยมในปัจจุบัน
- **Hydroquinidine 300 mg BID** เพิ่มได้ถึง 900 mg/วันเมื่อยัง inducible เป้าหมาย plasma level ที่อ้างถึงคือ 1–3 µg/mL
- ข้อบ่งชี้: electrical storm, recurrent appropriate ICD shock, ผู้ที่มีข้อบ่งชี้ ICD แต่ใส่ไม่ได้หรือปฏิเสธ และ AF ที่ต้องรักษา

### Electrical storm

- **Isoproterenol IV** เป็นยาแรก โดยเพิ่ม L-type Ca current และเพิ่ม heart rate จนลด dispersion regimen ที่รายงานคือ bolus **1–2 µg** แล้ว infusion **0.15–2 µg/min** ปรับตามการตอบสนอง หรือคิดตามน้ำหนักที่ **0.003–0.02 µg/kg/min**
- **Oral quinidine** เริ่มควบคู่เพื่อเป็นสะพานออกจาก infusion เพราะ VF มัก recur เมื่อหยุด isoproterenol โดยไม่มียา oral รับช่วง
- **Amiodarone และ beta-blocker ไม่ได้ผล**ในบริบทนี้ และ class III agent อาจเพิ่ม ST elevation

### Catheter ablation

Substrate อยู่ที่ RVOT epicardium ในรูปของ late fractionated electrogram การ ablate บริเวณนั้นทำให้ type 1 pattern หายไปพร้อมลด VF ซึ่งเป็นหลักฐานเชิงกลไกที่หนุน depolarization hypothesis

- Single-arm meta-analysis 13 cohort ผู้ป่วย 555 ราย พบ **type 1 resolution 91%** และ elimination ของ abnormal electrogram **91%** โดยยังมี **recurrent VT/VF 12%** และ appropriate ICD therapy **8%** หลัง ablation
- **BRAVE (2025)** เป็น RCT แรก ผู้ป่วย symptomatic BrS ที่มี ICD 50–52 ราย สุ่มเป็น ablation เทียบ control พบ VF ใน **5 ราย (20%)** ในกลุ่ม ablation เทียบ **13 ราย (52%)** ในกลุ่ม control (**HR 0.288, 95%CI 0.102–0.811, p=0.018**) เข้าเกณฑ์หยุดการศึกษาที่ interim analysis ในกลุ่มที่ ablate ทั้งหมด **83% ไม่มี VF หลังทำครั้งเดียว** และ **90% หลังทำซ้ำ** complication คือ hemopericardium 1 ราย
- **Pappone RCT (Europace 2025)** เป็น RCT ที่สองในทิศเดียวกัน โดยกลุ่ม control ยังได้ quinidine ต่อ ต่างจาก BRAVE ที่กลุ่ม control ไม่ได้ยา
- **จุดที่ต้องระวังเวลาอ่าน guideline** 2022 ESC ยังให้ ablation เป็น **Class IIb** สำหรับ recurrent shock และ**ไม่แนะนำ**ใน asymptomatic ซึ่งเป็นคำแนะนำที่ออกก่อน RCT ทั้งสองฉบับ ทางปฏิบัติในศูนย์ที่ทำได้จึงเดินหน้ากว่าตัวหนังสือ แต่ยังไม่มีหลักฐานว่า ablation แทน ICD ได้ ทุกการศึกษาทำในผู้ป่วยที่มี ICD อยู่แล้ว

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> 
> 

> - **ไข้เป็น trigger ที่ป้องกันได้ง่ายที่สุดและถูกมองข้ามบ่อยที่สุด** ต้องลดไข้เชิงรุกและตรวจ ECG ซ้ำขณะไข้ โดยเฉพาะในเด็กที่ phenotype โผล่ตอนไข้เป็นหลัก
> 

> - **ห้ามให้ class IA/IC antiarrhythmic, TCA, cocaine หรือ alcohol ปริมาณมาก** ทุกตัวคือ unmasker ที่ทำให้เกิด type 1 และ VF ตรวจรายการใน [brugadadrugs.org](http://brugadadrugs.org) ก่อนสั่งยาใหม่ทุกครั้ง
> 

> - **ห้ามทำ sodium channel blocker challenge ในผู้ที่เคยมี type 1 pattern แล้ว** ไม่ได้ข้อมูลเพิ่มและเสี่ยง VF โดยตรง (2022 ESC ระบุว่าไม่แนะนำ)
> 

> - **Amiodarone และ beta-blocker ไม่ใช่การรักษา electrical storm ของ BrS** การให้ตามความเคยชินทำให้เสียเวลาและอาจแย่ลง ทางที่ถูกคือ isoproterenol แล้วต่อด้วย oral quinidine
> 

> 🇹🇭 **Thai availability**
> 

> - **Ajmaline ไม่มีในไทย** provocation test จึงใช้ flecainide หรือ procainamide เป็นหลัก โดยยอมรับว่า sensitivity ต่ำกว่า
> 

> - **Quinidine เข้าถึงยาก** เป็นปัญหาระดับโลกจากการที่ผู้ผลิตหลายรายเลิกผลิต และเป็นเหตุผลที่ BRAVE ถูกออกแบบมาเพื่อบริบทที่ quinidine ไม่มีหรือทนไม่ได้ ต้องเช็คกับเภสัชกรรมของแต่ละสถาบันก่อนวางแผนใช้จริง
> 

> - **Isoproterenol** มีในไทย ใช้ได้ตาม regimen ข้างต้น
> 

> - **Ablation** ทำได้ในไทย โดยศูนย์ไทยเป็นผู้ร่วมผลิตหลักฐานระดับ RCT ในหัวข้อนี้ (BRAVE ดำเนินการโดยทีมไทยร่วมหลายศูนย์)
> 

## 5. 📚 Landmark Trials & Literature

- **FINGER Brugada Syndrome Registry (Circulation 2010)** ผู้ป่วย 1,029 ราย เป็นฐานของ event rate ที่ยังใช้อ้างถึงปัจจุบัน 7.7% / 1.9% / 0.5% ต่อปี และแสดงว่า family history กับ inducibility ไม่ทำนาย event
- **PRELUDE registry** inducibility จาก programmed stimulation ไม่ทำนาย arrhythmic event เป็นเหตุที่ PES ถูกลดบทบาทลงเหลือ Class IIb
- **Belhassen quinidine series** quinidine ขนาดสูงป้องกัน VF re-induction 88% พร้อม side effect 36% เป็นฐานของบทบาท I_to blocker ในโรคนี้
- **Shanghai score validation (Kawada, JACC Clin EP 2018)** ผู้ป่วย 393 ราย event rate ต่อ 10 ปี ไล่จาก 0% ถึง 32.5% ตามกลุ่มคะแนน
- **Probst intermediate-risk cohort** score ที่มีอยู่แยกความเสี่ยงในกลุ่ม intermediate ไม่ได้ ยืนยันว่าช่องว่างเชิงเครื่องมือยังเปิดอยู่
- **BRAVO registry (Circulation 2023)** long-term outcome ของ substrate ablation ในหลายศูนย์ เป็นฐานก่อนเข้าสู่ยุค RCT
- **BRAVE (Heart Rhythm 2025;22:1975–1983)** RCT แรกของ epicardial substrate ablation HR 0.288 (95%CI 0.102–0.811) หยุดการศึกษาที่ interim analysis
- **Pappone RCT (Europace 2025)** RCT ที่สองในทิศเดียวกัน โดยกลุ่ม control ได้ quinidine ต่อ
- **Epicardial ablation meta-analysis (Heart Rhythm 2025)** 555 ราย type 1 resolution 91% recurrent VT/VF 12%
- **RE5 enhancer variant (Circulation 2025;151(1))** noncoding enhancer variant ใน SCN5A พบ 3.9% ของผู้ป่วยไทย OR 45.2 ลด sodium current 30% ใน hiPSC-CM ผู้มี variant มี cardiac arrest 89%
- **2022 ESC Guidelines on Ventricular Arrhythmias & SCD** กรอบการวินิจฉัยและการจัดการที่ใช้อ้างอิงในหน้านี้ทั้งหมด

## 🎯 High-Yield Recall

- **Dx**: spontaneous type 1 (coved ≥2 mm, V1–V2 standard หรือ high lead) วินิจฉัยได้เลย · induced type 1 ต้องมี clinical factor ร่วม (arrhythmic syncope, FHx BrS, FHx SCD น้อยกว่า 45 ปี autopsy negative) จึงเป็น IIa
- **Mechanism**: I_Na ลด / I_to เกิน ที่ RVOT epicardium → phase 2 reentry ปลายทางร่วมคือ reduced RVOT conduction reserve; SCN5A เป็นยีน definitive เดียว yield ไทยราว 5% เทียบยุโรป 20%
- **Thai context**: ความชุกราว 1:1,000 · โรคใหลตาย SUDS 25.9/100,000 person-years ในชายอีสาน 20–49 ปี · p.Arg965Cys 6.5% + RE5 enhancer variant 3.9% (OR 45.2)
- **Risk**: aborted SCA **7.7%/ปี** · syncope+spontaneous **2.3–3.7%** · asymptomatic+spontaneous **0.8–1.2%** · asymptomatic+drug-induced **0.2–0.3%**; ICD แลกมาด้วย inappropriate shock 3.3%/ปี + complication อื่น 4.5%/ปี
- **Rx**: ลดไข้ + เลี่ยงยาตาม [brugadadrugs.org](http://brugadadrugs.org) ทุกราย · ICD Class I เมื่อ aborted SCA/sustained VT, IIa เมื่อ spontaneous type 1 + arrhythmic syncope · storm ใช้ isoproterenol แล้วต่อ oral quinidine ≤600 mg/วัน
- **Ablation 2025**: BRAVE HR 0.288 (p=0.018) และ Pappone RCT หนุน epicardial substrate ablation ในผู้ที่มี ICD แล้ว ขณะที่ 2022 ESC ยังเป็น Class IIb ซึ่งเป็นช่องว่างที่ guideline ยังไม่ตามหลักฐาน
- 🔍 Verification status
    
    **✅ Searched & verified (12 ส.ค. 2026, full retrofit)**
    
    - **2022 ESC BrS recommendations** spontaneous type 1 = diagnosis; induced type 1 + ≥1 clinical factor = IIa; induced type 1 alone = IIb; SCN5A genetic testing Class I; ILR IIa; PES IIb; sodium channel blocker test not recommended เมื่อเคยมี type 1 — ✅ (guideline text, Eur Heart J 2022;43:3997–4126)
    - 🔴 **แก้ claim ที่ผิด** เวอร์ชันเดิมเขียนว่า type 1 เพียงอย่างเดียวไม่พอวินิจฉัย ซึ่งสลับเงื่อนไขระหว่าง spontaneous กับ induced → แก้แล้ว
    - **Shanghai score ทุกองค์ประกอบและคะแนน** รวม cutoff ≥3.5 / 2–3 / น้อยกว่า 2 และ event rate ต่อ 10 ปี 0% → 32.5% ตามกลุ่ม — ✅ (J Wave Syndrome Consensus 2016; Kawada validation JACC Clin EP 2018)
    - **Event rate**: FINGER 7.7% / 1.9% / 0.5% ต่อปี; refined strata 0.21–0.3% / 0.81–1.18% / 0.98–1.96% / 2.3–3.66% — ✅
    - **ICD complication**: inappropriate shock 3.3%/ปี, complication อื่น 4.5%/ปี จาก meta-analysis 1,539 ราย — ✅
    - **Provocation doses**: ajmaline 1 mg/kg (max 100 mg) ใน 5 นาที; flecainide 2 mg/kg (max 150 mg) ใน 10 นาที; procainamide 10 mg/kg ใน 10 นาที (บางโปรโตคอล 20–30 นาที); oral flecainide 200–400 mg; stop เมื่อ QRS ≥130% baseline; false positive 4–27% — ✅
    - **Quinidine**: ขนาดสูง mean 1,483 mg ป้องกัน re-induction 88% side effect 36%; ≤600 mg/วัน efficacy ราว 85%; hydroquinidine 300 mg BID ถึง 900 mg/วัน; target plasma 1–3 µg/mL — ✅
    - **Isoproterenol**: bolus 1–2 µg แล้ว 0.15–2 µg/min หรือ 0.003–0.02 µg/kg/min — ✅ ([brugadadrugs.org](http://brugadadrugs.org) emergencies page + case series)
    - **Ablation**: meta-analysis 13 cohort/555 ราย type 1 resolution 91%, abnormal EGM elimination 91%, recurrent VT/VF 12%, appropriate ICD therapy 8% — ✅ (Heart Rhythm 2025)
    - **BRAVE**: VF 5/25 (20%) ablation เทียบ 13/25 (52%) control, HR 0.288 (95%CI 0.102–0.811), p=0.0184, stopping criterion HR น้อยกว่า 0.342, 83% VF-free หลัง 1 procedure และ 90% หลังทำซ้ำ, hemopericardium 1 ราย — ✅ (Heart Rhythm 2025;22:1975–1983)
    - **Thai genetics**: SCN5A yield ไทยราว 5% เทียบยุโรป 20%; p.Arg965Cys ราว 6.5% ของ case; RE5 enhancer variant 3.9%, OR 45.2, ลด I_Na 30% ใน hiPSC-CM, cardiac arrest 89% — ✅ (Circulation 2025;151(1))
    - **Thai epidemiology**: SUDS 25.9/100,000 person-years ในชายอีสาน 20–49 ปี, FHx 40.3%, seasonality 38% มี.ค.–พ.ค.; ความชุกไทยราว 1:1,000 เทียบ 1:2,000 — ✅ (Thai autopsy/epidemiology series + Chula press material)
    - **Risk score performance**: Sieira AUC ราว 0.80 (multi-centre) / pooled 0.71, Shanghai 0.63–0.71, ทั้งสาม AUC ราว 0.75 PPV 3% NPV 99.8%; score แยกความเสี่ยงในกลุ่ม intermediate ไม่ได้ — ✅
    - **Substrate/genotype HR**: substrate size HR 1.13, aborted cardiac arrest HR 2.98, SCN5A HR 2.22 — ✅ (Europace ablation cohort)
    
    **⚠️ From source/textbook, not re-verified in this pass**
    
    - M:F ประมาณ 8:1 และอายุเฉลี่ยที่มาแสดงอาการราว 40 ปี
    - กลไก repolarization vs depolarization hypothesis, phase 2 reentry, บทบาท testosterone และ vagal tone (standard teaching)
    - รายการ phenocopy และรายการยาที่ห้ามใช้ (อ้าง [brugadadrugs.org](http://brugadadrugs.org) เป็น source ปฏิบัติ)
    
    **🔴 Flagged uncertain**
    
    - **Type 2 morphologic criteria (β angle, base of triangle)** ตั้งใจไม่ระบุตัวเลขในหน้านี้ เพราะยังไม่ verify ค่าตัดในรอบนี้และค่าต่างกันตามการศึกษา
    - **Quinidine availability ในไทย** ยืนยันได้เพียงว่าเป็นปัญหาการเข้าถึงระดับโลกและเป็นเหตุผลออกแบบ BRAVE ไม่พบเอกสารสถานะทะเบียนยาในไทยที่ระบุชัด → ต้องเช็คกับเภสัชกรรมของสถาบัน
    - **Ajmaline ไม่มีในไทย** เป็นข้อมูลจาก digest เดิมร่วมกับรายงานว่าการเข้าถึง ajmaline จำกัดในหลายประเทศ ไม่พบเอกสารทะเบียนยาไทยที่ยืนยันตรง
    - **Pappone RCT (Europace 2025)** ยืนยันการมีอยู่และ design (control ได้ quinidine ต่อ) แต่ไม่ได้ดึงตัวเลข primary endpoint มาในรอบนี้ จึงไม่ระบุตัวเลข
