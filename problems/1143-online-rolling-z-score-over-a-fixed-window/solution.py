import collections
import math
def rolling_zscore(stream, window):
    # stream: list of numbers
    # window: positive int, fixed window size
    # return: list of floats, same length as stream
    stream_list = list(stream)
    if not stream_list or window <= 0:
        return [0.0 for _ in stream_list] if stream_list else []

    result = []
    dq = collections.deque()

    for x in stream_list:
        dq.append(x)
        if len(dq) > window:
            dq.popleft()

        # Warm-up period: fewer than `window` values observed
        if len(dq) < window:
            result.append(0.0)
        else:
            # Compute mean and population variance over the rolling window
            mean = sum(dq) / window
            variance = sum((val - mean) ** 2 for val in dq) / window
            std_dev = math.sqrt(variance)

            # If standard deviation is zero, avoid division by zero and emit 0.0
            if std_dev == 0.0:
                result.append(0.0)
            else:
                z = (x - mean) / std_dev
                result.append(float(z))

    return result
    
    pass