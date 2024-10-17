from bs4 import BeautifulSoup


# open txt file
names = open('names.txt', 'r', encoding='utf-8') 


# open and read html file
with open('index.html', 'r', encoding='utf-8') as html_file: 
    html_content = html_file.read()


# parse html file
soup = BeautifulSoup(html_content, 'html.parser') 
htmlNames = soup.find_all('span', class_='default')


size = 2
count = 0


while (count != size):

    for i in range(count):
        for n in names:
            for html in htmlNames:
                html.string = n

    with open(f'print-it/index_updated{count}.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    count += 1

# close file
names.close()




# end



# for name in names:
#     print(name.get_text())

# for name in names:
#     name.string = "aaa"