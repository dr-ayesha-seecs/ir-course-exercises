"""
Exercise 2: Rank Your Results (TF-IDF and BM25)

Run from the repository root:   python exercise2/starter.py
Reuses load_documents() and preprocess() from Exercise 1, so finish
exercise1/starter.py first.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "exercise1"))
from starter import load_documents, preprocess  # noqa: E402

K1 = 1.2
B = 0.75


# ---------------------------------------------------------------- Part A
def compute_tf(docs_tokens):
    """Return tf[doc_id][term] = raw count. TODO"""
    tf = {doc_id: {} for doc_id in docs_tokens}
    # TODO
    return tf


def compute_idf(docs_tokens):
    """Return idf[term] = log(N / df) (natural log, as in the lecture). TODO"""
    idf = {}
    # TODO
    return idf


def compute_tfidf(tf, idf):
    """Return tfidf_scores[doc_id][term] = TF x IDF. TODO"""
    tfidf_scores = {doc_id: {} for doc_id in tf}
    # TODO
    return tfidf_scores


# ---------------------------------------------------------------- Part B
def rank_tfidf(query, tfidf_scores):
    """Preprocess the query, sum TF-IDF of query terms per doc,
    return [(doc_id, score), ...] sorted by score descending. TODO"""
    return []


# ---------------------------------------------------------------- Part C
def rank_bm25(query, docs_tokens, idf, k1=K1, b=B):
    """BM25(q,d) = sum_i IDF(qi) * f(qi,d)*(k1+1) / (f(qi,d) + k1*(1 - b + b*|d|/avgdl))
    Return [(doc_id, score), ...] sorted descending. TODO"""
    return []


# ---------------------------------------------------------------- Bonus (+2%)
def rank_bm25_weighted(query_weights, docs_tokens, idf):
    """BONUS: query term weighting, e.g. {"cat": 2.0, "dog": 1.0}. TODO"""
    return []


def print_table(query, tfidf_rank, bm25_rank, k=5):
    print(f"\nQuery: {query!r}")
    print(f"  {'Rank':<5}{'TF-IDF doc':<12}{'score':>8}   {'BM25 doc':<12}{'score':>8}")
    for i in range(k):
        a = tfidf_rank[i] if i < len(tfidf_rank) else ("-", 0.0)
        c = bm25_rank[i] if i < len(bm25_rank) else ("-", 0.0)
        print(f"  {i+1:<5}{a[0]:<12}{a[1]:>8.3f}   {c[0]:<12}{c[1]:>8.3f}")


if __name__ == "__main__":
    docs = load_documents()
    docs_tokens = {d: preprocess(t) for d, t in docs.items()}
    tf = compute_tf(docs_tokens)
    idf = compute_idf(docs_tokens)
    tfidf_scores = compute_tfidf(tf, idf)
    for q in ["cat dog", "sat mat", "played"]:
        print_table(q, rank_tfidf(q, tfidf_scores), rank_bm25(q, docs_tokens, idf))
