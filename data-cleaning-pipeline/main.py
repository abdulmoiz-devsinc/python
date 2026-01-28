from utils.ReadDataset import read_dataset
from utils.RemoveNulls import removeNulls
from utils.RemoveDuplicates import removeDuplicate

df=read_dataset('dataset/data.csv')
print("Dataset Info: ",df.info())
print("Dataset Shape: ",df.shape)
df=removeNulls(df)
df=removeDuplicate(df)



