from distutils.core import setup
from setuptools import find_packages

setup(
    name='traffic-light-simulation-turtle',
    packages=["simulation"],
    include_package_data=True,
    package_data={'simulation': ['*']},
    version='0.1',
    description='A Traffic Light Simulator works on turtle and tkinter',
    author='Rama krishna kumar Lingamgunta',
    author_email='ramkumar2606@gmail.com',
    url='https://github.com/ramkumar2606/traffic-simulation',
    download_url='https://github.com/ramkumar2606/traffic-simulation/archive/master.zip',
    keywords=['python', 'traffic light simulation', 'example', 'testing'],
    classifiers=[],
    entry_points={
        'console_scripts': ['traffic-light-simulation=simulation.main:main'],
    },
)
