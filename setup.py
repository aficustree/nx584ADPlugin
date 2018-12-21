from setuptools import setup

setup(name='nx584ADPlugIn',
      version='1.0',
      py_modules=['nx584ADPlugIn'],
      entry_points={'pynx584': ['test=nx584ADPlugIn:HomeBridgePing']},
      )
