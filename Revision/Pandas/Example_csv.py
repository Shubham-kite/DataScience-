import pandas as pd 
filedata =pd.read_csv('data.csv')
filedata = pd.DataFrame(filedata)
#print(filedata)
#to check max numer of row display by ur system
#print(pd.options.display.max_rows)
''' diplay top five data '''
print(filedata.head(5))

''' display bottom 5 data '''
print(filedata.tail(5))

''' for the information about dataset '''
print(filedata.info())