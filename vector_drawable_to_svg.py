"""
Convert android vector drawable to svg.

Note:
	- Color and dimen references wwill not work as the value is didrectly
      extracted from the vector drawable. Use hard-coded values
"""

import xml.etree.ElementTree as ET

vec_filename = 'filename.xml'
svg_filename = 'filename.svg'
vec_xmlns = '{http://schemas.android.com/apk/res/android}'

vec = ET.parse(vec_filename).getroot()

svg_attrib = {
    'xmlns': 'http://www.w3.org/2000/svg',
    'width': vec.get(vec_xmlns + 'width')[:-2],
    'height': vec.get(vec_xmlns + 'height')[:-2],
    'viewBox': '0 0 {} {}'.format(vec.get(vec_xmlns + 'viewportWidth'), vec.get(vec_xmlns + 'viewportHeight'))
}

svg = ET.Element('svg', attrib=svg_attrib)

for vec_path in vec.iter('path'):
    svg_path_attrib = {
        'fill': vec_path.get(vec_xmlns + 'fillColor', 'none'),
        'd': vec_path.get(vec_xmlns + 'pathData')
    }
    svg_path = ET.SubElement(svg, 'path', attrib=svg_path_attrib)

    stroke_color = vec_path.get(vec_xmlns + 'strokeColor')
    if not stroke_color == None:
        svg_path.set('stroke', stroke_color)

    stroke_width = vec_path.get(vec_xmlns + 'strokeWidth')
    if not stroke_width == None:
        svg_path.set('stroke-width', stroke_width)

    fill_type = vec_path.get(vec_xmlns + 'fillType')
    if not fill_type == None:
        svg_path.set('fill-rule', fill_type)

with open(svg_filename, "w") as svg_file:
    svg_file.write(ET.tostring(svg).decode('utf-8'))
