
# DemoQA — Portfolio QA

Este repositório contém automações de testes para o site [DemoQA](https://demoqa.com), que é uma plataforma amplamente utilizada para praticar testes de interface.  
Aqui, desenvolvo testes que cobrem interações complexas com componentes, formulários, alertas, botões, e muito mais.

---

## 🎯 Objetivos

- Explorar diferentes componentes da página DemoQA (botões, formulários, alerts, seletores, etc).  
- Escrever testes robustos e reutilizáveis para simular interações reais de usuário.  
- Demonstrar domínio em automação UI usando boas práticas de design de código.  
- Aumentar a confiança em testes por meio de asserts bem definidos e validações visuais.

---

## 🔧 Tecnologias e Ferramentas

- **Selenium WebDriver** para automação de interface  
- Linguagem: **JavaScript / Python / Java** (depende do seu setup — ajuste aqui)  
- Estrutura de testes: Mocha / Jest / Pytest / outra de sua escolha  
- Uso de localizadores variados (CSS, XPath, ID) para cobrir diferentes tipos de elementos

---

## 📂 Estrutura do Projeto

```

/tests
├── botões.spec.js         # testes para botões
├── formulario.spec.js     # preenchimento de formulários
├── alerts.spec.js         # interação com alertas e diálogos
/support
└── helpers.js              # funções utilitárias




## 🚀 Como rodar os testes

1. Clone este repositório  
   ```bash
   git clone https://github.com/danielafoggiatto/DemoQA---Portfolio-QA.git  
````

2. Instale dependências

   ```bash
   npm install  # se for JS  
   # ou  
   pip install -r requirements.txt  # se for Python  
   ```
3. Faça o download do driver do navegador (ex: ChromeDriver) compatível com sua versão do navegador.
4. Execute os testes:

   ```bash
   npx mocha tests  # para JS + Mocha  
   # ou  
   pytest tests/    # para Python  
   ```

---

## 💡 Exemplos de Cenários Testados

* Clicar em diferentes tipos de botões e verificar comportamento
* Preenchimento de formulários com diferentes tipos de campo (texto, dropdown, checkbox)
* Manipulação de alertas, janelas modais e diálogos
* Validação de elementos dinâmicos e esperas explícitas para garantir estabilidade dos testes

---

## ✅ Boas Práticas Utilizadas

* Organização de testes em módulos lógicos
* Localizadores bem definidos para evitar falhas em mudanças de UI
* Funções auxiliares para repetição de ações comuns
* Asserts robustos para verificar se a aplicação realmente está no estado esperado após cada ação

---

## 📚 Referências

* [DemoQA – site de prática para automação](https://demoqa.com)
* [Documentação Selenium WebDriver](https://www.selenium.dev/documentation/)
* [Estratégias de localização de elementos com CSS e XPath](https://www.selenium.dev/documentation/webdriver/elements/locators/)

---

## 👩‍💻 Sobre a Autora

**Daniela Foggiatto** — QA Automation

* Experiência com automação de testes, frameworks bem organizados e código limpo
* Paixão por testes que simulam cenários reais e por explorar componentes complexos
* Sempre buscando qualidade, segurança e escalabilidade nos testes

---



