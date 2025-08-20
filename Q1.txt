<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>IITM MLP – RevealJS Deck</title>
  <!-- Reveal.js core & theme from CDN -->
  <link rel="stylesheet" href="https://unpkg.com/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://unpkg.com/reveal.js@5/dist/theme/black.css" id="theme">
  <!-- Code highlighting (highlight.js default theme via Reveal plugin) -->
  <link rel="stylesheet" href="https://unpkg.com/highlight.js@11.9.0/styles/github.min.css">
  <style>
    .footer {
      position: absolute; bottom: 10px; left: 20px; font-size: 16px; opacity: .6;
    }
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">

      <!-- 1) Title slide with email present in the presentation -->
      <section>
        <h2>IITM MLP – RevealJS Demo</h2>
        <h4>Deck features: Markdown, fragments, code, math, notes</h4>
        <p class="fragment">Presenter: Anindya (example)</p>
        <p class="fragment">Email: <strong>23f3000916@ds.study.iitm.ac.in</strong></p>
        <aside class="notes">
          Greet the audience. Mention that this deck demonstrates all the requested capabilities.
          Point out that the email is visible on the first slide per requirements.
        </aside>
        <div class="footer">Email: 23f3000916@ds.study.iitm.ac.in</div>
      </section>

      <!-- 2) A slide written entirely in Markdown -->
      <section data-markdown>
        <textarea data-template>
# Markdown Slide ✅

- **This entire slide is authored in Markdown.**
- It supports *inline code* like `print("hello")` and lists.
- You can also include images and links.

> Pro tip: Use Markdown for fast iteration!

**Contact:** 23f3000916@ds.study.iitm.ac.in

Notes:
- These speaker notes can be added in HTML using `<aside class="notes">`, but here we showcase Markdown content.
        </textarea>
        <aside class="notes">
          Explain that Reveal can parse Markdown directly. Mention how convenient it is for writing content quickly.
        </aside>
      </section>

      <!-- 3) Fragments (animated elements) -->
      <section>
        <h3>Fragments (Animated Reveals)</h3>
        <ul>
          <li class="fragment">Point 1 appears first</li>
          <li class="fragment">Point 2 appears on click</li>
          <li class="fragment fade-up">Point 3 with fade-up</li>
          <li class="fragment highlight-current-blue">Point 4 (highlight)</li>
        </ul>
        <aside class="notes">Speak to each point as it appears. Keep a steady pace.</aside>
      </section>

      <!-- 4) Code samples with syntax highlighting -->
      <section>
        <h3>Code Sample – Python</h3>
        <pre><code class="language-python">from dataclasses import dataclass
from typing import List

@dataclass
class Transaction:
    amount: float
    date: str

def npv(rate: float, cashflows: List[Transaction]) -> float:
    return sum(t.amount / ((1 + rate) ** i) for i, t in enumerate(cashflows, start=1))

print(npv(0.1, [Transaction(100, "2025-01-01"), Transaction(200, "2026-01-01")]))
</code></pre>
        <aside class="notes">Point out automatic syntax highlighting via highlight.js plugin.</aside>
      </section>

      <section>
        <h3>Code Sample – JavaScript</h3>
        <pre><code class="language-javascript">// Compound interest
function futureValue(PV, r, n) {
  return PV * Math.pow(1 + r, n);
}
console.log(futureValue(1000, 0.08, 5));
</code></pre>
        <aside class="notes">Show JS example and connect to the later math slide.</aside>
      </section>

      <!-- 5) Mathematical equations (financial formulas) -->
      <section>
        <h3>Financial Math (KaTeX)</h3>
        <p>Compound Interest:</p>
        <p>\( FV = PV\,(1+r)^{n} \)</p>
        <p>Net Present Value:</p>
        <p>\( \mathrm{NPV} = \sum_{t=1}^{T} \dfrac{CF_t}{(1 + r)^{t}} \)</p>
        <aside class="notes">Briefly explain the meaning of each symbol and how it relates to earlier code.</aside>
      </section>

      <!-- 6) Speaker notes guidance slide -->
      <section>
        <h3>Speaker Notes</h3>
        <p>Press <kbd>s</kbd> to open the speaker view.</p>
        <p class="fragment">Use notes to pace yourself and remember key points.</p>
        <aside class="notes">Demonstrate opening speaker view if presenting live.</aside>
      </section>

      <!-- 7) Outro / Next steps -->
      <section>
        <h2>You're all set 🎉</h2>
        <ol>
          <li class="fragment">Commit this <code>index.html</code> to your GitHub repo.</li>
          <li class="fragment">Enable GitHub Pages from the repo settings.</li>
          <li class="fragment">Open your GitHub Pages URL and present!</li>
        </ol>
        <p><strong>Contact: 23f3000916@ds.study.iitm.ac.in</strong></p>
        <aside class="notes">Wrap up and share the URL with the audience.</aside>
      </section>

    </div>
  </div>

  <!-- Reveal core & plugins -->
  <script src="https://unpkg.com/reveal.js@5/dist/reveal.js"></script>
  <script src="https://unpkg.com/reveal.js@5/plugin/markdown/markdown.js"></script>
  <script src="https://unpkg.com/reveal.js@5/plugin/notes/notes.js"></script>
  <script src="https://unpkg.com/reveal.js@5/plugin/highlight/highlight.js"></script>
  <!-- Math plugin (KaTeX) -->
  <script src="https://unpkg.com/reveal.js@5/plugin/math/math.js"></script>

  <script>
    Reveal.initialize({
      hash: true,
      slideNumber: true,
      plugins: [ RevealMarkdown, RevealNotes, RevealHighlight, RevealMath.KaTeX ],
      // Optional: Highlight.js options
      highlight: {
        // auto-detect languages in <code> blocks
      },
      // Optional: KaTeX options
      math: {
        // KaTeX is bundled by the plugin via CDN automatically
        // You can pass KaTeX options here if needed
      }
    });
  </script>
</body>
</html>
