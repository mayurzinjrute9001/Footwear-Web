from django.shortcuts import render
from django.views import View
from z_footware_app.models.register import Register


class Register_user(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        temp = False
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        print(name,email,password,address,city,state,zip)

        try:
            register = Register(name=name, email=email, password=password, address=address, city=city, state=state,
                                zip=zip)
            temp=True
            register.save()
        except:
            pass


        return render(request, 'registration.html', {'temp': temp})
