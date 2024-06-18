from setuptools import find_packages, setup


HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str)->list[str]:
    '''
    This function will read the requiremnet file
    '''
    reqirements = []
    with open(file_path) as file_obj:
        reqirements = file_obj.readline()
        reqirements = [req.replace('/n', '') for req in reqirements]

        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)

    return reqirements

setup(
    name = 'generic_machine_learning',
    version='0.0.1',
    author = 'Lakshhay',
    author_email = 'lakshaysaini@gmail.com',
    packages=find_packages,
    install_requires = get_requirments('requirements.txt')
)