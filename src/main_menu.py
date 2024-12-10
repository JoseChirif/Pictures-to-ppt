#Import libraries
import tkinter as tk
import sys
import os
import subprocess
from PIL import Image, ImageTk, ImageOps

# go to the parent directory if you are running this script directly (uncomment the following lines)
# import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.functions import run_picture_center, run_picture_in_panoramic_slide, run_picture_covering_panoramic_slide, open_web_page, adjust_text
from config.config import icon_picture_png, icon_picture_ico, logo_github_png, pictures_center, pictures_in_pan_slide, pictures_covering_slide, __version__

current_version = f'v{__version__}'

# Variables
project_title = "Pictures to Power Point"
text_button_1 = "Picture with border in the center of the slide"
picture_button_1 = pictures_center
text_button_2 = "Picture in panoramic slide"
picture_button_2 = pictures_in_pan_slide
text_button_3 = "Picture covering panoramic slice"
picture_button_3 = pictures_covering_slide
instructions_title = "Instructions:"
instructions_content = "1. Move the .exe file in the folder where are located. \n2. Execute the program. \n3. Choose your option."
notes_title = "Notes:"
notes_content = f"-The 1st option ({text_button_1}) centers the image to the slide with an heigh of 17.43 cm and add a 0.75pt black border to the image.\n- If you choose the 3rd option ({text_button_3}), the picture will be croped to get the slide aspect ratio."


# Styles
background = '#F0F0F0'
button_padding = 2
button_spacing = 10
button_border_width = 2
button_color_border = "black"
padding_text_button_x = 20  # Horizontal padding between text and button border
padding_text_button_y = 2  # Vertical padding between text and button border
window_size = "650x650"   # Custom window size (width x height)
margin = 30        # left margin to align texts
minimum_window_width = 300
link_color = "#0770E0"


    
    
def create_button_with_image(parent_frame, path_to_picture, text_button, command):
    """
    Creates a frame with an image on the left and a button on the right.

    Args:
        parent_frame (tk.Frame): The frame where the button with the image will be added.
        path_to_picture (str): Path to the image file.
        text_button (str): Text to display on the button.
        command (function): Function to execute when the button is clicked.
    """
    # Create the container frame
    frame_button = tk.Frame(parent_frame, bg=background)
    frame_button.pack(fill="x", pady=(button_padding, button_spacing), padx=margin + 10)
    
    # Load and process the image
    img = Image.open(path_to_picture)
    aspect_ratio = img.width / img.height
    new_height = 50  # Button height
    new_width = int(new_height * aspect_ratio)
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    img_bordered = ImageOps.expand(img_resized, border=1, fill="black")
    img_tk = ImageTk.PhotoImage(img_bordered)
    
    # Create the image label
    label_img = tk.Label(frame_button, image=img_tk, bg=background, cursor="hand2")
    label_img.image = img_tk  # Keep reference to prevent garbage collection
    label_img.pack(side="left")
    
    # Bind click event to the image
    label_img.bind("<Button-1>", lambda event: command())
    
    # Create the button
    btn_option = tk.Button(
        frame_button,
        text=text_button,
        font=("Arial", 10),
        command=command,
        borderwidth=button_border_width,
        highlightbackground=button_color_border,
        cursor="hand2",
    )
    btn_option.pack(side="left", expand=True, fill="both")
        
    return btn_option




    
# Function to create the main menu
def main_menu():
    """
    Displays the main menu for the project, allowing the user to navigate between different functionalities. 
    The function customizes the content and interface based on the provided language parameter.

    This function is located in src/main_menu.py

    Arg:
        language (str): The language code (e.g., 'en', 'es') passed to customize the language-specific content and labels on the menu.

    Returns:
        None: This function does not return any value. It opens the main menu interface and handles user interaction for navigation.
    """
    window = tk.Tk()
    window.title(project_title)
    
    # Set the minimum width
    window.wm_minsize(minimum_window_width, 0)
    
    # Set window size and background size
    window.geometry(window_size)
    window.configure(bg=background)

    # Make the window come to the foreground
    window.attributes("-topmost", True)
    window.after(1, lambda: window.attributes("-topmost", False))  # Return to normal state after opening
    
    # Add the icon to the window
    window.iconbitmap(icon_picture_ico)
    
    # Close the whole program when I close the menu
    window.protocol("WM_DELETE_WINDOW", lambda: (window.destroy(), sys.exit()))
    
    


    
    
    
    ## TITLE
    empty_space = tk.Frame(window, height=20)  # An empty frame
    empty_space.pack()
    # Create a frame for the project_title and the icon_picture_png image
    frame_project_title = tk.Frame(window, bg=background)
    frame_project_title.pack(pady=10, padx=margin, fill='x')

    # Load the icon_picture_png
    img = Image.open(icon_picture_png)
    img = img.resize((50, 50), Image.LANCZOS)  # Sets the icon size
    icon_picture_png_tk = ImageTk.PhotoImage(img)
    


    # Label for the icon_picture_png
    lbl_icon_picture_png = tk.Label(frame_project_title, image=icon_picture_png_tk, bg=background)
    lbl_icon_picture_png.image = icon_picture_png_tk  # Keep a reference to prevent deletion
    lbl_icon_picture_png.pack(side=tk.LEFT)

    # project_title
    lbl_project_title = tk.Label(frame_project_title, text=project_title, font=("Arial", 14, "bold"), bg=background)
    lbl_project_title.pack(fill='x', expand=True, padx=10)
    

    
    ## OPTIONS
    frame_options_and_notes = tk.Frame(window, bg=background)
    frame_options_and_notes.pack(expand=True, fill='both', pady=5)
    
    # Select an option text
    lbl_menu = tk.Label(frame_options_and_notes, text="Select an option:", font=("Arial", 10, "bold"), bg=background, anchor="w")
    lbl_menu.pack(expand=True, fill='both', pady=5, padx=margin, anchor="w")


    ## Buttons
    button_nr_1 = create_button_with_image(frame_options_and_notes, picture_button_1, text_button_1, run_picture_center)
    button_nr_2 = create_button_with_image(frame_options_and_notes, picture_button_2, text_button_2, run_picture_in_panoramic_slide)
    button_nr_3 = create_button_with_image(frame_options_and_notes, picture_button_3, text_button_3, run_picture_covering_panoramic_slide)
    
   
    

    # Instructions title text
    lbl_project_title_instructions_content = tk.Label(frame_options_and_notes, text=instructions_title, font=("Arial", 10, "bold"), bg=background, anchor="w")
    lbl_project_title_instructions_content.pack(expand=True, fill='both', pady=0, padx=margin, anchor="n")

    # instructions content
    lbl_instructions_content = tk.Label(frame_options_and_notes, text=instructions_content, font=("Arial", 10), justify="left", bg=background, anchor="n")
    lbl_instructions_content.pack(expand=True, fill='both', padx=margin)


    # Notes title text
    lbl_project_title_notes_content = tk.Label(frame_options_and_notes, text=notes_title, font=("Arial", 10, "bold"), bg=background, anchor="w")
    lbl_project_title_notes_content.pack(expand=True, fill='both', padx=margin, anchor="n")

    # notes content
    lbl_notes_content = tk.Label(frame_options_and_notes, text=notes_content, font=("Arial", 10), 
                                justify="left", bg=background, anchor="n")
    lbl_notes_content.pack(expand=True, fill='both', padx=margin, pady=(0, 0))





    ## REPOSITORY
    # Create a frame to align the icon_picture_png and the license
    frame_github = tk.Frame(window, bg=background)
    frame_github.place(relx=1.0, rely=0.0, anchor="se", x=-margin + 15, y=38)

    # Github text
    lbl_github_text = tk.Label(frame_github, text="GitHub", font=("Bell MT", 14), bg=background, fg=link_color, cursor="hand2") 
    lbl_github_text.pack(side=tk.LEFT, padx=(100, 0), pady=(5, 0))
    
    # Repository link (with the text)
    lbl_github_text.bind("<Button-1>", lambda e: open_web_page('https://github.com/JoseChirif/Pictures-to-slides','https://github.com/JoseChirif?tab=repositories', 'https://github.com/JoseChirif'))
    
    #PNG    
    # Load Github icon
    img_logo_github = Image.open(logo_github_png)
    img_logo_github = img_logo_github.resize((30, 30), Image.LANCZOS)
    icon_picture_png_Link_repositorio_tk = ImageTk.PhotoImage(img_logo_github)

    # Label for the icon_picture_png of Link_repository
    lbl_github_logo = tk.Label(frame_github, image=icon_picture_png_Link_repositorio_tk, bg=background, cursor="hand2")  # Hand cursor
    lbl_github_logo.image = icon_picture_png_Link_repositorio_tk  
    lbl_github_logo.pack(side=tk.LEFT, padx=(0, 10))  # Add padding on the right side

    # Repository link (with the icon)
    lbl_github_logo.bind("<Button-1>", lambda e: open_web_page('https://github.com/JoseChirif/Pictures-to-slides','https://github.com/JoseChirif?tab=repositories', 'https://github.com/JoseChirif'))
    
    



    ## LICENSE
    #frame_github = tk.Frame(window, bg=background)
    #frame_github.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-5)
    
    def get_license_route():
        """
        Returns the absolute path to the LICENSE.txt file located in the project's parent directory.

        This function is located in src/main_menu.py

        Returns:
            str: The absolute path to LICENSE.txt, allowing other parts of the application to access the license file regardless of the current working directory.
        """
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LICENSE'))
        
    def open_license():
        """
        Opens the LICENSE file in Notepad, regardless of its extension.
        """
        license_path = get_license_route()
        try:
            subprocess.run(["notepad", license_path], check=True)
        except FileNotFoundError:
            print("Notepad not found. Please ensure it is installed.")
        except Exception as e:
            print(f"An error occurred while trying to open the license file: {e}")


    # Show "MIT License" 
    lbl_license = tk.Label(window, text="MIT License", font=("Arial", 9), fg=link_color, cursor="hand2")    
    lbl_license.place(relx=1.0, rely=1.0, anchor="se", x=-margin, y=-5)
    # Llamar a open_license al hacer clic
    lbl_license.bind("<Button-1>", lambda e: open_license())


    ## Version
    lbl_version = tk.Label(window, text=current_version, font=("Arial", 9), fg="black")    
    lbl_version.place(relx=1.0, rely=1.0, anchor="se", x=-margin, y=-25)

 


    
    ## FINAL SETTINGS
    window.bind("<Configure>", lambda event: adjust_text(event, lbl_project_title, lbl_menu, lbl_project_title_instructions_content, button_nr_1, button_nr_2, button_nr_3,  lbl_instructions_content, lbl_project_title_notes_content, lbl_notes_content, margin=20))
    
    window.mainloop()





    
    
# Call main_menu
if __name__ == "__main__":
    main_menu()