# ESCOPlus Framework

**ESCOPlus** is an open-source framework designed to enhance the ESCO taxonomy by integrating emerging digital skills extracted from community-driven platforms like Stack Overflow. It provides a data-driven, expert-validated extension to ESCO, supporting workforce development, job matching, and curriculum design in the evolving labor market.

## 🔍 Overview

ESCOPlus follows a three-phase methodology:

1. **VISION**: Extract skills from Stack Overflow using tag co-occurrence and frequency filtering.
2. **ACTION**: Apply association rule mining and cosine similarity to detect alternative and new skills.
3. **PLAN**: Validate skills with expert feedback and integrate them into a structured extension of the ESCO taxonomy.

![esco_plus_schemas.png](https://github.com/dkavargy/ESCOPlus/blob/main/esco_plus_schema.png)

## 📁 Project Structure
```
ESCOPLUS-FRAMEWORK/
│
├── README.md                     # Project overview, installation, usage
├── LICENSE                       # Open-source license (e.g., MIT, Apache 2.0)
├── requirements.txt              # Python dependencies
├── setup.py                      # Optional: for pip install
│
├── data/                         # Raw and processed datasets
│   ├── raw/
│   │   └── stack_overflow_tags.csv
│   ├── processed/
│   │   ├── esco_skills_cleaned.csv
│   │   └── cooccurrence_matrix.pkl
│   └── external/
│       └── esco_taxonomy.json
│
├── notebooks/                    # Jupyter notebooks for exploratory analysis
│   ├── 01_exploration.ipynb
│   └── 02_similarity_analysis.ipynb
│
├── src/                          # Core source code
│   ├── __init__.py
│   ├── config.py                 # Configuration constants (paths, thresholds)
│   ├── data_retrieval/           # Stack Overflow data mining
│   │   ├── __init__.py
│   │   ├── so_scraper.py
│   │   └── tag_filtering.py
│   │
│   ├── preprocessing/            # Cleaning and transforming data
│   │   ├── __init__.py
│   │   ├── clean_esco.py
│   │   └── normalize_skills.py
│   │
│   ├── algorithms/               # Skill extraction and taxonomy enrichment
│   │   ├── __init__.py
│   │   ├── association_rules.py
│   │   ├── similarity_measures.py
│   │   ├── skill_classifier.py
│   │   └── clustering.py
│   │
│   └── validation/
│       ├── __init__.py
│       ├── expert_review_loader.py
│       └── evaluation_metrics.py
│
├── gui/                          # Web interface or visualization frontend
│   ├── app.py                    # Streamlit or Flask app
│   ├── components/
│   │   ├── skill_explorer.py
│   │   └── taxonomy_view.py
│   └── static/
│       └── style.css
│
├── tests/                        # Unit tests
│   ├── test_similarity.py
│   ├── test_preprocessing.py
│   └── test_rules.py
│
└── docs/                         # Documentation and diagrams
    ├── architecture.md
    ├── methodology.md
    └── screenshots/
        └── gui_demo.png

```

## ⚙️ Key Features

- Skill extraction from Stack Overflow
- Taxonomy enrichment via association rules and cosine similarity
- Expert validation layer for added reliability
- Interactive GUI for skill exploration
- Modular and extendable architecture

## 📊 Technologies Used

- Python 3.x
- pandas, scikit-learn, numpy
- NetworkX, matplotlib
- Flask (for GUI)
- PostgreSQL (for taxonomy storage)

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/escoplus-framework.git
cd escoplus-framework
pip install -r requirements.txt
```

## 🖥️ Visual Interface

ESCOPlus also includes an intuitive web-based GUI to explore and validate skills. Users can:

- Browse ESCO and non-ESCO skills
- Visualize skill associations and similarity scores
- Review suggested alternative and new skills

### 📸 GUI Preview

![ESCOPlus GUI](gui_of_escoplus.png)



