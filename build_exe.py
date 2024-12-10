import subprocess


def build_exe():
    """This function packs the project into a onefile.exe file."""
    subprocess.run([
        # Onefile mode
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--clean",
        "--noupx",
        "--log-level=DEBUG",
        
        # Adding project's folders
        "--add-data", "assets/*;assets",
        "--add-data", "config/*;config",
        "--add-data", "functions/*;functions",
        "--add-data", "src/*;src",
        "--add-data", "LICENSE;.",
        "--add-data", "README.md;.",

        # Adding specific files from "assets/example pictures"
        "--add-data", "assets/example pictures/Presentation - Pictures center ppt.jpg;assets/example pictures",
        "--add-data", "assets/example pictures/Presentation - pictures covering panoramic slides.jpg;assets/example pictures",
        "--add-data", "assets/example pictures/Presentation - pictures in panoramic slides.jpg;assets/example pictures",
        
        # Specify the hooks directory
        "--hidden-import", "pptx",
        "--hidden-import", "pptx.oxml",
        "--hidden-import", "pptx.oxml.nsmap",
        "--hidden-import", "pptx.enum",

        # Icon, name, and main script
        "--icon", "assets/icon.ico",
        "--name", "Pictures to slides.exe",

        # Main script
        "run.py"
    ])

    
    

if __name__ == "__main__":
    build_exe()
