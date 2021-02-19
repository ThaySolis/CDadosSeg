# Prática 2 - Parte 2: Análise de arquivos PE

## Parte 2.1

Este programa lê uma lista de arquivos PE (.exe) de um diretório e gera a lista de seções executáveis por arquivo.

Para usar esse script, invoque da seguinte maneira:

    python T2p2-1.py <diretório>
	
IMPORTANTE: é considerado que todos os arquivos no diretório informado sejam arquivos PE válidos. Se isso não for verdade, o script irá falhar.

## Parte 2.2

Este programa recebe como entrada dois arquivos PE (.exe) e os compara, imprimindo na saída padrão:
* quais seções são comuns a ambos os binários
* quais seções somente estão presentes no binário 1 
* quais seções somente estão presentes no binário 2

Para usar esse script, invoque da seguinte maneira:

    python T2p2-2.py <binario1> <binario2>
	
IMPORTANTE: é considerado que ambos os arquivos informados sejam arquivos PE válidos. O script também não aceita dois binários em caminhos diferentes, mas com o mesmo nome. Se essas condições não forem satisfeitas, o script irá falhar.