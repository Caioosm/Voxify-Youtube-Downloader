# Baixador de Áudio do YouTube

## Visão Geral
O Baixador de Áudio do YouTube é uma aplicação Python com uma interface gráfica simples (GUI) que permite aos usuários baixar áudio de vídeos do YouTube. A aplicação é construída utilizando a biblioteca Tkinter para a GUI e o Inno Setup para criar um instalador executável para distribuição.

## Funcionalidades
- **GUI Intuitiva**: A aplicação apresenta uma interface gráfica simples e fácil de usar, construída utilizando a biblioteca Tkinter do Python. Ela inclui campos para inserir a URL do vídeo do YouTube e para escolher a pasta de destino.
  
- **Download de Áudio do YouTube**: A aplicação utiliza a biblioteca `yt-dlp` para baixar o áudio dos vídeos do YouTube na melhor qualidade disponível.
  
- **Conversão para Formato WAV**: Após o download do áudio, a aplicação utiliza a biblioteca `ffmpeg` para converter o áudio para o formato WAV, garantindo compatibilidade com uma variedade de players de áudio.
  
- **Feedback de Progresso**: Durante o processo de download e conversão, a aplicação fornece feedback visual de progresso, como uma barra de progresso indicando o status do download e da conversão.
  
- **Personalização da Pasta de Destino**: Os usuários podem escolher a pasta onde desejam salvar o áudio baixado, oferecendo flexibilidade e controle sobre o armazenamento dos arquivos.

## Distribuição
A aplicação será distribuída como um instalador executável para o sistema operacional Windows. Isso será alcançado utilizando o Inno Setup para criar um instalador que inclua o executável Python, as dependências necessárias e quaisquer recursos adicionais, como um ícone personalizado.

## Escopo Adicional
- Implementar tratamento de erros e validação de entrada para lidar com URLs inválidas ou erros de download.
- Oferecer opções adicionais de formato de áudio para os usuários escolherem.
- Adicionar suporte para outros sistemas operacionais, como macOS e Linux, utilizando ferramentas de criação de instaladores adequadas para essas plataformas.

## Instalação
Para instalar o Baixador de Áudio do YouTube, basta baixar o instalador na página de releases e executá-lo no seu sistema Windows. Siga as instruções na tela para completar o processo de instalação.

## Uso
Após a instalação, inicie o Baixador de Áudio do YouTube a partir do menu Iniciar ou atalho na área de trabalho. Insira a URL do vídeo do YouTube no campo designado e escolha a pasta de destino onde deseja salvar o áudio. Clique no botão "Baixar Áudio" para iniciar o processo de download. A barra de progresso indicará o status do download e da conversão.

## Créditos
Este projeto foi criado por [Caioosm] como um projeto pessoal.

## Licença
Este projeto está licenciado sob a Licença [Nome da Licença] - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
