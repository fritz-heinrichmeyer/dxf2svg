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
def arc(center):
  #center=(10,10)
  arc_start= 30
  arc_end= 150
  p= Path(d=f"M {10 * math.cos(math.pi *arc_start/180 ) +center[0] } {10 * math.sin(math.pi * arc_start/180) +center[1]} ")
  target=(10 * math.cos(math.pi *arc_end/180 ) +center[0], 10 * math.sin(math.pi * arc_end/180)+center[1])
  p.push_arc(target=(10 * math.cos(math.pi *arc_end/180 ) +center[0], 10 * math.sin(math.pi * arc_end/180)+center[1]), rotation=30, r=(10,10), large_arc=True, angle_dir='-', absolute=True)
  # p.push("l 10 10 ")


  svg_entity = svgwrite.Drawing().path(d=p.commands,stroke="blue", stroke_width="1", fill="none")
  ergebnis = svg_entity._repr_svg_()
  return ergebnis
if __name__ == "__main__":
     punkte = [(10,10), (30,30), (60,60)]
     zeichung =""
     for punkt in punkte:
       zeichung += arc(punkt) + "\n "
     print(zeichung)    
# pdb(0)

