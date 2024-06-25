import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Mlops_mlflow"
AUTHOR_USER_NAME = "Agam-Shah"
SRC_REPO = "https://github.com/Agam-Shah/Mlops_mlflow"
AUTHOR_EMAIL = "agammehta93@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python pakage for ml app",
    long_Desxcription = long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"":"src"},
    packages=setuptools.find_packages(where="src")
)