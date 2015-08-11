L = []

while True:
    try:
        n = int(raw_input())
    except ValueError:
        print 'Invalid integer, please try again'
    else:
        break

def scan(list):
    cmd = list[0]
    if cmd == 'insert':
        L.insert(int(list[1]), int(list[2]))
    elif cmd == 'remove':
        L.remove(int(list[1]))
    elif cmd == 'append':
        L.append(int(list[1]))
    elif cmd == 'pop':
        L.pop()
    elif cmd == 'reverse':
        L.reverse()
    elif cmd == 'sort':
        L.sort()
    elif cmd == 'print':
        print L
    else:
        print 'Inavlid command, please try again'
        scan(raw_input().split(' '))
    
for i in range(0, n):
    commands = raw_input().split(' ')
    scan(commands)