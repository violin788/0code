exec(open('util.py').read())
import yfinance as yf
stock = yf.Ticker("MSFT")
hist = stock.history(period="5y")


numpy_array = hist.to_numpy()
array = []
header_row = [hist.index.name]
for a,val in enumerate(hist.keys()):
	header_row.append(val)
print(header_row)
array.append(header_row)
print(array)
index = hist.index
print(index)
for a,val in enumerate(index):
	print(str(val))
	#if a==100:
	#	break
	new_row = []
	new_row.append(str(val))
	for b,valb in enumerate(numpy_array[a]):
		valb2 = dec([valb,2])
		new_row.append(valb2)
	print(new_row)

	array.append(new_row)
#for a,val in enumerate(array):
#	print(val)


end()



print(hist.loc[index[0]])
print(type(hist.loc[index[0]]))
#print(hist.loc[index[0]])
end()

for a,val in enumerate(index):
	new_row = []
	new_row.append(str(val))

end()


print(hist)
print(hist.index.name)

end()

keys = hist.keys()
print(keys,len(keys))

end()

index = hist.index
numpy_array = hist.to_numpy()
new_row = []
new_row.append(str(index[0]))
for a,val in enumerate(numpy_array[0]):
	new_row.append(val)

#new_row.append(numpy_array[0])
print(new_row)
end()
print(array)
new_price_history = []

pri(array)

end()
for a,val in enumerate(index):
	new_row = []
	new_row.append(str(val))
	#new_row = new_row+array[a]
	print(array[a])
	new_price_history.append(new_row)

pri(new_price_history)
end()

#hist2 = hist.values()
end()

end()
print(type(hist))
print(hist["0"])
end()

stock = yf.Ticker("MSFT")
hist = stock.history(period="5y")

import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame(hist)

# Convert to NumPy array
array = df.to_numpy()

pri(array)

end()
"""
print(hist)
import pandas as pd

# Sample DataFrame
df = pd.DataFrame(hist)

# Save to a JSON file
df.to_json('0test.json', orient='records')


save_file = "0test.json"
with open(save_file, 'w') as f:
	json.dump(hist, f, indent=2)
	print(str(a)+" of "+str(len(to_get)))
	print(f"Data saved to {save_file}")

print(data)
"""