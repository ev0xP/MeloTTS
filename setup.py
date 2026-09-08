import os
from setuptools import setup, find_packages

setup(
    name='melotts',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "librosa>=0.10.0",
        "soundfile>=0.12.0",
        "pydantic>=2.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "transformers>=4.36.0",
        "torch>=2.0.0",
        "torchaudio>=2.0.0",
        "mecab-python3>=1.0.8",
        "unidic-lite>=1.0.8",  # Menggantikan unidic berat & menghilangkan 'python -m unidic download'
        "num2words>=0.5.12",
        "pypinyin>=0.49.0",
        "jieba>=0.42.1",
        "gruut>=2.2.3",
        "g2p_en>=2.1.0",
        "anyascii>=0.3.2",
    ],
    package_data={
        '': ['*.txt', 'cmudict_*'],
    },
    entry_points={
        "console_scripts": [
            "melotts = melo.main:main",
            "melo = melo.main:main",
            "melo-ui = melo.app:main",
        ],
    },
)
