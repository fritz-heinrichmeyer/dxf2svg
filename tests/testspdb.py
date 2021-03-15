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
svgKopf = """<?xml version="1.0" standalone="no"?>
<svg width="10cm" height="5.25cm" viewBox="0 0 1000 600"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
  <title>Example arcs01 - arc commands in path data</title>
  <title>Example arcs01 - arc commands in path data</title>
  <desc>Picture of a pie chart with two pie wedges and
     https://www.w3.org/TR/SVG/paths.html#PathDataEllipticalArcCommands
     https://www.december.com/html/spec/colorsvg.html
     https://de.wikipedia.org/wiki/Scalable_Vector_Graphics#Pfad
     http://jsfiddle.net/DFhUF/1393/
        a picture of a line with arc blips</desc>
  <rect x="1" y="1" width="1198" height="398"
        fill="none" stroke="blue" stroke-width="5" />
<path d="M 275 175 v -150 a150 150 0 0 0 -150 150 z"
        fill="yellow" stroke="blue" stroke-width="2px" />

"""
print(svgKopf)


def arc(center):
  center=center
  arc_start= 150
  arc_end= 30
  radius =center[2]
  #p= Path(d=f"M {center[0]} {center[1]}")
  p=Path(d=[])
  current_a = (-(radius * math.cos(math.pi * (arc_start/180.0 ))) +center[0], -(radius * math.sin(math.pi * (arc_start/180.0))) +center[1])
  
  #p.push(f"M {(radius * math.cos(math.pi *arc_start/180.0 )) +center[0] } {(radius * math.sin(math.pi * arc_start/180.0)) +center[1] } ")
  #p.push(f"M 0 0 L 0 0 {center[0]} {center[1]} ")
  p.push(f"M {current_a[0]} {current_a[1]} L {center[0]} {center[1]}  {current_a[0]} {current_a[1]} ")
  target=( -(radius * math.cos(math.pi * (arc_end/180.1) )) +center[0], -(radius * math.sin(math.pi * (arc_end/180.1)))+center[1] )
  p.push_arc(target, rotation=0, r=radius, large_arc=False , angle_dir='-', absolute=True)
  p.push(f" L {target[0]} {target[1]} ")
  
  p.push(f"L {target[0]} {target[1]} {center[0]} {center[1]}")


  svg_entity = svgwrite.Drawing().path(d=p.commands,stroke="blue", stroke_width="1", fill="none")
  ergebnis = svg_entity._repr_svg_()
  return ergebnis
if __name__ == "__main__":
     print("\n ")
     punkte = [(100,80,10), (200,80,20), (300,80,40)]
     zeichung =""
     for punkt in punkte:
       zeichung += arc(punkt) + "\n "
     print(zeichung)    
# pdb(0)
svgFuss = """</svg>
"""
print(svgFuss)


