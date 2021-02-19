# Ciência de Dados - ci1030-ERE2

## Detalhamento do projeto da disciplina

1. Dataset escolhido (tema): UNSW-NB15_1.csv, UNSW-NB15_2.csv, UNSW-NB15_3.csv e UNSW-NB15_4.csv (tráfego de rede)
2. Link para download: https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/
3. Campos/atributos do seu dataset: 
 - srcip - Endereço IP de origem
 - sport - Número da porta de origem
 - dstip - Endereço IP de destino
 - dsport - Número da porta de destino
 - proto - Protocolo de transporte (camada 4)
 - state - Indica o estado do protocolo de transporte: ACC, CLO, CON, ECO, ECR, FIN, INT, MAS, PAR, REQ, RST, TST, TXD, URH, URN, e (-) se não tiver estado.
 - dur - Duração total do registro
 - sbytes - Bytes de transação da origem para o destino
 - dbytes - Bytes de transação do destino para a origem
 - sttl - Valor do time to live (TTL, saltos) da origem para o destino
 - dttl - Valor do time to live (TTL, saltos) do destino para a origem
 - sloss - Pacotes da origem retransmitidos ou descartados
 - dloss - Pacotes do destino retransmitidos ou descartados
 - service - Serviço (camada 7): http, ftp, smtp, ssh, dns, ftp-data ,irc e (-) se não for um serviço muito usado
 - Sload - Bits por segundo da origem
 - Dload - Bits por segundo do destino
 - Spkts - Contagem de pacotes da origem para o destino
 - Dpkts - Contagem de pacotes do destino para a origem
 - swin - Tamanho de janela TCP anunciado pela origem
 - dwin - Tamanho de janela TCP anunciado pelo destino
 - stcpb - Número de sequência TCP inicial da origem
 - dtcpb - Número de sequência TCP inicial do destino
 - smeansz - Tamanho médio do pacote transmitido pela origem
 - dmeansz - Tamanho médio do pacote transmitido pelo destino.
 - trans_depth - Representa a profundidade de pipeline dentro da conexão de transação http request/response
 - res_bdy_len - Tamanho real do conteúdo não compactado dos dados transferidos do serviço http do servidor.
 - Sjit - Jitter da origem (mSec)
 - Djit - Jitter do destino (mSec)
 - Stime - Tempo inicial de registro
 - Ltime - Tempo final de registro
 - Sintpkt - Tempo entre pacotes recebidos na origem (mSec)
 - Dintpkt - Tempo entre pacotes recebidos no destinom (mSec)
 - tcprtt - Tempo total de estabelecimento da conexão TCP (soma de “synack” e “ackdat”).
 - synack - Tempo entre os pacotes SYN e SYN_ACK durante o estabelecimento da conexão TCP.
 - ackdat - Tempo entre os pacotes SYN_ACK e ACK durante o estabelecimento da conexão TCP.
 - is_sm_ips_ports - Se o endereço de IP de origem (1) e destino (3) forem iguais e os números de porta (2) (4) forem iguais, então esta variável recebe o valor 1, senão 0
 - ct_state_ttl - Número de cada estado (6) de acordo com um âmbito específico de valores para o time to live da origem/destino (10) (11).
 - ct_flw_http_mthd - Número de fluxos que tem métodos tais como Get e Post no serviço http.
 - is_ftp_login - Se a sessão FTP é acessada por usuário e senha, então 1, senão 0.
 - ct_ftp_cmd - Número de fluxos que tem um comando na sessão FTP.
 - ct_srv_src - Número de conexões que contém o mesmo serviço (14) e endereço de origem (1) em 100 conexões de acordo com o last time (30).
 - ct_srv_dst - Número de conexões que contém o mesmo serviço (14) e endereço de destino (3) em 100 conexões de acordo com o last time (30).
 - ct_dst_ltm - Número de conexões com o mesmo endereço de destino (3) em 100 conexões de acordo com o last time (30).
 - ct_src_ ltm - Número de conexões com o mesmo endereço de origem (1) em 100 conexões de acordo com o last time (30).
 - ct_src_dport_ltm - Número de conexões com o mesmo endereço de origem (1) e a porta de destino (4) em 100 conexões de acordo com o last time (30).
 - ct_dst_sport_ltm - Número de conexões com o mesmo endereço de destino (3) e a porta de origem (2) em 100 conexões de acordo com o last time (30).
 - ct_dst_src_ltm - Número de conexões com o mesmo endereço de origem (1) e destino (3) em 100 conexões de acordo com o last time (30).
 - attack_cat - O nome de cada categoria de ataque. Neste data set, nove categorias: Fuzzers, Analysis, Backdoors, DoS Exploits, Generic, Reconnaissance, Shellcode e Worms
 - Label - 0 para registros normais e 1 para registros de ataque
