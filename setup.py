from setuptools import find_packages, setup



setup(
    name='MCQ Generator',
    version='0.1.1',
    author='Kalpesh Tarsariya',
    author_email='kalpesh.tarsariya819@gmail.com',
    install_requires= ['openai','langchain','streamlit','python-dotenv','PyPdf2'],
    packages=find_packages()

)