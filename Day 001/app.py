from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Artificial Intelligence is amazing.",
    "Machine Learning is a subset of AI.",
    "Dogs are wonderful pets."
]

query = ["AI and Machine Learning"]

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(documents + query)

similarity = cosine_similarity(vectors[-1], vectors[:-1])

print(similarity)