string = raw_input()
substr = raw_input()
counter = 0

for i in range(0, len(string) - len(substr) + 1):
	if string[i:i+len(substr)] == substr:
		counter += 1

print counter