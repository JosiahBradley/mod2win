import setuptools

long_description = ""
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author='Josiah Bradley',
    author_email='JosiahBradley@gmail.com',
    name="mod2win",
    url="https://github.com/JosiahBradley/mod2win",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'play = mod2win.levels.level_launcher:launch',
            'compile = mod2win.levels.level_launcher:_compile',
            'scrub = mod2win.levels.level_launcher:scrub',
            'restore = mod2win.levels.level_launcher:restore',
            'spiral = mod2win.levels.spiral_test:main',
        ]
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
