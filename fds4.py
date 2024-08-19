import pandas as pd
sd=pd.DataFrame(
        {
            "ID":[1,2,3],
            "Name":['Raj','Riya','Ram'],
            "Age":[23,18,25]
        })
print('Structured Data\n',sd)
print('')
unsd='This is a unstructured data which contain audio, video,combination of data type.'
print('Unstructured Data\n',unsd,'\n')
semisd='{"Name":"Raju","Age":40,"Job":"Software engineer","Hobby":"Gamming"}'
print('Semistructured Data\n',semisd)