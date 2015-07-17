from setuptools import setup

setup(name='to_iri',
      version='0.1',
      description='Safely convert IRI-like string to IRI.\nReplaces invalid charactes with an underscore (i.e. does not support roundtripping).\nFalls back to standard URL percent encoding.',
      url='http://github.com/clariah-sdh/to_iri',
      author='Rinke Hoekstra (VU University Amsterdam/University of Amsterdam)',
      author_email='rinke.hoekstra@vu.nl',
      license='MIT',
      packages=['to_iri'],
      zip_safe=False)