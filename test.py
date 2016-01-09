import simulacram as sm

test = {'entries': {'type': 'exp', 'lam': 0.5}, 'names': {'type': 'name'}, 'salaries': {'type': 'norm', 'mean': 55000, 'sd': 20000}}
res = sm.create(100, coltypes=test)
print res

