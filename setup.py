# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='django-google-address',
    version='1.1.0',
    author=u'Leonardo Arroyo',
    author_email='contato@leonardoarroyo.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/leonardoarroyo/django-google-address',
    download_url='https://github.com/leonardoarroyo/django-google-address/tarball/1.1.0',
    license='MIT',
    description='',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    install_requires=reqs
)
