Directory Tree Visualizer

Este projeto é um **visualizador de estrutura de diretórios**, que gera uma árvore de diretórios e arquivos a partir de um caminho especificado. Ele permite visualizar a hierarquia de arquivos e diretórios, ignorando itens ocultos e a pasta `dist`, além de copiar a estrutura resultante para a área de transferência.

## Funcionalidades

- **Listagem hierárquica** de diretórios e arquivos, organizada de forma clara e fácil de entender.
- **Ignora arquivos e diretórios ocultos** (aqueles que começam com um ponto, como `.git`) e a pasta `dist`.
- **Copia automaticamente a estrutura gerada para a área de transferência**, facilitando o uso em ferramentas externas.
- Gera uma saída compatível com o site [tree.nathanfriend.io](https://tree.nathanfriend.io), onde você pode colar a estrutura para visualização gráfica.

## Como Usar

1. **Instale as dependências**:
   - Certifique-se de que você tem o Python instalado.
      - Utilize o comando abaixo para instalar a biblioteca `pyperclip`, se necessário:
        
         ```bash
            pip install pyperclip
         ```
2. **Execute o script**:
   - Execute o script Python e insira o caminho do diretório que deseja visualizar.
        ```bash
           python tree_visualizer.py
        ```
