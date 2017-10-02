
# find the average number of bytes transferred to clients when they request data.

# Step 1: Read file line by line

# Step 2: Filter on GET requests

# Step 3: Extract bytes transferred from last column

# Step 4: Filter on numeric bytes (ignore records with "-" in bytes column)

# Step 4: Reduce relevant bytes to avg bytes transferred

import functools

fh = open('access-log')

get_requests = filter(lambda string: "GET" in string,
                      fh)

byte_records = map(lambda string: string.split()[-1],
                   get_requests)

relevant_byte_records = filter(lambda byte_string: byte_string != '-',
                               byte_records)

def aggregator(aggr_dict, value):
    aggr_dict['bytes'] = aggr_dict.get('bytes', 0) + int(value)
    aggr_dict['count'] = aggr_dict.get('count', 0) + 1
    return aggr_dict


result = functools.reduce(aggregator, relevant_byte_records, {})
print(result)
print("Average: ", result['bytes']/result['count'])


