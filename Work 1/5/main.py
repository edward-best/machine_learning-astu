import pandas

data = pandas.read_csv('Титаник.csv', index_col='PassengerId', encoding='utf-16-le', sep=';')

print(f"Степень корреляции составляет {data['Родственики2гоПорядка'].corr(data['Родственики1гоПорядка'])}")
