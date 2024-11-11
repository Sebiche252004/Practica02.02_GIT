
#Precios

precio= input("Introduce el precio del producto en euros").replace(".",",")

division= precio.split(",") 

euros= division[0]

centimos= division[1]

print("El precio es",euros,"euros","con",centimos,"centimos")