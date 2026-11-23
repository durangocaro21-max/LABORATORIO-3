"""Installation script of the project (``pip install -e .``)."""
from setuptools import find_packages, setup

setup(
    name="tomotherapy-qa-pipeline",
    version="1.0.0",
    description="Pipeline for the detection of dosimetric errors (noise, shift, output) in dose images "
                "of helical TomoTherapy QA (ArcCHECK-inspired, synthetic data).",
    author="Dary Luz Durango Caro",
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.9",
    install_requires=["numpy", "pandas", "scipy", "matplotlib", "seaborn", "scikit-learn"],
    extras_require={"selection": ["skrebate", "mrmr-selection"], "dev": ["pytest", "jupyter"]},
)
