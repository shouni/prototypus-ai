from setuptools import setup, find_packages

setup(
    name='prototypus-ai',
    version='0.1.0',
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'google-generativeai>=0.3.0',
        'fire>=0.5.0',
        'python-dotenv>=1.0.0',
    ],
    entry_points='''
        [console_scripts]
        ptai=prototypus_ai.cli:main
    ''',
    package_dir={'': 'src'},
)