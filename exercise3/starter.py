"""
Exercise 3: Evaluate Your Search Engine

Run from the repository root:   python exercise3/starter.py
Reuses Exercises 1 and 2, so finish those first.
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "exercise2"))
sys.path.insert(0, os.path.join(ROOT, "exercise1"))
from starter import load_documents, preprocess  # noqa: E402  (exercise1)
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("ex2", os.path.join(ROOT, "exercise2", "starter.py"))
ex2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex2)

K = 5

# ---------------------------------------------------------------- Part A
# TODO: choose 5 queries and label EVERY document (doc01..doc20):
#   2 = highly relevant, 1 = somewhat relevant, 0 = not relevant
# Missing documents are treated as 0.
judgments = {
    "cat dog": {
        # "doc03": 2,
        # "doc01": 1,
    },
    # "query 2": {...},
    # ... 5 queries in total
}


# ---------------------------------------------------------------- Part B
def precision_at_k(ranking, rels, k):
    """ranking: [doc_id, ...]; rels: {doc_id: grade}. Relevant = grade > 0. TODO"""
    return 0.0


def recall_at_k(ranking, rels, k):
    """TODO"""
    return 0.0


def average_precision(ranking, rels):
    """AP = mean of P@i over the ranks i of relevant docs, divided by total relevant. TODO"""
    return 0.0


def ndcg_at_k(ranking, rels, k):
    """DCG uses gain (2^rel - 1) / log2(rank + 1), as in the lecture example. TODO"""
    return 0.0


# ---------------------------------------------------------------- Bonus (+2%)
def mean_average_precision(rankings, judgments):
    """BONUS: MAP over all queries. TODO"""
    return 0.0


def mrr(rankings, judgments):
    """BONUS: Mean Reciprocal Rank. TODO"""
    return 0.0


# ---------------------------------------------------------------- Part C
def evaluate(rank_fn):
    rows = {}
    for q, rels in judgments.items():
        ranking = [d for d, _ in rank_fn(q)]
        rows[q] = (precision_at_k(ranking, rels, K), recall_at_k(ranking, rels, K),
                   average_precision(ranking, rels), ndcg_at_k(ranking, rels, K))
    return rows


if __name__ == "__main__":
    docs = load_documents()
    docs_tokens = {d: preprocess(t) for d, t in docs.items()}
    tf = ex2.compute_tf(docs_tokens)
    idf = ex2.compute_idf(docs_tokens)
    tfidf_scores = ex2.compute_tfidf(tf, idf)
    systems = {
        "TF-IDF": lambda q: ex2.rank_tfidf(q, tfidf_scores),
        "BM25": lambda q: ex2.rank_bm25(q, docs_tokens, idf),
    }
    print(f"{'System':<8}{'Query':<20}{'P@5':>7}{'R@5':>7}{'AP':>7}{'nDCG@5':>8}")
    for name, fn in systems.items():
        rows = evaluate(fn)
        for q, (p, r, ap, nd) in rows.items():
            print(f"{name:<8}{q:<20}{p:>7.3f}{r:>7.3f}{ap:>7.3f}{nd:>8.3f}")
        if rows:
            m = [sum(v[i] for v in rows.values()) / len(rows) for i in range(4)]
            print(f"{name:<8}{'MEAN':<20}{m[0]:>7.3f}{m[1]:>7.3f}{m[2]:>7.3f}{m[3]:>8.3f}")
