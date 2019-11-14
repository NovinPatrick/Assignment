from setuptools import setup
import setuptools

setup(
    name='tan_egg',
    version='1.0.0',
    data_files=[('.',['__main__.py'])],
    entrypoints={'setuptools.installation': ["eggsecutable = src.main.main:main"]},

)
