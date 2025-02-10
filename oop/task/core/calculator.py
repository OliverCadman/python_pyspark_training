from abc import ABC, abstractmethod
import functools


class AbstractCalculator(ABC):

    def _convert_string_args_to_float(self, args):
        return [float(arg) for arg in list(args)]

    def _check_is_digit(func):
        """
        Doc string for decorator.
        """
        @functools.wraps(func)
        def wrapper(self, *args):
            """
            Doc string for wrapper.
            """
            try:
                float_args = self._convert_string_args_to_float(args)
                return func(self, *float_args)
            except ValueError:
                return "Please provide valid integers."
        return wrapper
    
    @abstractmethod
    def add(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def subtract(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def multiply(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def divide(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def pow2(self, x: float) -> float:
        pass


class Calculator(AbstractCalculator):
    
    @AbstractCalculator._check_is_digit
    def add(self, x: float, y: float) -> float:
        """
        Doc string in the add method.
        """
        return x + y

    @AbstractCalculator._check_is_digit
    def subtract(self, x: float, y: float) -> float:
        return x - y
    
    @AbstractCalculator._check_is_digit
    def multiply(self, x: float, y: float) -> float:
        return x * y
    
    @AbstractCalculator._check_is_digit
    def divide(self, x: float, y: float) -> float:

        try:
            return x / y
        except ZeroDivisionError:
            return "Cannot divide by zero."
        
    @AbstractCalculator._check_is_digit
    def pow2(self, x: float) -> float:
        return x ** 2
