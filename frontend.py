import PySimpleGUI as sg
import parsecsv


# Input window
input_size = (40, 1)

input_column = [
    [sg.Text("User Manual Inputs", font=("Helvetica", 30))],
    [sg.Text("Enter Average Temperature Value:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average pH Level:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average Value of Dissolved Oxygen:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average Conductivity Level:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average Biochemical Oxygen Demand:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average Value of Nitrate-n and Nitrite-n:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Text("Enter Average Fecal Coliform:", size=input_size), sg.InputText(), sg.Button('Edit')],
    [sg.Button('Submit')],
]

input_layout = [input_column]

input_window = sg.Window("Input Window", input_layout, element_justification='c')

temperature = 'Edit'
pH = 'Edit0'
oxygen = 'Edit1'
conductivity = 'Edit2'
biochemical = 'Edit3'
nitrate = 'Edit4'
coliform = 'Edit5'
submit = 'Submit'

# Run the Event Loop
while True:
    event, values = input_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        input_window.close()
        quit()
    elif event == temperature:
        print("temperature")
    elif event == pH:
        print("pH")
    elif event == oxygen:
        print("oxygen")
    elif event == conductivity:
        print("conductivity")
    elif event == biochemical:
        print("biochemical")
    elif event == nitrate:
        print("nitrate and nitrite")
    elif event == coliform:
        print("coliform")
    elif event == submit:
        print("submitted")
        break

input_window.close()


# Data Window
button_size = (30, 1)

data_column = [
    [sg.Text("River data informations", font=("Helvetica", 30))],
    [sg.Button("Sort by Average Temperature", size=button_size), 
     sg.Button("Sort by Average pH", size=button_size),
     sg.Button("Sort by Average Value of Dissolved Oxygen", size=button_size),
     sg.Button("Sort by Average Conductivity Level", size=button_size), 
     sg.Button("Sort by Average Biochemical Oxygen Demand", size=button_size), 
     sg.Button("Sort by Average Nitrate-n and Nitrite-n Values", size=button_size), 
     sg.Button("Sort by Average Fecal Coliform", size=button_size)]
]

data_layout = [data_column]


data_window = sg.Window("Zui\'s River Scouting Application", data_layout, element_justification='c')

while True:
    event, values = data_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

data_window.close()