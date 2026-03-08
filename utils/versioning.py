def version_to_tuple(v: str):
    """
    Convertit une version type 025.110.12:01 en tuple pour comparer.
    Remplace les séparateurs '.' et ':' par des int
    """
    if v is None:
        return tuple()
    parts = []
    for part in v.replace(':', '.').split('.'):
        try:
            parts.append(int(part))
        except:
            parts.append(0)
    return tuple(parts)
