from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="xmlmenu",
    version="1.0.0",
    author="Bernhard Arnold",
    author_email="bernhard.arnold@cern.ch",
    description=("Fast XML trigger menu reader"),
    license="GPLv3",
    url = "http://github.com/arnobaer/xmlmenu",
    py_modules=['xmlmenu'],
    install_requires=["lxml"],
    entry_points="""
        [console_scripts]
        xmlmenu=xmlmenu:main
    """,
    long_description=long_description,
)
