# https://en.wikipedia.org/wiki/Knuth's_up-arrow_notation

def knuth_operation(base, power, up_arrows):
  """
  Knuth's up-arrow notation is a generalization of hyperoperations

  The mathematical notation is like this :
    base ↑^m  power

  The m=1 hyperoperation refers to the exponentiation :
    base ↑ power = base^power

  The m=2 hyperoperation refers to the tetration :
    base ↑↑ power = 2 ↑ (2 ↑ (2 ↑ 2)) = 2^(2^(2^2)) = 2^(2^4) = 65 536

  Dummy implementations because Python is not happy with recursivity
  """
  if not isinstance(base, (int, float)):
    raise TypeError('the `base` parameter must be a number (integer or float)')
  if base == 0 or base == 1:
    return base

  if not isinstance(power, (int, float)):
    raise TypeError('the `power` parameter must be a number (integer or float)')
  if power == 0:
    return 1

  if not isinstance(up_arrows, int):
    raise TypeError('The `up_arrows` parameter must be an integer')
  if not (0 < up_arrows < 3):
    raise ValueError('The `up_arrows` parameter must be between 1 and 2')

  if up_arrows == 1:
    return base ** power

  if up_arrows == 2:
    i, acc = power, base
    while i > 0:
      acc = acc ** base
      i -= 1
    return acc

if __name__ == '__main__':
  """ Testing the function """
  tests = [
    {'base': 0, 'power': 2, 'up_arrows': 4, 'result': 0},
    {'base': 0, 'power': 4, 'up_arrows': 2, 'result': 0},
    {'base': 100, 'power': 0, 'up_arrows': 5, 'result': 1},
    {'base': 20, 'power': 0, 'up_arrows': 2, 'result': 1},
    {'base': 2, 'power': 4, 'up_arrows': 1, 'result': 16},
    {'base': 3, 'power': 3, 'up_arrows': 2, 'result': 7625597484987},
  ]

  for test in tests:
    computed = knuth_operation(test['base'], test['power'], test['up_arrows'])

    if computed == test['result']:
      print("[✔] {base} ↑^{up_arrows} {power} = {result}".format(**test))
    else:
      print("[✖] {base} ↑^{up_arrows} {power} != {result}".format(**test))

  type_error_fails = [
    {'base': 'a', 'power': 0, 'up_arrows': 2},
    {'base': 0, 'power': False, 'up_arrows': 2},
    {'base': 0, 'power': 0, 'up_arrows': 1.2},
  ]
  for fail in type_error_fails:
    try:
      knuth_operation(**fail)
    except TypeError as e:
      print("[✔] {base} ↑^{up_arrows} {power} correctly fails".format(**fail))

  try:
    knuth_operation(3, 5, -2)
  except ValueError:
    print("[✔] 3 ↑^(-2) 5 correctly fails")
