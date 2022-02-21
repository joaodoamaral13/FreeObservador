from selenium import webdriver
from selenium.webdriver.chrome.options import Options  


def getArticle(url):

    options = Options()  
    options.add_argument("--headless")  

    driver = webdriver.Chrome(chrome_options = options)

    driver.get(url)
    
    try:
        divs = driver.find_elements_by_class_name("article-body-content")

    except:
        divs = []

    
    for div in divs:
        
        P = div.find_elements_by_xpath("*") #find_elements_by_tag_name('p')

        for p in P:

            if p.tag_name == 'p':
                text = p.get_attribute('innerText')

                print(text)
    

if __name__ == "__main__":
    #getArticle("https://web.archive.org/web/20170131230332/https://www.nga.gov/collection/an.shtm")
    getArticle("https://observador.pt/opiniao/o-isolamento-das-democracias/")
    