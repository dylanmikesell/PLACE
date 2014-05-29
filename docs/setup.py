#try:
#    from setuptools import setup
#except ImportError:
from distutils.core import setup

#figure out version
#update URL
#install_requires
#license
setup(
    name='PyPAL',
    version='0.1.0',
    author='Jami L. Johnson, Kasper van Wijk, Henrik tom Wörden',
    author_email='jami.johnson@auckland.ac.nz',
    packages=['pypal','pypal.analysis','pypal.automate','pypal.automate.osci_card','pypal.automate.polytec','pypal.automate.tektronix','pypal.automate.xps_control'],
    scripts=['bin/Scan.py','bin/example_PALplots.py'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description= 'An open-source Python package for laboratory automation and analysis.',
    long_description=open('README.txt').read(),
    install_requires=["numpy", "obspy","scipy", "matplotlib", "h5py", "obspyh5"]
    )
