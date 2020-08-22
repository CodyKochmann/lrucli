from distutils.core import setup
from setuptools import find_packages

version = '2020.8.22'
name = 'lrucli'
packages = setuptools.find_packages()

assert name in packages, [name, packages]  # if package name doesnt show up, something is wrong

setup(
  name = name,
  version = version,
  packages = packages,
  install_requires = [],
  zip_safe=True,
  description = 'command line interface for pythons lru_cache for more command line fu',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/{}'.format(package_name),
  download_url = 'https://github.com/CodyKochmann/{}/tarball/{}'.format(package_name, version),
  keywords = [package_name, 'cli', 'lru', 'dedup', 'uniq', 'stdin', 'shell', 'bash'],
  entry_points = {
    'console_scripts': [
      'lru = lrucli.__main__:main'
    ]
  },
  python_requires='>=3.2',
  classifiers = []
)
