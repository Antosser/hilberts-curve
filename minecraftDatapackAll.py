import minecraftDatapack

def main():
	for i in range(1, 7):
		for j in (1, 2, 4, 8):
			minecraftDatapack.create(i, j)

if __name__ == '__main__':
	main()