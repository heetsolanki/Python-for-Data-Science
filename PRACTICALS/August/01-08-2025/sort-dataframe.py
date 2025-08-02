import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas', 'Suresh'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19, 15.5],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

df = pd.DataFrame(exam_data, index=labels)

sorted_df = df.sort_values(by=['name', 'score'], ascending=[False, True])
print(sorted_df)
