from collections import defaultdict
import random
import pandas as pd
import ast

df = pd.read_csv("bookSet.csv")
df["Genres"] = df["Genres"].apply(ast.literal_eval)
books = []
for index, row in df.iterrows():
    books.append({
        "title" : row["Title"],
        "genres" : set(row["Genres"]),
        "image" : row["cover"]
    })

users = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9", "user10"]
user_books = {}
for user in users:
    user_books[user] = random.sample(books, 10) 


def genre_query_boost(book_genres, query_genres, boost_weight=0.5):
    if not query_genres:
        return 0
    overlap = book_genres & query_genres
    return boost_weight * (len(overlap) / len(query_genres))

#weighted user profile
def build_weighted_user_profile(user_books, user):
    genre_count = defaultdict(int) 
    for book in user_books[user]:
        for genre in book["genres"]:
            genre_count[genre] += 1
    return dict(genre_count)

#create a list of all genres user has read
def get_user_genres(user_books, user):
    genres = set()
    for book in user_books[user]:
        genres.update(book["genres"])
    return genres

#add weights of matching genres and then normalize by total genre weight
def weighted_genre_similarity(user_profile, book_genres):
    score = 0
    total_weight = sum(user_profile.values())

    for genre in book_genres:
        score += user_profile.get(genre, 0)

    return score / total_weight if total_weight != 0 else 0


def recommend_books_custom(
        books, 
        user_books, 
        target_user, 
        query_genres=None, 
        top_n=5):
    
    user_profile = build_weighted_user_profile(user_books, target_user)
    read_titles = {book["title"] for book in user_books[target_user]}

    scored_books = []
    for book in books:
        if book["title"] not in read_titles:
            base_score = weighted_genre_similarity( 
                user_profile, book["genres"]
            )

            boost = genre_query_boost(book["genres"], query_genres)
            final_score = base_score + boost

            if final_score > 0:
                scored_books.append({
                    "title": book["title"],
                    "image": book["image"],
                    "score": round(final_score, 3),
                    "matched_genres": list(book["genres"] & query_genres)
                })

    scored_books.sort(key=lambda x: x["score"], reverse=True)
    return scored_books[:top_n]


#take explicitly defined genres.
user_input = input("Enter preferred genres (comma separated): ")
query_genres = {
    g.strip().title()
    for g in user_input.split(",")
    if g.strip()
}


recommendations = recommend_books_custom(
    books,
    user_books,
    target_user="user1",
    query_genres=query_genres
)

print("\n Recommendations based on your preferences:\n")

for rec in recommendations:
    print(f"📖 {rec['title']}")
    if rec["matched_genres"]:
        print(f" Matches: {', '.join(rec['matched_genres'])}")
