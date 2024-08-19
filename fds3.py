import matplotlib.pyplot as plt
roles=['Data Scientist','Data engineer','Data Analyst']
posting=[30,50,10]
plt.bar(roles,posting,width=0.2)
plt.title('Distribution of various data science role')
plt.xlabel('Job')
plt.ylabel('no of posting')
plt.show()
