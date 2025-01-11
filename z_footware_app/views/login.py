from django.shortcuts import render,redirect
from django.views import View
from z_footware_app.models.register import Register


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        temp = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user=Register.objects.get(email=email)
            if user:
                if password == user.password:
                    request.session['name']=user.name
                    request.session['id']=user.id
                    return redirect('home')
                else:
                    temp="Enter Correct Password"
            else:
                temp="Enter Correct Email"
        except:
            pass

        print(email,password)

        return render(request, 'login.html', {'temp': temp})
def logout(request):
    request.session.clear()
    return redirect('login')
