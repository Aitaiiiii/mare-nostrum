---
title: "Sepsis (Sepsis-3)"
aliases: ["Sepsis (Sepsis-3)"]
stage: Clerkship
rotation: "Internal Medicine"
specialty: "Critical Care"
type: "Disease"
guidelines: ["SSC/SCCM"]
review_status: "New"
tags: [emergency]
created: 2026-07-14
notion_id: 39d224ab-ad81-8123-b28b-e6433357042f
source: notion-migration
---

# Sepsis (Sepsis-3)

> 🔗 **Order set เต็ม (actionable, หน้างาน — dose/route/freq ครบ):** [Sepsis Standing Order](https://app.notion.com/p/Sepsis-321224abad8180d29ff5d96277b9e26e?pvs=21)
> 

## 1. 🧬 Etiology & Molecular Pathophysiology

ภาวะ **sepsis** ตามนิยาม **Sepsis-3** คือภาวะที่ร่างกายตอบสนองต่อการติดเชื้ออย่างผิดปกติจนเกิด **life-threatening organ dysfunction** ความเสียหายต่ออวัยวะมาจาก **dysregulated host response** ของตัวผู้ป่วยเอง เมื่อ **PAMPs** จากเชื้อและ **DAMPs** จากเนื้อเยื่อไปกระตุ้น **Toll-like receptors** ร่างกายจึงหลั่ง **pro-inflammatory cytokines** (**TNF-α**, **IL-1**, **IL-6**) ออกมามากจนเกิด **cytokine storm**

พายุไซโตไคน์นี้ทำให้ **endothelium** ทั่วร่างกายเสียหน้าที่ นำไปสู่ **capillary leak** และ vasodilation จาก **iNOS** ที่ผลิต **NO** มากเกิน จนเกิด **vasoplegia** ร่วมกับการกระตุ้น coagulation ผ่าน **tissue factor** จนเกิด **DIC** ผลรวมคือ **tissue hypoperfusion** และ **cellular hypoxia** ที่วัดออกมาเป็น **lactate** ที่สูงขึ้น

## 2. 🩺 Clinical Phenotypes & Advanced Nuances

อาการแสดงหลากหลายตาม source และอวัยวะที่ล้มเหลวก่อน ผู้ป่วยอาจมาด้วยไข้หรือตัวเย็น (**hypothermia** — สัญญาณที่แย่กว่า) สับสน ซึม หายใจเร็ว ความดันตก — จุดที่ต้องระวังคือ **ผู้สูงอายุ/immunocompromised อาจไม่มีไข้** มาด้วยแค่อาการซึมลง ทำให้วินิจฉัยช้า

การแยก phenotype ที่สำคัญที่สุดคือระบุว่าเข้าสู่ **septic shock** แล้วหรือยัง:

| ระดับ | นิยาม | Mortality โดยประมาณ |
| --- | --- | --- |
| **Sepsis** | infection + organ dysfunction (**SOFA ↑ ≥2**) | ~10% |
| **Septic shock** | sepsis + ต้องใช้ **vasopressor** คง **MAP ≥65**  • **lactate >2** ทั้งที่ให้ fluid พอ | ~40% |

## 3. 🩻 Advanced Diagnostics & Formal Criteria

- **SOFA score** — ประเมิน organ dysfunction 6 ระบบ; เพิ่ม **≥2 คะแนน** จาก baseline = sepsis
- **qSOFA** — bedside screen: **RR ≥22**, **altered mentation (GCS <15)**, **SBP ≤100**; ≥2 ข้อให้สงสัย
- **Lactate** — **≥2 mmol/L** = tissue hypoperfusion, **≥4** = high risk; ใช้ติดตาม response — ค่า **trend/clearance มีค่ากว่าจุดเดียว** แต่ระวังว่าไม่ได้มาจาก hypoperfusion เสมอไป (**type B lactate**: β-agonist/adrenaline, liver failure, metformin, thiamine deficiency)
- **ScvO₂ / SvO₂ (venous oxygen saturation)** — กระจกสะท้อนดุล **DO₂/VO₂ balance** (เลือดดำที่เหลือหลังเนื้อเยื่อดึง O₂ ไปใช้): **SvO₂ (mixed, จาก PA/Swan)** ปกติ ~65–75% · **ScvO₂ (central, จาก SVC/RA)** วัดง่ายกว่า ปกติ ~70%+; ค่าขยับตาม 4 ปัจจัย — cardiac output, Hb, SaO₂, oxygen consumption

การอ่าน lactate คู่กับ ScvO₂/SvO₂ ช่วยแยกชนิด shock ได้—ห้ามอ่านตัวเดียว:

| สถานการณ์ | Lactate | ScvO₂/SvO₂ | ตีความ |
| --- | --- | --- | --- |
| **Low-output / cardiogenic shock** | สูง | **ต่ำ (<65%)** | DO₂ ไม่พอ เนื้อเยื่อดึง O₂ มากขึ้นชดเชย → venous sat ตก |
| **Distributive / septic (vasoplegia)** | สูง | **ปกติ–สูง (>75%)** | shunt + cytopathic/microcirculatory — เลือดผ่านโดยเซลล์ดึง O₂ ไปใช้ไม่ได้ → venous sat สูงลวงทั้งที่ยัง hypoperfuse |
| **Resuscitation สำเร็จ** | เคลียร์ลง | เข้าสู่ปกติ | DO₂/VO₂ กลับสมดุล |

จุดที่ต้องระวังคือ **ScvO₂ สูง/ปกติไม่ได้แปลว่าปลอดภัยเสมอ** — ใน distributive/cytopathic hypoxia เลือดวิ่งผ่านเนื้อเยื่อโดยเซลล์ดึง O₂ ไปใช้ไม่ได้ ทำให้ venous sat สูงลวงทั้งที่ lactate ยังสูงและอวัยวะยังขาดเลือด — จึงต้องอ่านคู่ lactate เสมอ ไม่ใช้ตัวใดตัวหนึ่ง

❗ **Nuance:** qSOFA มี sensitivity ต่ำ ห้ามใช้คัดออก — ใช้ clinical judgment + SOFA ร่วม

## 4. 💊 Management & Pharmacodynamics

> 🔗 **Order actionable ทั้งชุดอยู่ที่:** [Sepsis Standing Order](https://app.notion.com/p/Sepsis-321224abad8180d29ff5d96277b9e26e?pvs=21) — ส่วนนี้อธิบายเฉพาะหลักการ (RULE 2: link ไม่เขียน order ซ้ำ)
> 

หลักการ **"early recognition, early resuscitation"** — ทุกชั่วโมงที่ล่าช้าเพิ่ม mortality:

**Guideline-anchored pillars (SSC)**

- **Early fluid** — crystalloid **30 mL/kg** ใน 3 ชม.แรก เพื่อฟื้น preload/perfusion แล้วประเมินซ้ำด้วย dynamic measures
- **Early empirical ATB** — ภายใน **1 ชม.** (shock) คลุมตาม source + local resistance แล้ว **de-escalate** เมื่อได้ culture (antimicrobial stewardship)
- **Vasopressor** — **norepinephrine** first-line เมื่อ MAP <65; กระตุ้น **α1-adrenergic receptor** หดหลอดเลือดสู้ vasoplegia
- **Source control** — drain/remove/ผ่าตัดภายใน 6–12 ชม. สำคัญไม่แพ้ยา

**Adjunctive / refractory**

- **Hydrocortisone** — refractory septic shock ที่ยังต้องใช้ vasopressor สูง; ฟื้น vascular responsiveness ต่อ catecholamine

> ⚠️ **ต้องอัปเดต:** เพจ order เดิมอ้าง **SSC 2021** — ตอนนี้มี **SSC 2026 (Crit Care Med, มี.ค. 2026)** ออกแล้ว ควรทบทวน order set ให้ตรง 2026
> 

## 5. 📚 Landmark Trials & Literature

- **Sepsis-3 (JAMA 2016)** — เลิก SIRS → ใช้ SOFA-based organ dysfunction
- **ARISE / ProCESS / ProMISe** — **EGDT** แบบ protocol เข้มไม่เหนือ usual care → เลิกยึด EGDT เดิม
- **ANDROMEDA-SHOCK (2019)** — CRT-guided resuscitation ไม่ด้อยกว่า lactate-guided
- **SSC 2021 → 2026** — guideline bundle หลัก ล่าสุดขยับเป็น 2026

## 🎯 High-Yield Recall

- **นิยาม**: Sepsis = infection + **SOFA ↑≥2**; **septic shock** = vasopressor คง MAP ≥65 + lactate >2 ทั้งที่ fluid พอ
- **Core mechanism**: dysregulated host response → cytokine storm → vasoplegia + capillary leak + microthrombosis
- **Bundle**: fluid 30 mL/kg/3hr + ATB ′1 ชม. + norepinephrine (MAP<65) + source control
- **Vasopressor**: norepinephrine first-line (α1 agonist); hydrocortisone ถ้า refractory
- **Trial**: Sepsis-3, ARISE/ProCESS/ProMISe, ANDROMEDA-SHOCK
- **Pitfall**: qSOFA sensitivity ต่ำ อย่าใช้คัดออก; สูงอายุ/immunocompromised อาจไม่มีไข้
