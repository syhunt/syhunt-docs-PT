# Preferências

Esta página lista as principais preferências do Syhunt Hybrid que podem ser definidas pela [linha de comando](../integrations/command-line.md#cli_prefs). As preferências são **globais** (afetam todas as varreduras e alvos) ou **específicas de um site** (aplicam-se à URL de uma única aplicação web).

> [!NOTE]
> As alterações não afetam varreduras já em andamento; elas valem para as varreduras iniciadas depois. As preferências definidas com o `scancore` são persistentes e afetam todas as varreduras futuras.

**Conteúdo**

- [Definindo valores pela CLI](#values)
- [Preferências de site](#prefs_site)
- [Preferências do Dynamic](#prefs_dynamic)
- [Preferências do Code](#prefs_code)
- [Preferências do Forensic](#prefs_forensic)
- [Outras preferências do Hybrid](#prefs_hybrid)
- [Preferências de rastreadores](#prefs_tracker)

<a id="values"></a>

## Definindo valores pela CLI

Com `scancore -prefset` e `scancore -tracker:set`, defina o valor de acordo com o tipo da preferência:

| Tipo | Como definir |
|---|---|
| **boolean** | `-v:true` ou `-v:false` |
| **string** | `-v:valor`, `-v:"meu valor"` ou `-vsecret` (para senhas) |
| **integer** | `-v:1000` |
| **stringlist** | `-fromfile:minhalista.lst` para ler os valores de um arquivo; `-v:[string1],[string2],[etc]` para listar várias strings; ou `-v:valor` / `-v:"meu valor"` para uma única linha |

Definir um valor do tipo errado gera um erro, o que protege as preferências contra alterações acidentais:

```
scancore -prefset:hybrid.report.company.logo.urldark -v:true
Error: Invalid type (provided boolean, must be string)

scancore -tg:http://127.0.0.1 -prefset:enabled -v:1
Error: Invalid type (provided integer, must be boolean)
```

Alguns detalhes:

- **Listas de strings:** em `-v:[valor1],[valor2],[valor3]`, cada valor entre colchetes vira uma linha separada, e o resultado é armazenado assim:
  ```
  valor1
  valor2
  valor3
  ```
- **Espaços:** coloque entre aspas duplas os valores que contêm espaços, por exemplo `-v:"meu valor"` ou `-v:"[meu valor1],[meu valor2]"`. Não use aspas simples.
- **Segredos:** o `-vsecret` pede o valor duas vezes, mascarando a digitação, para que valores sensíveis, como senhas, sejam confirmados e nunca apareçam na linha de comando.
- **Arquivos:** no Windows, o arquivo informado em `-fromfile` pode estar na pasta atual ou ser indicado com o caminho completo. No Linux, sempre informe o caminho completo, por exemplo `-fromfile:/caminho/para/minhalista.lst`.

Use `-prefprint` para exibir o valor atual de qualquer preferência. Para exemplos de como definir preferências globais e de sites, consulte [Linha de Comando: alterando as preferências](../integrations/command-line.md#cli_prefs_exbegin).

---

<a id="prefs_site"></a>

## Preferências de site

As preferências específicas de um site são definidas com `scancore -prefset` e o parâmetro `-tg`, que indica o alvo ([exemplos](../integrations/command-line.md#cli_prefs)). Elas valem apenas para esse alvo, mas para todas as varreduras DAST dele, qualquer que seja a forma de início: o comando `scanurl`, a interface web, a API REST, a API Lua, o módulo PowerShell ou a interface clássica.

Como os alvos são diferenciados:

- **Caminhos diferentes são alvos diferentes.** Por exemplo, `scancore -tg:http://127.0.0.1 -prefset:enabled -v:true` e `scancore -tg:http://127.0.0.1/demo/ -prefset:enabled -v:true` são armazenados separadamente, embora a URL base seja a mesma. Ao executar `scanurl <url>`, são usadas as preferências que correspondem ao caminho dessa URL.
- **Protocolos e portas diferentes são alvos diferentes.** `https://example.com`, `http://example.com` e `http://example.com:8080` têm, cada um, suas próprias preferências.
- **Precisa de vários perfis para a mesma URL?** Acrescente um parâmetro marcador, como `?syhunt_ref=1`, `?syhunt_ref=2` e assim por diante. A aplicação verificada o ignora, mas o Syhunt trata cada variante como um alvo separado.

| Preferência | Tipo | Descrição |
|---|---|---|
| `enabled` | boolean | **true** (padrão): habilita as preferências de site para a URL alvo. Esta é uma chave mestra.<br>**false**: desabilita todas as preferências de site e usa apenas as configurações padrão. |
| `name` | string | Nome descritivo do site alvo (por exemplo, Site da minha empresa). É exibido na interface do Syhunt e não afeta as varreduras. |
| `critlevel` | string | Nível de criticidade. Valores válidos: **undefined** (não definido), **none** (não crítico), **low**, **medium**, **high**, **critical**. É exibido na interface do Syhunt e não afeta as varreduras. Padrão: **undefined**. |
| `dynamic.augmented.detectoob` | boolean | **true** (padrão): habilita a execução de [OAST](technical-specifications.md#OAST) com o Syhunt Signal (recomendado), permitindo detectar vulnerabilidades out-of-band.<br>**false**: desabilita todos os testes OAST. |
| `dynamic.augmented.scanclisource` | boolean | **true** (padrão): habilita a execução de SAST no JavaScript do lado do cliente com o Syhunt Code.<br>**false**: desabilita todos os testes SAST dentro do DAST. |
| `dynamic.advanced.performdos` | boolean | **true** (padrão): habilita os testes de negação de serviço (DoS) contra a aplicação alvo. Ataques DoS buscam interromper o funcionamento normal de uma aplicação explorando vulnerabilidades ou sobrecarregando seus recursos, deixando-a indisponível para usuários legítimos.<br>**false**: desabilita todos os testes de DoS. |
| `dynamic.advanced.performauthforce` | boolean | **true** (padrão): realiza força bruta de autenticação, testando automaticamente usuários e senhas comuns em todas as áreas da aplicação que pedem credenciais.<br>**false**: desabilita a força bruta de autenticação. |
| `dynamic.advanced.forcewebrootstruct` | boolean | **true** (padrão): sempre inclui a raiz web na força bruta de estrutura.<br>**false**: não inclui a raiz web. Ou seja, se a URL alvo for `https://example.com/demo/`, a força bruta atingirá `https://example.com/demo/*`, mas não `https://example.com/*`. |
| `dynamic.advanced.incrementalscan` | string | Varredura incremental. Valores aceitos: **auto** (padrão) ou **disabled**. Desabilitá-la deixa as próximas varreduras mais lentas, pois o scanner não aproveitará os dados das varreduras anteriores. |

### Tecnologias web

O Syhunt Dynamic pode executar testes adaptados às tecnologias usadas por uma aplicação web, o que acelera os testes. Por padrão, ele detecta essas tecnologias automaticamente; por isso, a maioria destas opções tem o valor padrão `auto`.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.slang` | string | A principal linguagem de script do lado do servidor da aplicação alvo. Conhecê-la antecipadamente permite ao Syhunt otimizar a varredura e executar apenas as verificações relevantes para essa linguagem. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.slang`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt determina automaticamente a linguagem do alvo usando seus recursos de identificação (fingerprint). |
| `lang.asp` | A aplicação usa ASP clássico. |
| `lang.aspx` | A aplicação usa ASP.NET. |
| `lang.java` | A aplicação usa Java ou JSP (Java Server Pages). |
| `lang.kotlin` | A aplicação usa Kotlin. |
| `lang.ssjs` | A aplicação usa JavaScript do lado do servidor, como Node.js ou similar. |
| `lang.lua` | A aplicação usa Lua ou LuaJIT. |
| `lang.perl` | A aplicação usa Perl. |
| `lang.php` | A aplicação usa PHP. |
| `lang.python` | A aplicação usa Python. |
| `lang.ruby` | A aplicação usa Ruby ou Ruby on Rails. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.server` | string | O software de servidor web da aplicação alvo. Conhecê-lo antecipadamente permite ao Syhunt otimizar a varredura e executar apenas as verificações relevantes para esse servidor. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.server`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt determina automaticamente o software de servidor do alvo usando seus recursos de identificação. |
| `server.apache` | A aplicação usa Apache. |
| `server.tomcat` | A aplicação usa Apache Tomcat. |
| `server.iis` | A aplicação usa Microsoft IIS. |
| `server.nginx` | A aplicação usa NGINX ou OpenResty. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.os` | string | O sistema operacional da aplicação alvo. Conhecê-lo antecipadamente permite ao Syhunt otimizar a varredura e executar apenas as verificações relevantes para esse sistema. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.os`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt determina automaticamente o sistema operacional do alvo usando seus recursos de identificação. |
| `os.bsd` | A aplicação roda em BSD. |
| `os.linux` | A aplicação roda em uma distribuição Linux. |
| `os.solaris` | A aplicação roda em Solaris. |
| `os.unix` | A aplicação roda em Unix. |
| `os.windows` | A aplicação roda em Windows. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.datsql` | string | O principal banco de dados SQL ou NoSQL da aplicação alvo. Conhecê-lo antecipadamente permite ao Syhunt otimizar a varredura e executar apenas as verificações relevantes para esse banco. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.datsql`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt determina automaticamente o banco de dados do alvo usando seus recursos de identificação. |
| `db.sql.access` | A aplicação usa Microsoft Access. |
| `db.sql.db2` | A aplicação usa DB2. |
| `db.sql.informix` | A aplicação usa Informix. |
| `db.nosql.mongodb` | A aplicação usa MongoDB. |
| `db.sql.mysql` | A aplicação usa MariaDB ou MySQL. |
| `db.sql.oracle` | A aplicação usa Oracle. |
| `db.sql.postgresql` | A aplicação usa PostgreSQL. |
| `db.sql.sqlserver` | A aplicação usa Microsoft SQL Server. |
| `db.sql.sqlite` | A aplicação usa SQLite. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.haswaf` | string | A presença de WAF na aplicação alvo. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.haswaf`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt determina automaticamente se há WAF. |
| `inactive` | Não há WAF. |
| `active` | Há WAF. |
| `ipbypass` | Há WAF, com regra de liberação por IP. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.waf` | string | O fabricante do WAF ativo. Padrão: **auto**. |

Valores aceitos para `dynamic.webtech.waf`:

| Valor | Significado |
|---|---|
| `auto` | O Syhunt tenta determinar automaticamente o fabricante do WAF. |
| `waf.akamai` | Akamai |
| `waf.aws` | AWS |
| `waf.barracuda` | Barracuda |
| `waf.cloudflare` | Cloudflare |
| `waf.f5` | F5 |
| `waf.fortinet` | Fortinet |
| `waf.imperva` | Imperva |
| `waf.msazureappgat` | Microsoft Azure Application Gateway |
| `waf.modsecurity` | ModSecurity |
| `waf.nginx` | NGINX |
| `waf.ogasec` | OGASEC |
| `waf.radware` | Radware |
| `waf.sucuri` | Sucuri |
| `waf.unknown` | Outro |

### Inferência de versões de tecnologias

O Syhunt Dynamic também pode inferir quais tecnologias e versões de componentes um servidor web executa, analisando diversos aspectos da aplicação e de suas respostas. Assim, ele conhece a pilha de tecnologias sem nenhuma informação sua, para testes mais completos.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.webtech.guess.enabled` | boolean | **true** (padrão): tenta identificar as versões do software de servidor web usando o Syhunt HunterSense, mesmo com banners e assinaturas ocultos (recomendado). Esta é uma chave mestra.<br>**false**: desabilita a inferência do software de servidor web. |
| `dynamic.webtech.guess.apache` | boolean | **true** (padrão): identifica a versão do Apache.<br>**false**: desabilita a inferência da versão do Apache. |
| `dynamic.webtech.guess.nginx` | boolean | **true** (padrão): identifica a versão do NGINX.<br>**false**: desabilita a inferência da versão do NGINX. |
| `dynamic.webtech.guess.php` | boolean | **true** (padrão): identifica a versão do PHP.<br>**false**: desabilita a inferência da versão do PHP. |
| `dynamic.webtech.guess.phusion` | boolean | **true** (padrão): identifica a versão do Phusion Passenger.<br>**false**: desabilita a inferência da versão do Phusion Passenger. |
| `dynamic.webtech.guess.modssl` | boolean | **true** (padrão): identifica a versão do mod_ssl.<br>**false**: desabilita a inferência da versão do mod_ssl. |
| `dynamic.webtech.guess.openssl` | boolean | **true** (padrão): identifica a versão do OpenSSL.<br>**false**: desabilita a inferência da versão do OpenSSL. |

### Alcance do rastreamento

Estas opções restringem até onde o rastreador do Syhunt Dynamic explora. Por padrão não há limites de rastreamento, de modo que o scanner pode explorar o site amplamente; ainda assim, ele aplica regras integradas (que a Syhunt chama de *otimizações*) que o guiam pela estrutura e pelo conteúdo do site e aceleram o mapeamento.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.crawling.limitdepth` | boolean | **true**: usa um limite de profundidade. Esta é uma chave mestra.<br>**false** (padrão): sem limite de profundidade. |
| `dynamic.crawling.maxdepth` | integer | Profundidade máxima (exige o limite de profundidade habilitado). Padrão: **0**, que significa sem limite. |
| `dynamic.crawling.limittobase` | boolean | **true**: limita o rastreamento ao caminho da URL inicial e a URLs especificamente permitidas. Esta é uma chave mestra.<br>**false** (padrão): sem essa limitação. Se você habilitar esta opção e, por exemplo, o alvo for `https://example.com/demo/` e a aplicação tiver links para `https://example.com/test/`, o caminho `/test/` será ignorado. Como os caminhos das aplicações web costumam ser interligados, isso restringiria demais a varredura; por isso, a opção vem desabilitada. |
| `dynamic.lists.ignore.allowedpaths` | stringlist | Caminhos cujo rastreamento é permitido (por exemplo, /store/login.php). Padrão: lista vazia. |

As listas a seguir não exigem nenhuma chave mestra habilitada:

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.lists.starturls` | stringlist | URLs iniciais adicionais (por exemplo, /url1.php,/url2.php). Por padrão, o Syhunt Dynamic usa como ponto de partida o caminho da URL alvo informada. Esta chave permite incluir caminhos iniciais adicionais. Por exemplo, se o alvo for `https://example.com/demo/` e você também quiser incluir **/demov2/** e **/demov3/**, mesmo que não haja links para eles em **/demo/**, adicioná-los a esta lista garante que também sejam verificados. Padrão: lista vazia. |
| `dynamic.lists.ignore.urls` | stringlist | Caminhos a ignorar (por exemplo, /about1.php,/about2.php). Padrão: lista vazia. |
| `dynamic.lists.ignore.logoutpaths` | stringlist | Caminhos de logout a ignorar (por exemplo, /logout.php). Padrão: lista vazia. O Syhunt Dynamic já vem configurado para detectar os caminhos de logout mais comuns. |
| `dynamic.lists.ignore.form.names` | stringlist | Formulários a ignorar, pelo nome (por exemplo, search1,search2). Padrão: lista vazia. |

### Autenticação

Estas opções habilitam a autenticação por formulário web, métodos de autenticação de servidor como Basic e Bearer, ou ambos. Consulte [Varredura Autenticada](../scanning/authenticated-scanning.md).

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.formauth.type` | string | Tipo de autenticação. Valores aceitos: **None**, **Standard**, **Smart**, **Recorder**, **Selenium-Auto**, **Selenium-JS**, **Basic**, **Bearer**, **Digest** e **NTLM**. O padrão é **Standard**, ou seja, a autenticação por formulário fica habilitada enquanto os campos de usuário e senha não estiverem vazios. |
| `dynamic.formauth.username` | string | Usuário do formulário. Padrão: vazio. |
| `dynamic.formauth.password` | string | Senha do formulário. Padrão: vazio. |
| `dynamic.formauth.token.encrypted` | string | Token para autenticação Bearer. Padrão: vazio. |
| `dynamic.formauth.script.recorderjson.encrypted` | stringlist | [JSON do Recorder para autenticação](../scanning/authenticated-scanning.md#auth_recorder). Padrão: vazio. Só é usado se o tipo de autenticação for Recorder. |
| `dynamic.formauth.script.seleniumjs.encrypted` | stringlist | [Script Selenium em Node.js para autenticação](../scanning/authenticated-scanning.md#auth_selenium). Padrão: vazio. Só é usado se o tipo de autenticação for Selenium-JS. |
| `dynamic.lists.cookies` | stringlist | Cookies de sessão (por exemplo, ck1=valor;ck=valor). Padrão: vazio. |
| `dynamic.lists.cookiesforced` | stringlist | Cookies forçados (por exemplo, ck1=valor;ck=valor). Padrão: vazio. |

### Lista de vulnerabilidades ignoradas

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.lists.ignore.vulnsbyrules` | stringlist | Vulnerabilidades a ignorar (por ID ou regra), por exemplo vuln:v1:dast-my.js-xss-748. Padrão: vazio. |

<a id="prefs_dynamic"></a>

## Preferências do Dynamic

As preferências do Dynamic são globais: valem para todas as varreduras DAST, qualquer que seja a forma de início (o comando `scanurl`, a interface web, a API REST, a API Lua, o módulo PowerShell ou a interface clássica).

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.checks.dos` | boolean | **true** (padrão): realiza testes de negação de serviço (DoS).<br>**false**: desabilita os testes de DoS. |

### Emulação de navegador

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.emulation.redirect.autofollowinstarturl` | boolean | **true** (padrão): trata automaticamente redirecionamentos para fora do domínio na URL inicial.<br>**false**: desabilita esse tratamento. |
| `dynamic.emulation.mode` | string | Modo de emulação de navegador. Opções válidas: **Chrome**, **Edge**, **Firefox**, **MSIE**, **Opera**, **Safari**. Padrão: **Chrome**. |
| `dynamic.emulation.javascript.execution` | boolean | **true** (padrão): habilita a emulação de JavaScript.<br>**false**: desabilita totalmente a execução e emulação de JavaScript. |
| `dynamic.emulation.javascript.simuser` | boolean | **true** (padrão): simula a interação do usuário (teclas, cliques do mouse etc.).<br>**false**: desabilita totalmente a simulação de interação do usuário. |
| `dynamic.emulation.doxhrcalls` | boolean | **true** (padrão): realiza chamadas XHR.<br>**false**: desabilita totalmente o suporte a chamadas XHR. |
| `dynamic.emulation.javascript.analyzejs` | boolean | **true** (padrão): analisa o código JavaScript.<br>**false**: desabilita a análise de código JS. |
| `dynamic.emulation.javascript.analyzexhr` | boolean | **true** (padrão): analisa as chamadas XHR.<br>**false**: desabilita a análise de chamadas XHR. |
| `dynamic.emulation.cookies.accept` | boolean | **true** (padrão): aceita cookies.<br>**false**: desabilita totalmente o suporte a cookies. |
| `dynamic.emulation.cookies.maxsize` | integer | Tamanho máximo de cookie, em KB. Padrão: **4** (4 KB). |
| `dynamic.emulation.cookies.maxnumber` | integer | Número máximo de cookies por site. Padrão: **50**. |
| `dynamic.emulation.autofill.forms` | boolean | **true** (padrão): preenche automaticamente formulários web (nome, endereço, telefone, e-mail etc.).<br>**false**: desabilita o preenchimento automático de formulários. |
| `dynamic.emulation.autofill.loginforms` | boolean | **true** (padrão): preenche automaticamente formulários de login.<br>**false**: desabilita o preenchimento automático de formulários de login. |
| `dynamic.emulation.redirect.autofollow` | boolean | **true** (padrão): segue redirecionamentos automaticamente.<br>**false**: não segue redirecionamentos automaticamente. |
| `dynamic.emulation.intelparser` | boolean | **true** (padrão): usa análise inteligente de HTML (lida com HTML malformado).<br>**false**: desabilita a análise inteligente de HTML. |
| `dynamic.emulation.usenavbehavior` | boolean | **true** (padrão): usa o comportamento de navegador.<br>**false**: desabilita o comportamento de navegador. |
| `dynamic.emulation.referer.send` | boolean | **true** (padrão): envia o cabeçalho Referer.<br>**false**: não envia o Referer. |
| `dynamic.emulation.useragent` | string | User agent. O padrão é o user agent de um navegador Chrome. |
| `dynamic.emulation.forceuseragent` | boolean | **true** (padrão): força o user agent informado em todas as situações.<br>**false**: não força o user agent informado. |

### Alcance do rastreamento e tempo limite

Estas configurações globais limitam até onde o rastreador vai e quanto tempo cada varredura pode durar.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.crawling.max.linkspersite` | integer | Número máximo de links por servidor. Padrão: **10000**. |
| `dynamic.crawling.max.linksnumber` | integer | Número máximo de links por página. Padrão: **250**. |
| `dynamic.crawling.max.urlsize` | integer | Comprimento máximo de URL, em bytes. Padrão: **16384**. |
| `dynamic.crawling.max.filesize` | integer | Tamanho máximo de resposta, em KB. Padrão: **1024**. |
| `dynamic.crawling.analyze.robots` | boolean | **true** (padrão): analisa o robots.txt (se disponível).<br>**false**: desabilita a análise do robots.txt. |
| `dynamic.options.logout.prevent` | boolean | **true** (padrão): impede que o Syhunt Dynamic acesse acidentalmente a página de logout da aplicação durante o rastreamento ou os testes, evitando o encerramento não intencional da sessão.<br>**false**: desabilita os mecanismos de prevenção de logout. |
| `dynamic.options.logout.detect` | boolean | **true** (padrão): faz login novamente quando a sessão é encerrada prematuramente.<br>**false**: desabilita o novo login. |

| Preferência | Tipo | Descrição |
|---|---|---|
| `syhunt.dynamic.options.timelimit.enabled` | boolean | **false** (padrão): sem limite de tempo.<br>**true**: habilita o limite de tempo. Esta é uma chave mestra. |
| `syhunt.dynamic.options.timelimit.value` | integer | Duração máxima de uma varredura. Padrão: vazio (sem limite). Formatos aceitos: **1d** (um dia), **3h** (três horas), **2h30m** (duas horas e trinta minutos) ou **50m** (cinquenta minutos). Ao atingir essa duração, a varredura é cancelada automaticamente. |

### Intervalo entre requisições

Define um intervalo, em milissegundos, entre as requisições. Não recomendamos usá-lo em DAST, que normalmente envolve milhões de requisições: qualquer intervalo pode tornar as varreduras muito mais longas.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.options.delay.enabled` | boolean | **false** (padrão): sem intervalo entre requisições.<br>**true**: habilita o intervalo entre requisições. Esta é uma chave mestra. |
| `dynamic.options.delay.value` | integer | Intervalo, em ms. Padrão: **3000**. |
| `dynamic.options.delay.userandom` | boolean | **false** (padrão): sem intervalo aleatório.<br>**true**: usa um intervalo aleatório entre as requisições. |

### Evasão

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.evasion.detection.honeypot` | boolean | **true** (padrão): detecta se a aplicação alvo é um honeypot.<br>**false**: desabilita a detecção de honeypot. |
| `dynamic.evasion.detection.waf` | boolean | **true** (padrão): tenta detectar se a aplicação está atrás de um WAF (firewall de aplicação web).<br>**false**: desabilita a detecção de WAF. |
| `dynamic.evasion.reqdistrand` | boolean | **true**: distribui as requisições aleatoriamente durante o rastreamento (experimental).<br>**false** (padrão): sem distribuição aleatória. |
| `dynamic.evasion.evadeflt` | boolean | **true** (padrão): usa evasão de filtros.<br>**false**: desabilita a evasão de filtros. Esta é uma chave mestra. |
| `dynamic.checks.sub.xssev` | boolean | **true** (padrão): técnica de evasão: técnicas comuns de evasão de filtros de XSS.<br>**false**: desabilita essas técnicas. |
| `dynamic.checks.sub.utf8dev` | boolean | **true** (padrão): técnica de evasão: decodificação UTF-8.<br>**false**: desabilita essa técnica. |

### Protocolo

Os valores padrão abaixo são os recomendados: eles são otimizados para lidar com o tráfego web de forma eficiente e oferecem o melhor desempenho de varredura.

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.protocol.version` | string | Versão do protocolo. Aceita: HTTP/1.1 e HTTP/1.0. Padrão (e recomendado): **HTTP/1.1**. |
| `dynamic.protocol.ssl.type` | string | Tipo de SSL. Aceita: all, SSLv2, SSLv3, TLSv1, TLSv1_1, TLSv1_2, TLSv1_3, SSHv2. Padrão (e recomendado): **all**, que funciona com todos os tipos de SSL suportados em vez de se restringir a um. |
| `dynamic.protocol.keepalive` | boolean | **true** (padrão): habilita o suporte a Keep-Alive (recomendado).<br>**false**: desabilita o Keep-Alive, o que deixa as varreduras mais lentas, pois o Keep-Alive acelera as conexões. |
| `dynamic.protocol.usegzip` | boolean | **true** (padrão): habilita o suporte à compressão GZIP (recomendado).<br>**false**: desabilita o GZIP, o que deixa as varreduras mais lentas, pois a compressão acelera as conexões. |
| `dynamic.protocol.mknocache` | boolean | **true** (padrão): faz requisições sem cache (no-cache).<br>**false**: desabilita as requisições sem cache. |
| `dynamic.protocol.timeout.value` | integer | Tempo limite, em ms. Padrão: **10000**. |
| `dynamic.protocol.retries` | integer | Número de novas tentativas após o tempo limite. Padrão: **2**. |
| `syhunt.dynamic.options.augmented.jndiserver` | string | Servidor JNDIExploit (host sem porta) para detecção de Log4Shell. Padrão: vazio. |
| `dynamic.lists.protocol.customhdr` | stringlist | Cabeçalhos de requisição personalizados (por exemplo, X-Custom:UmValor). Padrão: vazio. |

### Lista de vulnerabilidades ignoradas

Cada vulnerabilidade DAST de um relatório termina com seu ID de exclusão, a forma mais simples e recomendada de suprimir um resultado. Para cenários mais amplos, use [regras de exclusão](../scanning/ignore-rules.md).

| Preferência | Tipo | Descrição |
|---|---|---|
| `dynamic.lists.ignore.vulnsbyrules` | stringlist | Vulnerabilidades a ignorar (por regra ou ID). Padrão: lista vazia. |

---

<a id="prefs_code"></a>

## Preferências do Code

As preferências do Code são globais: valem para todas as varreduras SAST, qualquer que seja a forma de início (o comando `scancode`, SAST dentro do DAST, a interface web, a API REST, a API Lua, o módulo PowerShell ou a interface clássica).

| Preferência | Tipo | Descrição |
|---|---|---|
| `code.checks.inflt` | boolean | **true** (padrão): analisa a filtragem de entradas no código-fonte da aplicação. Isso é essencial para eliminar falsos positivos, pois verifica o tratamento adequado das entradas do usuário e reduz detecções incorretas.<br>**false**: desabilita a análise de filtragem de entradas. |
| `code.options.target.tfsver` | string | Compatibilidade com versões do TFS. Aceita: latest, 2017, 2015, 2013, 2012, 2010. Padrão: **latest** (2018 ou posterior). |

### Lista de vulnerabilidades ignoradas

Cada vulnerabilidade SAST de um relatório termina com seu ID de exclusão, a forma mais simples e recomendada de suprimir um resultado; para cenários mais amplos, use [regras de exclusão](../scanning/ignore-rules.md). No SAST, em vez de `code.lists.ignore.vulnsbyrules`, a prática recomendada é usar um [arquivo `.vulnignore`](../scanning/code-scanning.md#advanced_vulnignore) no repositório verificado.

| Preferência | Tipo | Descrição |
|---|---|---|
| `code.lists.ignore.vulnsbyrules` | stringlist | Vulnerabilidades a ignorar (por regra ou ID). Padrão: lista vazia. |

### Tempo limite

| Preferência | Tipo | Descrição |
|---|---|---|
| `syhunt.code.options.timelimit.enabled` | boolean | **false** (padrão): sem limite de tempo.<br>**true**: habilita o limite de tempo. Esta é uma chave mestra. |
| `syhunt.code.options.timelimit.value` | integer | Duração máxima de uma varredura. Padrão: vazio (sem limite). Formatos aceitos: **1d** (um dia), **3h** (três horas), **2h30m** (duas horas e trinta minutos) ou **50m** (cinquenta minutos). Ao atingir essa duração, a varredura é cancelada automaticamente. |

---

<a id="prefs_forensic"></a>

## Preferências do Forensic

As preferências do Forensic são globais: valem para todas as varreduras FAST, iniciadas pelo comando `scanlog` ou pela interface clássica.

| Preferência | Tipo | Descrição |
|---|---|---|
| `insight.lists.ignorelist.paths` | stringlist | Lista de caminhos a ignorar (por exemplo, /robots.txt,robots2.txt). Padrão: lista vazia. |
| `insight.lists.ignorelist.srcips` | stringlist | Lista de IPs a ignorar (por exemplo, 1.1.1.1,2.2.2.2). Padrão: lista vazia. |
| `insight.options.logformat` | string | Formato do log. Aceita: auto, common, apache, iis, ncsa, nginx. Padrão: **auto** (detecta o formato automaticamente). |
| `insight.options.profileatk` | boolean | **true** (padrão): monta o perfil do atacante.<br>**false**: desabilita a criação de perfis de atacantes. |
| `insight.options.resolveip` | boolean | **true**: resolve os endereços IP dos atacantes (mais lento).<br>**false** (padrão): não resolve os endereços IP (mais rápido). |

---

<a id="prefs_hybrid"></a>

## Outras preferências do Hybrid

Estas preferências globais valem para todas as varreduras, qualquer que seja a forma de início (os comandos `scancode` ou `scanurl`, a interface web, a API REST, a API Lua, o módulo PowerShell ou a interface clássica).

| Preferência | Tipo | Descrição |
|---|---|---|
| `hybrid.report.defaultlanguage` | string | ID do idioma dos relatórios. Consulte a lista de [idiomas disponíveis](../integrations/command-line.md#report). Padrão: **EN** (relatórios em inglês). |
| `hybrid.report.company.logo.urldark` | string | URL do logotipo da organização para fundo escuro (por exemplo, `http://www.mycompany.com/logo.png`). Padrão: vazio. |
| `hybrid.lists.riskfine` | stringlist | Redefinição de risco. Cada linha deve usar o formato [ID único da verificação=severidade], por exemplo C-1603660271-7241=low. Padrão: lista vazia. |
| `syhunt.hybrid.advanced.ai.openai.apikey.encrypted` | string | Chave da OpenAI para habilitar os recursos com IA do Syhunt. Padrão: vazio. |
| `syhunt.hybrid.advanced.ai.options.exrepsolut` | boolean | **true** (padrão): compartilha trechos de código vulnerável para obter exemplos de correção. Exige `ai_reviewconsent: true` em um arquivo `.syhunt-ci.yml` na raiz de cada repositório alvo.<br>**false**: não compartilha trechos de código vulnerável, mesmo que existam arquivos de consentimento. |

---

<a id="prefs_tracker"></a>

## Preferências de rastreadores

As preferências de rastreadores são definidas com `scancore -tracker:set`, usando `-to` para indicar o rastreador e `-v` para o valor ([exemplos](../integrations/command-line.md#cli_trackers)). Elas valem apenas para esse rastreador.

Para exemplos de como criar rastreadores e definir suas preferências, consulte [Linha de Comando: usando rastreadores de issues](../integrations/command-line.md#clitrackerexbegin).

As chaves aplicáveis dependem do tipo de rastreador: por exemplo, um rastreador de e-mail usa `smtp.targetport`, enquanto um rastreador do GitHub a ignora. As seções após a tabela listam as chaves normalmente necessárias para cada tipo.

| Preferência | Tipo | Descrição |
|---|---|---|
| `project.name` | string | Nome do projeto (por exemplo, owner/repo). Padrão: vazio. |
| `auth.username` | string | Usuário. Padrão: vazio. |
| `auth.password` | string | Senha. Padrão: vazio. |
| `auth.token.encrypted` | string | Token de autenticação. Pode ser usado para definir um token de acesso pessoal (PAT) de um serviço. Padrão: vazio. |
| `auth.targethost` | string | Nome do host. Padrão: vazio. |
| `api.url` | string | URL da API/do servidor. Padrão: vazio. |
| `custom.fields` | stringlist | Campos personalizados. Padrão: lista vazia. |
| `custom.labels` | stringlist | Rótulos personalizados. Padrão: lista vazia. |
| `scan.minseverity` | string | Severidade mínima. Valores aceitos: Info, Low, Medium ou High. Padrão: **Info**. |
| `notifyonfailonly` | boolean | **true**: notifica apenas quando uma condição de reprovação é atendida.<br>**false** (padrão): sempre notifica (independentemente de condições de aprovação/reprovação). |

### Chaves por tipo de rastreador

| Rastreador | Chaves a definir |
|---|---|
| **Email** | `auth.targethost` (host SMTP), `auth.username` e `auth.password` (credenciais), além das chaves de e-mail abaixo. |
| **GitHub** | `project.name` (`owner/repo`), `auth.token.encrypted` (token de acesso pessoal) e, opcionalmente, `custom.labels` (por exemplo, `Vulnerability`). |
| **GitLab** | `project.name` (`owner/repo`), `api.url` (URL do servidor GitLab), `auth.token.encrypted` (token de acesso pessoal) e, opcionalmente, `custom.labels`. |
| **Jira** | `project.name` (projeto Jira), `api.url` (URL do servidor Jira), `auth.username` e `auth.password` e, opcionalmente, `custom.labels`, `custom.fields` e `jira.defitname`. |
| **DefectDojo** | `api.url` (URL do servidor), `auth.token.encrypted` (token de API) e, opcionalmente, `scan.minseverity`, `custom.labels` (tags, por exemplo `scan`) e as chaves do DefectDojo abaixo. |
| **Faraday** | `api.url` (URL do servidor), `project.name` (workspace; padrão `my_workspace`), `auth.username` e `auth.password`. |

### E-mail

| Preferência | Tipo | Descrição |
|---|---|---|
| `smtp.targetport` | integer | Porta SMTP. Padrão: **587**. |
| `message.from` | string | Endereço do remetente. Padrão: vazio. |
| `message.tolist` | string | Endereço do destinatário, ou uma lista de endereços separados por vírgula. Padrão: vazio. |
| `message.subject` | string | Assunto da mensagem. Padrão: vazio. |

### Jira

| Preferência | Tipo | Descrição |
|---|---|---|
| `jira.defitname` | string | Tipo de issue padrão. Padrão: **Task**. |

Use `custom.fields` para referenciar campos personalizados pelo nome, e não pelo ID. Para um campo personalizado do tipo SelectList, declare-o como `customfield_10100.value=UmValorPersonalizado`.

### DefectDojo

| Preferência | Tipo | Descrição |
|---|---|---|
| `scan.testtitle` | string | Contexto: título do teste. Padrão: vazio. |
| `scan.engagementname` | string | Contexto: nome do engagement. Padrão: vazio. |
| `scan.producttypename` | string | Contexto: nome do tipo de produto. Padrão: vazio. |
| `scan.productname` | string | Contexto: nome do produto. Padrão: vazio. |
| `scan.active` | boolean | **true** (padrão): marca os resultados como ativos.<br>**false**: marca-os como inativos. |
| `scan.verified` | boolean | **true** (padrão): marca os resultados como verificados.<br>**false**: marca-os como não verificados. |
| `scan.skipduplicates` | boolean | **true**: ignora duplicatas.<br>**false** (padrão): não ignora duplicatas. |
| `scan.closeoldfindings` | boolean | **true**: fecha resultados antigos.<br>**false** (padrão): não fecha resultados antigos. |
| `scan.pushtojira` | boolean | **true**: envia os resultados ao Jira.<br>**false** (padrão): não envia ao Jira. |
