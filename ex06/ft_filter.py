def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # If no function provided, use bool() as default (filters for truthy val)
    if function is None:
        function = bool

    # Use list comprehension to create filtered iterator
    return (item for item in iterable if function(item))
