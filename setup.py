from setuptools import setup, find_packages
from codecs import open
from os import path
import yaml

here = path.abspath(path.dirname(__file__))

conda_env_file = "environment.yml"
readme_file = "README.md"
pip_req_file = "requirements.txt"

def read(fname):
    with open(path.join(here,fname)) as fp:
        content = fp.read()
    return content

def read_yaml(fname):
    with open(path.join(here,fname)) as fp:
        content = yaml.load(fp)
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
if path.exists(conda_env_file):
    for line in read_yaml(conda_env_file)['dependencies']:
        if line.startswith('#'): continue # except only comments
        if line.strip().endswith('conda'): continue # except lines marked as only conda
        line = line.split('#')[0] # except comments
        if line.split('=')[2].startswith('py') and not line.split('=')[0].startswith('pip'):
            line = "==".join(line.split('=')[:2]) # except conda second version spec
            all_reqs.append(line)

all_reqs += read(pip_req_file).splitlines()

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip() for x in all_reqs if x.startswith('git+')]

setup(
    name='python-turtlpy',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version','pytest-runner'],
    description='Python client for the Turtl Note App System. This is basically a wrapper around the turtl-core. Useful for backing up or building interfaces to other note taking apps.',
    long_description=long_description,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    entry_points={'console_scripts': []},
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tobias Schoch',
    install_requires=install_requires,
    tests_require=['pytest'],
    dependency_links=dependency_links,
    author_email='tobias.schoch@vtxmail.ch'
)
