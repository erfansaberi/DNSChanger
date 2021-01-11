import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnschanger",
    version="0.1.3",
    author="Erfan Saberi",
    author_email="erfansmart12@gmail.com",
    description="A python script to change your dns provider, including google, shecan, clouflare and more providers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erfansaberi/DNSChanger",
    packages=setuptools.find_packages(),
    license = 'MIT',
    entry_points = {
        'console_scripts': ['dnsc=dnschanger.dnsc:main'],
    }
)