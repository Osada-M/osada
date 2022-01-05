import osada.__init__ as osada


def do_test():
    
    test_version()
    test_cprint()
    test_colored()
    test_array()
    


def test_version():
    print(osada.version)
    print(osada.getVersion())
    print(osada.versionMatch("0.0.0"))
    print(osada.versionMatch(osada.version))
    print(osada.versionMatch("1.0"))


def test_cprint():
    print("normal : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, end=" ")
    
    print("\n1.5    : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, c, end=" ", bloom=1.5)
    
    print("\nlight  : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, c, end=" ", bloom="light")
    
    print("\nnormal : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, c, end=" ")
    
    print("\ndark   : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, c, end=" ", bloom="dark")
    
    print("\n0.3    : ", end="")
    for c in osada.colors.keys():
        osada.cprint(f"{c}", c, c, end=" ", bloom=0.3)
    print()
    

def test_colored():
    print(f"光の三原色とは、{osada.colored('赤色', 'red')}、{osada.colored('緑色', 'green')}、{osada.colored('青色', 'blue')}の3つのことです。")
    
    
def test_array():
    print(osada.array(1, 2, 2))
    print(osada.array(1, 2, 3))
    print(osada.array(1, 2, 5))
    print(osada.randomArray(0, 1, 5))
    print(osada.randomArray(1, 10, 10, True))
    


if (__name__ == "__main__"):
    do_test()

