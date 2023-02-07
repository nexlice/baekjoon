import sys

# readline method
ssr = sys.stdin.readline

# get square's side's length
length = int(ssr())

# generate map for the squre
zido = [[0 for _ in range(length)] for _ in range(length)]

# read one line and change the map.
for i in range(length):
    tmp = ssr()
    for j in range(length):
        zido[i][j] = int(tmp[j])

# Define Shape for labeling
class Shape:
    def __init__(self, nextShape = None, nextNode = None):
        self.nextShape = nextShape
        self.nextNode = nextNode

# Define Node
class Node:
    def __init__(self, x = None, y = None, nextNode = None):
        self.nextNode = nextNode
        self.x = x
        self.y = y

Head = Shape()

queue = []

# find near 8 pixels
def find(x, y):

    # set variables as global.
    global queue
    global zido
    global Head
    global length
    curr = Head
    # if queue is empty, create new object.
    if len(queue) == 0:

        # move curr to the last shape.
        while(curr.nextShape != None):
            curr = curr.nextShape
        
        # append this coordinate to the queue.
        queue.append((x, y))

        # create Node to this shape.
        curr.nextShape = Shape()
        curr = curr.nextShape
        curr.nextNode = Node(x, y)
    
    else:
        assert("the queue should be empty at the beginning of the call.")

    # search near 8 pixels while queue is not empty.
    while len(queue) != 0:
        element = queue.pop()

        for i in range(3):            
            # if x index is out of range, continue.
            if element[0] + i - 1  < 0 or element[0] + i - 1 >= length:
                continue

            for j in range(3):
                # if it is diagonal, continue.
                if (i == 0 and j == 0) or (i == 0 and  j == 2) or (i == 2 and j == 0) or (i == 2 and j ==2):
                    continue
                # if y index is out of range, continue.
                if element[1] + j - 1  < 0 or element[1] + j - 1 >= length:
                    continue
                
                # if the pixel is 0, continue.
                if zido[element[0] + i - 1][element[1] + j - 1] == 0:
                    continue

                # if the pixel is 1, create Node and convert it to 0.
                else:
                    zido[element[0] + i - 1][element[1] + j - 1] = 0
                    curr.nextNode = Node(element[0] + i - 1, element[1] + j - 1)
                    queue.append((element[0] + i - 1, element[1] + j - 1))
                    curr = curr.nextNode




# traverse entire map.
for x in range(length):
    for y in range(length):
        if zido[x][y] == 1:
            find(x, y)

# find total object numbers
numObj = 0
currObj = Head

while(currObj.nextShape != None):
    currObj = currObj.nextShape
    numObj += 1

print(numObj)

# find size of each objects.
listSize = []
numSize = 0
currObj = Head
currNode = Node()

while currObj.nextShape != None:
    currObj = currObj.nextShape
    currNode = currObj

    while currNode.nextNode != None:
        currNode = currNode.nextNode
        numSize += 1
    listSize.append(numSize)
    numSize = 0

listSize.sort()

for element in listSize:
    print(element)