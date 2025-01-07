#!/usr/bin/env python
"""
Check for required dependencies for the workshop.
Usage::

  % python check_env.py

"""
from packaging.version import Version

# NOTE: Update minversion values as needed.
# This should match environment.yml and requirements.txt contents.
PKGS = {
    'jupyter': None,
    'notebook': '7.0',
    'numpy': '2.2.1',
    'scipy': '1.14.1',
    'skimage': '0.25.0',
    'matplotlib': '3.10.0',
    'jdaviz': '4.1.0',
    'astropy': '7.0.0',
    'asdf': '3.5.0',
    'gwcs': '0.20',
    'photutils': '2.1.0',
    'specutils': '1.19.0',
    'specreduce': '1.4.1',
    'astroquery': '0.4.7dev9008',
    'webbpsf': '1.5.0',
    'roman_datamodels': '0.22.0',
}


def check_package(package_name, minimum_version=None, verbose=True):
    errors = False
    try:
        pkg = __import__(package_name)
    except ImportError as err:
        print(f'Error: Failed import: {err}')
        errors = True
    else:
        if package_name in ('jupyter', 'keyring'):
            installed_version = ''
        elif package_name == 'xlwt':
            installed_version = pkg.__VERSION__
        else:
            installed_version = pkg.__version__
        if (minimum_version is not None and
                Version(installed_version) <
                Version(str(minimum_version))):
            print(f'Error: {package_name} version {minimum_version} or '
                  f'later is required, you have version {installed_version}')
            errors = True
        if not errors and verbose:
            print('Found', package_name, installed_version)
    return errors


def run_checks():
    errors = []
    for package_name, min_version in PKGS.items():
        errors.append(check_package(package_name, minimum_version=min_version))
    if any(errors):
        print('\nThere are errors that you must resolve before running the '
              'workshop notebooks.')
    else:
        print('\nYour Python environment is good to go! 🎉')


if __name__ == '__main__':
    run_checks()
