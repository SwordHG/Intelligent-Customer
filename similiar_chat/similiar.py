from langchain.vectorstores import FAISS
from similiar_chat.data_process import data_process
from server.knowledge_base.utils import load_embeddings
from configs.model_config import (EMBEDDING_MODEL, EMBEDDING_DEVICE)
# from langchain.embeddings.huggingface import HuggingFaceEmbeddings
# from similiar_chat.model_config import embedding_model_dict, EMBEDDING_MODEL

datas, QA_dict = data_process('./similiar_chat/train.json')

embeddings = load_embeddings(EMBEDDING_MODEL, EMBEDDING_DEVICE)

faiss_index = FAISS.from_texts(datas, embeddings)


def similiar_compute(faiss_model, dict_list, query):

    # docs = faiss_model.similarity_search(query, k=1)
    docs = faiss_model.similarity_search_with_score(query, k=2)

    title = []
    score = []
    for doc in docs:
        score.append(doc[1])
        title.append(dict(doc[0]).get('page_content'))

    results = list(zip(title, score))

    answer = dict_list.get(title[0])
    return answer, score[0]


if __name__ == "__main__":
    similiar_compute("继续教育专项如何扣除呢？")