from bs4 import BeautifulSoup
import requests


def get_vw() :
    html_text = requests.get("https://www.autoscout24.com/lst/volkswagen?atype=C&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&damaged_listing=exclude&desc=0&powertype=kw&search_id=1du5phrwvbd&sort=standard&source=homepage_search-mask&ustate=N%2CU").text
    soup = BeautifulSoup (html_text , "lxml")

    bmw_pages = soup.find ("li" , class_ = "pagination-item--disabled pagination-item--page-indicator").text.split(" ")
    pages = (int(bmw_pages[-1]))
    for i in range (1, int(pages)) :
        i = str(i)
        html_text1 = requests.get ("https://www.autoscout24.com/lst/volkswagen?atype=C&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&damaged_listing=exclude&desc=0&page="+ i +"&powertype=kw&search_id=1du5phrwvbd&sort=standard&source=listpage_pagination&ustate=N%2CU").text
        soup1 = BeautifulSoup (html_text1 , "lxml")
        bmws = soup1.find_all ("article" , class_= "cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__qyYw7")
        for bmw in bmws :
            bmw_name = bmw.find ("a" , class_= "ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I").text
            bmw_price = bmw.find ("p" , class_= "Price_price__APlgs PriceAndSeals_current_price__ykUpx").text.replace(".-" , "")
            bmw_img_src = bmw.find ("a" , class_="ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I")
            bmw_img_src1 = "https://www.autoscout24.com" + (bmw_img_src["href"])
            bmw_specs = bmw.find ("div" , class_="ListItem_listing__g3sc6")
            bmw_specs = str(bmw_specs).split(">")
            for i in range (len(bmw_specs)) :
                if "hp" in bmw_specs[i] :
                    horse_power = str(bmw_specs[i]).replace("</span" , "")
                elif "km" in bmw_specs[i] : 
                    mileage = str(bmw_specs[i]).replace("</span" , "")
                elif "20" in bmw_specs[i] :
                    date = str(bmw_specs[i]).replace("</span" , "")
                elif "19" in bmw_specs[i] :
                    date = str(bmw_specs[i]).replace("</span" , "")
            bmw_link = bmw.find("a" , class_= "ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I")
            bmw_link1 = "https://www.autoscout24.com" + (bmw_link["href"])
            bmw_link2 = bmw_link1.split("-")
            tracking_number = bmw_link2[-1]

            with open(f"F:\_net_scraping(autoscout)\\volks_wagen\\volks_wagen_{tracking_number}.txt", "w") as f :
                f.write(f"tracking no : {tracking_number} \n volks wagen name : \n {bmw_name} \n price of the volks wagen :\n {bmw_price} \n volks wagen advertisement : \n {bmw_link1} \n volks wagen image : \n {bmw_img_src1} \n volks wagen basic data : \n horse power : {horse_power} \n mileage : {mileage} \n date : {date} \n -------------------------------------------------------")


            print(f"volks wagen succesfully scraped !")
            print (f"\n ---------------------------------- \n")
get_vw()
