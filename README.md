# Projeto  : Forcria

### O objetivo deste projeto consiste em desenvolver um jogador de forca que possua alto grau de acerto, mesmo com apenas cinco vidas, através da utilização de uma estratégia baseada na obtenção de informações adicionais por meio de palpites. Essa estratégia consiste em analisar a frequência das letras nas palavras elegíveis para chute, visando obter o maior número possível de informações sobre a palavra a ser adivinhada.

### Para tanto, a cada chute realizado, é feita uma análise da frequência de cada letra nas palavras elegíveis para chute, a fim de identificar qual letra apresenta maior frequência dentre as possibilidades. A letra selecionada é, então, chutada e verificado se ela está presente na palavra a ser adivinhada. Em caso positivo, a lista de palavras elegíveis para chute é atualizada e o processo de análise e chute é repetido. Em caso negativo, o jogador perde uma vida e o processo é reiniciado. O objetivo final é adivinhar a palavra dentro das cinco vidas disponíveis.