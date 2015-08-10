# Enter your code here. Read input from STDIN. Print output to STDOUT

stdin = [raw_input().split() for _ in range(0,2)]
num_list = map(int,stdin[1])

def get_max(num_list, M=None):
    S = set(num_list)
    L = [x for x in S]

    if M <> None:   
        L.remove(M)
        get_max(L)

    return max(L)

M = get_max(num_list, max(num_list))

print M