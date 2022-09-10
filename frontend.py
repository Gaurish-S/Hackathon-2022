import PySimpleGUI as sg
from parsecsv import set_waste, show_waste

def make_input_window():
    input_size = (40, 1)
    layout = [
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
    return sg.Window('Input Window', layout, element_justification='c', modal=True)

temperature = 'Edit'
pH = 'Edit0'
oxygen = 'Edit1'
conductivity = 'Edit2'
biochemical = 'Edit3'
nitrate = 'Edit4'
coliform = 'Edit5'
submit = 'Submit'

def input_window_function():
    input_window = make_input_window()

    while True:
        event, values = input_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
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

# Input window
input_window_function()

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
     sg.Button("Sort by Average Fecal Coliform", size=button_size)],
     [sg.Button("Show Input Window")]
]



# Get data from backend, update table
def create_table():
    table_layout = [
        [
            sg.Table(
                headings=['River name:', 
                'Temperature', 
                'pH Level', 
                'Dissolved Oxygen:', 
                'Conductivity Level', 
                'Biochemical Oxygen Demand', 
                'Value of Nitrate-n and Nitrite-n', 
                'Fecal Coliform'],
                values=[['1', '2', '3', '4', '5', '6', '7', '8']],
                justification='center',
            )
        ]
    ]
    return table_layout


data_layout = [[data_column], [create_table()]]

data_window = sg.Window("Zui\'s River Scouting Application", data_layout, element_justification='c')

while True:
    event, values = data_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Show Input Window":
        input_window_function()
    elif event == "Sort by Average Temperature":
        print("change to temp")
    elif event == "Sort by Average pH":
        print("change to pH")
    elif event == "Sort by Average Value of Dissolved Oxygen":
        print("change to dissolved oxygen")
    elif event == "Sort by Average Conductivity Level":
        print("change to conductivity")
    elif event == "Sort by Average Biochemical Oxygen Demand":
        print("change to biochemical")
    elif event == "Sort by Average Nitrate-n and Nitrite-n Values":
        print("change to nitrate-n")
    elif event == "Sort by Average Fecal Coliform":
        print("change to coliform")

data_window.close()