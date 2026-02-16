from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))


        print("num1 : " , num1)
        print("num2 : " , num2)
        
        operation = request.POST.get('operation')

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render(request, 'calculator/home.html', {'result': result})
