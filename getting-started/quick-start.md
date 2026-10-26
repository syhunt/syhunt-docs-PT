# Início Rápido

> **Aplica-se a:** Syhunt Hybrid 7.2

O Syhunt Hybrid é uma suíte multilinguagem de avaliação de segurança de aplicações web. Ele procura as falhas mais comuns em aplicações web sob a perspectiva de um atacante: injeta dados nas aplicações e analisa suas respostas para determinar se o código é vulnerável a ataques específicos, como injeção de SQL, cross-site scripting (XSS) e muitos outros. Quando solicitado, o Syhunt também faz a varredura do código-fonte da aplicação em busca de problemas de segurança.

## O que o Syhunt pode verificar?

O Syhunt foi projetado para cobrir uma ampla variedade de plataformas:

- **Qualquer plataforma de servidor web** (por meio da varredura dinâmica), seja Unix, Linux ou Windows.
- **Dispositivos que servem páginas web**, como roteadores e firewalls.
- **Aplicações web escritas em** ASP.NET, Java, Node.js, Lua, Perl, PHP, Python, Ruby e muitas outras linguagens (por meio da varredura de código-fonte).
- **Firewalls de aplicação web e sistemas de detecção de intrusão** (por meio de suas técnicas de evasão).

<a id="proactivescanner"></a>

## Uma abordagem proativa

Scanners de aplicações web costumam ser vistos como antivírus: reativos e dependentes de atualizações frequentes de assinaturas, diárias ou pelo menos semanais. Isso vale para os scanners tradicionais. Desde 2008, porém, a Syhunt adota uma abordagem proativa na construção de suas verificações e de seu scanner híbrido, concentrando-se em fraquezas comuns (CWEs), e não em vulnerabilidades divulgadas individualmente (CVEs).

| Scanners tradicionais (reativos) | A abordagem proativa do Syhunt |
|---|---|
| Dependem fortemente de atualizações regulares de assinaturas voltadas a CVEs (**vulnerabilidades conhecidas e divulgadas** em aplicações de terceiros). | Não depende de atualizações frequentes. O desenvolvimento se concentra em [uma lista de CWEs](../reference/vulnerability-checks.md) (**fraquezas comuns**). Verificações específicas para CVEs são lançadas com as versões menores e maiores, como **complemento** às verificações proativas. |
| Não detectam vulnerabilidades não divulgadas em aplicações de terceiros. | Detecta **vulnerabilidades divulgadas e não divulgadas** em aplicações de terceiros: detectar com precisão uma única CWE significa identificar centenas de CVEs de uma só vez. |
| Deixam passar a maioria, se não todas, as vulnerabilidades das suas aplicações próprias. | É muito mais adequado para encontrar vulnerabilidades nas suas aplicações próprias. |
| Não analisam código-fonte. | Realiza **análise híbrida**: a análise dinâmica complementa a análise de código-fonte (DAST + SAST). |

## Próximos passos

| Tarefa | Guia |
|---|---|
| Executar sua primeira varredura dinâmica (caixa-preta) | [Varredura Dinâmica](../scanning/dynamic-scanning.md) |
| Executar sua primeira varredura de código-fonte (caixa-branca) | [Varredura de Código-Fonte](../scanning/code-scanning.md) |
| Escolher o método de varredura adequado | [Métodos de Varredura](../scanning/hunt-methods.md) |
| Agendar varreduras recorrentes | [Agendamento de Varreduras](../scanning/scheduling.md) |
| Personalizar relatórios | [Relatórios](../scanning/reporting.md) |
| Verificar o que é necessário antes de uma varredura dinâmica | [Requisitos prévios](../scanning/dynamic-scanning.md#dynscanreq) |
| Verificar os requisitos de hardware e software | [Especificações Técnicas](../reference/technical-specifications.md#specsbegin) |

<a id="redefineseverity_begin"></a>

## Redefinindo a severidade de uma vulnerabilidade

Se você discordar da severidade atribuída a uma vulnerabilidade relatada, pode definir uma nova severidade, que valerá para todas as varreduras futuras:

1. Na interface web, abra a tela Connectors (![](../images/menu.png) **Menu → Connectors**).
2. Adicione um conector do tipo **List** chamado `VULNSEVERITY`.
3. Informe o ID único da verificação da vulnerabilidade, seguido de `=` e da nova severidade. Por exemplo: `C-1603660271-7241=low`
4. Clique em **Add** para adicionar a entrada à lista.
5. Clique em **Save** para salvar a lista.
