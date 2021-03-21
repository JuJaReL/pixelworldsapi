from setuptools import setup
import os

def get_long_description():
        
        with open("README.md", encoding="utf-8") as f:
                readme = f.read()

        return readme

setup(
  name=__import__("pixelworlds").__title__,
  author=__import__("pixelworlds").__author__,
  description="🌎 A python wrapper for pixel worlds' data",
  long_description=get_long_description(),
  long_description_content_type='text/markdown',
  url="https://github.com/zenqii/pixelworldsapi",
  version=__import__("pixelworlds").__version__,
  python_requires=">=3.5",
  platforms=["Windows"],
  license=__import__("pixelworlds").__license__,
  keywords=["api", "pixelworlds"],
  download_url="https://github.com/zenqii/pixelworldsapi/tarball/main",
  zip_safe=False,
  include_package_data=True,
  install_requires = [
	"beautifulsoup",
	"requests"
  ],
  classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Topic :: Software Development",
		"Topic :: Software Development :: Libraries :: Python Modules",
	]
)
