from setuptools import find_packages,setup
# from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str):
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT=='-e .' in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

        
# meta-data info 
setup(
name='crop_clustering',
version = '0.0.1',
author='Keziah',
author_email='keziajael2000@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)
