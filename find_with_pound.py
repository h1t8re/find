def find_with_pound(unit, space):
	coordinate = []
	Pound = 0
	for (dimension, pound) in space:
		if not isinstance(dimension, list):
			if dimension == unit:
				coordinate.append(space.index((dimension, pound)))
				Pound = Pound +pound
				yield coordinate, pound
			else:
				pass
		else:
			for coord, Pound in find_with_pound(unit, dimension):
				Pound = Pound + pound
				coord.append(space.index((dimension, pound)))
				yield coord, Pound

def main():
	array = [( [([([([(0, 1)], 1)], 2)], 1)], 1)]
	print(array)
	result = []
	for coordinate, weight in find_with_pound(0, array):
		result.append((weight, coordinate[::-1]))
	print(result)

if __name__ == "__main__":
	main()
