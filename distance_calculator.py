import PySimpleGUI as sg
from geopy.geocoders import Nominatim
from geopy import distance


layout = [
# create a distance function and increament it as location and destination change per trip.

[sg.Text('What is your current location?', size=(40, 1))],
            [sg.Listbox(
            values=['Cameron Road Lagos State', 'Ikeja Lagos State', 'Onisiwo Road Ikoyi Lagos', 'Glover Ikoyi Lagos', 'Ikoyi Lagos State', 'Walter Carrington Crescent Lagos State', 'Ikoyi road Lagos State',
                    'Obalende Lagos State', 'Lekki Lagos State'], size=(20, 5), select_mode='single', key="CITY_1")],
[sg.Text('What is your current destination?', size=(40, 1))],
            [sg.Listbox(
            values=['Cameron Road Lagos State', 'Ikeja Lagos State', 'Onisiwo Road Ikoyi Lagos', 'Glover Ikoyi Lagos', 'Ikoyi Lagos State', 'Walter Carrington Crescent Lagos State', 'Ikoyi road Lagos State',
                    'Obalende Lagos State', 'Lekki Lagos State'], size=(20, 5), select_mode='single', key="CITY_2")],

''' To use text input mode, you can comment the two location and destination list above. And uncomment input mode bellow'''

# [sg.Text("City 1:"), sg.InputText(size=(10, 1), key="CITY_1")],
# [sg.Text("City 2:"), sg.InputText(size=(10, 1), key="CITY_2")],
[sg.Text("Last Milage"), sg.InputText(size=(10, 1), key="METER")],
[sg.Text("Distance travelled: "), sg.InputText(size=(10,1), key="DISTANCE", readonly=True) ],
[sg.Text("Current Milage"), sg.InputText(size=(10, 1), key="MILAGE", readonly=True)],
[sg.Button("Milage"), sg.Button("Exit")]
]

''' Window size is not auto formatted, change size to fit your device window accordingly below'''

window = sg.Window("Odometer increamenting",layout, size=(300, 500))


passed_score = 50

def clear_input():
    for key in values:
        window[key]('')
        return None       

    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Milage":
         geolocator = Nominatim(user_agent="efafe10@gmail.com")

         c1 = values["CITY_1"] # input("City 1:")
         c2 = values["CITY_2"] # input("City 2:")

         l1 = geolocator.geocode(c1)
         l2 = geolocator.geocode(c2)

         loc1 = ((l1.latitude, l1.longitude))
         loc2 = ((l2.latitude, l2.longitude))

         print(distance.distance(loc1, loc2).km, "kms")
         current_meter = int(values["METER"])
         increament = (current_meter + float(distance.distance(loc1, loc2).km))
         window["MILAGE"].update(round(increament), 5)
         sg.popup(distance.distance(loc1, loc2).km, "kms")
         window["DISTANCE"].update(round(float(distance.distance(loc1, loc2).km)), 5)
         # sg.popup(increament)
         
           
window.close()