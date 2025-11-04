from django.shortcuts import render,redirect

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

def survey(request):
    if request.method == "POST":
        Gender = request.POST.get("gender")
        Color = request.POST.get("favorite_color")
        Genre = request.POST.get("favorite_genre")
        request.session['survey_data'] = {
            'gender': Gender,
            'favorite_color': Color,
            'favorite_genre': Genre,
        }
        return redirect('thankyou')
    return render(request, "survey.html")


def thankyou(request):
    data = request.session.get('survey_data')
    if not data:
        return redirect('survey')
    return render(request, "thankyou.html", {'data': data})


def clear_session(request):
    if request.method == "POST":
        if 'survey_data' in request.session:
            del request.session['survey_data']
        return redirect('survey')
    return redirect('survey')
