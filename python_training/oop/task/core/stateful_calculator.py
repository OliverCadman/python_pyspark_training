from core.calculator import Calculator


class StatefulSymbolicCalculator(Calculator):

    def __init__(self):
        super().__init__() # Calculator.__init__()
        self.state = []

        self.method_map = {
            "+": self.add,
            "-": self.subtract,
            "x": self.multiply,
            "/": self.divide
        }
        
    def _split_input_string(self, input: str):
        split_input = input.split(" ")
        return split_input[0], split_input[1].lower(), split_input[2]
    
    def _map_operand_to_method(self, operand):
        return self.method_map.get(operand)
    
    def _input_string_to_method(self, input: str):
        split_string = self._split_input_string(input)
        return self._map_operand_to_method(split_string[1]), split_string[0], split_string[2]
    
    def calculate_from_input(self, input: str):
        method, first_val, second_val = self._input_string_to_method(input)
        
        result = method(first_val, second_val)
        self.state.append(result)
        return result
    
    def get_latest_calculation(self):
        if len(self.state) <= 0:
            return []
        return self.state[-1]
    
    def clear_state(self):
        self.state = []
