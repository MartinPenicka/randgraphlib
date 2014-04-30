randgraphlib
============

Randgraphlib is python library for generating random graphs in given format.

Status: ACTIVE
--------------

Under active development and maintenance.

Ideas behind this project
-------------------------

 - If you need to test some graph algorithm, you need to create lots of random graphs. Goal of this project is one library for generating graph with literary any given parameter (tree, graph with clique, graph colorable with n colors, etc.).
 - Generating graph in library format (adjacency matrix at this time) and in the future in any user given format.
 - Generation driven by config file and config consistency checking (e.g., graph cannot be tree and has clique >= 3)

Installation
------------

At this moment you must add whole library to your project. In the future -> setup.py and by pip.

Quickstart
----------