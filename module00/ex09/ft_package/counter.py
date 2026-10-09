def count_in_list(lst: list, item: object) -> int:
    """Count how many times an item appears in a list."""
    count = 0
    for n in lst:
        if item == n:
            count += 1
    return count
