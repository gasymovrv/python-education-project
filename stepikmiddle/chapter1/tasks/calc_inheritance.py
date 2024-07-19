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


n = int(input())

flat_nodes = dict()
for i in range(n):
    classes = input().split(' : ')
    child_name = classes[0]

    parent_names = []
    if len(classes) > 1:
        parent_names = classes[1].split(' ')

    # create or find parent nodes
    parents = []
    for pn in parent_names:
        if pn in flat_nodes:
            parent = flat_nodes[pn]
        else:
            parent = Node(pn)
            flat_nodes[pn] = parent
        parents.append(parent)

    # create or find child node
    if child_name in flat_nodes:
        child = flat_nodes[child_name]
    else:
        child = Node(child_name)
        flat_nodes[child_name] = child

    # add child to parents
    for p in parents:
        p.add_child(child)

q = int(input())

results = []
for i in range(q):
    query = input().split(' ')
    class1 = flat_nodes.get(query[0])
    class2 = query[1]
    if class1 is not None and class1.has_child(class2):
        results.append('Yes')
    else:
        results.append('No')

for r in results:
    print(r)
