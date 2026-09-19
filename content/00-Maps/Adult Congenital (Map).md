---
title: "Adult Congenital (Map)"
type: Map
tags: [map]
cssclasses:
  - map
---

# 👶 Adult Congenital

## Contents

_No notes yet._

<small>0 notes · live filterable table available in Obsidian (Dataview).</small>


## Lesions

```dataview
LIST rows.file.link
FROM #adult-congenital
WHERE type != "Map"
GROUP BY default(specialty, "General")
SORT file.name ASC
```
