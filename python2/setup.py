import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="a-parser-python2",
    version="0.0.1",
    author="bykovvvladlen",
    author_email="bykovvvladlen@gmail.com",
    description="A-Parser API Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-parser/api-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
