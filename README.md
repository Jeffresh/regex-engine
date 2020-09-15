# Regex engine

# About
Regular expressions are a fundamental part of computer science and natural language processing. In this project, you will write an extendable regex engine that can handle basic regex syntax, including literals (a, b, c, etc.), wild-cards (.), and metacharacters (?, *, +, ^, $).

# Learning outcomes
Learn about the regex syntax, practice working with parsing and slicing, and get more familiar with boolean algebra and recursion.

# Stage 1/6: Single character strings 

### Description

In this first stage, create a function that can compare a single character regex to a single character input string.

The reason we are only considering single characters for now is the presence of the wild card indicated by a period (.). Its role in a regular expression is to match any character in the target string. So, if the regex that we pass to our function as an argument is a wild-card, the function always returns True no matter what it is being compared to.

When working on this stage, keep in mind the following special rules of the regex syntax:

    An empty regex should always return True.
    An empty input string should always return False, except if the regex is also empty.
    An empty regex against an empty string always returns True.

These rules seem random at first, but later on they will make sense to you.
### Objectives

In this stage, your program should:

    Accept two characters, a regex and an input;
    Compare the regex to the input and return a boolean indicating if there's a match;
    Support . as a wild card character that matches any input;
    Follow the special syntax rules outlined above.
    
We kindly ask you not to use the re module for completing this project. Otherwise, you will learn nothing from it.


# This project is a part of the following track: Python Developer from Jetbrains Academy
