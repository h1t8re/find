def find(unit, space):
	coordinate = []
	for dimension in space:
		if not isinstance(dimension, list):
			if dimension == unit:
				coordinate.append(space.index(dimension))
				yield coordinate
			else:
				pass
		else:
			for coord in find(unit, dimension):
				coord.append(space.index(dimension))
				yield coord

def main():
	array = [1, [[2], 3], 4]
	print("The space is: ", end="\n")
	print(array)
	for i in range(1, 5):
		print("The coordinate of "+str(i)+" are: ", end="")
		for x in find(i, array):
			print(x[::-1], end="\n")

if __name__ == "__main__":
	main()
