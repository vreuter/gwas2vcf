import os
import sys
from setuptools import setup

PKG = "gwas2vcf"


with open(os.path.join(PKG, "_version.py"), 'r') as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")


def read_reqs(reqs_name):
    depsfile = os.path.join("requirements", f"reqs-{reqs_name}.txt")
    with open(depsfile, 'r') as f:
        return [l.strip() for l in f if l.strip()]


setup(
    name=PKG,
    packages=[PKG],
    version=version,
    description="Standardization of GWAS summary staatistics",
    long_description="Conversion of GWAS summary statistics to GWAS-VCF format, from less structure GWAS summary statistics",
    long_description_content_type='text', 
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="GWAS genetics bioinformatics",
    url="https://github.com/MRCIEU/{}/".format(PKG),
    author=u"Matthew Lyon, Gibran Hemani, Abdallah Amr Mahmoud, Ben Alexander",
    install_requires=read_reqs("base"), 
    test_suite="test",
    tests_require=read_reqs("test"),
    setup_requires=(["pytest-runner"] if {"test", "pytest", "ptr"} & set(sys.argv) else []),
)

