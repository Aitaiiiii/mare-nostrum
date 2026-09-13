---
title: "Clinical Epidemiology & Study Design"
aliases: ["Clinical Epidemiology & Study Design"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
type: "Discrete entity"
review_status: "New"
tags: []
created: 2026-06-28
notion_id: 38d224ab-ad81-8135-91e7-cffaabec6a11
source: notion-migration
---

# Clinical Epidemiology & Study Design

> **Source:** บรรยาย PMK Board Review — Clinical Epidemiology and Clinical Practice Guideline | สืบค้น: 28 มิ.ย. 2568 | เพิ่มเติมจาก SNC10 General Cardiology & Stat extraction (Part 3 + Part 6): 28 ก.ค. 2569
> 

> หน้านี้ครอบคลุม **study design, bias/confounding, diagnostic test statistics, magnitude of effect, hypothesis testing, meta-analysis appraisal** — เป็น toolkit สำหรับ**อ่าน/ตีความ clinical trial และ systematic review** ในชีวิตจริง (board exam + journal club)
> 

> 🚨 **STRICT AVOIDANCE / RED FLAGS**
> 

> - **Cohort ≠ Prospective, Case-Control ≠ Retrospective** — สับสนกันบ่อยที่สุด ทำให้อ่าน abstract ผิดว่า design เป็นอะไร
> 

> - **"Failure to prove superiority" ≠ "proven non-inferior"** — สองอย่างนี้คนละโจทย์ทางสถิติคนละแบบ — ห้ามสรุปเองว่ายา non-inferior เพราะ P value ของ superiority ไม่ถึง 0.05
> 

> - **Immortal time bias / verification bias / spectrum bias** เป็น bias ที่ซ่อนมาก โดยเฉพาะใน observational drug studies (เช่น SGLT2i mortality studies) — อ่าน methods section เสมอก่อนเชื่อ effect size
> 

> - **Subgroup analysis ที่ post-hoc/ไม่ significant interaction test** — ห้ามนำมาอ้างเป็น practice-changing evidence โดยไม่ระบุว่าเป็น exploratory/hypothesis-generating
> 

> - **I² thresholds และ Egger's test** ไม่ใช่ rigid cutoff — funnel plot asymmetry ไม่ได้แปลว่าเป็น publication bias เสมอ (small-study effect ก็ทำให้ asymmetric ได้)
> 

## 🧬 Etiology & Molecular Pathophysiology

*(นำไปใช้ section นี้เป็น Fundamentals)* — Clinical epidemiology คือเครื่องมือในการตีความถูกต้องของ evidence โดยใช้หลัก biostatistics + study design เพื่อตอบคำถามทางคลินิก

## 🩺 Clinical Phenotypes & Advanced Nuances

### Study Design

| ประเภท | นิยาม |
| --- | --- |
| **RCT** | Experimental study + มี randomization |
| **Non-RCT** | Experimental study, ไม่มี randomization |
| **Quasi-RCT** | Experimental, randomization ไม่สมบูรณ์ (เช่น แบ่งตามวันเกิด/HN คู่-คี่) |
| **Cohort** | Observational, เริ่มจาก **Exposure → Outcome** |
| **Case-Control** | Observational, เริ่มจาก **Outcome → Exposure** (ใช้สำหรับ rare disease) |
| **Cross-sectional** | ดู Exposure + Outcome พร้อมกันในเวลาเดียว |
| **Descriptive** | ไม่มีกลุ่ม control (single group observation) |

**ข้อผิดพลาดที่บ่อย**: Cohort ≠ Prospective, Case-Control ≠ Retrospective — คำว่า prospective/retrospective หมายถึงทิศทางการเก็บข้อมูล ไม่ใช่ study design

**2×2 Factorial Design**: เมื่อต้องการตอบ 2 คำถามในการทดลองเดียว — แบ่งกลุ่ม 4 แบบ (เช่น chlorhexidine vs povidone × scrub vs no-scrub)

> **Flow แยก design (จาก lecture):** มี assigned exposure? → ไม่มี = **observational** → มี comparison group? ไม่มี = **descriptive** (เช่น heat wave, outbreak report, single-arm Zika follow-up — ถึงพาเปอร์จะเขียน “prospective cohort” ก็ถือเป็น descriptive ถ้าไม่มี control); มี comparison = **analytic** → ดูทิศทาง exposure↔outcome
> 

**Allocation concealment:** หลัง randomize แล้ว ถ้าผู้วิจัยรู้ว่าคนไข้จะได้ A หรือ B → เกิด selection bias → ต้องซ่อนกลุ่มใน **sealed opaque envelope** (ต่างจาก blinding ที่ปิดระหว่าง intervention)

## 🩻 Advanced Diagnostics & Formal Criteria

### 2×2 Table — Measures of Association

|  | Disease (+) | Disease (−) |
| --- | --- | --- |
| **Exposed** | a | b |
| **Not exposed** | c | d |
| ตัวชี้วัด | สูตร | ใช้ใน |
| --------- | ------ | -------- |
| **Relative Risk (RR)** | [a/(a+b)] ÷ [c/(c+d)] | Cohort study |
| **Odds Ratio (OR)** | (a×d) ÷ (b×c) | Case-Control study |
| **Attributable Risk** | [a/(a+b)] − [c/(c+d)] | Cohort, ผลต่างของ risk |

**Incidence** = อุบัติการณ์ (new cases/population at risk/time) • **Prevalence** = ความชุก (all cases/population)

### Diagnostic Test Statistics

| ตัวชี้วัด | ความหมาย | สูตร |
| --- | --- | --- |
| **Sensitivity (Sens)** | ใน True disease → test (+) กี่% | a/(a+c) |
| **Specificity (Spec)** | ใน No disease → test (−) กี่% | d/(b+d) |
| **PPV** | ถ้า test (+) → มีโรคจริงกี่% | a/(a+b) |
| **NPV** | ถ้า test (−) → ไม่มีโรคจริงกี่% | d/(c+d) |
| **Accuracy** | test ถูกทั้งหมด | (a+d)/N |

**สำคัญ**: PPV และ NPV เปลี่ยนตาม **Prevalence** — Sens/Spec คงที— ที่ Prevalence ต่ำ PPV จะต่ำมากแม้ Sens/Spec สูง

**Trick: เขียน 2x2 table**: สมมติ N = 1,000 → คำนวณจำนวน disease จาก prevalence → fill a, b, c, d จาก Sens/Spec

### SPIN / SNOUT Rule

- **SPIN**: **SP**ecificity high + Positive → **rule IN** (Confirm disease)
- **SNOUT**: **SN**sensitivity high + Negative → **rule OUT** (Exclude disease)

*ตัวอย่าง*: Urine dipstick proteinuria (Sens 95%) — Negative → rule out proteinuria | PSA ที่ Spec 95%, cut-off 5 ng/mL → Positive → rule in prostate cancer

### Likelihood Ratio

- **+LR** = Sens ÷ (1 − Spec) — ถ้า test (+) ขลายโอกาสเป็นโรคกี่เท่า
- **−LR** = (1 − Sens) ÷ Spec — ถ้า test (−) ความน่าจะเป็นโรคลดลงกี่เท่า

### ROC Curve (AUC)

- แกน x = 1−Spec, แกน y = Sens — จุดที่ดีที่สุด: Sens + Spec สูงสุด (มุมซ้ายบน)
- AUC = 0.5 (ไม่มีคุณค่า) → 0.7 (acceptable) → 0.9+ (excellent)
- การเลือก cut-off ขึ้นกับวัตถุประสงค์: screening → เน้น Sens; confirmatory → เน้น Spec

## 💊 Management & Pharmacodynamics

### Biostatistics — การเลือกสถิติ

| ข้อมูล | Distribution | 2 กลุ่ม | มากกว่า  2 กลุ่ม |
| --- | --- | --- | --- |
| Continuous (BP, Hb) | Normal | **Unpaired t-test** | **ANOVA** |
| Continuous | Non-normal | Mann-Whitney U | Kruskal-Wallis |
| Categorical (proportion) | — | **Chi-square** | Chi-square |
| Paired data (before-after) | Normal | **Paired t-test** | Repeated ANOVA |

### Non-inferiority Trial

- เป้าหมาย: แสดงว่ายาใหม่ **ไม่แย่กว่ายาเดิม** เกินกว่า non-inferiority margin
- Non-inferior margin: ขีดนี้ CI กระทบ margin → non-inferior NOT shown
- ถ้า CI อยู่เหนือ 0 ด้วย → non-inferior AND superior

### Error Types

| ประเภท | ความหมาย | กำหนดไว้ที่ |
| --- | --- | --- |
| **Type I Error (α)** | False Positive — ยาไม่ได้ผล แต่บอกว่าได้ผล (อันตรายที่สุด) | < 5% (0.05) |
| **Type II Error (β)** | False Negative — ยาได้ผล แต่บอกว่าไม่ได้ผล (ยอมรับได้มากกว่า) | < 20% |
| **Power (1−β)** | โอกาสหาผลว่ายาได้ผลจริง | ≥ 80% |

### Confidence Interval — สิ่งที่เครื่องไม่ควรคร่อม

- Continuous data (Mean difference): **CI ไม่คร่อม 0** → significant
- Ratio data (RR, OR, HR): **CI ไม่คร่อม 1** → significant

### Number Needed to Treat / Harm

$NNT = \frac{1}{ARR} = \frac{1}{\text{Control rate} - \text{Treatment rate}}$

$NNH = \frac{1}{ARI} = \frac{1}{\text{Harm rate (new)} - \text{Harm rate (control)}}$

**สำคัญ**: ถ้า rate เป็น % → ต้องหารด้วย  100 ก่อน | ปัดขึ้นเสมอเพราะนับเป็นคน

**Relative Risk Reduction (RRR)** = [Control rate − Treatment rate] ÷ Control rate — ดูเสมอนเป็นตัวเลขเยอะเกินจริง — ใช้ ARR ในการตัดสินใจดีกว่า

### Forest Plot / Meta-analysis

- Square size ∝ N (ใหญ่ → weight มาก)
- Whiskers = 95% CI (N น้อย → CI กว้าง)
- Diamond = pooled estimate — ถ้าไม่คร่อม 1 (RR) → significant
- **Publication bias**: small studies ที่ได้ผลบวกได้รับตีพิมพ์มากกว่า negative studies — ดูด้วย **Funnel plot**

### Clinical Practice Guideline (CPG) — หลักการสร้างที่ดี

1. ใช้ **Systematic Review** (ไม่ใช้แค่ expert opinion)
2. สร้างโดย **multidisciplinary team** (รวม patient และ third party)
3. **Grade evidence** + **Grade recommendation** (GRADE system)
4. ทำ **External Review** ก่อนตีพิมพ์
5. **Update** อย่างสม่ำเสมอ
6. **Declare COI** — ต้อง transparent
7. เครื่องมือประเมินคุณภาพ: **AGREE statement**

## 📚 Landmark Trials & Literature

| เครื่องมือ | ความหมาย |
| --- | --- |
| **CONSORT** | มาตรฐานการรายงาน RCT |
| **STROBE** | มาตรฐานการรายงาน Observational study |
| **PRISMA** | มาตรฐานการรายงาน Systematic review / Meta-analysis |
| **AGREE** | ประเมินคุณภาพ CPG |

---

🖼️ **Visual Reference**

- [AGREE II Tool](https://www.agreetrust.org/resource-centre/agree-ii/)
- [Cochrane Handbook for Systematic Reviews](https://training.cochrane.org/handbook)

---

# 🧩 Additional Study Designs (Supplementary)

- **Nested case-control** — ทำภายใน cohort ที่มีอยู่แล้ว: ติดตามจนเกิดโรค แล้วย้อนกลับไปดู exposure, เลือก control จาก cohort เดียวกัน — ข้อดีคือลด **recall bias** เทียบกับ case-control ทั่วไป (exposure มักถูกเก็บไว้ล่วงหน้าแล้ว)
- **Historical control** — เปรียบเทียบกับข้อมูลอดีต มีข้อจำกัด 2 แบบ: **time-period effect** (การรักษา/แนวทางเปลี่ยนไปตามเวลา ทำให้ prognosis เปลี่ยน) และ **cohort effect** (ลักษณะผู้ป่วยกลุ่มเก่า-ใหม่ต่างกัน)
- **Cross-over trial (randomized)** — ผู้ป่วยได้รับทั้ง 2 treatment สลับกัน ต้องมี **washout period** เพียงพอเพื่อป้องกัน **carry-over effect** (ผลของยาตัวแรกตกค้างมาปนกับตัวหลัง)
- **Quasi-experimental design** — ไม่ randomize เนื่องจากข้อจำกัดทางจริยธรรม/logistics (เช่น เปรียบเทียบเทคนิคผ่าตัด 2 แบบ) — เสี่ยง **selection bias และ confounding สูง**
- **PROBE (Prospective Randomized Open-label Blinded Endpoint)** (✅ verified) — randomize แบบเปิดเผย (ผู้ป่วย/แพทย์รู้ว่าได้ยาอะไร) แต่ **endpoint ถูกตัดสินโดยคณะกรรมการที่ blind ต่อ treatment allocation** — ต้องการ endpoint ที่ชัดเจน/hard เพื่อลดผลกระทบจากการไม่ blind; ข้อดี: ต้นทุนต่ำ ใกล้เคียง real-world practice
- **PCT (Pragmatic Clinical Trial)** — ใช้ real-world data + propensity score matching เป้าหมายเพื่อ **ปรับปรุงเวชปฏิบัติ** ไม่ใช่พิสูจน์ cause-effect

**RCT vs PCT — เปรียบเทียบ:**

|  | RCT | PCT |
| --- | --- | --- |
| เป้าหมาย | หา cause/effect | ปรับปรุง practice/policy |
| Design | Placebo, protocol เข้มงวด | Real-world treatment, protocol ยืดหยุ่น |
| ผู้เข้าร่วม | คัดเลือกเข้มงวด | เป็นตัวแทนประชากรจริงมากกว่า |
| การวัดผล | นอกเหนือ routine care | เก็บง่ายในเวชปฏิบัติ |
| ผลลัพธ์ | มักไม่ตรงกับเวชปฏิบัติจริง | นำไปใช้ตัดสินใจได้จริง |

---

# 🧠 Causality, Confounding & Bias

**Nocebo effect vs placebo effect** — nocebo คือผลเสียจากความคาดหวังทางลบ (ตรงข้ามกับ placebo) ตัวอย่างคลาสสิก: **ORBITA trial** — PCI ใน stable angina ไม่ลด symptom เมื่อเทียบกับ sham-PCI (blinded) มากกว่าที่คาดจากการศึกษาแบบไม่ blind ก่อนหน้า

**Association (correlation)** — บวก/ลบ, อาจไม่ใช่ของจริง (artifactual — เกิดจาก chance, uncontrolled factors, bias, hypothesis ผิด)

**Association tree**: Statistical association → **Causal** (direct/indirect) หรือ **Non-causal** (secondary/confounded) → หรือ **Non-statistical** (by chance)

**Bradford Hill Criteria for Causality** (✅ verified — 9 criteria ดั้งเดิม, Hill 1965): **Strength** (ความแรงของ association) · **Consistency** (พบซ้ำในหลายการศึกษา/ประชากร) · **Specificity** · **Temporality** (exposure ต้องมาก่อน outcome เสมอ — เป็นเกณฑ์เดียวที่ *จำเป็น*) · **Biological gradient** (dose-response) · **Plausibility** (มี mechanism ที่สมเหตุสมผล) · **Coherence** (สอดคล้องกับความรู้ที่มีอยู่) · **Experiment** (การทดลอง/removal ของ exposure ลด disease) · **Analogy** — ตัวอย่างจาก source (LDL-atherosclerosis): plausible mechanism, strong graded relationship, risk factor precedes disease, independent of other factors, consistent across studies, coherent, supported by genetics (Mendelian randomization), risk-factor reduction → ลด disease risk

**Confounder — คุณสมบัติที่ต้องมีครบ:** (1) เป็น prognostic factor ของ outcome (2) กระจายไม่เท่ากันระหว่างกลุ่ม (3) **ต้องไม่อยู่ในทางเดินเชิงสาเหตุ (causal pathway) ระหว่าง exposure-outcome** — confounding by indication เป็นรูปแบบที่พบบ่อยในการศึกษาที่ไม่ randomize (ผู้ป่วยที่ป่วยหนักกว่ามักได้รับยา/หัตถการมากกว่า ทำให้ดูเหมือนยานั้นสัมพันธ์กับ outcome แย่กว่า)

- **Confounder ≠ Effect modifier**: confounder ต้องไม่ถูกกระทบโดย exposure เอง ส่วน effect modifier คือปัจจัยที่ผล (effect) ของ exposure แตกต่างกันตามระดับของมัน (ไม่ใช่ bias ต้อง report แยก ไม่ใช่ adjust ทิ้ง)
- **การกำจัดผล confounder**: ขั้น design — randomization, matching, restriction; ขั้น analysis — stratified analysis (**Mantel-Haenszel**), multiple regression (linear/logistic/Poisson/Cox), **propensity score**, **instrumental variable analysis**

**Bias ในการศึกษาวินิจฉัย (Diagnostic test bias)** (✅ verified):

- **Verification bias (work-up bias)** — ผล test เบื้องต้นมีผลต่อการตัดสินใจส่ง gold-standard test ยืนยัน (มักเกิดเมื่อผลลบ — ไม่ค่อยส่งตรวจต่อเพราะ invasive/แพง) → ทำให้ **sensitivity ลดลง, specificity เพิ่มขึ้น**
- **Spectrum bias** — ความรุนแรงของโรคต่างกันระหว่างกลุ่มที่ทดสอบ (เช่น case-control design มักทำให้ทั้ง sensitivity และ specificity สูงเกินจริงเทียบกับ real-world spectrum ของผู้ป่วย)
- **Immortal time bias** (✅ verified — ตัวอย่าง SGLT2i): ช่วงเวลาที่ผู้ป่วย "รอด" ก่อนได้ยา ถูกนับเป็นเวลาที่ได้ยา (แต่ในความจริงจะตายก่อนได้ยาไม่ได้) ทำให้กลุ่มที่ได้ยาดูเหมือน mortality ต่ำกว่าจริง — พบใน SGLT2i observational mortality studies ที่ immortal time (ช่วงตั้งแต่เริ่มยาลดน้ำตาลตัวแรกจนถึง SGLT2i) ถูกตัดออกจากกลุ่มเปรียบเทียบ ทำให้ mortality กลุ่มควบคุมดูสูงเกินจริง — แก้ไขด้วย **time-dependent Cox regression** (SGLT2i เป็น time-varying exposure)
- **Misclassified vs excluded immortal time**: misclassified = จัดกลุ่ม person-time ผิด (misclassification bias); excluded = ตัด person-time ออกทั้งหมด (selection bias) — ทั้งคู่ทำให้ overestimate ผลของยา

---

# 📊 Diagnostic Test Statistics — Post-Test Probability & Agreement

**Likelihood ratio ดีกว่า sens/spec เดี่ยวๆ** เพราะรองรับผล multi-level ได้ (ไม่ใช่แค่ positive/negative)

**การคำนวณ post-test probability**: pretest odds = Pr/(1−Pr); post-test odds = pretest odds × LR; post-test probability = odds/(1+odds)

> ตัวอย่าง: pretest probability 20% → pretest odds = 0.25; ถ้า LR+ = 6.0 → post-test odds = 1.5 → post-test probability = 60%
> 

**Agreement analysis** (✅ verified):

| ประเภทข้อมูล | เครื่องมือ |
| --- | --- |
| Categorical (2 หมวด) | **Cohen's Kappa**, McNemar's test |
| Numerical (paired) | Paired t-test, **Bland-Altman plot**, **Intraclass Correlation Coefficient (ICC)** |
| Association เชิงเส้น (parametric) | **Pearson correlation** (−1 ถึง +1) |
- **Cohen's Kappa** วัด agreement ระหว่างผู้ประเมิน 2 คนสำหรับข้อมูล nominal โดยหักลบ chance agreement ออกแล้ว (ในการทำ systematic review เกณฑ์ **kappa ≥0.7 ระหว่างผู้ทำ study selection ถือว่ายอมรับได้**)
- **Bland-Altman** ใช้ประเมิน agreement ของการวัดต่อเนื่อง (ไม่ใช้ correlation coefficient เพราะ correlation วัดความสัมพันธ์ ไม่ใช่ความสอดคล้อง/interchangeability) — พล็อต mean of differences ± limits of agreement
- **ICC** ใช้ประเมิน intra-/inter-rater reliability สำหรับข้อมูลต่อเนื่อง

---

# ⏳ Survival Analysis

- ใช้กับ **binary outcome เท่านั้น** (event เกิดหรือไม่เกิด) ที่มีมิติเวลาเข้ามาเกี่ยวข้อง (time-to-event)
- **Kaplan-Meier curve** (✅ verified) — non-parametric estimate ของ survival probability ตามเวลา กราฟจะ "ตก" เป็นขั้นบันไดทุกครั้งที่มี event เกิดขึ้น
- **Log-rank test** (✅ verified) — ใช้เปรียบเทียบ Kaplan-Meier curve ระหว่าง ≥2 กลุ่มว่าต่างกันอย่างมีนัยสำคัญหรือไม่ (เทียบเท่า Mantel-Haenszel สำหรับ survival data)
- **Sensitivity analysis สำหรับ loss-to-follow-up**: ทดสอบ worst-case scenario (สมมติผู้ที่ขาดหายไปทั้งหมดมี event หรือไม่มี event) เพื่อดูว่าผลสรุปยังคงเดิมหรือไม่

---

# 🔬 Subgroup Analysis — หลักการอ่าน/ทำอย่างเข้มงวด

- **Null hypothesis ของ subgroup analysis** = ไม่มีความแตกต่างของ treatment effect ระหว่าง subgroup
- **P for interaction**: เกณฑ์ที่ใช้มักหลวมกว่าปกติเพราะ interaction test มี power ต่ำ — ใช้ **P<0.10 แทน 0.05** เป็น threshold ของนัยสำคัญ (P<0.10 บ่งชี้ความเป็นไปได้ที่จะมี subgroup difference จริง ต้องศึกษาต่อ)
- **Bonferroni correction สำหรับ multiple subgroups** (✅ verified concept): ปรับ significance threshold เป็น **α/จำนวน pre-specified subgroups** (เช่น 3 subgroups → 0.05/3 ≈ 0.017)
- Subgroup ต้อง**significant ในการวิเคราะห์หลัก (overall) ก่อน** จึงจะพิจารณา subgroup ต่อได้
- **แนวทางที่ดีสำหรับ subgroup analysis**: (1) ตั้งสมมติฐานล่วงหน้า (pre-specified) (2) จำกัดเฉพาะ subgroup ที่มี biological plausibility (3) จำกัดเฉพาะเมื่อ overall treatment effect มีนัยสำคัญ (4) ต้องมี significant treatment×subgroup interaction test (5) ปรับสำหรับ multiple comparisons (6) รายงานเป็น exploratory เท่านั้น (7) หลีกเลี่ยงการ over-interpret

---

# 📐 Magnitude of Treatment Effect (เพิ่มเติม)

- **Relative Risk Reduction (RRR)** = [a/(a+b) − c/(c+d)] / [c/(c+d)] — **ดูตัวเลขใหญ่เกินจริงเสมอ** เทียบกับ ARR จึงควรใช้ ARR/NNT ประกอบการตัดสินใจทางคลินิก
- **Odds Ratio vs Relative Risk**: OR อยู่ห่างจาก 1 มากกว่า RR เสมอในชุดข้อมูลเดียวกัน (ไม่ว่า OR จะมากกว่าหรือน้อยกว่า 1); **OR ≈ RR เมื่อโรคพบน้อย** (a<<c และ b<<d, "rare disease assumption")
- **Hazard Ratio (HR)** — ประมาณ risk/odds เฉลี่ยตลอดช่วงเวลา ผ่าน Cox regression: ความน่าจะเป็นที่ผู้ป่วยคนหนึ่ง ณ เวลา t จะเกิด event ที่เวลานั้น (event-free survival) — ข้อจำกัด: ขึ้นกับ number-at-risk, **วัดเฉพาะ event แรกเท่านั้น** (ไม่ใช่ recurrent event); **relative hazard reduction = 1 − HR**

---

# 🧮 Meta-Analysis Appraisal — Fixed vs Random Effects & Heterogeneity

**Fixed-effect model**: สมมติว่ามี **single true effect** เดียว ไม่มี heterogeneity ระหว่างการศึกษา — ใช้ได้เมื่อ study เหมือนกันในเชิงหน้าที่ (functionally identical)

**Random-effect model**: ยอมรับ **between-study variation** — true effect ต่างกันในแต่ละการศึกษา ให้ผลที่ realistic/conservative กว่า

|  | Fixed | Random |
| --- | --- | --- |
| การศึกษาที่รวม | ชุดที่มีอยู่ทั้งหมด | สุ่มตัวอย่างจากประชากรทฤษฎี |
| True effect | ค่าเดียว | ต่างกันในแต่ละการศึกษา |
| Variance | Within-study | Within + between-study |
| ความหมายของ pooled estimate | True effect เดียว | ค่าเฉลี่ยของ true effect ที่ต่างกัน |
| CI | อาจแคบกว่า | อาจกว้างกว่า |
| ความไวต่อ publication bias | ต่ำกว่า | สูงกว่า |

**การอ่าน meta-analysis**:

- **Search/selection strategy**: ความครบถ้วนของ database, language restriction, unpublished data (grey literature), GIGO (garbage in garbage out)
- **Publication/reporting bias types**: publication bias, time-lag bias, multiple/duplicate publication bias, location bias, citation bias, language bias, outcome-reporting bias
- **Study selection kappa** ระหว่างผู้ทบทวน: ยอมรับที่ **≥0.7**
- **Egger's test** (✅ verified) — linear regression test หา funnel plot asymmetry, แนะนำเมื่อมี ≥10 studies ขึ้นไป; **ไม่ significant ≠ ไม่มี publication bias แน่นอน** เป็นเพียงหลักฐานสนับสนุน ไม่ใช่ definitive proof — funnel asymmetry อาจเกิดจาก **small-study effect** (การศึกษาเล็กมักได้ effect size สูงกว่าจริง) ไม่ใช่แค่ publication bias เท่านั้น
- **Heterogeneity**:
    - **Cochran's Q test** — ขึ้นกับจำนวน study (power ต่ำเมื่อ study น้อย) จึงใช้ **P<0.10 แทน 0.05** เป็น threshold ของนัยสำคัญ
    - **I² index** (✅ verified — Cochrane Handbook) — ไม่ขึ้นกับจำนวน study: แนวทางทั่วไป **0–40% = อาจไม่สำคัญ, 30–60% = moderate, 50–90% = substantial, 75–100% = considerable** (ตัวเลขช่วงคาบเกี่ยวกันโดยตั้งใจ — ⚠️ Cochrane เตือนว่า**ไม่ควรใช้เป็น rigid cutoff** ต้องพิจารณาบริบทประกอบ ทิศทาง/ขนาดผล และ Q-test p-value ร่วมด้วย) — **random-effect model เหมาะกับ heterogeneity สูง, fixed-effect เหมาะเมื่อ heterogeneity ต่ำ**
    - **การจัดการ heterogeneity**: ทบทวนลักษณะการศึกษาใหม่, พิจารณาไม่รวมผล (ทำเป็น systematic review อย่างเดียว), ตัดการศึกษาที่ risk of bias สูงออก, ทำ pre-specified subgrouping, ใช้ individual patient data (IPD) analysis, ใช้ random-effect model, ทำ meta-regression (เช่น ตามปีตีพิมพ์/ระยะเวลาติดตาม), ใช้ robust statistics (sensitivity analysis เทียบทั้ง fixed และ random ว่าผลไปทางเดียวกันหรือไม่)

---

# ⚖️ Non-Inferiority Trials — เพิ่มเติม

- **Failure to prove superiority ≠ non-inferiority claim** — ต้องออกแบบ non-inferiority trial ตั้งแต่ต้น (pre-specified margin) จะสรุปย้อนหลังจาก negative superiority trial ไม่ได้
- Treatment ใหม่**ด้อยกว่าได้เล็กน้อย แต่ขนาดต้องไม่มีนัยสำคัญทางคลินิก** (อยู่ภายใน pre-specified non-inferiority margin)
- **P สำหรับ non-inferiority เป็น one-tailed test ที่ <0.025** (✅ verified — เทียบเท่า two-sided 95% CI ปกติ) — ให้ critical value เดียวกับ two-sided alpha 0.05 ของ superiority trial
- **≥50% ของ minimal clinically important treatment effect (เทียบกับ active control vs placebo ในอดีต) ต้องคงอยู่** (constancy assumption)
- **การวิเคราะห์**: non-inferiority ต้องดูทั้ง **ITT และ per-protocol** (ทั้งคู่ต้องสอดคล้องกันจึงเชื่อมั่นได้ — เพราะ ITT อาจ anti-conservative ใน NI trial ต่างจาก superiority trial ที่ ITT อนุรักษ์นิยมกว่า); superiority trial ใช้ **ITT เท่านั้น** เป็นหลัก
- **FDA cardiovascular outcome cut-points สำหรับยาเบาหวานใหม่** (✅ verified — FDA 2008 guidance): upper bound ของ 95% CI ของ HR/RR สำหรับ MACE — **<1.8 = ยอมรับได้สำหรับ pre-approval; <1.3 = ต้องแสดงให้ได้หลัง approval (มิฉะนั้นต้องทำ post-approval CV outcome trial เพิ่ม); ≥1.8 = ไม่ผ่านเกณฑ์ FDA approval; point estimate <1.0 = superior**
- **Truncated RCT (หยุดก่อนกำหนดเพื่อ benefit)** — ถือว่า valid เมื่อ: มี pre-specified formal stopping rule ตั้งแต่ต้น, จำนวนครั้งของ interim analysis น้อย + ใช้ P ที่เข้มงวดมาก (<0.001), มีจำนวน event สะสมมากเพียงพอก่อนหยุด (≥200-300 events), และผลไม่ "ดีเกินจริงจนน่าสงสัย" (not too good to be true)

---

# 🎯 High-Yield Recall

- **Design ผิดบ่อย**: Cohort/Case-control ไม่ผูกกับ prospective/retrospective; PROBE = open-label + blinded endpoint committee; PCT ≠ RCT (real-world vs cause-effect)
- **Hill's Criteria**: Temporality เป็นเกณฑ์เดียวที่ *จำเป็น* (necessary) ส่วนที่เหลือเป็น supportive
- **Confounder ต้องไม่อยู่ใน causal pathway** — ถ้าอยู่ใน pathway คือ mediator ไม่ใช่ confounder
- **Bias สำคัญ**: verification bias (↓sens ↑spec), immortal time bias (SGLT2i mortality studies — แก้ด้วย time-dependent Cox)
- **Post-test probability**: pretest odds × LR = post-test odds → เปลี่ยนกลับเป็น probability
- **Agreement**: categorical→Kappa/McNemar; continuous→Bland-Altman/ICC (ไม่ใช้ Pearson correlation วัด agreement)
- **Survival**: Kaplan-Meier + log-rank test; วัดเฉพาะ binary time-to-event outcome
- **Subgroup**: null=ไม่ต่างกัน; P interaction <0.10 (ไม่ใช่ 0.05); Bonferroni = 0.05/n subgroups; ต้อง significant overall ก่อน
- **Non-inferiority**: P one-tailed <0.025; ต้องดูทั้ง ITT+PP; FDA DM CV outcome: <1.8 pre-approval / <1.3 post-approval / ≥1.8 ไม่ผ่าน
- **Meta-analysis**: Fixed=single true effect; Random=between-study variation (conservative กว่า); I² thresholds เป็น guide ไม่ใช่ rigid cutoff; Egger's test ไม่ significant ไม่ตัด publication bias ทิ้งเสมอไป
- **HR** วัด first event เท่านั้น; **OR ห่างจาก 1 มากกว่า RR เสมอ**, OR≈RR เมื่อโรคหายาก
- 🔍 Verification status
    
    **✅ Searched & verified (28 ก.ค. 2026)**
    
    - Bradford Hill's 9 criteria for causality (Strength, Consistency, Specificity, Temporality, Biological gradient, Plausibility, Coherence, Experiment, Analogy) — Wikipedia (Bradford Hill criteria), StatsDirect, UMC
    - PROBE design (open-label randomization + independent blinded endpoint committee) — original Hansson/Hedner 1992 PubMed citation, Blood Pressure journal
    - Immortal time bias in SGLT2i observational mortality studies (survivor treatment selection bias, time-dependent Cox regression as correction) — PubMed (Suissa 2018 "Real or Bias?"), arXiv statistical methods review
    - Verification (work-up) bias ↓sensitivity/↑specificity + spectrum bias (case-control design inflates both) — Catalog of Bias, Wikipedia (Verification bias)
    - Egger's test (regression test for funnel plot asymmetry, recommended ≥10 studies, intercept ≠0 = asymmetry, NOT definitive proof of publication bias — small-study effects confound interpretation) — AJE, [numberanalytics.com](http://numberanalytics.com), bookdown Doing Meta-Analysis in R
    - Cochrane I² categorization (0-40% not important, 30-60% moderate, 50-90% substantial, 75-100% considerable; NOT rigid cutoffs) — Cochrane Handbook 5.1 §9.5.2
    - Non-inferiority one-tailed α<0.025 (equivalent to two-sided 95% CI) — FDA Non-Inferiority Trial guidance ([fda.gov/media/78504](http://fda.gov/media/78504)), PMC methodology reviews
    - FDA 2008 CV outcome trial guidance for diabetes drugs (upper 95% CI bound <1.8 pre-approval, <1.3 post-approval definitive) — AHA Circulation reviews, Diabetes Care Editors' Forum
    - Kaplan-Meier curve + log-rank test (non-parametric survival estimate; compares ≥2 KM curves) — MedCalc, standard biostatistics references
    - Agreement analysis: Cohen's Kappa (categorical), Bland-Altman (continuous, NOT correlation), ICC (continuous reliability) — Clinical Biostatistics bookdown, ResearchGate methodology reviews
    
    **⚠️ From standard biostatistics knowledge, not individually re-verified this session**
    
    - Nested case-control, historical control (time-period/cohort effect), cross-over washout/carry-over — standard epidemiology methods teaching
    - Subgroup P-for-interaction <0.10 threshold + Bonferroni α/n concept — standard teaching, consistent with general subgroup-analysis methodology literature (exact 0.10 figure not individually re-verified this session)
    - ORBITA trial (sham-PCI, nocebo/placebo framing) — well-known trial, not re-verified in detail this session
    - Truncated RCT stopping-rule criteria (≥200-300 events, P<0.001 interim) — standard clinical trial methodology teaching, not individually re-verified
