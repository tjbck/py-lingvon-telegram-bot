import requests

word = 'cheval'

r = requests.get('https://www.dicts.info/examples.php?disa=1&lang2=french&word=' + word + '&go=Search')
print(r.content)