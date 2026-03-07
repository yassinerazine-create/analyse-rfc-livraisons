def version_to_tuple(v):

    try:
        return tuple(int(x) for x in str(v).split("."))
    except:
        return (0,)
