import pandas

data = pandas.read_csv('titanic.csv')
counted = data['Survived'].value_counts(normalize=True).map(lambda x: x * 100).round(2)

for idx, passenger_status in enumerate(counted.index.to_list()):
    print(f"Доля пассажиров со статусом выживания {passenger_status} составляет {counted.iloc[idx]}")
