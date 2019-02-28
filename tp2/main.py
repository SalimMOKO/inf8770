import ycbcr_converter as ycbcr
import bloc_divider as bdiv
import matplotlib.pyplot as py

image = py.imread('fjords.jpg').astype('float')

code420 = ycbcr.RGBtoYCbCr420(image)
decode420 = ycbcr.YCbCr420toRGB(code420)
py.imshow(decode420)
py.show()

code444 = ycbcr.RGBtoYCbCr444(image)
decode444 = ycbcr.YCbCr444toRGB(code444)
py.imshow(decode444)
py.show()

blocs = bdiv.divider8by8(image)
imageReconstruite = bdiv.rebuildFrom8by8(blocs)
py.imshow(imageReconstruite)
py.show()