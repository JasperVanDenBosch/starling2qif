from setuptools import setup, find_packages

requires = []
with open('requirements.txt') as reqfile:
    requires = reqfile.read().splitlines()


setup(
    name='starling2qif',
    version='0.0',
    description='Convert Starling bank statement csv files to the more widely supported QIF format',
    url='https://github.com/Charestlab/starling2qif',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT",
    ],
    author='Jasper J.F. van den Bosch',
    author_email='',
    keywords='Starlink bank statement qif',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="tests",
    scripts=['scripts/starling2qif'],
)