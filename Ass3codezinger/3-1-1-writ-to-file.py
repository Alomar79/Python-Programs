"""
Given a string S. Write the given string to a file. 
Write a function:
    def solution(S): 
that accepts a string S. The function should write the given string to “text.txt” file.

Input
    This is my python program.
Output
    This is my python program
"""
def solution(S):
    outfile = open("text.txt","w")
    outfile.write(S)

