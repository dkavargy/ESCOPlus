# clean_esco.py

import pandas as pd
import re


def load_esco_skills(filepath):
    """
    Loads ESCO skills from a CSV file.
    Assumes the file has a column named 'skill'.
    """
    return pd.read_csv(filepath)


def clean_skill_name(skill):
    """
    Cleans and normalizes a single skill name.
    """
    skill = skill.lower().strip()  # Lowercase and remove whitespace
    skill = re.sub(r'\s+', ' ', skill)  # Normalize whitespace
    skill = re.sub(r'[^\w\-\+\#\. ]', '', skill)  # Remove non-alphanumeric characters except common tech symbols
    return skill


def clean_esco_dataframe(df, skill_column='skill'):
    """
    Cleans an ESCO dataframe column and drops duplicates.
    """
    df[skill_column] = df[skill_column].astype(str).apply(clean_skill_name)
    df = df.drop_duplicates(subset=[skill_column])
    df = df[df[skill_column] != '']  # Remove empty entries
    return df.reset_index(drop=True)


def save_cleaned_esco(df, output_path):
    """
    Saves the cleaned ESCO skill list to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned ESCO skills to {output_path}")


if __name__ == "__main__":
    input_path = "data/raw/esco_skills.csv"
    output_path = "data/processed/esco_skills_cleaned.csv"
    
    df = load_esco_skills(input_path)
    df_clean = clean_esco_dataframe(df, skill_column='skill')
    save_cleaned_esco(df_clean, output_path)
