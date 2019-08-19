# Azure NOAA Open Dataset Simple Wheel
This wheel was developed to demonstrate a simple UDF using Azure Open Datasets, see article: https://stochasticcoder.com/2019/07/22/using-azure-open-datasets-with-databricks/.
 
 ### Build Wheel
 - Pip install setuptools
 From the whl directory run:
 '''
 python setup.py bdist_wheel 
'''

**See Article to learn how to attach wheel to Azure Databricks**



### Use new library
```

from DemoWheel import weatherfunc

##Creat UDF
tempConvert = udf(weatherfunc.celsius_to_fahrenheit)

##Register for SparkSQL
sqlContext.registerFunction('tempConvert',tempConvert)

#Display original dataset temperature (celsius) and converted (fahrenheit)
display(df.limit(5).select('temperature',tempConvert('temperature').alias('fahrenheit')))

```

### Create Temp View in Databricks

```

df.createOrReplaceTempView('NOAA')

```

### Spark UDF 
```

%sql

SELECT temperature as celsius, 
tempConvert(temperature) as fahrenheit
FROM NOAA
LIMIT 10;

```
