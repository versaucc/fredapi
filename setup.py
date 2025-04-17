from setuptools import setup, find_packages

setup(
    name='fredapi-py', 
    version='0.1.0',
    author='Oliver Grenon',
    author_email='grenonoliver@gmail.com',
    description='A Python wrapper for the Federal Reserve Economic Database (FRED) API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/versaucc/fredapi-py',
    packages=find_packages(include=['fredapi', 'fredapi.*']),
    install_requires=[
        'requests',
        'pandas'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache 2.0',
    ],
    include_package_data=True,
    license='Apache 2.0',
)