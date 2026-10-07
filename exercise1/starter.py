"""
Exercise 1: Build Your First Search Engine
Inverted index + Boolean retrieval (AND, OR, NOT).

Run from the repository root:   python exercise1/starter.py
Fill in every block marked TODO. Do not change function names/signatures:
Exercises 2 and 3 reuse them.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT, "documents")
STOPWORDS_FILE = os.path.join(ROOT, "stopwords.txt")


def load_documents(docs_dir=DOCS_DIR):
    """Return {doc_id: text}, e.g. {"doc01": "The cat sat ..."}. (Provided.)"""
    docs = {}
    for name in sorted(os.listdir(docs_dir)):
        if name.endswith(".txt"):
            with open(os.path.join(docs_dir, name), encoding="utf-8") as f:
                docs[name[:-4]] = f.read()
    return docs


def load_stopwords(path=STOPWORDS_FILE):
    """Return a set of stopwords. (Provided.)"""
    with open(path, encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


STOPWORDS = load_stopwords()


# ---------------------------------------------------------------- Part A
def preprocess(text):
    """Return a list of tokens.

    TODO:
      1. lowercase the text
      2. split into tokens (hint: drop punctuation first)
      3. remove stopwords (STOPWORDS)
      4. simple stemming: remove trailing "s", "ing", "ed"
    """
    tokens = []
    # TODO: your code here
    return tokens


# ---------------------------------------------------------------- Part B
def build_inverted_index(docs):
    """Return {term: sorted list of doc_ids}.

    TODO: for each document, preprocess it and add its ID to each term's posting list.
    """
    inverted_index = {}
    # TODO: your code here
    return inverted_index


# ---------------------------------------------------------------- Part C
def AND(index, t1, t2):
    """Docs containing both t1 and t2. TODO"""
    return []


def OR(index, t1, t2):
    """Docs containing t1 or t2. TODO"""
    return []


def NOT(index, t, all_doc_ids):
    """Docs NOT containing t. TODO"""
    return []


def term(t):
    """Preprocess a single query term so it matches the index (e.g. 'played' -> stem)."""
    toks = preprocess(t)
    return toks[0] if toks else t.lower()


# ---------------------------------------------------------------- Bonus (+2%)
def phrase_search(docs, phrase):
    """BONUS: return doc_ids containing the exact phrase (store token positions). TODO"""
    return []


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    # Part A
    print("\nFirst 20 tokens of doc01:", preprocess(docs["doc01"])[:20])

    # Part B
    index = build_inverted_index(docs)
    print("\nPosting lists:")
    for t in ["cat", "dog", "sat", "mat", "log"]:
        print(f"  {t!r}: {index.get(term(t), [])}")

    # Part C
    all_ids = sorted(docs)
    print('\n"cat" AND "sat"     :', AND(index, term("cat"), term("sat")))
    print('"cat" OR "dog"      :', OR(index, term("cat"), term("dog")))
    sat_not_dog = sorted(set(index.get(term("sat"), [])) & set(NOT(index, term("dog"), all_ids)))
    print('"sat" AND NOT "dog" :', sat_not_dog)
