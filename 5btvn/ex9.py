def get_even_list(ls):
    new_ls=[]
    for v in ls:
        if v%2==0:
            new_ls.append(v)
    return new_ls
ls= [1,4,5,-1,10]
new_ls = get_even_list(ls)
print(new_ls)