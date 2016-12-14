array = ["aaa", "bbb", "ccc"]

str = """aaaa
bbbbbbbbbbbbbb
cccccccccccccc
dddddddddddddd
eeeeeeeeeeeeee"""

params = [['aaa', 1, 2, 3, 4], ['bbb', 2, 3, 4, 5], ['ccc', 3, 4, 5, 6]]

for p in params:
    t = '<image file=\'{0}\'><box top=\'{y}\' left=\'{x]\' width=\'{w}\' height=\'{h}\'/></image>'.format(name=p[0], y=p[1], x=p[2], w=p[3], h=p[4], )
    print(t)

# f = open('text.txt', 'w')  # 書き込みモードで開く
# for a in array:
#     f.write(a)  # 引数の文字列をファイルに書き込む
#
# f = open('text.txt', 'r')
# print(f)
#
# f.close()  # ファイルを閉じる
