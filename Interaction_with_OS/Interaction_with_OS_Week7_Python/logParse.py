#!/usr/bin/env python3

# Import all the Python modules
import re
import operator  #sort islemleri icin gerekli
import csv

# one dict for the number of different error messages
error = {}
with open("syslog.log") as f:    
    for line in f.readlines():
        error_line = re.search(r"ERROR (.* )\((.*)\)", line)
        
        if error_line:
            if str(error_line[1]) in error.keys():
                error[str(error_line[1])] +=1
            else:
                error[str(error_line[1])] = 1


# one dict to count the number of entries for each user (splitting between INFO and ERROR).
per_user = {}
with open("syslog.log") as f:
    for line in f.readlines():
        user_line = re.search(r"ticky: ([\w]*)( .* )\((.*)\)", line)
        user_name = str(user_line[3])
        
        if str(user_line[1]) == 'INFO':
            if user_name in per_user.keys():
                per_user[user_name][0] +=1
            else:
                per_user[user_name] = []
                per_user[user_name].append(1)
                per_user[user_name].append(0)
        
        if str(user_line[1]) == 'ERROR':
            if user_name in per_user.keys():
                per_user[user_name][1] += 1
            else:
                per_user[user_name] = []
                per_user[user_name].append(0)
                per_user[user_name].append(1)


                
#print(error)
#print(per_user)

################################### Sort dictionaries ################################################
# error dictionary should be sorted by the number of errors from most common to least common.   
# To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.

# Note: sorted() function converts dictionary to a list
sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
#print(type(sorted_error))
#print(sorted_error)

# per_user dictionary should be sorted by username. we used for loop to make dictionary to be converted 3 columns list
sorted_user = []

for each in sorted(per_user.items(), key=operator.itemgetter(0)):
    sorted_user.append((each[0], each[1][0], each[1][1]))
                        
#print(sorted_user)

########################################################################################################

######################################## insert column names ###########################################
# Insert column names as ("Error", "Count") at the zero index position of the sorted error dictionary. 
sorted_error.insert(0,("Error","Count"))
### sorted_error = dict(sorted_error) # sorted function above converted the dict to a list so we change it back to dictionary

print(sorted_error)
n = 0
while n < 3: 
    print("###################################################################################")
    n += 1

# And insert column names as ("Username", "INFO", "ERROR") at the zero index position of the sorted per_user dictionary.
sorted_user.insert(0,("Username", "INFO", "ERROR"))
print(sorted_user)

#########################################################################################################

###################################### Write the Output into CSV ########################################

# After sorting these dictionaries, store them in two different files: error_message.csv and user_statistics.csv.
with open("error_message.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_error)
    file.close()
    
with open("user_statistics.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_user)
    file.close()