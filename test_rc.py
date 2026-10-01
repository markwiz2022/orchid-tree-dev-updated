import urllib.request
url = 'https://www.google.com/recaptcha/api2/anchor?k=6LfKp9MtAAAAADlEBlHphpcn7miDYH6Un0nu7rN'
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        if 'Invalid site key' in html:
            print('ERROR: Invalid site key found in HTML')
        else:
            print('SUCCESS: No invalid site key error found')
            if 'recaptcha-checkbox' in html:
                print('Checkbox found!')
except Exception as e:
    print('Exception:', e)
