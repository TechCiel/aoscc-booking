#!/usr/bin/env python3

import csv
import logging
from flask import Flask, request, render_template

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        app.logger.info(f'{request.headers.get("X-Real-IP")} {request.form}')
        with app.open_instance_resource('data.csv', 'r') as f:
            for line in csv.reader(f):
                if (
                    line[1] == request.form['name']
                    and line[2] == request.form['mobile']
                    and line[3] == request.form['idcard']
                ):
                    app.logger.info(line)
                    return render_template('info.html', u=line, int=int)
        return render_template('form.html', error=True)
    return render_template('form.html')
