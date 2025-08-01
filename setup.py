from setuptools import setup, find_packages

setup(
    name="sam-tp",
    version="0.1",
    description="SAM-TP: Traversability Prediction via SAM2",
    author="Jiaming Wang*, Diwen Liu*, Jizhuo Chen*, Jiaxuan Da, Nuowen Qian, Tram Minh Man, Harold Soh",
    packages=find_packages(include=["sam_tp", "sam_tp.*"]),
    install_requires=[  # keep in sync with requirements.txt
        # "numpy>=1.24.4",
        # "tqdm>=4.66.1",
        # "pillow>=9.4.0",
        # "opencv-python>=4.7.0",
        # "matplotlib>=3.9.1",
        # "jupyter>=1.0.0",
        # "flask>=3.0.3",
        # "flask-cors>=5.0.0",
        # "gunicorn>=23.0.0",
        # "dataclasses-json>=0.6.7",
        # "imagesize>=1.4.1",
        # "strawberry-graphql>=0.243.0",
        # "av>=13.0.0",
        # "pycocotools>=2.0.8",
        # "pandas>=2.2.2",
        # "scikit-image>=0.24.0",
        # "tensorboard>=2.17.0",
        # "submitit>=1.5.1",
        # "hydra-core>=1.3.2",
        # "iopath>=0.1.10",
        "numpy>=1.24.4",
        "tqdm>=4.66.1",
        "hydra-core>=1.3.2",
        "iopath>=0.1.10",
        "pillow>=9.4.0",
    ],
    python_requires=">=3.10",
)
