# Exercise 2: Rank Your Results (TF-IDF and BM25)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-ayesha-seecs/ir-course-exercises/blob/main/IR_Exercises_Colab.ipynb)

**Goal:** Move from Boolean (yes/no) retrieval to ranked retrieval using TF-IDF and BM25 scoring.

**Concepts:** term frequency (TF) · inverse document frequency (IDF) · TF-IDF · BM25 · ranked retrieval

**Dataset:** the same 20 documents from Exercise 1.

**File to complete:** [`starter.py`](starter.py) (imports `preprocess()` from `exercise1/starter.py`, so finish Exercise 1 first). Run: `python exercise2/starter.py`

## Worked example (query "cat dog")

Docs: 1 = "cat sat mat", 2 = "dog sat log", 3 = "cat dog played". N = 3, df(cat) = df(dog) = 2, IDF = ln(3/2) = 0.405.

| Doc | cat TF-IDF | dog TF-IDF | Total |
|:--|:--|:--|:--|
| 1 | 0.405 | 0 | 0.405 |
| 2 | 0 | 0.405 | 0.405 |
| 3 | 0.405 | 0.405 | 0.810 |

Ranking: Doc 3 > Doc 1 = Doc 2. (Note: the lecture uses the natural log.)

## Tasks

### Part A: Compute TF-IDF (60 min)
1. Compute TF (raw count). 2. Compute IDF = log(N / df). 3. Compute TF-IDF = TF × IDF. 4. Store `tfidf_scores[doc_id][term] = score`.

### Part B: Rank Documents (45 min)
1. Write `rank_tfidf(query)`: preprocess the query, sum TF-IDF of query terms per document, return a sorted list of `(doc_id, score)`.
2. Test: `"cat dog"`, `"sat mat"`, `"played"`.

### Part C: Implement BM25 (60 min)

```
BM25(q, d) = Σ IDF(qi) × (f(qi, d) × (k1 + 1)) / (f(qi, d) + k1 × (1 − b + b × |d| / avgdl))
k1 = 1.2, b = 0.75
```
1. Write `rank_bm25(query)`. 2. Compare BM25 vs TF-IDF.

## Deliverable
Python script + table + 3–4 sentence analysis (use [`../REPORT_TEMPLATE.md`](../REPORT_TEMPLATE.md)).

## Bonus (+2%)
Query term weighting — `rank_bm25_weighted()` stub.

## Why this exercise
TF-IDF and BM25 are the backbone of classical IR and still used in hybrid systems. BM25 is the default baseline in modern IR research (e.g. the [BEIR benchmark](https://github.com/beir-cellar/beir)); all neural models must beat it.
