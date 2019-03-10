n = input("mời nhập câu:")

bang_chu_cai= 'abcdefghijklmnopqrstuvxyz'
letter_count = {}
for k in n:
    if k in bang_chu_cai:
        if k in letter_count:
            letter_count[k] = letter_count[k]+1
        else:
            letter_count[k]=1

keys = letter_count.keys()
for k in sorted(keys):
    print(k, letter_count[k])

