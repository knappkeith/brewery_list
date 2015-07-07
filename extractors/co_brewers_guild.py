from selenium import webdriver

def pull_craft_brews():
    browser = webdriver.Firefox()

    browser.get("http://www.coloradocraftbrews.com/colorado-breweries/")

    table = browser.find_element_by_id("post-17")

    paras = table.find_elements_by_class_name("entry-content")

    breweries = paras[0].find_elements_by_tag_name("p")

    brew_array = []

    for i in breweries:
        brew_array.append({"org_str":i.text})

    browser.close()

    del brew_array[0]

    for i in brew_array:
        i['name'] = i['org_str'].split(":")[0].split(u"\u2013")[0].strip()
        i['city'] = i['org_str'].split(":")[0].split(u"\u2013")[1].strip()
        i['desc'] = " ".join(i['org_str'].split(":")[1:]).strip()

    return brew_array