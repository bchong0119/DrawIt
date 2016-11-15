''' color_tests.py: DrawIt color tests '''

import unittest

import drawit.color

# Color Unit Test

class ColorTest(unittest.TestCase):

    def test00_ColorInit(self):
        color = drawit.color.Color()
        self.assertTrue(color.r == 0 and color.g == 0 and color.b == 0)
        
        color = drawit.color.Color(1, 2, 3)
        self.assertTrue(color.r == 1 and color.g == 2 and color.b == 3)
        
        color = drawit.color.Color(g=1, b=2, r=3)
        self.assertTrue(color.r == 3 and color.g == 1 and color.b == 2)
    
    def test01_ColorEq(self):
        color0 = drawit.color.Color()
        color1 = drawit.color.Color()
        self.assertTrue(color0 == color1)
        
        color0 = drawit.color.Color(1, 2, 3)
        color1 = drawit.color.Color(r=1, g=2, b=3)
        self.assertTrue(color0 == color1)

    def test02_ColorStr(self):
        color = drawit.color.Color()
        self.assertTrue(str(color) == 'Color(r=0,g=0,b=0)')
        
        color = drawit.color.Color(1, 2, 3)
        self.assertTrue(str(color) == 'Color(r=1,g=2,b=3)')

        color = drawit.color.Color(g=1, b=2, r=3)
        self.assertTrue(str(color) == 'Color(r=3,g=1,b=2)')

    def test03_ColorGlobals(self):
        self.assertTrue(drawit.color.BLACK == drawit.color.Color())
        self.assertTrue(drawit.color.WHITE == drawit.color.Color(
            r = drawit.color.RED.r,
            g = drawit.color.GREEN.g,
            b = drawit.color.BLUE.b,
        ))
        self.assertTrue(drawit.color.WHITE == drawit.color.Color(
            r = drawit.color.MAGENTA.r,
            g = drawit.color.CYAN.g,
            b = drawit.color.MAGENTA.b,
        ))
        self.assertTrue(drawit.color.WHITE == drawit.color.Color(
            r = drawit.color.YELLOW.r,
            g = drawit.color.YELLOW.g,
            b = drawit.color.CYAN.b,
        ))

        self.assertTrue(len(drawit.color.COLORS) > 2)

# Main Execution

if __name__ == '__main__':
    unittest.main()
