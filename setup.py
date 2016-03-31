from setuptools import find_packages, setup

import django_nats

setup(
    name='django-nats',
    version=django_nats.version,
    packages=find_packages(exclude=["tests"]),
    install_requires=['cliez'],
    url='https://github.com/9nix00/django-nats',
    license='http://opensource.org/licenses/MIT',
    download_url='https://github.com/9nix00/django-nats/archive/master.zip',
    include_package_data=True,
    author='wangwenpei',
    author_email='wangwenpei@nextoa.com',
    description='django client for NATS message system',
    keywords='django_nats,',
)

