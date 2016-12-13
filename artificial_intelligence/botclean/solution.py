def find_closest(root, nodes):
	'''Finds the closest node to the root from a list of nodes. '''
	min_dist = None
    
	for node in nodes:
		dist = abs(node[0]-root[0]) + abs(node[1]-root[1])

		if min_dist == None:
			result  = node
			min_dist = dist
		elif dist < min_dist:
			result = node
			min_dist = dist

	return result
    
def find_dirty(board):
    '''Returns a list of dirty nodes. '''
    dirty = []
    for posr in range(0, len(board)):
        for posc in range(0, len(board[posr])):
            if board[posr][posc] == 'd':
                dirty.append((posr, posc))
    return dirty

def move_bot(posr, posc, board):
    '''Move bot towards closest dirty node if one exists. '''
    dirty = find_dirty(board)
    
    if len(dirty) > 0:
        closest = find_closest((posr, posc), dirty)
        board[posr][posc] = '-'
        
        if posr < closest[0]:
            board[posr+1][posc] = 'b'
            print('DOWN')
        elif posr > closest[0]:
            board[posr-1][posc] = 'b'
            print('UP')
        elif posc < closest[1]:
            board[posr][posc+1] = 'b'
            print('RIGHT')
        elif posc > closest[1]:
            board[posr][posc-1] = 'b'
            print('LEFT')
    
def next_move(posr, posc, board):
    '''Clean up node if dirty, or move to another node. '''
    if board[posr][posc] == 'd':
        board[posr][posc] = '-'
        print('CLEAN')
    else:
        move_bot(posr, posc, board)
                
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
