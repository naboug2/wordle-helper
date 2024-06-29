Overview
This project provides a GUI to assist in finding possible words based on given criteria, similar to solving a Wordle puzzle. The program reads a list of words from a file and filters them based on exact letter positions and known letters.

Files
-main.py: The main script containing the logic and GUI implementation.
-all_words.txt: A text file containing a list of possible words, one word per line.
-examples.txt: A sample file demonstrating the expected format and usage of the input word list.


Functionality
ExactLetters(S):
-Takes a string S with underscores representing unknown letters.
-Returns a list of words that match the pattern specified by S.

ContainsLetters(T):
-Takes a string T of letters that must be present in the words.
-Returns a list of words containing all the letters in T.

InBoth(L1, L2):
-Takes two lists of words L1 and L2.
-Returns a list of words that are present in both L1 and L2.

RunIt():
-Executes when the button in the Tkinter GUI is pressed.
-Validates input from text boxes.
-Uses ExactLetters and ContainsLetters to find words that match the criteria.
-Displays the results in a message box.


GUI Description
The GUI, built using Tkinter, consists of:
-Five text boxes for entering known letters at specific positions.
-Five text boxes for entering known letters that are in the word but whose positions are unknown.
-A button to execute the search based on the entered criteria.


Instructions for Use
1. Enter known letters in their respective positions in the top row of text boxes.
2. Enter known letters that must be in the word (but with unknown positions) in the bottom row of text boxes.
3. Click the "Find Me Some Words!" button to see the possible words that match your criteria.


Running the Program
1. Ensure all_words.txt and examples.txt are present in the same directory as main.py.
2. Run the script using Python: python main.py


GUI Interaction
-Enter "a" in the first text box of the top row if you know the word starts with "a".
-Enter "p" in the first text box of the bottom row if you know the word contains "p".
-Click "Find Me Some Words!" to get a list of possible words like "apple" or "ample".
