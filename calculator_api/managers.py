from rest_framework.response import Response


class CalculatorManager:
    """_summary_
    """
    def __init__(self):
        self.operands = {
            "+": {"func": self.add, "priority": 2},
            "-": {"func": self.subtract, "priority": 2},
            "*": {"func": self.multiply, "priority": 1},
            "/": {"func": self.divide, "priority": 1},
        }

    def calculate(self, parameters):
        numbers = []
        operations = []

        for param in parameters:
            if param in self.operands:
                priority = self.operands[param]["priority"]
                while (
                    operations
                    and self.operands[operations[-1]]["priority"] <= priority
                ):
                    operation = operations.pop()
                    number2 = numbers.pop()
                    number1 = numbers.pop()
                    operation_fn = self.operands[operation]["func"]
                    try:
                        result = operation_fn(number1, number2)
                        numbers.append(result)
                    except (ValueError, ZeroDivisionError) as e:
                        return Response({"error": str(e)}, status=400)
                operations.append(param)
            else:
                try:
                    number = float(param)
                    numbers.append(number)
                except ValueError:
                    return Response({"error": "Invalid input"}, status=400)

        while operations:
            operation = operations.pop()
            number2 = numbers.pop()
            number1 = numbers.pop()
            operation_fn = self.operands[operation]["func"]
            try:
                result = operation_fn(number1, number2)
                numbers.append(result)
            except (ValueError, ZeroDivisionError) as e:
                return Response({"error": str(e)}, status=400)

        if len(numbers) == 1:
            return Response({"result": numbers[0]})
        else:
            return Response({"error": "Invalid input"}, status=400)

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


class ParametersManager:
    """_summary_
    """
    def __init__(self, params):
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