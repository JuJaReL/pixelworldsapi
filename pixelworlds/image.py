#           Copyright (C) 2020  Zenqi. All rights reserved
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
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import io
from PIL import Image
import requests

class PixelWorldsImage:
    def __init__(self, image_url=None):
        self.url = image_url
        self.get_data_image()

    def get_data_image(self):
        self.content = requests.get(url=self.url).content
        data_image = Image.open(io.BytesIO(self.content))
        
        return data_image

    def download_image(self, name):
        self.get_data_image().save(name)
        

