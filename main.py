def reverse_merge(*args):
    """
    Merges multiple lists and returns the merged list in reversed order.

    Parameters:
        *args (list): Variable number of lists to be merged.

    Returns:
        list: The merged list in reversed order.
    """
    merged_list = []
    for lst in args:
        merged_list.extend(lst)
    return merged_list[::-1]


if __name__ == '__main__':
    # Teste deine Funktion
    print(
        reverse_merge([1, 2], [3, 4], [5, 6])
    )  # Erwarteter Output: [6, 5, 4, 3, 2, 1]
