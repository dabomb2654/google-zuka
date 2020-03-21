import pandas as pd
import dash 
import dash_core_components as dcc
import dash_html_components as html
import datetime

def importAllData():
    names = ["Troupe", "EnglishTitle", "JapaneseTitle", "RomanizedTitle", "Venue", "Director", "Author", "Composer","Choreographer", "TopStar", "TopStarNIR", "TopMusume","TopMusumeNIR", "Lead", "OA", "TA", "SP", "DS", "Genre","Adapt","Revival","RevivalTroupe", "AdaptFrom", "Start Day", "Start Month", "Start Year", "End Day", "End Month", "End Year"]
    years=["2000"]
    paths = []
    for year in years:
        paths.append("https://raw.githubusercontent.com/dabomb2654/dabomb2654.github.io/master/zuka_performances_period_"+year+".csv")
    from_csv = pd.read_csv(paths[0], encoding='utf-8', error_bad_lines=False, header=None, names=names)
    print(from_csv.shape)
    for path in paths[1:]:
        from_csv = from_csv.append(pd.read_csv(path, encoding='utf-8', error_bad_lines=False, header=None, names=names))
    print(from_csv.shape)
    return from_csv

class Flower:
    eng_name = "flower"
    jpn_name = "花組"
    color = "#F489A1"
class Snow:
    eng_name = "snow"
    jpn_name = "雪組"
    color = "#A8D7C4"
class Moon:
    eng_name = "moon"
    jpn_name = "月組"
    color = "#F2D269"
class Star:
    eng_name = "star"
    jpn_name = "星組"
    color = "#5ABCD8"
class Cosmos:
    eng_name = "cosmos"
    jpn_name = "宙組"
    color = "#E5C6DE"
class Senka:
    eng_name = "senka"
    jpn_name = "専科"
    color = "#5C508D"

info_flower = Flower()
info_snow = Snow()
info_moon = Moon()
info_star = Star()
info_cosmos = Cosmos()
info_senka = Senka()

from_csv = importAllData()
app = dash.Dash(__name__)
server = app.server

input_types = ( "day", "month", "year", "name")
time_val = str(datetime.datetime.now())
troupe_names = [info_flower.eng_name, info_snow.eng_name, info_moon.eng_name, info_star.eng_name, info_cosmos.eng_name, info_senka.eng_name]
troupe_names_jpn = [info_flower.jpn_name, info_snow.jpn_name, info_moon.jpn_name, info_star.jpn_name, info_cosmos.jpn_name, info_senka.jpn_name]
colors = [info_flower.color, info_snow.color, info_moon.color, info_star.color, info_cosmos.color, info_senka.color]
numFlower = 0
numSnow = 0
numStar = 0 
numCosmos = 0
numMoon = 0
numSenka = 0
genres = []
genre_counter = dict()
for x in from_csv["Genre"]:
    if isinstance(x, float) == True or x == "genre":
        continue
    x = x.lower()
    if " " in x:
        x = x.replace(" ", "")
    if '.' in x:
        x.replace(" ", "")
        genre_split = x.split('.')
        for y in genre_split:
            if y not in genres:
                genres.append(y)
                genre_counter.update({y:1})
            elif y in genres:
                genre_counter[y] += 1
    elif x in genres:
        genre_counter[x] += 1
    elif x not in genres:
        genres.append(x)
        genre_counter.update({x:1})
print (genre_counter)
values_genre = []
for x in genre_counter:
    values_genre.append(genre_counter[x])
print(values_genre)
for x in from_csv["Troupe"]:
    if "Flower" in x:
        numFlower += 1
    if "Snow" in x:
        numSnow += 1
    if "Star" in x:
        numStar += 1
    if "Cosmos" in x:
        numCosmos += 1
    if "Moon" in x:
        numMoon += 1
    if "Senka" in x:
        numSenka += 1
labels=troupe_names
values = [numFlower, numSnow, numMoon, numStar, numCosmos, numSenka]
data = [{
      'values': values,
      'labels':labels,
      'type': 'pie',
      'showlegend': True,
      'marker': dict(colors=colors, line=dict(color='#000000', width=2))
    },
    ]
data_genre = [{
    'values':values_genre,
    'labels': genres,
    'type': 'pie',
    'showlegend':False,
    },
    ]
id_name = 'graph'+time_val
line_data = [{
      'x': [906, 1013],
      'y': [1, 1],
      'type': 'scatter',
      'mode': 'lines+markers',
      'showlegend': True,
    },
    {
      'x': [1004, 1111],
      'y': [2, 2],
      'type': 'scatter',
      'mode': 'lines+markers',
      'showlegend': True,
    },
    {
      'x': [1012, 1110],
      'y': [3, 3],
      'type': 'scatter',
      'mode': 'lines+markers',
      'showlegend': True,
    },
    {
      'x': [1016, 1017, 1022],
      'y': [4, 4, 4],
      'type': 'scatter',
      'mode': 'markers',
      'showlegend': True,
    },
    ]
data = pd.read_csv("https://raw.githubusercontent.com/dabomb2654/google-zuka/master/tsr_final.csv")
print(len(data))
line_info = []
for x in range(len(data)):
	name = str(data['name_eng'][x]) + ", " + str(data['name_jpn'][x])
	start_split = data['start_date'][x].split("/")
	start_year = float(start_split[2])
	if start_year < 50.0:
		start_year = start_year + 2000.0
	else:
		start_year = start_year + 1900.0
	start_year = start_year - 1976.0
	start_num_months = (start_year * 12.0) + float(start_split[0]) + (float(start_split[1]) / 31)
	end_split = data['end_date'][x].split("/")
	end_year = float(end_split[2])
	if end_year < 50.0:
		end_year = end_year + 2000.0
	else:
		end_year = end_year + 1900.0
	end_year = end_year - 1976.0
	end_num_months = (end_year * 12.0) + float(end_split[0]) + (float(end_split[1]) / 31)
	default_dict = {'x': [start_num_months, end_num_months],'y':[x,x],'type':'scatter','mode':'lines+markers','name':name,}
	line_info.append(default_dict)
''' start of dash plotly layout '''
app.layout = html.Div(children=[  
#html.H1("zuka charts", id="title", className="title"),
#html.H4("a site to make charts of data compiled from the takawiki", id="site-description",className="site-description"),
#html.Button('make a chart', id='button_makeChart'),
#html.Button('make a schedule', id='button_makeSchedule'),
#html.H5("troupe", id="text_textboxes_troupe"),
    dcc.Graph(
    	id='bar-chart',
  		animate=True,
    	figure={
    		'data': line_info,
    	}
    	),
'''
dcc.Graph(
    id='numshowspie',
    figure={
    'data': data,
    'layout': {
        'margin': {
                    'l': 25,
                    'r': 25,
                    'b': 25,
                    't': 25
        },
        'legend':{'Flower':numFlower, 'Snow':numSnow, 'Cosmos':numCosmos, 'Snow':numSnow, 'Senka':numSenka, 'Moon':numMoon}
        }
      }
  ),
html.Div(
    [
        dcc.Input(
            id = "input_{}".format(x),
            type="text",
            placeholder="please input {}".format(x),
            )
        for x in input_types
    ]
),
html.Button('add', id='button_add'),
dcc.Graph(
    id='genrepie',
    figure={
    'data':data_genre,
    'layout':{
        'margin': {
                    'l': 25,
                    'r': 25,
                    'b': 25,
                    't': 25
        },
    }
    }),
dcc.Dropdown(
    id='dropdown-day',
    options=[
        {'label':'1', 'value': '1'},
        {'label':'2', 'value': '2'},
        {'label':'3', 'value': '3'},
        {'label':'4', 'value': '4'},
        {'label':'5', 'value': '5'},
        {'label':'6', 'value': '6'},
        {'label':'7', 'value': '7'},
        {'label':'8', 'value': '8'},
        {'label':'9', 'value': '9'},
        {'label':'10', 'value': '10'},
        {'label':'11', 'value': '11'},
        {'label':'12', 'value': '12'},
    ],
    value='1'
),
html.Div(id='output-container-1'),
dcc.Dropdown(
    options=[
        {'label':'1', 'value': '1'},
        {'label':'2', 'value': '2'},
        {'label':'3', 'value': '3'},
        {'label':'4', 'value': '4'},
        {'label':'5', 'value': '5'},
        {'label':'6', 'value': '6'},
        {'label':'7', 'value': '7'},
        {'label':'8', 'value': '8'},
        {'label':'9', 'value': '9'},
        {'label':'10', 'value': '10'},
        {'label':'11', 'value': '11'},
        {'label':'12', 'value': '12'},
        {'label':'13', 'value': '13'},
        {'label':'14', 'value': '14'},
        {'label':'15', 'value': '15'},
        {'label':'16', 'value': '16'},
        {'label':'17', 'value': '17'},
        {'label':'18', 'value': '18'},
        {'label':'19', 'value': '19'},
        {'label':'20', 'value': '20'},
        {'label':'21', 'value': '21'},
        {'label':'22', 'value': '22'},
        {'label':'23', 'value': '23'},
        {'label':'24', 'value': '24'},
        {'label':'25', 'value': '25'},
        {'label':'26', 'value': '26'},
        {'label':'27', 'value': '27'},
        {'label':'28', 'value': '28'},
        {'label':'29', 'value': '29'},
        {'label':'30', 'value': '30'},
        {'label':'31', 'value': '31'},

    ],
    value='1'
),
dcc.Dropdown(
    options=[
        {'label':'2019', 'value': '2019'},
        {'label':'2020', 'value': '2020'}
    ],
    value='2019'
),
dcc.Dropdown(
    id='dropdown-day-2',
    options=[
        {'label':'1', 'value': '1'},
        {'label':'2', 'value': '2'},
        {'label':'3', 'value': '3'},
        {'label':'4', 'value': '4'},
        {'label':'5', 'value': '5'},
        {'label':'6', 'value': '6'},
        {'label':'7', 'value': '7'},
        {'label':'8', 'value': '8'},
        {'label':'9', 'value': '9'},
        {'label':'10', 'value': '10'},
        {'label':'11', 'value': '11'},
        {'label':'12', 'value': '12'},
    ],
    value='1'
),
html.Div(id='output-container-2'),
dcc.Dropdown(
    options=[
        {'label':'1', 'value': '1'},
        {'label':'2', 'value': '2'},
        {'label':'3', 'value': '3'},
        {'label':'4', 'value': '4'},
        {'label':'5', 'value': '5'},
        {'label':'6', 'value': '6'},
        {'label':'7', 'value': '7'},
        {'label':'8', 'value': '8'},
        {'label':'9', 'value': '9'},
        {'label':'10', 'value': '10'},
        {'label':'11', 'value': '11'},
        {'label':'12', 'value': '12'},
        {'label':'13', 'value': '13'},
        {'label':'14', 'value': '14'},
        {'label':'15', 'value': '15'},
        {'label':'16', 'value': '16'},
        {'label':'17', 'value': '17'},
        {'label':'18', 'value': '18'},
        {'label':'19', 'value': '19'},
        {'label':'20', 'value': '20'},
        {'label':'21', 'value': '21'},
        {'label':'22', 'value': '22'},
        {'label':'23', 'value': '23'},
        {'label':'24', 'value': '24'},
        {'label':'25', 'value': '25'},
        {'label':'26', 'value': '26'},
        {'label':'27', 'value': '27'},
        {'label':'28', 'value': '28'},
        {'label':'29', 'value': '29'},
        {'label':'30', 'value': '30'},
        {'label':'31', 'value': '31'},

    ],
    value='1'
),
dcc.Dropdown(
    options=[
        {'label':'2019', 'value': '2019'},
        {'label':'2020', 'value': '2020'}
    ],
    value='2019'
),
dcc.Dropdown(
    id="show_graph",
    options = [
    {'label':'show', 'value':'true'},
    {'label':'don''t show', 'value':'false'}
    ],
    value = 'true'
    ),
html.Div(id="container_line_graph", children=[dcc.Graph(
    id='line-test',
    figure={
    'data': line_data,
    }
    )]),
'''

])
@app.callback(
    dash.dependencies.Output('output-container-1', 'children'),
    [dash.dependencies.Input('dropdown-day', 'value')])

def update_output(value):
    return ('hello')

print("about to run")
if __name__ == '__main__':
    app.run_server(debug=False)



