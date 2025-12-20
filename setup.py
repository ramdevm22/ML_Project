from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()  
            if line and line != "-e .":
                requirements.append(line)
    return requirements


setup(
    name='ML_Project',
    version='0.1.0',
    author='Ramdev',
    author_email='vsskpkmp008@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
