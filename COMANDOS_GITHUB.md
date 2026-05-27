# Passo a passo sugerido para versionamento no GitHub

Execute estes comandos dentro da pasta do projeto:

```bash
git init

git add Varejo.csv
git commit -m "Importa base de dados do projeto"

git add mini_projeto.py
git commit -m "Adiciona leitura csv e analise exploratoria inicial"

git add mini_projeto.py
git commit -m "Implementa validacao de identificador de compra e tratamento de datas"

git add mini_projeto.py df_limpo.csv
git commit -m "Implementa limpeza estatisticas e agrupamentos"

git add README.md README_VictorHugo_Analise_de_Dados_T1.md COMANDOS_GITHUB.md
git commit -m "Finaliza documentacao do mini projeto"

git branch -M main
git remote add origin LINK_DO_REPOSITORIO
git push -u origin main
```

Substitua `LINK_DO_REPOSITORIO` pelo link do repositório criado no GitHub.
