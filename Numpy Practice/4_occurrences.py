import numpy as np
a=np.array([1,1,2,2,2,3,3,3,3,4,4,4])
print(np.unique(a))
unique_elements,count=np.unique(a,return_counts="true")
print(f"elements {unique_elements} count {count}")