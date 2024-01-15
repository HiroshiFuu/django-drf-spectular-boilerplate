from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [
    Extension('*',  ['core/*.py']),
    Extension('*',  ['backend/*.py']),
    Extension('*',  ['backend/v1/*.py']),
    Extension('*',  ['backend/v2/*.py']),
]

setup(
    name = 'MyTemplate',
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(ext_modules, language_level='3')
)
