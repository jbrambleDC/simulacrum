from setuptools import setup

setup(name = 'simulacram',
      version = '0.1',
      description = 'Create Pandas DataFrames of simulated data with columns following statistical distributions or categorical datatypes',
      url = 'https://github.com/jbrambleDC/simulacram',
      download_url = 'https://github.com/jbrambleDC/simulacram/tarball/0.1',
      author = 'Jordan Bramble',
      author_email = 'jordanbramble@gmail.com',
      license = 'MIT',
      packages = ['simulacram'],
      keywords = ['simulation', 'data', 'data science'],
      install_requires = ['pandas', 'faker'],
      zip_safe = False)
