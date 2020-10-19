import MandelBrot
import ColorMapper
import Matplotlib
from PIL import Image

height = 100
width = 100
center = (0.0, 0.0)
radius = 2.0
px = MandelBrot.draw(center[0], center[1], radius, 100, height, width)
imageData = ColorMapper.mapToRed(px, width, height)

Matplotlib.showImage(imageData, (width, height), (center[0]-radius, center[0]+radius, center[1]+radius, center[1]-radius))
im2 = Image.new('RGB', (width,height))
im2.putdata(imageData)
im2.save('c:/temp/mandel.png')