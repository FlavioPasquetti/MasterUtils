from tkinter import Y
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import numpy as np
import pandas as pd
import seaborn as sns   
import scipy
import matplotlib.cm as cm


#---------------------------------------------------------------------------------------------
#PLOT PADRAO, LINHAS E PONTOS 2D 

class graficPlot():
    #Faltando: circulo e retangulo

    def __init__(self, X1 = [], Y1 = [], X2 = [], Y2 = [], X3 = [], Y3 = [], texts1 = [], texts2 = [], texts3 = [], \
        linewidth1 = 2, linewidth2 = 2, linewidth3 = 2, colorLine1 = "red", colorLine2 = "green", colorLine3 = "blue", \
        marker1 = [], marker2 = [], marker3 = [], xlabel = "", ylabel1 = "", ylabel2 = "", ylabel3 = "", \
        legendText1 = [], legendText2 = [], legendText3 = [], colorText1 = "red", colorText2 = "blue", colorText3 = "green", \
        colorgrondText1 = "Yellow", colorgrondText2 = "Yellow", colorgrondText3 = "Yellow", \
        xLim = None, y1Lim = None, y2Lim = None, y3Lim = None, legendLoc1 = "upper left", legendLoc2 = "upper right", legendLoc3 = "lower right", \
        xscale = "linear", y1Scale = "linear", y2Scale = "linear", y3Scale = "linear", \
        sizeText = 10, grid = True, textEffect = True, title = "", degrad = True, colorList = False, \
        circle = False, circlePos = [], circleColor = "black", circleFill = None, circleTrans = 0.75, circlePlot = 1, \
        rect = False, rectPos = [], rectColor = "black", rectFill = None, rectTrans = 0.75, rectPlot = 1, \
        addLogo = False, pathLogo = "", backgroundImg = False, pathImg = ""):
        
        self.X1 = X1                    #Plots primeiro eixo
        self.Y1 = Y1                    #Plots primeiro eixo
        self.X2 = X2                    #Plots segundo eixo
        self.Y2 = Y2                    #Plots segundo eixo
        self.X3 = X3                    #Plots terceiro eixo
        self.Y3 = Y3                    #Plots terceiro eixo

        self.texts1 = texts1            #Plot de textos exe: ax.text(x, y, "texto")
        self.texts2 = texts2            #Plot de textos exe: ax.text(x, y, "texto")
        self.texts3 = texts3            #Plot de textos exe: ax.text(x, y, "texto")

        self.colorText1 = colorText1    #Cor das Text 1
        self.colorText2 = colorText2    #Cor das Text 2
        self.colorText3 = colorText3    #Cor das Text 3 

        self.colorgrondText1 = colorgrondText1    #Cor ao redor das Text 1
        self.colorgrondText2 = colorgrondText2    #Cor ao redor das Text 2
        self.colorgrondText3 = colorgrondText3    #Cor ao redor das Text 3 

        self.legendText1 = legendText1  #Legenda dos plots 1
        self.legendText2 = legendText2  #Legenda dos plots 2
        self.legendText3 = legendText3  #Legenda dos plots 3

        self.linewidth1 = linewidth1    #Grossura da plots 1 
        self.linewidth2 = linewidth2    #Grossura da plots 2 
        self.linewidth3 = linewidth3    #Grossura da plots 3

        self.colorLine1 = colorLine1    #Cor das plots 1
        self.colorLine2 = colorLine2    #Cor das plots 2
        self.colorLine3 = colorLine3    #Cor das plots 3 

        self.marker1 = marker1          #Tipo de Marcador plots 1
        self.marker2 = marker2          #Tipo de Marcador plots 2
        self.marker3 = marker3          #Tipo de Marcador plots 3

        self.xlabel = xlabel            #Titulo do Eixo X
        self.ylabel1 = ylabel1          #Titulo do Eixo Y1        
        self.ylabel2 = ylabel2          #Titulo do Eixo Y2
        self.ylabel3 = ylabel3          #Titulo do Eixo Y3

        self.xLim = xLim                #Limites do Eixo X
        self.y1Lim = y1Lim              #Limites do Eixo Y1        
        self.y2Lim = y2Lim              #Limites do Eixo Y2
        self.y3Lim = y3Lim              #Limites do Eixo Y3

        self.xscale = xscale            #linear, log, symlog, logit
        self.y1Scale = y1Scale          #linear, log, symlog, logit
        self.y2Scale = y2Scale          #linear, log, symlog, logit
        self.y3Scale = y3Scale          #linear, log, symlog, logit

        self.legendLoc1 = legendLoc1    #Localizacao da legenda - best, upper right, upper left, lower left, lower right, right, center right, lower center, upper center, center
        self.legendLoc2 = legendLoc2    #Localizacao da legenda - best, upper right, upper left, lower left, lower right, right, center right, lower center, upper center, center
        self.legendLoc3 = legendLoc3    #Localizacao da legenda - best, upper right, upper left, lower left, lower right, right, center right, lower center, upper center, center 
        
        self.sizeText = sizeText        #Tamanho do text
        self.grid = grid                #Ativa Grid
        self.textEffect = textEffect    #Efeito no Texto
        self.title = title              #Titulo do Grafico
        self.degrad = degrad			#Degrade nos plots com a mesma cor
        self.colorList = colorList      #Define as cores de cada ponto 

        self.circle = circle
        self.circlePos = circlePos
        self.circleColor = circleColor
        self.circleFill = circleFill
        self.circleTrans = circleTrans
        self.circlePlot = circlePlot

        self.rect = rect
        self.rectPos = rectPos
        self.rectColor = rectColor
        self.rectFill = rectFill
        self.rectTrans = rectTrans
        self.rectPlot = rectPlot

        self.addLogo = addLogo
        self.pathLogo = pathLogo

        self.backgroundImg = backgroundImg
        self.pathImg = pathImg

        self.configPlot()


    def plotDef(self, X1 = None, Y1 = None, X2 = None, Y2 = None, X3 = None, Y3 = None, texts1 = None, texts2 = None, texts3 = None, \
        linewidth1 = None, linewidth2 = None, linewidth3 = None, colorLine1 = None, colorLine2 = None, colorLine3 = None, \
        marker1 = None, marker2 = None, marker3 = None, xlabel = None, ylabel1 = None, ylabel2 = None, ylabel3 = None, \
        legendText1 = None, legendText2 = None, legendText3 = None, colorText1 = None, colorText2 = None, colorText3 = None, \
        colorgrondText1 = None, colorgrondText2 = None, colorgrondText3 = None, \
        xLim = None, y1Lim = None, y2Lim = None, y3Lim = None, \
        legendLoc1 = None, legendLoc2 = None, legendLoc3 = None, \
        xscale = None, y1Scale = None, y2Scale = None, y3Scale = None, \
        sizeText = None, grid = None, textEffect = None, title = "", degrad = None, colorList = None, \
        circle = None, circlePos = None, circleColor = None, circleFill = None, circleTrans = None, circlePlot = None, \
        rect = None, rectPos = None, rectColor = None, rectFill = None, rectTrans = None, rectPlot = None, \
        addLogo = False, pathLogo = "", backgroundImg = False, pathImg = ""):

        if (X1 != None): self.X1 = X1                    #Plots primeiro eixo
        if (Y1 != None): self.Y1 = Y1                    #Plots primeiro eixo
        if (X2 != None): self.X2 = X2                    #Plots segundo eixo
        if (Y2 != None): self.Y2 = Y2                    #Plots segundo eixo
        if (X3 != None): self.X3 = X3                    #Plots terceiro eixo
        if (Y3 != None): self.Y3 = Y3                    #Plots terceiro eixo

        if (texts1 != None): self.texts1 = texts1        #Plot de textos exe: ax.text(x, y, "texto")
        if (texts2 != None): self.texts2 = texts2        #Plot de textos exe: ax.text(x, y, "texto")
        if (texts3 != None): self.texts3 = texts3        #Plot de textos exe: ax.text(x, y, "texto")

        if (colorText1 != None): self.colorText1 = colorText1    #Cor das Text 1
        if (colorText2 != None): self.colorText2 = colorText2    #Cor das Text 2
        if (colorText3 != None): self.colorText3 = colorText3    #Cor das Text 3 

        if (colorgrondText1 != None): self.colorgrondText1 = colorgrondText1    #Cor ao redor das Text 1
        if (colorgrondText2 != None): self.colorgrondText2 = colorgrondText2    #Cor ao redor das Text 2
        if (colorgrondText3 != None): self.colorgrondText3 = colorgrondText3    #Cor ao redor das Text 3 

        if (legendText1 != None): self.legendText1 = legendText1  #Legenda dos plots 1
        if (legendText2 != None): self.legendText2 = legendText2  #Legenda dos plots 2
        if (legendText3 != None): self.legendText3 = legendText3  #Legenda dos plots 3

        if (linewidth1 != None): self.linewidth1 = linewidth1    #Grossura da plots 1 
        if (linewidth2 != None): self.linewidth2 = linewidth2    #Grossura da plots 2 
        if (linewidth3 != None): self.linewidth3 = linewidth3    #Grossura da plots 3

        if (colorLine1 != None): self.colorLine1 = colorLine1    #Cor das plots 1
        if (colorLine2 != None): self.colorLine2 = colorLine2    #Cor das plots 2
        if (colorLine3 != None): self.colorLine3 = colorLine3    #Cor das plots 3 

        if (marker1 != None): self.marker1 = marker1          #Tipo de Marcador plots 1
        if (marker2 != None): self.marker2 = marker2          #Tipo de Marcador plots 2
        if (marker3 != None): self.marker3 = marker3          #Tipo de Marcador plots 3

        if (xlabel   != None): self.xlabel = xlabel           #Titulo do Eixo X
        if (ylabel1 != None): self.ylabel1 = ylabel1          #Titulo do Eixo Y1        
        if (ylabel2 != None): self.ylabel2 = ylabel2          #Titulo do Eixo Y2
        if (ylabel3 != None): self.ylabel2 = ylabel3          #Titulo do Eixo Y3

        if (xLim   != None): self.xLim = xLim               #Limites do Eixo X
        if (y1Lim != None): self.y1Lim = y1Lim              #Limites do Eixo Y1        
        if (y2Lim != None): self.y2Lim = y2Lim              #Limites do Eixo Y2
        if (y3Lim != None): self.y3Lim = y3Lim              #Limites do Eixo Y3

        if (xscale   != None): self.xscale = xscale           #linear, log, symlog, logit
        if (y1Scale != None): self.y1Scale = y1Scale          #linear, log, symlog, logit
        if (y2Scale != None): self.y2Scale = y2Scale          #linear, log, symlog, logit
        if (y3Scale != None): self.y3Scale = y3Scale          #linear, log, symlog, logit

        if (legendLoc1 != None): self.legendLoc1 = legendLoc1   #Localizacao da legenda
        if (legendLoc2 != None): self.legendLoc2 = legendLoc2   #Localizacao da legenda
        if (legendLoc3 != None): self.legendLoc3 = legendLoc3   #Localizacao da legenda
        
        if (sizeText != None): self.sizeText = sizeText         #Tamanho do text
        if (grid != None): self.grid = grid                     #Ativa Grid
        if (textEffect != None): self.textEffect = textEffect   #Efeito no Texto
        if (title != None): self.title = title                  #Titulo do Grafico
        if (degrad != None): self.degrad = degrad
        if (colorList != None): self.colorList = colorList      #Define as cores de cada ponto

        if (circle != None): self.circle = circle
        if (circlePos != None): self.circlePos = circlePos
        if (circleColor != None): self.circleColor = circleColor
        if (circleFill != None): self.circleFill = circleFill
        if (circleTrans != None): self.circleTrans = circleTrans
        if (circlePlot != None): self.circlePlot = circlePlot

        if (rect != None): self.rect = rect
        if (rectPos != None): self.rectPos = rectPos
        if (rectColor != None): self.rectColor = rectColor
        if (rectFill != None): self.rectFill = rectFill
        if (rectTrans != None): self.rectTrans = rectTrans
        if (rectPlot != None): self.rectPlot = rectPlot

        if (addLogo != None): self.addLogo = addLogo
        if (pathLogo != None): self.pathLogo = pathLogo
        if (backgroundImg != None): self.backgroundImg = backgroundImg
        if (pathImg != None): self.pathImg = pathImg


    def configPlot (self):

        self.fig, self.graphicHost = plt.subplots()

        #CONFIG PLOT 01 
        if (len(self.X1) > 0):

            qlines = len(self.X1)
            transpAdd = 0.80/qlines
            nplot = 0

            for X in self.X1:
                nplot += 1 
                nX = np.array(X)
                nY = np.array(self.Y1[nplot-1])

                marker = "-"
                if (len(self.marker1) >= nplot):
                    marker = self.marker1[nplot-1]

                legend = ""
                if (len(self.legendText1) >= nplot):
                    legend = self.legendText1[nplot-1]

                colorTransp = 0.20 + transpAdd*nplot
                if (not self.degrad): colorTransp = 1

                colorDef = self.colorLine1
                if (self.colorList): colorDef = self.colorLine1[nplot-1]

                self.graphicHost.plot(nX, nY, marker, lw = self.linewidth1, label=legend, color = colorDef, alpha = colorTransp)

            self.graphicHost.legend(loc=self.legendLoc1)
            if (len(self.legendText1) == 0): self.graphicHost.get_legend().remove()
            self.graphicHost.yaxis.label.set_color(colorDef)
            self.graphicHost.set(xlim = self.xLim, ylim = self.y1Lim, xlabel = self.xlabel, ylabel = self.ylabel1, title = self.title)
            
            if (self.xLim != None): 
                self.graphicHost.set_xlim(self.xLim)
            if (self.y1Lim != None): 
                self.graphicHost.set_ylim(self.y1Lim)

            for text in self.texts1:
                textInsert = self.graphicHost.text (text[0], text[1], text[2], color = self.colorText1, ha = "center", va = "center", rotation = 0, size = self.sizeText)        
                textInsert.set_path_effects([path_effects.Stroke(linewidth = self.sizeText/3, foreground=self.colorgrondText1), path_effects.Normal()])


            #CONFIGURANDO PLOT2
            if (len(self.X2) > 0):
                
                self.graphicTwo = self.graphicHost.twinx()

                qlines = len(self.X2)
                transpAdd = 0.80/qlines
                nplot = 0

                for X in self.X2:
                    nplot += 1 
                    nX = np.array(X)
                    nY = np.array(self.Y2[nplot-1])

                    marker = "-"
                    if (len(self.marker2) >= nplot):
                        marker = self.marker2[nplot-1]

                    legend = ""
                    if (len(self.legendText2) >= nplot):
                        legend = self.legendText2[nplot-1]

                    colorTransp = 0.20 + transpAdd*nplot
                    if (not self.degrad): colorTransp = 1

                    colorDef = self.colorLine2
                    if (self.colorList): colorDef = self.colorLine2[nplot-1]

                    self.graphicTwo.plot(nX, nY, marker, lw = self.linewidth2, label=legend, color = colorDef, alpha = colorTransp)

                self.graphicTwo.yaxis.label.set_color(colorDef)
                self.graphicTwo.legend(loc=self.legendLoc2)
                if (len(self.legendText2) == 0): self.graphicTwo.get_legend().remove()
                self.graphicTwo.set_ylabel(self.ylabel2)

                if (self.y2Lim != None): self.graphicTwo.set_ylim(self.y2Lim)

                for text in self.texts2:
                    textInsert = self.graphicHost.text (text[0], text[1], text[2], color = self.colorText2, ha = "center", va = "center", rotation = 0, size = self.sizeText)        
                    textInsert.set_path_effects([path_effects.Stroke(linewidth = self.sizeText/3, foreground=self.colorgrondText2), path_effects.Normal()])

            #CONFIGURANDO PLOT3
            if (len(self.X3) > 0):
                
                self.graphicThree = self.graphicHost.twinx()

                qlines = len(self.X3)
                transpAdd = 0.80/qlines
                nplot = 0

                for X in self.X3:
                    nplot += 1 
                    nX = np.array(X)
                    nY = np.array(self.Y3[nplot-1])

                    marker = "-"
                    if (len(self.marker3) >= nplot):
                        marker = self.marker3[nplot-1]

                    legend = ""
                    if (len(self.legendText3) >= nplot):
                        legend = self.legendText3[nplot-1]

                    colorTransp = 0.20 + transpAdd*nplot
                    if (not self.degrad): colorTransp = 1

                    colorDef = self.colorLine3
                    if (self.colorList): colorDef = self.colorLine3[nplot-1]

                    self.graphicThree.plot(nX, nY, marker, lw = self.linewidth3, label=legend, color = colorDef, alpha = colorTransp)

                self.graphicThree.yaxis.label.set_color(colorDef)
                self.graphicThree.legend(loc=self.legendLoc3)
                if (len(self.legendText3) == 0): self.graphicThree.get_legend().remove()
                self.graphicThree.set_ylabel(self.ylabel3)
                self.graphicThree.spines['right'].set_position(('outward', 60))
                #self.graphicThree.xaxis.set_ticks([])

                if (self.y3Lim != None): self.graphicThree.set_ylim(self.y3Lim)

                for text in self.texts3:
                    textInsert = self.graphicHost.text (text[0], text[1], text[2], color = self.colorText3, ha = "center", va = "center", rotation = 0, size = self.sizeText)        
                    textInsert.set_path_effects([path_effects.Stroke(linewidth = self.sizeText/3, foreground=self.colorgrondText3), path_effects.Normal()])

    
            #ADICIONANDO LOGO
            if (self.addLogo):
                plt.rcParams["figure.figsize"] = [3,3]
                plt.rcParams["figure.autolayout"] = True
                im = plt.imread(self.pathLogo)

                newax = self.fig.add_axes([0.80,0.80,0.15,0.15], anchor='NE', zorder=1)
                newax.imshow(im)
                newax.axis('off')

            #ADICIONANDO IMAGEM DE FUNDO
            if (self.backgroundImg):
                bg = plt.imread(self.pathImg)
                bg = self.graphicHost.imshow(bg, extent=[self.xLim[0],self.xLim[1], self.y1Lim[0], self.y1Lim[1]])  


            #CONFIGURANCAO GERAL
            #self.graphicHost.axis('tight')
            self.fig.tight_layout()

            plt.grid(visible = self.grid)


    def show(self):
        plt.show()

    def addLegend (self, legend, marker, colorDef, colorTransp = 1.0):
        self.graphicHost.plot(0.0, 0.0, marker, lw = 0, label=legend, color = colorDef, alpha = colorTransp)
        self.graphicHost.legend(loc=self.legendLoc1)

#---------------------------------------------------------------------------------------------
#PLOT HISTOGRAMA

def dfPlot (dataFrame, xValue, yValue= None, zValue= None, xName= "", yName= "", title= "", kind= "count", aspect= None, palette= "GnBu_d", grid= False, bins= None, orient= "h", style= None, size_inches= None):

    # kinds -> count, cumulative, distplot, boxplot
    # style -> white, dark, whitegrid, darkgrid, ticks
    # palette -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r

    #Variaveis globais ---------------
    if (style != None):
        sns.set_style(style)

    if (palette != None):
        sns.set_palette(palette)
        
    if title != "":
        plt.title(title)

    plt.grid(grid)

    if xName != "":
        plt.xlabel(xName)
        
    if yName != "": 
        plt.ylabel(yName)

    #Definindo o plot -------------
    if (kind == "count"):
        graph= sns.catplot(x = xValue, data = dataFrame, 
            kind=kind, 
            aspect=aspect,
            order = dataFrame[xValue].value_counts().index)
        
    elif (kind == "distplot"):
        
        graph= sns.distplot (dataFrame[xValue], bins= bins, kde= False)
        
    elif (kind == "cumulative"):
        
        graph= sns.distplot (dataFrame[xValue], hist_kws = {"cumulative": True}, kde_kws = {"cumulative": True}, bins= bins)
        
    elif (kind == "boxplot"):
    
        graph= sns.boxplot ( x= xValue, y= yValue, data= dataFrame, orient= orient)
        
    elif (kind == "pairplot"):
        #xValue e yValue podem ser uma lista 
        graph= sns.pairplot (dataFrame, y_vars= yValue, x_vars=xValue)
        
    elif (kind == "jointplot"):
        
        graph= sns.jointplot (x= xValue, y= yValue, data= dataFrame, kind= "reg")

    elif (kind == "lmplot"):
        
        graph= sns.lmplot (x= xValue, y= yValue, data= dataFrame, col= zValue)

    elif (kind == "scatterplot"):

        graph= sns.scatterplot(x= xValue, y= yValue)

    elif (kind == "imshow"):
        #xValue deve ser o intervalo do eixo X - ex: [1.0, 2.0]
        #yValue deve ser o intervalo do eixo Y - ex: [0.1, 0.5]
        graph= plt.imshow(list(dataFrame.values), origin= "lower", cmap= cm.rainbow, interpolation= "quadric", extent= (xValue[0], xValue[1], yValue[0], yValue[1]))
        
    elif (kind == "relev"):
        #zValue deve ter a dimensao X x Y .. pois define o valor da altura para cada ponto 
        graph = plt.contour(df[xValue].values, df[yValue].values, list(df[zValue].values), colors= "k", linewidth= 1.5)
        plt.clabel (graph, inline= True, fontsize= 15.0, inline_spacing = 10)

    if size_inches != None:
        graph.figure.set_size_inches(size_inches[0], size_inches[1])

    plt.show()





if (__name__ == "__main__"):    

    teste_graficPlot = False
    teste_histPlot = True

    if (teste_graficPlot):

        valoresX1= [[1,2,3],[2,3,4]]
        valoresY1= [[2,3,4],[3,4,5]]
        valoresX2= [[3,7,9],[2,3,4]]
        valoresY2= [[4,7,10],[3,4,5]]
        valoresX3= [[5,7,12],[2,3,4]]
        valoresY3= [[6,7,13],[3,4,5]]

        texts1 = [[1,2,"valor1"], [2,3,"valor2"]]

        grafico = graficPlot(X1 = valoresX1, Y1 = valoresY1, X2 = valoresX2, Y2 = valoresY2, X3 = valoresX3, Y3 = valoresY3, texts1 = texts1, texts2 = [], texts3 = [], 
        linewidth1 = 2, linewidth2 = 2, linewidth3 = 2, colorLine1 = "red", colorLine2 = "green", colorLine3 = "blue", 
        marker1 = ["o", "^"], marker2 = [], marker3 = [], xlabel = "testeLabelX", ylabel1 = "testeLabel1", ylabel2 = "", ylabel3 = "", 
        legendText1 = ["valores1", "valores2"], legendText2 = [], legendText3 = [], colorText1 = "red", colorText2 = "blue", colorText3 = "green", 
        colorgrondText1 = "Yellow", colorgrondText2 = "Yellow", colorgrondText3 = "Yellow", 
        xLim = [1,10], y1Lim = [2,9], y2Lim = None, y3Lim = None, legendLoc1 = "upper left", legendLoc2 = "upper right", legendLoc3 = "lower right", 
        xscale = "linear", y1Scale = "linear", y2Scale = "linear", y3Scale = "linear", 
        sizeText = 10, grid = True, textEffect = True, title = "", degrad = True, colorList = False, 
        circle = False, circlePos = [], circleColor = "black", circleFill = None, circleTrans = 0.75, circlePlot = 1, 
        rect = False, rectPos = [], rectColor = "black", rectFill = None, rectTrans = 0.75, rectPlot = 1, 
        addLogo = False, pathLogo = "", backgroundImg = False, pathImg = "")

        grafico.show()

    if (teste_histPlot):

        df= pd.read_csv(r"./arquivosTeste/Curso de Estatística/dados.csv")
        print (df)
        
        #histPlot(df, xLabel1= "Frequência", yLabel1="Ocorrencias", title= "Teste Titulo", kind= "count", aspect= 3, palette= "GnBu_d", grid= True)

        #histPlot(df, xValue= "Idade", yName="Ocorrencias", title= "Teste Titulo", kind= "cumulative", aspect= 2, palette= "GnBu_d", grid= True)
        histPlot(df, xValue= "Anos de Estudo", yValue= "Sexo", kind= "boxplot")


