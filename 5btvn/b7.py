def remove_dollar_sign(st):
    new_st = st.replace("$", "")
    return new_st
st = str(input("Enter a string: "))
new_st = remove_dollar_sign(st)
print(new_st)