from setuptools import setup,find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='wc_csv',
    version='0.23',
    description='This tool can be csv to string',
    url='https://github.com/Oshita/wc_csv',
    author='NoriakiOshita',
    author_email='oshitanoriaki@gmail.com',
    license='MIT',
    long_description=readme,
    keywords='wordcloud csv',
    packages=find_packages(),
)