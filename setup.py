from setuptools import setup, find_packages

setup(
    name="cutsub",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "pysubs2",
        "pytest",
        "pytest-sugar",
    ],
    entry_points="""
        [console_scripts]
        cutsub=cutsub.cli:cut_subtitle
    """,
    author="Kaloyan Mirchev",
    author_email="kaloyan.mir4ev@gmail.com",
    description="CLI tool to cut subtitle files based on start and end times",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cutsub",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
