from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

# Probably should be changed, __init__.py is no longer required for Python 3
for dirpath, dirnames, filenames in os.walk('correspondence_tables'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


setup(
    name='correspondence_tables',
    version="0.2",
    packages=packages,
    author="BONSAI team",
    author_email="info@bonsai.uno",
    license=open('LICENSE').read(),
    package_data={'correspondence_tables': package_files(os.path.join('correspondence_tables', 'data'))},
    entry_points = {
        'console_scripts': [
            'correspondence_tables-cli = correspondence_tables.bin.correspondence_tables_cli:main',
        ]
    },
    install_requires=[
        'docopt',
        'pandas',
        'rdflib',
        'xlrd',
    ],
    url="https://github.com/BONSAMURAIS/correspondence_tables",
    long_description=open('README.md').read(),
    description="Generate the URIs needed for the BONSAI knowledge graph",
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
