import numpy as np
import matplotlib.pyplot as plt
import pyqtree

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)

spindex = pyqtree.Index(bbox=[0,-100,100,400])

items = []
for i in range(1, len(x)):
	#print x.item(i), y.item(i)
	obj = lambda:None
	obj.x = x.item(i)
	obj.y = y.item(i)
	obj.bbox = [x.item(i)-0.5, y.item(i)-0.5, x.item(i)+0.5, y.item(i)+0.5]
	items.append(obj)

#this example assumes you have a list of items with bbox attribute
for item in items:
    spindex.insert(item=item, bbox=item.bbox)

overlapbbox = (51,51,86,186)
matches = spindex.intersect(overlapbbox)

#for m in matches:
#	print m.bbox

def drawbox(x, y, x1, y1, color):
	plt.plot([x, x1], [y, y], color)
	plt.plot([x, x1], [y1, y1], color)
	plt.plot([x, x], [y, y1], color)
	plt.plot([x1, x1], [y, y1], color)

def drawtree(node):
	#print(len(node.children), len(node.nodes))
	if len(node.children) == 4: 
		for child in node.children:
			plt.plot([child.center[0] - child.width/2, child.center[0] + child.width/2], [child.center[1], child.center[1]], 'k-')
			plt.plot([child.center[0], child.center[0]], [child.center[1] - child.height/2, child.center[1] + child.height/2], 'k-')
			drawbox(child.center[0] - child.width/2, child.center[1] - child.height/2, child.center[0] + child.width/2, child.center[1] + child.height/2, 'r-')
			drawtree(child)
	else:
		for elem in node.nodes:
			#print(elem.item.bbox)
			pass

plt.plot(x, y, "o")

drawtree(spindex)
# Boundaries -- not necessary
#plt.plot([spindex.center[0] - spindex.width, spindex.center[0] - spindex.width], [spindex.center[1] - spindex.height, spindex.center[1] + spindex.height], color='k', linestyle='-', linewidth=2)
#plt.plot([spindex.center[0] + spindex.width, spindex.center[0] + spindex.width], [spindex.center[1] - spindex.height, spindex.center[1] + spindex.height], color='k', linestyle='-', linewidth=2)
#plt.plot([spindex.center[0] - spindex.width, spindex.center[0] + spindex.width], [spindex.center[1] - spindex.height, spindex.center[1] - spindex.height], color='k', linestyle='-', linewidth=2)
#plt.plot([spindex.center[0] - spindex.width, spindex.center[0] + spindex.width], [spindex.center[1] + spindex.height, spindex.center[1] + spindex.height], color='k', linestyle='-', linewidth=2)

#plt.plot([70, 70], [100, 250], 'k-', lw=2)	# draw vertical line from (70,100) to (70, 250)
#plt.plot([70, 90], [90, 200], 'k-')		# draw diagonal line from (70, 90) to (90, 200)

plt.show()

