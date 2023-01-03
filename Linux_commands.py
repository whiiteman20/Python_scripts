import requests

"""
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res)

print(res.status_code == requests.codes.ok)

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
"""
"""
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

split = image_url.split('/')

r = requests.get(image_url)

with open(split[-1], 'wb') as file:
    file.write(r.content)
"""

"""
file_url = 'https://learning.lpi.org/pdfstore/LPI-Learning-Material-030-100-en.pdf'

r = requests.get(file_url, stream=True)

with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
"""

file_url = 'https://www.kaggle.com/datasets/michaelbryantds/university-enrollments-dataset/download?datasetVersionNumber=3'

r = requests.get(file_url)

with open("python.csv", "wb") as csv:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            csv.write(chunk)
