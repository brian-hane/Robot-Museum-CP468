'''
Created on Nov 29, 2018

@author: Nathan
'''
import dataStructures


def aStar(enviro, startList, rendev):
    '''
    A* implementation to traverse a 2D discrete environment
    Parameters:
    enviro: nested list (a 2D array), so enviro[y][x] is the format
    startlist: list of 2 value lists, each start is listed in [x , y]
    rendev: single list of 2 values, in order [x, y]

    returns:
    list of all solutions
    each element is a pair of values
    solution[0][0]: the start location for the first solution
    solution[0][1]: the list of moves taken from the start to the rendevous point, is None if no solution found
    solution[1]: the solution pair for the second starting location, if any

    '''
    allSolutions = []

    for botStart in startList:
        nodeQueue = dataStructures.PriorityQueue()
        # create the start node for the robot
        startNode = dataStructures.Node(
            botStart, enviro[botStart[1]][botStart[0]], None, rendev)
        nodeQueue.push(startNode)
        # set up the priority queue, and the first node, the start node

        visited = {}  # to store squares that have been added to the priority queue

        for y in range(len(enviro)):
            visited[y] = {}
            for x in range(len(enviro[y])):
                #visited[y][x] = 0
                # ? copy enviro so walls automatically omitted
                visited[y][x] = enviro[y][x]
        # initiate the visited list

        visited[botStart[1]][botStart[0]] = 4
        # indicate the starting square has been visited

        while (nodeQueue.length > 0):  # while there are still unexplored nodes

            curr = nodeQueue.pop()  # get the first element in the queue
            if curr is None:
                # there are no remaining nodes in the list
                break

            if curr.x == rendev[0] and curr.y == rendev[1]:
                # solution has been found
                break
            else:
                visited[curr.y][curr.x] = 3
                # 3 indicates expanded node

            if curr.x > 0 and visited[curr.y][curr.x - 1] == 0:
                nodeQueue.push(dataStructures.Node(
                    [curr.x - 1, curr.y], enviro[curr.y][curr.x - 1], curr, rendev))
                # if not against a wall on the left side, push to queue
                visited[curr.y][curr.x - 1] = 2
                # set the value to show it has been added to the queue
                # value 2 indicates it has been added as part of the frontier

            if curr.x < (len(enviro[0]) - 1) and visited[curr.y][curr.x + 1] == 0:
                nodeQueue.push(dataStructures.Node(
                    [curr.x + 1, curr.y], enviro[curr.y][curr.x + 1], curr, rendev))
                # if not against a wall on the right side, push to queue
                visited[curr.y][curr.x + 1] = 2

            if curr.y > 0 and visited[curr.y - 1][curr.x] == 0:
                nodeQueue.push(dataStructures.Node(
                    [curr.x, curr.y - 1], enviro[curr.y - 1][curr.x], curr, rendev))
                # if not against a wall on the top side, push to queue
                visited[curr.y - 1][curr.x] = 2

            if curr.y < (len(enviro) - 1) and visited[curr.y + 1][curr.x] == 0:
                nodeQueue.push(dataStructures.Node(
                    [curr.x, curr.y + 1], enviro[curr.y + 1][curr.x], curr, rendev))
                # if not against a wall on the bottom side, push to queue
                visited[curr.y + 1][curr.x] = 2

        if curr is None or curr.x != rendev[0] or curr.y != rendev[1]:
            # solution was not found
            allSolutions.append([botStart, None])
            # add none to the solution list
        else:
            # solution was found

            solution = []
            while curr.x != botStart[0] or curr.y != botStart[1]:
                # while the start node has not been found
                solution.insert(0, [curr.x, curr.y])
                # insert node at front of list, results in start node being
                # first, and goal node being last
                curr = curr.prevNode
                # backtrack to previous node

            solution.insert(0, [curr.x, curr.y])  # insert the starting node in
            allSolutions.append([botStart, solution])
            # add the solution to the solution list

    return allSolutions


if __name__ == '__main__':

    # temp hardcoding for testing purposes
    enviro = []
    startList = []
    rendev = []
    '''
    #Assignment example
    enviro.append([1,0,0,0,0,0,0,0,0,1])
    enviro.append([1,1,0,0,0,0,0,0,1,1])
    enviro.append([0,0,0,0,0,0,0,0,0,0])
    enviro.append([1,0,0,0,1,1,0,0,0,1])
    enviro.append([1,0,0,1,1,1,1,0,0,1])
    enviro.append([0,0,0,1,1,1,1,0,0,0])
    enviro.append([0,0,0,0,1,1,0,0,0,0])
    enviro.append([1,1,0,0,0,0,0,0,1,1])
    #defined as y, x

    startList.append([2,1])
    startList.append([8,2])
    
    rendev = [4, 7]
    '''
    '''
    #test case for unsolvable enviroment
    enviro.append([0,0,1])
    enviro.append([0,1,0])
    enviro.append([1,0,0])
    
    startList.append([0,0])
    
    rendev = [2,2]
    '''

    solutions = aStar(enviro, startList, rendev)
    for sol in solutions:
        print(sol)
