import setuptools

with open('README.md','r',encoding='utf-8') as f:
    long_description=f.read()

__version__='0.0.0'

REPO_NAME='Drinks-Quality-Prediction-System'
AUTHOR_USER_NAME='mdzaheerjk'
SRC_REPO='mlProject'
AUTHOR_EMAIL='zaheerjkxai@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/mdzaheerjk/Drinks-Quality-Prediction-System",
    project_urls={
        "Bug Tracker":f"https://github.com/mdzaheerjk/Drinks-Quality-Prediction-System/issues"

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')

)