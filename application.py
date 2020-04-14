# Standard library
import os
import time
import xml.dom.minidom as minidom
import sys

# Third-party depedencies
from bottle import run, route, response, request, post, get

# Local modules
from src.estimator import estimator, sample_input_data


def create_xml_from_json(json_data: dict):
    '''Generate xml from json. Doesn\'t work properly yet'''
    document = minidom.Document()
    rootElement = document.appendChild(
        document.createElement('covid-19-estimate'))
    for key, value in json_data.items():
        element = document.createElement(str(key))
        if isinstance(value, dict):
            for key, value in value.items():
                childElement = document.createElement(str(key))
                childElement.appendChild(document.createTextNode(str(value)))
                element.appendChild(childElement)

        else:
            element.appendChild(document.createTextNode(str(value)))

        rootElement.appendChild(element)
    return document


def allow_cors(func):
    def wrapper(*args, **kwargs):
        response.set_header('Access-Control-Allow-Origin', '*')
        response.set_header('Access-Control-Allow-Methods',
                            'GET, POST, PUT, OPTIONS')
        response.set_header('Access-Control-Allow-Headers',
                            'Origin, Accept, Content-Type,X-Requested-With')
        if request.method != 'OPTIONS':
            return func(*args, **kwargs)
    return wrapper


@route('/api/v1/on-covid-19', method=['OPTIONS', 'POST'])
@route('/api/v1/on-covid-19/', method=['OPTIONS', 'POST'])
@allow_cors
def json_response():
    reques_time = time.monotonic()

    try:
        data = estimator(request.json)
    except:
        data = {}

    with open('./access.log', 'a') as log:
        log.write(
            f'{request.method} \t\t {request.path} \t\t {response.status_code} \t\t {round(time.monotonic()-reques_time, 3)} S \n')

    return data


@route('/api/v1/on-covid-19/xml', method=['OPTIONS', 'POST'])
@route('/api/v1/on-covid-19/xml/', method=['OPTIONS', 'POST'])
@allow_cors
def xml_response():
    reques_time = time.monotonic()

    response.set_header('content-type', 'text/xml')

    try:
        data = estimator(request.json)
    except:
        data = {}

    xml_data = create_xml_from_json(data).toprettyxml()

    with open('./access.log', 'a') as log:
        log.write(
            f'{request.method} \t\t {request.path} \t\t {response.status_code} \t\t {round(time.monotonic()-reques_time, 3)} S \n')

    return xml_data


@route('/api/v1/on-covid-19/logs/', method=['OPTIONS', 'GET'])
@route('/api/v1/on-covid-19/logs', method=['OPTIONS', 'GET'])
def logs():
    reques_time = time.monotonic()

    response.set_header('content-type', 'text/plain')

    with open('./access.log', 'a') as log:
        log.write(
            f'{request.method} \t\t {request.path} \t\t {response.status_code} \t\t {round(time.monotonic()-reques_time, 3)} S \n')

    with open('./access.log', 'r') as log:
        return log.read()


run(host='localhost', port=8080, debug=True, reloader=True)
