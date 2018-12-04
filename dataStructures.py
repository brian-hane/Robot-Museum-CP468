'''
Created on Nov 29, 2018

@author: Nathan
'''



class Node(object):
    '''
    node representing a given discrete coordinate
    '''
    
    def __init__(self, startCoord, nodeType, prevNode, rendevous):
        self.x = startCoord[0]
        self.y = startCoord[1] #x,y coordinate for this node 
        
        self.nodeType = nodeType #describes if it is a wall or tile
        
        self.prevNode = prevNode #this node's ancestor
    
        if prevNode is not None: #None indicates start node
            self.gCost = prevNode.gCost + 1 #cost from start is cost from prev node plus 1, as all moves have cost 1
        else:
            self.gCost = 0
        '''    
        if nodeType is 1:
            self.hcost = 999999
        else:
        '''
        self.hCost = abs(rendevous[0] - self.x) + abs(rendevous[1] - self.y) #estimate cost based on straight line heuristic
        
        self.fCost = self.gCost + self.hCost #total function cost is gCost + hCost
        
        
class PriorityNode(object):
    '''
    container for normal node
    '''
    
    def __init__(self, n, prevNode, nextNode):
        self.node = n #container for base nodes
        self.prevNode = prevNode 
        self.nextNode = nextNode #nodes for linked list
    
    
class PriorityQueue(object):
    '''
    priority queue
    '''

    def __init__(self):
        self.length = 0
        self.start = None
        
        
    def push(self, node):#node used is base node, not priorityNode
        if self.start is None:
            n = PriorityNode(node, None, None)
            self.start = n
            self.length = 1 #if queue is empty, set new node to start, set length to 1
        else:
            '''
            if node.nodeType == 1:
                break;#if the node is a wall, don't add it to the queue
            ''' #depends on where walss are to be omitted
            curr = self.start
            
            if node.fCost < curr.node.fCost:
                #if the new node has a lower fCost than the first node in list
                pNode = PriorityNode(node, None, curr)
                curr.prevNode = pNode
                self.start = pNode
                self.length =+ 1
                return
                
            while (curr.nextNode is not None):
                if curr.nextNode.node.fCost > node.fCost:
                    break #if the next item fCost is greater than the node fCost, then the previous must be less, and the node should be inserted
                else:
                    curr = curr.nextNode
                    #will exit when end of queue reached, if end reached, it will be inserted there
                
            if curr == self.start:#if inserting at start of priority queue
                pNode = PriorityNode(node, None, curr)
                self.start.prevNode = pNode
                self.start = pNode #if the new node has a lower f cost than the start node, replace the start node

            elif curr.nextNode is not None:#if inserting anywhere other than start or end
                pNode = PriorityNode(node, curr, curr.nextNode)
                curr.nextNode.prevNode = pNode
                curr.nextNode = pNode
                
            else:#if inserting at the end of the priority queue
                pNode = PriorityNode(node, curr, None)
                curr.nextNode = pNode
                
            self.length += 1 #insert the node
            
    def pop(self): #return node at top of priority
        if self.start is None:
            return None
        else:
            temp = self.start
            self.start = temp.nextNode
            self.length -= 1
            return temp.node
