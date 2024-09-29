import pandas

data = pandas.read_csv('Титаник.csv', index_col='PassengerId', encoding='utf-16-le', sep=';')
counted = data['Пол'].value_counts()

print(f"На корабле плыло {counted['мужской']} мужчин и {counted['женский']} женщин")