import re

def version_to_tuple(v: str):
    try:
        return tuple(int(x) for x in re.findall(r'\d+', str(v)))
    except:
        return (0,)
