# Terminal File Transfer
## Trabalho Final - MATA49
### Grupo:
- Felipe Carvalho Passos
- Douglas

O projeto trata de um sistema para depósito e recuperação de arquivos em servidores remotos.

No **modo de depósito**, o cliente é capaz de depositar um arquivo com qualquer extensão, informando também o nível de tolerância a falhas desejado.

O nível de tolerância dita a quantidade de cópias a serem feitas nos servidores satélites. Por exemplo, um arquivo com nível de tolerância 3 deve ser depositado em três servidores satélites.

OBS: A quantidade máxima de servidores satélites que podem ser abertos é informada na variável MAX_SATELLITE_INSTANCES do projeto file-satellite-server.

Toda vez que um arquivo é depositado, primeiro limpamos qualquer cópia pré existente nos servidores. Isso serve para garantir que o número de cópias esteja consistente com a última solicitação do cliente.

No **modo de recuperação**, o servidor principal retorna o arquivo do primeiro servidor satélite que o contém. Por exemplo, se um arquivo "file.txt" está armazenado em três servidores satélites diferentes, quando o servidor principal encontra a primeira cópia ele a retorna para o cliente e finaliza a execução. Caso não encontre o arquivo, informa ao cliente.