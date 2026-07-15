What is a Vector Database?

A vector database stores embeddings (numerical vectors) instead of plain text. It enables fast semantic search by finding vectors that are closest to a query vector.

Traditional Database vs Vector Database

| Traditional Database        | Vector Database                 |
| --------------------------- | ------------------------------- |
| Stores text, numbers, dates | Stores high-dimensional vectors |
| Exact matching              | Semantic similarity search      |
| SQL queries                 | Nearest Neighbor Search         |
| Best for structured data    | Best for AI applications        |


Popular Vector Databases

| Database | Open Source | Cloud | Best Use Case             |
| -------- | ----------- | ----- | ------------------------- |
| FAISS    | ✅           | ❌     | Local applications        |
| ChromaDB | ✅           | ❌     | RAG prototypes            |
| Pinecone | ❌           | ✅     | Production cloud AI       |
| Milvus   | ✅           | ✅     | Large-scale vector search |
| Weaviate | ✅           | ✅     | Enterprise AI             |


Architecture:

```mermaid
flowchart LR

A[User Query]
    --> B[Embedding Model]

B --> C[Vector Database]

C --> D[Nearest Neighbor Search]

D --> E[Top-k Documents]

E --> F[LLM]

F --> G[Final Response]
```