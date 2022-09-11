import PySimpleGUI as sg
from parsecsv import set_waste, show_waste, parse_lake_data
from analysis import getDifference, sortList
from convert import dictionary_to_list
import parsecsv

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
button_size = (25, 1)

data_column = [
    [sg.Text("River data informations", font=("Helvetica", 30))],
    [sg.Button("Sort by Average Temperature", size=button_size,), 
     sg.Button("Sort by Average pH", size=button_size),
     sg.Button("Sort by Average Value of Dissolved Oxygen", size=button_size),
     sg.Button("Sort by Average Conductivity Level", size=button_size), 
     sg.Button("Sort by Average Biochemical Oxygen Demand", size=button_size), 
     sg.Button("Sort by Average Nitrate-n and Nitrite-n Values", size=button_size), 
     sg.Button("Sort by Average Fecal Coliform", size=button_size)],
     [sg.Button("Show Input Window")]
]



parse_lake_data()
dict_list = getDifference()

sorted_list = dictionary_to_list(dict_list)
# Get data from backend, update table
# TODO: automate table generation based on given data (table array)
def create_table():
    table_layout = [
        [
            sg.Table(
                headings=['River location:', 
                'Temperature', 
                'pH Level', 
                'Dissolved Oxygen:', 
                'Conductivity Level', 
                'Biochemical Oxygen Demand', 
                'Value of Nitrate-n and Nitrite-n', 
                'Fecal Coliform'],
                values=sorted_list,
                justification='center',
                col_widths=[25, 25, 25, 25, 25, 25, 25, 25], 
                auto_size_columns=False,
                key='table',
                display_row_numbers=True,
                row_height=75,
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
        sorted_list = dictionary_to_list(getDifference())
    elif event == "Sort by Average Temperature":
        print('sort by temperature')
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'tempDiff')))
        print(sortList(getDifference(), 'temp')[0:50])
    elif event == "Sort by Average pH":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'pHDiff')))
        print('sort by pH')
    elif event == "Sort by Average Value of Dissolved Oxygen":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'DODiff')))
        print("change to dissolved oxygen")
    elif event == "Sort by Average Conductivity Level":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'conductivityDiff')))
        print("change to conductivity")
    elif event == "Sort by Average Biochemical Oxygen Demand":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'BODDiff')))
        print("change to biochemical")
    elif event == "Sort by Average Nitrate-n and Nitrite-n Values":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'nitrate_n_nitriteDiff')))
        print("change to nitrate-n")
    elif event == "Sort by Average Fecal Coliform":
        data_window['table'].update(dictionary_to_list(sortList(getDifference(), 'fecal_coliformDiff')))
        print("change to coliform")
    print(parsecsv.waste)


data_window.close()