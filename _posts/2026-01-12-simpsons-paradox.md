---
layout: post
title: "Simpson's Paradox"
date: 2026-01-12
categories: probability statistics paradox
toc: true
---

## A Drug Trial Gone Wrong

A hospital tests a new drug. Among patients who received it, 78% recovered. Among those who didn't, 83% recovered. The drug appears harmful.

But look at the breakdown by severity:

**Mild cases:**
- Drug group: 81 of 87 recovered (93%)
- Control group: 234 of 270 recovered (87%)

**Severe cases:**
- Drug group: 192 of 263 recovered (73%)
- Control group: 55 of 80 recovered (69%)

The drug improves recovery in mild cases. It improves recovery in severe cases. Yet when you combine the groups, recovery is worse with the drug.

This is Simpson's Paradox: a trend that appears in subgroups can reverse or disappear when the subgroups are combined.

---

## The Arithmetic

The numbers aren't a trick of rounding. They follow from how the patients were distributed.

|  | Drug | Control |
|--|------|---------|
| Mild | 81 of 87 (93%) | 234 of 270 (87%) |
| Severe | 192 of 263 (73%) | 55 of 80 (69%) |
| **Total** | **273 of 350 (78%)** | **289 of 350 (83%)** |

The drug wins in both subgroups but loses overall.

The key is patient allocation. Most drug patients had severe cases (263 of 350, or 75%), while most control patients had mild cases (270 of 350, or 77%). Severe cases have lower recovery rates regardless of treatment. When you pool the data, this imbalance drags down the drug group's overall rate.

Verify the totals:

$$
\text{Drug: } \frac{81 + 192}{87 + 263} = \frac{273}{350} = 78\%
$$

$$
\text{Control: } \frac{234 + 55}{270 + 80} = \frac{289}{350} = 82.6\%
$$

The aggregate reverses the subgroup pattern because severity—which affects both treatment assignment and outcome—isn't held constant.

---

## See It Happen

Drag patients between groups. Watch the aggregate rates shift.

<div id="simpson-demo" style="max-width: 720px; margin: 0 auto;">
  <svg id="simpson-svg" style="width:100%; height:340px; background:#fff; border:1px solid #000;"></svg>

  <div class="simpson-controls">
    <button id="simpson-reset">Reset</button>
    <button id="simpson-scenario1">Scenario: Drug looks harmful</button>
    <button id="simpson-scenario2">Scenario: Drug looks helpful</button>
  </div>

  <div class="simpson-stats">
    <div class="simpson-stat-row">
      <span>Drug group recovery:</span>
      <strong id="drug-total">—</strong>
    </div>
    <div class="simpson-stat-row">
      <span>Control group recovery:</span>
      <strong id="control-total">—</strong>
    </div>
    <div class="simpson-stat-row">
      <span>Drug better in mild?</span>
      <strong id="mild-winner">—</strong>
    </div>
    <div class="simpson-stat-row">
      <span>Drug better in severe?</span>
      <strong id="severe-winner">—</strong>
    </div>
  </div>

  <div id="simpson-narrative" class="simpson-narrative">
    Adjust the sliders to change how patients are distributed between groups.
  </div>
</div>

{% raw %}
<style>
#simpson-demo { font-variant-numeric: tabular-nums; }
#simpson-demo * { box-sizing: border-box; }

#simpson-demo .simpson-controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 10px;
}

#simpson-demo button {
  padding: 0.5em 1em;
  font-size: 0.95em;
  cursor: pointer;
  border: 1px solid #000;
  background: #fff;
}
#simpson-demo button:hover {
  background: #eee;
}

#simpson-demo .simpson-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
  margin-top: 10px;
}
@media (max-width: 500px) {
  #simpson-demo .simpson-stats { grid-template-columns: 1fr; }
}

#simpson-demo .simpson-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}

#simpson-demo .simpson-narrative {
  border-top: 1px solid #000;
  padding: 10px 0;
  font-size: 0.95em;
}
</style>

<script>
(function(){
  const svg = document.getElementById('simpson-svg');

  // Recovery rates (fixed)
  const rates = {
    mild: { drug: 0.93, control: 0.87 },
    severe: { drug: 0.73, control: 0.69 }
  };

  // Patient counts (adjustable)
  let counts = {
    mild: { drug: 87, control: 270 },
    severe: { drug: 263, control: 80 }
  };

  function computeRecoveries(group) {
    const mildRec = Math.round(counts.mild[group] * rates.mild[group]);
    const severeRec = Math.round(counts.severe[group] * rates.severe[group]);
    const totalPat = counts.mild[group] + counts.severe[group];
    const totalRec = mildRec + severeRec;
    return { mildRec, severeRec, totalPat, totalRec };
  }

  function draw() {
    const rect = svg.getBoundingClientRect();
    const W = rect.width, H = rect.height;
    const rem = parseFloat(getComputedStyle(document.documentElement).fontSize);
    const pad = 0.875 * rem;
    const innerW = W - pad * 2;
    const innerH = H - pad * 2;

    let html = '';
    html += `<rect x="${pad}" y="${pad}" width="${innerW}" height="${innerH}" fill="none" stroke="#000"/>`;

    const colW = innerW / 2 - pad;
    const drugX = pad + pad;
    const ctrlX = pad + innerW / 2 + pad / 2;

    const fontSize = Math.min(14, innerW * 0.025);
    const titleY = pad + pad + fontSize;

    html += `<text x="${drugX + colW/2}" y="${titleY}" text-anchor="middle" font-size="${fontSize + 2}" font-weight="bold">Drug Group</text>`;
    html += `<text x="${ctrlX + colW/2}" y="${titleY}" text-anchor="middle" font-size="${fontSize + 2}" font-weight="bold">Control Group</text>`;

    const boxTop = titleY + pad;
    const boxH = (innerH - boxTop + pad - pad * 2) / 2 - pad / 2;

    // Mild boxes
    const mildY = boxTop;
    html += drawBox(drugX, mildY, colW, boxH, 'Mild', counts.mild.drug, rates.mild.drug, fontSize);
    html += drawBox(ctrlX, mildY, colW, boxH, 'Mild', counts.mild.control, rates.mild.control, fontSize);

    // Severe boxes
    const sevY = mildY + boxH + pad / 2;
    html += drawBox(drugX, sevY, colW, boxH, 'Severe', counts.severe.drug, rates.severe.drug, fontSize);
    html += drawBox(ctrlX, sevY, colW, boxH, 'Severe', counts.severe.control, rates.severe.control, fontSize);

    // Sliders (as draggable indicators)
    const sliderY = sevY + boxH + pad;

    svg.innerHTML = html;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

    updateStats();
  }

  function drawBox(x, y, w, h, label, n, rate, fontSize) {
    const recovered = Math.round(n * rate);
    const pct = (rate * 100).toFixed(0);
    let s = '';
    s += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#fff" stroke="#000"/>`;
    s += `<text x="${x + w/2}" y="${y + fontSize + 4}" text-anchor="middle" font-size="${fontSize}" font-weight="bold">${label}</text>`;
    s += `<text x="${x + w/2}" y="${y + h/2 + fontSize/3}" text-anchor="middle" font-size="${fontSize}">${recovered} of ${n} recovered</text>`;
    s += `<text x="${x + w/2}" y="${y + h/2 + fontSize * 1.5}" text-anchor="middle" font-size="${fontSize}">(${pct}%)</text>`;
    return s;
  }

  function updateStats() {
    const drug = computeRecoveries('drug');
    const ctrl = computeRecoveries('control');

    const drugPct = drug.totalPat > 0 ? (100 * drug.totalRec / drug.totalPat).toFixed(1) : '—';
    const ctrlPct = ctrl.totalPat > 0 ? (100 * ctrl.totalRec / ctrl.totalPat).toFixed(1) : '—';

    document.getElementById('drug-total').textContent = `${drug.totalRec} of ${drug.totalPat} (${drugPct}%)`;
    document.getElementById('control-total').textContent = `${ctrl.totalRec} of ${ctrl.totalPat} (${ctrlPct}%)`;

    const mildDrugPct = rates.mild.drug * 100;
    const mildCtrlPct = rates.mild.control * 100;
    const sevDrugPct = rates.severe.drug * 100;
    const sevCtrlPct = rates.severe.control * 100;

    document.getElementById('mild-winner').textContent = `Yes (${mildDrugPct.toFixed(0)}% vs ${mildCtrlPct.toFixed(0)}%)`;
    document.getElementById('severe-winner').textContent = `Yes (${sevDrugPct.toFixed(0)}% vs ${sevCtrlPct.toFixed(0)}%)`;

    const drugWinsOverall = parseFloat(drugPct) > parseFloat(ctrlPct);
    const narrative = document.getElementById('simpson-narrative');

    if (drugWinsOverall) {
      narrative.textContent = `The drug wins in both subgroups AND overall. No paradox here—the groups are balanced.`;
    } else {
      narrative.textContent = `The drug wins in both subgroups but LOSES overall. The paradox emerges because ${counts.severe.drug} of ${drug.totalPat} drug patients (${(100*counts.severe.drug/drug.totalPat).toFixed(0)}%) had severe cases, vs only ${counts.severe.control} of ${ctrl.totalPat} (${(100*counts.severe.control/ctrl.totalPat).toFixed(0)}%) in control.`;
    }
  }

  function setScenario(mildDrug, mildCtrl, sevDrug, sevCtrl) {
    counts.mild.drug = mildDrug;
    counts.mild.control = mildCtrl;
    counts.severe.drug = sevDrug;
    counts.severe.control = sevCtrl;
    draw();
  }

  document.getElementById('simpson-reset').addEventListener('click', () => setScenario(175, 175, 175, 175));
  document.getElementById('simpson-scenario1').addEventListener('click', () => setScenario(87, 270, 263, 80));
  document.getElementById('simpson-scenario2').addEventListener('click', () => setScenario(270, 87, 80, 263));

  window.addEventListener('resize', draw);
  draw();
})();
</script>
{% endraw %}

---

## Berkeley, 1973

The paradox made headlines in a 1975 paper by Bickel, Hammel, and O'Connell examining graduate admissions at UC Berkeley.

The aggregate numbers looked damning:

|  | Applicants | Admitted |
|--|------------|----------|
| Men | 8,442 | 44% |
| Women | 4,321 | 35% |

A nine-point gap. The university faced accusations of discrimination.

But when the researchers examined individual departments, the pattern reversed. In most departments, women were admitted at equal or higher rates than men. Four of the six largest departments favored women.

The explanation: women applied disproportionately to competitive departments (English, History) with low acceptance rates for everyone. Men applied more often to less competitive departments (Engineering, Chemistry) with high acceptance rates for everyone.

The admissions process within each department showed no bias. The aggregate showed a gap because of where candidates chose to apply.

---

## Kidney Stones, 1986

A study compared two treatments for kidney stones: open surgery (Treatment A) and a newer, less invasive procedure (Treatment B).

|  | Treatment A | Treatment B |
|--|-------------|-------------|
| Small stones | 93% success (81/87) | 87% success (234/270) |
| Large stones | 73% success (192/263) | 69% success (55/80) |
| **Overall** | **78% success (273/350)** | **83% success (289/350)** |

Treatment A wins in both categories but loses overall.

The reason: doctors assigned the newer, gentler Treatment B to easier cases (small stones). Treatment A, being more invasive, was reserved for difficult cases (large stones). When you ignore stone size and just count successes, Treatment B looks better because it was given to patients who would have done well anyway.

This matters for medical decisions. A patient with large kidney stones should prefer Treatment A, despite its worse aggregate numbers.

---

## The Confounding Variable

Simpson's Paradox arises when a third variable influences both the grouping and the outcome.

In the drug example, severity determines both which treatment patients receive (sicker patients get the drug) and how likely they are to recover (sicker patients do worse). Severity is a **confounding variable**.

Graphically:

```
Severity ──────► Treatment
    │                │
    │                │
    ▼                ▼
         Recovery
```

Severity affects treatment assignment. Severity affects recovery. If you ignore severity, you conflate its effect with the treatment's effect.

The solution is **stratification**: analyze within levels of the confounder. The drug works in mild cases and works in severe cases. That's the real story. The aggregate is misleading because it mixes two different populations.

---

## When to Pool, When to Split

The paradox raises a practical question: which answer is right? Should we trust the subgroup analysis or the aggregate?

There's no universal rule. It depends on the causal structure.

**Pool when** the subgroups are arbitrary divisions that don't affect the outcome. If you split patients by birth month and find different treatment effects in each month, you should probably pool—birth month isn't a cause of recovery.

**Split when** the subgroups reflect a genuine confounder that affects both treatment and outcome. If sicker patients systematically receive one treatment and do worse regardless of treatment, you need to control for severity.

The Berkeley case is instructive. Should we pool across departments or not? It depends what question you're asking. If you're asking "Are admissions committees biased?", split by department—that's where decisions happen. If you're asking "Do women face barriers to graduate education at Berkeley?", the aggregate might matter, because whatever steered women toward competitive departments is part of the system.

---

## Simpson, Yule, and the History

The paradox carries Edward Simpson's name from his 1951 paper, but the phenomenon was known earlier.

In 1903, Udny Yule noted that correlations could reverse when populations were combined. Karl Pearson described similar reversals around the same time. Some call it the Yule-Simpson effect.

The name "paradox" overstates the case. Once you understand confounding, the reversal is arithmetically inevitable under certain conditions. The surprise comes from expecting aggregates to preserve subgroup relationships—an expectation that probability doesn't guarantee.

---

## Aggregation and Interpretation

Averages are summaries, and summaries discard information. When the discarded information matters, the summary misleads.

Simpson's Paradox is a reminder that data doesn't interpret itself. The same numbers support opposite conclusions depending on which comparisons you make. Choosing the right comparison requires understanding the causal structure—what causes what, and what you're trying to learn.

A drug can work for everyone and help no one, if "everyone" hides the populations where it's tested.
