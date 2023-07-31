from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,View
from bt_app.forms import SignUpForm,SignInForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


class SignUpView(CreateView):
    model=User
    form_class=SignUpForm
    template_name='signup.html'
    success_url=reverse_lazy('login')


    def form_valid(self, form):
        messages.success(self.request,'Registration Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'Registration failed')
        return super().form_invalid(form)

class SignInView(FormView):
    template_name='signin.html'
    form_class=SignInForm
    
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,'You have been logged in successfully.')
                return redirect('index')
            messages.error(request,'Login failed. Please login again.')
            return render(request,self.template_name,{form:'form'})
            
        
class IndexView(View):
    template_name='index.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
    
def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,'You have been logged out successfully.')
    return redirect('login')




