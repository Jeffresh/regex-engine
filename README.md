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
longer than the input string, which is undefined behavior at this point.
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

# Stage 4/6: Implementing the operators and $

### Description

Regular expressions are useful and flexible because they include a set of metacharacters. So far, the only metacharacter
we an handle is the wild char(.) Although it is certainly useful, our engine still lacks the flexibility we need.

Let's think of a case where we would want a pattern to match only if it happens in a certain part of the input string, for example
only the beginning or the end. Do you remember the example for the previous stage where we wanted to match only the nouns that end with the
suffix ```tion```? That's exactly the case where we need the metacharacter ```$```. The regex ```tion$``` will match the string 
```section``` but not ```sections```, even though ```tion``` is part of both strings.

The metacharacter ```^``` is the opposite: it only matches a pattern if it is located ad the beginning of the input string. This
way, the regex ```^be``` will match the strings ```beware````, ```become```, ```behind````, but not ```to be```, even
though it contains ```be```.

### Objectives

Your task is to add some metacharacters to the already existing regex engine.

At this stage, you should add the following special cases:

- ```^``` can occur at the beginning of the regex, and it means that the following regex should be matched only at the beginning of
input string.

- ```$``` can occur at the end of the regex, and it means that the preceding regex should be matched only at the end of the input string.

Actually, the engine already contains a function that matches only the beginning of the input string: you crated one in the second
stage! Yet you should directly invoke it from the current entry point only if the regex starts with the character ```^```.
Also, do not forget that you shouldn't pass the regex ```^``` itself to the function!

The case with ```$``` is a bit more complicated. Don't worry: with a little thinking, we can get our heads around it. How
do we know if the input string ends with the regex succeeded by ```$```? Normally, if a regex matches the end of a string,
they are consumed at the same iteration, and ```True``` is returned according to the terminating conditions. However, since
```$``` is a metacharacter, it should be at the end of the regex when the input string has already been consumed. At the current
state of the function, it should return ```False``` because the input string is consumed while the gex is not. Yet since we know
that ```$``` has a special meaning, if we see it as the last character of a string, we should assume that the input string is empty.
It should be checked, and if that is the case, the function should return ```True```.

Note: the position of the terminating conditions can alter the behavior of the function! This condition should be added after
the regex has been determined as empty or not, but before the same is determined for the input string.

# Stage 5/6: Controlling repetition

### Description

What could be better than metacharacters? More metacharacters! In this stage, you should add the following metacharacters
to your engine:

- ```?``` matches the preceding character zero times or once.
- ```*``` matches the preceding character zero or more times.
- ```+``` matches the preceding character once or more times.

Let's consider these in more detail. Basically, the most important feature of a regex engine is the presence of the repetition
operators, ```?```, ```*```, and ```+```. They are used to determine how many times a certain character or sequence
can be repeated in the string. These operators can make a regular expression really compact and elegant.

Let's look at the sequence ```aaaaaaaaaab```. We can match this string with teh following regular expressions: 
```aaaaaaaaaab```, ```a*b```, ```a+b```, ```.*b```, ```.+b```.

As you can see, the main role of these operators is to control the repetition of the preceding character.

Note hat the wildcard (```.``) can also be placed before these operators, in which case any character is matched zero or
several times.

### Objectives

The  best way to implement these metacharacters is by adding more conditions to the function that matches the patterns of equal length.

In the case of the operator ```?```, there are two possible scenarios:

 1. The preceding character occurs zero times, so basically it is skipped. This means that only the part of the regex after the metacharacter
 ```?``` is passed to the recursive function along with the unmodified input string.
 
 2. The preceding character occurs one. This means that if the character preceding ```?``` matches the first character of
 the input string, the part of the regex after ```?``` is passed to the recursive function along with the part of the input string without
 the character that is already matched.
 
 In the case of the operator ```*```, there are the following scenarios:
 
 1. The preceding character occurs zero times (just like with ```?```) The condition from the previous case can be reused.
 2. The preceding character occurs one or more times. Like in the case of ```?```, the character preceding ```*``` should
 match the first character of the input string. Since we don't know how many times it is going to be repeated, the regex
 should be passed to the recursive function without any modification, and the first character of the input string should be chopped
 off. In this case, since the metacharacter ```*``` is not removed, the second case is repeated until the preceding character can be
 matched. After that, the first case applies and the function comes out of the recursion.
 
 Finally, here is what can happen with the operator ```+```:
 
 1. The preceding character occurs once. This case is the same as the second case with the operator ```?```.
 2. The preceding character occurs more than once. this case is basically the same as the second case with the operator ```*```.
 
 You could create separate functions for each operator and invoke them from the ```match``` function, or your could include
 these cases into that function. The important thing to understand is that the logic of recursion does not change with the
 implementation of these operators, but you might have to fiddle with the number of characters that are going (or not going)
 to be sliced. Use boolean logic where possible in order to simplify the code and minimize the number of ```if else``` clauses.

### Examples
````
Input: 'colou?r|color'       Output: True
Input: 'colou?r|colour'      Output: True
Input: 'colou?r|colouur'     Output: False
Input: 'colou*r|color'       Output: True
Input: 'colou*r|colour'      Output: True
Input: 'colou*r|colouur'     Output: True
Input:  'col.*r|color'       Output: True
Input:  'col.*r|colour'      Output: True
Input:  'col.*r|colr'        Output: True
Input:  'col.*r|collar'      Output: True
Input: 'col.*r$|colors'      Output: False
````


# This project is a part of the following track: Python Developer from Jetbrains Academy
