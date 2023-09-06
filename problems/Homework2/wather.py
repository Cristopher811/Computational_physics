from datetime import datetime 
from meteostat import Point, Daily
import matplotlib.pyplot as plt

# Set time period
start = datetime(2023, 5, 1)
end = datetime(2023, 9, 1)


# Create Point for Colima, México
place = Point(19.2413696,-103.7041664)

data = Daily(place, start, end)
data = data.fetch()

data.plot(y=['tavg', 'tmin', 'tmax'])

plt.title("Weather in Colima (01/08/2023 to 01/09/2023)")
plt.show()

