from setuptools import setup, find_packages

setup(
    name='meda-sync-search',
    packages=find_packages(),
    version='0.1',
    description='Python Flask App to Phonetically Search Prescription Drugs and Equipment by Name',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/meda-sync-search',
    download_url='https://github.com/DEV3L/meda-sync-search/tarball/0.1',
    keywords=['dev3l', 'flask', 'heroku', 'pheonetic', 'soundex', 'prescription'],
    install_requires=[
        'flask',
        'flask-runner',
        'fuzzy',
        'gunicorn',
        # tests / ci
        'bandit',
        'coverage',
        'coveralls',
        'pylint',
        'pytest'
        'tox',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: THE BEER-WARE LICENSE',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
