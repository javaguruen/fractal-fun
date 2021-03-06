def mapToRed(data, width, height):
    colored = []
    for pixel in range(width * height):
        colored.append( ( min(255, 16 * data[pixel]), 0, 0) )
    return colored


def mapToBlue(data, width, height):
    colored = []
    for pixel in range(width * height):
        colored.append( ( 0, 0, min(255, 16 * data[pixel])) )
    return colored