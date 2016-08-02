name = "ptex"

version = "2.0.62"

variants = [
    ["platform-linux"]
]

def commands():
    env.CMAKE_MODULE_PATH.append("{root}/cmake")
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
