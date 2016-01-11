###Simulacram
Simulacram is a simple way to pass in a dictionary object, with column names and corresponding data types and output a pandas
DataFrame of random data. This is great for creating a fake data set or testing a data science script whose validity through
generalization needs to be tested. This is still a work in Progress. right now numerical data can be made to fit a common
statistical distribution so long as the proper statistical parameters are included with the type key in the dictionary.

###Installation

`$ git clone https://github.com/jbrambleDC/simulacram.git && cd simulacram`

`$ python setup.py install`

###Usage
To create a fake pandas dataframe consisting of 100 rows. we would do the following:
```python

import simulacram as sm

test = {'entries': {'type': 'exp', 'lam': 0.5}, 'names': {'type': 'name'}, 'salaries': {'type': 'norm', 'mean': 55000, 'sd': 20000}}
res = sm.create(100, coltypes=test)
```
For the test variable which will be passed as coltypes, each key corresponds to the column name. Each value must be a dictionary
with one key being type and then whatever statistical parameters if any correspond to that type. Please review source code to
see how to properly pass the correct keys and values. Possible types are as follows:

`{'num': num_data, 'int': num_int, 'norm': norm_data, 'exp': exp_data, 'bin': binom_data, 'pois': poisson_data, 'txt': text_data, 'name': name_data, 'addr': address_data, 'zip': zip_data}`

Each key corresponds to a possible type, and the value is the function called in the source.

