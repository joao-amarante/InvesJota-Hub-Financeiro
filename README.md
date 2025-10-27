💎 InvesJota: Hub de Ferramentas Financeiras .
InvesJota é uma plataforma web desenvolvida para oferecer um hub minimalista de calculadoras e notícias focadas em finanças e investimentos. O projeto visa combinar funcionalidade máxima com um design elegante e de alto contraste (Black & Gold Minimalist), facilitando decisões financeiras complexas.

✨ Tecnologias Utilizadas
Este é um projeto puramente front-end, garantindo carregamento rápido e baixo custo de manutenção (Hospedagem Gratuita via GitHub Pages).

Linguagens: HTML5, CSS3, JavaScript (ES6+)

Design: Tema Black & Gold Minimalist (Alto Contraste)

Gráficos: Chart.js (Para visualização dinâmica de projeções)

Interatividade: CSS Transitions, Scroll Animations (Vanilla JS), Dark/Light Mode Toggle.

Hospedagem: GitHub Pages

🌟 Funcionalidades e Diferenciais
O InvesJota é dividido em um core principal (calculadoras e notícias) e funcionalidades complementares de monetização.

Calculadoras Integradas (Com Conteúdo Educacional)
Todas as calculadoras fornecem uma seção educativa (mais de 500 palavras) que explica a fórmula, aplicação e riscos.

Calculadora de Juros Compostos: Projeta o crescimento exponencial do capital com aportes mensais.

Meta Primeiro Milhão: Calcula o tempo exato (em anos e meses) para atingir R$ 1.000.000,00.

Capital para Viver de Renda: Determina o capital total necessário para gerar uma renda mensal desejada, baseado na Taxa Segura de Retirada (TSR).

Comparador de Cartões: Analisa o custo-benefício (Anuidade + Risco Rotativo vs. Milhas/Cashback) de dois cartões.

Juros Simples: Ferramenta para cálculos lineares e didáticos.

Design e UX
Tema Dinâmico (Dark/Light Mode): O usuário pode alternar entre os temas Claro (Minimalista) e Escuro (Alto Contraste) através de um toggle, com preservação de preferência via localStorage.

Animações Suaves: Elementos da página inicial e do catálogo (cards) utilizam animações de deslizamento (fade-in) acionadas pelo scroll.

💻 Como Executar o Projeto (Desenvolvimento/Local)
Como este é um projeto estático, a execução é extremamente simples, ideal para o Codespaces ou Visual Studio.

Clone o Repositório:

Bash

git clone https://github.com/SEU_USUARIO/InvesJota-Hub-Financeiro.git
cd InvesJota-Hub-Financeiro
Servidor Local: Abra a pasta raiz do projeto (HubFinanceiro) e abra o arquivo index.html diretamente no seu navegador. Recomendamos usar uma extensão como Live Server no VS Code para visualizar corretamente todos os caminhos e o JavaScript.

⚙️ Estrutura do Projeto (Para Desenvolvedores)
A arquitetura foi movida para a raiz para garantir a melhor compatibilidade com o GitHub Pages.

/HubFinanceiro (RAIZ)
├── assets/
│   ├── css/
│   │   └── invesjota_base.css  <- VARIÁVEIS DE TEMA E ESTILOS GERAIS
│   └── imagens/
│       └── banner_principal.jpg.webp
├── index.html                   <- Home Page (Ponto de Entrada)
├── catalogo_calculadoras.html   <- Catálogo de Links
├── juros_compostos.html         <- Calculadora com Gráfico Chart.js
├── calculadora_renda.html
├── primeiro_milhao.html
└── ... (Demais arquivos .html)
🤝 Contribuições
Sua contribuição para refinar as lógicas financeiras, adicionar novas ferramentas ou melhorar o design responsivo é bem-vinda!

Faça um Fork do projeto.

Crie um Branch para sua funcionalidade (git checkout -b feature/minha-melhoria).

Faça o Commit das suas alterações e envie um Pull Request.
