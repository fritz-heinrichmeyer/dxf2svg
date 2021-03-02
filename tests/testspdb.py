#import  dxf2svg 
#import *
#import dxf2svg.pycore as dxf2svg 
#import os

#test_dxf_path = os.path.join(os.path.dirname(__file__), 'entwurf0.dxf')
#---
#dxf2svg.save_svg_from_dxf(test_dxf_path, frame_name='drawing1')
#dxf2svg.save_svg_from_dxf(test_dxf_path, frame_name='spam')
#dxf2svg.save_svg_from_dxf(test_dxf_path)
#dxf2svg.extract_all(test_dxf_path)

# from testspdb import *
def pdb(e):
 #   for e in dxf.modelspace():
 #           point = None
  from ezdxf.colors import DXF_DEFAULT_COLORS, int2rgb
   rgb24 = DXF_DEFAULT_COLORS[3]
    print(f'RGB Hex Value: #{rgb24:06X}')#:  RGB Hex Value:   #00FF00
   
     print (e.dxftype())
     return 42
     if e.dxftype() == 'LINE':
         point = slice_l2(e.dxf.start)
         print ('LINE')
     if e.dxftype() == 'CIRCLE': point = slice_l2(e.dxf.center)
     if e.dxftype() == 'TEXT': point = slice_l2(e.dxf.insert)
#     if e.dxftype() == 'ARC':

if __name__ == "__main__":
     print ('tschüßß')
# pdb(0)

