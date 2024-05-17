from setuptools import find_packages, setup
from typing import List


HEPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) ->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HEPHEN_E_DOT in requirements:
            requirements.remove(HEPHEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Ivan Lima',
    author_email='ivanlima@misterivanlima.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)