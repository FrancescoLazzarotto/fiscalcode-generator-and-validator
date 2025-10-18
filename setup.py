from setuptools import setup, find_packages

setup(
    name="cf-generator",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas>=2.0"],
    entry_points={
        "console_scripts": [
            "cf-gen = main:main",
        ]
    },
)



 
        