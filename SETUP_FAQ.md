# Setup Guide and FAQ

## Option 1: Google Colab (no installation)
1. Open the notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dr-ayesha-seecs/ir-course-exercises/blob/main/IR_Exercises_Colab.ipynb)
2. Run the first cell — it clones this repository into Colab.
3. Open the file browser (folder icon on the left), double-click `ir-course-exercises/exercise1/starter.py` and edit it.
4. Run the notebook cell for that exercise. Colab files are deleted when the session ends — **download your edited `starter.py` files** (right-click → Download) or push them to your own GitHub fork.

## Option 2: Local (Windows / macOS / Linux)
Requires Python 3.8 or newer.
```bash
git clone https://github.com/dr-ayesha-seecs/ir-course-exercises.git
cd ir-course-exercises
python exercise1/starter.py      # run from the repository root
```
No packages are needed: everything uses the Python standard library. (`pip install -r requirements.txt` only installs Jupyter, if you want to run the notebook locally.)

## FAQ
**The starter prints empty lists / zeros.** Expected — the TODO functions return empty placeholders until you implement them.

**`FileNotFoundError: documents`** — run commands from the repository root, or keep the folder structure unchanged.

**Exercise 2 says it can't import `starter`.** Keep `exercise1/starter.py` in place; Exercises 2 and 3 import your `preprocess()` from it.

**Which log should I use?** Natural log (`math.log`) for IDF, as in the lecture example (ln(3/2) = 0.405). nDCG uses `math.log2`.

**My stemmer turns "played" into "play" and "sat" stays "sat". OK?** Yes. Always preprocess queries with the same `preprocess()` as documents.

**Can I use libraries such as NLTK, scikit-learn or rank_bm25?** The goal is to build things from scratch, so implement the required parts yourself. You may use them only to cross-check your results.

**How do I submit?** See "Submitting Work" in the main README.
