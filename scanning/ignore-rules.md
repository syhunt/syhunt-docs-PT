# Regras de Exclusão

> **Aplica-se a:** Syhunt Hybrid 7.2

As regras de exclusão (ignore rules) impedem que vulnerabilidades correspondentes sejam relatadas. Elas complementam os IDs de exclusão (exibidos ao final de cada vulnerabilidade no relatório) quando você precisa suprimir um conjunto mais amplo de resultados. Você pode adicioná-las:

- por alvo, na lista de exclusões do alvo (consulte [Varredura Dinâmica](dynamic-scanning.md#advanced_vulnignore));
- por repositório, em um arquivo `.vulnignore` (consulte [Varredura de Código-Fonte](code-scanning.md#advanced_vulnignore));
- globalmente, para todas as varreduras (consulte [Regras globais](#global) abaixo).

## Sintaxe

Uma regra começa com `rule:` seguido de pares `parâmetro=valor` separados por vírgulas. Coloque o par entre aspas duplas se o valor contiver espaços ou vírgulas.

### Exemplos

| Regra | Efeito |
|---|---|
| `rule:path=*,checkid=C-1603659845-9557` | Ignora qualquer vulnerabilidade com o ID de verificação `C-1603659845-9557`. |
| `rule:path=*,name=XSS` | Ignora qualquer vulnerabilidade com "XSS" no título. |
| `rule:path=/demo/*,name=XSS` | Ignora vulnerabilidades com "XSS" no título cujo caminho começa com `/demo/`. |
| `rule:path=*,"name=Web Technology Disclosure"` | Ignora qualquer vulnerabilidade com "Web Technology Disclosure" no título. |
| `rule:path=/demo.php,lines=10` | *(SAST)* Ignora vulnerabilidades na linha 10 de `/demo.php`. |
| `rule:path=/demo.php,"lines=10,11"` | *(SAST)* Ignora vulnerabilidades nas linhas 10 e 11 de `/demo.php`. |

### Parâmetros

| Parâmetro | Comparado com |
|---|---|
| `path` **(obrigatório)** | O caminho afetado. Aceita os curingas `?` e `*`. |
| `checkid` | O ID de verificação da vulnerabilidade. |
| `name` | O título da vulnerabilidade. |
| `params` | O(s) parâmetro(s) afetado(s). Separe vários parâmetros com vírgulas. |
| `risk` | O risco da vulnerabilidade: `low`, `medium`, `high` ou `info`. |
| `module` | O módulo que encontrou a vulnerabilidade: `dyn` ou `code`. Se omitido, a regra vale para resultados do Dynamic e do Code. |
| `lines` | A(s) linha(s) de código-fonte afetada(s). Separe várias linhas com vírgulas. |
| `cve` | Um ID de CVE entre as referências CVE da vulnerabilidade. |
| `cwe` | Um número de CWE entre as referências CWE da vulnerabilidade. |

<a id="global"></a>

## Regras globais

Para criar regras que valham para todas as varreduras dinâmicas ou de código:

1. Abra a tela Connectors (![](../images/menu.png) **Menu → Connectors**) e adicione um conector do tipo **List** chamado `VULNIGNORE-DAST` (para varreduras dinâmicas) ou `VULNIGNORE-SAST` (para varreduras de código).
2. Clique no conector na lista para adicionar ou editar suas regras.
