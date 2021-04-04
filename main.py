# First import two necessary modules for path (os) and data file (csv)
import os
import csv

#Create refernce path for data file
datapath=os.path.join('.','Resources','budget_data.csv')

#open file using second method taught
with open(datapath) as datafile:
    data = csv.reader(datafile, delimiter=',')
    # skip headers row 
    header = next(data)

    # establish variables
    pvalue = int(0)
    count = int(0)
    total = int(0)
    totalchange = int(0)
    aveprofit = int(0)
    avechange = int(0)
    hmonth = ()
    maxprofit = int(0)
    lmonth = ()
    maxloss = int(0)
   

    
#step thru lines to create additional desired fields
    for row in data:
        row.append(pvalue)                  #prior value, index[2]
        row.append(int(row[1])-pvalue)      #change value, index[3]
        pvalue=int(row[1])
        count=count+1
      
             
        total += int(row[1])                #This works
        aveprofit = int(total / count)      #This works
        totalchange += int(row[3])          #>>>>>>>>>>>THIS DOES NOT WORK (Grrrrr!)
        avechange = int(totalchange/ count)


        if int(row[3]) > int(maxprofit):    #This works
            hmonth = row[0]
            maxprofit = int(row[3])
        
            
    
        if int(row[3]) < int(maxloss):      #This works
            lmonth = row[0]
            maxloss = int(row[3])
        
            
    
    
    #print findings to terminal
    print(f"The total profit over the aggregate period of {count} months was {total}, with an average profit of {aveprofit} and average change of {avechange}.")  
    print(f"The greatest increase in profits occured in {hmonth} ({maxprofit}).")
    print(f"The greatest decrease in profits occured in {lmonth} ({maxloss}.)")
 
#create path to output text file with summary analysis

output_path = os.path.join('.','Analysis','Findings.txt')

#write to output summary text file
with open(output_path, 'w', newline='') as txtfile:

    txtfile.write(f"The total profit over the aggregate period of {count} months was {total}, with an average profit of {aveprofit}and average change of {avechange}.")
    txtfile.write(f"The greatest increase in profits occured in {hmonth} ({maxprofit}).")
    txtfile.write(f"The greatest decrease in profits occured in {lmonth} ({maxloss}.)")
    txtfile.close