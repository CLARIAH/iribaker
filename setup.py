from setuptools import setup

setup(name='iribaker',
      version='0.1.3',
      description='Safely convert IRI-like string to IRI.\nReplaces invalid charactes with an underscore (i.e. does not support roundtripping).\nFalls back to standard URL percent encoding.',
      url='http://github.com/clariah-sdh/iribaker',
      author='Rinke Hoekstra (VU University Amsterdam/University of Amsterdam)',
      author_email='rinke.hoekstra@vu.nl',
      license='MIT',
      packages=['iribaker'],
      install_requires=[
          'rfc3987',
      ],
      zip_safe=False)
