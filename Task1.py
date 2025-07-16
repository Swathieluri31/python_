# convert to Uppercase
s = "welome to myworld"
print(s.upper())

#covert to Lowercase
s = "HI! THIS IS SWATHI"
print(s.lower())

#Capitalize First Letter
s = "bapathu venkata kotireddy"
print(s.capitalize())

#Title case each word
s = "welcome to my world"
print(s.title())

#Count occurence of Substring
s = "i like you"
print(s.count("i"))

#Replace Substring
s = "hema"
print(s.replace('a','u'))

#Check if String Starts or Ends with Substring
s="hema"
print("hema".startswith("he"), "hema".endswith("a"))

#Find position of Substring
s= "i am very happy"
print(s.find("very"))

#Remove Whitespace
s= "i am very happy"
print("  i am very happy ".replace(" ", ""))

#join list of strings
s = " i like you "
print(" ".join(["i", "like", "you"]))
