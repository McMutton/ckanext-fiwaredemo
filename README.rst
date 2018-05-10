
=============
ckanext-fiwaredemo
=============


------------
Requirements
------------

CKAN 2.7


------------
Installation
------------

To install ckanext-fiwaredemo:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-fiwaredemo Python package into your virtual environment::

     pip install ckanext-fiwaredemo

3. Add ``fiwaredemo`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

------------------------
Development Installation
------------------------

To install ckanext-fiwaredemo for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/"McMutton"/ckanext-fiwaredemo.git
    cd ckanext-fiwaredemo
    python setup.py develop
    pip install -r dev-requirements.txt
