from setuptools import find_packages, setup
from typing import List


hypen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements



setup(
name='RAG with Llama3.1',
version='0.0.1',
author='Muhammad Rasel',
author_email='zenithstat@gmail.com',
packages=find_packages(),
install_packages=get_requirements('requirements.txt')
)