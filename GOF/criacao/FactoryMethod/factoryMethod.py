from __future import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self) -> str:
        #chama o factory method para criar um objeto produto
        product = self.factory_method()

        #agora usa o produto
        result = f"Criando: o codigo do mesmo creator acabou de trabalhar com {product.operation()}"

        return result
    
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreator1()
    
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreator2()      

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado do ConcreteProduct2}"  
    
def cliente_code(creator: Creator) -> None:
    print(f"Cliente: Não conheço a classe do creator, mas ainda funciona; \n"
           f"{creator.some_operation()}",end="")
    
if __name__ == "__main__": # __AlgumaPalavra -> Sao palavras reservadas
    print("App: Lançado com o ConcreteCreator1.")
    cliente_code(ConcreteCreator1())
    print("\n")
    print("App: Lançado com o ConcreteCreator2.")
    cliente_code(ConcreteCreator2())
    print("\n")


        