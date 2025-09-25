from setuptools import setup, find_packages

setup(
    name='prototypus-ai',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-generativeai>=0.3.0',
        'click>=8.1.3',
        'python-dotenv>=1.0.0',
    ],
    entry_points='''
        [console_scripts]
        prototypus-ai=prototypus_ai.cli:cli
    ''',
)