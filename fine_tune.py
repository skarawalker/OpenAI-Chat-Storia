import requests
import json
import sys

API_KEY = "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"

url = "https://api.openai.com/v1/fine-tunes"
headers = {"Content-Type": "application/json", "Authorization":"Bearer "+API_KEY}
data = json.dumps({
    "training_file": "file-krPN4Al2LkcndSy6ezeFhyj6",
    "validation_file": "file-3ohulkKJp271xdi22r3mgOpd",
    "model": "davinci",
    "n_epochs": 10
})

if len(sys.argv)==1:
    exit('Comando non inserito')

command = sys.argv[1]
if command == 'train':
    res = requests.post(url, headers=headers, data=data)
    print(res.text)
elif command == 'status':
    res = requests.get(url+"/ft-hn3TjKgQhxsRrlC7uWiCr4QH", headers=headers)
    print(res.text)
else:
    print('Comando non riconosciuto')