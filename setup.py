from setuptools import setup

setup(
    name='fixer-demo',
    version='0.2',
    description='Fixer service demo package',
    url='https://github.com/thisisZoya/fixer-demo',
    author='Zoya', 
    author_email='zoya.zq.210@gmail.com',
    license='MIT',
    packages=['fixer'],
    install_requires=['requests'], 
    zip_safe=False)