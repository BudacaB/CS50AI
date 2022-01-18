import csv

names = {}
people = {}
movies = {}

# Load people
with open(f"small/people.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        people[row["id"]] = {
            "name": row["name"],
            "birth": row["birth"],
            "movies": set()
        }
        if row["name"].lower() not in names:
            names[row["name"].lower()] = {row["id"]}
        else:
            names[row["name"].lower()].add(row["id"])

# Load movies
with open(f"small/movies.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movies[row["id"]] = {
            "title": row["title"],
            "year": row["year"],
            "stars": set()
        }

# Load stars
with open(f"small/stars.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            people[row["person_id"]]["movies"].add(row["movie_id"])
            movies[row["movie_id"]]["stars"].add(row["person_id"])
        except KeyError:
            pass

movie_ids = people['102']['movies']
neighbors = set()
for movie_id in movie_ids:
    for person_id in movies[movie_id]["stars"]:
        neighbors.add((movie_id, person_id))

print(people['102']['movies'])
print(neighbors)