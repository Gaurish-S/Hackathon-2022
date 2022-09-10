import PySimpleGUI as sg
import os.path
# Column with all possible charts to be generated
list_column = [
    [sg.Text("Image Folder"),
     sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
     sg.FolderBrowse(),],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
]
# Column with data associated from list (generated image or chart from the left)
# Includes raw data values (number data)
data_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TEXT-")],
    [sg.Image(key="-IMAGE-")],
]

# Column containing data entries that can be added
input_column = [
    [sg.Text("User Manual Inputs")],
    [sg.Text("Enter pH Level:"), sg.InputText()],
    [sg.Text("Enter Waste Hardness:"), sg.InputText()],
    [sg.Text("Enter Solids:"), sg.InputText()],
    [sg.Text("Enter Chloramines:"), sg.InputText()],
    [sg.Text("Enter Sulfate:"), sg.InputText()],
    [sg.Text("Enter Conductivity:"), sg.InputText()],
    [sg.Text("Enter Organic Carbons:"), sg.InputText()],
    [sg.Text("Enter Trihalomethanes:"), sg.InputText()],
    [sg.Text("Enter Turbidity:"), sg.InputText()],
    [sg.Text("Enter Potability:"), sg.InputText()],
]

# 1. Ph Value
# 2. Hardness
# 3. Solids
# 4. Chloramines
# 5. Sulfate
# 6. Conductivity
# 7. Organic_carbon
# 8. Trihalomethanes
# 9. Turbidity
# 10. Potability


# scaling
def get_scaling():
    # called before window created
    root = sg.tk.Tk()
    scaling = root.winfo_fpixels('1i')/72
    root.destroy()
    return scaling

# Find the number in original screen when GUI designed.
my_scaling = 2      # call get_scaling()
my_width, my_height = 1920, 1080     # call sg.Window.get_screen_size()

# Get the number for new screen
scaling_old = get_scaling()
width, height = sg.Window.get_screen_size()

scaling = scaling_old * min(width / my_width, height / my_height)
sg.set_options(scaling=scaling)

# ----- Full layout -----
layout = [
    [sg.Column(list_column),
     sg.VSeperator(),
     sg.Column(data_column),
     sg.VSeperator(),
     sg.Column(input_column),]
]
window = sg.Window("Zui\'s Waste Quality Software", layout)
# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()