==============================
Dxf2svg - dxf to svg converter
==============================

Dxf2svg is a dxf to svg format converter.
This project is a **fork** from https://bitbucket.org/lukaszlaba/dxf2svg

(from Lukasz Laba <lukaszlab@o2.pl>)


Changelog
---------

dxf2svg 0.1.2

- first public release (alfa stage) 
- LINE, CIRCE, TEXT dxf entity supported
- all entities go to one linetype, color and weight

Requirements
------------
1. svgwrite (https://pypi.python.org/pypi/svgwrite)
#. ezdxf (https://pypi.python.org/pypi/ezdxf)

How to install
--------------

(according to https://python-packaging.readthedocs.io/en/latest/)::

   git clone https://github.com/fritz-heinrichmeyer/dxf2svg.git
   cd dxf2svg
   pip install .

(*local*)

oder::
  
   pip install -e .

(*symlink,handy for tests*)

.. Dxf2svg is available through PyPI and can be install with pip command. To install dxf2svg and needed requiremen   ts use pip by typing ::
   pip install svgwrite ezdxf dxf2svg

Using dxf2svg
-------------
The syntax of the dxf2svg command is ::

  dxf2svg dxffilename [size]

In the most simple case, set the current directory to the location of your drwing.dxf and execute::

  dxf2svg drwing.dxf

you can also specife output svg size you want, for example ::

  dxf2svg drwing.dxf 300

After that you will get output svg files in the same directory where your drwing.dxf is.

Limitation
----------
At the moment not all dxf entitles type are supported during converting. It convert LINE, CIRCE, TEXT and all those entities go to one linetype, color and weight.

Licence
-------
Dxf2svg is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Copyright (C) 2018 Lukasz Laba <lukaszlab@o2.pl>

Contributions
-------------
If you want to help out, create a pull request or write email.

More information
----------------
Project website(old): https://bitbucket.org/lukaszlaba/dxf2svg

Code repository(new): https://github.com/fritz-heinrichmeyer/dxf2svg

PyPI package: https://pypi.python.org/pypi/dxf2svg

Contact(old): Lukasz Laba <lukaszlab@o2.pl>

Contact(new): Fritz Heinrichmeyer <Fritz.Heinrichmeyer@gmail.com>
