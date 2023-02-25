import requests

API_KEY = "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"

def upload_file(file_name, purpose):
    url = "https://api.openai.com/v1/files"
    headers = {"Authorization":"Bearer "+API_KEY}
    data = {"purpose":purpose}
    input_file = "".join([el for el in open(file_name, encoding='utf-8')])
    files = {"file":input_file}
    res = requests.post(url, headers=headers, data=data, files=files).json()
    if not ('id' in res):
        return "Error: file not created"
    else:
        return res['id']
    
def file_list():
    url = "https://api.openai.com/v1/files"
    headers = {"Authorization":"Bearer "+API_KEY}
    res = requests.get(url, headers=headers)
    file_list = []
    for f in res.json()['data']:
        file_list.append(f['id'])
    return file_list

def delete_file(file_id):
    url = "https://api.openai.com/v1/files/"+file_id
    headers = {"Authorization":"Bearer "+API_KEY}
    res = requests.delete(url, headers=headers).json()
    return not ('error' in res)


print(upload_file("./training_set_generation/training_set.jsonl", "fine-tune"))
print(upload_file("./training_set_generation/validation_set.jsonl", "fine-tune"))