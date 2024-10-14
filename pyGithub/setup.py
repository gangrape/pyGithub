from setuptools import setup, find_packages

setup(
    name="pyGithub",
    version="0.1.0",
    author="Akami Yen",
    author_email="none@none.com",
    description="A simple Github API wrapper",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)