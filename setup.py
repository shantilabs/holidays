from distutils.core import setup


setup(
    name='holidays',
    version='1.2019.0',
    author='Maxim Oransky',
    author_email='maxim.oransky@gmail.com',
    packages=[
        'holidays',
    ],
    package_data={
        'holidays': ['data/ru/*'],
    },
    url='https://github.com/shantilabs/holidays',
)
