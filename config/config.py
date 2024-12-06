# Import functions
from functions.functions import relative_route_to_file

# Version
__version__ = '1.0.0'

# Common routes and variables
# icon_picture_ico
icon_picture_ico = relative_route_to_file("assets", "icon.ico")

# icon_picture_png
icon_picture_png = relative_route_to_file("assets", "icon.png")
  
# logo_github
logo_github_png = relative_route_to_file("assets", "logo_github.png")



# Pictures extensions supported by ppt
pictures_extensions = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".svg",
    ".ico"
)

        



