# Graph Report - STUDY-TEMPLATE  (2026-11-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 571 nodes · 1638 edges · 21 communities (18 shown, 3 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 159 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 19

## God Nodes (most connected - your core abstractions)
1. `m()` - 72 edges
2. `e()` - 66 edges
3. `t()` - 42 edges
4. `b()` - 40 edges
5. `r()` - 39 edges
6. `q()` - 32 edges
7. `G()` - 27 edges
8. `ec()` - 25 edges
9. `wc()` - 23 edges
10. `ee()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `jp()` --indirect_call--> `qt()`  [INFERRED]
  site/assets/javascripts/bundle.77dd0ce9.min.js → site/assets/javascripts/workers/search.c47bb847.min.js
- `rs()` --indirect_call--> `ce()`  [INFERRED]
  site/assets/javascripts/bundle.77dd0ce9.min.js → site/assets/javascripts/workers/search.c47bb847.min.js
- `Vr()` --indirect_call--> `ve()`  [INFERRED]
  site/assets/javascripts/bundle.77dd0ce9.min.js → site/assets/javascripts/workers/search.c47bb847.min.js
- `bt()` --indirect_call--> `e()`  [INFERRED]
  site/assets/javascripts/workers/search.c47bb847.min.js → site/assets/javascripts/bundle.77dd0ce9.min.js
- `Ht()` --indirect_call--> `e()`  [INFERRED]
  site/assets/javascripts/workers/search.c47bb847.min.js → site/assets/javascripts/bundle.77dd0ce9.min.js

## Import Cycles
- None detected.

## Communities (21 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (98): Ac(), ae(), af(), Ap(), b(), bc(), bf(), br() (+90 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (70): a(), ao(), bn(), dn(), dr(), El(), eo(), fn() (+62 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (61): A(), ae(), At(), B(), bt(), C(), ce(), Ct() (+53 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (65): Ai(), an(), Ar(), at(), bi(), Ci(), cn(), co() (+57 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (42): copyright, extra, generator, extra_javascript, social, markdown_extensions, pymdownx.highlight, pymdownx.tabbed (+34 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (42): copyright, extra, generator, extra_javascript, social, markdown_extensions, pymdownx.highlight, pymdownx.tabbed (+34 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (25): as(), Ba(), be(), Cl(), ei(), fo(), ge(), H() (+17 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (28): environment, runs-on, steps, concurrency, cancel-in-progress, group, name, url (+20 more)

### Community 8 - "Community 8"
Cohesion: 0.16
Nodes (15): Bu(), Cs(), ds(), Du(), ep(), fp(), Gu(), hs() (+7 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (15): constructor(), f(), Fa(), gf(), iu(), ls(), ms(), na() (+7 more)

### Community 10 - "Community 10"
Cohesion: 0.18
Nodes (13): au(), bt(), Da(), es(), Hu(), ko(), se(), tu() (+5 more)

### Community 11 - "Community 11"
Cohesion: 0.27
Nodes (12): cu(), gt(), Ir(), Ka(), mp(), op(), pt(), Qa() (+4 more)

### Community 12 - "Community 12"
Cohesion: 0.31
Nodes (3): main(), parse_args(), prompt_with_default()

### Community 13 - "Community 13"
Cohesion: 0.28
Nodes (9): Bp(), Gp(), Gr(), nc(), oc(), qp(), vn(), Yp() (+1 more)

### Community 14 - "Community 14"
Cohesion: 0.40
Nodes (5): ns(), rn(), tn(), vi(), xl()

### Community 15 - "Community 15"
Cohesion: 0.50
Nodes (4): dl(), en(), ml(), oa()

### Community 16 - "Community 16"
Cohesion: 0.50
Nodes (4): Do(), fs(), Vu(), wu()

### Community 17 - "Community 17"
Cohesion: 0.67
Nodes (3): is(), pu(), Ya()

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `e()` connect `Community 3` to `Community 0`, `Community 1`, `Community 2`, `Community 6`, `Community 8`, `Community 11`, `Community 13`, `Community 14`?**
  _High betweenness centrality (0.150) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `e()` (e.g. with `bi()` and `d()`) actually correct?**
  _`e()` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06247836621668398 - nodes in this community are weakly interconnected._
- **Why does `se()` connect `Community 2` to `Community 3`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `t()` (e.g. with `bundle.77dd0ce9.min.js` and `Cr()`) actually correct?**
  _`t()` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05789473684210526 - nodes in this community are weakly interconnected._
- **Why does `ui()` connect `Community 1` to `Community 3`, `Community 6`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._