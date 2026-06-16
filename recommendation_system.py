import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "User":        ["Alice", "Bob", "Charlie", "David", "Eve",
                    "Alice", "Bob", "Charlie", "David", "Eve",
                    "Alice", "Bob", "Charlie", "David", "Eve",
                    "Alice", "Bob", "Charlie", "David", "Eve",
                    "Alice", "Bob", "Charlie", "David", "Eve"],

    "Movie":       ["Imaikka Nodigal", "Imaikka Nodigal", "Imaikka Nodigal", "Imaikka Nodigal", "Imaikka Nodigal",
                    "Master", "Master", "Master", "Master", "Master",
                    "Poojai", "Poojai", "Poojai", "Poojai", "Poojai",
                    "Sarkar", "Sarkar", "Sarkar", "Sarkar", "Sarkar",
                    "Leo", "Leo", "Leo", "Leo", "Leo"],

    "Rating":      [5, 4, 0, 3, 5,
                    4, 0, 5, 4, 3,
                    5, 5, 4, 0, 4,
                    0, 3, 4, 5, 2,
                    3, 4, 0, 4, 5]
}

df = pd.DataFrame(data)

matrix = df.pivot_table(index="User", columns="Movie", values="Rating", fill_value=0)

print("=" * 55)
print("         🎬 Movie Recommendation System")
print("=" * 55)
print("\n📊 User-Movie Rating Matrix:\n")
print(matrix)

similarity = cosine_similarity(matrix)
similarity_df = pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

print("\n\n👥 User Similarity Scores:\n")
print(similarity_df.round(2))

def recommend(user, n=3):
    if user not in matrix.index:
        return f"❌ User '{user}' not found! Available users: {list(matrix.index)}"

    sim_scores = similarity_df[user].drop(user)

    unwatched = matrix.loc[user][matrix.loc[user] == 0].index.tolist()

    if not unwatched:
        return f"✅ {user} has watched all movies!"

    scores = {}
    for movie in unwatched:
        weighted_sum = 0
        sim_sum = 0
        for other_user in sim_scores.index:
            rating = matrix.loc[other_user, movie]
            if rating > 0:
                weighted_sum += sim_scores[other_user] * rating
                sim_sum += sim_scores[other_user]
        if sim_sum > 0:
            scores[movie] = weighted_sum / sim_sum

    if not scores:
        return "⚠️ No recommendations found!"

    recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]
    return recommended

print("\n\n🎯 Available Users: Alice, Bob, Charlie, David, Eve")

while True:
    print("\n" + "─" * 55)
    user = input("Enter username (or 'quit' to exit): ").strip().title()
    if user.lower() == "quit":
        print("\n👋 Thanks for using the Recommendation System!")
        break
    try:
        n = int(input("How many recommendations do you want? (1-5): "))
        if n < 1 or n > 5:
            print("⚠️ Please enter a number between 1 and 5!")
            continue
    except ValueError:
        print("⚠️ Invalid input! Enter a number.")
        continue
    result = recommend(user, n)
    if isinstance(result, str):
        print(f"\n{result}")
    else:
        print(f"\n🎬 Top {n} Movie Recommendations for {user}:\n")
        for i, (movie, score) in enumerate(result, 1):
            print(f"  {i}. {movie}  (Score: {score:.2f})")
