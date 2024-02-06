import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"

REPO_NAME = "mlops-driven-airline-passenger-satisfaction"
AUTHOR_NAME = "shrikanth"
AUTHOR_EMAIL = "Shrikanthp04@gmail.com"
SRC_REPO = "airline-passenger-satisfaction"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for mlapp",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_NAME}p04/{REPO_NAME}",
    Project_urls={
        "Bug Tracker ":f"https://github.com/{AUTHOR_NAME}p04/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)