---
layout: post
title: "Leaky Locks"
date: 2025-12-06
categories: security probability information-theory
toc: true
---

## The Shadow of the Secret

You encrypt a message. The ciphertext is random noise to anyone without the key. The content is safe.

But you sent the message at 2:47 AM. It was 3.2 kilobytes. You sent another one 12 minutes later, shorter. Then nothing until morning.

The message is hidden. Its *shadow* is not.

This is meta-information: data about data. And it turns out that protecting the secret is easy compared to protecting its shape.

---

## The Beeping Safe

In the 1980s, hotel room safes used a simple four-digit code. Guests would set their own combination, and the safe would beep once for each correct digit as you entered it.

Beep. Beep. Beep. Beep. The safe opens.

Thieves figured it out immediately. Start with 0000. If the safe beeps once, the first digit is 0. If not, try 1000. Work through 0-9 until you hear a beep. Then move to the second digit.

A four-digit safe should require up to 10,000 attempts to crack. These safes fell in at most 40.

The safe never revealed the code. It revealed *meta-information about* the code: how many digits were correct. That was enough.

---

## The Collapse

Here is what happens mathematically when meta-information leaks.

A password with $n$ positions, each drawn from an alphabet of size $k$, has $k^n$ possible values. For a 4-digit PIN:

$$
10^4 = 10{,}000 \text{ attempts}
$$

But if the system leaks whether each position is correct independently, the attacker can solve each position separately:

$$
k \times n = 10 \times 4 = 40 \text{ attempts}
$$

The exponent becomes a multiplier. What was $k^n$ is now $kn$.

| Password length | Without leak | With leak | Collapse factor |
|-----------------|--------------|-----------|-----------------|
| 4 digits        | 10,000       | 40        | 250$\times$ |
| 8 lowercase     | 208 billion  | 208       | 1 billion$\times$ |
| 12 mixed        | $10^{21}$    | 744       | $10^{18}\times$ |

The longer the secret, the more catastrophic the leak.

---

## See the Collapse

<div id="collapse-viz" style="max-width: 720px; margin: 1.5em auto;">
  <div style="margin-bottom: 1em;">
    <label>Alphabet size (k):
      <input type="range" id="k-slider" min="2" max="26" value="10" style="width: 120px;">
      <span id="k-value">10</span>
    </label>
    &nbsp;&nbsp;
    <label>Password length (n):
      <input type="range" id="n-slider" min="2" max="12" value="4" style="width: 120px;">
      <span id="n-value">4</span>
    </label>
  </div>

  <svg id="collapse-svg" viewBox="0 0 700 300" style="width: 100%; height: auto; border: 1px solid #000; background: #fff;">
  </svg>

  <div style="display: flex; justify-content: space-between; margin-top: 1em; padding: 0.5em; background: #fafafa; border: 1px solid #ddd;">
    <div>
      <span class="lightText">Without leak:</span><br>
      <strong id="exp-value" style="font-family: monospace;">10,000</strong>
    </div>
    <div>
      <span class="lightText">With leak:</span><br>
      <strong id="lin-value" style="font-family: monospace;">40</strong>
    </div>
    <div>
      <span class="lightText">Collapse factor:</span><br>
      <strong id="ratio-value" style="font-family: monospace;">250x</strong>
    </div>
  </div>
</div>

{% raw %}
<script>
(function(){
  const svg = document.getElementById('collapse-svg');
  const kSlider = document.getElementById('k-slider');
  const nSlider = document.getElementById('n-slider');
  const kValue = document.getElementById('k-value');
  const nValue = document.getElementById('n-value');
  const expValue = document.getElementById('exp-value');
  const linValue = document.getElementById('lin-value');
  const ratioValue = document.getElementById('ratio-value');

  function formatNumber(x) {
    if (x >= 1e18) return (x / 1e18).toFixed(1) + ' quintillion';
    if (x >= 1e15) return (x / 1e15).toFixed(1) + ' quadrillion';
    if (x >= 1e12) return (x / 1e12).toFixed(1) + ' trillion';
    if (x >= 1e9) return (x / 1e9).toFixed(1) + ' billion';
    if (x >= 1e6) return (x / 1e6).toFixed(1) + ' million';
    if (x >= 1e3) return x.toLocaleString();
    return x.toString();
  }

  function draw() {
    const k = parseInt(kSlider.value);
    const n = parseInt(nSlider.value);
    kValue.textContent = k;
    nValue.textContent = n;

    const exp = Math.pow(k, n);
    const lin = k * n;
    const ratio = exp / lin;

    expValue.textContent = formatNumber(exp);
    linValue.textContent = formatNumber(lin);
    ratioValue.textContent = formatNumber(Math.round(ratio)) + 'x';

    // Visualization: two bars on log scale
    const maxLog = Math.log10(Math.pow(26, 12)); // max possible
    const expLog = Math.log10(exp);
    const linLog = Math.log10(lin);

    const W = 700, H = 300;
    const pad = 60;
    const barH = 50;
    const gap = 40;

    let html = '';

    // Y axis label
    html += `<text x="30" y="${H/2}" text-anchor="middle" font-size="14" transform="rotate(-90, 30, ${H/2})">Attempts (log scale)</text>`;

    // Scale
    const scaleW = W - pad * 2;
    const expBarW = (expLog / maxLog) * scaleW;
    const linBarW = (linLog / maxLog) * scaleW;

    // Exponential bar
    const y1 = 80;
    html += `<rect x="${pad}" y="${y1}" width="${expBarW}" height="${barH}" fill="#c66" stroke="#000"/>`;
    html += `<text x="${pad - 10}" y="${y1 + barH/2 + 5}" text-anchor="end" font-size="13">Without leak</text>`;
    html += `<text x="${pad + expBarW + 10}" y="${y1 + barH/2 + 5}" font-size="13" font-family="monospace">${formatNumber(exp)}</text>`;

    // Linear bar
    const y2 = y1 + barH + gap;
    html += `<rect x="${pad}" y="${y2}" width="${Math.max(linBarW, 2)}" height="${barH}" fill="#6a6" stroke="#000"/>`;
    html += `<text x="${pad - 10}" y="${y2 + barH/2 + 5}" text-anchor="end" font-size="13">With leak</text>`;
    html += `<text x="${pad + Math.max(linBarW, 2) + 10}" y="${y2 + barH/2 + 5}" font-size="13" font-family="monospace">${formatNumber(lin)}</text>`;

    // Axis
    html += `<line x1="${pad}" y1="${H - 40}" x2="${W - pad}" y2="${H - 40}" stroke="#000"/>`;

    // Tick marks
    for (let i = 0; i <= 24; i += 6) {
      const x = pad + (i / 24) * scaleW;
      html += `<line x1="${x}" y1="${H - 40}" x2="${x}" y2="${H - 35}" stroke="#000"/>`;
      html += `<text x="${x}" y="${H - 20}" text-anchor="middle" font-size="11">10^${i}</text>`;
    }

    svg.innerHTML = html;
  }

  kSlider.addEventListener('input', draw);
  nSlider.addEventListener('input', draw);
  draw();
})();
</script>
{% endraw %}

---

## Timing: The Invisible Beep

The hotel safe's feedback was obvious. Modern systems leak more subtly.

A naive password check:

```python
def check_password(input, stored):
    for i in range(len(stored)):
        if input[i] != stored[i]:
            return False   # Fails fast
    return True
```

This code returns immediately when it finds a wrong character. A password with a wrong first letter fails in 1 microsecond. A password with only the last character wrong takes 8 microseconds.

The timing *is* the beep.

An attacker who measures response times can learn each position independently - the same exponential-to-linear collapse.

In 2003, researchers demonstrated this against OpenSSL's RSA implementation. The attack worked remotely, over a network. Millisecond differences, amplified across thousands of requests, revealed private keys.

---

## Cable TV: Cracking the Broadcast

In the 1990s, satellite TV signals were encrypted. Subscribers got a smart card that decrypted the signal. Pirates wanted in.

The encryption was strong. But the smart cards would respond differently to valid versus invalid decryption attempts. By probing the card with carefully crafted inputs and measuring its responses, attackers could extract the keys incrementally.

The encryption protected the content. The card's *behavior* leaked the keys.

Same pattern. Different domain.

---

## Physical Locks: The Original Leak

This vulnerability predates computers entirely.

A traditional safe dial has numbers 0-99. A three-number combination has $100^3 = 1{,}000{,}000$ possibilities. But the mechanism has physical tolerances.

Skilled safecrackers apply slight pressure to the handle while slowly turning the dial. When a wheel reaches the correct position, the resistance changes subtly - a tiny give, a faint click.

This reduces the problem from a million combinations to roughly $100 \times 3 = 300$ tests. Each wheel can be solved independently.

The lock doesn't reveal the combination. It reveals *which wheel you're getting right*. That's enough.

---

## The Unfixable Leaks

You might think: just remove the feedback. Make everything constant-time. Don't beep, don't vary timing, don't respond differently.

But the hardware betrays you.

**Branch prediction.** Modern CPUs guess which way an if-statement will go and execute speculatively. Different guesses leave different traces in the cache. Spectre and Meltdown exploited this.

**Cache timing.** Accessing memory that's cached is faster than accessing memory that isn't. An attacker who shares your CPU can tell what memory addresses you've touched.

**Power consumption.** Chips draw different power for different operations. Measure the power draw with enough precision and you can reconstruct the computation.

**Electromagnetic radiation.** Wires emit radio signals proportional to their current. The Van Eck attack reconstructs CRT monitor images from across the room.

You can fix your code. You cannot fix physics.

---

## The Shape of Secrets

The deepest version of this problem goes beyond security.

Netflix encrypts your video stream. An eavesdropper sees only noise. But the *pattern* of the traffic - when packets arrive, how large they are, when you pause - reveals what you're watching. Researchers have identified specific movies from encrypted Netflix streams with over 99% accuracy.

The content is hidden. The *shape* of the content is not.

This is true everywhere:

**Encrypted messaging.** The messages are hidden but the timing, frequency, and size of messages reveal the relationship. Metadata is data.

**Keystroke dynamics.** How you type - your rhythm, your pauses, your patterns - identifies you as reliably as a fingerprint. Even through Tor, even with encrypted chat.

**Website fingerprinting.** HTTPS hides which page you're viewing but not the pattern of requests. The sequence of encrypted packet sizes reveals the site.

**Behavioral biometrics.** How you hold your phone, how you scroll, how you move your mouse. All of it is a signature you cannot turn off.

---

## Try It: Behavioral Fingerprinting

<div id="fingerprint-demo" style="max-width: 720px; margin: 1.5em auto; padding: 1em; border: 1px solid #000; background: #fff;">
  <p style="margin-top: 0;">Type anything in the box below. Your keystroke timing creates a signature.</p>

  <input type="text" id="fp-input" placeholder="Type here..." style="width: 100%; padding: 0.5em; font-size: 1em; border: 1px solid #000; box-sizing: border-box;">

  <div style="margin-top: 1em;">
    <canvas id="fp-canvas" style="width: 100%; height: 100px; border: 1px solid #000; background: #fafafa;"></canvas>
  </div>

  <div style="margin-top: 0.5em; font-size: 0.9em;">
    <span class="lightText">Average interval:</span> <strong id="fp-avg">—</strong>ms
    &nbsp;&nbsp;
    <span class="lightText">Variance:</span> <strong id="fp-var">—</strong>
    &nbsp;&nbsp;
    <span class="lightText">Pattern:</span> <span id="fp-pattern" style="font-family: monospace;">—</span>
  </div>

  <p class="lightText" style="margin-bottom: 0; font-size: 0.9em;">Different people produce different patterns. The content doesn't matter - the rhythm is the fingerprint.</p>
</div>

{% raw %}
<script>
(function(){
  const input = document.getElementById('fp-input');
  const canvas = document.getElementById('fp-canvas');
  const ctx = canvas.getContext('2d');
  const avgEl = document.getElementById('fp-avg');
  const varEl = document.getElementById('fp-var');
  const patternEl = document.getElementById('fp-pattern');

  let times = [];
  let intervals = [];

  function resizeCanvas() {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw();
  }

  function draw() {
    const W = canvas.clientWidth, H = canvas.clientHeight;
    ctx.clearRect(0, 0, W, H);

    if (intervals.length < 2) return;

    const maxInterval = Math.max(...intervals, 200);
    const barW = Math.min(20, (W - 20) / intervals.length);

    ctx.fillStyle = '#369';
    for (let i = 0; i < intervals.length; i++) {
      const h = (intervals[i] / maxInterval) * (H - 20);
      const x = 10 + i * barW;
      ctx.fillRect(x, H - 10 - h, barW - 2, h);
    }
  }

  function updateStats() {
    if (intervals.length < 2) {
      avgEl.textContent = '—';
      varEl.textContent = '—';
      patternEl.textContent = '—';
      return;
    }

    const avg = intervals.reduce((a, b) => a + b, 0) / intervals.length;
    const variance = intervals.reduce((sum, x) => sum + Math.pow(x - avg, 2), 0) / intervals.length;

    avgEl.textContent = avg.toFixed(0);
    varEl.textContent = variance.toFixed(0);

    // Create a simple pattern signature
    const pattern = intervals.slice(-10).map(i => {
      if (i < avg * 0.7) return 'F';  // Fast
      if (i > avg * 1.3) return 'S';  // Slow
      return 'M';  // Medium
    }).join('');
    patternEl.textContent = pattern;
  }

  input.addEventListener('keydown', function(e) {
    const now = performance.now();
    if (times.length > 0) {
      intervals.push(now - times[times.length - 1]);
    }
    times.push(now);

    // Keep last 50
    if (times.length > 50) {
      times.shift();
      intervals.shift();
    }

    updateStats();
    draw();
  });

  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();
})();
</script>
{% endraw %}

---

## What You Cannot Hide

The pattern is everywhere:

| What's protected | What leaks |
|------------------|------------|
| Password | Which characters are correct |
| Encrypted message | When it was sent, how large it is |
| HTTPS content | Sequence of request sizes |
| Video stream | Traffic pattern reveals the title |
| Text content | Keystroke rhythm reveals the author |
| File contents | Access patterns reveal what you're doing |

Encryption hides the content. Nothing hides the shape.

---

## The Design Lesson

Every system casts a shadow. The question is not whether information leaks, but *which* information, and whether it matters.

The beeping safe was obvious. Timing attacks are subtle. Hardware side-channels are fundamental. Behavioral biometrics are inescapable.

You can reduce leakage:
- Constant-time comparisons
- Traffic padding
- Randomized delays
- Noise injection

But you cannot eliminate it. The act of processing information leaves traces. Physics guarantees this.

The practical lesson is not paranoia. It's designing with awareness:

1. **Know what your system reveals** - not just directly, but through timing, size, frequency, and pattern
2. **Separate sensitive operations** - isolation limits what an attacker can correlate
3. **Assume the shape leaks** - design so that shape reveals less
4. **Defense in depth** - no single layer is leak-proof

The lock will always talk. The art is in giving it nothing important to say.
