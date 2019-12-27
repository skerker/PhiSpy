import setuptools
from distutils.core import Extension
import os

# Read the markdown files for the long description
def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        if os.path.exists(filename):
            with open(filename, "r", encoding=encoding) as f:
                buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.md')


# write the current version to PhiSpy/__init__.py for automatically updating
def write_version(ver):
    if os.path.exists('PhiSpy/__init__.py'):
        txt = []
        with open('PhiSpy/__init__.py', 'r') as f:
            for l in f:
                if l.startswith("__version__"):
                    txt.append("__version__='{}'\n".format(ver))
                else:
                    txt.append(l)
        with open('PhiSpy/__init__.py', 'w') as out:
            out.write("".join(txt))

def get_version():
    with open("VERSION", 'r') as f:
        v = f.readline().strip()
        write_version(v)
        return v





def main():
    setuptools.setup(
        name="PhiSpy",
        version=get_version(),
        description="Prophage finder using multiple metrics",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Rob Edwards",
        platforms='any',
        keywords="phage prophage bioinformatics microbiology bacteria genome genomics",
        author_email="raedwards@gmail.com",
        url='https://github.com/linsalrob/PhiSpy',
        license='The MIT License (MIT)',
        scripts=['PhiSpy.py'],
        packages=setuptools.find_packages(),
        zip_safe=True,
        ext_modules=[Extension("PhiSpyRepeatFinder", sources=["src/repeatFinder.cpp"], language='c++')],
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3.0',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        entry_points = {
            'console_scripts': [
                'phispy = PhiSpy.py:main'
            ]
        },
        install_requires = [
            'biopython>=1.74',
            'numpy>=1.17.0',
            'scikit-learn>=0.21.3',
        ]
        )

if __name__ == "__main__":
    main()
