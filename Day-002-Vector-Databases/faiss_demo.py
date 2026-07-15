import numpy as np
import faiss

# Create sample embeddings (5 vectors of dimension 4)
embeddings = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.8, 0.7, 0.6, 0.5],
    [0.2, 0.1, 0.4, 0.3],
    [0.9, 0.8, 0.7, 0.6],
    [0.4, 0.5, 0.6, 0.7]
], dtype="float32")

# Build FAISS index
index = faiss.IndexFlatL2(4)
index.add(embeddings)

# Query vector
query = np.array([[0.15, 0.25, 0.35, 0.45]], dtype="float32")

# Search top-2 nearest neighbors
distances, indices = index.search(query, 2)

print("Nearest indices:", indices)
print("Distances:", distances)