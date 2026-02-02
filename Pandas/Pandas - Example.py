import pandas as pd
mydataset = {
    'cars' : ["BMW","Volvo"], 'passings' : [3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)