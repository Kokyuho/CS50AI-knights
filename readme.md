# CS50’s Introduction to Artificial Intelligence with Python
# Project 1: Knowledge: Knights

**Aim**: Write a program to solve logic puzzles.

Description: In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.

Although a puzzle with few statements is simple to solve, with more characters and more sentences, the puzzles can get trickier! Thus, an algorithm is implemented able to solve these puzzles for us using propositional logic.

Two files are included, logic.py which implements the logical classes and checks of our problem, and puzzle.py which translates the statements to propositional logic using those classes and solves the puzzles.

See full problem description here: https://cs50.harvard.edu/ai/2020/projects/1/knights/

Usage:
```
python puzzle.py
```

Example:
```
$ python puzzle.py
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```
