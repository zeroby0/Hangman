# Hangman
by: Vishnu Sai Sankeerth, Aravind V and Oormila G.

The popular Hangman pen & paper game implemented in GUI with Python Tkinter library.

The game consists of one player giving a word unknown to other player and asking him
to guess it. Here the role of the first player is taken by the computer. Then as the player
guesses the word based on number of letters in the word, each successful attempt
makes the letter to be revealed, however if the player fails to do so and makes a wrong
guess, a part of the hangman figure is drawn, one after the other. The number of
chances given to the user depends on the number of steps in drawing hangman. If the
player fails to guess the word in his limited number of chances, he fails.

run `` install.sh `` to install dependencies required for the game.  
``
$ python hangman
``
to run the game

## Dependencies  
Python-Tk (Tkinter).   
Python-imaging-tk.  
The install script can install these for you if you're using version 2.7, but please feel free to install them using your favourite package manager.
```
sudo apt-get install python-Tk
sudo apt-get install python-imaging-tk
```
