import pickle
import faiss

from sentence_transformers import SentenceTransformer


VECTOR_PATH = "vector_db/aws_index.faiss"
METADATA_PATH = "vector_db/metadata.pkl"


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


index = faiss.read_index(
    VECTOR_PATH
)


with open(
    METADATA_PATH,
    "rb"
) as file:
    metadata = pickle.load(file)



def retrieve_context(query, k=3):

    query_embedding = model.encode(
        [query]
    )


    distances, indices = index.search(
        query_embedding,
        k
    )


    context = ""

    sources = []


    for idx in indices[0]:

        document = metadata[idx]


        context += (
            "\n\n"
            + document["text"]
        )


        sources.append(
            {
                "service": document["service"],
                "url": document["url"]
            }
        )


    return context, sources