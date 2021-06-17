import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvisascope",
    version="0.0.1",
    author="Zezhong Song",
    author_email="szzsdu1989@oulook.com",
    description="PyVISAScope provides an interface to different scopes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/szztj668/scope-.git",
    packages=setuptools.find_packages(),
    install_requires=[
   'pyvisa>1.5'],
)
