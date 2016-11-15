Project 01: DrawIt
==================

The first project is to create **DrawIt**, a simple drawing package for
composing two-dimensional images in [PPM] format.

Overview
--------

The project has the following layout:

    drawit
        \_ drawit                           DrawIt Python Package
                \_ __init__.py
                \_ color.py                 DrawIt Color Module
                \_ image.py                 DrawIt Image Module
                \_ point.py                 DrawIt Point Module
                \_ ppm.py                   DrawIt PPM Module
                \_ tests                    DrawIt Tests
                    \_ color_tests.py       DrawIt Color Module Tests
                    \_ image_tests.py       DrawIt Image Module Tests
                    \_ point_tests.py       DrawIt Point Module Tests
        \_ draw_circle.py                   Circle Demo Script
        \_ draw_freight_train.py            Freight Train Demo Script
        \_ draw_line.py                     Line Demo Script
        \_ draw_point.py                    Point Demo Script
        \_ draw_rectangle.py                Rectangle

For this project, you only need to modify the following the `color.py`,
`image.py`, and `point.py` files.

Tests
-----

To run the unit tests, you can use the [unittest] module as follows:

    $ python -m unittest -v drawit.tests
    test00_ColorInit (drawit.tests.color_tests.ColorTest) ... ok
    test01_ColorEq (drawit.tests.color_tests.ColorTest) ... ok
    test02_ColorStr (drawit.tests.color_tests.ColorTest) ... ok
    test03_ColorGlobals (drawit.tests.color_tests.ColorTest) ... ok
    test00_ImageInit (drawit.tests.image_tests.ImageTest) ... ok
    test01_ImageEq (drawit.tests.image_tests.ImageTest) ... ok
    test02_ImageStr (drawit.tests.image_tests.ImageTest) ... ok
    test03_ImageGetItem (drawit.tests.image_tests.ImageTest) ... ok
    test03_ImageSetItem (drawit.tests.image_tests.ImageTest) ... ok
    test04_ImageClear (drawit.tests.image_tests.ImageTest) ... ok
    test05_ImageLine (drawit.tests.image_tests.ImageTest) ... ok
    test06_ImageRectangle (drawit.tests.image_tests.ImageTest) ... ok
    test07_ImageCircle (drawit.tests.image_tests.ImageTest) ... ok
    test00_PointInit (drawit.tests.point_tests.PointTest) ... ok
    test01_PointStr (drawit.tests.point_tests.PointTest) ... ok
    test02_PointStr (drawit.tests.point_tests.PointTest) ... ok
    test03_PointDistanceFrom (drawit.tests.point_tests.PointTest) ... ok

    ----------------------------------------------------------------------
    Ran 17 tests in 5.369s

    OK

For your convenience, you can also use the following command:

    $ make test

Scripts
-------

In addition to the unit tests, you are also provided a few example demo
scripts.  The first few scripts demonstrate each of the drawing primitives:
    
    $ ./draw_point.py > draw_point.ppm

![draw_point](http://www3.nd.edu/~pbui/teaching/cdt.30020.sp16/static/img/draw_point.png)

    
    $ ./draw_line.py > draw_line.ppm

![draw_line](http://www3.nd.edu/~pbui/teaching/cdt.30020.sp16/static/img/draw_line.png)
    
    $ ./draw_rectangle.py > draw_rectangle.ppm

![draw_rectangle](http://www3.nd.edu/~pbui/teaching/cdt.30020.sp16/static/img/draw_rectangle.png)

    $ ./draw_circle.py > draw_circle.ppm

![draw_circle](http://www3.nd.edu/~pbui/teaching/cdt.30020.sp16/static/img/draw_circle.png)

One special script, demonstrates how you can put all of these things together
to make a pretty cool image:

    $ ./draw_freight_train.py > draw_freight_train.ppm

![draw_freight_train](http://www3.nd.edu/~pbui/teaching/cdt.30020.sp16/static/img/draw_freight_train.png)

For your convenience, you can run all of these scripts at once by doing:

    $ make ppms

This will generate [PPM] files that you can view.  If you prefer [PNG] files,
you can do the following instead:

    $ make pngs

To `make` a single image, you can do:

    $ make draw_line.png

**Note**: The `make` commands will automatically run any script that begins
with `draw_`, so if you use that prefix for your scripts, then you can also use
the `make` command.

[unittest]: https://docs.python.org/2/library/unittest.html
[PPM]:      https://en.wikipedia.org/wiki/Netpbm_format
