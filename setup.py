# setup.py

from setuptools import setup, find_packages

setup(
    name='MR',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Mr Al-Rees',
    author_email='mralrees@gmail.com',
    description='A library that stops code execution based on a specified timeout and deletes a log entry after the timeout expires.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Alrees2/MR',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
