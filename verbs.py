import pandas as pd

cards = pd.read_csv('C:/MyStuff/DataScience/Projects/Italian/italianexport.csv', index_col = False)

words = cards['Field 1 (Front)']

words[1].endswith('ere')

# get words that end in ere (almost always a verb)
ere = [word for word in words if word.endswith('ere')]

# get words that end in are (almost always a verb)
are = [word for word in words if word.endswith('are')]

# get words that end in ire (almost always a verb)
ire = [word for word in words if word.endswith('ire')]


ere.extend(ire)
ere.extend(are)

verbs = pd.DataFrame({'Verbs':ere})

verbs.to_csv('C:/MyStuff/DataScience/Projects/Italian/verbs.csv', index = False)



