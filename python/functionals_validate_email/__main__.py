import re

emails = []
valid_emails = []

n = int(raw_input())

for _ in range(0, n):
	emails.append(raw_input())

for address in emails:
    p = re.compile(r'^[-_a-z0-9]+@[a-z0-9]+\.\w{1,3}$', re.I)
    m = p.match(address)
    if m:
        valid_emails.append(address)

print sorted(valid_emails)