class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.designation = ''

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self): # Count ancestors
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level


    def print_tree(self, choice):
        if choice == 'name':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + '|--' if self.parent else ''
            print(prefix + self.data)

            if self.children:
                for child in self.children:
                    child.print_tree('name')

        if choice == 'designation':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + '|--' if self.parent else ''
            print(prefix + self.designation)

            if self.children:
                for child in self.children:
                    child.print_tree('designation')

        if choice == 'both':
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + '|--' if self.parent else ''
            print(prefix + self.data, self.designation)

            if self.children:
                for child in self.children:
                    child.print_tree('both')





def build_product_tree():
    root = TreeNode("Nilupul")
    root.designation = "(CEO)"

    chinmay = TreeNode("Chinmay")
    chinmay.designation = '(CTO)'

    vishwa = TreeNode('Vishwa')
    vishwa.designation = '(Infrastructure Head)'

    dhaval = TreeNode('Dhaval')
    dhaval.designation = '(Cloud Manager)'

    abhijit = TreeNode('Abhijit')
    abhijit.designation = '(App Manager)'

    aamir = TreeNode('Aamir')
    aamir.designation = '(Application Head)'

    gels = TreeNode('Gels')
    gels.designation = '(HR Head)'

    peter = TreeNode('Peter')
    peter.designation = '(Recruitment Manger)'

    waqas = TreeNode('Waqas')
    waqas.designation = '(Policy Manager)'

    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)

    chinmay.add_child(vishwa)

    gels.add_child(peter)
    gels.add_child(waqas)

    root.add_child(chinmay)
    root.add_child(gels)

    return root


root = build_product_tree()
root.print_tree('both')
# print(root.get_level())




