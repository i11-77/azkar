from setuptools import setup, find_packages

setup(
    name="azkar",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="مكتبة بايثون بسيطة تعطي ذكر إسلامي عشوائي",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="BOYKA",
    url="https://github.com/i11-75/azkar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
