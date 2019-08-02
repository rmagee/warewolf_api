=============================
warewolf_api
=============================

.. image:: https://gitlab.com/serial-lab/warewolf_api/badges/master/coverage.svg
   :target: https://gitlab.com/serial-lab/warewolf_api/pipelines
.. image:: https://gitlab.com/serial-lab/warewolf_api/badges/master/build.svg
   :target: https://gitlab.com/serial-lab/warewolf_api/commits/master
.. image:: https://badge.fury.io/py/warewolf_api.svg
    :target: https://badge.fury.io/py/warewolf_api

The API layer for W4R3W0LF

Documentation
-------------

The full documentation is at https://serial-lab.gitlab.io/warewolf_api/

Quickstart
----------

Install warewolf_api::

    pip install warewolf_api

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'warewolf_api.apps.WarewolfApiConfig',
        ...
    )

Add warewolf_api's URL patterns:

.. code-block:: python

    from warewolf_api import urls as warewolf_api_urls


    urlpatterns = [
        ...
        url(r'^', include(warewolf_api_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

