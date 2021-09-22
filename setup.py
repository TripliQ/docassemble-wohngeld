import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.wohngeld',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# NRW Wohngeldantrag\r\n\r\n![Wohngeld Logo](docassemble/wohngeld/data/static/welcome_screen.svg)\r\n\r\nA [docassemble](https://github.com/jhpyle/docassemble) interview to easily create the NRW Wohngeldantrag via an online Interview.\r\n\r\n\r\n## Installation and Usage\r\n\r\n1. Navigate to the docassemble `Playground`\r\n2. Click the `Pull` icon\r\n3. Pull from the repository with the following `GitHub URL`\r\n```\r\nhttps://github.com/TripliQ/docassemble-wohngeld.git\r\n```\r\n\r\n## File/Folder Structure\r\n\r\n```\r\n├── docassemble                           # Main files for interview\r\n    ├── wohngeld                          # Project name\r\n        ├── data                          # All data files\r\n            ├── questions                 # All question `yml` files\r\n                ├── document.yml          # Logic for filling document pdf fields\r\n                ├── interview.yml         # Main interview logic\r\n                ├── questions.yml         # All questions asked during interview\r\n                ├── review.yml            # Review screen questions\r\n            ├── sources           \r\n            ├── static                    # All static content such as pictures\r\n            ├── templates                 # Templates to be filled\r\n                ├── wohngeldantrag.pdf    # Main PDF form to be filled\r\n├── LICENSE \r\n├── MANIFEST.in\r\n├── README.md\r\n├── setup.cfg                   \r\n└── setup.py\r\n```\r\n\r\n## Authors\r\n\r\nTripliQ\r\n\r\nLegal Tech Lab Cologne\r\n',
      long_description_content_type='text/markdown',
      author='Simon Damschen',
      author_email='simon.damschen@outlook.de',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/wohngeld/', package='docassemble.wohngeld'),
     )

