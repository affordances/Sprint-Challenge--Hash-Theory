def get_indices_of_item_weights(weights, limit):
    candidates = {}
    for i, weight in enumerate(weights):
        candidates[weight] = i
    for i, weight in enumerate(weights):
        if limit - weight in candidates:
            j = candidates[limit - weight]
            if i > j:
                return (i, j)
            else:
                return (j, i)
    return ()


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
