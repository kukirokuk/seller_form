from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def calculate(self, operations):
        numbers = [float(operations[0])]
        result = numbers[0]

        for i in range(1, len(operations), 2):
            operation = operations[i]
            number = float(operations[i + 1])

            if operation in self.operations:
                operation_fn = self.operations[operation]
                result = operation_fn(result, number)
                numbers.append(number)
            else:
                raise ValueError("Invalid operation")

        return result

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")


class CalculatorAPIView(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            operations = [i for i in request.data.items() if i[0].split('_')[0] == 'pos' and int(i[0].split('_')[1])]
        except:
            return Response({"error": "Invalid input"}, status=400)
        if len(operations) < 3:
            print(111, list(request.data.items()))
            return Response({"error": "At least two numbers and one operator must be in input"}, status=400)
        
        sorted_operations = sorted(operations, key=lambda x: x[0])
        operations = [i[1] for i in sorted_operations]
        calculator = Calculator()
        try:
            result = calculator.calculate(operations)
            return Response({"result": result})
        except (ValueError, ZeroDivisionError) as e:
            return Response({"error": str(e)}, status=400)



def calculator_view(request):
    return render(request, 'calculator.html')