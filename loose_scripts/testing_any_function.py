"""
Using any() function to check in given programmer has desired set of skills.

"""
# ver. 1


def programmer_checker(list):
    boolList = []
    for record in list:
        if (('Python' in record['skills']) and ('JavaScript' in record['skills'])):
            boolList.append(True)
        else:
            boolList.append(False)
    return any(boolList)

# ver. 2


def programmer_checker2(list):
    return any([(('Python' in record['skills']) and ('JavaScript' in record['skills'])) for record in list])


john = {'name': 'John Doe',
        'age': 30,
        'skills': ['Python', 'JavaScript', 'C++']}

jane = {'name': 'Jane Smith',
        'age': 25,
        'skills': ['Python', 'JavaScript', 'Java']}


programmers = [john, jane]

print(programmer_checker2(programmers))
