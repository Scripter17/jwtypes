import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="jwtypes",
	version="0.1",
	author="James C. Wise (Scripter17)",
	author_email="jameschristopherwise@gmail.com",
	description="A package for adding improved versions of built-in types",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Scripter17/jwtypes",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)