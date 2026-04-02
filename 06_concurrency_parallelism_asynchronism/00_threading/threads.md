# Thread
É uma "linha de execução" dentro de um `processo`. Um `processo` pode ter várias threads.
- Memória: compartilhada;
- Comunicação: mais fácil;
- Criação: Leve;
- Isolamento: Baixo.

No `Python` por conta do **GIL (Global Interpreter Lock)** apenas uma `thread` roda python por vez, ou seja, em Python `threads` não são *paralelizaveis* elas são *concorrentes*.

Por conta disso `multithread` não ajuda com **CPU-bound**, ela ajuda em **I/O** como o `async`.
- API;
- Leitura de arquivos;
- Banco de dados.

![image](../images/thread_process.png)