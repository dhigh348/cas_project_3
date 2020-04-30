import numpy as np 
import tensorflow as tf
from tensorflow import keras
import math 

class LogMap:

	def __init__(self, r):
		self.r = r

	def log_map_func(self, x: float) -> float:
		'''
		Function to compute one iteration of the log map function at point x
		args:
			float value point
		returns:
			float value computed with log function
		'''
		return self.r * x * (1 - x)
	
	def log_map_data(self, iterations: int, start_value: float) -> np.ndarray:
		'''
		Function to create log map data for the specified number of iterations
		args:
			iteration integer
		returns:
			starting value float
		'''
		values = np.zeros((iterations, 1))
		values[0] = start_value
		for i in range(iterations - 1):
			values[i + 1] = self.log_map_func(values[i])
		return values

