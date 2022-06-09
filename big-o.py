from stock_picker import picker
import time
import random
import statistics

functions = picker,
check = [random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100),random.randrange(1,100)]


# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
  for i in range(500):  # adjust accordingly so whole thing takes a few sec
    t0 = time.time()
    func(check)
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)



for name, numbers in times.items():
  print('FUNCTION:', name, 'Used', len(numbers), 'times')
  print('\tMEDIAN', statistics.median(numbers))
  print('\tMEAN  ', statistics.mean(numbers))
  print('\tSTDEV ', statistics.stdev(numbers))