import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

data_files = []
for root, dirs, files in os.walk('src/mod2die/resources/arcade'):
    ff = []
    for file in files:
        ff.append(os.path.join(root, file))
    data_files.append((root, ff))

setuptools.setup(
    author='Josiah Bradley',
    author_email='Josiah Bradley@gmail.com',
    name="mod2win",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'play = mod2win.levels.level_01:main',
            'level1 = mod2win.levels.level_01:main',
            'level2 = mod2win.levels.level_02:main',
            'level3 = mod2win.levels.level_03:main',
            'spiral = mod2win.levels.spiral_test:main'
        ]
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    data_files=data_files,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
