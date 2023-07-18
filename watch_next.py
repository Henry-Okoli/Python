import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

# Function to compute similarity score between two movie descriptions
def compute_similarity(movie_desc1, movie_desc2):
    doc1 = nlp(movie_desc1)
    doc2 = nlp(movie_desc2)
    return doc1.similarity(doc2)

# Function to suggest the next movie based on similarity
def suggested_next_movie(watched_movie):
    with open('movies.txt', 'r') as file:
        lines = file.readlines()

    max_similarity = 0.0
    suggested_movie = None

    for i, line in enumerate(lines):
        movie_desc = line.strip()
        similarity = compute_similarity(watched_movie, movie_desc)

        if similarity > max_similarity:
            max_similarity = similarity
            if i + 1 < len(lines):
                suggested_movie = lines[i + 1].strip()

    return suggested_movie

# Example usage
watched_movie = "Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed."
next_movie = suggested_next_movie(watched_movie)

# If found, it returns the next movie description from the file. If no more movies are available, it returns None.
if next_movie:
    print("Next movie you can watch:", next_movie)
else:
    print("No more movies available.")


