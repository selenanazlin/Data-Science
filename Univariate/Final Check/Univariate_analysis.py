import pandas as pd
import numpy as np

class Univariate():
    def QuanQual(dataset):
    
        Qual = []
        Quan = []
        for columnName in dataset.columns:
            if(dataset[columnName].dtype == 'O'):
               Qual.append(columnName)
            else:
               Quan.append(columnName)
        return Quan,Qual
        
        # Percentile
        
    def descriptive(dataset,Quan):
        descriptive=pd.DataFrame(index = ["Mean","Median","Mode","Q1:25%","Q2:50%",
                                    "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=Quan)
    
        for ColumnName in Quan:
             descriptive[ColumnName]["Mean"]=dataset[ColumnName].mean()
             descriptive[ColumnName]["Median"]=dataset[ColumnName].median()
             descriptive[ColumnName]["Mode"]=dataset[ColumnName].mode()[0]       
             descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
             descriptive[ColumnName]["Q2:50%"]=dataset.describe()[ColumnName]["50%"]
             descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]
             descriptive[ColumnName]["99%"]=np.percentile(dataset[ColumnName],99)
             descriptive[ColumnName]["Q4:100%"]=dataset.describe()[ColumnName]["max"]
            # descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
             #descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]              
             descriptive[ColumnName]["IQR"]=descriptive[ColumnName]["Q3:75%"] - descriptive[ColumnName]["Q1:25%"]
             descriptive[ColumnName]["1.5rule"]= 1.5 * descriptive[ColumnName]["IQR"] 
             descriptive[ColumnName]["Lesser"]=descriptive[ColumnName]["Q1:25%"] - descriptive[ColumnName]["1.5rule"]
             descriptive[ColumnName]["Greater"]=descriptive[ColumnName]["Q3:75%"] + descriptive[ColumnName]["1.5rule"]
             descriptive[ColumnName]["Min"]=dataset[ColumnName].min()
             descriptive[ColumnName]["Max"]=dataset[ColumnName].max()
        

             return descriptive

# frequency
    def freqTable(ColumnName, dataset):
    
        freqTable = pd.DataFrame(columns = ["Unique_values", "Frequency", "Relative_Frequency", "Cumulative_Frequency"])
        
        freqTable["Unique_values"] = dataset [ColumnName].value_counts().index
        freqTable["Frequency"] = dataset [ColumnName].value_counts().values
        freqTable["Relative_Frequency"] = (freqTable["Frequency"]/103)
        freqTable["Cumulative_Frequency"] = freqTable ["Relative_Frequency"].cumsum()
    
        return freqTable        



