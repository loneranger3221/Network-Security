'''This is the setup script for the project. It specifies the dependencies required to run the project.Helps create our ML applcn as a package '''
from setuptools import setup,find_packages
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open (file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 
        return requirements
    '''we added -e . to run setup.py in editable mode. This allows us to make changes to our code and have those changes reflected immediately without needing to reinstall the package. It is particularly useful during development when we are frequently updating our code.'''
    

setup(
    name='mlops_app',
    version='0.1',
    author='Sayak',
    suthor_email='sayak.legend12@gmail.com',
    description='A machine learning application for Network Security project ',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)