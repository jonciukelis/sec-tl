from setuptools import setup

setup(
    name='software_engineering_challenge_package',
    version='0.0.1',
    install_requires=[
        'flask',
        'requests'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'requests-mock',
        ],
    },
)
