import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Jasmeet-102116124",
    version="0.0.0",
    description="TOPSIS implementation by Jasmeet Kaur",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Jasmeet-Kaur16/Topsis-Jasmeet-102116124",
    author="Jasmeet Kaur",
    author_email="jasmeet.k.2003@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "sys",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis.__main__:main",
        ],
    },
)