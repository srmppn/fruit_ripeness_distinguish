from PIL import Image
import os

index = 1

for filename in os.listdir('D:\\3 picture'):

    # reset threshold values
    avgR = 0
    avgB = 0
    avgG = 0

    if filename.endswith('.jpg'):
        img = Image.open('D:\\3 picture\\' + str(index) + '.jpg')
        img.show()
        pixels = img.load()  # create the pixel map
        sumR = 0
        sumG = 0
        sumB = 0
        count = 0
        for i in range(img.size[0]):  # for every pixel:
            for j in range(img.size[1]):
                sumR += pixels[i, j][0]
                sumG += pixels[i, j][1]
                sumB += pixels[i, j][2]
                count += 1

        avgR = sumR / count
        avgG = sumG / count
        avgB = sumB / count

        if avgR / avgG < 1:
            os.rename("D:\\3 picture\\" + str(index) + '.jpg', "D:\\3 picture\\raw\\" + str(index) + '.jpg')
        elif avgR / avgG < 1.2 and avgR / avgB < 2:
            os.rename("D:\\3 picture\\" + str(index) + '.jpg', "D:\\3 picture\\ripe\\" + str(index) + '.jpg')
        elif avgR / avgG < 1.36 and avgR / avgB < 2.5:
            print('Ripe')
        else:
            print('Very ripe')

    index += 1


