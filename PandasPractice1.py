#My first code implemented on python without using pandas
__parsed_rows = []

def parse_csv():
    import csv
    __file_path = "C:\\Users\\<name>\\Downloads\\Import_User_Sample_en.csv"
    __index = {
        'user_name': 0,
        'first_name': 1,
        'last_name': 2,
        'job_title': 3,
        'department': 4,
        'office_number': 5,
        'mobile_phone': 6,
        'fax': 7,
        'address': 8,
        'city': 9,
        'state_or_province': 10,
        'zip_or_postal_code': 11,
        'country_or_region': 12 
    }

    global __parsed_rows
    with open(__file_path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            __parsed_rows.append( {
                'user_name': row[__index['user_name']],
                'first_name': row[__index['first_name']],
                'last_name': row[__index['last_name']],
                'job_title': row[__index['job_title']],
                'department': row[__index['department']],
                'office_number': row[__index['office_number']],
                'mobile_phone': row[__index['mobile_phone']],
                'fax': row[__index['fax']],
                'address': row[__index['address']],
                'city': row[__index['city']],
                'state_or_province': row[__index['state_or_province']],
                'zip_or_postal_code': row[__index['zip_or_postal_code']],
                'country_or_region': row[__index['country_or_region']] 
            })

def display():
    for row in __parsed_rows:
        print(row)


if __name__ =='__main__':
    parse_csv()
    display()
