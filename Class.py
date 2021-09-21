class Time:
    def _init_(self, pontos, gols, partidas, gols_contra):
        self.pontos = pontos            
        self.gols = gols            
        self.gols_contra = gols_contra            
        self.partidas = partidas
   

    def calcularMediaGolsPorPartida(gols, partidas):
        gols = gols
        partidas = partidas
        mediaGols = gols/partidas
        return mediaGols

    def calcularMediaPontosPorPartida(pontos, partidas):
        pontos = pontos
        partidas = partidas
        mediaPontos = pontos/partidas
        return mediaPontos

    def calcularSaldoGolsTime(gols, gols_contra):
        gols = gols
        gols_contra = gols_contra
        mediaGols = gols - gols_contra
        return mediaGols

    def calcularSaldoGolsTime(self, pontos, gols, gols_contra):
        if (gols > gols_contra):
            resultado = 'V'

        resultado = 'D'
        self.pontos = pontos            
        self.gols = gols            
        self.gols_contra = gols_contra            

        return resultado

    def setStatusTime(self, gols, gols_contra):
        if (gols > gols_contra):
            self.pontos = self.pontos + 3
        elif (gols_contra == gols):
            self.pontos = self.pontos + 1
        
        return [
                self.partidas, 
                self.pontos, 
                self.calcularMediaGolsPorPartida(self.gols, self.partidas), 
                self.calcularMediaPontosPorPartida(self.gols, self.partidas),  
            ]