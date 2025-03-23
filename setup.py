from setuptools import setup, find_packages

setup(
    name='escoplus',
    version='0.1.0',
    description='A framework to enrich the ESCO taxonomy using skills extracted from Stack Overflow.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/escoplus-framework',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pandas>=1.5",
        "numpy>=1.23",
        "scikit-learn>=1.2",
        "matplotlib>=3.7",
        "seaborn>=0.12",
        "networkx>=3.1",
        "mlxtend>=0.22",
        "python-igraph>=0.10",
        "leidenalg>=0.10",
        "requests>=2.31",
        "streamlit>=1.25",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires='>=3.8',
)
