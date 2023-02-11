impossible_values = [2, 3 ,4 ,5 ,6 , 7, 8 ]
impossible_values[3] = -1
impossible_values[:3] = impossible_values[4:]
print(impossible_values)