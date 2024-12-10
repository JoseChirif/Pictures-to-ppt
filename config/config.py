# Import functions
from functions.functions import relative_route_to_file

# Version
__version__ = '1.0.0'

# Common routes and variables
# icon_picture_ico
icon_picture_ico = relative_route_to_file("assets", file="icon.ico")

# icon_picture_png
icon_picture_png = relative_route_to_file("assets", file="icon.png")
  
# logo_github
logo_github_png = relative_route_to_file("assets", file="logo_github.png")

# Example picutres
pictures_center = relative_route_to_file("assets", "example pictures", file="Presentation - Pictures center ppt.jpg")
pictures_in_pan_slide = relative_route_to_file("assets", "example pictures", file="Presentation - pictures in panoramic slides.jpg")
pictures_covering_slide = relative_route_to_file("assets", "example pictures", file="Presentation - pictures covering panoramic slides.jpg")




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

        



