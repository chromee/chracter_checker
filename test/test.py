import os

params = [['aaa', 1, 2, 3, 4], ['bbb', 2, 3, 4, 5], ['ccc', 3, 4, 5, 6]]
tag = ""
for p in params:
    tag += r"""
<image file='{0}'>
  <box top='{1}' left='{2}' width='{3}' height='{4}'/>
</image>""".format(p[0], p[1], p[2], p[3], p[4])

print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# f = open('a.txt', 'w')
# f.write(tag)
#
# f.close()
