test_cases = int(raw_input())

def move_cube(origin, destination, side):
	''' Moves a cube from origin to destination '''
	if side == 'right':
		move_cube = origin.pop(len(origin)-1)
	else:
		move_cube = origin.pop(0)
	destination.append(move_cube)

def stackable(cur_cubes, stacked_cubes):
	''' Determine if cubes are stackable '''

	while len(cur_cubes) > 0:

		top_cube = stacked_cubes[len(stacked_cubes)-1]
		left_cube = cur_cubes[0]
		right_cube = cur_cubes[len(cur_cubes)-1]

		if (right_cube <= top_cube) and (left_cube <= top_cube): # If both cubes are stackable 
			if right_cube > left_cube:
				move_cube(cur_cubes, stacked_cubes, 'right')
			else:
				move_cube(cur_cubes, stacked_cubes, 'left')

		elif (right_cube <= top_cube) and (left_cube > top_cube): # If right cube is stackable
			move_cube(cur_cubes, stacked_cubes, 'right')

		elif (right_cube > top_cube) and (left_cube <= top_cube): # If left cube is stackable
			move_cube(cur_cubes, stacked_cubes, 'left')

		else:
			return 'No'

	return 'Yes'

for _ in xrange(0, test_cases):
	num_cubes = int(raw_input())
	cubes = [int(x) for x in raw_input().strip().split()]
	print stackable(cubes, [max(cubes)])