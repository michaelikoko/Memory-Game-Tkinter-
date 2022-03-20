from random import shuffle
from tkinter import *
from tkinter.messagebox import *
import os

class Memory_Game:
    def __init__(self) -> None:
        self.coordinates = []
        cur_dir = os.getcwd()
        self.tileFilePath = [
            f'{cur_dir}\\tiles\\c#.gif',
            f'{cur_dir}\\tiles\\c++.gif',
            f'{cur_dir}\\tiles\\c.gif',
            f'{cur_dir}\\tiles\\java.gif',
            f'{cur_dir}\\tiles\\js.gif',
            f'{cur_dir}\\tiles\\matlab.gif', 
            f'{cur_dir}\\tiles\\php.gif',
            f'{cur_dir}\\tiles\\python.gif',
            f'{cur_dir}\\tiles\\ruby.gif', 
            f'{cur_dir}\\tiles\\swift.gif'
        ]
        self.tileImg = [PhotoImage(file=f) for f in self.tileFilePath]
        self.movesLeft = 30
        self.moves = StringVar()
        self.moves.set(f'{self.movesLeft} moves left')
        self.count = 0
        self.movesLabel = Label(textvariable=self.moves, fg='blue', font='Sans-serif 16 bold roman')
        self.tileNum = [i for i in range(10)]*2 
        shuffle(self.tileNum)
        self.astBoard = [['*' for col in range(4)]for row in range(5)]
        self.grayImg = PhotoImage(file='C:\\Users\\hp\\OneDrive\\Documents\\PROGRAMMING\PYTHON\\.vscode\\TKINTER\\Memory_Game\\tiles\\plain.gif')
        self.tileNumBoard = [[self.tileNum[4*i + j] for j in range(4)] for i in range(5)]
        shuffle(self.tileNumBoard)
        self.buttons = [[0 for c in range(4)] for r in range(5)]
        for r in range(5):
            for c in range(4):
                self.buttons[r][c] = Button(image=self.grayImg, command= lambda row=r, col=c: self.callback(row, col))
                self.buttons[r][c].grid(row = r, column = c)
        self.movesLabel.grid(row=5, column=0, columnspan=4)
        print(self.tileNumBoard)

    def printState(self):
        for r in self.astBoard:
            for i in r:
                print(i, end=' ')
            print()

    def callback(self, r, c):
        if self.astBoard[r][c] == '*':
            self.count += 1     
            self.coordinates += [r,c]
            self.flipTile(r, c)
            self.astBoard[r][c] = self.tileNumBoard[r][c]
            root.update()
            if self.count == 2:
                r1, c1, r2, c2 = self.coordinates
                if self.tileNumBoard[r1][c1] != self.tileNumBoard[r2][c2]:
                    root.after(500, self.reverseFlip(r1, c1, r2, c2))
                    self.astBoard[r1][c1] = '*'
                    self.astBoard[r2][c2] = '*'
                else:
                    pass
                self.movesLeft -= 1
                self.moves.set(f'{self.movesLeft} moves left.' if self.movesLeft > 1 else f'{self.movesLeft} move left.')
                self.coordinates = []
                self.count = 0
            self.winOrLoss()
            self.printState()

    def flipTile(self, r, c):
        n = self.tileNumBoard[r][c]
        self.buttons[r][c].configure(image=self.tileImg[n])

    def reverseFlip(self, r1, c1, r2, c2):
        self.buttons[r1][c1].configure(image=self.grayImg)
        self.buttons[r2][c2].configure(image=self.grayImg)        

    def winOrLoss(self):
        if self.movesLeft == 0 and self.astBoard != self.tileNumBoard:
            print('Out of moves')
            self.showAll()
            ans = askokcancel(title='Out of moves!', message='You have ran out of moves!\nDo you want to play again?')
            createObject(ans)
        elif self.astBoard == self.tileNumBoard:
            print('You win')
            ans = askokcancel(title='You win!' ,message='You win!\nDo you want to play again?')
            createObject(ans)

    def showAll(self):
        for r in range(5):
            for c in range(4):
                n = self.tileNumBoard[r][c]
                self.buttons[r][c].configure(image = self.tileImg[n])                    

def quitterFunction():
    ans = askquestion(title='Quit?', message='Do you really want to quit?')
    if ans == 'yes':
        root.destroy()

root = Tk()
root.title('Memory Tiles')
root.protocol('WM_DELETE_WINDOW', quitterFunction)
def createObject(ans):
    if ans == True:
        memGame = Memory_Game()
    else:
        root.destroy()

if __name__ == '__main__':
    createObject(True)
mainloop()
