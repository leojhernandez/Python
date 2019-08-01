import csv

with open('file_name .csv', 'r') as file:                # lets open a csv file
    reader = csv.reader(file)
    
    with open('new_file.csv', 'w') as new_file:         # we created a new csv file
        writer = csv.writer(new_file, delimiter='\t')
        
        for line in reader:
            writer.writerow(line)
            
with open('new_file.csv', 'r') as file_2:              # now lets open that new file

    reader = csv.reader(file, delimiter='\t')
    
    for line in reader_2:
        print(line)          
# ignore
# ignore once again 