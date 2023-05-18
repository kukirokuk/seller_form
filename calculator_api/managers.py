from rest_framework.response import Response


class CalculatorManager:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def calculate(self, parameters):
        numbers = [float(parameters[0])]
        result = numbers[0]

        for i in range(1, len(parameters), 2):
            param = parameters[i]
            number = float(parameters[i + 1])

            if param in self.operations:
                operation_fn = self.operations[param]
                try:
                    result = operation_fn(result, number)
                    numbers.append(number)
                    return Response({"result": result})
                except (ValueError, ZeroDivisionError) as e:
                    return Response({"error": str(e)}, status=400)
            else:
                raise Response({"error": "Invalid operation"}, status=400)

        return result

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


class ParametersManager:
    def __init__(self, params) -> None:
        self.params = params
    
    def get_params(self):
        try:
            params = [i for i in self.params.items() if i[0].split('_')[0] == 'pos' and int(i[0].split('_')[1])]
            if len(params) < 3:
                return Response({"error": "At least two numbers and one operator must be in input"}, status=400)
            return params
        except:
            return Response({"error": "Invalid input"}, status=400)  
              
    def sort_params(self, params):
        sorted_params = sorted(params, key=lambda x: x[0])
        return [i[1] for i in sorted_params]