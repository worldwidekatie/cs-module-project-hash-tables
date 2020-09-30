# what Has Tables Solve

# We need to look up some data quickly
## Some data that was slow to generate or obtain

# In lieu of linear search...

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

var = d.items() # gives a list of tuples
#print(var)
var = sorted(var) # sorts by key

x = dict(var)
#print(x)

items = list(d.items())
# Sort by Value!
def sort_by(t):
    print(f'sort by({repr(t)}) called!')
    return t[1]

#y = items.sort(key=sort_by)


x = var.sort(key=lambda t: t[1], reverse=True)
print(x)