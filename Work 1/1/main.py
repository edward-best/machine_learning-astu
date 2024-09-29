import pandas

data = pandas.read_csv('Титаник.csv', encoding='utf-16-le', sep=';')
counted = data['Пол'].value_counts()

print(f"На корабле плыло {counted['мужской']} мужчин и {counted['женский']} женщин")