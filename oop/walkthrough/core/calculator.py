from abc import ABC, abstractmethod



class AbstractCalculator(ABC):


    @abstractmethod
    def add(self, x: float, y: float) -> float:
        pass

class Calculator(AbstractCalculator):

    def add(self, x: float, y: float) -> float:
        return x + y
    
    # Subtract

    # Multiply

    # Divide

    # Pow2


