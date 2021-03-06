========================
Django Elasticsearch 
========================

.. image:: https://badge.fury.io/py/django-elasticsearch-dsl.svg
    :target: https://pypi.python.org/pypi/django-elasticsearch-dsl

This is a package that allows indexing of django models in elasticsearch. It is
built as a thin wrapper around elasticsearch-dsl-py_ so you can use all the features developed
by the elasticsearch-dsl-py team.


Features
--------

- Java SE Downloads JDK http://www.oracle.com/technetwork/java/javase/downloads/index.html

- Download Elasticsearch https://www.elastic.co/downloads/past-releases/elasticsearch-5-6-8

- Based on elasticsearch-dsl-py_ so you can make queries with the Search_ class.
- Django signal receivers on save and delete for keeping Elasticsearch in sync.
- Management commands for creating, deleting, rebuilding and populating indices.
- Elasticsearch auto mapping from django models fields.
- Complex field type support (ObjectField, NestedField).
- Requirements
   - Django >= 1.8
   - Python 2.7, 3.4, 3.5, 3.6
   - Elasticsearch >= 2.0 < 7.0

.. _Search: http://elasticsearch-dsl.readthedocs.io/en/stable/search_dsl.html


Quickstart
----------

Install Virtualenv::

    sudo pip3 install virtualenv

    virtualenv venv

    source venv/bin/activate or deactivate

    pip install -r requirements.txt

    python manage.py makemigrations blog

    python manage.py migrate

    python manage.py search_index --rebuild



Quickstart
----------

Install Django Elasticsearch DSL::

    pip install django-elasticsearch-dsl

    # Elasticsearch 6.x
    pip install 'elasticsearch-dsl>=6.0,<7.0'

    # Elasticsearch 5.x
    pip install 'elasticsearch-dsl>=5.0,<6.0'

    # Elasticsearch 2.x
    pip install 'elasticsearch-dsl>=2.1,<3.0'

Then add ``django_elasticsearch_dsl`` to the INSTALLED_APPS

You must define ``ELASTICSEARCH_DSL`` in your django settings.