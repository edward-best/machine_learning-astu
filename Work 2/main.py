from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.feature_selection import SelectKBest, RFE, f_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def generate_data():
    np.random.seed(0)
    size = 750
    X = np.random.uniform(0, 1, (size, 14))
    Y = (10 * np.sin(np.pi * X[:,0] * X[:,1]) + 20 * (X[:,2] - .5) ** 2 + \
         10 * X[:,3] + 5*X[:,4] ** 5 + np.random.normal(0,1))
    X[:,10:] = X[:,:4] + np.random.normal(0, .025, (size, 4))

    return (X, Y)

def rank_to_dict(ranks, value_names):
    ranks = np.abs(ranks)

    min_max = MinMaxScaler()

    ranks = min_max.fit_transform(np.array(ranks).reshape(14, 1)).ravel()
    ranks = map(lambda x: round(x.item(), 2), ranks)
    return dict(zip(value_names, ranks))

data = generate_data()

# Создание объекта линеной регрессии
linear = LinearRegression()
linear.fit(*data)

# Создание объекта гребневой регрессии
ridge = Ridge(alpha=7)
ridge.fit(*data)

# Создание объекта регрессии лассо
lasso = Lasso(alpha=.05)
lasso.fit(*data)

# Создание модели с методом рекурсивного исключения признаков
tmp_linear = LinearRegression()
tmp_linear.fit(*data)
rfe = RFE(tmp_linear)
rfe.fit(*data)

# Создание объекта случайного леса
random_forest = RandomForestRegressor(n_estimators=10, random_state=42)
random_forest.fit(*data)

# Модель с использованием метода F регрессии
fs = SelectKBest(score_func=f_regression, k='all')
fs.fit(*data)

value_names = ["x%s" % i for i in range(1, 15)]

ranks = {}
ranks["Linear Regression"] = rank_to_dict(linear.coef_, value_names)
ranks["Ridge"] = rank_to_dict(ridge.coef_, value_names)
ranks["Lasso"] = rank_to_dict(lasso.coef_, value_names)
ranks["RFE"] = rank_to_dict(rfe.ranking_, value_names)
ranks["Random Forest Regression"] = rank_to_dict(random_forest.feature_importances_, value_names)
ranks["F Regression"] = rank_to_dict(fs.scores_, value_names)

mean = {}

for key, value in ranks.items():
    for item in value.items():
        if(item[0] not in mean):
            mean[item[0]] = 0
        mean[item[0]] += item[1]
    
for key, value in mean.items():
    res = value / len(ranks)
    mean[key] = round(res, 2)

mean = sorted(mean.items(), key = lambda x: x[1], reverse=True) 

print("Mean")
print(mean)

for key, value in ranks.items():
    ranks[key] = sorted(value.items(), key=lambda x: x[1], reverse=True)

for key, value in ranks.items():
    print(key)
    print(value)

