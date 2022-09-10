import PySimpleGUI as sg

def get_scaling():
    # called before window created
    root = sg.tk.Tk()
    scaling = root.winfo_fpixels('1i')/72
    root.destroy()
    return scaling

# Column with all possible charts to be generated
list_column = [
    [sg.Text("Data:")],
]
# IDK YET
data_column = [
    [sg.Text("Image Folder"),
     sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
     sg.FolderBrowse(),],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
]

# Column containing data entries that can be added
inputSize = (20, 1)

input_column = [
    [sg.Text("User Manual Inputs", key='text', font=("Bookman Old Style", 25))],
    [sg.Text("Enter pH Level:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Waste Hardness:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Solids:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Chloramines:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Sulfate:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Conductivity:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Organic Carbons:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Trihalomethanes:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Turbidity:", size = inputSize), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Potability:", size = inputSize), sg.InputText(), sg.Button('Edit')],
]

# Scaling
# Find the number in original screen when GUI designed.
my_scaling = 2      # call get_scaling()
my_width, my_height = 1920, 1080     # call sg.Window.get_screen_size()

# Get the number for new screen
scaling_old = get_scaling()
width, height = sg.Window.get_screen_size()

scaling = scaling_old * min(width / my_width, height / my_height)
sg.set_options(scaling=scaling)

# Layout of main page
layout = [
    [sg.Column(list_column),
     sg.VSeperator(),
     sg.Column(data_column),
     sg.VSeperator(),
     sg.Column(input_column),]
]

# Window definition, with centering
window = sg.Window("Zui\'s Waste Quality Software", layout, element_justification='c').finalize()

# Button Definitions (can be changed)
pH = "Edit"
hardness = "Edit0"
solids = "Edit1"
chloramines = "Edit2"
sulfate = "Edit3"
conductivity = "Edit4"
carbons = "Edit5"
trihalomethanes = "Edit6"
turbidity = "Edit7"
potability = "Edit8"

# Actual event loop to run code
while True:
    # Different cases for button functions
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == pH:
        print("pH")
    elif event == hardness:
        print("hardness")
    elif event == solids:
        print("solids")
    elif event == chloramines:
        print("chloramines")
    elif event == sulfate:
        print("sulfate")
    elif event == conductivity:
        print("conductivity")
    elif event == carbons:
        print("carbons")
    elif event == trihalomethanes:
        print("trihalomethanes")
    elif event == turbidity:
        print("turbidity")
    elif event == potability:
        print("potability")

window.close()