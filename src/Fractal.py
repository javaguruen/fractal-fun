import MandelBrot
import ColorMapper
from PIL import Image

height = 1000
width = 1000
px = MandelBrot.draw(-0.75, 0.1, 0.01, 200, height, width)
imageData = ColorMapper.mapToRed(px, width, height)
# for h in range(height):
#    print( imageData[h * height: h*height+width])
im2 = Image.new('RGB', (width,height))
im2.putdata(imageData)
im2.save('c:/temp/mandel.png')