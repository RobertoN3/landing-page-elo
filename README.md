# elo — Landing page

Landing page em português para o conceito de um anel assistente com toque capacitivo, anotações por voz e lembretes por contexto.

## Executar localmente

Com Python 3 instalado, execute na pasta do projeto:

```sh
python server.py
```

Acesse http://127.0.0.1:5174.

Também é possível hospedar `index.html` e `elo-ring.png` em qualquer serviço de páginas estáticas. Não há dependências de build. As fontes são carregadas do Google Fonts, com fontes locais alternativas.

## Recursos

- Layout responsivo.
- Demonstrações interativas de lembretes e listas.
- Prévia de três acabamentos com cores simuladas.
- Perguntas frequentes.
- Botões “Tenho interesse” visíveis, temporariamente sem ação.

## Estado do produto

O elo é apresentado como conceito. A imagem foi gerada por IA. Preço, autonomia, conectividade e disponibilidade não estão definidos. O site não realiza vendas nem coleta dados pessoais. O servidor local rejeita envios de formulário.

## Arquivos

- `index.html`: página, estilos e interações.
- `elo-ring.png`: imagem conceitual do produto.
- `image-prompt.txt`: descrição usada na geração da imagem.
- `server.py`: servidor de prévia local, sem banco de dados.

Dados de testes e eventuais cadastros locais anteriores não fazem parte deste repositório.
