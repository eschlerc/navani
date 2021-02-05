from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='navani',
    url='https://github.com/BenSmithGreyGroup/navani',
    author='Ben Smith',
    author_email='ben.ed.smith2@gmail.com',
    # Needed to actually package something
    packages=['navani'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'scipy', 'galvani', 'matplotlib'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Package for processing and plotting echem data from cyclers',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)