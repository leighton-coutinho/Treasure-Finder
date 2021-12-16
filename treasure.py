#Leighton Coutinho Student ID:261016919
def load_treasure_map(filename):
    ''' (str) --> (list)
    >>> load_treasure_map('map0.txt')
    [['>', '>', '>', 'v', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'v', '.', '.', '.', '<', '<', '.'],
    ['.', '.', '.', 'v', '.', '.', '.', '.', '.', '.'],
    ['v', '.', '.', 'v', '.', '.', '.', '.', '^', '.'],
    ['v', '.', '.', '>', '>', '*', '.', '.', '^', '.'],
    ['v', '.', '.', '.', '.', '.', '.', '.', '^', '.']]
    '''
    validchars = ['X','v','>','<','^','.','*','|','1','2','3','4','5','6','7','8','9']
    treasure_map = open(filename, "r") 
    file_content = treasure_map.read()
    line = []
    map1 = []
    #need to add AssertionError part for other exceptions
    #function returns a map that is missing the last row
    for i in range(len(file_content)):
        if file_content[i] == '\n':
            map1.append(line)
            line = []
        else:
            line.append(file_content[i])
            if i == (len(file_content)-1):
                map1.append(line)
                
            
    
    treasure_map.close()
    for i in map1:
        for j in i:
            if j not in validchars:
                raise AssertionError('Invalid file format for a treasure map')
    return map1


def write_treasure_map(treasure_map, filename):
    ''' (list,str) --> (None)
    This function will write a list called treasure map to a
    text file and save this as a new file with
    the name as the string in the
    argument filename
    >>> my_map = load_treasure_map('map0.txt')
    >>> write_treasure_map(my_map, 'new_map.txt')
    >>> my_map2 = load_treasure_map('new_map.txt')
    >>> my_map == my_map2
    True
    '''
    newmap = open(filename, "w")
    mylines = ''
    for line in treasure_map:
        mylines += ''.join(line) + '\n'
        
    newmap.write(mylines) # write line to file
    newmap.close()
 
def write_X_to_map(filename, row, col):
    ''' (str,num,num) --> (None)
    This funcions will take a string of the filename and
    numbers corresponding to the rows and columns of the map
    it will then insert an X in this position and save this in
    a new file with new_ appended to the original name
    >>> write_X_to_map('map8.txt', 3, 6)
    >>> f = open('new_map8.txt', 'r')
    >>> for line in f:
    print(line.strip())
    >>v......v
    ..v......v
    ..v.......
    ..>>>>X...
    ..........
    ..^v^...<<
    >>> f.close()
    '''
    newmap = load_treasure_map(filename)
    newmap[row][col] = 'X'
    newfilename = 'new_' + filename
    write_treasure_map(newmap, newfilename)
    
def follow_trail(filename, treasure_map, start_row, start_col):
    ''' (str,list,num,num) --> (tuple)
    This funcions will take a string of the filename, a list
    representing a map as well as numbers corresponding to the
    starting row and column of the map. It will then follow the
    trail at the point and return a tuple based on which
    characters it encounters
    >>> my_map = load_treasure_map('map0.txt')
    >>> follow_trail('map0.txt', my_map, 0, 0)
    (1, 4, 5)
    >>> my_map = load_treasure_map('map1.txt')
    >>> follow_trail('map1.txt', my_map, 4, 5)
    (8, 0, 0)
    >>> my_map = load_treasure_map('map8.txt')
    >>> follow_trail('map8.txt', my_map, 0, 0)
    (-1, 3, 6)
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
           NEED TO ADD MY OWN 3 EXAMPLES HERE
    '''
    row = start_row
    column = start_col
    count = 0
    while row < (len(treasure_map)):
        while column < (len(treasure_map[row])):
            count +=1
            if count > 150:
                raise AssertionError("Infinite loop due to invalid directions(e.g ><)")
            if treasure_map[row][column] == '>':
                column += 1
            elif treasure_map[row][column] == '<':
                column -= 1
            elif treasure_map[row][column] == 'v':
                row += 1
            elif treasure_map[row][column] == '^':
                row -= 1
            elif treasure_map[row][column] == '.':
                write_X_to_map(filename, row, column)
                return (-1,row,column)
            elif treasure_map[row][column] == '*':
                nextmap = int(filename[-5]) + 1
                return (nextmap,row,column)
            elif treasure_map[row][column] in ['0','1','2','3','4','5','6','7','8','9']:
                nextmap = int(treasure_map[row][column])
                return (nextmap,0,0)
            else:
                raise AssertionError("Invalid Character")
        
        #Dealing with going off the path
            if row == 0 and treasure_map[row][column] == '^':
                raise AssertionError('Going off the grid')
            elif row == (len(treasure_map)-1) and treasure_map[row][column] == 'v':
                raise AssertionError('Going off the grid')
            elif column == (len(treasure_map[row])-1) and treasure_map[row][column] == '>':
                raise AssertionError('Going off the grid')
            elif column == (0) and treasure_map[row][column] == '<':
                raise AssertionError('Going off the grid')


def find_treasure(start_map_num):
    ''' (num) --> (tuple)
    This funcions will take a number corresponding to a map number,
    it will start at 0,0 in the grid and follow the trail through
    the maps untill it finds the treasure, it will then return the
    column and row of the treasure position as a tuple
    >>> find_treasure(0)
    (3, 6)
    >>> my_map = load_treasure_map('new_map8.txt')
    >>> my_map[3][6]
    'X'
    '''
    filename = 'map' + str(start_map_num) + '.txt'
    finaltuple = (0,0,0)
    row = 0
    column = 0
    while finaltuple[0] != -1:
        mymap = load_treasure_map(filename)
        finaltuple = follow_trail(filename, mymap, row, column)
        if finaltuple[0] == (int(filename[-5]) + 1):
            filename = 'map' + str(finaltuple[0]) + '.txt'
            row = finaltuple[1]
            column = finaltuple[2]
        elif finaltuple[1:] == (0,0):
            filename = 'map' + str(finaltuple[0]) + '.txt'
            row = 0
            column = 0
            
    return finaltuple[1:]



        
