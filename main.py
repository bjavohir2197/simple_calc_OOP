class Kalkulyator:
    versiya_nomeri = "1.0"

    @staticmethod
    def qosh(a, b):
        """Ikki sonni qo‘shadi"""
        return a + b

    @staticmethod
    def ayir(a, b):
        """Ikki sonni ayiradi"""
        return a - b

    @staticmethod
    def kopaytir(a, b):
        """Ikki sonni ko‘paytiradi"""
        return a * b

    @classmethod
    def versiya(cls):
        """Kalkulyator versiyasini qaytaradi"""
        return f"Kalkulyator versiyasi: {cls.versiya_nomeri}"



print(Kalkulyator.qosh(5, 3))       
print(Kalkulyator.ayir(10, 4))      
print(Kalkulyator.kopaytir(6, 7))    
print(Kalkulyator.versiya())         
