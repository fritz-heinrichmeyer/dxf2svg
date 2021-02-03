import  dxf2svg 
#import *
import dxf2svg.pycore as test
import os

test_dxf_path = os.path.join(os.path.dirname(__file__), 'drawing.dxf')
#---
test.save_svg_from_dxf(test_dxf_path, svgfilepath=0, frame_name='drawing1', size=300)
test.save_svg_from_dxf(test_dxf_path, svgfilepath=0, frame_name='spam', size=300)
test.save_svg_from_dxf(test_dxf_path)
test.extract_all(test_dxf_path, size=300)