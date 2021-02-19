# Prática 2 - Parte 1: Análise de APKs

Este programa lê uma lista de arquivos AndroidManifest.xml (extraídos de APKs) de um diretório e gera:
* uma lista de permissões de cada APK
* uma lista de permissões únicas de cada APK
* uma lista de permissões comuns a todas as APKs analisadas

Para usar esse script, invoque da seguinte maneira:

    python T2p1.py <diretório>

IMPORTANTE: o nome dos arquivos xml deve seguir o seguinte padrão: AndroidManifest_<nome_do_APK>.xml. É considerado que todos os arquivos no diretório informado sejam arquivos AndroidManifest válidos. Se isso não for verdade, o script irá falhar.