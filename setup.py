from setuptools import setup, find_packages

version = '0.0.1'

setup(
	name='indian_banks',
	version=version,
	description='as',
	author='sa',
	author_email='v@d.c',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=("frappe",),
)
