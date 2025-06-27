# Frei Gilson YouTube Analyzer

Um projeto Python para coleta e análise de dados do canal oficial do Frei Gilson no YouTube. Baseado no projeto [LB-Project](https://github.com/MarkVN2/LB-Project), este analisador foi especificamente adaptado para extrair e processar informações do canal "Frei Gilson / Som do Monte - OFICIAL".

## 🎯 Funcionalidades

- **Coleta de dados de vídeos individuais ou em lote**
- **Extração de metadados**: título, descrição, visualizações, curtidas, data de publicação
- **Coleta de comentários** com informações dos autores e curtidas
- **Extração de transcrições** automáticas (quando disponíveis)
- **Coleta de dados de chat ao vivo** para transmissões
- **Armazenamento em JSON** para portabilidade
- **Integração com MongoDB** para armazenamento persistente
- **Análise e classificação automática** do tipo de conteúdo
- **Geração de relatórios resumidos** com estatísticas

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conexão com a internet
- MongoDB (opcional, para armazenamento em banco de dados)
- Chave da API do YouTube (opcional, para melhor performance)

## 🚀 Instalação

1. **Clone ou baixe o projeto:**
```bash
git clone <url-do-repositorio>
cd freigilson_youtube_analyzer
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente (opcional):**
Crie um arquivo `.env` na raiz do projeto:
```
YOUTUBE_API_KEY=sua_chave_da_api_aqui
MONGO_HOST=localhost
MONGO_PORT=27017
DB_NAME=freigilson_db
COLLECTION_NAME=videos
```

## 📖 Como Usar

### Análise de um vídeo específico

```bash
# Analisar um vídeo e exibir resultados
python main.py --video "https://www.youtube.com/watch?v=VIDEO_ID" --show

# Analisar e salvar em JSON
python main.py --video "https://www.youtube.com/watch?v=VIDEO_ID" --save-json

# Análise completa com todos os dados
python main.py --video "https://www.youtube.com/watch?v=VIDEO_ID" --data-level 4 --save-json --save-mongodb
```

### Análise de múltiplos vídeos do canal

```bash
# Analisar os 10 vídeos mais recentes
python main.py --channel --max-videos 10

# Análise rápida (apenas dados básicos)
python main.py --channel --max-videos 20 --data-level 1 --save-json

# Análise completa de 50 vídeos
python main.py --channel --max-videos 50 --data-level 4 --save-json --save-mongodb
```

### Opções de linha de comando

```
--video URL              Analisar um vídeo específico
--channel               Analisar múltiplos vídeos do canal
--data-level N          Nível de coleta (1-4, padrão: 4)
--max-videos N          Máximo de vídeos para processar (padrão: 50)
--show                  Exibir dados no terminal
--save-json             Salvar em arquivo JSON
--save-mongodb          Salvar no MongoDB
--no-save               Não salvar (apenas exibir)
--output-file NOME      Nome do arquivo JSON de saída
--verbose, -v           Modo verboso
--quiet, -q             Modo silencioso
```

### Níveis de coleta de dados

- **Nível 1**: Dados básicos (título, visualizações, curtidas, descrição)
- **Nível 2**: + Comentários (até 100 por vídeo)
- **Nível 3**: + Transcrições automáticas (quando disponíveis)
- **Nível 4**: + Dados de chat ao vivo (para transmissões)

## 📁 Estrutura do Projeto

```
freigilson_youtube_analyzer/
├── main.py                 # Script principal
├── data_collector.py       # Módulo de coleta de dados
├── data_processor.py       # Módulo de processamento
├── config.py              # Configurações
├── requirements.txt       # Dependências
├── README.md             # Este arquivo
├── data/                 # Diretório de dados
│   ├── raw_data/         # Dados brutos (JSON)
│   └── processed_data/   # Dados processados e resumos
└── .env                  # Variáveis de ambiente (opcional)
```

## 📊 Exemplo de Dados Coletados

```json
{
  "video_id": "VIDEO_ID",
  "title": "Acalma minha tempestade (Ao Vivo)",
  "description": "Música católica ao vivo...",
  "view_count": 5900000,
  "like_count": 89000,
  "comments_count": 1250,
  "transcript_available": true,
  "content_type": "música",
  "engagement_rate": 1.5234,
  "collected_at": "2025-06-26T19:30:00",
  "comments": [...],
  "transcript": [...]
}
```

## 🔧 Configuração Avançada

### MongoDB

Para usar o MongoDB, certifique-se de que está rodando e configure as variáveis:

```bash
# Iniciar MongoDB (Ubuntu/Debian)
sudo systemctl start mongod

# Verificar status
sudo systemctl status mongod
```

### API do YouTube

Para melhor performance e acesso a mais dados, obtenha uma chave da API:

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a YouTube Data API v3
4. Crie credenciais (chave de API)
5. Configure a variável `YOUTUBE_API_KEY`

## 📈 Análise de Dados

O projeto gera automaticamente relatórios com:

- **Estatísticas gerais**: total de visualizações, curtidas, comentários
- **Distribuição por tipo de conteúdo**: orações, pregações, músicas, etc.
- **Vídeos mais populares** e com maior engajamento
- **Métricas de performance** por vídeo

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique a documentação
2. Consulte os logs de erro
3. Abra uma issue no repositório
4. Verifique se todas as dependências estão instaladas

---
## GIF:
![Demonstração do projeto](./WhatsAppVideo2025-06-27at20.06.28-ezgif.com-video-to-gif-converter (1).gif)


**Desenvolvido com ❤️ para a comunidade católica**


