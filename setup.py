from setuptools import setup, find_packages

setup(
    name="example-package-ramos",  # Replace with your package name
    version="0.2.9",  # Replace with your version
    packages=find_packages(),  # This will automatically discover your packages
    install_requires=[
        # Add any dependencies your package requires here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or change to your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the Python version requirement
)
