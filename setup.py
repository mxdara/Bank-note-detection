from setuptools import find_packages, setup
from typing import List # type: ignore

E_DOT = '-e .'

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements

setup(
    name='bank-note-detection',
    version='0.0.1',
    author='Sameer',
    author_email='sameer.ahad@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)