# Enter your code here. Read input from STDIN. Print output to STDOUT

def build_set():
    a = int(raw_input())
    a_str = raw_input()
    a_list = map(int, a_str.split())
    a_set = set(a_list)
    return a_set

one = build_set()
two = build_set()

diff_one = one.difference(two)
diff_two = two.difference(one)

diff = diff_one.union(diff_two)

diff_list = [x for x in diff]
diff_list = sorted(diff_list)

for i in diff_list:
    print i