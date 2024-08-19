import pandas as pd
import matplotlib.pyplot as plt
name=['Data Scientist','Data Analyst','Data engineer','ML engineer']
data=[30,50,10,20]
plt.pie(data, labels=name)
plt.title('Role of Data Science')
plt.show()