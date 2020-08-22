.. _home:

Open Data API
===============

Welcome to **Open Data API** project documentation page.

Open Data API (abbreviated to :py:mod:`odapi`) is a Python3 package providing
a generic interfaces on top of multiple data sources and data models in
order to abstract their differences and manipulate them in a standardized way.

Open Data API mainly standardizes Time Series and Geomatic management using
the powerful `Pandas`_ DataFrame object under the hood.

.. _Pandas: https://pandas.pydata.org/

Open Data API also defines flexible interfaces to control how data model and flow
are built and enforce quality and consistency of connectors developments.

Contents
--------

Open Data API documentation decomposes as follow:

.. toctree::
   Quick Start Guide <pages/quickstart.rst>
   Connectors <pages/connectors.rst>
   Interfaces <pages/interfaces.rst>
   Toolbox <pages/toolbox.rst>
   Exceptions <pages/errors.rst>
   Sources <pages/sources.rst>
   :maxdepth: 1


Installation
------------

Open Data API uses classic `setuptools`_ flow, to install the package
just follow the usual procedure:

.. _setuptools: https://setuptools.readthedocs.io/en/latest/

.. code-block:: bash

   python3 setup.py install

The package repository is available at https://github.com/jlandercy/odapi.

A KISS interface
----------------

We aim to fit with the KISS principle. Download time series data with
Open Data API package is as easy as:

.. literalinclude:: pages/resources/scripts/home_example.py
   :language: python
   :linenos:

This light-weight snippet above download the last seven days of
Nitrogen Oxides for Brussels from the Irceline Air Quality SOS API.

Documentation
-------------

Learn more about how the package is built and works:

 - Visit our :ref:`Quick Start Guide<quickstart>`
 - Use existing APIs defined in :ref:`Connectors<connectors>`
 - Define new APIs using :ref:`Interfaces<interfaces>`
 - Choose the right method from the :ref:`Toolbox<toolbox>`
 - Read references about :ref:`Sources<sources>` and underlying APIs

Indices
-------

Navigate through the package structure:

 - :ref:`Search<search>` for a specific object
 - See object references using the :ref:`Index<genindex>`
 - See package namespace using the :ref:`Module Index<modindex>`
