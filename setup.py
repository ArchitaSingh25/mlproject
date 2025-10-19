from setuptools import setup, find_packages
from typing import List

HYPEN_V = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', '') for req in requirement ]
        if HYPEN_V in requirement:
            requirement.remove(HYPEN_V)
    return requirement

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)