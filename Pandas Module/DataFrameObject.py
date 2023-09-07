import pandas as pd

weatherData = {
    'day' : ['1/1/2017', '2/1/2017', '3/1/2017', '4/1/2017', '5/1/2017', '6/1/2017' ],
    'temperature' : [32,35,28,24,32,31],
    'wind_speed' : [6,7,2,7,4,2],
    'event' : ['Snow','Rain','Sunny','Rain','Sunny','Snow']
}

df = pd.DataFrame(weatherData)
print(df)
print("Shape:",df.shape)
rows ,columns = df.shape
print(f"Rows: {rows}, Columns: {columns}")
