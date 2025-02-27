# Первые n строк - описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

# Sample Input:
#
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A

# Sample Output:
#
# Yes
# Yes
# Yes
# No


class Node:
    def __init__(self, name, children=None):
        if children is None or not isinstance(children, list):
            children = []

        self.name = name
        self.children = children

    def __repr__(self):
        return f"(name: {self.name}, children: {self.children})"

    def __eq__(self, other):
        return self.name == other.name

    def has_child(self, child_name):
        if self.name == child_name:
            return True
        if self.children is None:
            return False

        result = False
        for child in self.children:
            if child.name == child_name:
                return True
            result = child.has_child(child_name)
            if result:
                return True

        return result

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        self.children.extend(children)


class BidirectionalNode(Node):
    def __init__(self, name, children=None, parents=None):
        super().__init__(name, children)
        if parents is None or not isinstance(parents, list):
            parents = []
        self.parents = parents

    def has_parent(self, p_name):
        if self.name == p_name:
            return True
        if self.parents is None:
            return False

        result = False
        for p in self.parents:
            if p.name == p_name:
                return True
            result = p.has_parent(p_name)
            if result:
                return True

        return result

    def has_any_parent(self, p_names):
        for p_name in p_names:
            if self.has_parent(p_name):
                return True

    def add_parent(self, p):
        self.parents.append(p)

    def add_parents(self, ps):
        self.parents.extend(ps)


def create_hierarchy(bi_node=False, hierarchy=None):
    n = int(input())
    if hierarchy is None:
        hierarchy = dict()

    for i in range(n):
        # child is only one name on the left
        classes = input().split(" : ")
        child_name = classes[0]

        # parents are several names separate by space on the right (multiple inheritance)
        parent_names = []
        if len(classes) > 1:
            parent_names = classes[1].split(" ")

        # create or find parent nodes
        parents = []
        for pn in parent_names:
            if pn in hierarchy:
                parent = hierarchy[pn]
            else:
                if bi_node:
                    parent = BidirectionalNode(pn)
                else:
                    parent = Node(pn)
                hierarchy[pn] = parent
            parents.append(parent)

        # create or find child node
        if child_name in hierarchy:
            child = hierarchy[child_name]
        else:
            if bi_node:
                child = BidirectionalNode(child_name)
            else:
                child = Node(child_name)
            hierarchy[child_name] = child

        # add child to parents and parents to child for BidirectionalNode
        for p in parents:
            p.add_child(child)
            if bi_node:
                child.add_parent(p)
    return hierarchy


# Exclude this execution from imports
if __name__ == "__main__":
    print("I'm in main")
    nodes = create_hierarchy()

    q = int(input())

    results = []
    for i in range(q):
        query = input().split(" ")
        class1 = nodes.get(query[0])
        class2 = query[1]
        if class1 is not None and class1.has_child(class2):
            results.append("Yes")
        else:
            results.append("No")

    for r in results:
        print(r)

else:
    print(f"{__name__} imported")
