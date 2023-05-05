The language I implemented is Arithmetic Haiku. Each operation must be specified using one of two specific 5 or 7 syllable phrases. While I initially wanted to force the user to input each instruction on a new line and try to make them alternate between 5 and 7 syllables like a Haiku, unfortunately after over 12 grueling hours of trying, I could not figure out how to implement this so my language is kind of lackluster in that aspect
For addition: 
you must input a number/expression followed by a space, then either the 5 or 7 syllable phrase, followed by a space and then another number/expression. 
- *number/expression* "add these together" *number/expression*
- *number/expression* "add these two terms together" *number/expression*
For subtraction:
you must input a number/expression followed by a space, then either the 5 or 7 syllable phrase, followed by a space and then another number/expression. 
- *number/expression* "subtract this term from the first" *number/expression*
- *number/expression* "subtract these two terms" *number/expression*
For multiplication:
you must input a number/expression followed by a space, then either the 5 or 7 syllable phrase, followed by a space and then another number/expression. 
- *number/expression* "multiply the terms" *number/expression*
- *number/expression* "multiply these two numbers" *number/expression*
For division:
you must input a number/expression followed by a space, then either the 5 or 7 syllable phrase, followed by a space and then another number/expression. 
- *number/expression* "divide by the next number" *number/expression*
- *number/expression* "divide these two terms" *number/expression*
For Parentheses:
you must input the open parentheses phrase then an expression, then the close parentheses phrase
"open the parentheses" *expression* "now we close parentheses"


To run this code from the command line you should type: “python haikuMath”
Then type in the equation phrase that you want and the output will be evaluated.

Sample programs are below and also in the python file commented out

#number expression: "4 + 5" 
#Haiku expression = "4 add these two terms together 5" 
Output: 9.0

#number expression: "3 - 5" 
#Haiku expression = "3 subtract this term from the first 5" 
Output: -2.0

# Number expression "3 * (4 + 5) - 6 / 2 = 24" 
# Haiku expression = "3 multiply the term open the parentheses 4 add these two terms together 5 now we close parentheses subtract this term from the first 6 divide by the next number 2"
Output: 24.0
