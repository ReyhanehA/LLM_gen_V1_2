#4.# Example 4: CWE-352 - Cross-Site Request Forgery (CSRF)

from django.shortcuts import render

def update_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # Vulnerable line: CSRF token not checked
        return render(request, 'profile.html', {'name': name, 'email': email})