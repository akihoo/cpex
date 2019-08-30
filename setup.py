from setuptools import setup

setup(
    name='cpex',
    version='0.0.1',
    author='C. Simpson',
    author_email='c.a.simpson01@gmail.com',
    packages=['pyxe'],
    include_package_data=True,
    url='https://github.com/casimp/pyxe',
    download_url = 'https://github.com/casimp/pyxe/tarball/v0.9.3',
    license='LICENSE.txt',
    description='Extraction and manipulation of crystal plasticity data from ODB files.',
    keywords = ['CP', 'crystal plasticity', 'XRD', 'EDXRD', 'x-ray', 'diffraction', 'strain'],
#    long_description=open('description').read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]
)