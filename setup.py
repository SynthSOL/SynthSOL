from setuptools import setup, find_packages

setup(
    name="synth_framework",
    version="1.0.0",
    description="A Solana-based AI framework for on-chain AI solutions",
    author="Anonymous",
    author_email="anonymous@example.com",
    packages=find_packages(),
    install_requires=[
        "solana>=0.21.0",
        "setuptools>=57.0.0"
    ],
    python_requires=">=3.7",
)
