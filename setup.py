import setuptools
from setuptools import setup

setup(name='gym_gridworlds',
      version='0.0.1',
      author='Per Mattsson',
      author_email='magni84@gmail.com',
      description='Implements some minimalisitc GridWorld environments for Gymnasium',
      url='https://github.com/magni84/gym_gridworlds',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
      install_requires=['gymnasium', 'numpy']
)
