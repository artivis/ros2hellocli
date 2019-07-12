from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2hellocli',
    version='0.7.0',
    packages=find_packages(exclude=['test']),
    install_requires=['ros2cli'],
    zip_safe=True,
    author='Jeremie Deray',
    author_email='jeremie.deray@canonical.org',
    maintainer='Jeremie Deray',
    maintainer_email='jeremie.deray@canonical.org',
    url='https://github.com/ros2/ros2cli/tree/master/ros2hellocli',
    download_url='https://github.com/ros2/ros2cli/releases',
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
        'ros2cli.extension_point': [
            'ros2hellocli.verb = ros2hellocli.verb:VerbExtension',
        ],
        'ros2hellocli.verb': [
            'cli = ros2hellocli.verb.cli:CliVerb',
            'world = ros2hellocli.verb.world:WorldVerb',
        ],
    }
)
