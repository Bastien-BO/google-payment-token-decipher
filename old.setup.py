from google_payment_token_decipher.version import VERSION
from setuptools import setup

setup(
    name="google-payment-token-decipher",
    version=VERSION,
    description="A python google payment token decipher library",
    long_description="A simple python implementation of the decipher process for google payment token",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    author="Bastien BO",
    author_email="bastien.bo@free.fr",
    url="https://github.com/Bastien-BO/google-payment-token-decipher",
    license="Apache 2.0",
    packages=["google_payment_token_decipher"],
    python_requires=">=3.7",
)
