from abc import ABC, abstractmethod
import functools


class AbstractCompleteCalculator(ABC):

    @abstractmethod
    def _convert_string_args_to_float(self, *args):
        pass

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


class CompleteCalculator(AbstractCompleteCalculator):

    def _convert_string_args_to_float(self, args):
        return [float(arg) for arg in list(args)]
        
    def _check_is_digit(func):
        @functools.wraps(func)
        def wrapper(self, *args):
            args_list = list(args)
            for arg in args_list:
                try:
                    float_args = self._convert_string_args_to_float(args)
                    return func(self, *float_args)
                except ValueError:
                    return "Please provide valid integers."
        return wrapper
    
    @_check_is_digit
    def add(self, x: float, y: float) -> float:
        return x + y

    @_check_is_digit
    def subtract(self, x: float, y: float) -> float:
        return x - y
    
    @_check_is_digit
    def multiply(self, x: float, y: float) -> float:
        return x * y
    
    @_check_is_digit
    def divide(self, x: float, y: float) -> float:

        try:
            return x / y
        except ZeroDivisionError:
            return "Cannot divide by zero."
        
    @_check_is_digit
    def pow2(self, x: float) -> float:
        return x ** 2
