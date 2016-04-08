#!/usr/bin/python

from Tkinter import *
import os
import sys


def placeatcenter(window, title):  # function to place windows at center of the screen, assign a title, change background to theme color: white and make the windows non re-sizeable

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.wm_title(title)
    x = screen_width / 2 - 500 / 2
    y = screen_height / 2 - 400 / 2
    window.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    window.config(background='white')
    window.resizable(width=FALSE, height=FALSE)


def play(level, genre):  # function withdraws the present window and opens the next game window, closes the present wiindow and stops process after the child window is closed, also removes .pyc files formed, if any

    root.withdraw()
    os.system('python loading.py')
    os.system('python game.py %d %d' % (genre, level))

          # root.destroy

    os.system('rm *.pyc')
    sys.exit()


class level:  # This class has implementations for the level selection window

    def __init__(self, master):

        def clr():  # ~ obtains level and genre information, if valid, passes to play function after clearing every thing in present window. If not valid, pops up an error screen showing the error
            level = self.level_variable.get()
            genre = self.genre_variable.get()
            if level * genre != 0:

                self.levellabel.destroy()
                self.lev1.destroy()
                self.lev2.destroy()
                self.lev3.destroy()

                self.gen1.destroy()
                self.gen2.destroy()
                self.gen3.destroy()
                self.genlabel.destroy()
                self.frame.destroy()

                play(level, genre)
            else:

             # #~if genre or level of questions have not been selected ~

                def clr():
                    root.deiconify()
                    placeatcenter(root, 'HangMan 2.0')
                    error.destroy()

                root.withdraw()  # ~if level or class is not valid ~
                error = Tk()

                placeatcenter(error, 'Note: ')
                errorframe = Frame(error, width=500, height=400,
                                   bg='white')
                errorframe.pack()

                if level == 0:
                    errormessage = Label(errorframe,
                            text='Please select Level', anchor=W,
                            bg='white', fg='black')
                    errormessage.place(x=190, y=140)
                else:
                    errormessage = Label(errorframe,
                            text='please select the genre of questions you like'
                            , anchor=W, bg='white')
                    errormessage.place(x=115, y=140)

                errorbutton = Button(errorframe, text='OK!',
                        command=clr)
                errorbutton.place(x=220, y=190)
                errorbutton.config(bg='#E6E6FA', relief=RIDGE,
                                   activebackground='#D1D1FF',
                                   activeforeground='white',
                                   command=clr)

       # ################################## ~end of clr() definition

        self.frame = Frame(master, width=700, height=500)
        self.frame.pack()
        self.frame.config(background='white')

        self.levellabel = Label(master, text='Select a level to play: '
                                , bg='white')
        self.levellabel.place(x=50, y=40)

        self.level_variable = IntVar()

        # ~radio buttons for level and genre selection

        self.lev1 = Radiobutton(
            master,
            text='Beginner',
            variable=self.level_variable,
            value=1,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.lev1.place(x=50, y=80, anchor=W)
        self.lev2 = Radiobutton(
            master,
            text='Intermediate',
            variable=self.level_variable,
            value=2,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.lev2.place(x=50, y=110, anchor=W)
        self.lev3 = Radiobutton(
            master,
            text='Master',
            variable=self.level_variable,
            value=3,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.lev3.place(x=50, y=140, anchor=W)

        self.genlabel = Label(master, text='Which is your favourite?',
                              bg='white')
        self.genlabel.place(x=300, y=40)

        self.genre_variable = IntVar()

        self.gen1 = Radiobutton(
            master,
            text='Science',
            variable=self.genre_variable,
            value=1,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.gen1.place(x=300, y=80, anchor=W)
        self.gen2 = Radiobutton(
            master,
            text='Animals',
            variable=self.genre_variable,
            value=2,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.gen2.place(x=300, y=110, anchor=W)
        self.gen3 = Radiobutton(
            master,
            text='Fruits',
            variable=self.genre_variable,
            value=3,
            bg='white',
            relief=FLAT,
            highlightthickness=0,
            )
        self.gen3.place(x=300, y=140, anchor=W)

        self.gobutton = Button(self.frame, text='Go!')  # ~ Go! button ~
        self.gobutton.place(x=220, y=190)
        self.gobutton.config(bg='#E6E6FA', relief=RIDGE,
                             activebackground='#D1D1FF',
                             activeforeground='white', command=clr)


# ~ class welcome screen ~

class welcome:

    def __init__(self, master):

    # ~ clears every thing on the welcome screen and hand-overs window to level ~

        def clr():
            self.frame.destroy()
            level(master)

        self.frame = Frame(master)
        self.frame.pack()
        self.frame.config(background='white')

        self.image = Label(self.frame, image=welcome_image, bg='white')
        self.image.pack()

        self.playbutton = Button(self.frame, text='Play!', command=clr)
        self.playbutton.place(x=300, y=200)
        self.playbutton.config(bg='#E6E6FA', relief=RIDGE,
                               activebackground='#D1D1FF',
                               activeforeground='white')


if __name__ == '__main__':

    root = Tk()

    placeatcenter(root, 'HangMan 2.0')

    welcome_image = PhotoImage(file='HangMan_img/backgrounds/greet.png')

  # ~ icon in launcher ~

    icon = PhotoImage(file='HangMan_img/icons/ico.png')
    root.tk.call('wm', 'iconphoto', root._w, icon)

  # ~ window settings

    root.config(background='white')
    root.resizable(width=FALSE, height=FALSE)

  # ~ game initialistion ~

    start = welcome(root)
    root.mainloop()

# <syntax-source>~ http://effbot.org/tkinterbook/wm.htm ~
### Aravind ###


			
