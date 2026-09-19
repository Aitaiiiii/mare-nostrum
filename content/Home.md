---
title: "Home"
tags: [home]
cssclasses:
  - dashboard
---

# 🐚 Mare Nostrum

<div class="mn-hero">
  <div class="mn-title">🐚 Mare Nostrum</div>
  <div class="mn-sub">Personal clinical second brain · Cold Peaks</div>
</div>

```dataviewjs
const typed = dv.pages().where(x => x.type);
const c = t => typed.where(x => x.type === t).length;
const tiles = [
  ["🧠 Diseases", c("Disease"), "#ef7d6b"],
  ["💊 Standing Orders", c("Standing Order"), "#f6d06a"],
  ["🫀 EKGs", c("EKG"), "#7fb6da"],
  ["🔁 Reviewing", dv.pages().where(x => x.review_status === "Reviewing").length, "#7fc9a3"],
];
const el = dv.el("div", "", { cls: "mn-kpi" });
el.innerHTML = tiles.map(([lab, n, z]) =>
  `<div class="mn-tile" style="--z:${z}"><div class="mn-num">${n}</div><div class="mn-lab">${lab}</div></div>`
).join("");
```

> [!info] Everything at a glance in [[Wiki Index]] — or launch a specialty map below. Tables update themselves as pages change.

###### quick launch
[[Cardiology (Map)]] [[Cardiothoracic Surgery (Map)]] [[Pediatric Cardiology (Map)]] [[Pulmonology (Map)]] [[Nephrology (Map)]] [[Endocrinology (Map)]] [[Gastroenterology & Hepatology (Map)]] [[Hematology-Oncology (Map)]] [[Infectious Disease (Map)]] [[Neurology (Map)]] [[Rheumatology (Map)]] [[Critical Care (Map)]] [[Cardiac Pharmacology (Map)]] [[Physiology (Map)]] [[Cardiology Approaches & Workflows (Map)]]

---

## 📊 Monographs by specialty

```dataviewjs
const specs = {};
for (const x of dv.pages().where(p => p.type === "Disease" && p.specialty)) {
  const s = "" + x.specialty;
  specs[s] = (specs[s] || 0) + 1;
}
const rows = Object.entries(specs).sort((a, b) => b[1] - a[1]);
const max = Math.max(1, ...rows.map(r => r[1]));
const bars = dv.el("div", "", { cls: "mn-bars" });
bars.innerHTML = rows.map(([s, n]) =>
  `<div class="mn-bar-row"><div class="mn-bar-lab">${s}</div><div class="mn-bar-track"><div class="mn-bar-fill" style="width:${(n / max * 100).toFixed(1)}%"></div></div><div class="mn-bar-val">${n}</div></div>`
).join("");
```

---

## 🔁 Currently reviewing

```base
filters:
  and:
    - review_status == "Reviewing"
views:
  - type: table
    name: In progress
    order:
      - file.name
      - specialty
      - rotation
      - updated
    sort:
      - property: updated
        direction: DESC
```

## 🆕 Recently updated

```base
filters:
  and:
    - type != null
    - '!file.inFolder("_raw")'
    - '!file.inFolder("_system")'
views:
  - type: table
    name: Latest
    order:
      - file.name
      - type
      - specialty
      - file.mtime
    sort:
      - property: file.mtime
        direction: DESC
    limit: 12
```

## ❤️ Cardiology

```base
filters:
  and:
    - specialty == "Cardiology"
    - type == "Disease"
views:
  - type: table
    name: Cardiology monographs
    order:
      - file.name
      - subspecialty
      - review_status
    sort:
      - property: file.name
        direction: ASC
    limit: 50
```

## 💊 Standing Orders

```base
filters:
  and:
    - type == "Standing Order"
views:
  - type: table
    name: Order sets
    order:
      - file.name
      - specialty
    sort:
      - property: specialty
        direction: ASC
```

## 🧹 Needs a summary

```base
filters:
  and:
    - type == "Disease"
    - '!summary'
views:
  - type: table
    name: Missing summary
    order:
      - file.name
      - specialty
      - updated
    sort:
      - property: file.name
        direction: ASC
    limit: 40
```

## 🫀 EKG library

```base
filters:
  and:
    - type == "EKG"
views:
  - type: cards
    name: EKGs
    order:
      - file.name
    sort:
      - property: file.name
        direction: ASC
    limit: 24
```
