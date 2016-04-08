#!/usr/bin/python

from Tkinter import *
from string import letters, lowercase
import random
import time
import os
import sys

from words import worddatabase
i = [0]


def placeatcenter(window, title):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.wm_title(title)
    x = screen_width / 2 - 500 / 2
    y = screen_height / 2 - 400 / 2
    window.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    window.config(background='white')
    window.resizable(width=FALSE, height=FALSE)


def gameover(winorloss, wordslist):

    def quitgame():
        os.system('rm *.pyc')
        root.destroy()
        hm.destroy()

    class endgame:

        def playagain(self):
            root.destroy()
            hm.deiconify()
            placeatcenter(hm, 'HangMan 2.0')
            hm.drawman()
            hm.setword()
            hm.update()

        def quit(self):
            quitgame()
            sys.exit()
            root.destroy()

        def newgame(self):
            hm.destroy()
            root.withdraw()
            os.system('python hangman.py')
            root.destroy()

        def __init__(
            self,
            master,
            winorloss,
            wordslist,
            ):
            i[0] += 1
            hm.withdraw()
            self.frame = Frame(master, bg='white', width=500,
                               height=400)
            self.frame.pack()
            self.gameoverlabel = Label(self.frame, text='Game Over!',
                    bg='white')
            self.gameoverlabel.place(x=210, y=130)

            if winorloss == 1:
                self.status = 'You Won!'
            else:
                self.status = 'You Lost.'

            self.gamestatus = Label(self.frame, text=self.status,
                                    bg='white')
            self.gamestatus.place(x=220, y=160)

            self.newgame = Button(self.frame, text='New Game!',
                                  bg='white', fg='black',
                                  command=self.newgame)
            self.newgame.place(x=50, y=200)
            self.newgame.config(height=1, width=10, relief=RIDGE)

            self.playagain = Button(self.frame, text='Play Again!',
                                    bg='white', fg='black',
                                    command=self.playagain)
            if len(wordslist) > 0:
                self.playagain.place(x=200, y=200)

            self.playagain.config(height=1, width=10, relief=RIDGE)

            self.quit = Button(self.frame, text='Bye!', bg='white',
                               fg='black', command=self.quit)
            self.quit.place(x=350, y=200)
            self.quit.config(height=1, width=10, relief=RIDGE)

            self.wordframe = Frame(self.frame, bg='white', width=500,
                                   height=200)
            self.wordframe.place(x=0, y=260)

            self.wordinfo = Label(self.wordframe, text='The word was: '
                                  + hm.currentword, bg='white',
                                  fg='blue')
            self.wordinfo.place(x=10 + 500 / 2 - (14
                                + len(hm.currentword)) * 4, y=0)  # #############################

   # (500/2)-((14+len(hm.currentword))*4)

    root = Tk()

    placeatcenter(root, 'Game Over!')

  # ~ icon in launcher ~

    icon = PhotoImage(file='HangMan_img/icons/ico.png')

 # ~ game initialistion ~

    end = endgame(root, winorloss, wordslist)
    root.mainloop()


FONT = 'Courier 36 bold'
FONT2 = 'Courier 30 bold'


class HangMan(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title('HangMan')
        self.bind('<Any-Key>', self.binder)

        # use words from database if level &genre are available, otherwise use the give list

        if int(len(sys.argv)) == 3:
            genre = int(sys.argv[1])
            level = int(sys.argv[2])
            self.words = worddatabase[genre][level]
        else:

            self.words = [
                'oyster',
                'python',
                'destroy',
                'employ',
                'reason',
                'royal',
                'cowboy',
                'enjoy',
                'lovable',
                'voyage',
                'winter',
                ]
        random.shuffle(self.words)

        gameframe = Frame(self)

        self.canvas = Canvas(gameframe, background='white', width=300,
                             height=300)
        self.canvas.pack(side='left')

        self.drawman()

        # fills letter frame with letters of lower case

        self.letters = {}
        letterframe = Frame(gameframe, bg='white')
        col = 0
        row = 0
        for letter in lowercase:
            l = Label(letterframe, text=letter, font=FONT, bg='white',
                      foreground='blue')
            l.config(fg='blue')
            l.grid(row=row, column=col)
            self.letters[letter] = l
            col = col + 1
            if col == 6:
                row = row + 1
                col = 0
        letterframe.pack(side='left')
        gameframe.pack()

        inputframe = Frame(self, bg='white')
        self.theword = Label(inputframe, text='_ _ _ _ _', font=FONT2,
                             bg='white', fg='blue')
        self.theword.pack(anchor=CENTER)
        inputframe.pack(fill='x')

        self.setword()

    def setword(self):  # selects word and places it in appropriate position
        i[0] = 0
        self.guessed = []

        if len(self.words) > 0:
            self.currentword = self.words.pop()
        else:

            gameover(1, self.words)

        while len(self.currentword) > 11:
            self.currentword = self.words.pop()
        self.theword.config(text='_ ' * len(self.currentword))

        for l in self.letters.values():  # #color of letters in letter box
            l.config(fg='white')
        self.update()

    def binder(self, event):  # binds keystrokes, This function is vital as it controls the next turn of game
        key = event.keysym

        print 'binder called', event.keycode, key
        print len(self.bodyparts)

        self.title('HangMan' + ' letters left: '
                   + str(len(self.bodyparts)))

        if len(self.bodyparts) == 2 or len(self.bodyparts) == 1 \
            or len(self.bodyparts) == 0:
            if i[0] == 0:
                os.system('sleep 1s')
                gameover(0, self.words)

        if key not in letters:

             # # ignore

            return 'break'

        if key not in self.guessed:
            self.guessed.append(key)
            self.strike(key)
            self.showletter()

            if key not in self.currentword:
                self.shownext()
                return 'break'
        return 'break'

    def shownext(self):

         # # draw the next part of the hang man

        try:
            id = self.bodyparts.pop()
        except:

             # # try this word again!

            self.showword()
            time.sleep(1)

            self.drawman()
            self.words.append(self.currentword)
            self.setword()
            return 'break'
        try:
            self.canvas.itemconfig(id, outline='blue')
        except:
            self.canvas.itemconfig(id, fill='blue')

    def showword(self):  # displays word at end of game
        self.theword.config(text=self.currentword)
        self.update()

    def showletter(self):  # reveals letter behind dashes

         # ~ print "showletter called"

        out = []
        for c in self.currentword:
            if c in self.guessed:
                out.append(c)
            else:
                out.append('_')

        self.theword.config(text=' '.join(out))
        hm.update
        self.update()
        if '_' in out:

             # keep going....

            pass
        else:
            time.sleep(1)
            gameover(1, self.words)

    def strike(self, letter):  # marks letters guessed
        if letter in lowercase:
            l = self.letters[letter]
            l.config(fg='#D1D1FF')

    def drawman(self):  # returns elements of hangman figure as a list
        self.canvas.delete('all')
        self.bodyparts = []

         # noose and stand

        id = self.canvas.create_line(50, 250, 250, 250, fill='white')
        self.bodyparts.append(id)

        id = self.canvas.create_line(50, 250, 50, 50, fill='white')
        self.bodyparts.append(id)

        id = self.canvas.create_line(50, 50, 150, 50, fill='white')
        self.bodyparts.append(id)

        id = self.canvas.create_line(150, 50, 150, 75, fill='white')
        self.bodyparts.append(id)

         # head

        id = self.canvas.create_oval(140, 75, 160, 95, outline='white')
        self.bodyparts.append(id)

        id = self.canvas.create_line(150, 95, 150, 150, fill='white')
        self.bodyparts.append(id)

         # leg

        id = self.canvas.create_line(150, 150, 125, 175, fill='white')
        self.bodyparts.append(id)

         # leg

        id = self.canvas.create_line(150, 150, 175, 175, fill='white')
        self.bodyparts.append(id)

         # arm

        id = self.canvas.create_line(150, 95, 125, 115, fill='white')
        self.bodyparts.append(id)

         # arm

        id = self.canvas.create_line(150, 95, 175, 115, fill='white')
        self.bodyparts.append(id)

        self.bodyparts.reverse()


hm = HangMan()

icon = PhotoImage(file='HangMan_img/icons/ico.png')
hm.tk.call('wm', 'iconphoto', hm._w, icon)  # <source>~ http://effbot.org/tkinterbook/wm.htm ~

    # calculate position x and y coordinates

placeatcenter(hm, 'HangMan 2.0')
hm.mainloop()


			
