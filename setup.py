from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2hellocli',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['ros2cli'],
    zip_safe=True,
    author='Jeremie Deray',
    author_email='jeremie.deray@canonical.org',
    maintainer='Jeremie Deray',
    maintainer_email='jeremie.deray@canonical.org',
    url='https://github.com/artivis/ros2hellocli',
    download_url='https://github.com/artivis/ros2hellocli/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='A minimal plugin example for ROS 2 command line tools.',
    long_description="""\
The package provides the hello command as a plugin example of ROS 2 command line tools.""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'hello = ros2hellocli.command.hello:HelloCommand',
        ],
        'ros2hellocli.verb': [
            'world = ros2hellocli.verb.world:WorldVerb',
        ],
    }
)
