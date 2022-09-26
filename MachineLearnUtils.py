from re import X
from symbol import testlist_star_expr
from sklearn.model_selection import train_test_split
import pandas as pd



if __name__ == "__main__":

    dados = pd.read_csv(r"./arquivosTeste/Consumo_cerveja.csv", sep= ";")

    y= dados ["consumo"]
    X= dados [["temp_max", "chuva", "fds"]]
    
    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3, random_state= 42)
    
    
