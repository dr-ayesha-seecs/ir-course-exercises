# Exercise 1: Build Your First Search Engine

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-ayesha-seecs/ir-course-exercises/blob/main/IR_Exercises_Colab.ipynb)

**Goal:** Understand how a search engine works by building an inverted index and Boolean retrieval system from scratch.

**Concepts:** documents, terms, tokens · text preprocessing (lowercasing, tokenization, stopword removal, stemming) · inverted index · Boolean retrieval (AND, OR, NOT)

**Dataset:** the 20 plain text files in [`../documents/`](../documents) and [`../stopwords.txt`](../stopwords.txt).

**File to complete:** [`starter.py`](starter.py). Run it from the repository root: `python exercise1/starter.py`

## Worked example

```
Doc 1: "The cat sat on the mat"   -> ["cat", "sat", "mat"]
Doc 2: "The dog sat on the log"   -> ["dog", "sat", "log"]
Doc 3: "The cat and dog played"   -> ["cat", "dog", "played"]

Inverted index:
"cat": [1, 3]   "sat": [1, 2]   "mat": [1]
"dog": [2, 3]   "log": [2]      "played": [3]
```

## Tasks

### Part A: Text Preprocessing (30 min)
1. Load all documents (`load_documents()` is provided).
2. Write `preprocess(text)` that lowercases, splits into tokens, removes stopwords (`stopwords.txt`) and applies simple stemming (remove trailing "s", "ing", "ed").
3. Print the first 20 tokens of one preprocessed document.

### Part B: Build Inverted Index (45 min)
1. Create `inverted_index`: term → list of doc IDs.
2. For each document, add its ID to each term's posting list.
3. Print posting lists for 5 terms.

### Part C: Boolean Retrieval (45 min)
1. Implement `AND(t1, t2)`, `OR(t1, t2)`, `NOT(t)`.
2. Test: `"cat" AND "sat"`, `"cat" OR "dog"`, `"sat" AND NOT "dog"`.

## Deliverable
Python script + screenshot of posting lists and query results.

## Bonus (+2%)
Phrase search (store token positions) — `phrase_search()` stub in `starter.py`.

## Why this matters
Google's index is an inverted index. You are building the same data structure.

## Self-check
Your stemmed terms may differ slightly from others' (e.g. `"played"` → `"play"`); that is fine as long as queries are preprocessed the same way as documents (the provided `term()` helper does this).
