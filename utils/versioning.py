import re


def version_to_tuple(version):

    version = str(version).replace(":", ".")
    nums = re.findall(r'\d+', version)

    return tuple(int(n) for n in nums)
