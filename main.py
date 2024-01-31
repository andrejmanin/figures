def figure_a():
    print("***\n.**\n..*\n")
def figure_b():
    print("*..\n**.\n***\n")
def figure_v():
    print("***\n.*.\n...\n")
def figure_g():
    print("...\n.*.\n***\n")
def figure_d():
    print("***\n.*.\n***\n")
def figure_e():
    print("*.*\n***\n*.*\n")
def figure_j():
    print("*..\n**.\n*..\n")
def figure_z():
    print("..*\n.**\n..*\n")
def figure_u():
    print("***\n**.\n*..\n")
def figure_k():
    print("..*\n.**\n***\n")

def show():
    # funks = [figure_a(), figure_b(), figure_v(), figure_g(), figure_d(), figure_e(), figure_j(), figure_z(), figure_u(), figure_k()]
    inp = ''
    print("You can use this symbols: a, b, v, g, d, e, j, z, u, k")
    while(inp not in {'n', 'N'}):
        inp = str(input("Enter a figure leter: "))
        if(inp == 'a' or inp == 'A'):
            figure_a()
        elif(inp == 'b' or inp == 'B'):
            figure_b()
        elif (inp == 'v' or inp == 'V'):
            figure_v()
        elif (inp == 'g' or inp == 'G'):
            figure_g()
        elif (inp == 'd' or inp == 'D'):
            figure_d()
        elif (inp == 'e' or inp == 'E'):
            figure_e()
        elif (inp == 'j' or inp == 'J'):
            figure_j()
        elif (inp == 'z' or inp == 'Z'):
            figure_z()
        elif (inp == 'u' or inp == 'U'):
            figure_u()
        elif (inp == 'k' or inp == 'K'):
            figure_a()
        else:
            print("You entered wrong letter!")
            break



show()