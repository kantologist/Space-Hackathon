from flask import Flask, request, make_response, redirect, url_for, \
                    render_template, session, flash, current_app, abort, jsonify
from . import main
from .. import db
from ..utils import do_all
from webargs.flaskparser import use_args, use_kwargs, parser
from argument import *
import numpy as np
import pandas as pd


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/video')
def video():
    return render_template('video.html')

@main.route('/where')
def where():
    return render_template('where.html')

@main.route('/space')
def space():
    return render_template('space.html')

@main.route('/earth')
def earth():
    return render_template('earth.html')

@main.route('/appliance/<float:Power>')
def appliance(Power):
    Power = Power
    return render_template('appliance.html', Power=Power)


@main.route('/api/v1/predict')
@use_kwargs(features)
def predict(barometric, humidity, speed, temp, direction, eff, panel_area):
    X = np.array([barometric, humidity, speed, temp, direction])
    # X= pd.Series({"barometric": barometric, "humidity": humidity,
    #               "speed": speed, "temp": temp, "direction":direction})
    total = do_all(X, eff, panel_area)
    total = total[0]
    print total
    return jsonify({"total": str(total)})
