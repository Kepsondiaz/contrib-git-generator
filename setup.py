from setuptools import setup, find_packages

setup(
    name="contribguide",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'generate-contrib-guide=contribguide.generator:generate_contributing_guide',
        ],
    },
)
