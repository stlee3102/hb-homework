log_file = open("um-server-01.txt") #open txt file


def sales_reports(log_file): #take a file into function to process
    for line in log_file: #for each line in the file
        line = line.rstrip() #remove any trailing excess spaces from the line
        day = line[0:3] #grab the first three letters of the line, this is the day
        if day == "Mon": #if the day is Monday
            print(line) #print the line


sales_reports(log_file) #call function using the variable holding the txt file
