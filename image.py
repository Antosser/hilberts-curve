from PIL import Image
import PIL
from hilbertsCurve import hilbertsCurve
import colorsys
import numpy

def generate(size):
	im = PIL.Image.new('RGB', ((2 ** size) * 3, (2 ** size) * 3), 'black')

	curve = hilbertsCurve(size)

	for i in range(len(curve)):
		color = colorsys.hsv_to_rgb(i / len(curve) * 2 / 3, 1, 1)
		color = numpy.asarray(color).tolist()
		for j in range(3):
			color[j] *= 255
			color[j] = int(color[j])
		color = tuple(color)

		im.putpixel((curve[i][0] * 3 + 1, curve[i][1] * 3 + 1), color)

		if i == 0:
			im.putpixel((curve[i][0] * 3, curve[i][1] * 3 + 1), color)
		elif curve[i - 1][0] < curve[i][0]:
			im.putpixel((curve[i][0] * 3, curve[i][1] * 3 + 1), color)
		elif curve[i - 1][0] > curve[i][0]:
			im.putpixel((curve[i][0] * 3 + 2, curve[i][1] * 3 + 1), color)
		elif curve[i - 1][1] < curve[i][1]:
			im.putpixel((curve[i][0] * 3 + 1, curve[i][1] * 3), color)
		elif curve[i - 1][1] > curve[i][1]:
			im.putpixel((curve[i][0] * 3 + 1, curve[i][1] * 3 + 2), color)
		
		if i == len(curve) - 1:
			im.putpixel((curve[i][0] * 3 + 2, curve[i][1] * 3 + 1), color)
		elif curve[i + 1][0] < curve[i][0]:
			im.putpixel((curve[i][0] * 3, curve[i][1] * 3 + 1), color)
		elif curve[i + 1][0] > curve[i][0]:
			im.putpixel((curve[i][0] * 3 + 2, curve[i][1] * 3 + 1), color)
		elif curve[i + 1][1] < curve[i][1]:
			im.putpixel((curve[i][0] * 3 + 1, curve[i][1] * 3), color)
		elif curve[i + 1][1] > curve[i][1]:
			im.putpixel((curve[i][0] * 3 + 1, curve[i][1] * 3 + 2), color)

	im.save('image.png')

if __name__ == '__main__':
	generate(int(input('Size: ')))