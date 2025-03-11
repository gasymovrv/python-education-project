import time
from collections import Counter, defaultdict

lst = ['a', 'b', 'a', 'c', 'b', 'a']

print("\n===================== counting using dict =====================")
counter = {}
for item in lst:
    counter[item] = counter.get(item, 0) + 1
print(counter)

print("\n===================== counting using Counter =====================")
counter = Counter(lst)
print(counter)

print("\n===================== counting using defaultdict =====================")
counter = defaultdict(int)  # int used as factory to create default values (int() creates 0)
for item in lst:
    counter[item] += 1

print(dict(counter))

print("\n===================== compare defaultdict and dict =====================")
#  Instead of doing a second lookup (like in a regular dict),
#  it holds a slot for the missing key and immediately fills it with the default value in a single step.
default_dict = defaultdict(int)
default_dict['missing']  # ✅ Automatically set to 0
print(default_dict)  # defaultdict(<class 'int'>, {'missing': 0})

regular_dict = {}
# print(regular_dict['missing'])  # ❌ KeyError!


print("\n===================== compare performance =====================")
lst = ['a', 'b', 'a', 'c', 'b', 'a'] * 1000000

# Using dict.get()
start = time.time()
counter_dict = {}
for item in lst:
    counter_dict[item] = counter_dict.get(item, 0) + 1
end = time.time()
print("dict (million elements incremented):", end - start)

# Using Counter
start = time.time()
counter = Counter(lst)
end = time.time()
print("Counter (million elements incremented):", end - start)

# Using defaultdict
start = time.time()
counter_dd = defaultdict(int)
for item in lst:
    counter_dd[item] += 1
end = time.time()
print("defaultdict (million elements incremented):", end - start)
