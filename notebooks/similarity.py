# similarity_measures.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_tfidf_matrix(terms_1, terms_2):
    """
    Computes the combined TF-IDF matrix for two lists of terms.
    """
    combined_terms = list(set(terms_1 + terms_2))
    vectorizer = TfidfVectorizer().fit(combined_terms)
    tfidf_matrix_1 = vectorizer.transform(terms_1)
    tfidf_matrix_2 = vectorizer.transform(terms_2)
    return tfidf_matrix_1, tfidf_matrix_2


def compute_cosine_sim_matrix(tfidf_matrix_1, tfidf_matrix_2):
    """
    Computes cosine similarity between two TF-IDF matrices.
    """
    return cosine_similarity(tfidf_matrix_1, tfidf_matrix_2)


def get_top_similar_pairs(esco_skills, non_esco_skills, top_n=1, threshold=0.7):
    """
    Computes cosine similarity between ESCO and non-ESCO skills and returns
    top matching pairs above a similarity threshold.
    """
    tfidf_esco, tfidf_non_esco = compute_tfidf_matrix(esco_skills, non_esco_skills)
    sim_matrix = compute_cosine_sim_matrix(tfidf_esco, tfidf_non_esco)

    results = []
    for i, esco_skill in enumerate(esco_skills):
        similarities = list(enumerate(sim_matrix[i]))
        top_matches = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]
        for j, score in top_matches:
            if score >= threshold:
                results.append({
                    "ESCO Skill": esco_skill,
                    "Non-ESCO Skill": non_esco_skills[j],
                    "Similarity Score": round(score, 4)
                })
    return pd.DataFrame(results)


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("data/processed/skill_pairs.csv")  # Must contain 'ESCOskill', 'noESCO'
    esco = df['ESCOskill'].dropna().unique().tolist()
    non_esco = df['noESCO'].dropna().unique().tolist()

    matches = get_top_similar_pairs(esco, non_esco, top_n=1, threshold=0.7)
    print(matches.head())
