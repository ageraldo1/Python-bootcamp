import csv

csv_source = 'resources/budget_data.csv'   # relative path location for budget_data.csv dataset
amount_change = []                         # list used to calculate average change
profit_lost = []                           # list used to store profit/lost amounts

with open(file=csv_source, mode='r', encoding='utf-8') as csv_file:
    # using DictReader instead. Make code easier because you can 
    # get data using column name instead of column index
    csv_reader = csv.DictReader(csv_file, delimiter=',')

    for line in csv_reader:
        # using column name instead of column index. 
        # Makes code easier to understand
        profit_lost.append(float(line["Profit/Losses"]))

        # in order to calculate the average change  :
        # actual [profit/lost] - previous  [profit/lost]
        # sum all amounts and divide by the number of entries  
        if ( len(profit_lost) > 1):  # note that we need at least 2 values to calculate the change
            # this if statement guarantee there are at least 2 entries
            actual_amount   = profit_lost[len(profit_lost)-1]
            previous_amount = profit_lost[len(profit_lost)-2] 
            avg_change      = actual_amount - previous_amount
            amount_change.append( avg_change )
    
    total_avg_change = sum(amount_change) # calculate the total amount changed
    print (f"Average Change : {total_avg_change/len(amount_change):,.2f}")



