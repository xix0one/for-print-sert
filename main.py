from bs4 import BeautifulSoup

names = []

# open txt file and save names in array
with open('names.txt', 'r', encoding='utf-8') as n:
    for i, line in enumerate(n):
        names.append(line)


# open and read html file
with open('index.html', 'r', encoding='utf-8') as html_file: 
    html_content = html_file.read()


# parse html file
soup = BeautifulSoup(html_content, 'html.parser') 
htmlNames = soup.find_all('span', class_='default')

count = 0

def add(count):
     with open(f'index_updated{count}.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

for n in range(len(names)):
    for html in htmlNames:
            if count < len(names):
                html.string = names[count]
                count += 1
            else:
                break
    add(count)

if len(names) % 2 != 0:
    print("*Последний файл имеет лишний сертификат*")

print("Успешно завершено")