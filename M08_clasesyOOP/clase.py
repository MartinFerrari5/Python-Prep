class Ver:
    def __init__(self,valores):
        self.valor=valores
        print("No se han proporcionado valores")
    
#     def prim (self,val1):
#         primo=True
#         for i in range(2,val1):
#             if val1%i==0:
#                 primo=False
#                 return print(primo)
#         return  print(primo)
#     def contar (self):
#         lista_num=[]
#         lista_repetidos=[]
#         for i in self.valores:
#             if i in lista_num:
#                 indice = lista_num.index(i)
#                 lista_repetidos[indice]+=1
#             else:
#                 lista_num.append(i)
#                 lista_repetidos.append(1)
#         res = 0
#         b=0
#         for i in lista_repetidos:
#             if(i>b):
#                 indice = lista_repetidos.index(i)
#                 numero= lista_num[indice]
            
#                 res = "El numero que más se repite es",numero,"un total de",i,"veces"
#                 b=i
#             elif(i==b):
#                 indice = lista_repetidos.index(i)
#                 indice2 = lista_repetidos.index(i,indice+1)
#                 numero= lista_num[indice]
#                 numero2= lista_num[indice2]
#                 res="Los numeros que más se repiten son", numero, "y",numero2,"un total de",i,"veces"
#                 b=i
            
#         return res
#     def temp(self,valor, input, output):
#         if(input=="c"):
#             if(output=="f"):
#                 res= valor * (9/5) + 32
#             else: 
#                 res= valor + 273.15
#         elif(input=="f"):
#             if(output=="c"):
#                 res= (valor-32)/(9/5) 
#             else: 
#                 res = (valor-32)/(9/5) + 273.15
#         else:
#             if(input=="c"):
#                 res = valor - 273.15
#             else:
#                 res= (valor - 273.15)  * (9/5) + 32
#         return res
    
# def fact (val):
#     if(type(val)!=int or val<0):
#          return None
#     if(val>1):

#         val=val * fact(val-1)
#     return val