
from config import *
from data import *
from ui import *
import dash_bootstrap_components as dbc
import pandas as pd
import warnings
import dash
import os

initialize_data()

if not os.path.exists('./out/'): os.mkdir('./out')

app = dash.Dash(__name__, use_pages = True, external_stylesheets = [dbc.themes.SANDSTONE])

app.title = 'Mind-Wealth'
app.layout = get_app_layout()

warnings.simplefilter(action = 'ignore', category = FutureWarning)

app.run(debug = False, host = 'localhost', port = 1000)
