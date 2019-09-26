import msvcrt
class player:
    def __init__(self, name, field):
        self.name = name
        self.row = 0
        self.col = 0
        self.field = field

    def move(self, direction):
        self.field.move(self, direction)
        

class gameField:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        line1 = []
        line2 = []
        self.field = []
        self.string = ''
        for i in range(col + 1):
            if(i < col):
                line1.append('+------')
                line2.append('|      ')
            else:
                line1.append('+\n')
                line2.append('|\n')

        for j in range(2 * row + 1):
            if(j % 2 == 0):
                self.field.append(line1[:])
            else:
                self.field.append(line2[:])

    def draw(self):
        self.string = ''
        for i in self.field:
            for j in i:
                self.string += j
        print(self.string)

    def add(self, player, row, col):
        if(row > self.row or col > self.col):
            return
        self.field[2 * row - 1][col - 1] = '|  ' + player.name[0] + '   '
        player.row = row
        player.col = col
        
    def remove(self, player, row, col):
        if(row > self.row or col > self.col):
            return
        self.field[2 * row - 1][col - 1] = '|      '
        player.row = 0
        player.col = 0

    def move(self, player, direction):
        if(direction == 'up'):
            if(player.row == 1):
                return
            else:
                tmprow = player.row
                tmpcol = player.col
                self.remove(player, player.row, player.col)
                self.add(player, tmprow - 1, tmpcol)
        if(direction == 'down'):
            if(player.row == self.row):
                return
            else:
                tmprow = player.row
                tmpcol = player.col
                self.remove(player, tmprow, tmpcol)
                self.add(player, tmprow + 1, tmpcol)
        if(direction == 'left'):
            if(player.col == 1):
                return
            else:
                tmprow = player.row
                tmpcol = player.col
                self.remove(player, player.row, player.col)
                self.add(player, tmprow, tmpcol - 1)               
        if(direction == 'right'):
            if(player.col == self.col):
                return
            else:
                tmprow = player.row
                tmpcol = player.col
                self.remove(player, player.row, player.col)
                self.add(player, tmprow, tmpcol + 1)


    def addPlayer(self, newplayer, row, col):
        self.add(newplayer, row, col)
        
if __name__ == "__main__":

    myfield = gameField(10,10)
    xiaoming = player('xiaoming', myfield)
    myfield.addPlayer(xiaoming,5,9)
    myfield.draw()
    
    while(1):

        cmd = input()
        if(cmd == 'w'):
            xiaoming.move('up')
        elif(cmd == 'a'):
            xiaoming.move('left')
        elif(cmd == 's'):
            xiaoming.move('down')
        elif(cmd == 'd'):
            xiaoming.move('right')
        myfield.draw()
