from setuptools import setup

setup(
    name='lektor-google-analytics',
    author='Khaled Monsoor',
    author_email='k@kmonsoor.com',
    url='http://github.com/kmonsoor/lektor-google-analytics',
    version='0.1',
    license='BSD',
    py_modules=['lektor-google-analytics'],
    entry_points={
        'lektor.plugins': [
            'google-analytics = lektor_google_analytics:GoogleAnalyticsPlugin',
        ]
    }
)
