name = "ptex"

version = "2.1.28"

#requires = [
#  "pyside"
#]

variants = [
    ["platform-linux"]
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python2.7/site-packages")
