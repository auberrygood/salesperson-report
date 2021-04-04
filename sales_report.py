"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #list of salespersons selling melons
melons_sold = [] #list of melons sold by each salesperson

#salespeople/melons_sold data, probably better off being collected as a dictionary, 
#so that melons sold can be tied to a specific saleperson without needing to know anything but the person's name

f = open('sales-report.txt')  #accessing data within sales-report.txt file
for line in f: #loop over each line in sales-report.txt file
    line = line.rstrip() #ridding of any trailing whitespace within file
    entries = line.split('|') #distinguising individual elements of file, by using "|" as seperator 

    salesperson = entries[0]  #salesperson's name is the 1st element of each line in the file
    melons = int(entries[2]) #melons sold is the third element of each line in the file

    if salesperson in salespeople:   #checking if name already exists in list of salepeople
        position = salespeople.index(salesperson)  #if yes, what is the index of the person in the salespeople list?

        melons_sold[position] += melons   
        #index of person == index of melons sold, 
        # use index to find position of that person's melons within the melons_sold list
        #update the number of melons that person has sold (melons already recorded in list + melons sold on file line = melons sold)

    else:
        salespeople.append(salesperson) #if person not already in salespeople list, add their name to list
        melons_sold.append(melons)   #add the number of melons they sold to melons list


for i in range(len(salespeople)):    #loop over indices of salespeople list (stopping at end of list) to do following:
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')   #print the salesperson's name, and the total of melons they sold


#file is not closed within program, should probably add?