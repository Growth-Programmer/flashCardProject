This is a French/English flash card program that displays a French Language flash card first, and after 3 seconds, displays the English version of the text. This program utilizes the pandas library, and csv files; demonstrating 
data manipulation. 

To run the program, you must have the data, images, and main.py files. You can either use your own virtual environment or just clone the project into PyCharm. If you are not interested in using the program,
the code is available in the main.py file.

Lastly, in the program, there are two buttons. One for known words (green check mark) and one for unknown words (red x mark). Both buttons go to the next card, however, when the known words button is clicked, a new dictionary of 
words that **DO NOT** include the known one or ones is created. The program will use **this** dictionary of updated data instead of the old one to present the flash cards in order to present the user with words that **they do not know**.
If the unknown button is clicked, the program will just go to the next card.
