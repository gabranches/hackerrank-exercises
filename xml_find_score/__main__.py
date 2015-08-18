import xml.etree.ElementTree as etree

n = int(raw_input())
xml = ""
score = 0

for _ in range(0, n):
    xml += raw_input()

tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()

def getScore(root):

	global score
	
	for _ in root.attrib:
		score += 1

	for child in root:
		getScore(child)

getScore(root)

print score