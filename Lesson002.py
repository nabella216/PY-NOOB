i = 0                                                         # Assigning a value to a Variable

print("BASICS OF PYTHON | GITHUB/NARCOTIC | LESSON-002")      # Print to Screen
print()                                                       # Print an Empty Line

strng = input("Enter a String : ")                            # Input a String
first_chars = int(input("Print first __ characters : "))      # Input a value to a Integer Variable
print()                                                       # Print an Empty Line

if first_chars <= len(strng):                                 # Function: len() returns the length of a String
                                                              # If the length of String is less than or equal to x
  while i < first_chars:                                      # While Loop
    print(strng[i])                                           # Print the String as an array elements
    i=i+1                                                     # Increment i by 1

else:                                                         # If the length of String is greater than x
  print("String contains only ", len(strng), " items.")       # Print to Screen
  print("Cannot output ", first_chars, " items.")             # Print to Screen

print()
print("THAT'S IT FOR SECOND LESSON. TAKE A LOOK AT THE THIRD ONE")
print("@ -> GITHUB/NARCOTIC/PY-NOOB")
