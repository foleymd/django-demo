''' getting weather from openweathermap.org based on command line args and
    prints formatted data
    example on command line:
    python3 get_open_weather_formatted.py 30.266666 -97.733330 minutely,hourly,daily
    API docs: https://openweathermap.org/api
'''

import json
import requests
import sys
import pytz
from datetime import datetime
from geopy import Nominatim
from timezonefinder import TimezoneFinder
from weather.secret import open_weather_appid
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import CoordinateForm



class HomePageView(TemplateView):

    template_name = "weather.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context


class CurrentView(FormView):

    form_class = CoordinateForm
    template_name = 'current.html'

    # converts meteorological degrees to a cardinal direction
    def degrees_to_cardinal(self, degrees):

        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                      "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        ix = int((degrees + 11.25)/22.5 - 0.02)

        return directions[ix % 16]

    def get_weather(self, latitude, longitude):
        url = 'https://api.openweathermap.org/data/2.5/onecall?units=imperial&lat=%s&lon=%s&exclude=%s&appid=%s' % (
        latitude, longitude, 'daily, hourly, minutely', '4f454912d2fa235365a9b5ceaec5e95a')

        response = requests.get(url)
        response.raise_for_status()

        # formats json into python data structures
        current_weather_data = json.loads(response.text)["current"]
        return current_weather_data

    def get_location(self, latitude, longitude):

        # Nominatim takes combined lat and lon in one argument
        input_location = str(latitude + ', ' + longitude)

        # user_agent can be any email address
        geolocator = Nominatim(user_agent="foleymd@gmail.com")

        # actual call to get location data
        location = geolocator.reverse(input_location)

        # the location includes a ton of data - getting the raw data to provide
        # more generic information
        address = location.raw['address']
        address_list = [address.get('city', ''),
                        address.get('state', ''),
                        address.get('country', '')]

        display_location = ", ".join(filter(None, address_list))

        return display_location

    def get_timezone(self, latitude, longitude):
        # timezone processing requires lat and lon to be separate floats, though
        latitude, longitude = float(latitude), float(longitude)
        tz = pytz.timezone(TimezoneFinder().timezone_at(
            lng=longitude, lat=latitude))

        return tz

    def format_weather_data(self, weather, location, tz):
        # converting to month/day/year & 12-hr time based on time zone

        current_weather = {}
        current_weather['date'] = str(datetime.fromtimestamp(
            weather['dt'], tz).strftime('%m/%d/%Y %I:%M %p'))

        current_weather['description'] = weather["weather"][0]["description"].title()

        # # rounds and adds degree symbol + Fahrenheit
        current_weather['temp'] = self.format_temp(weather['temp'])
        current_weather['feels_like'] = self.format_temp(weather['feels_like'])

        # sunrise and sunset human-readable time based on time zone
        current_weather['sunrise'] = datetime.fromtimestamp(
            weather["sunrise"], tz).strftime('%I:%M %p')
        current_weather['sunset'] = datetime.fromtimestamp(weather["sunset"], tz).strftime('%I:%M %p')

        # adding units + direction of wind
        wind_speed = str(round(weather["wind_speed"], 1))
        wind_deg = str(self.degrees_to_cardinal(weather["wind_deg"]))
        current_weather['wind'] = str(wind_deg + ' ' + wind_speed)

        # more formatting
        current_weather['pressure'] = weather["pressure"]
        current_weather['humidity'] = weather["humidity"]
        current_weather['dew_point'] = self.format_temp(weather['dew_point'])

        # convert feet to miles, round
        current_weather['visibility'] =  str(round(weather["visibility"] / 1609.34, 1))

        return current_weather

    #standardized temperature output
    def format_temp(self, temp):
        temp = str(round(temp, 1)) + u"\N{DEGREE SIGN}" + 'F'
        return temp

    def get(self, request):
        form = self.form_class(initial=self.initial)
        template_name = 'current.html'
        return render(request, self.template_name, {'form': form, 'hello': template_name})

    def post(self, request):
        form = self.form_class(request.POST)
        latitude = form['latitude'].value()
        longitude = form['longitude'].value()
        weather = self.get_weather(latitude, longitude)
        location = self.get_location(latitude, longitude)
        tz = self.get_timezone(latitude, longitude)
        formatted_weather = self.format_weather_data(weather, location, tz)

        if form.is_valid():
            # <process form cleaned data>
            return render(request,
                          self.template_name,
                          {'form': form,
                          'weather': formatted_weather,
                          'location': location })
