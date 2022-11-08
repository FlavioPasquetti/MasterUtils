from scipy.stats import binom, poisson, norm, ranksums
from statsmodels.stats.weightstats import zconfint, DescrStatsW

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Binomial

def Probabilidade_DistribBinomial (k, n, p, cumulativo= False):
    
    #p= probabilidade de sucesso evento unico
    #q= (1-p) = probabilidade de fracasso evento unico
    #n= numero de eventos estudados
    #k= numero de eventos desejados que tenham sucesso (pode ser uma lista)

    if (cumulativo):
        return binom.cdf(k,n,p)

    else:
        return binom.pmf(k,n,p)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Poisson

def Probabilidade_DistribPoisson (k, u):

    #e= constante= 2.718281828459045
    #u= representa o numero medio de ocorrencias em um determinado intervalo de tempo ou espaco
    #k= numero de sucessos no intervalo desejado

    return poisson.pmf(k, u)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Normal

def Probabilidade_DistribNormal (x, o, u, typeP= "cumulative"):

    #x= variavel normal
    #o= desvio padrao
    #u= media
    #typeP= cumulative, between, rest

    if (typeP== "cumulative"):
        Z= (x - u)/o

        return norm.cdf(Z)

    elif (typeP== "between"):
        Zinf= (x[0] - u)/o
        Zsup= (x[1] - u)/o

        return norm.cdf(Zsup) - norm.cdf(Zinf)

    elif (typeP== "rest"):
        Z= (x - u)/o

        return 1 - norm.cdf(Z)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Intervalo de Confianca Normal

def intervaloConfianca_Norm(significancia, media_amostral, sigma):

    #sigma= desvio padrao/ raiz(quantidade Amostra)
    
    return norm.interval (alpha= significancia, loc= media_amostral, scale= sigma)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Intervalo de Confianca Z - Amostras Grandes

def intervaloConfianca_Zconf(df, significancia= 0.05):

    return zconfint(df, alpha= significancia)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Intervalo de Confianca T - Amostras Pequenas

def intervaloConfianca_Tconf(df, significancia= 0.05):

    df_DescStats= DescrStatsW(df)
    return df_DescStats.tconfint_mean(alpha= significancia)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Quantidade Amostra

def tamanhoAmostra (z, e, o):

    #z= variavel normal padronizada - ex: caso queira 95% de confianca Z= norm.ppf(0.5 + (0.95/2))
    #o= desvio padrao populacional ou amostral (s) caso seja desconhecido o desvio padrao
    #e= erro inferencial - valor que pode ser variada a variavel normal ex: R$3000 +- 100.. o 100 seria o erro inferencial

    return (z*(o/e))**2

def tamanhoAmostra (N, z, o, e):

    #N= Tamanho da populacao
    #z= variavel normal padronizada - ex: caso queira 95% de confianca Z= norm.ppf(0.5 + (0.95/2))
    #o= desvio padrao populacional ou amostral (s) caso seja desconhecido o desvio padrao
    #e= erro inferencial - valor que pode ser variada a variavel normal ex: R$3000 +- 100.. o 100 seria o erro inferencial

    return ((z**2)*(o**2)*N) / ( ((z**2)*(o**2)) + (e**2)*(N-1) )




if __name__ == "__main__":

    teste_Distribuicoes= False

    if (teste_Distribuicoes):

        k= [5,8]
        n= 10
        p= 1/4

        result= Probabilidade_DistribBinomial (k, n, p)
        print (result)

        u= 20
        k= 15

        result= Probabilidade_DistribPoisson (k, u)
        print (result)
        
        x= 1.8
        u= 1.7
        o= 0.1

        result= Probabilidade_DistribNormal(x, o, u)
        print (result)
        