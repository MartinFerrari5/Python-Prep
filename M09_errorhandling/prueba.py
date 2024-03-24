import unittest

def temp(valor, input, output):
        if(type(input)!=str or type(output)!=str):
            raise TypeError("Non accepted characters")
        if(input=="c"):
            if(output=="f"):
                res= valor * (9/5) + 32
            else: 
                res= valor + 273.15
        elif(input=="f"):
            if(output=="c"):
                res= (valor-32)/(9/5) 
            else: 
                res = (valor-32)/(9/5) + 273.15
        else:
            if(input=="c"):
                res = valor - 273.15
            else:
                res= (valor - 273.15)  * (9/5) + 32
        return res

class Prueba(unittest.TestCase):
    # def __init__(self):
    #     pass
    def test_temp(self):
        res=temp(0,"c","k")
        return res
        # self.assertEqual(res,273.15)
a1=Prueba()
print(a1.test_temp())
# unittest.main(argv=[''], verbosity=2, exit=False)

