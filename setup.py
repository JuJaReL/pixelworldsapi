

from setuptools import find_packages, setup

def get_long_description():
  with open("README.md", "r") as f:
    data = f.read()
  return data

setup(
  name="pixelworldsapi",
  description="A python wrapper for Pixel Worlds' data",
  long_description=get_long_description(),
  long_description_content_type='text/markdown',
  install_requires=[
    "beautifulsoup",
    "requests"
  ]
  download_url="https://github.com/zenqii/pixelworldsapi/tarball/main",
  classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Topic :: Software Development",
		"Topic :: Software Development :: Libraries :: Python Modules",
	]
)

