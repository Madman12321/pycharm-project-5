# Draws the top part of the tree
def tree(height):
    spaces = height - 1
    ast = 0
    for i in range(height):
        print(" " * (spaces) + ('*' * (ast + 1)))
        spaces -= 1
        ast += 2
    # TODO


# Draws the trunk for a tree of height
def trunk(height):
    for i in range(3):
        print(' ' * (height - 2), end='')
        print("*"*3)
        # TODO


def drawTree(height):
    tree(height)
    trunk(height)

drawTree(3)