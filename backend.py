import requests

API_KEY = "3710347f23ce737983697beea61105ce"


def get_data(city, forecastdays=None, option=None):
    # url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    # response = requests.get(url)
    # data = response.json()
    data = {'cod': '200', 'message': 0, 'cnt': 40,
            'list': [{'dt': 1721876400, 'main': {'temp': 304.91, 'feels_like': 310.56, 'temp_min': 304.91, 'temp_max': 305.86, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 63, 'temp_kf': -0.95}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 58}, 'wind': {'speed': 1.2, 'deg': 146, 'gust': 1.82}, 'visibility': 10000, 'pop': 0.34, 'rain': {'3h': 0.31}, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-25 03:00:00'}, {'dt': 1721887200, 'main': {'temp': 305.57, 'feels_like': 310.59, 'temp_min': 305.57, 'temp_max': 306.13, 'pressure': 1007, 'sea_level': 1007, 'grnd_level': 1006, 'humidity': 58, 'temp_kf': -0.56}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 78}, 'wind': {'speed': 4.78, 'deg': 169, 'gust': 4.36}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-25 06:00:00'}, {'dt': 1721898000, 'main': {'temp': 304.35, 'feels_like': 308.17, 'temp_min': 304.35, 'temp_max': 304.35, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 59, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 99}, 'wind': {'speed': 5.54, 'deg': 160, 'gust': 5.53}, 'visibility': 10000, 'pop': 0.17, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-25 09:00:00'}, {'dt': 1721908800, 'main': {'temp': 304.13, 'feels_like': 307.95, 'temp_min': 304.13, 'temp_max': 304.13, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1007, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.84, 'deg': 171, 'gust': 3.02}, 'visibility': 10000, 'pop': 0.03, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-25 12:00:00'}, {'dt': 1721919600, 'main': {'temp': 303.57, 'feels_like': 307.48, 'temp_min': 303.57, 'temp_max': 303.57, 'pressure': 1010, 'sea_level': 1010, 'grnd_level': 1008, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 83}, 'wind': {'speed': 0.86, 'deg': 320, 'gust': 3.15}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-25 15:00:00'}, {'dt': 1721930400, 'main': {'temp': 302.71, 'feels_like': 306.3, 'temp_min': 302.71, 'temp_max': 302.71, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1009, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 59}, 'wind': {'speed': 2.62, 'deg': 347, 'gust': 2.99}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-25 18:00:00'}, {'dt': 1721941200, 'main': {'temp': 302.23, 'feels_like': 305.32, 'temp_min': 302.23, 'temp_max': 302.23, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 66, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 60}, 'wind': {'speed': 1.31, 'deg': 21, 'gust': 1.52}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-25 21:00:00'}, {'dt': 1721952000, 'main': {'temp': 304.28, 'feels_like': 307.53, 'temp_min': 304.28, 'temp_max': 304.28, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 57, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 75}, 'wind': {'speed': 1.14, 'deg': 52, 'gust': 1.07}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-26 00:00:00'}, {'dt': 1721962800, 'main': {'temp': 306.07, 'feels_like': 309.86, 'temp_min': 306.07, 'temp_max': 306.07, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 52, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 99}, 'wind': {'speed': 3.63, 'deg': 158, 'gust': 2.35}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-26 03:00:00'}, {'dt': 1721973600, 'main': {'temp': 305.53, 'feels_like': 309.89, 'temp_min': 305.53, 'temp_max': 305.53, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1012, 'humidity': 56, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 96}, 'wind': {'speed': 5.43, 'deg': 166, 'gust': 4.57}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-26 06:00:00'}, {'dt': 1721984400, 'main': {'temp': 305.39, 'feels_like': 309.87, 'temp_min': 305.39, 'temp_max': 305.39, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 57, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 78}, 'wind': {'speed': 4.78, 'deg': 169, 'gust': 4.49}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-26 09:00:00'}, {'dt': 1721995200, 'main': {'temp': 305, 'feels_like': 309.3, 'temp_min': 305, 'temp_max': 305, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1013, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 78}, 'wind': {'speed': 2.44, 'deg': 185, 'gust': 2.84}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-26 12:00:00'}, {'dt': 1722006000, 'main': {'temp': 304.18, 'feels_like': 308.83, 'temp_min': 304.18, 'temp_max': 304.18, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1014, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.02, 'deg': 35, 'gust': 3.04}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-26 15:00:00'}, {'dt': 1722016800, 'main': {'temp': 303.57, 'feels_like': 307.72, 'temp_min': 303.57, 'temp_max': 303.57, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1013, 'humidity': 64, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.7, 'deg': 19, 'gust': 2.18}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-26 18:00:00'}, {'dt': 1722027600, 'main': {'temp': 303.36, 'feels_like': 307.04, 'temp_min': 303.36, 'temp_max': 303.36, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1015, 'humidity': 63, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.53, 'deg': 31, 'gust': 2.78}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-26 21:00:00'}, {'dt': 1722038400, 'main': {'temp': 304.38, 'feels_like': 308.75, 'temp_min': 304.38, 'temp_max': 304.38, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1015, 'humidity': 61, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.51, 'deg': 62, 'gust': 2.14}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-27 00:00:00'}, {'dt': 1722049200, 'main': {'temp': 307.14, 'feels_like': 311.86, 'temp_min': 307.14, 'temp_max': 307.14, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1014, 'humidity': 51, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.28, 'deg': 124, 'gust': 2.25}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-27 03:00:00'}, {'dt': 1722060000, 'main': {'temp': 306.78, 'feels_like': 311.73, 'temp_min': 306.78, 'temp_max': 306.78, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1013, 'humidity': 53, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 91}, 'wind': {'speed': 8.02, 'deg': 153, 'gust': 6.04}, 'visibility': 10000, 'pop': 0.03, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-27 06:00:00'}, {'dt': 1722070800, 'main': {'temp': 303.47, 'feels_like': 308.47, 'temp_min': 303.47, 'temp_max': 303.47, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1014, 'humidity': 68, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 5.73, 'deg': 126, 'gust': 5.62}, 'visibility': 10000, 'pop': 0.63, 'rain': {'3h': 0.53}, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-27 09:00:00'}, {'dt': 1722081600, 'main': {'temp': 301.26, 'feels_like': 305.05, 'temp_min': 301.26, 'temp_max': 301.26, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1016, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 97}, 'wind': {'speed': 5.25, 'deg': 85, 'gust': 5.48}, 'visibility': 10000, 'pop': 0.92, 'rain': {'3h': 0.3}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-27 12:00:00'}, {'dt': 1722092400, 'main': {'temp': 300.2, 'feels_like': 302.91, 'temp_min': 300.2, 'temp_max': 300.2, 'pressure': 1016, 'sea_level': 1016, 'grnd_level': 1015, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.46, 'deg': 60, 'gust': 3}, 'visibility': 10000, 'pop': 0.8, 'rain': {'3h': 0.7}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-27 15:00:00'}, {'dt': 1722103200, 'main': {'temp': 299.31, 'feels_like': 299.31, 'temp_min': 299.31, 'temp_max': 299.31, 'pressure': 1015, 'sea_level': 1015, 'grnd_level': 1013, 'humidity': 83, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.66, 'deg': 72, 'gust': 2.42}, 'visibility': 10000, 'pop': 1, 'rain': {'3h': 2.02}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-27 18:00:00'}, {'dt': 1722114000, 'main': {'temp': 299.92, 'feels_like': 302.39, 'temp_min': 299.92, 'temp_max': 299.92, 'pressure': 1014, 'sea_level': 1014, 'grnd_level': 1013, 'humidity': 80, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.48, 'deg': 145, 'gust': 1.17}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-27 21:00:00'}, {'dt': 1722124800, 'main': {'temp': 302.1, 'feels_like': 305.95, 'temp_min': 302.1, 'temp_max': 302.1, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 1011, 'humidity': 71, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 2.81, 'deg': 183, 'gust': 2.6}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-28 00:00:00'}, {'dt': 1722135600, 'main': {'temp': 304.88, 'feels_like': 309.6, 'temp_min': 304.88, 'temp_max': 304.88, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 1009, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.98, 'deg': 150, 'gust': 2.22}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-28 03:00:00'}, {'dt': 1722146400, 'main': {'temp': 306.11, 'feels_like': 310.56, 'temp_min': 306.11, 'temp_max': 306.11, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1007, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 4.35, 'deg': 151, 'gust': 2.55}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-28 06:00:00'}, {'dt': 1722157200, 'main': {'temp': 304.49, 'feels_like': 308.73, 'temp_min': 304.49, 'temp_max': 304.49, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1007, 'humidity': 60, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 89}, 'wind': {'speed': 5.2, 'deg': 160, 'gust': 4.59}, 'visibility': 10000, 'pop': 0.2, 'rain': {'3h': 0.2}, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-28 09:00:00'}, {'dt': 1722168000, 'main': {'temp': 302.3, 'feels_like': 307.22, 'temp_min': 302.3, 'temp_max': 302.3, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 1008, 'humidity': 75, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 95}, 'wind': {'speed': 3.4, 'deg': 132, 'gust': 3.22}, 'visibility': 10000, 'pop': 0.67, 'rain': {'3h': 0.55}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-28 12:00:00'}, {'dt': 1722178800, 'main': {'temp': 301.93, 'feels_like': 306.69, 'temp_min': 301.93, 'temp_max': 301.93, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 1006, 'humidity': 77, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.75, 'deg': 156, 'gust': 1.01}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-28 15:00:00'}, {'dt': 1722189600, 'main': {'temp': 302.61, 'feels_like': 307.56, 'temp_min': 302.61, 'temp_max': 302.61, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 73, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.85, 'deg': 265, 'gust': 1.44}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-28 18:00:00'}, {'dt': 1722200400, 'main': {'temp': 302.62, 'feels_like': 306.31, 'temp_min': 302.62, 'temp_max': 302.62, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 1004, 'humidity': 67, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 0.63, 'deg': 73, 'gust': 0.15}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-28 21:00:00'}, {'dt': 1722211200, 'main': {'temp': 305.08, 'feels_like': 309.48, 'temp_min': 305.08, 'temp_max': 305.08, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 1003, 'humidity': 58, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.07, 'deg': 192, 'gust': 1.28}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-29 00:00:00'}, {'dt': 1722222000, 'main': {'temp': 308.56, 'feels_like': 312.14, 'temp_min': 308.56, 'temp_max': 308.56, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 1001, 'humidity': 43, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.27, 'deg': 175, 'gust': 3.08}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-29 03:00:00'}, {'dt': 1722232800, 'main': {'temp': 309.93, 'feels_like': 313.51, 'temp_min': 309.93, 'temp_max': 309.93, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 999, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 94}, 'wind': {'speed': 5.63, 'deg': 181, 'gust': 5.92}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-29 06:00:00'}, {'dt': 1722243600, 'main': {'temp': 308.61, 'feels_like': 312.24, 'temp_min': 308.61, 'temp_max': 308.61, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 999, 'humidity': 43, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 93}, 'wind': {'speed': 5.65, 'deg': 203, 'gust': 4.47}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-29 09:00:00'}, {'dt': 1722254400, 'main': {'temp': 306.1, 'feels_like': 309.63, 'temp_min': 306.1, 'temp_max': 306.1, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 1000, 'humidity': 51, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 69}, 'wind': {'speed': 3.52, 'deg': 182, 'gust': 3.41}, 'visibility': 10000, 'pop': 0.2, 'rain': {'3h': 0.12}, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-29 12:00:00'}, {'dt': 1722265200, 'main': {'temp': 304.9, 'feels_like': 308.02, 'temp_min': 304.9, 'temp_max': 304.9, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 999, 'humidity': 54, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 66}, 'wind': {'speed': 1.96, 'deg': 237, 'gust': 2.53}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-29 15:00:00'}, {'dt': 1722276000, 'main': {'temp': 304.48, 'feels_like': 306.54, 'temp_min': 304.48, 'temp_max': 304.48, 'pressure': 999, 'sea_level': 999, 'grnd_level': 998, 'humidity': 51, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'clouds': {'all': 83}, 'wind': {'speed': 2.39, 'deg': 358, 'gust': 3.52}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2024-07-29 18:00:00'}, {'dt': 1722286800, 'main': {'temp': 303.8, 'feels_like': 305.38, 'temp_min': 303.8, 'temp_max': 303.8, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 999, 'humidity': 51, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 4.04, 'deg': 8, 'gust': 5.73}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-29 21:00:00'}, {'dt': 1722297600, 'main': {'temp': 302.62, 'feels_like': 305.36, 'temp_min': 302.62, 'temp_max': 302.62, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 1000, 'humidity': 62, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 100}, 'wind': {'speed': 3.62, 'deg': 21, 'gust': 4.29}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-07-30 00:00:00'}], 'city': {'id': 1850144, 'name': 'Tokyo', 'coord': {'lat': 35.6895, 'lon': 139.6917}, 'country': 'JP', 'population': 12445327, 'timezone': 32400, 'sunrise': 1721850220, 'sunset': 1721901092}}
    filtered_data = data['list']
    nr_values = 8 * forecastdays
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", forecastdays=3, option="Sky"))