from logmap import LogMap
import numpy as np
import tensorflow as tf


def main():
    logmap = LogMap(3.94)
    data = logmap.log_map_data(100, 0.2)
    print(data)
    tf.data.Dataset().from_tensor_slices([(1, 2,3), (4, 5, 6)])

if __name__ == '__main__':
    main()
    for i in range(20):
        print('hello')
    