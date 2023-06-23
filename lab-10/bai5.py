school_details = {
	'students': [
			{'firstName': 'Nikki', 'lastName': 'Roysden'},
			{'firstName': 'Mervin', 'lastName': 'Friedland'},
			{'firstName': 'Aron ', 'lastName': 'Wilkins'}
	], 
	'teachers': [
			{'firstName': 'Amberly', 'lastName': 'Calico'},
			{'firstName': 'Regine', 'lastName': 'Agtarap'}
	]
}
print("Students: ")
for i in range(len(school_details["students"])):
    first_name = school_details['students'][i]["firstName"]
    last_name = school_details['students'][i]["lastName"]
    print(f" - {first_name} {last_name}")

print("Teacher: ")
for i in range(len(school_details["teachers"])):
    first_name = school_details['teachers'][i]["firstName"]
    last_name = school_details['teachers'][i]["lastName"]
    print(f" - {first_name} {last_name}")