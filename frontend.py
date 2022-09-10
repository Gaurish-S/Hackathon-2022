import PySimpleGUI as sg
from parsecsv import set_waste, show_waste

# Input window
input_size = (40, 1)

input_column = [
    [sg.Text("User Manual Inputs", font=("Helvetica", 30))],
    [sg.Text("Enter Average Temperature Value:", size=input_size), sg.InputText(key='temperature'), sg.Button('Edit')],
    [sg.Text("Enter Average pH Level:", size=input_size), sg.InputText(key='pH'), sg.Button('Edit')],
    [sg.Text("Enter Average Value of Dissolved Oxygen:", size=input_size), sg.InputText(key='oxygen'), sg.Button('Edit')],
    [sg.Text("Enter Average Conductivity Level:", size=input_size), sg.InputText(key='conductivity'), sg.Button('Edit')],
    [sg.Text("Enter Average Biochemical Oxygen Demand:", size=input_size), sg.InputText(key='biochemical'), sg.Button('Edit')],
    [sg.Text("Enter Average Value of Nitrate-n and Nitrite-n:", size=input_size), sg.InputText(key='nitrate_n'), sg.Button('Edit')],
    [sg.Text("Enter Average Fecal Coliform:", size=input_size), sg.InputText(key='coliform'), sg.Button('Edit')],
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
        set_waste("temp", values['temperature'])
        show_waste("temp")
    elif event == pH:
        set_waste("pH", values['pH'])
        show_waste("pH")
    elif event == oxygen:
        set_waste("DO", values['oxygen'])
        show_waste("DO")
    elif event == conductivity:
        set_waste("conductivity", values['conductivity'])
        show_waste("conductivity")
    elif event == biochemical:
        set_waste("BOD", values['biochemical'])
        show_waste("BOD")
    elif event == nitrate:
        set_waste("nitrate_n_nitrite", values['nitrate_n'])
        show_waste("nitrate_n_nitrite")
    elif event == coliform:
        set_waste("fecal_coliform", values['coliform'])
        show_waste("fecal_coliform")
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