from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from .forms import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from werkzeug.utils import secure_filename
# from Marketing_tool.settings import BASE_DIR
URL = ""
countryId = 0
categoryId = 0
cityId = 0
stateId = 0
D = ''
details = ''
Details_list=''
def webapps(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
    # return HttpResponse("Hello world!")

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def Search(request):
    context={
        'category': Category.objects.all(),
        'country': Country.objects.all(),
        'state': State.objects.all(),
        'city': City.objects.all()}
    # print('CATEGORY::',context['category'])
    return render(request,'search.html',context)


def Submit(request):
    
    selected_country = request.POST['country'] 
    # print('selected country:',str(selected_country))
    selected_state = request.POST['state']
    # print('selected state:',str(selected_state))
    selected_city = request.POST['city']
    # print('selected city:',str(selected_city))
    selected_category = request.POST['selected_category']
    # print('search category:',str(selected_category))
    context={
        'category': Category.objects.all(),
        'country': Country.objects.all(),
        'state': State.objects.all(),
        'city': City.objects.all(),
        'url': Url.objects.all(),
        'details': Details.objects.all() }
    # print('CATEGORY::',context['category'])
    Search = request.POST['search']
    # print('search:',Search)
    place = City.objects.filter(id=selected_city).values('city_name')
    Place = place[0]['city_name']
    # print('selected city name :', Place)
    url = "https://www.google.com/maps/search/" + Search + Place
    # print('in submit',url)
    # driver = webdriver.Chrome(executable_path="C:\\Users\Dell\Downloads\chromedriver_win32\\chromedriver.exe")#OldChromedriver
    driver = webdriver.Chrome(executable_path="C:\\Webdrivers\\chromedriver.exe")
    driver.implicitly_wait(300)
    driver.maximize_window()
    try:
        driver.set_page_load_timeout(300)
        driver.get(url)
                           
        class_name = "HlvSq"
        # Set initial scroll height and current scroll height
        scroll_height = 0
        last_scroll_height = driver.execute_script("return document.body.scrollHeight;")

        # Loop until element is not found
        while True:
            # Scroll down the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # print('In while loop')
            try:
                # Wait for the page to load
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(@class, '{class_name}')]")))
            except TimeoutException:
                # If element is not found, break out of loop
                print(f"Element {class_name} not found!")
                break
            # Get new scroll height
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            # If scroll height hasn't changed, break out of loop
            if scroll_height == last_scroll_height:
                print(f"Element {class_name} not found!")
                break
            # Set last scroll height to new scroll height
            last_scroll_height = scroll_height
        
        k=[]
        lnks=driver.find_elements(By.CLASS_NAME, "hfpxzc") 
        # print('kk',lnks)
        for lnk in lnks:
        # get_attribute() to get all href
            value = lnk.get_attribute('href')
            # print('valuee:',value)

        #[str(value)] is append on k list so data directly stored on list.
            k.append(str(value))
        # print('Print k:',k)

        for i in range(0, len(k)):
            # for c in range(0, len(cat)):str(selected_state)
                url = Url(country_id= int(selected_country), state_id = int(selected_state), city_id= int(selected_city), category_id = int(selected_category), url= k[i] )   
                if not Url.objects.filter(url = k[i]).exists():
                    url.save()
                    # print('i:', i) 
                else:
                    # print('Already Exists!!',i)
                    pass     
                # i=i+1
    except TimeoutException as ex:
        # isrunning= 0
        print("Exception Has Been Thrown" + str(ex))
        
        driver.close()
    
    return render(request, 'url_list2.html', context)
    # template = loader.get_template('url_list2.html')
    # return HttpResponse(template.render())
     
def Urls(request):
    global URL, countryId, categoryId, cityId, stateId
    # print('global country:', countryId)
    # print('global state:', stateId)
    # print('global city:', cityId)
    # print('global category:', categoryId)
    
    context={
        'category': Category.objects.all(),
        'country': Country.objects.all(),
        'state': State.objects.all(),
        'city': City.objects.all(),
        'url': Url.objects.all(),
        'details': Details.objects.all().order_by('id')}
    data1 = request.GET.get('country_id')
    data2 = request.GET.get('state_id')
    data3 = request.GET.get('city_id')
    data4 = request.GET.get('category_id')
    # countryId = data1
    # stateId = data2
    # cityId = data3
    # categoryId = data4
    
        # data = request.GET.get('data')
        # print('DATA:', str(data))s
        # countryId = request.POST['country']
        # selected_state = request.POST['state']
        # selected_city = request.POST['city']
        # selected_category = request.POST['selection']

        # if selected_country == 'select' and selected_state == 'select' and selected_city == 'select' and selected_category != None:
        #     print('category:', selected_category )
        #     urls = Url.objects.filter(category_id=str(selected_category)).all().order_by('id')
        #     # print(urls)
        #     context['url'] = urls
        # elif selected_country == 'select' and selected_state == 'select' and selected_city != None:
        #     print('city:', selected_city )
        #     urls = Url.objects.filter(city_id=str(selected_city)).all().order_by('id')
        #     # print(urls)
        #     context['url'] = urls
        # elif selected_country == 'select' and selected_state != None:
        #     print('state:', selected_state )
        #     urls = Url.objects.filter(state_id=str(selected_state)).all().order_by('id')
        #     # print(urls)
        #     context['url'] = urls
    
    
    if data1 is not None :
        countryId = data1
    if data2 is not None:
        stateId = data2
    if data3 is not None:
        cityId = data3
    if data4 is not None:
        categoryId = data4
    # print('city id:', cityId)
    # print('state id:', stateId)
    # print('country id:', countryId)

    # if cityId !=None:
    #     print('in city is not none')
    #     print('city:', cityId)
    #     if categoryId != None:
    #         # print('styate:', cityId)
    #         print('city is not none & category is::', categoryId )
    #         urls = Url.objects.filter(city_id=str(cityId),category_id=str(categoryId)).all().order_by('id')
    #         context['url'] = urls
    #         URL =list(urls.values())
    #     else:
    #         urls = Url.objects.filter(city_id=str(cityId)).all().order_by('id')
    #         context['url'] = urls
    #         URL =list(urls.values())
    # if stateId !=None:
    #     print('in state is not none')
    #     print('state:', stateId)
    #     if cityId != None:
    #         # print('styate:', stateId)
    #         print('state is not none & city is::', cityId )
    #         urls = Url.objects.filter(state_id=str(stateId),city_id=str(cityId)).all().order_by('id')
    #         context['url'] = urls
    #         URL =list(urls.values())
    #     elif categoryId != None:
    #         # print('styate:', stateId)
    #         print('state is not none & category is::', categoryId )
    #         urls = Url.objects.filter(state_id=str(stateId),category_id=str(categoryId)).all().order_by('id')
    #         context['url'] = urls
    #         URL =list(urls.values())
    #     else:
    #         urls = Url.objects.filter(state_id=str(stateId)).all().order_by('id')
    #         context['url'] = urls
    #         URL =list(urls.values())
    
    if countryId != None:
        if data2 != None:
                stateId= data2
                # print('country is not none & state:', stateId )
                urls = Url.objects.filter(country_id=str(countryId),state_id=str(stateId)).all().order_by('id')
                context['url'] = urls
                URL =list(urls.values())
        elif data3 != None:
                cityId= data3
                # print('country is not none & city is::', cityId )
                urls = Url.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId)).all().order_by('id')
                context['url'] = urls
                URL =list(urls.values())
        elif data4 != None:
                categoryId =data4
                # print('country is not none & category is::', categoryId )
                urls = Url.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId),category_id=str(categoryId)).all().order_by('id')
                context['url'] = urls
                URL =list(urls.values())
        else:
            # print('country:', countryId )
            urls = Url.objects.filter(country_id=str(countryId)).all().order_by('id')
            context['url'] = urls
            URL =list(urls.values())
    else:
        urls = Url.objects.all().order_by('id')
        URL =list(urls.values())
        context['url'] = urls
    return render(request, 'url_list2.html', context)

def Process(request):
    import googlemaps
    import psycopg2
    import datetime
    from datetime import date, datetime
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    # import psycopg2
    import time
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    global URL
    context={
        'category': Category.objects.all(),
        'country': Country.objects.all(),
        'state': State.objects.all(),
        'city': City.objects.all(),
        'url': Url.objects.all(),
        'details': Details.objects.all() }
    
    # print('URL::', URL)
    DateTime= datetime.now()
    print("date time:",DateTime)
    # result = list(Url.objects.values())
    # print('RESULT:', result)
    # print('results of details id::',URL[0]['id'])
    # print('results of details url::',URL[0]['city_id'])

    # PLEASE CHECK FOR THE URL LIST IN THIS LOOPS 
    # if request.method =='POST':
        
    # logo = [ "https://www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png", 
    #                     "https://www.gstatic.com/images/icons/material/system_gm/1x/schedule_gm_blue_24dp.png", 
    #                     "https://www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png", 
    #                     "https://www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png", 
    #                     "https://maps.gstatic.com/mapfiles/maps_lite/images/2x/ic_plus_code.png", 
    #                     "https://maps.gstatic.com/consumer/images/icons/1x/send_to_mobile_alt_gm_blue_24dp.png", 
    #                     "https://www.gstatic.com/local/placeinfo/lgbtq_friendly_ic_24dp.png", 
    #                     "https://www.gstatic.com/local/placeinfo/women_led_updated_ic_24dp.png",
    #                     "https://fonts.gstatic.com/s/i/googlematerialicons/event/v14/gm_blue-24dp/1x/gm_event_gm_blue_24dp.png"]

    logo =             ["Copy address", 
                        "Copy open hours", 
                        "Open website", 
                        "Copy phone number", 
                        "Learn more about plus codes", 
                        "https://maps.gstatic.com/consumer/images/icons/1x/send_to_mobile_alt_gm_blue_24dp.png", 
                        "https://www.gstatic.com/local/placeinfo/lgbtq_friendly_ic_24dp.png", 
                        "https://www.gstatic.com/local/placeinfo/women_led_updated_ic_24dp.png",
                        "https://fonts.gstatic.com/s/i/googlematerialicons/event/v14/gm_blue-24dp/1x/gm_event_gm_blue_24dp.png"]
    
    for j in range(0,len(URL)):
                            # print( j , url[j])
                            # url = URL[j][5]
                            url = URL[j]['url']
                            country = URL[j]['country_id']
                            state = URL[j]['state_id']
                            city = URL[j]['city_id']
                            category = URL[j]['category_id']
                            # print('url of webApp',url)
                            # driver = webdriver.Chrome(executable_path="C:\\Users\BinTech\Downloads\chromedriver_win32 (1)\\chromedriver")
                            driver = webdriver.Chrome(executable_path="C:\\Webdrivers\\chromedriver.exe")
                            driver.implicitly_wait(1)
                            try:
                                driver.set_page_load_timeout(25)
                                driver.get(url)
                            
                                # print(j, url_)
                                # print(j)
                            # NAME TEST
                                try:
                                    name=driver.find_element(By.TAG_NAME, 'h1').text #name of url
                                    # print("Name:", name)
                                except NoSuchElementException:
                                    name=''
                            # ADDRESS TEST                                 //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button
                                try:                                       
                                        img=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button') #website of navkar institute
                                        A=img.get_attribute('data-tooltip')
                                        # print('Adress:', A)
                                        if logo[0]==A:
                                            Address=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[3]/button/div[1]/div[3]/div[1]').text #Address of Navkar Institute
                                            # print('adress:', Address)
                                        else:
                                            pass
                                            # print("There is not Address!!")
                                except NoSuchElementException:
                                        Address=''
                                        # print("ActionToRunInCaseNoSuchElementTrue") 
                                if Address=='':
                                    try:
                                            imga=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/button') #website of navkar institute
                                            A1=imga.get_attribute('data-tooltip')
                                            if logo[0]==A1:
                                                Address=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/button/div[1]/div[3]/div[1]').text #Address of Navkar Institute
                                                # print('adress:', Address)
                                                
                                            else:
                                                pass
                                                # print("There is not Address!!")      //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div[1]/div[3]/div[1]
                                    except NoSuchElementException:
                                            Address=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass        
                                if Address=='':
                                    try:
                                            imga=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button') #website of navkar institute
                                            A1=imga.get_attribute('data-tooltip')
                                            if logo[0]==A1:
                                                Address=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[3]/button/div[1]/div[3]/div[1]').text #Address of Navkar Institute
                                                # print('adress:', Address)
                                                
                                            else:
                                                pass
                                                # print("There is not Address!!")
                                    except NoSuchElementException:
                                            Address=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                # WEBSITE TEST                               //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/a
                                try:
                                        img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/a')
                                        W2=img_2.get_attribute('data-tooltip')
                                        if logo[2]==W2:
                                            web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/a') #website of navkar institute
                                            Website=web2.get_attribute('href')
                                            # print('website:', Website)

                                        else:
                                        #     print("Website:", ' ')
                                            Website=''
                                except NoSuchElementException:
                                        Website=''
                                        # print("ActionToRunInCaseNoSuchElementTrue")
                                if Website=='':
                                    try:
                                            img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/a')
                                            W2=img_2.get_attribute('data-tooltip')
                                            if logo[2]==W2:
                                                web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/a') #website of navkar institute
                                                Website=web2.get_attribute('href')
                                                # print("website:", Website)
                                            else:
                                            #     print("Website:", ' ')
                                                Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")    
                                else:
                                     pass        
                                if Website=='':
                                    try:
                                            img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/a')
                                            W2=img_2.get_attribute('data-tooltip')
                                            if logo[2]==W2:
                                                web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/a') #website of navkar institute
                                                Website=web2.get_attribute('href')
                                                # print("website:", Website)
                                            else:
                                            #     print("Website:", ' ')
                                                Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")    
                                else:
                                     pass        
                                if Website=='':
                                    try:
                                            img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[5]/a')
                                            W2=img_2.get_attribute('data-tooltip')
                                            if logo[2]==W2:
                                                web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[5]/a') #website of navkar institute
                                                Website=web2.get_attribute('href')
                                                # print('website:', Website)

                                            else:
                                            #     print("Website:", ' ')
                                                Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")    
                                else:
                                     pass
                                if Website=='':
                                    try:
                                            img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[4]/a')
                                            W2=img_2.get_attribute('data-tooltip')
                                            if logo[2]==W2:
                                                web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[4]/a') #website of navkar institute
                                                Website=web2.get_attribute('href')
                                                # print('website:', Website)

                                            else:
                                            #     print("Website:", ' ')
                                                Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")    
                                else:
                                     pass
                                if Website=='':
                                    try:
                                            img_2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/a')
                                            W2=img_2.get_attribute('data-tooltip')
                                            if logo[2]==W2:
                                                web2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[3]/a') #website of navkar institute
                                                Website=web2.get_attribute('href')
                                                # print('website:', Website)

                                            else:
                                            #     print("Website:", ' ')
                                                Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")    
                                else:
                                     pass
                                if Website=='':
                                    try:
                                            
                                            img21=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/a')
                                            W1=img21.get_attribute('data-tooltip')
                                            
                                            if logo[2]==W1:
                                                web1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/a')
                                                Website=web1.get_attribute('href')
                                                # print('website:', Website)

                                            # else:
                                            # #     print("Website:", ' ')
                                            #     Website=''
                                    except NoSuchElementException:
                                            Website=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                try:
                                        img2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a') #website of navkar institute
                                        W=img2.get_attribute('data-tooltip')
                                            # print(E)
                                        if logo[2]==W:
                                            web=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/a') #website of navkar institute
                                            Website=web.get_attribute('href')
                                            # print('website:', Website)
                                            
                                        # else:
                                        #      #             print("Event:", ' ')
                                        #     Website=''
                                except NoSuchElementException: 
                                        pass
                                #        # print("Action To Run In Case No Such Element True")
                                if Website=='':
                                    try:
                                        imgf=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/a') #website of navkar institute
                                        W3=imgf.get_attribute('data-tooltip')
                                           
                                        if logo[2]==W3:
                                            web_3=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/a') #website of navkar institute
                                            Website=web_3.get_attribute('href')
                                            # print('website:', Website)

                                #         # else:
                                #         #     print("Website:", ' ')
                                    except NoSuchElementException:
                                        Website=''
                                #         # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                    pass
                                # PHONE TEST                                  //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[5]/button
                                try:                                          
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            # phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/div[2]/div/div[2]/a') #telephone no. of navkar institute
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[6]/div/div/div[2]/a') #xpath has been changed for phone no.
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            # print(Phone_No, '')
                                            Phone_No=''
                                except NoSuchElementException:
                                        Phone_No=''
                                        # print("ActionToRunInCaseNoSuchElementTrue") 
                                if Phone_No=='':
                                    try:
                                        # driver.implicitly_wait(5)           
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[8]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[8]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            # print(Phone_No, '')
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass        
                                if Phone_No=='':
                                    try:
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[7]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            # print(Phone_No, '')
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass        
                                if Phone_No=='':
                                    try:
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                if Phone_No=='':
                                    try:
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[6]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[6]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                if Phone_No=='':
                                    try:
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[5]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[5]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                if Phone_No=='':
                                    try:
                                        img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[4]/button')
                                        P1=img3_1.get_attribute('data-tooltip')
                                        # print(P1)
                                        if logo[3]==P1:
                                            phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[8]/div[4]/div/div/div[2]/a') #telephone no. of navkar institute
                                            Phone_No=phno1.get_attribute('href')
                                            # print('phone:', Phone_No)
                                        else:
                                            Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                if  Phone_No=='':       
                                    try:
                                            img3_1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[7]/button')
                                            P1=img3_1.get_attribute('data-tooltip')
                                            # print(P1)
                                            if logo[3]==P1:
                                                phno1=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[7]/div/div/div[2]/a') #telephone no. of navkar institute
                                                Phone_No=phno1.get_attribute('href')
                                                # print('phone:', Phone_No)
                                            else:
                                                # print(Phone_No, '')
                                                Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''
                                            # print("ActionToRunInCaseNoSuchElementTrue")
                                else:
                                     pass
                                if Phone_No=='':
                                    try:
                                            img3=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/button')
                                            P3=img3.get_attribute('data-tooltip')
                                            # print(P3)
                                            if logo[3]==P3:
                                                phno3=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/div/div/div[2]/a') #telephone no. of navkar institute
                                                Phone_No=phno3.get_attribute('href')
                                                # print('phone:', Phone_No)
                                            else:
                                                # print(Phone_No, '')
                                                Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''               
                                            # print("ActionToRunInCaseNoSuchElementTrue") 
                                else:
                                     pass 
                                if Phone_No=='':
                                    try:
                                            im=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/button')
                                            P2=im.get_attribute('data-tooltip')
                                            # print(P2)                                //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/div/div/div[2]/a
                                            #                                          //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[6]/div/div/div[2]/a
                                            if logo[3]==P2:
                                                phno2=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[5]/div/div/div[2]/a') #telephone no. of navkar institute
                                                Phone_No=phno2.get_attribute('href') 
                                                # print('phone:', Phone_No)
                                            else:
                                                # print(Phone_No, '')
                                                Phone_No=''
                                    except NoSuchElementException:
                                            Phone_No=''  
                                else:
                                    pass                         
                                        # print("ActionToRunInCaseNoSuchElementTrue")
                                if Phone_No=='':
                                    try:
                                            
                                            img_3=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/button')   
                                            P=img_3.get_attribute('data-tooltip')  
                                            # print(P)
                                            if logo[3]==P:
                                                phno=driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/div[2]/div/div[2]/a') #telephone no. of navkar institute
                                                Phone_No=phno.get_attribute('href')
                                                # print('phone:', Phone_No)
                                            else:
                                                Phone_No=''
                                    except NoSuchElementException:
                                            pass
                                else:
                                    pass
                                        # print("ActionToRunInCaseNoSuchElementTrue")
                                # print('before',str(Phone_No))
                                if "tel:0" in Phone_No:
                                    Phone_No1 = Phone_No.replace("tel:0", "").replace("%20","")
                                else:
                                    Phone_No1 = Phone_No.replace("tel:", "").replace("%20","")
                                # print('after:',Phone_No1)
                                if Address!='':
                                # for i in range(0, len(URL_1)):
                                # ADD=URL_1[i][1]
                                # print(ADD, "==address")
                                # Requires API key 
                                    gmaps = googlemaps.Client(key='AIzaSyBsqJFvJbRA0kP8tCezzr47UwkNWFWi6zM')

                                    distance = gmaps.distance_matrix(Address ,'401 Samedh Panchwati Cross Road, Chimanlal Girdharlal Rd, Ahmedabad, Gujarat 380009')['rows'][0]['elements'][0]
                                    if  'distance' in distance:
                                        d1=distance['distance']['text']
                                        # d2=distance['duration']['text']
                                    else:
                                        d1=''
                                    if  'duration' in distance:
                                        d2=distance['duration']['text']
                                        # d2=distance['duration']['text']
                                    else:
                                        d2=''

                                
                                # print(distance['distance']['duration'])
                                else:
                                    d1=''
                                    d2=''

                                response = Details.objects.filter(name = name).values()
                                # print('response details name:',response)
                                # print('LENGTH',len(response))
                                # print("selected::",response)
                                
                                Datetime=datetime.now()
                                # if  len(response) > 0 and name == NAME :
                                    # print('up')
                                if  len(response) > 0:
                                    for r in range(0, len(response)):
                                        # print('up')
                                        ID= response[r]['id']
                                        NAME =response[r]['name']
                                        ADDRESS = response[r]['address']
                                        WEBSITE = response[r]['website']
                                        PHONE = response[r]['phone_no']
                                        # print('details response:', ID, NAME, ADDRESS, WEBSITE, PHONE)
                                        if  name == NAME :
                                            # print('response name::',name)
                                            if Address != ADDRESS or Website != WEBSITE or Phone_No1 != PHONE :
                                                # cur.execute("UPDATE data_details SET Updated_at=%s  WHERE Name=%s AND id=%s ;", ( Datetime, NAME, ID)) #this runs and update the datetime when id and name of response is matches input name
                                                # print('unexpected address:', Address)
                                                # cur.execute("UPDATE data_details SET Address=%s, Website=%s, Phone_No=%s ,Updated_at=%s   WHERE Name=%s AND id=%s ;", (Address, Website , Phone_No1 , Datetime, NAME, ID))
                                                obj = Details(id = ID, name= name, address=Address,website=Website, phone_no=Phone_No1, category_id=category, country_id=country, state_id=state, city_id=city, updated_at= Datetime)
                                                # pass the object as instance in form
                                                
                                                # save the data from the form and
                                                # redirect to detail_view
                                                # if obj.method == 'POST':
                                                obj.save()
                                                # print('update')
                                else:
                                    print('down')
                                    details = Details(url= url, name= name, address=Address, distance=d1, time=d2, website=Website, phone_no=Phone_No1,category_id=category, country_id=country, state_id=state, city_id=city, created_at=DateTime)
                                    details.save()
                                    print('insert')
                                
                                
                                try:
                                        obj = get_object_or_404(Url, id= URL[j]['id'])
                                        if request.method =="POST":
                                            # delete object
                                            # print('delete url:', URL[j]['id'])
                                            obj.delete()
                                except NoSuchElementException:
                                    pass
                            except TimeoutException as ex:
                            # isrunning= 0s
                                print("Exception Has Been Thrown" + str(ex))
                            driver.close()
              
    return render(request, 'shop_details.html', context)

def Detail(request):
    context={
        'category': Category.objects.all(),
        'country': Country.objects.all(),
        'state': State.objects.all(),
        'city': City.objects.all(),
        'url': Url.objects.all(),
        'details': Details.objects.all().order_by('id'),
          }
    global countryId, categoryId, cityId, stateId
    # print('global country:', countryId)
    # print('global state:', stateId)
    # print('global city:', cityId)
    # print('global category:', categoryId)
    
    data1 = request.GET.get('country_id')
    data2 = request.GET.get('state_id')
    data3 = request.GET.get('city_id')
    data4 = request.GET.get('category_id')
    # print('data2', data2)
    if data1 is not None :
        countryId = data1
    if data2 is not None:
        stateId = data2
    if data3 is not None:
        cityId = data3
    if data4 is not None:
        categoryId = data4
    if countryId != None:
        if data2 != None:
            stateId= data2
            # print('country is not none & state:', stateId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId)).all().order_by('id')
            context['details'] = details
        elif data3 != None:
            cityId= data3
            # print('country is not none & city is::', cityId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId)).all().order_by('id')
            context['details'] = details
        elif data4 != None:
            categoryId =data4
            # print('country is not none & category is::', categoryId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId),category_id=str(categoryId)).all().order_by('id')
            context['details'] = details
        else:
            # print('country:', countryId )
            details = Details.objects.filter(country_id=str(countryId)).all().order_by('id')
            context['details'] = details
    else:
        details = Details.objects.all().order_by('id')
        context['details'] = details
    
    return render(request, 'shop_details.html', context)

# def selected(request):
#      if request.method =='POST':
#          selected_category = request.POST['selection']
#          print('selected category:', str(selected_category))
#          data = Details.objects.filter(category_id=str(selected_category)).values().order_by('id')
#          print(data)
#          return render(request, 'shop_details.html', {'details':data})
         
def phone_list(request):
    from whatsapp_api_client_python import API as API
    import requests
    import json
    context={
            'category': Category.objects.all(),
            'country': Country.objects.all(),
            'state': State.objects.all(),
            'city': City.objects.all(),
            'url': Url.objects.all(),
            'details': Details.objects.all().order_by('id'),
            'members': Member.objects.all().order_by('id') }
    global D, details,Details_list, countryId, categoryId, cityId, stateId
    # print('global country:', countryId)
    # print('global state:', stateId)
    # print('global city:', cityId)
    # print('global category:', categoryId)
    
    data1 = request.GET.get('country_id')
    data2 = request.GET.get('state_id')
    data3 = request.GET.get('city_id')
    data4 = request.GET.get('category_id')
    # print('data2', data2)
    if data1 is not None :
        countryId = data1
    if data2 is not None:
        stateId = data2
    if data3 is not None:
        cityId = data3
    if data4 is not None:
        categoryId = data4
    if countryId != None:
        if data2 != None:
            stateId= data2
            # print('country is not none & state:', stateId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId)).all().order_by('id')
            # context['details'] = details
        elif data3 != None:
            cityId= data3
            # print('country is not none & city is::', cityId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId)).all().order_by('id')
            # context['details'] = details
        elif data4 != None:
            categoryId =data4
            # print('country is not none & category is::', categoryId )
            details = Details.objects.filter(country_id=str(countryId),state_id=str(stateId),city_id=str(cityId),category_id=str(categoryId)).all().order_by('id')
            # context['details'] = details
        else:
            # print('country:', countryId )
            details = Details.objects.filter(country_id=str(countryId)).all().order_by('id')
            # context['details'] = details
    else:
        details = Details.objects.all().order_by('id')
        # context['details'] = details
    context['details'] = details
    D = details.filter(whatsapp = "Yes").order_by('id')
    # print("D for whatsapp filter", D)
    Details_list=list(details.values().order_by('id'))
    # print(Details_list)
    # print(':LIST FOR PHONE DETAILS', Details_list)
    return render(request, 'phone_list.html', context)

def checkphonenumber(request):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    context={
            'category': Category.objects.all(),
            'country': Country.objects.all(),
            'state': State.objects.all(),
            'city': City.objects.all(),
            'url': Url.objects.all(),
            'details': Details.objects.all().order_by('id'),
            'members': Member.objects.all().order_by('id') }
    global details,  Details_list
    # print('global detail', details)
    Details_list
    # print('List:', Details_list)
    M = Member.objects.all().values().order_by('id')
    # print('members',list(M))
    driver = webdriver.Chrome(executable_path="C:\\Users\BinTech\Downloads\chromedriver_win32 (1)\\chromedriver") 
    # mobile_number = "+916355618155"
    # ID = Details_list[1]['id']
    # print(ID)
    # Construct the URL to the user's chat window
    for p in range(0, len(Details_list)):
        I = Details_list[p]['id']
        phone_Number = Details_list[p]['phone_no']
        # print('id:',int(I), 'phone number:', phone_Number)
        # detail = Details.objects.order_by('id')[int(I)]
        detail = Details.objects.get(id=I)
        # print('detail', detail)
        if phone_Number !='':
            chat_url = f"https://web.whatsapp.com/send?phone={phone_Number}"
            driver.get(chat_url) # Wait for the chat window to load
            time.sleep(20) # Check if the chat window contains the message input field
            try: 
                message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']") 
                # print(f"The mobile number {phone_Number} is registered with WhatsApp.") 
                detail.whatsapp = "Yes"
                detail.save()
            except: 
                # print(f"The mobile number {phone_Number} is not registered with WhatsApp.") # Close the browser 
                detail.whatsapp = "No"
                detail.save()
        else:
            # print('Undefined!') 
            detail.whatsapp = "Undefined"
            detail.save()
        # d = Details.objects.filter(id=I).all()
        # print('dd:', d)
    member=list(M)
    for p in range(0, len(member)):
        I = member[p]['id']
        phone_Number = member[p]['phone']
        print('id:',int(I), 'phone number:', phone_Number)
        Members = Member.objects.all().order_by('id')[p]
        print('detail', Members)
        if phone_Number != None:
            chat_url = f"https://web.whatsapp.com/send?phone={phone_Number}"
            # Navigate to the chat window for the mobile number
            driver.get(chat_url) # Wait for the chat window to load
            time.sleep(20) # Check if the chat window contains the message input field
            try: 
                message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']") 
                print(f"The mobile number {phone_Number} is registered with WhatsApp.") 
                Members.whatsapp = "Yes"
                Members.save()
            except: 
                print(f"The mobile number {phone_Number} is not registered with WhatsApp.") # Close the browser 
                Members.whatsapp = "No"
                Members.save()
        else:
            print('Undefined!') 
            Members.whatsapp = "Undefined"
            Members.save()
    driver.quit()
    context['details']= details
    # D= details.filter(whatsapp="Yes").all()
    # print('d:', D)
    return render(request, 'phone_list.html', context)

def filter_whatsapp(request):
    # D
    context={
            'category': Category.objects.all(),
            'country': Country.objects.all(),
            'state': State.objects.all(),
            'city': City.objects.all(),
            'url': Url.objects.all(),
            'details': Details.objects.all().order_by('id'),
            'members': Member.objects.all().order_by('id') }
    # print("D for whatsapp filter", D)
    M= Member.objects.filter(whatsapp="Yes").all().order_by('id')
    # print("M for whatsapp filter", M)
    context['members'] = M
    context['details'] = D
    return render(request, 'phone_list.html', context)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def whatsApp(request):
    import pywhatkit
    import os
    import time
    from pynput.keyboard import Key, Controller
    import pyautogui
    import keyboard
    import requests
    from whatsapp_api_client_python import API as API
    import requests
    import json
    keyboard= Controller()
    import webbrowser
    # global details
    # print('Details::', details)
    url = "https://www.google.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open_new_tab(url)
    if request.method == 'POST':
        checked =  request.POST.getlist('mycheck')
        # print('checked:', checked)
        for check in range(0, len(checked)):
            # list = Details.objects.filter(id=checked[check]).values()
            # print('check list of phone', list)
            # Name=list[0]['name']
            # phoneNumber =list[0]['phone_no']
            # print(Name, phoneNumber, 'list of checked')
            List = Member.objects.filter(id=checked[check]).values()
            # print('List =', List)
            Name =List[0]['firstname']
            phoneNumber =List[0]['phone']
            # print('values:', Name, phoneNumber)
            phone_no= str("+91" + str(phoneNumber))
            # print('phone:' , phone_no)
            msg = request.POST['massage']
            Message_type = request.POST['type']
            # print('selected_type =', Message_type)
            if Message_type == "Personalized" :
                # print('IN PERSONALIZED!', Message_type)
                try:
                        # print('in')
                        # Message = 'Dear '+ Name + ','+'\n' + msg
                        message = 'Dear %Company Name%' + ','+'\n' + msg
                        text =str(message)
                        print(text)
                        Message = text.replace("%Company Name%", Name)

                        # print('massege::',Message)
                        form = ImageForm(request.POST, request.FILES)
                        try:
                            if request.FILES['img-file'] != '':
                                file = request.FILES['img-file']
                                # print('File ::',file)
                                if msg == "":
                                    # print('only image in general!')
                                    pywhatkit.sendwhats_image(
                                                                phone_no, 
                                                                file,  
                                                                tab_close=True)
                                elif  msg!= "" and file != "":
                                    # print('elif: both in general!')
                                    pywhatkit.sendwhats_image(
                                                                phone_no, 
                                                                file, Message, 
                                                                tab_close=True)
                        except:
                            if msg != "" :
                                # print('else: only msg in personalized')
                                pywhatkit.sendwhatmsg_instantly(
                                    phone_no, 
                                    Message, 
                                    tab_close=True        )
                        # print("Image sent successfully!")
                except Exception as e:
                                    print(str(e))
            else:
                text=str(msg)
                message= text.replace("%Company Name%", Name)
                # print('IN GENERALIZED!')
                # try:
                # print('generalized')
                form = ImageForm(request.POST, request.FILES)
                try:
                    if request.FILES['img-file'] != '':
                        file = request.FILES['img-file']
                        # print('File ::',file)
                        if msg == "":
                            # print('only image in general!')
                            pywhatkit.sendwhats_image(
                                                        phone_no, 
                                                        file,  
                                                        tab_close=True)
                            print('only image in general!')
                        elif  msg!= "" and file != "":
                            # print('elif: both in general!')
                            pywhatkit.sendwhats_image(
                                                        phone_no, 
                                                        file, message, 
                                                        tab_close=True)
                except:
                    if msg != "" :
                        # print('else: only msg in general')
                        # pywhatkit.sendwhatmsg_instantly(
                        #     phone_no, 
                        #     msg, 
                        #     tab_close=True        )
                        # pyautogui.click()
                        # time.sleep(20)
                        # pyautogui.click()
                        # time.sleep(10)
                        # keyboard.press(Key.enter)
                        # keyboard.release(Key.enter)
                        pywhatkit.sendwhatmsg(phone_no, message, time.localtime().tm_hour, time.localtime().tm_min+1, wait_time=10)
                # print("Image sent successfully!")
                # except Exception as e:
                #                     print(str(e))
            time.sleep(2) 
            
    #     time.sleep(1) 
    # time.sleep(1)
    # pyautogui.hotkey('ctrl', 'c')
    return render(request, 'whatsup.html')

def imageUpload(request):
 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        # print('valid:',form)
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})
 
def success(request):
    return HttpResponse('successfully uploaded')

def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        images = UploadImage.objects.all()
        return render(request, 'display_img.html', {'display_images': images})
    
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def countries(request):
    country=Country.objects.all().order_by('id')
    for i, c in enumerate(country):
        c.serial = i + 1
    context={
        'country': country }
    # print('COUNTRY::',context['country'])

    return render(request,'country.html',context)
    
def add_country(request):
    context = {}
    # print(request.POST)
    form = CountryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('country')
    context['form']= form
       
    return render(request , 'add_country.html', context)
    

def update_country(request,cid):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Country, id = cid)
    # pass the object as instance in form
    form = CountryForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('country')
    # add form dictionary to context
    context["form"] = form
    return render(request, "update_country.html", context)
   

def delete_country(request, cid ):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Country, id = cid)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('country')
    return render(request, "delete_country.html", context)

def states(request):
    state=State.objects.all().order_by('id')
    for i, s in enumerate(state):
        s.serial = i + 1
    context={
        'state': state, }
    # print('STATE::',context['state'])
    return render(request,'state.html',context)
    
def add_state(request):
    context = {}
    # print(request.POST)
    form = StateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('state')
    context['form']= form
    return render(request , 'state_add.html', context)
    
def update_state(request,sid):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(State, id = sid)
    # pass the object as instance in form
    form = StateForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('state')
    # add form dictionary to context
    context["form"] = form
    return render(request, "state_update.html", context)
    
def delete_state(request, sid ):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(State, id = sid)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('state')
    return render(request, "state_delete.html", context)


def cities(request):
    city=City.objects.all().order_by('id')
    for i, cy in enumerate(city):
        cy.serial = i + 1
    context={
        'city': city }  
    
    # print('CITY::',context['city'])
    
    return render(request,'city.html',context)
    
def add_city(request):
    context = {}
    # print(request.POST)
    form = CityForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('city')
    context['form']= form
       
    return render(request , 'city_add.html', context)

def update_city(request,cid):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(City, id = cid)
    # pass the object as instance in form
    form = CityForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('city')
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_city.html", context)

def delete_city(request, cid ):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(City, id = cid)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('city')
    return render(request, "delete_city.html", context)

def categories(request):
    category=Category.objects.all().order_by('id')
    for i , cat in enumerate(category):
        cat.serial = i+1
    context={
        'category': category }
    # print('CATEGORY::',context['category'])
    
    return render(request,'category.html',context)
  
def add_category(request):
    context = {}
    # print(request.POST)
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('category')
    context['form']= form
       
    return render(request , 'add_category.html', context)
    
def update_category(request, cid):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Category, id = cid)
    # pass the object as instance in form
    form = CategoryForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('category')
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_category.html", context)

def delete_category(request,  cid ):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Category, id = cid)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("/")
        return redirect('category')
    return render(request, "delete_category.html", context)
   
def about(request):
#     # return render_template('about.html')
#     # import pandas as pd
#     import openpyxl
#     import json
#     from datetime import date, datetime

# # Define variable to load the dataframe
#     df = openpyxl.load_workbook("C:\\Users\BinTech\marketing_automation\Marketing_tool\WebApp\static\distributor.xlsx")
    
#     # Define variable to read sheet
#     df1 = df.active
#     print(df1)
#     Company = []
#     for row in df1.iter_rows(min_row=2, values_only=True,max_row=57):
#         Company.append({
#             'country': 1,
#             'state': 1,
#             'city': 1,
#             'category':1,
#             'address': row[0],
#             'company_name': row[1],
#             'contact': row[3],
#             'website': row[5],
#             # Add more columns as needed
#         })
#     # json_data = json.dumps(Company)
#     # print('json data::', json_data[1][0])
#     print(Company)
#     # return HttpResponse(json_data, content_type='application/json')

#     for company in Company:
#         country=company['country']
#         state=company['state']
#         city=company['city']
#         category=company['category']
#         Address=company['address']
#         Name=company['company_name']
#         Phone_no=str(company['contact'])
#         Website=company['website']
#         DateTime= datetime.now()
#         # print("Phone_no:", Phone_no)
#         phone = Phone_no.replace(".0", "")
#         print("Name",Name,"Address",Address,"Phone_no:", phone,"Website",Website)
#         details = Details(url= '', name= Name, address=Address, distance='', time='', website=Website, phone_no=phone,category_id=category, country_id=country, state_id=state, city_id=city, created_at=DateTime)
#         details.save()
#         # print("company::",Company, "::::")
        
    
    template = loader.get_template('about.html')
    return HttpResponse(template.render())