import urllib.request
def test(k):
    url = f'https://www.google.com/recaptcha/api2/anchor?k={k}'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            if 'Invalid site key' in html:
                print(f'ERROR for {k}')
            else:
                print(f'SUCCESS for {k}!!!')
    except Exception as e:
        pass

test('6LfKp9MtAAAAADlEBlHphpcn7miDYH6UnOnu7rN')
test('6LfKp9MtAAAAADIEBlHphpcn7miDYH6UnOnu7rN')
test('6LfKp9MtAAAAAD1EBlHphpcn7miDYH6Un0nu7rN')
