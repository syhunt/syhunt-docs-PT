# Documentação do Syhunt

Documentação do **Syhunt Hybrid** e de seus módulos: Syhunt Dynamic (DAST), Syhunt Code e Mobile (SAST/MAST), Syhunt API e Syhunt Forensic.

É novo no Syhunt? Comece pelo [Guia de Boas-Vindas](getting-started/welcome-guide.md) e, em seguida, pelo [Início Rápido](getting-started/quick-start.md).

## Primeiros passos

| Guia | Descrição |
|---|---|
| [Guia de Boas-Vindas](getting-started/welcome-guide.md) | Ative sua licença, mantenha-se informado e saiba onde obter ajuda. |
| [Início Rápido](getting-started/quick-start.md) | O que o Syhunt faz e por onde continuar. |
| [Download](getting-started/download.md) | Onde obter os instaladores. |
| [Plano de Testes de Prova de Conceito](getting-started/poc-test-plan.md) | Uma avaliação passo a passo dos principais recursos. |
| [Perguntas Frequentes](getting-started/faq.md) | Dúvidas comuns. |

## Instalação

| Guia | Descrição |
|---|---|
| [Visão Geral da Instalação e Windows](installation/install-windows.md) | Edições, instalação no Windows, extensão Sandcat para navegador, requisitos de rede, atualização e desinstalação. |
| [Linux](installation/install-linux.md) | Instalação passo a passo no Kali, Ubuntu, Debian, Fedora, distribuições baseadas em RHEL e outras. |
| [macOS](installation/install-macos.md) | Instalação em Macs com Apple Silicon e Intel, e no Parallels Desktop. |
| [Interface Web](installation/web-ui.md) | Habilitação da interface web, usuários, perfis e política de senhas. |
| [Instalando o Wine](installation/wine.md) | Instalação do Wine64 para as edições Linux e macOS (Carbon). |
| [Notas de Migração](installation/migration-notes.md) | O que muda ao atualizar entre versões. |
| [Ajuste de Desempenho](installation/performance-tuning.md) | Como lidar com varreduras longas. |

## Varreduras

| Guia | Descrição |
|---|---|
| [Varredura Dinâmica (DAST)](scanning/dynamic-scanning.md) | Varreduras caixa-preta de aplicações web em execução. |
| [Varredura Autenticada](scanning/authenticated-scanning.md) | Varredura de áreas protegidas por login. |
| [Varredura de Código-Fonte (SAST/MAST)](scanning/code-scanning.md) | Varreduras caixa-branca de código-fonte web e mobile. |
| [Varredura de APIs Web](scanning/api-scanning.md) | Varredura de APIs a partir de suas especificações. |
| [Métodos de Varredura](scanning/hunt-methods.md) | Como escolher um método de varredura. |
| [Regras de Exclusão](scanning/ignore-rules.md) | Como suprimir resultados. |
| [Agendamento de Varreduras](scanning/scheduling.md) | Como executar varreduras automaticamente. |
| [Análise Forense de Logs](scanning/forensic-log-analysis.md) | Investigação de ataques a partir de logs de servidores web. |
| [Relatórios](scanning/reporting.md) | Personalização e exportação de relatórios. |

## Integrações

| Guia | Descrição |
|---|---|
| [Linha de Comando (CLI)](integrations/command-line.md) | `scanurl`, `scancode`, `scancore` e mais. |
| [PowerShell](integrations/powershell.md) | `Start-DynamicScan` e `Start-CodeScan`. |
| [API Web](integrations/web-api.md) | Como iniciar varreduras e obter resultados via HTTP. |
| [API Lua](integrations/lua-api.md) | Automação do Syhunt com scripts Lua. |
| [GitHub](integrations/github.md) | GitHub Actions e GitHub Issues. |
| [GitLab](integrations/gitlab.md) | GitLab CI, painel de segurança e GitLab Issues. |
| [Bitbucket](integrations/bitbucket.md) | Bitbucket Pipelines. |
| [Azure DevOps](integrations/azure-devops.md) | Repositórios Azure DevOps e TFS. |
| [Jenkins](integrations/jenkins.md) | Pipelines e agentes do Jenkins. |
| [Rastreadores de Issues](integrations/issue-trackers.md) | Rastreadores do GitHub, GitLab e Jira. |
| [DefectDojo](integrations/defectdojo.md) | Envio de resultados ao DefectDojo. |
| [Faraday](integrations/faraday.md) | Envio de resultados ao Faraday. |

## Referência

| Documento | Descrição |
|---|---|
| [Especificações Técnicas](reference/technical-specifications.md) | Recursos, requisitos de sistema e glossário. |
| [Preferências](reference/preferences.md) | Todas as preferências que podem ser definidas pela CLI. |
| [Verificações de Vulnerabilidades](reference/vulnerability-checks.md) | A lista de verificações para aplicações web. |

## Suporte

| Documento | Descrição |
|---|---|
| [Como Relatar Bugs e Obter Suporte](support/reporting-bugs.md) | Falsos positivos, logs de depuração e tickets de suporte. |
