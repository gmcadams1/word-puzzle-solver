import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="word-puzzle-solver-gmcadams1", # Replace with your own username
    version="0.0.1",
    author="Gregory McAdams",
    author_email="gmcadams1@comcast.net",
    description="Relatively efficient word puzzle solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gmcadams1/word-puzzle-solver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)