<h1 align="center">
    Pixel Worlds API
</h1>
<p align="center">
    🌎 A python wrapper for pixel worlds' data
</p>
<p align="center">
    <a href="#">About</a> |
    <a href="#">Installation</a> |
    <a href="#">Usage</a> |
    <a href="#">Author</a> |
    <a href="#">License</a> |
</p>

## About

**Pixel Worlds API** is a *python* wrapper for Pixel Worlds' **data**. It was built to get **blocks** info, **recipes**, **wearables** and also **events**.

You can easily get information without storing thousands of pixel worlds data time to time. With just a single module, you can get everything you want.

---

## Installation

First of all you need to install [**python**](https://www.python.org/downloads/). Please choose version 3.x. Next step is download it via pip:

(copy this command and paste to your terminal)

```
$ pip install pixelworldsapi
```

---

## Usage

- Search for item information
  

```python
from pixelworlds import Item

item = Item("soil block")

# Item class functions:
#
# get_description() -> Get description
# get_complexity_info() -> Get complexxity info
# get_tier_info() -> Get tier info 
# get_rarity_info() -> Get rarity info
# get_item_type() -> Get item type 
# get_farmable_info() -> Get farmable info
# get_growth_time() -> Get growth time
# get_data() -> Get all data in a dict for


print(item.get_data()) # Get all data in a json format

# Output:
#
# {
#    "name": "Soil Block",
#    "description": "This is what natural ground is made of. Most common block of them all.",    
#    "complexity": "1",
#    "tier": "1",
#    "rarity": "Common",
#    "itemType": "Blocks",
#    "farmable": "Farmable",
#    "growthTime": "31s",
# }

print(item.get_description()) # Get description info
# Output:
# This is what natural ground is made of. Most common block of them all.



```

---

- Search for recipes
  

```python
# On going
```

---

- Search for events
  

---

## Author

**Pixel Worlds API Author/s**

| ![](https://github.com/zenqii.png?size=50) |
| --- |
| [Zenqi](https://github.com/zenqii) |

---

## License

**Pixel worlds API** is under [GNU Affero General Public License](https://github.com/zenqii/pixelworldsapi/blob/main/LICENSE).
