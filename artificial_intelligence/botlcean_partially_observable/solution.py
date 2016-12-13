import random

def find_closest(root, nodes):
    '''Finds the closest node to the root from a list of nodes. '''
    if len(nodes) == 0:
        return None
    
    min_dist = None
    for node in nodes:
        dist = abs(node[0]-root[0]) + abs(node[1]-root[1])
        
        if min_dist == None:
            result  = node
            min_dist = dist
        elif dist <= min_dist:
            result = node
            min_dist = dist
            
    return result
    
def find_all(board, kind):
    '''Returns a list of all nodes of a certain kind. '''
    result = []
    for posr in range(0, len(board)):
        for posc in range(0, len(board[posr])):
            if board[posr][posc] == kind:
                result.append((posr, posc))
    return result

def rand_node(nodes):
    return random.sample(nodes, 1)[0]

def move_bot(posr, posc, board, target):
    '''Move bot towards closest node. '''
    if posr < target[0]:
        print('DOWN')
    elif posr > target[0]:
        print('UP')
    elif posc < target[1]:
        print('RIGHT')
    elif posc > target[1]:
        print('LEFT')
    
def next_move(posr, posc, board):
    '''Clean up node if dirty, or move to another node. '''
    if board[posr][posc] == 'd':
        print('CLEAN')
    else:
        dirty = find_closest((posr, posc), find_all(board, 'd'))
        # Move towards dirty node
        if dirty:
            move_bot(posr, posc, board, dirty)
        # If no dirty nodes, move towards invisible node
        else:
            move_bot(posr, posc, board, rand_node(find_all(board, 'o')))
                
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
