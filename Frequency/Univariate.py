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
    def Univariet(dataset,Quan)
    descriptive=pd.DataFrame(index=["Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%"],columns=Quan)
    
        for ColumnName in Quan:
                
            descriptive[ColumnName]["Q1:25%"]=dataset.describe()[ColumnName]["25%"]
            descriptive[ColumnName]["Q2:50%"]=dataset.describe()[ColumnName]["50%"]
            descriptive[ColumnName]["Q3:75%"]=dataset.describe()[ColumnName]["75%"]
            descriptive[ColumnName]["99%"]=np.percentile(dataset[ColumnName],99)
            descriptive[ColumnName]["Q4:100%"]=dataset.describe()[ColumnName]["max"]
        
