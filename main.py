class AB:
    # Construct
    def __init__(self, racine = None, left = None, right = None):
        if racine is not None:
            self.racine = [racine]
        else:
            self.racine = None
        self.left = left
        self.right = right

    #Getters
    def get_racine(self):
        return self.racine[0]
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    #Setters
    def set_racine(self, valeur):
        if self.racine is None:
            self.racine = [valeur]
        else:
            self.racine[0] = valeur

    def set_left(self, valeur):
        self.left = valeur

    def set_right(self, valeur):
        self.right = valeur

    #Method
    def isEmpty(self):
        return len(self.racine) == 0 and self.left is None and self.right is None

    def __str__(self):
        return f"AB({self.racine}, {self.left}, {self.right})"
    
    #Show tree parcours
    def display_prefix_tree(self):
        if self.isEmpty():
            print("Empty tree")
        else:
            print(self.get_racine())
            if self.get_left() is not None:
                self.get_left().display_prefix_tree()
            if self.get_right() is not None:
                self.get_right().display_prefix_tree()
    
    def display_infix_tree(self):
        if self.isEmpty():
            print("Empty tree")
        else:
            if self.get_left() is not None:
                self.get_left().display_infix_tree()
            print(self.get_racine())
            if self.get_right() is not None:
                self.get_right().display_infix_tree()

    def display_postfix_tree(self):
        if self.isEmpty():
            print("Empty tree")
        else:
            if self.get_left() is not None:
                self.get_left().display_infix_tree()
            if self.get_right() is not None:
                self.get_right().display_infix_tree()
            print(self.get_racine())

    #Show the size of a tree
    def tree_size(self):
        if self.isEmpty():
            return 0
        else:
            return 1 + (self.get_left().tree_size() if self.get_left() is not None else 0) + (self.get_right().tree_size() if self.get_right() is not None else 0)

    #Show the height of a tree
    def tree_height(self):
        if self.isEmpty():
            return -1
        else:
            left_height = self.get_left().tree_height() if self.get_left() is not None else -1
            right_height = self.get_right().tree_height() if self.get_right() is not None else -1
            return 1 + max(left_height, right_height)

    #Check if the tree is an ABR or not
    def isABR(self):
        if self.isEmpty():
            return True
        else:
            if self.get_left() is not None:
                if self.get_left().get_racine() > self.get_racine():
                    return False
                if not self.get_left().isABR():
                    return False
            if self.get_right() is not None:
                if self.get_right().get_racine() < self.get_racine():
                    return False
                if not self.get_right().isABR():
                    return False
            return True
        
    #Check if the tree is balanced or not
    def isBalanced(self):
        if self.isEmpty():
            return True
        else:
            delta = 0
            left_height = self.get_left().tree_height() if self.get_left() is not None else -1
            right_height = self.get_right().tree_height() if self.get_right() is not None else -1
            delta = abs(left_height - right_height)
            if delta > 1 or delta < -1:
                return False
            else:
                left_height = self.get_left().isBalanced() if self.get_left() is not None else True
                right_height = self.get_right().isBalanced() if self.get_right() is not None else True
                return True and left_height and right_height
            
#----------END CLASS--------------------------------#

# Functions to draw a prefix parcour tree from a file
def prefix_tree_from_file(parcours):
    if not parcours:
        return AB()
    else:
        racine = parcours[0]
        index_pivot = 1
        while index_pivot < len(parcours) and parcours[index_pivot] < racine:
            index_pivot += 1
        left = prefix_tree_from_file(parcours[1:index_pivot])
        right = prefix_tree_from_file(parcours[index_pivot:])
        return AB(racine, left, right)

# Functions to draw a postfix parcour tree from a file
def postfix_tree_from_file(parcours):
    if not parcours:
        return AB()
    else:
        racine = parcours[-1]
        index_pivot = len(parcours) - 2
        while index_pivot >= 0 and parcours[index_pivot] > racine:
            index_pivot -= 1
        left = postfix_tree_from_file(parcours[:index_pivot+1])
        right = postfix_tree_from_file(parcours[index_pivot+1:-1])
        return AB(racine, left, right)

# Functions to draw a infix parcour tree from a file
def infix_tree_from_file(parcours):
    if not parcours:
        return AB()
    else:
        milieu = len(parcours) // 2
        racine = parcours[milieu]
        left = infix_tree_from_file(parcours[:milieu])
        right = infix_tree_from_file(parcours[milieu+1:])
        return AB(racine, left, right)

# Function switch to know which parcour we need to apply
def make_binary_tree(data, type):
    with open(data, "r") as f:
        content = f.read()
    num = [int(x) for x in content.split()]
    if type == "prefix":
        return prefix_tree_from_file(num)
    elif type == "infix":
        return infix_tree_from_file(num)
    elif type == "postfix":
        return postfix_tree_from_file(num)
    else:
        print("Type de parcours inconnu.")


A1 = AB()
A2 = AB()
A2.set_racine(5)

A3 = AB()
A3.set_racine(3)
A2.set_left(A3)

A4 = AB()
A4.set_racine(8)
A2.set_right(A4)

A5 = AB()
A5.set_racine(10)
A5.set_left(A2)

A6 = AB()
A6.set_racine(12)
A5.set_right(A6)

# A5.display_prefix_tree()
# print("height", A5.tree_height())
# print(A5.isABR())
# print(A5.isBalanced())

# print(make_binary_tree("data.txt", "prefix"))
