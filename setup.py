from setuptools import setup

setup(name='eand',
      version='0.1',
      description='Easy Algebraic Numerical Differentiation for Python',
      url='http://github.com/ph4m/eand.py',
      author='Tu-Hoa Pham',
      author_email='thp@pham.in',
      license='GPL v3',
      packages=['eand','eand.kmand', 'eand.mddig'],
      zip_safe=True)
