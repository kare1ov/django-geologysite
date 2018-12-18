import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-geologysite',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['beautifulsoup4==4.6.3',
                      'django-bootstrap-form == 3.4',
                      'django-ckeditor==5.6.1',
                      'django-js-asset==1.1.0',
                      'Pillow==5.3.0'],
    license='BSD License',
    description='My first Django app.',
    long_description=README,
    url='https://www.example.com/',
    author='Ruslan Karelov',
    author_email='ruslan.karelov@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',

    ],
)