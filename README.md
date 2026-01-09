# Basic-ecryption-algorithm
This project implements a basic Caesar Cypher using a fixed shift of 13 positions (commonly known as ROT13). Each letter in the input string is shifted 13 places forward in the English alphabet. If the shift goes past Z, it wraps around to the beginning of the alphabet. 
This cypher works symmetrically, meaning the same function can be used for both encryption and decryption.

How the Cypher Works
Each alphabetic character is shifted 13 letters forward
Non-alphabetic characters (spaces, numbers, punctuation) remain unchanged
The alphabet wraps around when the end is reached

EXAMPLE
Input:   HELLO
Output:  URYYB

Input:   URYYB
Output:  HELLO

Features:
Fixed 13-character shift (ROT13)
Supports uppercase and lowercase letters
Preserves spaces and punctuation
Simple and beginner-friendly Python code

HOW TO RUN THE PROGRAM
Prerequisites:
Python 3.x installed
Steps:
python main.py

Concepts Used:
ASCII values
Strings and character manipulation
Conditional statements
Loops
Basic cryptography principles

Future Improvements:
Allow user-defined shift values
Add file encryption support
Implement GUI
Add unit tests

License
This project is licensed under the MIT License.

Author
Hanya Mursaleen
Aspiring Computer Science Student | Python Developer
