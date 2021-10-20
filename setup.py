import setuptools
import pathlib


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name="revolut_api",
    version="0.1.9",
    author="olatokunbo ogunlade",
    author_email="olatokunboalege@gmail.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/olateekay/revolut-assesment",
    description="A simple api package",
    packages=setuptools.find_packages(),
    install_requires=["flask", "psycopg2-binary", "flask_sqlalchemy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)