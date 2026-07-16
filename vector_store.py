import os
import json
import pickle

import faiss

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


DOC_PATH = "data/processed_docs"

VECTOR_PATH = "vector_db/aws_index.faiss"

METADATA_PATH = "vector_db/metadata.pkl"


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



def load_documents():

    documents = []


    for file_name in os.listdir(DOC_PATH):

        if file_name.endswith(".json"):

            path = os.path.join(
                DOC_PATH,
                file_name
            )


            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                document = json.load(
                    file
                )


                documents.append(
                    {
                        "service": document["service"],
                        "url": document["url"],
                        "content": document["content"]
                    }
                )


    return documents




def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=700,

        chunk_overlap=100

    )


    chunks = []


    for document in documents:


        split_texts = splitter.split_text(
            document["content"]
        )


        for text in split_texts:


            chunks.append(

                {

                    "service": document["service"],

                    "url": document["url"],

                    "text": text

                }

            )


    return chunks





def build_vector_store():


    print("Loading documents...")


    documents = load_documents()


    print(
        f"Loaded {len(documents)} documents"
    )



    print("Creating chunks...")


    chunks = create_chunks(
        documents
    )


    print(
        f"Created {len(chunks)} chunks"
    )



    texts = [

        chunk["text"]

        for chunk in chunks

    ]



    print(
        "Generating embeddings..."
    )



    embeddings = embedding_model.encode(

        texts,

        show_progress_bar=True

    )



    dimension = embeddings.shape[1]



    index = faiss.IndexFlatL2(

        dimension

    )



    index.add(

        embeddings

    )



    os.makedirs(

        "vector_db",

        exist_ok=True

    )



    faiss.write_index(

        index,

        VECTOR_PATH

    )



    with open(

        METADATA_PATH,

        "wb"

    ) as file:


        pickle.dump(

            chunks,

            file

        )



    print(
        "Vector database created successfully!"
    )




if __name__ == "__main__":

    build_vector_store()