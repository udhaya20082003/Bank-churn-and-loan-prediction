from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
Model = joblib.load('E:\Bank churn and prediction\APPLICATION-20241105T113142Z-001\APPLICATION\PROJECT\APP\CHURN.pkl')  
  
def Deploy_9(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        if output == 0:
            A = "THE CUSTOMER MIGHT NOT CHURN IN THIS CONDITIONS"
            B = "RETENTION : NO NEED RETENTION PROCEDURES."
            
        elif output == 1:
            A = "THE CUSTOMER MIGHT CHURN IN THIS CONDITIONS"
            B = "RETENTION : Enhance personalized customer experiences through data analysis and targeted offers.Implement proactive communication strategies to address customer concerns and needs.Develop loyalty programs and incentives to encourage continued patronage.Utilize predictive analytics to identify at-risk customers and intervene accordingly.Continuously improve services based on customer feedback and market trends to foster long-term satisfaction and loyalty."
        
        return render(request, '9_Deploy.html', {"prediction_text": A, "B":B})

    else:
        return render(request, '9_Deploy.html')
    
def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

Model2 = joblib.load('E:\Bank churn and prediction\APPLICATION-20241105T113142Z-001\APPLICATION\PROJECT\APP\LOAN.pkl')  
def Deploy_11(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model2.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        if output == 0:
            A = "THE LOAN AMOUNT MIGHT BE ATTAIN IN THIS CODITIONS."
            B = "HOW TO IMPROVE CREDEBILITY : NO NEED"
        elif output == 1:
            A = "THE LOAN AMOUNT MIGHT NOT BE ATTAIN IN THIS CODITIONS."
            B = "HOW TO IMPROVE CREDEBILITY : Implement rigorous identity verification protocols during account opening.Provide comprehensive financial education resources to promote responsible banking behavior.Offer personalized support and proactive communication to address customer concerns promptly.Utilize advanced fraud detection technology to safeguard accounts and transactions.Foster transparency through clear policies and disclosures regarding fees, terms, and account access."



        return render(request, '11_Deploy.html', {"prediction_text": A, "B":B})

    else:
        return render(request, '11_Deploy.html')

def Logout(request):
    logout(request)
    return redirect('Landing_1')
