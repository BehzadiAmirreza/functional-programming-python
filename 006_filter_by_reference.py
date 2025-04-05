def filter_values(reference, values):
    """
    Filters the `values` list based on the binary `reference` list.
    Returns a new list containing only the values where the corresponding
    reference value is 1.
    """
    return list(v for _, v in filter(lambda rv: rv[0] == 1, zip(reference, values)))

if __name__ == "__main__":
    reference = [0, 1, 1, 0, 1, 0]
    values = ["a", "b", "c", "d", "e", "f"]
    filtered_values = filter_values(reference, values)
    print(filtered_values)
