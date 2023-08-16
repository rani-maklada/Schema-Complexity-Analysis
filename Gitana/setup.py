"""The setuptools for Gitana"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
        name='gitana',
        version='1.0',
        description='Gitana: a SQL-based Project Activity Inspector',
        long_description='Gitana imports and digests the data of a Git repository, issue trackers and Q&A web-sites to '
                         'a relational database in order to ease browsing and querying activities with standard SQL '
                         'syntax and tools',
        url='https://github.com/SOM-Research/gitana',

        author='Valerio Cosentino',
        author_email='valcos@bitergia.com',

        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'License :: OSI Approved :: MIT License'
        ],
        keywords='gitana project-information-analysis communication-channels issue-trackers version-control-systems',
        packages=find_packages(exclude=['test', 'docs']),

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs pip's
        # requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=['networkx', 'gitpython', 'python-bugzilla', 'pygithub',
                          'selenium', 'py-stackexchange', 'slacker', 'pygal',
                          'mysql-connector-python-rf', 'beautifulsoup4'],

        # List additional groups of dependencies here (e.g. development
        # dependencies). You can install these using the following syntax,
        # for example:
        # $ pip install -e .[dev,test]
        # extras_require={
        #     'dev': ['check-manifest'],
        #     'test': ['coverage'],
        # },

        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        include_package_data=True,
        package_data={
            'exporters': ['exporters/resources/queries.json', 'exporters/resources/jumbotron.png'],
        },
        data_files=[('exporters/resources', ['exporters/resources/queries.json', 'exporters/resources/jumbotron.png'])]

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        # data_files=[('my_data', ['data/data_file'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        # entry_points={
        #     'console_scripts': [
        #         'sample=sample:main',
        #     ],
        # },
)
