import urllib.request
url = 'https://www.google.com/recaptcha/api2/anchor?k=6LfKp9MtAAAAADIEBlHphpcn7miDYH6Un0nu7rN'
try:
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        if 'Invalid site key' in html:
            print('ERROR: Invalid site key found in HTML for I')
        else:
            print('SUCCESS: Valid key for I!')
except Exception as e:
    pass

url2 = 'https://www.google.com/recaptcha/api2/anchor?k=6LfKp9MtAAAAADlEB1Hphpcn7miDYH6Un0nu7rN'
try:
    with urllib.request.urlopen(url2) as response:
        html = response.read().decode('utf-8')
        if 'Invalid site key' in html:
            print('ERROR: Invalid site key found in HTML for 1')
        else:
            print('SUCCESS: Valid key for 1!')
except Exception as e:
    pass

