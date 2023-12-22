import subprocess as sp


def read_k_configs() -> any:
    if dirs != 0:
        dirs = read_k_configs()
        txt = sp.run(["find", "-maxdepth", "1", "-type", "d"], stdout=sp.PIPE)
        testing = txt.stdout.decode("utf-8").split("\n")
        print(testing)
    return len(testing)

tst = read_k_configs()