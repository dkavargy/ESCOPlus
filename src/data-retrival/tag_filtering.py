# tag_filtering.py

import pandas as pd
import re

def load_tags(filepath):
    """
    Loads a CSV file containing Stack Overflow tags.
    Assumes columns: 'tag', 'count'
    """
    return pd.read_csv(filepath)


def remove_low_frequency_tags(df, min_count=1000):
    """
    Filters out tags with frequency below the specified threshold.
    """
    return df[df['count'] >= min_count].reset_index(drop=True)


def remove_non_skill_tags(df):
    """
    Removes tags that are unlikely to be technical skills (e.g., meta, vague).
    """
    stopwords = ['beginner', 'learning', 'book', 'homework', 'project', 'tools',
                 'tutorials', 'example', 'windows-7', 'windows-xp', 'error', 'help']

    def is_valid_tag(tag):
        return not any(sw in tag for sw in stopwords) and re.match(r'^[a-zA-Z0-9\.\+#\-]+$', tag)

    return df[df['tag'].apply(is_valid_tag)].reset_index(drop=True)


def normalize_tags(df):
    """
    Normalize tag formatting (e.g., lowercasing, stripping).
    """
    df['tag'] = df['tag'].str.strip().str.lower()
    return df


def filter_and_save(input_path, output_path, min_count=1000):
    """
    Runs the full filtering pipeline and saves to a new CSV.
    """
    df = load_tags(input_path)
    df = normalize_tags(df)
    df = remove_low_frequency_tags(df, min_count)
    df = remove_non_skill_tags(df)
    df.to_csv(output_path, index=False)
    print(f"Filtered tags saved to {output_path}. Total: {len(df)} tags.")


if __name__ == "__main__":
    input_file = "data/raw/stackoverflow_tags.csv"
    output_file = "data/processed/filtered_tags.csv"
    filter_and_save(input_file, output_file, min_count=1000)
