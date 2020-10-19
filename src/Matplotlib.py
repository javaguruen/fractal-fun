import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def showImage(data, dim, extent):
    width = dim[0]
    height = dim[1]
    mappedData = []
    for h in range(height):
        row = []
        for w in range(width):
            pixel = data[h*height + w]
            row.append([pixel[0]/255.0, 0.0, 0.0 ])
        mappedData.append(row)

    fig = plt.figure()
    imgplot = plt.imshow(mappedData, extent=extent)
#    plt.axhspan(-2, 2)
#    plt.axvspan(-2, 2)
    plt.show()