#Check string and modify string methods
a = "my college"

#String methods
print(a.lower())            # convert to lowercase
print(a.upper())            # convert to uppercase
print(a.replace('m', 'z'))  # replace 'm' with 'z'

#Check words in string
if "my" in a:
    print("Yes, 'my' is in the string")
elif "free" not in a:
    print("No, 'free' is not in the string")
