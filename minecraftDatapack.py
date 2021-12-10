from hilbertsCurve import hilbertsCurve
import numpy as np

def create(size, multiplier=None):
	if multiplier == None:
		multiplier = 1

	print(f'Size: {size}')
	grid = np.zeros(shape=(2 ** size * 3, 2 ** size * 3))

	grid = grid.tolist()

	for i in range(len(grid)):
		for j in range(len(grid)):
			grid[i][j] = 1

	print('Generating curve...')
	curve = hilbertsCurve(size)

	print('Generating grid...')
	for i in range(len(curve)):
		grid[curve[i][0] * 3 + 1][curve[i][1] * 3 + 1] = 0
		

		if i == 0:
			grid[curve[i][0] * 3][curve[i][1] * 3 + 1] = 0
		elif curve[i - 1][0] < curve[i][0]:
			grid[curve[i][0] * 3][curve[i][1] * 3 + 1] = 0
		elif curve[i - 1][0] > curve[i][0]:
			grid[curve[i][0] * 3 + 2][curve[i][1] * 3 + 1] = 0
		elif curve[i - 1][1] < curve[i][1]:
			grid[curve[i][0] * 3 + 1][curve[i][1] * 3] = 0
		elif curve[i - 1][1] > curve[i][1]:
			grid[curve[i][0] * 3 + 1][curve[i][1] * 3 + 2] = 0
		
		if i == len(curve) - 1:
			grid[curve[i][0] * 3 + 2][curve[i][1] * 3 + 1] = 0
		elif curve[i + 1][0] < curve[i][0]:
			grid[curve[i][0] * 3][curve[i][1] * 3 + 1] = 0
		elif curve[i + 1][0] > curve[i][0]:
			grid[curve[i][0] * 3 + 2][curve[i][1] * 3 + 1] = 0
		elif curve[i + 1][1] < curve[i][1]:
			grid[curve[i][0] * 3 + 1][curve[i][1] * 3] = 0
		elif curve[i + 1][1] > curve[i][1]:
			grid[curve[i][0] * 3 + 1][curve[i][1] * 3 + 2] = 0

	print('Writing to file...')
	with open(f'{size}_{multiplier}x.mcfunction', 'w') as f:
		result = ''
		#result += 'setblock ~ ~10 ~ barrier\ntp @s ~ ~11 ~\n'
		#result += f'fill ~ ~ ~ ~{2 ** size * 3 - 1} ~ ~{2 ** size * 3 - 1} stone_bricks\n'
		#result += f'fill ~ ~1 ~ ~{2 ** size * 3 - 1} ~1 ~{2 ** size * 3 - 1} stone_bricks\n'
		#result += f'fill ~ ~2 ~ ~{2 ** size * 3 - 1} ~2 ~{2 ** size * 3 - 1} stone_bricks\n'
		for i in range(len(grid)):
			for j in range(len(grid)):
				result += f'fill ~{i*multiplier} ~-1 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~3 ~{j*multiplier + multiplier - 1} stone_bricks\n'
				if grid[i][j] == 0:
					result += f'fill ~{i*multiplier} ~0 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~2 ~{j*multiplier + multiplier - 1} air\n'
				else:
					#result += f'fill ~{i*multiplier} ~0 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~2 ~{j*multiplier + multiplier - 1} stone_bricks\n'
					#if not i == 0 and not j == 0 and not i == len(grid) - 1 and not j == len(grid) - 1:
					result += f'fill ~{i*multiplier} ~2 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~2 ~{j*multiplier + multiplier - 1} glowstone\n'
					result += f'fill ~{i*multiplier} ~3 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~3 ~{j*multiplier + multiplier - 1} air\n'
					result += f'fill ~{i*multiplier} ~-1 ~{j*multiplier} ~{i*multiplier + multiplier - 1} ~-1 ~{j*multiplier + multiplier - 1} air\n'
		result += f'tp ~ ~ ~{j*multiplier - 1}\n'
		result += 'tellraw @s {"text": "Finished!", "color": "green"}'
		f.write(result)
	print('Done!')

if __name__ == '__main__':
	create(int(input('Size: ')))