from setuptools import setup, find_packages

setup(
    name='baby',
    version='0.0.1',
    author='Megan Marsh',
    author_email='megan.n.marsh@gmail.com',
    maintainer='Megan Marsh',
    maintainer_email='megan.n.marsh@gmail.com',
    description='Baby Announcement',
    url='https://www.github.com/swampdragons/baby',
    packages=find_packages(exclude=["*.tests",
                                    "*.tests.*",
                                    "tests.*",
                                    "tests"]),
    include_package_data=True,
    zip_safe=False,
    test_requires=[
        'mock==1.0.1',
        'nose==1.3.1',
    ],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ),
)
