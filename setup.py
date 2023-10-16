import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raghavnarula",  # Replace with your own username
    version="1.0.0",
    author="Atharva, Divit, Mrityunjay, Raghav",
    author_email="aaathorve@gmail.com",
    description="A recommendation engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raghavnarula/MovieRecommender",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
