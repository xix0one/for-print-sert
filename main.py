from bs4 import BeautifulSoup

names = []

# open txt file and save names in array
with open('names.txt', 'r', encoding='utf-8') as n:
    for i, line in enumerate(n):
        names.append(line)

iteration = 0
count = 0

def onePage():

    address = []

    # add address from text.txt
    with open('title.txt', 'r', encoding='utf-8') as n:
        for i, line in enumerate(n):
            address.append(line)

    # open and read html file
    with open('oneImage.html', 'r', encoding='utf-8') as html_file: 
        html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'html.parser') 
    htmlNames = soup.find_all('span', class_='default')
    htmlAddress = soup.find_all('span', class_='address')
    htmlSpanText = str(soup.find('span', class_='text').string)
    htmlSpanManagerTitle = str(soup.find('span', class_='title').string)
    htmlSpanManagerNameSurname = str(soup.find('span', class_='surnameName').string)

    def add(n):
        global iteration

        if n == 0:
            for html in htmlNames:
                html.string = names[n]
            for ha in htmlAddress:
                ha.string = address[n]
        else:
            new_div = soup.new_tag('div')

            p = soup.new_tag('p', attrs={'class': 'name'})
            spanManager = soup.new_tag('span', attrs={'class': 'manager'})

            spanDefault = soup.new_tag('span', attrs={'class': 'default'})
            spanDefault.string = names[n].rstrip()

            spanAddress = soup.new_tag('span', attrs={'class': 'address'})
            spanAddress.string = address[n].rstrip()

            spanText = soup.new_tag('span', attrs={'class': 'text'})
            spanText.string = htmlSpanText

            managerTitle = soup.new_tag('span', attrs={'class': 'title'})
            managerTitle.string = htmlSpanManagerTitle

            managerNameSurname = soup.new_tag('span', attrs={'class': 'surnameName'})
            managerNameSurname.string = htmlSpanManagerNameSurname

            space_div = soup.new_tag('div', attrs={'class': 'space'})
            
            p.append(spanDefault)
            p.append(spanAddress)
            p.append(spanText)
            p.append(spanManager)
            spanManager.append(managerTitle)
            spanManager.append(managerNameSurname)
            new_div.append(p)
            soup.body.append(new_div)
            soup.body.append(space_div)

        with open(f'oneImage_updated.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))
        iteration += 1    

    for n in range(len(names)):
        add(n)


# --------------------------------------------

def twoPages():

    # open and read html file
    with open('twoImages.html', 'r', encoding='utf-8') as html_file: 
        html_content = html_file.read()


    # parse html file
    soup = BeautifulSoup(html_content, 'html.parser') 
    htmlNames = soup.find_all('span', class_='default')

    def add(count):
        global iteration
        new_names = names[count:count + 2]  # Get the next two names to add in each iteration
        if count < 2:
            index = 0
            for html in htmlNames:
                html.string = new_names[index]
                if len(names) > 1:
                    index += 1
        else:
            flag = True 

            new_div = soup.new_tag('div')
            br = soup.new_tag('br')

            for name in new_names:
                
                p1 = soup.new_tag('p', attrs={'class': 'name'})
                span1 = soup.new_tag('span', attrs={'class': 'default'})
                span1.string = name.rstrip()  # Add the name from the file
                p1.append(span1)
                
                new_div.append(p1)

                if flag:
                    new_div.append(br)
                    flag = False
                else:
                    flag = True
            
            soup.body.append(new_div)

            space_div = soup.new_tag('div', attrs={'class': 'space'})
            soup.body.append(space_div)

        with open(f'twoImages_updated.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))
            iteration += 1

        print("Лист №:", iteration, "Добавлено: ", new_names)

    for n in range(0, len(names), 2):
        global count
        add(count)
        if count < len(names):
            count += 2
        else:
            break

    if len(names) % 2 != 0:
        print("\nВсего добавлено: ", count - 1)
    else:
        print("\nВсего добавлено: ", count)



print("\nСколько листов на странице (1 или 2)?: ", end="")
choose = int(input())

if choose == 1:
    onePage()
elif choose == 2:
    twoPages()


print("Всего страниц:", iteration)
print("Успешно завершено")