from setuptools import find_packages, setup


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile("README.rst")
changes = readfile("CHANGES.rst")

install_requires = [
    "toml ~= 0.10.2",
    "plaster >= 0.5",
]

setup(
    name="plaster_toml",
    description=(
        "A loader implementing the TOML syntax to be used by plaster."
    ),
    long_description=readme + "\n\n" + changes,
    version="1.0",
    author="Jeremiasz Nelz",
    author_email="remi6397@gmail.com",
    url="https://github.com/remi6397/plaster_toml",
    zip_safe=False,
    install_requires=install_requires,
    python_requires=">=3.7",
    keywords="plaster toml plaster_toml config",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "plaster.loader_factory": [
            "toml=plaster_toml:Loader",
        ],
    },
)
