from setuptools import setup, find_packages, Extension
from codecs import open
from os import path
try:
    from Cython.Build import cythonize
except ImportError:
     def cythonize(*args, **kwargs):
         from Cython.Build import cythonize
         return cythonize(*args, **kwargs)

here = path.abspath(path.dirname(__file__))

readme_file = "README.md"
pip_req_file = "requirements.txt"

def read(fname):
    with open(path.join(here,fname)) as fp:
        content = fp.read()
    return content

# Get the long description from the README file
long_description = read(readme_file)

changelog = read(readme_file).splitlines()
for i,line in enumerate(changelog):
    if line.startswith('Change-Log'):
        line = changelog[i+1]
        j = 1
        while line.strip()=='' or line.startswith('---'):
            j += 1
            line = changelog[i+j]
        version = line.strip('# ')
        break

# get the dependencies and installs
all_reqs = []
all_reqs += read(pip_req_file).splitlines()


turtlpy_core_ext = Extension(
    name="turtlpy.core",
    sources=["turtlpy/turtle_core.pyx"],
    libraries=["turtl_core"],
    library_dirs=["./turtlpy"],
    include_dirs=[]
)
install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip() for x in all_reqs if x.startswith('git+')]

setup(
    name='turtlpy',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version','pytest-runner','cython'],
    description='Python client for the Turtl Note App System. This is basically a wrapper around the turtl-core. Useful for backing up or building interfaces to other note taking apps.',
    long_description=long_description,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    entry_points={'console_scripts': []},
    keywords='',
    ext_modules=cythonize([turtlpy_core_ext]),
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tobias Schoch',
    install_requires=install_requires,
    tests_require=['pytest'],
    dependency_links=dependency_links,
    author_email='tobias.schoch@vtxmail.ch'
)
