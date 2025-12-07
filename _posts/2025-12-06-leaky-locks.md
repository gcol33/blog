---
layout: post
title: "Leaky Locks"
date: 2025-12-06
categories: security information-theory history
toc: true
---

## What Counts as Information?

In 1943, the telephone in Winston Churchill's war room was a problem.

The transatlantic calls to Roosevelt were encrypted by a system called SIGSALY, fifty tons of equipment that digitized speech, scrambled it with one-time pads, and reassembled it on the other end. The voice channel was mathematically unbreakable. The Germans couldn't decode a single word.

But Bell Labs engineer A.B. Clark noticed something troubling. The encryption scrambled the *content* of Churchill's speech. It didn't scramble the *rhythm*. The timing of syllables, the cadence of sentences, the patterns of pauses: all of it passed through intact.

Clark realized that rhythm alone might be enough to reconstruct words. He was right. The phenomenon would later be called "residual intelligibility." The secret wasn't in the message. It was in the *shape* of the message.

SIGSALY was redesigned to mask timing patterns. The fix added more equipment. More weight. More complexity. All to hide something no one had thought to protect: the rhythm.

This is the story of the twentieth century's long education in what counts as information.

---

## The Beeping Safe

The lesson had to be learned many times.

In the 1980s, hotel room safes used a simple four-digit code. Guests would set their own combination, and the safe would beep once for each correct digit as you entered it.

Thieves figured it out immediately. Start with 0000. If the safe beeps once, the first digit is 0. If not, try 1000. Work through 0-9 until you hear a beep. Then move to the second digit.

A four-digit safe has 10,000 combinations. These safes fell in 40 tries.

The safe protected the code. It didn't protect *information about* the code: how many digits were correct. That distinction cost everything.

---

## The Collapse

Here is the mathematics of what happens when structure leaks.

A password with $n$ positions, each drawn from an alphabet of size $k$, has $k^n$ possible values. For a 4-digit PIN:

$$
10^4 = 10{,}000 \text{ attempts}
$$

But if the system reveals whether each position is correct independently, the attacker solves each position separately:

$$
k \times n = 10 \times 4 = 40 \text{ attempts}
$$

The exponent becomes a multiplier. Security collapses from $k^n$ to $kn$.

| Secret length | Without leak | With leak | Collapse |
|---------------|--------------|-----------|----------|
| 4 digits      | 10,000       | 40        | 250× |
| 8 lowercase   | 208 billion  | 208       | 1 billion× |
| 12 mixed      | $10^{21}$    | 744       | $10^{18}$× |

The longer the secret, the more catastrophic the leak. This is not a bug in one safe. It's a theorem about information.

---

## The Collapse, Visualized

<div id="collapse-demo" style="max-width: 720px; margin: 0 auto;">
  <div style="border: 1px solid #000; overflow: hidden;">
    <svg id="collapse-svg" style="width:100%; height:260px; background:#fff;"></svg>
  </div>

  <div class="collapse-controls">
    <label>Alphabet size (k)
      <input type="range" id="k-slider" min="2" max="26" value="10" />
    </label>
    <label>Length (n)
      <input type="range" id="n-slider" min="2" max="12" value="4" />
    </label>
  </div>

  <div id="collapse-stats" class="collapse-stats">
    <div class="collapse-stat-row"><span>Without leak:</span><strong id="exp-value">10,000</strong></div>
    <div class="collapse-stat-row"><span>With leak:</span><strong id="lin-value">40</strong></div>
    <div class="collapse-stat-row"><span>Collapse factor:</span><strong id="ratio-value">250×</strong></div>
  </div>
</div>

{% raw %}
<style>
#collapse-demo { font-variant-numeric: tabular-nums; }
#collapse-demo * { box-sizing: border-box; }

#collapse-demo .collapse-controls {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 10px;
}
@media (max-width: 560px) {
  #collapse-demo .collapse-controls { grid-template-columns: 1fr; }
}

#collapse-demo label {
  display: flex;
  flex-direction: column;
  font-size: 0.95em;
  gap: 4px;
}

#collapse-demo input[type="range"] {
  width: 100%;
  appearance: none;
  height: 6px;
  background: #eee;
  outline: none;
}
#collapse-demo input[type="range"]::-webkit-slider-thumb {
  appearance: none; width: 14px; height: 14px;
  border-radius: 50%; background: #000; cursor: pointer;
}
#collapse-demo input[type="range"]::-moz-range-thumb {
  width: 14px; height: 14px; border: none;
  border-radius: 50%; background: #000; cursor: pointer;
}

#collapse-demo .collapse-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#collapse-demo .collapse-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}
</style>

<script>
(function(){
  const svg = document.getElementById('collapse-svg');
  const kSlider = document.getElementById('k-slider');
  const nSlider = document.getElementById('n-slider');

  function fmt(x) {
    if (x >= 1e18) return (x / 1e18).toFixed(1) + ' × 10¹⁸';
    if (x >= 1e15) return (x / 1e15).toFixed(1) + ' × 10¹⁵';
    if (x >= 1e12) return (x / 1e12).toFixed(1) + ' trillion';
    if (x >= 1e9) return (x / 1e9).toFixed(1) + ' billion';
    if (x >= 1e6) return (x / 1e6).toFixed(1) + ' million';
    if (x >= 1e3) return x.toLocaleString();
    return x.toString();
  }

  function draw() {
    const k = parseInt(kSlider.value);
    const n = parseInt(nSlider.value);

    const exp = Math.pow(k, n);
    const lin = k * n;
    document.getElementById('exp-value').textContent = fmt(exp);
    document.getElementById('lin-value').textContent = fmt(lin);
    document.getElementById('ratio-value').textContent = fmt(Math.round(exp / lin)) + '×';

    const W = 700, H = 260;
    const pad = 14;  // constant border padding on all sides
    const innerW = W - pad * 2;
    const innerH = H - pad * 2;
    const labelMargin = 65;  // space for labels inside inner border
    const expLog = Math.log10(exp);
    const linLog = Math.log10(lin);
    const maxLog = Math.ceil(expLog);
    const scaleW = innerW - labelMargin - 10;

    let html = '';

    // Inner border
    html += `<rect x="${pad}" y="${pad}" width="${innerW}" height="${innerH}" fill="none" stroke="#000"/>`;

    const barLeft = pad + labelMargin;
    const y1 = pad + 30, y2 = pad + 95, barH = 40;
    const expW = (expLog / maxLog) * scaleW;
    const linW = (linLog / maxLog) * scaleW;

    html += `<rect x="${barLeft}" y="${y1}" width="${expW}" height="${barH}" fill="#000" stroke="#000"/>`;
    html += `<text x="${barLeft-8}" y="${y1+barH/2+5}" text-anchor="end" font-size="13">No leak</text>`;

    html += `<rect x="${barLeft}" y="${y2}" width="${Math.max(linW,3)}" height="${barH}" fill="#fff" stroke="#000"/>`;
    html += `<text x="${barLeft-8}" y="${y2+barH/2+5}" text-anchor="end" font-size="13">With leak</text>`;

    const axisY = pad + innerH - 30;
    html += `<line x1="${barLeft}" y1="${axisY}" x2="${barLeft + scaleW}" y2="${axisY}" stroke="#000"/>`;
    const tickStep = Math.max(1, Math.ceil(maxLog / 6));
    for (let i = 0; i <= maxLog; i += tickStep) {
      const x = barLeft + (i / maxLog) * scaleW;
      html += `<line x1="${x}" y1="${axisY}" x2="${x}" y2="${axisY + 5}" stroke="#000"/>`;
      html += `<text x="${x}" y="${axisY + 16}" text-anchor="middle" font-size="11">10^${i}</text>`;
    }

    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    svg.innerHTML = html;
  }

  kSlider.addEventListener('input', draw);
  nSlider.addEventListener('input', draw);
  draw();
})();
</script>
{% endraw %}

---

## Paul Kocher's Discovery

For decades after the beeping safe, cryptographers believed they had learned the lesson. Don't leak partial information. Make verification all-or-nothing.

They were wrong. They had only learned half the lesson.

In 1996, a twenty-three-year-old cryptographer named Paul Kocher published a paper that redrew the boundaries of information security. He showed that even when software reveals nothing explicitly, the *time it takes to compute* is itself a channel.

Consider password verification:

```python
def check(input, stored):
    for i in range(len(stored)):
        if input[i] != stored[i]:
            return False
    return True
```

This code returns as soon as it finds a mismatch. A wrong first character fails in one microsecond. A wrong last character takes eight microseconds.

The timing *is* the beep.

Kocher demonstrated the attack against RSA implementations. By measuring how long decryption took for different inputs, he could extract private keys bit by bit. The attack worked remotely. It worked through noise. It worked against code that had been audited for security and revealed nothing through any official channel.

The cryptographic community was stunned. They had protected the message. They hadn't thought to protect the *duration* of the computation.

---

## The Expanding Boundary

Kocher's work opened a floodgate.

If timing is information, what else might be?

**1998: Power analysis.** Kocher again. The power consumed by a chip varies with the operations it performs. Different instructions draw different current. By measuring power consumption during cryptographic operations, attackers could extract keys from smart cards.

**1985 (published much later): Van Eck radiation.** Every wire is an antenna. CRT monitors emit electromagnetic radiation proportional to what they display. Wim van Eck showed you could reconstruct screen contents from across the street. Later researchers demonstrated the same for LCD screens, keyboards, and network cables.

**2003: Cache timing.** Modern CPUs have memory caches. Accessing cached data is fast; uncached data is slow. An attacker who shares your CPU can deduce what memory addresses you're touching, including cryptographic key material.

**2018: Spectre and Meltdown.** CPUs speculate about which instructions to execute next. Sometimes they guess wrong and roll back. But the speculative execution leaves traces in the cache. These traces leak secrets across process boundaries, across virtual machines, across the boundary between user code and the operating system kernel.

Each discovery expanded the definition of "information." First it was the message. Then it was metadata. Then timing. Then power. Then radiation. Then cache state. Then speculative execution.

The boundary is still moving.

---

## Shannon's Definition

The history of side channels is a history of expanding the concept of information itself.

Shannon defined information as reduction in uncertainty. A message conveys information because it tells you something you didn't know. By this definition, *anything* that reduces uncertainty is information, whether or not it was intended to communicate.

The safe's beep reduces uncertainty about which digit is correct. The computation's timing reduces uncertainty about which branch was taken. The chip's power draw reduces uncertainty about which operations occurred. The radiation from a cable reduces uncertainty about what it's carrying.

None of these channels were designed. All of them communicate.

---

## The Shape of Everything

**Netflix and traffic analysis.** Your video stream is encrypted. An eavesdropper sees only noise. But the *pattern* of the traffic (packet sizes, timing, bitrate changes) correlates with what you're watching. Researchers have identified specific movies from encrypted Netflix streams with over 99% accuracy.

**Keystroke dynamics.** The rhythm of your typing (how long you hold each key, the gaps between keystrokes) identifies you as reliably as a fingerprint. This works through encryption, through Tor, through any anonymizing layer.

**Website fingerprinting.** HTTPS hides which page you're viewing but not the pattern of requests: how many resources, what sizes, what timing. The pattern is enough to identify the site with high accuracy.

These are not attacks in the traditional sense. No lock is picked. No cipher is broken. The information was there all along, in the shape of the activity.

---

## Your Rhythm

<div id="rhythm-demo" style="max-width: 720px; margin: 0 auto;">
  <p style="margin-top: 0;">Type anything below. The content doesn't matter. Your rhythm is the signal.</p>

  <div style="border: 1px solid #000; overflow: hidden;">
    <input type="text" id="rhythm-input" placeholder="Type here..." style="width: 100%; padding: 0.5em; font-size: 1em; border: none; border-bottom: 1px solid #000; box-sizing: border-box;">
    <canvas id="rhythm-canvas" style="width: 100%; height: 100px; background: #fff;"></canvas>
  </div>

  <div class="rhythm-stats">
    <div class="rhythm-stat-row"><span>Mean interval:</span><strong id="r-mean">—</strong> ms</div>
    <div class="rhythm-stat-row"><span>Std dev:</span><strong id="r-std">—</strong> ms</div>
    <div class="rhythm-stat-row"><span>Signature:</span><strong id="r-sig" style="font-family: monospace; letter-spacing: 1px;">—</strong></div>
  </div>
</div>

{% raw %}
<style>
#rhythm-demo { font-variant-numeric: tabular-nums; }
#rhythm-demo * { box-sizing: border-box; }

#rhythm-demo .rhythm-stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  margin-top: 10px;
}
#rhythm-demo .rhythm-stat-row {
  border-top: 1px solid #000;
  padding: 6px 0;
  font-size: 0.95em;
  display: flex;
  gap: 6px;
}
</style>

<script>
(function(){
  const input = document.getElementById('rhythm-input');
  const canvas = document.getElementById('rhythm-canvas');
  const ctx = canvas.getContext('2d');

  let times = [], intervals = [];

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function draw() {
    const W = canvas.clientWidth, H = canvas.clientHeight;
    const pad = Math.round(Math.min(W, H) * 0.047);  // ~14px at 300px height
    ctx.clearRect(0, 0, W, H);

    // Inner border
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 1;
    ctx.strokeRect(pad, pad, W - pad*2, H - pad*2);

    if (intervals.length < 2) return;

    const max = Math.max(...intervals, 150);
    const innerW = W - pad*2;
    const innerH = H - pad*2;
    const barW = Math.min(16, (innerW - pad) / intervals.length);

    ctx.fillStyle = '#000';
    for (let i = 0; i < intervals.length; i++) {
      const h = (intervals[i] / max) * (innerH - pad);
      ctx.fillRect(pad + pad/2 + i * barW, H - pad - pad/2 - h, barW - 2, h);
    }
  }

  function update() {
    if (intervals.length < 2) return;
    const mean = intervals.reduce((a, b) => a + b, 0) / intervals.length;
    const std = Math.sqrt(intervals.reduce((s, x) => s + (x - mean) ** 2, 0) / intervals.length);

    document.getElementById('r-mean').textContent = mean.toFixed(0);
    document.getElementById('r-std').textContent = std.toFixed(0);

    const sig = intervals.slice(-12).map(i => i < mean * 0.75 ? '▄' : i > mean * 1.25 ? '█' : '▆').join('');
    document.getElementById('r-sig').textContent = sig || '—';
  }

  input.addEventListener('keydown', () => {
    const now = performance.now();
    if (times.length > 0) intervals.push(now - times[times.length - 1]);
    times.push(now);
    if (times.length > 60) { times.shift(); intervals.shift(); }
    update();
    draw();
  });

  window.addEventListener('resize', resize);
  resize();
})();
</script>
{% endraw %}

Different people produce different patterns. The text vanishes into encryption. The signature persists.

---

## The Arms Race Has No End

The natural response is: fix the leaks. And cryptographers have tried.

**Constant-time code.** Compare all characters, even after finding a mismatch. Make every branch take the same time. Never let computation depend on secret data.

**Blinding.** Add random noise to inputs. The answer is the same, but the intermediate steps are randomized, masking power and timing patterns.

**Shielding.** Faraday cages block electromagnetic radiation. Expensive. Imperfect. A well-funded adversary can still get through.

Each fix addresses one channel. But physics guarantees there are always more.

Computation requires energy. Energy dissipates as heat, radiation, vibration. Any physical process leaves traces. The question is not whether information leaks, but whether an adversary can detect it.

For the NSA, the threshold is low. For a random thief, high. But the threshold keeps falling as sensors improve and analysis gets cheaper.

---

## The Moving Boundary

Here is what the twentieth century taught us:

**Information is not what you intend to reveal. It is what can be inferred from what you do.**

The boundary between "the secret" and "information about the secret" is not fixed. It moves as our ability to measure improves. What leaked undetectably in 1980 leaks detectably in 2000. What seems safe today will leak tomorrow.

This is not paranoia. It is physics.

Churchill's engineers thought they were protecting speech. They were forced to protect rhythm. Cryptographers thought they were protecting keys. They were forced to protect timing, power, radiation, cache access, and speculative execution.

Each generation discovers that the last generation's definition of "the secret" was too narrow.

---

## Privacy, Anonymity, AI

**Privacy.** Every digital action has a shape: timing, size, frequency. Encryption hides content but not shape. Metadata is data.

**Anonymity.** Behavioral patterns are signatures. How you type, how you move your mouse, how you browse. These patterns persist across contexts. True anonymity requires suppressing not just identity but behavior, and behavior is hard to fake.

**AI.** Machine learning excels at finding patterns humans miss. The leaks that were too subtle to exploit manually become tractable with enough data and compute. The attacker's threshold keeps dropping.

---

## The Lock Will Always Talk

Return to the beeping safe.

The fix seems obvious: remove the beep. But the beep was not the problem. The problem was that the mechanism processed each digit separately, and that separation was detectable.

Make the electronics silent and the timing still differs. Equalize the timing and the power draw still differs. Shield the power and the EM radiation still differs. Shield everything and the fact that you're standing in front of the safe still reveals something.

Every physical process is a broadcast. Security is not about stopping the broadcast. It is about ensuring the broadcast conveys nothing useful.

This is hard. It requires understanding what information is: not what you intend to transmit, but what can be received.
