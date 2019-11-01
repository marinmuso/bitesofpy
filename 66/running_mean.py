def running_mean(sequence):
   total = 0
   avgs = [0] * len(sequence)
   for ind, num in enumerate(sequence):
      total += num
      avgs[ind] = round(total / (ind + 1), 2)
   return avgs
   