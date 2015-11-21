import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.md')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_mako',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
	'passlib',
	'webhelpers2'			# Various web building related helpers
]

setup(name='sins',
      version='0.0',
      description='SINS is not SFIM',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      author='Travis Rigg',
      author_email='rigg.travis@gmail.com',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='sins',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sins:main
      [console_scripts]
      initialize_sins_db = sins.scripts.initializedb:main
      """,
)
