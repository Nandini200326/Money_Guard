from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    
    # Ensure the profile exists
    if not profile:
        profile = Profile.objects.create(user=request.user, income=0.0, balance=0.0, expenses=0.0)
    
    expenses = Expense.objects.filter(user=request.user)
    
    if request.method == 'POST':
        text = request.POST.get('text')
        amount = float(request.POST.get('amount', 0))  # Convert amount to float
        expense_type = request.POST.get('expense_type')
        
        # Create and save the expense
        expense = Expense(name=text, amount=amount, expense_type=expense_type, user=request.user)
        expense.save()
        
        # Update the profile instance
        if expense_type.lower() == 'positive':
            profile.balance += amount
        elif expense_type.lower() == 'negative':
            profile.expenses += amount
            profile.balance -= amount
        
        # Save the updated profile
        profile.save()
        return redirect('/')
    
    context = {'profile': profile, 'expenses': expenses}
    return render(request, "home.html", context)