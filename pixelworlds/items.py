
#    Copyright (C) 2020  Zenqi. All rights reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


from bs4 import BeautifulSoup
from .errors import InternalError
import requests
import json


class Items(object):
    def __init__(self, item: str=None):
        if item == None:
            print("Please specify item")
        self.item = item
        self.data = {}
        self.tokenize()
        self.baseurl = "https://pixelworlds.fandom.com/wiki/{}".format(self.item)
        self.scrape()
        


    def tokenize(self):
        _items = self.item.split(" ")
        _item_list = [item.capitalize() for item in _items]
        self.item = " ".join([str(strItem) for strItem in _item_list])

            
    def scrape(self):
        session = requests.Session()
        self.content = session.get(url=self.baseurl).text
        self.soup = BeautifulSoup(self.content, "html.parser")

    def get_title(self):
        try:
            title = self.soup.find("h1", {"class": "page-header__title"})
        except Exception:
            raise InternalError("%s not found. Try being specific in terms of items?" %(self.item))
        return title.text

    def get_image(self):
        images = self.soup.find_all("img", alt=True)    
        for image in images:
            if image["alt"] == f"{self.item}.png":
                image_src = image["src"]

        return image_src 

    def get_complexity_info(self):
        _complexity = self.soup.find("td", {"class": "complexityinfo"})        
        complexity = _complexity.text.split(": ")[1]
        return complexity


    def get_tier_info(self):
        _tier_info = self.soup.find("td", {"class": "tierinfo"})
        tier_info = _tier_info.text.split(": ")[1]
        return tier_info

    def get_description(self):
        description = self.soup.find("td", {"class": "descriptionbox"}) 
        return description.text

    def get_farmable_info(self):
        farmable = self.soup.find("td", {"class": "farmableinfo"})
        if farmable.text.split(" ")[1] == "Farmable":
            return True
        elif farmable.text.split(" ")[1] != "Farmable":
            return False

    def get_rarity_info(self):
        _rarity = self.soup.find("td", {"class": "rarityinfo"})
        rarity = _rarity.text.split(":  ")[1]
        return rarity

    def get_item_type(self):
        itemType = self.soup.find("td", {"class": "itemtypeinfo"})
        return itemType.text.split(":  ")[1]

    def get_growth_time(self):
        growthtime = self.soup.find("td", {"class": "growthtimeinfo"})
        return growthtime.text.split(": ")[1]


    def get_recipe(self):
        _ = self.soup.find("td", {"class": "crossbreedable"})
        __ = _.text
        if __ != "non-crossbreedable":
            return __.replace('\u200b', '')
        
        else:
            return None
        

    def get_data(self):
        self.data["name"] = self.item
        self.data["image"] = self.get_image()
        self.data["description"] = self.get_description()
        self.data["complexity"] = self.get_complexity_info() 
        self.data["tier"] = self.get_tier_info()
        self.data["rarity"] = self.get_rarity_info()
        self.data["itemType"] = self.get_item_type()
        self.data["isFarmable"] = self.get_farmable_info()
        self.data["growthTime"] = self.get_growth_time()
        self.data["recipe"] = self.get_recipe()


        
        return self.data

