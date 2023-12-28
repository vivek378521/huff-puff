import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huff-puff",
    version="0.1.0",
    author="Vivek Khatri",
    author_email="vvk3785@gmail.com",
    description="Python package for file compression using Huffman coding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vivek378521/huff-puff",  # Replace with your GitHub repository URL
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
