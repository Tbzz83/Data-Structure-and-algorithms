class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self): # Count ancestors
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self, value=None):
        if value is not None:
            if self.get_level() <= value:
                spaces = ' ' * self.get_level() * 3
                prefix = spaces + '|--' if self.parent else ''
                print(prefix + self.data)
                if self.children:
                    for child in self.children:
                        child.print_tree(value)
        else:
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + '|--' if self.parent else ''
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree()
            # Best method
            # if self.get_level() > level:
            #             return
            #         spaces = ' ' * self.get_level() * 3
            #         prefix = spaces + "|__" if self.parent else ""
            #         print(prefix + self.data)
            #         if self.children:
            #             for child in self.children:
            #                 child.print_tree(level)
def build_product_tree():
    root = TreeNode('Global')

    india = TreeNode('India')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Adhmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Banglurur'))
    karnataka.add_child(TreeNode('Mysore'))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode('USA')

    new_jersey = TreeNode('New Jersey')
    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))

    california = TreeNode('California')
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))

    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)


    return root


root = build_product_tree()
root.print_tree(1)
# print(root.get_level())




