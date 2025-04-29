#product list:
products=[{"id": 1, "name":"roz Abi","price":170,"stock":300 ,"takhfif":},
{"id": 2, "name":"roz Sefid","price":100,"stock":100},"takhfif":10%]

def shoe_products():
    print("/n products list")
    for product in products:
        print(f"id:{product["id"]},name:{product["name"]},stock:{product["stock"]},")