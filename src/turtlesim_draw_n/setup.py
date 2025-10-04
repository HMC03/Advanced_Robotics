from setuptools import find_packages, setup

package_name = 'turtlesim_draw_n'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hayden',
    maintainer_email='haydenmcameron@proton.me',
    description='Enables Turtlesim to draw an N for \'NC State\'',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlesim_draw_n = turtlesim_draw_n.turtlesim_draw_n:main'
        ],
    },
)
