import json
import numpy as np
import tsp

with open('DistanceMatrixResponse.json') as json_file:
    data = json.load(json_file)


def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

travel_values = extract_values(data, 'value')
durations = travel_values[::2]
np_dur = np.array(durations)
import math
dur_len = int(math.sqrt(len(np_dur)))

B = np.reshape(np_dur, (-1, dur_len)).tolist()
r = range(len(B))
# Dictionary of distance
dist = {(i, j): B[i][j] for i in r for j in r}
data = tsp.tsp(r, dist)
print(data[1])

