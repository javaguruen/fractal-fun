import ColorMapper

# let xkoord = 0;
# let ykoord = 0;
# let r =  4;
# let maxiterations = 1000;

def draw(centerX, centerY, radius, maxiterations, imageHeight, imageWidth):
    print("draw()")
    # background(255, 0, 0);
    # loadPixels();
    pixels = []

    width = radius * 2.0
    height = width * imageHeight / imageWidth

    startX = centerX - width / 2.0
    startY = centerY + height / 2.0

    dx = (width) / (imageWidth)
    dy = (height) / (imageHeight)

    print("imageWidth = ", imageWidth)
    print("imageHeight = ", imageHeight)
    print("width = ", width)
    print("height = ", height)
    print("startX = ", startX)
    print("startY = ", startY)
    print("dx = ", dx)
    print("dy = ", dy)

    for ph in range(imageHeight):
        y = startY - ph * dy
        for pw in range(imageWidth):
            x = startX + pw * dx

            a = 0
            b = 0
            iter = 0
            while iter < maxiterations and a * a + b * b < 4:
                aa = a * a
                bb = b * b
                twoab = 2.0 * a * b
                a = aa - bb + x
                b = twoab + y
                iter += 1
            if iter == maxiterations:
                pixels.append(0)
            else:
                pixels.append(iter)
    return pixels
