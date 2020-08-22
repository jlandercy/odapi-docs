Toolbox
=======

.. automodule:: odapi.toolbox

Time Series
-----------

This module provides commodities to handle Time Series.
Typical outputs is shown below:

 .. image:: resources/figures/ecdf.png
   :width: 480
   :alt: Time Series ECDF

 .. image:: resources/figures/autocorr.png
   :width: 480
   :alt: Time Series Auto-Correlation

 .. image:: resources/figures/profile.png
   :width: 480
   :alt: Time Series Week Profiles

.. automodule:: odapi.toolbox.timeseries
.. autoclass:: odapi.toolbox.timeseries.TimeSeries
   :members:
   :special-members: __init__


Psychrometry
------------

This module provides classes to draw Psychrometric Chart for Water/Air mixture.
A typical output is shown below:

 .. image:: resources/figures/psychro.png
   :width: 480
   :alt: Wind Bins Mapping

.. automodule:: odapi.toolbox.psychro
   :members:


Weather
-------

.. automodule:: odapi.toolbox.weather
.. autoclass:: odapi.toolbox.weather.Weather
   :members:
   :special-members: __init__

Wind
####

This class provides methods to cope with Wind Speed time series. Wind Speed is essentially a vector
quantity. Which is generally decomposed into three scalar quantities:

 - Wind Direction (expressed by convention in azimuthal coordinate with direction associated on where the wind blows from);
 - Scalar Mean Speed (the mean of the norms of the speed);
 - Vector Mean Speed (the norm of mean speed).

Those three quantities contains enough information to recreate an average Wind Speed vector and
assess Wind Speed stability during the averaging period.

It is important to underline the direction coordinate is by convention not expressed in the
trigonometric system but in goniometric system (goniometry is the science of direction finding).
The figure below shows a Wind Rose with related `Azimuthal`_ coordinates:

.. _Azimuthal: https://en.wikipedia.org/wiki/Azimuth

.. image:: https://upload.wikimedia.org/wikipedia/commons/6/61/Kompassrose.svg
   :width: 300
   :alt: Goniometric Coordinates

The transformation between trigonometric and goniometric system is equivalent to:

 :math:`x_\mathrm{trigo} = 90^\circ - x_\mathrm{gonio}`

It means goniometric and trigonometric angles are complementary, so they have their origins shifted
by a right angle and their coordinates are moving in opposite directions.

Also notice that the transformation between coordinate systems is an `involution`_.

.. _involution: https://en.wikipedia.org/wiki/Involution_%28mathematics%29

.. .. image:: https://upload.wikimedia.org/wikipedia/commons/c/c9/Unit_circle_angles.svg
  :width: 200
  :alt: Angles

.. .. image:: https://upload.wikimedia.org/wikipedia/commons/1/1a/Brosen_windrose.svg
   :width: 200
   :alt: Wind Rose

The algorithm used to define Wind Direction bins from Goniometric angles is summarized on
the figure below:

 .. image:: resources/figures/windbins.png
   :width: 680
   :alt: Wind Bins Mapping

Typical outputs is shown below:

 .. image:: resources/figures/windbox.png
   :width: 380
   :alt: Wind Box Plots

 .. image:: resources/figures/windrose.png
   :width: 380
   :alt: Wind Rose

.. autoclass:: odapi.toolbox.weather.Wind
   :members:
   :special-members: __init__

Humidity
########

.. autoclass:: odapi.toolbox.weather.Humidity
   :members:
   :special-members: __init__

Sun
###

.. autoclass:: odapi.toolbox.weather.Sun
   :members:
   :special-members: __init__

