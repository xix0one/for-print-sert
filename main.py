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
        print("Лист №:", iteration, "Добавлено: ", names[n], end="")   

    for n in range(len(names)):
        add(n)

    print()

# --------------------------------------------

def twoPages():

    # open and read html file
    with open('twoImages.html', 'r', encoding='utf-8') as html_file: 
        html_content = html_file.read()

    # parse html file
    soup = BeautifulSoup(html_content, 'html.parser') 
    htmlDefault = soup.find_all('span', class_='default')

    def add(n):
        global iteration

        if n == 0:
            for html in htmlDefault:
                html.string = names[n].rstrip()

                iteration += 1
                print("Лист №:", iteration, "Добавлено: ", names[n], end="")
            if len(names) > 1:
                br = soup.find('br')
            
                pName = soup.new_tag('p', attrs={'class': 'name'})  
                defaultSpan = soup.new_tag('span', attrs={'class': 'default'}) 
                defaultSpan.string = names[1].rstrip() 

                pName.append(defaultSpan)  
                br.insert_after(pName)

                print("Лист №:", iteration, "Добавлено: ", names[1], end="")
        else:
            space_div = soup.new_tag('div', attrs={'class': 'space'})
            new_div = soup.new_tag('div')
            br = soup.new_tag('br')

            p1 = soup.new_tag('p', attrs={'class': 'name'})
            spanDefault1 = soup.new_tag('span', attrs={'class': 'default'})
            spanDefault1.string = names[n].rstrip()
            p1.append(spanDefault1)
            new_div.append(p1)
            new_div.append(br)

            iteration += 1
            print("Лист №:", iteration, "Добавлено: ", names[n], end="")

            if n + 1 < len(names):
                p2 = soup.new_tag('p', attrs={'class': 'name'})
                spanDefault2 = soup.new_tag('span', attrs={'class': 'default'})
                spanDefault2.string = names[n + 1].rstrip()
                p2.append(spanDefault2)
                new_div.append(p2)

                print("Лист №:", iteration, "Добавлено: ", names[n+1], end="")
        
            soup.body.append(new_div)
            soup.body.append(space_div)

        with open(f'twoImages_updated.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))

    for n in range(0, len(names), 2):
        add(n)
        print()

print("\nСколько шаблонов на странице (1 или 2)?: ", end="")
choose = int(input())

onePage() if choose == 1 else twoPages()

print("\nВсего страниц:", iteration)
print("Успешно завершено")