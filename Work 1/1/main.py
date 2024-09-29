import pandas

data = pandas.read_csv('titanic.csv')
men = data['Name'][data['Name'].str.contains("|".join(["Mr ", "Master", "Sig"]))].count()
women = data['Name'][data['Name'].str.contains("|".join(["Miss", "Mrs", "Mme"]))].count()

print(f"На корабле плавало {men} мужчин, {women} женщин и {data['Name'].count() - men - women} неопознанного рода")