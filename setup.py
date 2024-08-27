# building application as a package to easily install easily in any system.....

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path) ->List[str]:
    '''
        the function return the list or requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="radha",
    author_email="radhabarsaiya007@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt')
)

