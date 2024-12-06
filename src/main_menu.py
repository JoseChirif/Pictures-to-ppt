#Import libraries
import tkinter as tk
from tkinter import ttk
import sys
import os
import subprocess
from PIL import Image, ImageTk

# go to the parent directory if you are running this script directly (uncomment the following lines)
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.functions import run_picture_center, run_picture_in_panoramic_slide, run_picture_covering_panoramic_slide, open_web_page, adjust_text

# Import parameters from config
from config.config import icon_picture_png, icon_picture_ico, logo_github_png, __version__

current_version = f'v{__version__}'

# Variables
project_title = "Pictures to Power Point"
text_button_1 = "Picture with border in the center of the slide"
text_button_2 = "Picture in panoramic slide"
text_button_3 = "Picture covering panoramic slice"
instructions_title = "Instructions:"
instructions_content = "1. Move the .exe file in the folder where are located. \n2. Execute the program. \n3. Chose your option."
notes_title = "Notes:"
notes_content = f"-The 1st option ({text_button_1}) centers the image to the slide with an heigh of 17.43 cm and add a 0.75pt black border to the image.\n- If you chose the 3rd option ({text_button_3}), the picture will be croped to get the slide aspect ratio."


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
    global window, combo_languages # Make 'window' and combo_languages global
    global lbl_project_title, lbl_languages, lbl_menu, language_text, btn_option_1, btn_option_2, btn_option_3, lbl_project_title_notes_content, lbl_notes_content, lbl_instructions  # Make the widgets global to update them in select_language..
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

    # Button 1: Create Excel
    btn_option_1 = tk.Button(frame_options_and_notes, text=text_button_1, font=("Arial", 10), command=lambda: run_picture_center(),
                            borderwidth=button_border_width, highlightbackground=button_color_border,
                            padx=padding_text_button_x, pady=padding_text_button_y)
    btn_option_1.pack(expand=True, fill='both', padx=margin+10, pady=(button_padding, button_spacing))

    # Button 2: Modify names
    btn_option_2 = tk.Button(frame_options_and_notes, text=text_button_2, font=("Arial", 10),command=lambda: run_picture_in_panoramic_slide(),
                            borderwidth=button_border_width, highlightbackground=button_color_border,
                            padx=padding_text_button_x, pady=padding_text_button_y)
    btn_option_2.pack(expand=True, fill='both', padx=margin+10, pady=(button_padding, button_spacing))

    # Button 3: Unlock Excel sheet
    btn_option_3 = tk.Button(frame_options_and_notes, text=text_button_3, font=("Arial", 10),command=lambda: run_picture_covering_panoramic_slide(),
                            borderwidth=button_border_width, highlightbackground=button_color_border,
                            padx=padding_text_button_x, pady=padding_text_button_y)
    btn_option_3.pack(expand=True, fill='both', padx=margin+10, pady=(button_padding, button_spacing))


    # Instructions title text
    lbl_project_title_instructions_content = tk.Label(frame_options_and_notes, text=instructions_title, font=("Arial", 10, "bold"), bg=background, anchor="w")
    lbl_project_title_instructions_content.pack(expand=True, fill='both', pady=0, padx=margin, anchor="n")

    # instructions content
    lbl_instructions_content = tk.Label(frame_options_and_notes, text=instructions_content, font=("Arial", 10), 
                                justify="left", bg=background, anchor="n")
    lbl_instructions_content.pack(expand=True, fill='both', padx=margin, pady=0)


    # Notes title text
    lbl_project_title_notes_content = tk.Label(frame_options_and_notes, text=notes_title, font=("Arial", 10, "bold"), bg=background, anchor="w")
    lbl_project_title_notes_content.pack(expand=True, fill='both', pady=(0, 0), padx=margin, anchor="n")

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
    lbl_github_text.bind("<Button-1>", lambda e: open_web_page('https://github.com/JoseChirif/Pictures-to-ppt','https://github.com/JoseChirif?tab=repositories', 'https://github.com/JoseChirif'))
    
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
    lbl_github_logo.bind("<Button-1>", lambda e: open_web_page('https://github.com/JoseChirif/Pictures-to-ppt','https://github.com/JoseChirif?tab=repositories', 'https://github.com/JoseChirif'))
    
    



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
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LICENSE.txt'))
        
    def open_license():
        """
        Opens the LICENSE.txt file in the default text editor (Notepad on Windows) for viewing.

        This function is located in src/main_menu.py

        Args:
            None

        Returns:
            None: This function does not return any value. It opens the license file in a new Notepad window if the file exists at the specified path.
        """
        license_path = get_license_route()
        subprocess.Popen(['notepad.exe', license_path])


    # Show "MIT License" 
    lbl_license = tk.Label(window, text="MIT License", font=("Arial", 9), fg=link_color, cursor="hand2")    
    lbl_license.place(relx=1.0, rely=1.0, anchor="se", x=-margin, y=-5)
    # Llamar a open_license al hacer clic
    lbl_license.bind("<Button-1>", lambda e: open_license())


    ## Version
    lbl_version = tk.Label(window, text=current_version, font=("Arial", 9), fg="black")    
    lbl_version.place(relx=1.0, rely=1.0, anchor="se", x=-margin, y=-25)

 
    
    
    ## FINAL SETTINGS
    window.bind("<Configure>", lambda event: adjust_text(event, lbl_project_title, lbl_menu, btn_option_1, btn_option_2, btn_option_3, lbl_project_title_instructions_content, lbl_instructions_content, lbl_project_title_notes_content, lbl_notes_content, margin=20))
    
    window.mainloop()





    
    
# Call main_menu
if __name__ == "__main__":
    main_menu()
    
    
