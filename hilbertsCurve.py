import numpy

def hilbertsCurve(size):
	if size < 1:
		raise Exception('The fuck? I cannot do that. Size needs to be 1 or higher')
		return
	if size == 1:
		return [[0, 1], [0, 0], [1, 0], [1, 1]]
	
	smaller = hilbertsCurve(size - 1)
	result = []

	currentSmaller = numpy.copy(smaller).tolist()
	for i in range(len(currentSmaller)):
		currentSmaller[i][1] *= -1
		currentSmaller[i][1] += (2 ** (size - 1)) - 1
		currentSmaller[i] = currentSmaller[i][::-1]
		currentSmaller[i][1] *= -1
		currentSmaller[i][1] += (2 ** (size - 1)) - 1
		currentSmaller[i][1] += (2 ** size) / 2
	result += currentSmaller
	
	result += smaller

	currentSmaller = numpy.copy(smaller).tolist()
	for i in range(len(currentSmaller)):
		currentSmaller[i][0] += (2 ** size) / 2
	result += currentSmaller

	currentSmaller = numpy.copy(smaller).tolist()
	for i in range(len(currentSmaller)):
		currentSmaller[i] = currentSmaller[i][::-1]
		currentSmaller[i][1] += (2 ** size) / 2
		currentSmaller[i][0] += (2 ** size) / 2
	result += currentSmaller

	for i in range(len(result)):
		result[i][0] = int(result[i][0])
		result[i][1] = int(result[i][1])

	return result

# hilbertsCurve(3)