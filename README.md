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

# Stage 2/6: Matching two equal length strings

### Description

A single character is not a alot, so let's extend our new regex engine to handle regex-string paris of equal length. Don't
forget about supporting the wildcard symbol! It is still not the most realistic way to use a regex engine, but we are slowly getting there.

### Objectives

Create a new function that calls the function from the first stage on every character of the regex-string pair and returns True only
if there is a match for every character. In other words, fora complete match, either every character pair should be the same, or the 
regex should contain a wild card. There are different ways to achieve this, but the most elegant is probably recursion.

Recall that recursion is when a function calls itself from its own code. It can be used to break down a problem into smaller steps,
thus simplifying the  code.

This is exactly what you are going to do in this stage! First, invoke the function from the first stage on the first characters of the regex-string pair.
If there is a match, pass the remainder of the string recursively to the same function, but this time without the first characters
of the regex and the input string, thus "consuming" them step by step.

Some terminating conditions should be added to stop the function from entering infinite recursion:
- If the regex has been entirely consumed, the function should return ```True``` since it means that all the characters in the regex-string
pair are the same.
- If the regex has not been consumed but the input string has, the function should return ```False``` since it means that the regex is
longer thatn the input string, which is undefined behavior at this point.
- If the first character of the regex does not match the first character of the input string, the function should return ```False``` because it
guarantees that the two patterns are different.

If none of the above apply, the recursion should continue until the regex-string pair is entirely consumed through slicing.

This logic can be illustrated as follows:

![recursive-scheme](/assets/recursive-scheme.png)

Note that some of the steps can be concatenated with the help of boolean logic and smartly coned return statements. 
If your program works but you find it awkward or overly complicated, try to combine some of the steps to make your code more readable.

### Examples:

````Python
Input: 'apple|apple'     Output: True
Input: '.pple|apple'     Output: True
Input: 'appl.|apple'     Output: True
Input: '.....|apple'     Output: True
Input: 'peach|apple'     Output: False
````

# Stage 3/6: Working with strings of different length

### Description

At this point, your regex engine is pretty basic and not very useful. Comparing two equal length patterns to each other is not what we usually need. Let's add support for comparing regex-string pairs of different lengths.

For example, the engine will be able to compare the substring tion with the following words and find matches: section, seduction, introduction, intersection, motion, neon, chair, mockingbird. As you can see, this scenario is already more realistic: there is a bunch of words and we only want to select those with a specific suffix.

So, how does it work if our function can only work with regex-string pairs of equal length? Remember, in the previous step we added two terminating conditions to the function: if the regex is consumed, we return True, and if the string is consumed, we return False. The first condition means that we have gone over the whole regex and there is a match. The other case shows that there cannot be a match since the regex has not been consumed and there is no string to compare it to. These two conditions make sure that the function does not break if the text is for some reason longer than the regex or vice versa.

One way to tackle this problem is to repeatedly invoke that function and check if there is a match. If there isn't, another section of the string should be passed.

Let's see how can this be done with our suffix example:

`````python
Input: ‘tion|Section’     Output: False
Input: ‘tion|ection’      Output: False
Input: ‘tion|ction’       Output: False
Input: ‘tion|tion’        Output: True
`````

### Objectives

Your improved regex engine should do the following:

- A new function is created as an entry point;
- It should repeatedly invoke the function that compares two equal length patterns;
- If that function returns ```True```, the new function should also return True;
- If that functions returns ```False```, the input string should be passed to the matching function with an incremented
starting position, and the regex should be passed unmodified;
- The process goes on until the entire input string has been consumed.

A way to implement this is to use slicing like in the previous stages, but do it only to progress the input string.
The input string should be consumed character by character, and the regex should be checked against every position.

A loop can be used to take care of the changing starting characters, but you can also experiment more with recursion.

In case you choose to use a loop, keep in mind that the type of the loop you use is optional, but in order to slice a string, 
integers should be passed as string indexes, and an index should not be greater than the length of the input string. 
If the end of the string is reached, the input string is consumed without a match, which should return ```False```.

If you prefer to stick to recursion, use the same logic you used earlier. However, keep in mind that Python has a limit 
on recursion, and it might be reached if you're dealing with longer strings. To counter this, the following lines should 
be added to your program if it throws an error message about reaching the recursion limit:

`````python
import sys
sys.setrecursionlimit(10000)
`````

### Examples

Input: 'apple|apple'     Output: True
Input:    'ap|apple'     Output: True
Input:    'le|apple'     Output: True
Input:     'a|apple'     Output: True
Input:     '.|apple'     Output: True
Input: 'apwle|apple'     Output: False
Input: 'peach|apple'     Output: False






# This project is a part of the following track: Python Developer from Jetbrains Academy
