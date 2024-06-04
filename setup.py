from setuptools import setup, find_packages

setup(
    name="auto_chat_template",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'act=auto_chat_template.main:main'
        ]
    }
)