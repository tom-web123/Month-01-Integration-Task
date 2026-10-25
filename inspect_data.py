import csv

# with open('Tabata_wards.csv', encoding= 'utf-8-sig') as f:
#     reader = csv.DictReader(f)     
#     rows = list(reader)

# print('Number of rows:', len(rows))
# print('Columns:', list(rows[0].keys()))


# values = []
# for row in rows:
#     raw = row['area_km2'].strip()
#     if raw== '':
#         continue
#     values.append(float(raw))
#     value = float(row['area_km2'])
#     values.append(value)

# print('Largest value:', max(values))
# print('Smallest value:', min(values))    
# print('Count:', len(values))

def inspect_column(filename, column):
    with open(filename, encoding= 'utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw== '':
            continue
        values.append(float(raw))

    return{
        'smallest':min(values),
        'largest':max(values),
        'count':len(values)
    }    

result = inspect_column('Tabata_wards.csv', 'area_km2')
print(result)

result = inspect_column('Tabata_wards.csv', 'population')
print(result)

