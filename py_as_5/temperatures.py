import numpy as np

temperatures = [30, 32, 31, 29, 28, 33]

# converting array into numpy array
temperatures = np.array(temperatures)
print("Numpy Array:\n", temperatures)

#Reshaping into 2x3 matrix
temp_matrix = temperatures.reshape(2,3)
print("Reshaped into 2x3 matrix:\n", temp_matrix)

#Finding the  max temperature
temp_max = np.max(temperatures)
print("max temperature:\t", temp_max)

#Finding the average temperature of every row
temp_row_avg = np.mean(temp_matrix, axis = 1)
print("Every row average temperature:\t", temp_row_avg)

#Temperature of the week using mean 
week_temp_avg = np.mean(temperatures)
print("Average temperature of the week:\t", week_temp_avg)

#boolean check all temperature with average temperature
bool_avg_temp = temperatures > week_temp_avg
print(bool_avg_temp)
