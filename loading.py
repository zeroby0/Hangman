#!/usr/bin/python

##### ~ http://stackoverflow.com/questions/7960600/python-tkinter-display-animated-gif-using-pil ~
## source of code can be found at the above web page, I have modified the code to suit my needs.

from Tkinter import *
from PIL import Image, ImageTk


class MyLabel(Label):

    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))  # skip to next frame
        except EOFError:
            pass  # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0],
                       highlightthickness=0, bg='white')

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


root = Tk()
anim = MyLabel(root, 'HangMan_img/loading/google.gif')
anim.place(x=140, y=90)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.config(bg='white')

root.overrideredirect(1)
x = screen_width / 2 - 500 / 2
y = screen_height / 2 - 400 / 2
root.geometry('%dx%d+%d+%d' % (500, 400, x, y))

anim.after(2000, root.destroy)
root.mainloop()



			
