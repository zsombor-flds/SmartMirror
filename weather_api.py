def weather():
    ''' http://openweathermap.org/'''
    import pyowm
    data = {}
    owm = pyowm.OWM("00d400860e6a288e5682427bfd178b29")
    forecast = owm.daily_forecast("Budapest,hu")
    # print help(forecast.get_forecast())
    today_weather = forecast.get_forecast().get(0)
    temp = today_weather.get_temperature(unit='celsius')

    data["status"] = today_weather.get_detailed_status()  #
    data["icon"] = today_weather.get_weather_icon_name()  # http://openweathermap.org/weather-conditions
    data["temp"] = str(int(temp["day"]))

    return data


if __name__ == "__main__":
    raw = weather()
    for i in raw.keys():
        print i + ": " + str(raw[i])
