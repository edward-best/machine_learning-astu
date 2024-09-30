import pandas
import re

women_attrs = [
    "Miss",
    "Mrs",
    "Mme",
    "Lady",
    "Mlle",
    "Ms",
    "Countess",
    "Dona",
]

women_regex = list(map(lambda w: f"\\b{w}\\b", women_attrs))

def extract_name(raw: str) -> str | None:
    exp = re.compile("|".join(women_regex))
    for word in raw.split():
        if not exp.search(word):
            return word
    return None

data = pandas.read_csv('titanic.csv')
women_names = data['Name'][data['Name'].str.contains("|".join(women_regex), regex=True)] \
    .map(lambda raw: ",".join(raw.split(",")[1:])) \
    .map(extract_name)

most_popular = women_names.value_counts().head(1)

print(f"Самым популярным женским именем среди пассажиров было {most_popular.index.to_list()[0]}")
