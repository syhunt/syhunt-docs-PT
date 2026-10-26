# Linha de Comando (CLI)

> **Aplica-se a:** Syhunt Hybrid 7.2

**Conteúdo**

- [Introdução](#intro)
- [Varreduras dinâmicas](#cli_dynamic_begin)
- [Varreduras de API](#cli_api_begin)
- [Varreduras de código-fonte](#cli_code_begin)
- [Varreduras forenses](#cli_forensic)
- [Condições de aprovação/reprovação](#pfcond)
- [Modos de varredura incremental](#incremental)
- [Formatos, modelos e idiomas de relatório](#report)
- [Alterando as preferências do Syhunt](#cli_prefs)
- [Usando rastreadores de issues](#cli_trackers)
- [Atualizando o Syhunt](#cli_update)

<a id="intro"></a>

## Introdução

Este guia explica como executar varreduras e gerar relatórios de vulnerabilidades pela linha de comando.

As ferramentas de linha de comando ficam na pasta de instalação do Syhunt, que depende do sistema operacional e da edição:

| Sistema | Local padrão |
|---|---|
| Windows | `C:\Program Files\Syhunt Hybrid\`<br>`C:\Program Files (x86)\Syhunt Hybrid\`<br>`C:\Program Files\Syhunt Community` |
| Linux | `/home/<usuário>/syhunt-hybrid/carbon/`<br>`/home/<usuário>/syhunt-community/carbon/` |
| macOS | `/Applications/Syhunt Hybrid/carbon`<br>`/Applications/Syhunt Community/carbon` |

| Ferramenta | Finalidade |
|---|---|
| `scanurl` | Varreduras dinâmicas (DAST) e de API |
| `scancode` | Varreduras de código-fonte (SAST/MAST) |
| `scanlog` | Análise forense de logs |
| `scancore` | Preferências, rastreadores e comandos de manutenção |
| `scanupdate` | Atualizações (Linux e macOS) |

Abra um terminal ou Prompt de Comando na pasta de instalação antes de executar os comandos abaixo.

<a id="cli_dynamic_begin"></a>

## Varreduras dinâmicas

```
scanurl <urlinicial> -hm:<metodo>
```

Exemplo:

```
scanurl http://www.somehost.com -hm:appscan
```

O `scanurl` gera e salva um relatório automaticamente, a menos que você informe `-nr`.

<a id="cli_dynamic_parameters"></a>

### Parâmetros do `scanurl`

Todos os parâmetros são opcionais.

| Parâmetro | Descrição | Padrão |
|---|---|---|
| `-sn:<nome>` | Nome da sessão; deve ser único. Se omitido, um ID único é gerado. | ID gerado |
| `-hm:<nome>` | [Método de varredura](../scanning/hunt-methods.md) a ser usado. | `appscan` |
| `-emu:<modo>` | Modo de emulação de navegador: `chrome`, `edge`, `firefox`, `msie` ou `safari`. | `chrome` |
| `-srcdir:<pasta>` | Pasta do código-fonte do alvo para uma varredura híbrida (por exemplo, `"C:\www\docs\"` ou `/home/user/www/`). | |
| `-tk:<rastreador>` | Envia as vulnerabilidades a um rastreador após a varredura. Pode ser combinado com `-pfcond`. | |
| `-tk2:<rastreador>`, `-tk3:<rastreador>` | Rastreadores adicionais, como acima. | |
| `-nr` | Não gera relatório após a varredura. | |
| `-or` | Abre o relatório após gerá-lo. | |
| `-rout:<arquivo>` | Nome do arquivo de relatório; a extensão define o [formato](#repfmt). | `Report_<sessão>.html` |
| `-rtpl:<nome>` | [Modelo de relatório](#reptemplates). | `Standard` |
| `-xout:<arquivo>` | Nome do arquivo de exportação; a extensão define o [formato](#repfmt). | `Export_<sessão>.xml` |
| `-xout2:<arquivo>` | Um segundo arquivo de exportação. | `Export_<sessão>.xml` |
| `-pfcond:<condição>` | [Condição de aprovação/reprovação](#pfcond) a ser verificada. | |
| `-nv` | Saída menos detalhada (erros e informações básicas continuam sendo exibidos). | |
| `-inc:<modo>` | [Modo de varredura incremental](#incremental). | `targetpref` |
| `-inctag:<nome>` | Armazena os dados da varredura incremental sob uma tag. | |
| `-mnl:<n>` | Número máximo de links por servidor. | `10000` |
| `-mnr:<n>` | Número máximo de novas tentativas. | `2` |
| `-tmo:<ms>` | Tempo limite das requisições, em milissegundos. | `8000` |
| `-tml:<tempo>` | Tempo máximo da varredura, por exemplo `1d`, `3h`, `2h30m`, `50m`. | Sem limite |
| `-ver:<v>` | Versão do HTTP. | `1.1` |
| `-nofris` | Não segue automaticamente um redirecionamento para fora do domínio na URL inicial. | |
| `-nodos` | Desativa os testes de negação de serviço. | |
| `-nojs` | Desativa a emulação e execução de JavaScript. | |
| `-atype:<tipo>` | Tipo de autenticação: `Basic`, `Form` ou `Manual`. | |
| `-auser:<usuário>` | Usuário para autenticação. | |
| `-apass:<senha>` | Senha para autenticação. | |
| `-about` | Exibe informações sobre a versão. | |
| `-help` (ou `/?`) | Lista os parâmetros disponíveis. | |

### Varredura de endereços IPv6

Coloque endereços IPv6 entre colchetes, por exemplo `http://[2001:4860:0:2001::68]/index.php`.

<a id="cli_dynamic_end"></a>
<a id="cli_api_begin"></a>

## Varreduras de API

As varreduras de API também usam o `scanurl`. A única diferença é que você informa a URL da **especificação da API** em vez de uma URL inicial. Se informar a URL da própria API, o Syhunt executará uma varredura dinâmica tradicional, sem mapeamento da API, validação de esquema ou testes específicos de API.

Por exemplo, se a especificação estiver em `https://example.com/openapi.json` e descrever uma API em `https://api.example.com`:

```
scanurl https://example.com/openapi.json -hm:appscan   # correto: varredura de API
scanurl https://api.example.com                        # errado: executa uma varredura DAST tradicional
```

O `scanurl` aceita os mesmos [parâmetros opcionais](#cli_dynamic_parameters) nas varreduras de API. Consulte [Varredura de APIs Web](../scanning/api-scanning.md) para mais detalhes.

<a id="cli_api_end"></a>
<a id="cli_code_begin"></a>

## Varreduras de código-fonte

```
scancode <alvo> -hm:<metodo>
```

Exemplos:

```bat
:: Repositórios Git
scancode git://sub.domain.com/repo.git
scancode https://github.com/user/repo.git -rb:master

:: Caminhos locais
scancode /source/www/
scancode c:\source\www\
scancode c:\source\www\file.php
scancode c:\mobile\myapp.apk
scancode "c:\source code\www\"
```

<a id="cli_code_windows"></a>

Repositórios Azure DevOps / TFS:

```bat
scancode https://dev.azure.com/user/project
scancode https://myserver/tfs/project
scancode collection:https://dev.azure.com/user$/project
```

O `scancode` gera e salva um relatório automaticamente, a menos que você informe `-nr`.

### Parâmetros do `scancode`

Todos os parâmetros são opcionais.

| Parâmetro | Descrição | Padrão |
|---|---|---|
| `-sn:<nome>` | Nome da sessão; deve ser único. Se omitido, um ID único é gerado. | ID gerado |
| `-hm:<nome>` | [Método de varredura](../scanning/hunt-methods.md) a ser usado. | `appscan` |
| `-rb:<branch>` | Branch do repositório Git. | |
| `-tfsv:<versão>` | Versão do TFS. | `default` |
| `-tk:<rastreador>` | Envia as vulnerabilidades a um rastreador após a varredura. Pode ser combinado com `-pfcond`. | |
| `-tk2:<rastreador>`, `-tk3:<rastreador>` | Rastreadores adicionais, como acima. | |
| `-nr` | Não gera relatório após a varredura. | |
| `-or` | Abre o relatório após gerá-lo. | |
| `-rout:<arquivo>` | Nome do arquivo de relatório; a extensão define o [formato](#repfmt). | `Report_<sessão>.html` |
| `-rtpl:<nome>` | [Modelo de relatório](#reptemplates). | `Standard` |
| `-xout:<arquivo>` | Nome do arquivo de exportação; a extensão define o [formato](#repfmt). | `Export_<sessão>.xml` |
| `-xout2:<arquivo>` | Um segundo arquivo de exportação. | `Export_<sessão>.xml` |
| `-pfcond:<condição>` | [Condição de aprovação/reprovação](#pfcond) a ser verificada. | |
| `-nv` | Saída menos detalhada (erros e informações básicas continuam sendo exibidos). | |
| `-inc:<modo>` | [Modo de varredura incremental](#incremental). | `targetpref` |
| `-inctag:<nome>` | Armazena os dados da varredura incremental sob uma tag. | |
| `-excp:<caminhos>` | Caminhos a excluir da análise, por exemplo `-excp:/path/*,/path2/*`. | |
| `-refurl:<url>` | Uma URL associada ao código, apenas para referência. | |
| `-noifa` | Desativa a análise de filtragem de entrada. | |
| `-tml:<tempo>` | Tempo máximo da varredura, por exemplo `1d`, `3h`, `2h30m`, `50m`. | Sem limite |
| `-about` | Exibe informações sobre a versão. | |
| `-help` (ou `/?`) | Lista os parâmetros disponíveis. | |

<a id="cli_code_end"></a>
<a id="cli_forensic"></a>

## Varreduras forenses

A análise forense de logs é executada com o `scanlog`. No Syhunt Hybrid 7.2, esta é a única forma de executar o Syhunt Forensic. Consulte [Análise Forense de Logs](../scanning/forensic-log-analysis.md). Execute `scanlog -help` para listar seus parâmetros.

<a id="pfcond"></a>

## Condições de aprovação/reprovação

Informe uma condição de aprovação/reprovação ao `scanurl` ou ao `scancode` com o parâmetro `-pfcond`.

<a id="pfcondbegin"></a>

| Condição | Reprova se… |
|---|---|
| `high` ou `fail-if:risk=high` | for encontrada uma vulnerabilidade ou ameaça de risco Alto. |
| `medium` ou `fail-if:risk=mediumup` | for encontrada uma vulnerabilidade ou ameaça de risco Médio ou Alto. |
| `low` ou `fail-if:risk=lowup` | for encontrada uma vulnerabilidade ou ameaça de risco Baixo, Médio ou Alto. |

<a id="pfcondend"></a>
<a id="incremental"></a>

## Modos de varredura incremental

| Modo | Descrição |
|---|---|
| `auto` | Gerencia o cache de varredura incremental automaticamente (recomendado). |
| `disabled` | Desativa o cache de varredura incremental. As varreduras levam de 3 a 4 vezes mais tempo. |
| `forced` | Usa sempre a varredura incremental. Se usar este modo, execute também uma varredura normal, não forçada, cerca de uma vez por mês. |
| `targetpref` | Usa o modo definido nas preferências do alvo. |

Para limpar o cache de varredura incremental, execute `scancore -runcmd:clearinc`.

<a id="report"></a>

## Formatos, modelos e idiomas de relatório

<a id="replanguages"></a>

### Idiomas

| Código | Idioma |
|---|---|
| `EN` | Inglês |
| `DE` | Alemão |
| `ES` | Espanhol |
| `FR` | Francês |
| `IT` | Italiano |
| `JP` | Japonês |
| `KR` | Coreano |
| `PT` | Português |

Para definir o idioma dos relatórios:

```
scancore -prefset:hybrid.report.defaultlanguage -v:PT
```

Também é possível defini-lo pela interface: ![](../images/menu.png) **Menu → Preferences → Other Hybrid Preferences**.

<a id="repfmt"></a>

### Formatos

O formato de saída é definido pela extensão do arquivo informado em `-rout` ou `-xout`:

| Extensão | Formato |
|---|---|
| `.html` | Relatório HTML |
| `.pdf` | Relatório PDF |
| `.xml` | Exportação XML |
| `.json` | Exportação de vulnerabilidades em JSON |
| `.csv` | CSV (valores separados por vírgula) |
| `.mse.csv` | CSV para Microsoft Excel |
| `.txt` | Relatório em texto |

<a id="reptemplates"></a>

### Modelos

| Modelo | Conteúdo |
|---|---|
| `Standard` | Informações sobre vulnerabilidades de risco baixo a alto. |
| `Comparison` | O conteúdo padrão, mais a evolução das vulnerabilidades entre varreduras. |
| `Compliance` | Informações de conformidade com OWASP Top 10, CWE/SANS Top 25 (2019) e PCI DSS 3.2.1. |
| `Mobile` | Informações de conformidade com OWASP Mobile Top 10, CWE/SANS Top 25 (2019) e PCI DSS 3.2.1. |
| `Complete` | O conteúdo padrão, mais detalhes de comparação, conformidade, requisição/resposta e cobertura. |

<a id="huntmethods_begin"></a>

Para os métodos de varredura disponíveis e seus nomes na CLI, consulte [Métodos de Varredura](../scanning/hunt-methods.md).

<a id="cli_prefs"></a>

## Alterando as preferências do Syhunt

Desde o Syhunt 6.9.6.3, você pode alterar as [preferências persistentes](../reference/preferences.md) do Syhunt, globalmente ou para um alvo específico, com `scancore -prefset`. Use `-prefprint` para exibir o valor atual de qualquer preferência.

<a id="cli_prefs_exbegin"></a>

```lua
-- Exemplo 1: definir o logotipo exibido nos novos relatórios
scancore -prefset:hybrid.report.company.logo.urldark -v:https://www.mydomain.com/mylogo.png

-- Exemplo 2: exibir a URL atual do logotipo dos relatórios
scancore -prefprint:hybrid.report.company.logo.urldark

-- Exemplo 3: definir autenticação Basic para um site específico
scancore -tg:http://127.0.0.1 -prefset:dynamic.formauth.type -v:Basic
scancore -tg:http://127.0.0.1 -prefset:dynamic.formauth.username -v:myuser
scancore -tg:http://127.0.0.1 -prefset:dynamic.formauth.password -vsecret

-- Exemplo 4: habilitar ou desabilitar as preferências de um site específico
scancore -tg:http://127.0.0.1 -prefset:enabled -v:true
scancore -tg:http://127.0.0.1 -prefset:enabled -v:false

-- Exemplo 5: definir um valor a partir de um arquivo de lista
scancore -tg:http://127.0.0.1 -prefset:dynamic.lists.cookies -fromfile:mycookies.lst
```

<a id="cli_prefs_exend"></a>

Consulte [Preferências](../reference/preferences.md) para a lista completa de IDs de preferências.

### Limpando todas as preferências

```lua
-- Limpar as preferências globais
scancore -runcmd:clearpref
-- Limpar as preferências de todos os sites
scancore -runcmd:clearsite
```

<a id="cli_trackers"></a>

## Usando rastreadores de issues

Desde o Syhunt 6.9.6.3, você pode adicionar, gerenciar e usar [rastreadores de issues](issue-trackers.md) pela linha de comando com `scancore -tracker`.

<a id="clitrackerexbegin"></a>

```lua
-- Exemplo 1: adicionar um rastreador do GitHub
scancore -tracker:add
-- Informe o tipo (GitHub) e um nome para o rastreador e pressione Enter.
-- Configure-o:
scancore -tracker:set to:mytrackername -key:project.name -v:owner/repo
scancore -tracker:set to:mytrackername -key:auth.token.encrypted -vsecret

-- Exemplo 2: adicionar um rastreador de e-mail
scancore -tracker:add
-- Informe o tipo (Email) e um nome para o rastreador e pressione Enter.
scancore -tracker:set to:myemailtracker -key:message.from -v:robot@yourdomain.com
scancore -tracker:set to:myemailtracker -key:message.tolist -v:security@yourdomain.com,team@yourdomain.com
scancore -tracker:set to:myemailtracker -key:auth.targethost -v:smtp.yourdomain.com
scancore -tracker:set to:myemailtracker -key:smtp.targetport -v:587
scancore -tracker:set to:myemailtracker -key:auth.username -v:myusername
scancore -tracker:set to:myemailtracker -key:auth.password -vsecret

-- Exemplo 3: testar um rastreador
scancore -tracker:send -tid:TEST -to:mytrackername -note:"Meu comentário"

-- Exemplo 4: enviar uma vulnerabilidade de um relatório a um rastreador
-- 1596281007-7-4771 é o track ID da vulnerabilidade, obtido no relatório.
scancore -tracker:send -tid:1596281007-7-4771 -to:mytrackername -note:"Meu comentário"

-- Exemplo 5: listar os rastreadores
scancore -tracker:list

-- Exemplo 6: excluir um rastreador
scancore -tracker:del to:mytrackername
```

<a id="clitrackerexend"></a>

Consulte [Preferências: rastreadores](../reference/preferences.md#prefs_tracker) para a lista de IDs de preferências de rastreadores.

<a id="cli_trackers_send"></a>

### Enviando vulnerabilidades a um rastreador após a varredura

Informe `-tk` ao `scanurl` ou ao `scancode` para enviar a um rastreador um resumo das vulnerabilidades encontradas:

```lua
-- Exemplo 1: usar um rastreador existente
scanurl mydomain -tk:trackername

-- Exemplo 2: enviar apenas se forem encontradas vulnerabilidades de severidade alta
scanurl mydomain -tk:trackername -pfcond:fail-if:risk=high

-- Exemplo 3: definir o rastreador na hora
scanurl mydomain -tk:"?app=github###project=user/repo###token=ghp_etc"
```

> [!NOTE]
> Ao informar preferências de rastreadores em `-tk`, use os [nomes abreviados](issue-trackers.md#shortnames).

### Removendo todos os rastreadores

```
scancore -runcmd:cleartrack
```

<a id="cli_update"></a>

## Atualizando o Syhunt

No Linux e no macOS, execute `scanupdate` para verificar se há atualizações; se houver, o Syhunt pergunta se deve baixá-las e instalá-las. Execute `scanupdate auto` para instalá-las sem pedir confirmação.

No Windows, baixe e instale as atualizações a partir do site da Syhunt.
