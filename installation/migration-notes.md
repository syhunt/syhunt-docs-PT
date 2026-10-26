# Notas de Migração

Leia as notas de todas as versões entre a sua versão atual e a que você está instalando.

## Migração para o Syhunt 7.2

- **A interface clássica de desktop foi descontinuada.** A interface de desktop mostrada abaixo não é mais incluída; ela foi substituída pela nova interface web.

  ![](../images/screenshot-syhunthybridv6.png)

- **Mesmos recursos no Linux.** Recursos antes disponíveis apenas no Windows, como a autenticação baseada em Selenium e o rastreador AJAX avançado, agora também estão disponíveis no Linux.
- **O Forensic Scanner está disponível apenas pela CLI.** Use o comando `scanlog`. Uma atualização futura permitirá ver os resultados das varreduras forenses na interface web.
- **Revise seus alvos.** Abra a [tela Targets](https://127.0.0.1:8018/syhunt/?n=targets) e procure ícones de alerta ao lado de algum alvo. Passe o mouse sobre o ícone para ver quais preferências ou configurações precisam de atenção. Em especial:
  - O método de autenticação **Selenium-Py** está obsoleto. Migre para um dos novos métodos: Smart, Recorder, Selenium-Auto ou Selenium-JS.
  - O **AI-Powered Login** foi descontinuado. Migre para Smart, Recorder ou Selenium-Auto.
- **As extensões Plus agora vêm incluídas.** Não é mais necessário instalar o instalador separado das extensões Plus; o instalador da versão 7.2 já inclui todos os componentes necessários.

## Migração para o Syhunt 7.0

No Windows Server, certifique-se de que o **WebView2 Runtime** está instalado. Sem ele, o Syhunt exibe um alerta ao abrir sua interface. Você pode obtê-lo no [Evergreen Standalone Installer](https://developer.microsoft.com/en-us/microsoft-edge/webview2/).

## Migração para o Syhunt 6.9.26.1

Esta versão muda o funcionamento das preferências de site no Syhunt Dynamic: diferentes caminhos de URL inicial no mesmo domínio agora podem ter suas próprias preferências. Por exemplo, `https://mydomain/`, `https://mydomain/admin/` e `https://mydomain/members/` passam a ser URLs iniciais distintas, cada uma com suas próprias preferências de site.

A mudança se aplica às preferências definidas ao iniciar uma varredura sob demanda, nas varreduras agendadas, na tela de alvos dinâmicos e pela ferramenta de CLI `scancore`.

Revise suas preferências de site existentes. Se uma URL inicial inclui um caminho (ou seja, não é a raiz do site), suas preferências agora mostrarão os valores padrão, e será necessário recriar configurações anteriores, como credenciais e restrições de rastreamento.

## Migração para o Syhunt 6.9.9

- No Linux, baixe e instale esta atualização manualmente, em vez de usar o `scanupdate`.
- Verifique se as varreduras de código agendadas e em pipelines de repositórios Git apontam para o branch correto. Versões anteriores usavam o branch `master` por padrão; a partir da 6.9.9, o nome do branch fica vazio por padrão e o cliente Git escolhe o branch padrão do repositório, a menos que você defina um explicitamente.
- Certifique-se de atender aos novos [requisitos de conexão com a Internet](install-windows.md#sysreq_net).

## Migração para o Syhunt 6.9.7 ou posterior

Até a versão 6.9.6, o Syhunt para Windows armazenava os dados do usuário em `%AppData%\Local\Syhunt`. Como parte de melhorias de arquitetura, a versão 6.9.7 e posteriores os armazenam em `%ProgramData%\Syhunt`.

Antes de atualizar, exporte suas preferências para poder importá-las depois:

1. Abra o Syhunt Hybrid 6.9.6 (ou sua versão mais antiga).
2. Escolha ![](../images/menu.png) **Menu → Import & Export → Export Preferences**.
3. Salve o arquivo de backup em um local fácil de encontrar, com um nome fácil de lembrar.
4. Instale o Syhunt 6.9.7 ou posterior.
5. Escolha ![](../images/menu.png) **Menu → Import & Export → Import Preferences**, selecione o arquivo de backup e clique em **Open**.
6. Todas as configurações da instalação anterior, incluindo as varreduras agendadas, estarão importadas e ativas.

### *(Opcional)* Migração do histórico e dos resultados de sessões

- Para manter suas sessões anteriores, mova os arquivos e pastas de `%AppData%\Local\Syhunt\Sessions` para `%ProgramData%\Syhunt\Sessions`. Elas voltarão a aparecer na tela Past Sessions.
- Se necessário, mova também `%AppData%\Local\Syhunt\Output` para `%ProgramData%\Syhunt\Output`.
- As demais pastas em `%AppData%\Local\Syhunt\` contêm dados temporários e podem ser excluídas com segurança.

### Modo AppData forçado

No Windows, o Syhunt 6.9.7.1 e posteriores podem ser forçados a continuar usando a pasta local AppData em vez da ProgramData: crie um arquivo vazio chamado `LocalAppData.json` no local padrão do Syhunt (consulte o [guia de Linha de Comando](../integrations/command-line.md) para ver os locais padrão).

> [!WARNING]
> Alguns recursos importantes, como o agendador de varreduras, **não** funcionam neste modo.
