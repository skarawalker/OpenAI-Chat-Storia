import pandas
import random
df = pandas.read_csv('eventi_storici.csv', dtype={'ANNO':'Int64'})

set_domande = []

for i in range(1700, 2023):
    eventi_in_i = list(df[df['ANNO']==i]['EVENTO'])
    prompt = "Cosa è successo nel "+str(i)+"?"
    if len(eventi_in_i)!=0:
        completion = "Nel "+str(i)+" è successo questo: "+eventi_in_i[0]
        for e in range(1,len(eventi_in_i)):
            completion = completion+", "+eventi_in_i[e]
        set_domande.append("{\"prompt\":\""+prompt+"\",\"completion\":\""+completion+" STOPSTOP\"}\n")

for index, row in df.iterrows():
    prompt = "Quando è successo "+row['EVENTO']+"?"
    completion = row['EVENTO']+" è successo nel "+str(row['ANNO'])
    set_domande.append("{\"prompt\":\""+prompt+"\",\"completion\":\""+completion+" STOPSTOP\"}\n")

secoli = {
    "'700":[1700, 1799],
    "'800":[1800, 1899],
    "'900":[1900, 1999],
    "2000":[2000, 2023]
}
for i in secoli:
    eventi_in_i = list(df[(df['ANNO']>=secoli[i][0]) & (df['ANNO']<=secoli[i][1])]['EVENTO'])
    prompt = "Cosa è successo nel "+i+"?"
    if len(eventi_in_i)!=0:
        completion = "Nel "+str(i)+" è successo questo: "+eventi_in_i[0]
        for e in range(1,len(eventi_in_i)):
            completion = completion+", "+eventi_in_i[e]
        set_domande.append("{\"prompt\":\""+prompt+"\",\"completion\":\""+completion+" STOPSTOP\"}\n")

random.shuffle(set_domande)
validation = set_domande[0:int(len(set_domande)/10)]
training = set_domande[int(len(set_domande)/10):]

training_file = open('training_set.jsonl', 'w', encoding='utf-8')
validation_file = open('validation_set.jsonl', 'w', encoding='utf-8')

training_set = "".join([el for el in training])
validation_set = "".join([el for el in validation])

training_file.write(training_set)
validation_file.write(validation_set)

exit('Generation complete.')