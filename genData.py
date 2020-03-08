import json
data = [{'title': 'Generic Report',
         'header':['Employee ID', 'First', 'Middle Initial', 'Last'],
         'footer':['FOOTER', 'FOOTER', 'FOOTER', 'FOOTER'],
         'rows':{
            'row1':['1000000000', 'John', 'C', 'Doe'],
            'row2':['1000123456', 'Keiran', 'C', 'Rowan'],
            'row3':['1000000000', 'Jane', 'D', 'Doe'],
            'row4':['1000000000', 'Doug', 'H', 'Smith']
         }}
        ]
with open('data/employeeData.json', 'w') as f:
    json.dump(data, f, indent=4)
