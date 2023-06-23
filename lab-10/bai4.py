school_details = {
	'students': [
			{'firstName': 'Nikki', 'lastName': 'Roysden'},
			{'firstName': 'Mervin', 'lastName': 'Friedland'},
			{'firstName': 'Aron ', 'lastName': 'Wilkins'}
	]
}
print("Students: ")
for i in range(len(school_details["students"])):
    first_name = school_details['students'][i]["firstName"]
    last_name = school_details['students'][i]["lastName"]
    print(f" - {first_name} {last_name}")