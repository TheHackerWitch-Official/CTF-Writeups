from sh import nc

output = nc("mercury.picoctf.net", "35652")

# remove all the stuff we don't want (newlines and spaces)
output = output.replace("\n", ",")
output = output.replace(" ", "")

# the numbers are separated by commas. let's turn them into a list                                                 
list = output.split(",")                                                                                           
                                                                                                                   
# remove any empty strings from the list                                                                           
list[:] = [x for x in list if x]                                                                                   
                                                                                                                   
flag = ""                                                                                                          
                                                                                                                   
# for every integer in the list, convert it to a character, and add it to the flag string                                  
for item in list:                                                                                                  
    flag += chr(int(item))

# print our flag
print(flag)
