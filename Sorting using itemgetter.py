from operator import itemgetter

tup_lst = [
    ('Jony', '17', '93'), #format(name, age, score)
    ('Tom', '19', '80'),
    ('Jony', '17', '91'),
    ('Json', '21', '85'),
    ('John', '20', '90')
    ]

print(sorted(tup_lst, key=itemgetter(1))) #sorting by age