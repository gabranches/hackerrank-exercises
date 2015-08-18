import xml.etree.ElementTree as etree

n = int(raw_input())
xml = ""
max_depth = 0

for _ in range(0, n):
    xml += raw_input()

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

def getDepth(root, cur_depth):

	global max_depth

	if cur_depth > max_depth:
		max_depth = cur_depth

	for child in root:
		getDepth(child, cur_depth + 1)


getDepth(root, 0)

print max_depth
