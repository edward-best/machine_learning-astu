import pandas

data = pandas.read_csv('titanic.csv')
ages = data['Age'][data['Class/Dept'].str.contains("Class")]
avg = ages.mean().round(2)
mdn = ages.median()

print(f"Средняя по возрасту составляет {avg}, медиана возраста составляет {mdn}")