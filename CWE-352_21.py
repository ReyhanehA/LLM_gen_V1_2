#8.# Example 8: CWE-352 - Cross-Site Request Forgery (CSRF)

from django.shortcuts import render

def update_settings(request):
    if request.method == 'POST':
        setting = request.POST.get('setting')
        value = request.POST.get('value')
        # Vulnerable line: CSRF token not checked
        return render(request, 'settings.html', {'setting': setting, 'value': value})