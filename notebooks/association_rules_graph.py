# association_rules.py

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def prepare_transactions(df, skill_columns):
    """
    Converts a dataframe with multiple skill columns into a one-hot encoded format.
    """
    one_hot = pd.get_dummies(df[skill_columns].stack()).groupby(level=0).sum()
    return one_hot

def extract_frequent_itemsets(one_hot_df, min_support=0.01):
    """
    Applies the Apriori algorithm to find frequent skill combinations.
    """
    return apriori(one_hot_df, min_support=min_support, use_colnames=True)

def generate_association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6):
    """
    Extracts association rules from frequent itemsets based on the selected metric.
    """
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
    return rules

def filter_rules_by_esco(rules_df, esco_skills):
    """
    Filters rules where antecedents or consequents involve ESCO skills.
    """
    return rules_df[
        rules_df['antecedents'].apply(lambda x: any(i in esco_skills for i in x)) |
        rules_df['consequents'].apply(lambda x: any(i in esco_skills for i in x))
    ]

# Example usage
if __name__ == "__main__":
    # Example CSV format: columns = ['ESCOskill', 'noESCO']
    df = pd.read_csv("data/processed/skill_pairs.csv")
    skill_cols = ['ESCOskill', 'noESCO']

    one_hot_df = prepare_transactions(df, skill_cols)
    freq_items = extract_frequent_itemsets(one_hot_df)
    rules = generate_association_rules(freq_items)

    # Load known ESCO skills
    esco_list = df['ESCOskill'].dropna().unique().tolist()
    filtered_rules = filter_rules_by_esco(rules, esco_list)

    print(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())
