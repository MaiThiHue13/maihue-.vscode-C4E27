prices ={
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3 
    }

stock={
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15 
    }

n = input("Mời nhập tên mặt hàng: ")
if n in prices and stock:
    print("price: ", prices[n])
    print("stock: ", stock[n])
else:
    print("Nhập sai rồi, mời bạn nhập lại:")
    n = input("Mời nhập tên mặt hàng: ")
    print("price: ",prices[n])
    print("stock: ", stock[n])
    
    
total = 0
for key in prices:
    print()
    print(key)
    print("price: ",prices[key])
    print("stock: ",stock[key])
    print("value",key,": ",prices[key] * stock[key] )
    print()
    total = total + (prices[key] * stock[key])

print("total: ",total)