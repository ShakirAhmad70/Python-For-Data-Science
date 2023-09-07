#DF(DataFrame) is a table data structure
import pandas as pd
df = pd.read_csv("weatherData.csv") #returns the dataframe object


def main():
    print(df)
    print()
    print("Shape is:",df.shape[0],"Rows and",df.shape[1],"Columns")
    print()
    print("##########Printing 5 rows from the table###########")
    print(df.head()) #Print 5 rows from the table
    print()
    print("##########Printing 2 rows from the table###########")
    print(df.head(2)) #Print 2 rows from the table
    print()
    print("##########Printing last 5 rows from the table###########")
    print(df.tail()) #Print last 5 rows from the table
    print()
    print("##########Printing last 1 row from the table###########")
    print(df.tail(1)) #Print last 1 row from the table
    print()
    print("##########Printing rows 2(inclusive) to 5(exclusive) from the table###########")
    print(df[2:5]) #Print rows 2(inclusive) to 5(exclusive) from the table
    print()
    print("##########Printing table in reverse order###########")
    print(df[::-1]) #Print table in reverse order
    print()
    print("##########Printing columns of table###########")
    print(df.columns) #Print columns of table
    print()
    print("##########Printing individual column(e.g. Day) of table###########")
    print(df["Day"]) #Print individual column(e.g. Day) of table
    ########OR
    # print(df.Day) #Print individual column(e.g. Day) of table
    print()
    print("##########Printing data type of column's content of table###########")
    print(df.dtypes) #Print data type of column's content of table
    print()   
    print("##########Printing two columns of table###########")
    print(df[["Day","Temperature"]]) #Print two columns of table
    print()
    print("##########Printing max temperature of table###########")
    print(df["Temperature"].max()) #Print max temperature of table
    print()
    print("##########Printing min temperature of table###########")
    print(df["Temperature"].min()) #Print min temperature of table
    print()
    print("##########Printing mean of temperature of table###########")
    print(df["Temperature"].mean()) #Print mean of temperature of table
    print()
    print("##########Printing sum of temperature of table###########")
    print(df["Temperature"].sum()) #Print sum of temperature of table
    print()
    print("##########Printing standard deviation of temperature of table###########")
    print(df["Temperature"].std()) #Print standard deviation of temperature of table
    print()
    print("##########Printing last date of table###########")
    print(df["Day"].tail(1)) #Print last date of table
    print()
    print("##########Printing stats of table###########")
    print(df.describe()) #Print stats of table
    print()
    print("##########Printing info of table###########")
    print(df.info()) #Print info of table
    print()
    print("##########Printing temperature > 32 from table###########")
    print(df[df["Temperature"] > 32]) #Print temperature > 32 from table    
    print()
    print("##########Printing the row in which temperature is maximum from table###########")
    print(df[df.Temperature == df.Temperature.max()]) #Print the row in which temperature is maximum from table
    print()
    
    
    

if __name__ == "__main__":
    main()
    