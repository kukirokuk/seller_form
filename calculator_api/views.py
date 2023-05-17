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

    def calculate(self, operation, num1, num2):
        if operation in self.operations:
            return self.operations[operation](num1, num2)
        else:
            raise ValueError("Invalid operation")

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
        operation = request.data.get("operation")
        num1 = float(request.data.get("num1"))
        num2 = float(request.data.get("num2"))
        
        calculator = Calculator()
        try:
            result = calculator.calculate(operation, num1, num2)
            return Response({"result": result})
        except ValueError as e:
            return Response({"error": str(e)}, status=400)


def calculator_view(request):
    return render(request, 'calculator.html')