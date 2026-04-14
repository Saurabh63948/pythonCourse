def pour_chai(n):
  if n == 0:
    return "All cups poured"
  print(n)
  return pour_chai(n-1)

print(pour_chai(3))