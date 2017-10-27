import datetime
from functools import reduce
import time


# function used by map to create a dictionary containing the date from the row and the taxons
def extract(row):
    return {'date': datetime.datetime.strptime(row[1], "%Y:%m:%d:%H:%M:%S").date(), 'taxon': row[22].split(','),
            'mcp': row[6]}


# function to reduce the dictionary to a dictionary of counts
def reduce_dict(counts_dictionary, taxon_dictionary):
    # check if we have counts for the given year, if not initialize and empty dictionary to hold them
    year = taxon_dictionary['date'].year
    if year not in counts_dictionary:
        counts_dictionary[year] = {}
    # each row contains a comma separated list of taxons, split on the comma to count each taxon separately
    for value in taxon_dictionary['taxon']:
        # remove any white spaces so that ' human' will be the same as 'human' etc...
        value = value.strip()
        # increment the count for the taxon or initialize it to 0 and add 1 if it does not exist
        counts_dictionary[year][value] = counts_dictionary[year].get(value, 0) + 1
    # return the updated counts dictionary
    return counts_dictionary


start = time.time()
# empty list to hold the contents of the file
lst = []
# TODO - ENSURE THAT THIS MATCHES THE PATH TO YOUR FILE
with open('./cleaned_GPMDB_table.tsv', 'r') as f:
    # move the file past the header line as we do not need it
    f.readline()
    # go through every line in the file
    for line in f:
        # strip the line endings(this removes the \n from the end of each line) then split the line on the \t
        temp = line.strip().split('\t')
        # check that there are the correct number of columns in the row otherwise raise an exception
        if len(temp) == 23:
            lst.append(temp)
        else:
            raise Exception('There are not 23 columns in line {} of the file.'.format(len(lst) + 1))

# apply the extract function using map to the list of rows from the file
date_taxon_list = map(extract, lst)
# filter the mapped data so that only entries within the specified dates kept
date_taxon_2010_list = filter(lambda row: 'sp|TRYP_PIG|' not in row['mcp'] and 'sp|ALBU_BOVIN|' not in row['mcp'],
                              date_taxon_list)

# reduce the filtered list of dictionaries down to a single dictionary containing a count for each taxon
counts = reduce(reduce_dict, date_taxon_2010_list, {})
# find the taxon with the highest count each year and print it (sorted sorts the dictioanry by year)
for k, v in sorted(counts.items(), key=lambda x: x[0]):
    print('year: {}, max: {:<20} - {:>8}'.format(k, *max(v.items(), key=lambda x: x[1])))
print("program took {} seconds to execute".format(time.time() - start))
