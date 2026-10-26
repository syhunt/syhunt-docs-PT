# Métodos de Varredura

> **Aplica-se a:** Syhunt Hybrid 7.0.11

Um *método de varredura* (hunt method) define o que o Syhunt procura e com que intensidade ele testa. O **Application Scan** é o padrão; escolha outro método quando precisar de uma varredura mais focada ou mais profunda.

<a id="begin"></a>
<a id="huntmethods_begin"></a>
<a id="diffstart"></a>

## Comparação

| Método de varredura | Nome na CLI | Tipo | Força bruta | Injeção | DoS | Demorado |
|---|---|---|---|---|---|---|
| **Application Scan** (padrão) | `appscan` | ▣ | S | S | S | N |
| **Application Scan** (foco no lado do servidor) | `appscanss` | ▣ | S | S | S | N |
| **Structure Brute Force** | `structbf` | ■ | S (profunda) | N | N | S (muito) |
| **Old & Backup Files** | `fileold` | ■ | S | N | N | S |
| **Fault Injection** | `faultinj` | ▣ | N | S | S | N |
| **OWASP Top 10** | `top10` | ▣ | N | P (Top 10) | S | N |
| **OWASP Mobile Top 10** | `top10mob` | □ | N | P (Mobile Top 10) | N | N |
| **CWE Top 25** | `top25cwe` | ▣ | N | P (Top 25) | S | N |
| **OWASP PHP Top 5** | `top5php` | ▣ | N | P (Top 5) | N | N |
| **Cross-Site Scripting** | `xss` | ▣ | N | P (XSS) | N | N |
| **SQL Injection** | `sqlinj` | ▣ | N | P (SQL) | N | N |
| **File Inclusion** | `fileinc` | ▣ | N | P (FI) | N | N |
| **Unvalidated Redirects** | `unvredir` | ▣ | N | P (UR) | N | N |
| **Malware Content** | `malscan` | ▣ | P (malware) | P (malware) | N | N |
| **Passive** | `passive` | ▣ | N | N | N | N |
| **Spider Only** | `spider` | ■ | N | N | N | N |
| **Complete Scan** | `complete` | ▣ | S | S | S | S (muito) |
| **Complete Scan, No DoS** | `compnodos` | ▣ | S | S | N | S (muito) |
| **Complete Scan, Paranoid** | `comppnoid` | ▣ | S (profunda) | S | S | S (muito) |

**S** = sim, **N** = não, **P** = parcial (limitado à categoria indicada).

<a id="type"></a>

**Tipo de teste**

- ▣ Híbrido (caixa-cinza): dinâmico e de código
- ■ Somente dinâmico (caixa-preta)
- □ Somente de código (caixa-branca)

<a id="timecon"></a>

**Demorado:** *S* significa que o método executa verificações e mutações de ataque adicionais, e que o número de verificações cresce com a quantidade de diretórios encontrados durante o rastreamento.

<a id="diffend"></a>
<a id="descstart"></a>

## Descrição dos métodos

<a id="hmas"></a>

### Application Scan

Encontra falhas em aplicações web próprias, em software de servidor web e em componentes de terceiros. Rastreia o site e ataca tanto a estrutura do site quanto as aplicações, incluindo testes de injeção de falhas como XSS, injeção de SQL e inclusão de arquivos.

<a id="hmsbf"></a>

### Structure Brute Force

Procura por:

- Scripts vulneráveis comuns
- Arquivos comuns
- Arquivos personalizados (definidos pelo usuário)
- Exposição de bancos de dados
- Backdoors baseados na web

O número de verificações cresce com a quantidade de diretórios encontrados durante o rastreamento.

<a id="hmfileold"></a>

### Old & Backup Files

Testa extensões de backup e de arquivos antigos em cada item da estrutura mapeada do site.

<a id="hmtop10"></a>

### OWASP Top 10

Procura especificamente os riscos do OWASP Top 10 (2017):

1. A1: Injection (Injeção)
2. A2: Broken Authentication (Quebra de autenticação)
3. A3: Sensitive Data Exposure (Exposição de dados sensíveis)
4. A4: XML External Entities (XXE)
5. A5: Broken Access Control (Quebra de controle de acesso)
6. A6: Security Misconfiguration (Configuração de segurança incorreta)
7. A7: Cross-Site Scripting (XSS)
8. A8: Insecure Deserialization (Desserialização insegura)
9. A9: Using Components with Known Vulnerabilities (Uso de componentes com vulnerabilidades conhecidas)
10. A10: Insufficient Logging & Monitoring (Registro e monitoramento insuficientes)

<a id="hmtop25"></a>

### CWE Top 25

Procura especificamente as [CWE Top 25 Most Dangerous Software Errors de 2019](https://cwe.mitre.org/top25/archive/2019/2019_cwe_top25.html).

<a id="hmphptop5"></a>

### OWASP PHP Top 5

Procura especificamente as cinco principais vulnerabilidades de PHP segundo a OWASP:

1. Execução remota de comandos
2. Cross-site scripting (XSS), incluindo DOM XSS
3. Injeção de SQL
4. Configuração incorreta do PHP
5. Ataques ao sistema de arquivos, incluindo inclusão de arquivos

<a id="hmfi"></a>

### Fault Injection

Procura apenas vulnerabilidades de injeção de falhas. Todas as verificações que não envolvem injeção são desativadas, e o Syhunt se concentra em injeção de SQL, XSS, inclusão de arquivos e falhas semelhantes.

<a id="hmxss"></a>

### Cross-Site Scripting (XSS)

Procura especificamente vulnerabilidades de XSS, incluindo XSS baseado em DOM.

<a id="hmsqli"></a>

### SQL Injection

Procura especificamente vulnerabilidades de injeção de SQL e NoSQL.

<a id="hmfileinc"></a>

### File Inclusion

Procura especificamente vulnerabilidades de inclusão de arquivos e de travessia de diretórios (directory traversal).

<a id="hmunvredir"></a>

### Unvalidated Redirects

Procura especificamente vulnerabilidades de redirecionamento não validado.

<a id="hmmalware"></a>

### Malware Content

Procura especificamente conteúdo malicioso, como:

- Backdoors web
- Conteúdo malicioso
- Parâmetros de depuração ocultos

<a id="hmpassive"></a>

### Passive

Mapeia a estrutura do site e relata problemas sem realizar nenhum ataque, por exemplo:

- Vulnerabilidades em JavaScript do lado do cliente
- Fraquezas em formulários
- Divulgação de tecnologias web
- Cabeçalhos HTTP inseguros
- Software de servidor desatualizado e vulnerável
- Scripts referenciados desatualizados e vulneráveis
- Comentários HTML suspeitos
- Divulgação de código-fonte
- Conteúdo malicioso sendo servido

<a id="hmspider"></a>

### Spider Only

Mapeia a estrutura do site sem testar nem relatar nenhuma vulnerabilidade ou fraqueza.

<a id="hmcmp"></a>

### Complete Scan

Testa todos os tipos de vulnerabilidades de aplicações web usando todas as mutações e técnicas de teste de invasão disponíveis, incluindo ataques de manipulação de cabeçalhos. Pode demorar bastante em servidores com muitas pastas e pontos de entrada.

<a id="hmcnd"></a>

### Complete Scan, No DoS

Igual ao Complete Scan, mas com os testes de negação de serviço desativados.

<a id="hmcpn"></a>

### Complete Scan, Paranoid

Igual ao Complete Scan, com uma força bruta de estrutura mais profunda. Pode demorar muito, principalmente em sites grandes. Também executa uma força bruta com verificação tripla para servidores que diferenciam maiúsculas de minúsculas, testando todas as variações de cada nome de arquivo (tudo em maiúsculas, tudo em minúsculas, iniciais maiúsculas e assim por diante).

<a id="descend"></a>
<a id="end"></a>
