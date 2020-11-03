# 【Techの道も一歩から】第21回「setup.pyを書いてpipでインストール可能にしよう」
#  https://buildersbox.corp-sansan.com/entry/2019/07/11/110000
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="m21server",
    version="0.1.0",
    license="MIT",
    description="",
    author="desktopgame",
    url="https://github.com/desktopgame/m21server",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    entry_points={
        'console_scripts': [
            'm21server = m21server.main:main',
        ],
    },
)
