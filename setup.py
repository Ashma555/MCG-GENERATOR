from setuptools import find_packages,setup


setup(
    name = 'mcggenerator',
    version='0.0.1',
    author='Ashma555',
    author_email='ashmasky786@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages()
)