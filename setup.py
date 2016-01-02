from setuptools import setup

README = open('README.md').read()

setup(
        name='lektor-google-analytics',
        author='Khaled Monsoor',
        author_email='k@kmonsoor.com',
        url='http://github.com/kmonsoor/lektor-google-analytics',
        version='0.1.3',
        license='BSD',
        description='Adds support for Google analytics to Lektor CMS',
        long_description=README,
        py_modules=['lektor_google_analytics'],
        entry_points={
            'lektor.plugins': [
                'google-analytics=lektor_google_analytics:GoogleAnalyticsPlugin',
            ]
        },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ], requires=['lektor']
)
