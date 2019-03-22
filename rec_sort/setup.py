from setuptools import setup, find_packages

setup(
    name='recsort',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My first deliverable python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/tpadi/recsort',
    author='tpadi',
    author_email='padi.thabiso@gmail.com'
)
