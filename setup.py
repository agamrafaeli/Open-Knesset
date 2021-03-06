from setuptools import setup, find_packages

install_requires = [
    # 'python-yadis',
    'BeautifulSoup',
    'South',
    'django-debug-toolbar',
    'django-extensions',
    'django-nose',
    'django-pagination',
    'django-tagging',
    'feedparser',
    'gdata',
    'gunicorn',
    'mimeparse',
    'mimms',
    'python-social-auth',
    'nose',
    'oauth',
    'pil',
    'pyth',
    'python-dateutil',
    'python-memcached',
    'python-openid',
    'vobject',
    'django-tastypie',
    'django-ratings',

]

setup(
    name="Open-Knesset",
    version="0.1",
    url='http://github.com/ofri/Open-Knesset',
    description="Bringing transperancy to the Israeli Knesset",
    author='Ofri Raviv and others',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Hebrew',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript'
    ],
)
