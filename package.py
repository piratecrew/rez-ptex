name = "ptex"

version = "2.1.28"

variants = [
    ["platform-linux"]
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
