from setuptools import setup, find_packages

setup(
    name='nillanet',
    version='0.1.0',
    author='James Smith',
    author_email='james.smith@rcsb.org',
    description='linear neural net component',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_awesome_package',
    packages=find_packages(),
    install_requires=[      
        'requests>=2.25.1',
        'cupy',
        'numpy',
    ],
    classifiers=[          
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)

