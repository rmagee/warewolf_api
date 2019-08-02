=====
Usage
=====

To use warewolf_api in a project, add it to your `INSTALLED_APPS`:

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
