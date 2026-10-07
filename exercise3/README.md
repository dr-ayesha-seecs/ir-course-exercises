# Exercise 3: Evaluate Your Search Engine

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-ayesha-seecs/ir-course-exercises/blob/main/IR_Exercises_Colab.ipynb)

**Goal:** Measure whether a search engine is good using standard IR metrics.

**Concepts:** relevance judgments (ground truth) · Precision, Recall · P@K, R@K · Average Precision (AP) · nDCG

**Dataset:** the same 20 documents from Exercises 1 and 2.

**File to complete:** [`starter.py`](starter.py) (uses Exercises 1 and 2). Run: `python exercise3/starter.py`

## Worked example: AP
Ranking D1 (rel), D2, D3 (rel), D4 (rel), D5; total relevant = 3.
P@1 = 1.0, P@3 = 0.667, P@4 = 0.75 → AP = (1/3)(1.0 + 0.667 + 0.75) = **0.806**

## Worked example: nDCG
Relevance D1=2, D2=0, D3=1, D4=2, D5=0; gain = 2^rel − 1, discount = log2(rank + 1).
DCG = 3/1 + 0 + 1/2 + 3/2.322 + 0 = 4.792; ideal 2,2,1,0,0 → IDCG = 3 + 1.893 + 0.5 = 5.393 → nDCG = **0.889**

Use these two examples to test your metric functions.

## Tasks

### Part A: Create Relevance Judgments (45 min)
1. Choose 5 queries. 2. Label each document: 2 (highly), 1 (somewhat), 0 (not). 3. Store `judgments[query][doc_id] = score` (template in `starter.py`).

### Part B: Implement Metrics (90 min)
Precision@K · Recall@K · AP · nDCG@K

### Part C: Evaluate and Compare (45 min)
1. Run TF-IDF and BM25 on your 5 queries. 2. Compute P@5, R@5, AP, nDCG@5. 3. Create a comparison table. 4. Write a 1-paragraph analysis.

## Deliverable
Python script + report (judgments, metrics, analysis) — use [`../REPORT_TEMPLATE.md`](../REPORT_TEMPLATE.md).

## Bonus (+2%)
MAP, MRR — stubs in `starter.py`.

## Why this matters
Every IR paper reports nDCG@10. You are learning the evaluation framework used at SIGIR, NeurIPS and ACL.
