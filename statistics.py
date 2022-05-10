import math
def calculateStats(numbers):
  """ function that calculates statistics like average, minimum and maximum of numbers """
  computed_stats = {"avg": math.nan, "max": math.nan, "min": math.nan}
  if numbers:
    average = sum(numbers)/len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    computed_stats.update({"avg":average, "max": maximum, "min": minimum})
  return computed_stats
