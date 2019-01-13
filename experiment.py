


#This script is to take a list of ASIN numbers as input in the form of a text file
#and downloads all the reviews of each individual product with a unique ASIN and then saves the
#reviews of every product in a separate text file named in the format ASIN_number.txt in the present working directory


import requests
from bs4 import BeautifulSoup
from lxml import html
import random
import re

users = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0',
    'Mozilla/5.0 (X11; U; Windows NT 6; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.587.0 Safari/534.12',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14',
     'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0'
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
     'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
     'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5004; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5001; Windows NT 5.1; Trident/4.0)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5000; Windows NT 5.1; Trident/4.0; FunWebProducts)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.5000; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.27; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.27; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.2)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.17; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.168; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.168; Windows NT 5.1; Trident/4.0; GTB7.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.130; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.130; Windows NT 5.1; Trident/4.0; FunWebProducts; GTB6.6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; yie8)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 5.1; Trident/4.0; GTB6.3)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.124; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.122; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.122; Windows NT 5.1; Trident/4.0; FunWebProducts)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.111; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.110; Windows NT 5.1; Trident/4.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.104; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.6; AOLBuild 4340.128; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.5; AOLBuild 4337.43; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.5; AOLBuild 4337.29; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.21022; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.93; Windows NT 5.1; Trident/4.0; DigExt; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.89; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.81; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.81; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618) (Compatible; ; ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.81; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.80; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.53; Windows NT 6.0; FunWebProducts; GTB6; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.43; Windows NT 6.0; WOW64; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.43; Windows NT 5.1; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.43; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.42; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 6.0; FunWebProducts; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 5.1; Trident/4.0; GTB6; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.40; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.36; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.30618; .NET CLR 3.5.30729)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.36; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; .NET CLR 1.1.4322)',
     'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.36; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'
]


header = {'User-Agent': users[random.randint(0, len(users) - 1)]}
ASIN_list = []
with open('asin_test.txt','r') as fi:
    ASIN_list = fi.read().splitlines()

i = 0
counter = 0
for asin in ASIN_list:
    total_reviews = ""
    print("Working on the product wiith ASIN: ",ASIN_list[i])
    #url = "https://www.amazon.com/dp/" + ASIN_list[i]
    url = "https://www.amazon.com/dp/" + asin
    source_code = requests.get(url, headers=header)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")

    # Getting the link that says see all reviews
    all_reviews_link = soup.find('a',{'class': "a-link-emphasis a-text-bold", 'data-hook': "see-all-reviews-link-foot"})
    while all_reviews_link == None:
        source_code = requests.get(url, headers=header)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        all_reviews_link = soup.find('a',
                                     {'class': "a-link-emphasis a-text-bold", 'data-hook': "see-all-reviews-link-foot"})
    print("The all reviews link is: " , all_reviews_link)
    only_link = (all_reviews_link['href'])
    total_link = "https://www.amazon.com" + only_link + "&pageNumber="
    print(total_link)

    # For getting the total number of pages with reviews
    see_all_reviews_text = all_reviews_link.text
    list_after_splitting = see_all_reviews_text.split()[2]
    try:
        str_no_of_reviews = int(list_after_splitting)
    except:
        str_no_of_reviews = int(list_after_splitting.replace(',', ''))
    iterator= int(str_no_of_reviews/10)
    if (str_no_of_reviews%10) == 0:
        iterator = int(str_no_of_reviews/10)
    else:
        iterator += 1
    print("The product has ", iterator , "pages of reviews")


    page = 1
    fw = open(asin + '.txt', 'w+', encoding="utf-8")
    while page <= iterator:
        print("Now, working on page: ", page)
        review_link_with_pageno = total_link + str(page)
        header_1 = {'User-Agent': users[random.randint(0, len(users) - 1)]}
        source_code_1 = requests.get(review_link_with_pageno, headers=header_1)
        plain_code = source_code_1.text
        soup_1 = BeautifulSoup(plain_code, "lxml")
        reviews = soup_1.findAll('span', {'class': "a-size-base review-text", 'data-hook': "review-body"})
        # The type of reviews is <class 'bs4.element.ResultSet'>
        # Thus, converting it into string format below
        str_reviews = str(reviews)
        one_review_per_line = str_reviews.replace('[<span class="a-size-base review-text" data-hook="review-body">', '')
        one_review_per_line = str_reviews.replace('<span class="a-size-base review-text" data-hook="review-body">', '')
        one_review_per_line = one_review_per_line.replace('</span>,', '\n')
        one_review_per_line = one_review_per_line.replace('</span>]','')
        one_review_per_line = one_review_per_line.replace(one_review_per_line[0], ' ')
        if len(one_review_per_line) < 3 and one_review_per_line[1]=="]":
            print("the data could not be retrieved from the page: ", page)
            one_review_per_line = ""
        if one_review_per_line !="":
            total_reviews = total_reviews  + one_review_per_line + "\n"
        else:
            continue


        page += 1
        date = ""
        stars = 0
        helpful_votes = 0
        '''
        Collecting the following metadata from each customer review:
        1. Date of review
        2. Star rating
        3. Number of helpful votes on each review
        4. Percentage of upper case letters in each review
        5. Percentage of lower case letters in each review
        '''


        def percentages_upper_lower(line):
            no_upper_case_letters = 0
            no_lower_case_letters = 0
            total_no_letters = (len(line)-1)
            # total - 1 since every line has a \n at the end of the line
            for l in line[:-1]:
                if l.islower():
                    no_lower_case_letters += 1
                elif l.isupper():
                    no_upper_case_letters += 1
                elif l.isspace():
                    total_no_letters -= 1
                else:
                    pass
            upper_case_percentage = round(((no_upper_case_letters / total_no_letters) * 100))
            # print(f"Upper Case: {upper_case_percentage}")
            lower_case_percentage = round(((no_lower_case_letters / total_no_letters) * 100))
            # print(f"Lower Case: {lower_case_percentage}")
            return upper_case_percentage, lower_case_percentage


        with open(asin + 'metadata.csv', 'a') as fa:
            with open(asin + 'titles.txt', 'a', encoding="utf-8") as fs:
                for rev in soup_1.findAll('div', {'data-hook': "review", 'class': "a-section review"}):
                    just_one_review_out_of_10 = str(rev)
                    mini_soup = BeautifulSoup(just_one_review_out_of_10, "lxml")
                    # print(rev.prettify())
                    # print("\n\n\n")


                    # mini_content_for_xpath = html.fromstring(mini_soup.text)
                    # helpful_votes_xpath = '//span[@data-hook="helpful-vote-statement"]/text()'
                    # helpful_votes_using_xpath = mini_content_for_xpath.xpath(helpful_votes_xpath)
                    # print(helpful_votes_using_xpath)


                    date = mini_soup.find('span', {'data-hook': "review-date"}).string
                    rep = {"January": "01", "February": "02","March": "03","April": "04","May": "05","June": "06", "July": "07","August": "08", "September": "09","October": "10","November": "11","December": "12"}  # define desired replacements here

                    rep = dict((re.escape(k), v) for k, v in rep.items())
                    date_pattern = re.compile("|".join(rep.keys()))
                    date = date_pattern.sub(lambda m: rep[re.escape(m.group(0))], date)

                    date = date.replace('on ', '')
                    date = date.replace(', ', '/')
                    date = date.replace(' ', '/')

                    stars = str(mini_soup.find('span', {'class': "a-icon-alt"}).string[0])
                    helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement", 'class': "a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component"}))
                    # print(f" ==================================\n\n {mini_soup.prettify()}")


                    helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement",'class': "a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component"}))
                    try:
                        helpful_votes = helpful_votes.replace(
                            '<span class="a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component" data-hook="helpful-vote-statement">','')
                    except:
                        pass
                    if helpful_votes == 'None':
                        helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement",'class': "a-size-base a-color-tertiary cr-vote-text"}))
                        try:
                            helpful_votes = helpful_votes.replace(
                                '<span class="a-size-base a-color-tertiary cr-vote-text" data-hook="helpful-vote-statement">','')
                        except:
                            pass
                    if helpful_votes == 'None':
                        helpful_votes = '0'
                    if helpful_votes != '0':
                        helpful_votes = helpful_votes.replace(' found this helpful</span>', '')
                        if 'people' in helpful_votes:
                            helpful_votes = helpful_votes.replace(' people' , '')
                        elif 'One person' in helpful_votes:
                            helpful_votes = helpful_votes.replace('One person', '1')
                    if ',' in helpful_votes:
                        helpful_votes = helpful_votes.replace(',', '')
                    # print(helpful_votes)


                    fa.write(date + ',' + stars + ',' + helpful_votes  + "\n")
                for title in soup_1.findAll('a', {'data-hook': "review-title",
                                                  'class': "a-size-base a-link-normal review-title a-color-base a-text-bold"}):
                    total_review_titles = ''
                    title = str(title)
                    title = title[194:]
                    if title[0] == '>':
                        title = title[1:]
                    title = title.replace('</a>', '')
                    # print(f" Title Upper : {title_lower_percentage} \n Title Lower:{ title_upper_percentage}")
                    # print("====================================================")

                    total_review_titles = total_review_titles + title + '\n'
                    fs.write(total_review_titles)
    i += 1
    fw.write(total_reviews)
    fw.close()

    with open(asin +'titles.txt','r', encoding="utf-8") as title_read:
        with open(asin + 'titles_metadata.csv', 'w+') as title_write:
            for t_line in title_read.readlines():
                title_lower_percentage = 0
                title_upper_percentage = 0
                title_upper_percentage, title_lower_percentage = percentages_upper_lower(t_line)
                no_words_in_title = len(t_line.split())
                length_title = len(t_line)-1
                title_metadata = str(no_words_in_title) + ',' + str(length_title) + ',' + str(title_upper_percentage) + ',' + str(title_lower_percentage) +'\n'
                title_write.write(title_metadata)






