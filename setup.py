from setuptools import setup, find_packages

__version__ = '0.1'
__description__ = 'Microdots-Python'
__long_description__ = 'Middleware to WSGI applications'

__author__ = 'Fernando Marcio, Mbodock'
__author_email__ = 'ferandomarcio13@gmail.com, mbodock@gmail.com'

requires = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='microdots-python',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/mbodock/django-cepfield/',
    keywords='Django, CEP, Address, Brazil',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
)
