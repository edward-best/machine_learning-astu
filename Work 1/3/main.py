import pandas

data = pandas.read_csv('titanic.csv')
passengers = data[data['Class/Dept'].str.contains("Class")]
counted = passengers['Class/Dept'].value_counts(normalize=True).map(lambda x: x * 100).round(2)

print(f"Доля пассажиров первого класса составляет {counted['1st Class']}")