<h2><a href="https://codeforces.com/contest/1790/problem/A" target="_blank" rel="noopener noreferrer">1790A — Polycarp and the Day of Pi</a></h2>

| | |
|---|---|
| **Difficulty** | 800 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1790A](https://codeforces.com/contest/1790/problem/A) |

## Topics
`implementation` `math` `strings`

---

## Problem Statement

<div class="header"><div class="title">A. Polycarp and the Day of Pi</div><div class="time-limit"><div class="property-title">time limit per test</div>1 second</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>On March 14, the day of the number $$$\pi$$$ is celebrated all over the world. This is a very important mathematical constant equal to the ratio of the circumference of a circle to its diameter.</p><p>Polycarp was told at school that the number $$$\pi$$$ is irrational, therefore it has an infinite number of digits in decimal notation. He wanted to prepare for the Day of the number $$$\pi$$$ by memorizing this number as accurately as possible.</p><p>Polycarp wrote out all the digits that he managed to remember. For example, if Polycarp remembered $$$\pi$$$ as $$$3.1415$$$, he wrote out <span class="tex-font-style-tt">31415</span>.</p><p>Polycarp was in a hurry and could have made a mistake, so you decided to check how many first digits of the number $$$\pi$$$ Polycarp actually remembers correctly.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input data contains the single integer $$$t$$$ ($$$1 \le t \le 10^3$$$) — the number of test cases in the test. </p><p>Each test case is described by a single string of digits $$$n$$$, which was written out by Polycarp.</p><p>The string $$$n$$$ contains up to $$$30$$$ digits.</p></div><div class="output-specification"><div class="section-title">Output</div><p>Output $$$t$$$ integers, each of which is the answer to the corresponding test case, that is how many first digits of the number $$$\pi$$$ Polycarp remembers correctly.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id004229278590184138" id="id004416311594483895" class="input-output-copier">Copy</div></div><pre data-content="9
000
3
4141592653
141592653589793238462643383279
31420
31415
314159265358
27182
314159265358979323846264338327
" id="id004229278590184138"><div class="test-example-line test-example-line-even test-example-line-0">9</div><div class="test-example-line test-example-line-odd test-example-line-1">000</div><div class="test-example-line test-example-line-even test-example-line-2">3</div><div class="test-example-line test-example-line-odd test-example-line-3">4141592653</div><div class="test-example-line test-example-line-even test-example-line-4">141592653589793238462643383279</div><div class="test-example-line test-example-line-odd test-example-line-5">31420</div><div class="test-example-line test-example-line-even test-example-line-6">31415</div><div class="test-example-line test-example-line-odd test-example-line-7">314159265358</div><div class="test-example-line test-example-line-even test-example-line-8">27182</div><div class="test-example-line test-example-line-odd test-example-line-9">314159265358979323846264338327</div></pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id00004455653641480484" id="id008923365897603236" class="input-output-copier">Copy</div></div><pre id="id00004455653641480484">0
1
0
0
3
5
12
0
30
</pre></div></div></div>