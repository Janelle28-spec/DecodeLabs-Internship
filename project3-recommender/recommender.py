# ==========================================================
# DECODELABS AI PROJECT 3
# AI RECOMMENDATION LOGIC (Content-Based Filtering)
# ==========================================================

# ----------------------------------------------------------
# 1. ITEM CATALOG: each movie is described by its tags
# ----------------------------------------------------------
movies = {
    "Inception":           {"sci-fi", "thriller", "action"},
    "The Matrix":          {"sci-fi", "action"},
    "Interstellar":        {"sci-fi", "drama", "space"},
    "The Martian":         {"sci-fi", "space", "comedy"},
    "John Wick":           {"action", "thriller", "crime"},
    "Mad Max: Fury Road":  {"action", "adventure", "sci-fi"},
    "The Notebook":        {"romance", "drama"},
    "La La Land":          {"romance", "music", "drama"},
    "Superbad":            {"comedy", "teen"},
    "The Hangover":        {"comedy", "adventure"},
    "Get Out":             {"horror", "thriller"},
    "A Quiet Place":       {"horror", "thriller", "sci-fi"},
    "Coco":                {"animation", "music", "family"},
    "Toy Story":           {"animation", "comedy", "family"},
}

# All tags that exist in the catalog (used to validate user input)
all_tags = sorted(set().union(*movies.values()))


# ----------------------------------------------------------
# 2. SIMILARITY FUNCTION (Jaccard similarity)
#    shared tags / total unique tags -> a score from 0 to 1
# ----------------------------------------------------------
def similarity(user_interests, item_tags):
    shared = user_interests & item_tags
    total = user_interests | item_tags
    return len(shared) / len(total)


# ----------------------------------------------------------
# 3. RECOMMENDATION ENGINE
# ----------------------------------------------------------
def recommend(user_interests, top_n=3):
    scored = []
    for title, tags in movies.items():
        score = similarity(user_interests, tags)
        if score > 0:
            scored.append((title, score, user_interests & tags))

    # Highest score first
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:top_n]


# ----------------------------------------------------------
# 4. INPUT HANDLING
# ----------------------------------------------------------
def get_interests(raw_text):
    # Sanitize: lowercase, split on commas, trim spaces
    wanted = {part.strip().lower() for part in raw_text.split(",")}
    wanted.discard("")

    valid = wanted & set(all_tags)
    unknown = wanted - set(all_tags)
    return valid, unknown


# ----------------------------------------------------------
# 5. MAIN PROGRAM
# ----------------------------------------------------------
def run_recommender():
    print("=" * 50)
    print("      DECODELABS MOVIE RECOMMENDER")
    print("=" * 50)
    print("\nAvailable interests:")
    print(", ".join(all_tags))
    print("\nEnter your interests separated by commas.")
    print("Type 'quit' to exit.\n")

    while True:
        raw = input("Your interests: ")

        if raw.strip().lower() in {"quit", "exit", "bye"}:
            print("\nGoodbye! Enjoy your movies.")
            break

        interests, unknown = get_interests(raw)

        if unknown:
            print("Ignored (not in catalog):", ", ".join(sorted(unknown)))

        if not interests:
            print("Please enter at least one valid interest.\n")
            continue

        results = recommend(interests)

        if not results:
            print("No matches found. Try other interests.\n")
            continue

        print("\nTop recommendations for you:")
        for rank, (title, score, matched) in enumerate(results, start=1):
            print(f"  {rank}. {title}  ({score * 100:.0f}% match)")
            print(f"     Matched on: {', '.join(sorted(matched))}")
        print()


if __name__ == "__main__":
    run_recommender()