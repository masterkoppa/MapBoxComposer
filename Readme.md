MapBoxComposer
-------------

This is the home of a small script that will allow you to compose and stick images from
a MapBox created image.

Purpose
-------
Initially the whole purpose of this was to fix a small problem I saw with a website. 
The awesome people at Tele Geography created a interactive version of their 
[Submarine Cable Map]
(http://www.telegeography.com/telecom-maps/submarine-cable-map/index.html).
The only problem was that it was extremely slow to load tiles when zoomed in at any level.
After countless minutes of frustration I decided to try and reverse engineer the whole thing
to download the images and compose them myself for fast browsing. The result is this set 
of scripts that you see here.


Future
------
In the future the plan is to expand this to compose any interactive map or image that 
uses the [MapBox](https://github.com/mapbox).


This is a work in progress...


Files Purpose
------------

DownloadTiles.py
================

Generates a Makefile that will use wget to download the 
tiles using the original folder structure.

Makefile
========
Downloads all the tiles based on the instructions set in DownloadTiles.py

The whole purpose of this is to speed up the process and make it more realistic
to the server just in case. Additionally its extremely fast to do so in parralel using
the -j flags.


FixFilenames.py
===============
When using any * completion the shell will detect 2 as being larger than 10,
because its a string comparison. Since the server gives me the files as
1 and not 01, this script fixes this issue.

StichFolder.py
==============
This script will run through each folder and do the vertical stiching required
to join all the images.  
  
TODO: As soon as all the vertical stiching is done then do the horizontal stiching.  
TODO: Since each folder is completely independent from each other and the whole
      process takes long then we should turn it into a Makefile and use the -j flag
      or make it parallel in some other way.
      
