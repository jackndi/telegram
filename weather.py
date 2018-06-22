from pyowm import OWM

owm = OWM("5a38db36afbbae4aa06ddde8c4cc9d27")


def get_forecasts(lat, lon):
    observation = owm.three_hours_forecast_at_coords(lat, lon)
    forecasts = observation.get_forecast()

    location = forecasts.get_location()
    loc_name = location.get_name()
    loc_lat = location.get_lat()
    loc_lon = location.get_lon()

    results = []

    for forecast in forecasts:
        time = forecast.get_reference_time('iso')
        status = forecast.get_status()
        detailed = forecast.get_detailed_status()
        temperature = forecast.get_temperature('celsius')
        temp = temperature.get("temp")
        temp_min = temperature.get("temp_min")
        temp_max = temperature.get("temp_max")

        results.append("""
        Location : {} Lat : {} Lon {}
        Time : {}
        Status : {}
        Detailed : {}
        Temperature : {}
        Min Temperature : {}
        Max Temperature : {}
        """.format(loc_name, loc_lat, loc_lon, time,
                   status, detailed, temp, temp_min, temp_max))

    return "".join(results[:10])


if __name__ == "__main__":
    print(get_forecasts(-1.2, 36))
