import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plp
import plotly.express as px

with open('Dwarf_Stars.csv','r',encoding='utf8') as f:
    data_list = csv.reader(f)
    data = list(data_list)

# headers = data[0]
planet_data = data[1:]

mass = []
radius = []
name = []
distance = []

for i in planet_data:
    try:
        p_mass = float(i[3])*1.989e+30
        p_radius = float(i[4])*6.957e+8
    except:
        p_mass = ''
        p_radius = ''

    mass.append(p_mass)
    radius.append(p_radius)
    name.append(i[1])
    distance.append(i[2])

gravity = []

def find_gravity(x=[],y=[]):
    for i,v in enumerate(x):
        for a,t in enumerate(y):
            if i == a and v != '' and t != '':
                g = ((float(v))/(float(t)**2))*6.67e-11
                gravity.append(g)
    return gravity

grv = find_gravity(x=mass, y=radius)

n_headers = ['Name','Distance','Mass','Radius','Gravity(in m/s2)']
n_planet_data = ['',
                 name,
                 distance,
                 mass,
                 radius,
                 gravity]

csv_data = pd.DataFrame(list(zip(name,distance,mass,radius,gravity)),columns=n_headers)
csv_data.to_csv('project131output(2).csv')