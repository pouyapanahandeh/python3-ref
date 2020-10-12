# ex 1
# |1  1   1   1   1|
# |1  0   0   0   1|
# |1  0   9   0   1|
# |1  0   0   0   1|
# |1  1   1   1   1|

import numpy as np

main_arr = np.ones((5,5), dtype="int32")
zero_arr = np.zeros((3,3), dtype="int32")
zero_arr[1,1] = 9
main_arr[1:-1,1:-1] = zero_arr
print(main_arr)