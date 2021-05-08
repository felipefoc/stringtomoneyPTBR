# String to Extense

- Feito somento com Python


## Recebe um arquivo.txt e retorna outro arquivo com os valores por extenso e em reais.

- Os valores devem ser separados por , com no máximo 11 digitos.
- 9 digitos antes da virgula, 2 digitos após
- Ex: XXXXXX,XX


Como rodar a aplicação
-------------

No terminal, clone o projeto
```bash
$ git clone https://github.com/felipefoc/stringtomoneyPTBR.git
```
Entre na pasta do projeto
```bash
$ cd stringtomoneyPTBR
```
Execute o comando informando o caminho do arquivo e o destino/nome da saida do arquivo
```bash
$ python main.py -i caminho/para/o/arquivo.txt -o nomedoarquivo.txt
```
ou
```bash
$ main.py -i caminho/para/o/arquivo.txt -o caminho/do/aquivoondeserasalvo/nomedoarquivo.txt
```

Para rodar os testes
-------------
```bash
$ python test.py
```