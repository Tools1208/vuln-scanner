from setuptools import setup, find_packages

setup(
    name='vuln-scanner',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'jinja2',
        'reportlab',
        'pyopenssl',
        'cve_search',
        'nuclei',
        'sqlmap',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'vulnscan=cli:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
