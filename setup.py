import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pyevals",  # Replace with your own username
    version="1.1.3",
    author="Anirudh Palaparthi",
    author_email="anirudhpalaparthi@gmail.com",
    description="A small package for evaluating models.",
    url="https://github.com/anirudhpnbb/Pyevals",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
