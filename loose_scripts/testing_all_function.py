"""
Using all() function to check in given programmer has desired set of skills.

"""


def has_required_skill(person, skills):
    return all(skill in person['skills'] for skill in skills)


john = {'name': 'John Doe', 'age': 30,
        'skills': ['Python', 'JavaScript', 'C++']}

jane = {'name': 'Jane Smith', 'age': 25, 'skills': ['Python', 'Java']}


requiredSkills = ['Python', 'JavaScript']

print(has_required_skill(john, requiredSkills))


print(skill in john['skills'] for skill in requiredSkills)
