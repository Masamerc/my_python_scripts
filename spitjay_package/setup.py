try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

# better approach: declarative way, reading config from setup.cfg
setup()

# # traditional approach

# with open('README.md', 'r') as f:
#     long_description = f.read()

# setup(
#     name='spitjay',
#     description='test package',
#     long_description=long_description,
#     author='Masa Fukui',
#     author_email='masahiro.m.fukui@gmai.com',
#     keywords='test package demo',
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: MIT License'
#     ],
#     version='0.7.1',
#     packages=find_packages(),
#     # packages=['src/spitjay'] # in case we do not have setuptools
#     entry_points={'console_scripts': ['spitjay1000=spitjay.core:spit_1000_json']}
# )