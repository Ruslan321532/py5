Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

delited = Geeks.pop("bag")
Geeks['address'] = 'Ibraimova 103'
Geeks['phone'] = '+996507052018'
Geeks['instagram'] = '@geeks_edu'
additioanl_courses = ['JavaScript', 'UX/UI', 'Figma', 'Java', 'Ios', 'Android']
Geeks['courses'] = set(Geeks['courses'] + additioanl_courses)
Geeks["date"] = "05.2018"

# Geeks['courses'].append('Основы программирования',)
print("Количество курсов:", len(Geeks['courses']))
for key, value in Geeks.items():
    print(key + ":", value)