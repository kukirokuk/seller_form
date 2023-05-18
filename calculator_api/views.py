from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .managers import ParametersManager, CalculatorManager


class CalculatorAPIView(APIView):
    @csrf_exempt
    def post(self, request):
        params_manager = ParametersManager(request.data)
        params = params_manager.get_params()
        params = params_manager.sort_params(params)
        
        calculator = CalculatorManager()
        result = calculator.calculate(params)
        return result




def calculator_view(request):
    return render(request, 'calculator.html')