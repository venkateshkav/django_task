from django.shortcuts import render

def register_form(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Mail = request.POST.get("email")
        Age = request.POST.get("age")
        City = request.POST.get("city")
        request.session['user_name'] = Name
        request.session['user_mail'] = Mail
        request.session['user_age'] = int(Age)
        request.session['user_city'] = City
    return render(request,"index.html")
def show_details(request):
    User_name = request.session.get('user_name')
    User_mail = request.session.get('user_mail')
    User_age = request.session.get('user_age')
    User_city = request.session.get('user_city')
    return render(request,"summary.html",{'User_name':User_name,'User_mail':User_mail,'User_age':User_age,'User_city':User_city})