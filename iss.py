#!/usr/bin/env python

__author__ = 'pattersonday (pair programmed with astephens91)'

import requests
import json
import turtle
import time


def astronaunts():
    r = requests.get('http://api.open-notify.org/astros.json')
    crew_dictionary = json.loads(r.text)
    for members in crew_dictionary['people']:
        print('{} is floating around in space'.format(members['name']))


def coordinates():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    coordinate_dictionary = json.loads(r.text)
    longitude = coordinate_dictionary['iss_position']['longitude']
    latitude = coordinate_dictionary['iss_position']['latitude']
    print('The ISS is floating at this {} and this {}'.format(
        latitude, longitude))
    return (float(longitude), float(latitude))


def create_map(pos):
    new_screen = turtle.Screen()
    new_screen.bgpic('./map.gif')
    new_screen.addshape('iss.gif')
    new_screen.setup(width=720, height=360)
    new_screen.setworldcoordinates(-180, -90, 180, 90)

    positions = turtle.Turtle()
    positions.shape('iss.gif')
    positions.penup()
    positions.goto(pos)

    indy_coordinates = turtle.Turtle()
    indy_coordinates.shape('circle')
    indy_coordinates.color('purple')
    indy_coordinates.penup()
    indy_coordinates.goto(-86.1349, 39.7684)

    print_stmt = turtle.Turtle()
    print_stmt.color('white')
    print_stmt.penup()
    print_stmt.goto(-90.1349, 48.7684)
    print_stmt.write(time_until_pass(), font=("Times New Roman", 18, "normal"))

    new_screen.exitonclick()


def time_until_pass():
    r = requests.get('http://api.open-notify.org/iss-pass.json',
                     {'lon': -86.1349, 'lat': 39.7684, 'n': 1})
    indianapolis_coordinates = json.loads(r.text)

    for place in indianapolis_coordinates['response']:
        next_pass = time.ctime(place['risetime'])
    return ('ISS will be above Indy {}'.format(next_pass))


def main():
    astronaunts()
    var = coordinates()
    create_map(var)
    time_until_pass()


if __name__ == '__main__':
    main()
