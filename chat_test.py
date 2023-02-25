import requests
import json

API_KEY = "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"

def call_completion(prompt):
    url = "https://api.openai.com/v1/completions"
    headers = {"Content-Type": "application/json", "Authorization":"Bearer "+API_KEY}
    data = json.dumps({
    "model": "davinci:ft-personal-2023-02-25-12-04-07",
    "prompt": prompt,
    "max_tokens": 200,
    "temperature": 0,
    "stop": "STOPSTOP"
    })

    res = requests.post(url, headers=headers, data=data).json()
    if 'error' in res:
        return "Errore: "+res['error']
    else:
        return res['choices'][0]['text']
    
while True:
    prompt = input('ME: ')
    print('AI: '+str(call_completion(prompt)))