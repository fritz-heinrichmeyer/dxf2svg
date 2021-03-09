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
#pp e.dxf.lineweight, e.dxf.thickness
# from testspdb import *
from svgwrite.path import Path
import svgwrite
import math
center=(10,10)
arc_start= 30
arc_end= 150
p= Path(d=f"M {10 * math.cos(math.pi *arc_start/180 ) +center[0] } {10 * math.sin(math.pi * arc_start/180) +center[1]} ")
target=(10 * math.cos(math.pi *arc_end/180 ) +center[0], 10 * math.sin(math.pi * arc_end/180)+center[1])
p.push_arc(target=(10 * math.cos(math.pi *arc_end/180 ) +center[0], 10 * math.sin(math.pi * arc_end/180)+center[1]), rotation=30, r=center, large_arc=True, angle_dir='-', absolute=True)


svg_entity = svgwrite.Drawing().path(d=p.commands,stroke="blue", stroke_width="0.01")
print (svg_entity._repr_svg_())
print (svg_entity.commands)
print (p.commands)

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

