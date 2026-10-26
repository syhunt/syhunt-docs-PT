# API Lua

> **Aplica-se a:** Syhunt Hybrid 6.9.12

**Conteúdo**

- [Introdução](#lapi_intro_begin)
- [Iniciando uma varredura dinâmica](#lapi_dynamic_begin)
- [Iniciando uma varredura de código-fonte](#lapi_code_begin)
- [Obtendo resultados](#lapi_getresults_begin)
- [Gerando um relatório ou exportação](#lapi_genreport_begin)
- [Obtendo detalhes da sessão](#lapi_getsessiondetails_begin)
- [Enviando um relatório por e-mail](#lapi_emailreport_begin)
- [Atualizando preferências](#lapi_prefupdate)
- [Outras funções](#lapi_extras)

<a id="lapi_intro_begin"></a>

## Introdução

O Syhunt Hybrid Platinum inclui uma API Lua simples para iniciar varreduras dinâmicas e de código-fonte, obter o status, o relatório e o log de uma sessão de varredura, e mais. As mesmas operações estão disponíveis via HTTP pela [API Web](web-api.md).

### Carregando a biblioteca do Syhunt

Carregue a biblioteca do Syhunt antes de usar a API:

```lua
-- Em um aplicativo com interface gráfica
require "SyMini"
-- Em um aplicativo de console
require "SyMini.Console"
```

<a id="lapi_dynamic_begin"></a>

## Iniciando uma varredura dinâmica

```lua
local res = symini.scantask_launch({
  sessionname = "Test",
  starturl = "http://127.0.0.1",
  huntmethod = "appscan",
  reporttemplate = "Complete"
})
if res.result == true then
  print(res.sessionname)
end
```

<a id="lapi_dynlaunch_begin"></a>

| Chave | Descrição |
|---|---|
| `starturl` **(obrigatória)** | A URL alvo. |
| `sessionname` | Um nome de sessão único e alfanumérico. Se omitido, um nome aleatório é gerado. |
| `huntmethod` | Um nome de [método de varredura](../scanning/hunt-methods.md) válido. |
| `reporttemplate` | Um modelo de relatório: `Standard`, `Comparison`, `Compliance` ou `Complete`. |
| `reportgl` | Se `true`, retorna saída JSON no formato do GitLab. |
| `timelimit` | Tempo máximo da varredura, por exemplo `1d`, `3h`, `2h30m`, `50m`. A varredura é interrompida ao atingir o limite. Sem limite por padrão. |

<a id="lapi_dynlaunch_end"></a>
<a id="lapi_dynlaunchret_begin"></a>

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `pid` | Um ID de processo único da varredura em execução. |
| `result` | `true` se a varredura foi iniciada; `false` se não foi possível iniciá-la. |
| `resultstr` | Se `result` for `false`, uma descrição do erro. |
| `sessionname` | O nome da sessão da varredura. Se você não informou um, este é o nome gerado. Use-o nas chamadas seguintes para obter os resultados. |
| `sessiontype` | O tipo da sessão: `dynamic` ou `code`. |

<a id="lapi_dynlaunchret_end"></a>
<a id="lapi_code_begin"></a>

## Iniciando uma varredura de código-fonte

```lua
-- Varredura de uma pasta local
local res = symini.scantask_launch({
  sessionname = "Test",
  sourcetarget = "P:\\Private\\MyWebApp\\",
  huntmethod = "normal",
  reporttemplate = "Complete"
})

-- Varredura de uma URL de repositório
local res = symini.scantask_launch({
  sessionname = "Test",
  sourcetarget = "https://github.com/drnic/php-helloworld.git",
  sourcebranch = "master",
  huntmethod = "normal",
  reporttemplate = "Complete"
})

if res.result == true then
  print(res.sessionname)
end
```

<a id="lapi_codelaunch_begin"></a>

| Chave | Descrição |
|---|---|
| `sourcetarget` **(obrigatória)** | Uma pasta local ou uma URL Git. |
| `sourcebranch` | O branch a ser verificado, para URLs de repositório. |
| `sessionname`, `huntmethod`, `reporttemplate`, `reportgl`, `timelimit` | Como nas [varreduras dinâmicas](#lapi_dynlaunch_begin). |

<a id="lapi_codelaunch_end"></a>
<a id="lapi_codelaunchret_begin"></a>

A tabela retornada é a mesma das [varreduras dinâmicas](#lapi_dynlaunchret_begin).

<a id="lapi_codelaunchret_end"></a>
<a id="lapi_getresults_begin"></a>

## Obtendo resultados

### Status

```lua
local res = symini.scantask_getresults({
  sessionname = "Test",
  resulttype = "status"
})
```

<a id="lapi_results_begin"></a>

| Chave | Descrição |
|---|---|
| `sessionname` **(obrigatória)** | A sessão cujos resultados você quer obter. |
| `resulttype` **(obrigatória)** | `status`, `report_xml`, `report_json` ou `session_log`. |

<a id="lapi_results_end"></a>
<a id="lapi_resultsret_begin"></a>

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `report_xml_available` | `true` se houver um relatório XML disponível. |
| `report_json_available` | `true` se houver um relatório JSON disponível. |
| `session_log_available` | `true` se houver um log de varredura disponível. |
| `status` | O status da sessão: `Scanning` ou, após o fim da varredura, `Completed`. |

<a id="lapi_resultsret_end"></a>

### Relatório

```lua
-- Relatório XML
local res = symini.scantask_getresults({
  sessionname = "Test",
  resulttype = "report_xml"
})

-- Relatório JSON
local res = symini.scantask_getresults({
  sessionname = "Test",
  resulttype = "report_json"
})
```

### Log

```lua
local res = symini.scantask_getresults({
  sessionname = "Test",
  resulttype = "session_log"
})
```

Retorna o log da varredura como texto.

<a id="lapi_genreport_begin"></a>

## Gerando um relatório ou exportação

```lua
local res = symini.genreport({
  sessionname = 'mysessionname',
  outfilename = 'myreport.pdf',
  template = 'Standard'
})
```

| Chave | Descrição |
|---|---|
| `sessionname` **(obrigatória)** | A sessão do relatório. |
| `outfilename` **(obrigatória)** | O nome do arquivo de saída do relatório; a extensão define o [formato](command-line.md#repfmt). |
| `template` | O [modelo de relatório](command-line.md#reptemplates). Padrão: `Standard`. |
| `passfailcond` | Uma [condição de aprovação/reprovação](command-line.md#pfcondbegin). |

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `outfilename` | O caminho completo do relatório gerado. |
| `result` | `true` se o relatório foi gerado. |
| `resultstr` | Status da geração do relatório. |
| `passfail_result` | `true` se a condição de aprovação/reprovação foi aprovada. |
| `passfail_status` | Status da condição de aprovação/reprovação. |
| `passfail_resultstr` | Motivo do resultado de aprovação/reprovação. |

<a id="lapi_getsessiondetails_begin"></a>

## Obtendo detalhes da sessão

```lua
local res = symini.getsessiondetails('mysessionname')
```

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `huntmethod` | Método de varredura. |
| `datetime` | Data e hora da varredura. |
| `duration` | Duração da varredura. |
| `targets` | Alvo(s) da varredura. |
| `targetdesc` | Descrição do alvo. |
| `sourcedir` | Pasta de código-fonte do alvo, se houver. |
| `targetfile` | Arquivo alvo, se houver. |
| `targeturl` | URL alvo, se houver. |
| `vulncount` | Número de vulnerabilidades. |
| `attackcount` | Número de ataques (varreduras de logs de servidores web). |
| `ports` | Portas do alvo, se houver. |
| `status` | Status da sessão. |
| `resultsdesc` | Descrição dos resultados. |
| `launcher` | Nome da ferramenta que iniciou a sessão. |

<a id="lapi_emailreport_begin"></a>

## Enviando um relatório por e-mail

```lua
local res = symini.emailreport({
  tracker = 'myemailtrackername',
  filename = 'myreport.pdf',
  subject = 'My Test Report'
})
```

| Chave | Descrição |
|---|---|
| `tracker` **(obrigatória)** | O nome de um [rastreador de e-mail](command-line.md#cli_trackers) já configurado. |
| `filename` **(obrigatória)** | Caminho completo do relatório a ser enviado. |
| `subject` | Assunto do e-mail. Padrão: `Syhunt Scanner Report`. |

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `result` | `true` se o e-mail foi enviado. |
| `resultstr` | Status, incluindo eventual mensagem de erro. |
| `resultdbg` | Log de depuração da operação. |

<a id="lapi_prefupdate"></a>

## Atualizando preferências

| Função | Descrição |
|---|---|
| `symini.prefs_set(key, value [, targeturl])` | Define uma preferência persistente, global ou de um alvo. |
| `symini.prefs_get(key [, targeturl])` | Obtém uma preferência persistente, global ou de um alvo. |

Consulte [Preferências](../reference/preferences.md) para os IDs de preferências disponíveis.

```lua
-- Atualizar uma preferência de site
local res = symini.prefs_set('enabled', true, 'http://127.0.0.1')
-- Atualizar uma preferência global
local res = symini.prefs_set('hybrid.report.company.logo.url', 'https://www.mydomain.com/mylogo.png')
if res.result == true then
  print('Preferência atualizada.')
end
```

**Tabela retornada:**

| Chave | Descrição |
|---|---|
| `result` | `true` se a operação foi bem-sucedida. |
| `resultstr` | Status, incluindo eventual mensagem de erro. |
| `value` | O valor da preferência (somente em `prefs_get`). |

<a id="lapi_extras"></a>

## Outras funções

| Função | Descrição |
|---|---|
| `symini.info.version` | A versão do Syhunt. |
| `symini.getsessionname()` | Retorna um nome de sessão aleatório que pode ser usado para iniciar uma varredura. |
| `symini.getsessioncomparison(sessionname1, sessionname2)` | Retorna uma comparação entre duas sessões. |
| `symini.getsessionlist([maxdays])` | Retorna a lista de sessões anteriores. |
| `symini.runcmd(cmdname)` | Executa um comando (veja abaixo). |

Comandos disponíveis para `symini.runcmd`:

| Comando | Efeito |
|---|---|
| `stop` | Interrompe todos os processos em execução desta instalação do Syhunt. |
| `clearinc` | Limpa o cache de varredura incremental. |
| `clearpref` | Limpa as preferências globais. |
| `clearsite` | Limpa as preferências de sites. |
| `cleartrack` | Remove todos os rastreadores de issues. |

Mais exemplos, incluindo uso baseado em objetos, estão no [repositório scantools](https://github.com/syhunt/scantools/tree/master/src).
