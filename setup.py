from setuptools import setup, find_packages


PYPI_RESTRUCTURED_TEXT_INFO = \
"""
Adds ordering to Django's many-to-many relations.

Full documentation at http://github.com/markfinger/django-ordered-m2m
"""

setup(
    name = 'django-ordered-m2m',
    version = '1.0.2',
    packages = find_packages(),
    package_data={
        'ordered_m2m': [
            'static/ordered_m2m/*.*',
        ],
    },
    entry_points = {},

    # metadata for upload to PyPI
    author = 'Mark Finger',
    author_email = 'markfinger@gmail.com',
    description = 'Adds ordering to Django\'s many-to-many relations.',
    license = 'MIT',
    platforms=['any'],
    keywords = 'django m2m many-to-many order ordered ordering',
    url = 'https://github.com/markfinger/django-ordered-m2m',
    long_description = PYPI_RESTRUCTURED_TEXT_INFO,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
)