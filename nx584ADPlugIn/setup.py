from setuptools import setup

setup(name='nx584ADPlugIn',
      version='1.0',
      py_modules=['nx584ADPlugIn'],
      install_requires=[
            'setuptools>=40.5.0',
            'requests>=2.19.1'
      ],
      entry_points={'pynx584': ['test=src.nx584ADPlugIn:HomeBridgePing']},
      )
