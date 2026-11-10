# Name: Aurora Dawn Tackett 
# Date: 11/9/2026
# Program Name: programHelpScreenTask01.py
# Description: Command-line programs print a help screen when you type -h. Write a program that prints the help screen for a pretend tool called gradebook.
print("=" * 40)
print("  GRADEBOOK  version 1.0\n  A tool for tracking class scores")
print("=" *40)
print("USAGE:")
print("  gradebook [option] [file]")
print("\n\nOPTIONS:")
print("  -a\tAdd a new score")
print("  -l\tList all scores")
print("  -r\tPrint a report")
print("  -h\tShow this help screen")
print("\n\nEXAMPLES:")
print("  gradebook -l C:\\BPA\\scores.txt")
print("  gradebook -a ""quiz 3""")
print("\n\n\n", "-" * 40)
print("Tip: options are case sensitive.\n-A is not the same as -a.")
print("=" * 40)