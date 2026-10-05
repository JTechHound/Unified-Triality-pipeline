# [REPAIRED 2026-10-04] joined import line split ("import osfrom setuptools..." in source).
import os
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="unified-triality-pipeline",
    version="6.0.0",
    author="u/Mikey-506",
    author_email="mikey506.systems@example.com",
    description="Advanced non-equilibrium open quantum systems engineering simulation framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    project_urls={
        "Bug Tracker": "https://github.com/issues",
        "Documentation": "https://github.com/wiki",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "qutip>=4.7.1",
    ],
)
