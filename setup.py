from setuptools import find_packages,setup
from typing import List




def get_requirments(file_path:str)->List[str]:

    with open(file_path) as f:
        requirements=[i.strip() for i in f.readlines() if i!='-e .']
    print(requirements)


    return requirements



setup(
    name='ml_project',
    version='0.0.1',
    author='ram',
    author_email='saisriramthota@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)