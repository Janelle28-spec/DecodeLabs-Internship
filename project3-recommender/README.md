# AI Movie Recommender

## Description
A content-based recommendation system built in Python for the DecodeLabs AI internship. The user enters their interests, and the program matches them against a catalog of movies using a similarity score, then displays the top recommendations with the reasons they matched.

## What It Does
1. Takes user interests as input (comma-separated, for example `sci-fi, action`)
2. Cleans the input (lowercase, trimmed, unknown interests ignored)
3. Scores every movie using Jaccard similarity: shared tags divided by total unique tags
4. Ranks the movies and displays the top 3 with their match percentage and matching tags

## Example
Input:
```
Your interests: sci-fi, action
```

Output:
```
Top recommendations for you:
  1. The Matrix  (100% match)
     Matched on: action, sci-fi
  2. Inception  (67% match)
     Matched on: action, sci-fi
  3. Mad Max: Fury Road  (67% match)
     Matched on: action, sci-fi
```

## Technologies
- Python 3 (no external libraries required)

## How to Run
```
python recommender.py
```

Type your interests separated by commas, and type `quit` to exit.

## Key Learning
Recommendation engines compare user preferences with item attributes. Representing items as sets of tags makes similarity easy to calculate and easy to explain.