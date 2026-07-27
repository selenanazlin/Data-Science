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
