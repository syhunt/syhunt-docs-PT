# Visão Geral da Instalação e Windows

> **Aplica-se a:** Syhunt Hybrid 7.2

**Conteúdo**

- [Introdução](#intro)
- [Edições Windows e Linux/macOS](#versions)
- [Instalação no Windows](#windows)
- [Instalação no macOS](#mac)
- [Instalação no Linux](#linux)
- [Instalação da extensão Syhunt Sandcat para navegador](#sandcat)
- [Requisitos de sistema](#sysreq)
- [Requisitos de conexão com a Internet](#sysreq_net)
- [Atualização do Syhunt](#update)
- [Desinstalação do Syhunt](#uninstall)

<a id="intro"></a>

## Introdução

O Syhunt Hybrid 7 é um scanner de segurança de aplicações multiplataforma de 64 bits. Ele roda no Windows, no macOS e em distribuições Linux como Ubuntu Desktop/Server, Debian e Fedora, praticamente sem esforço de configuração. O Syhunt Hybrid realiza testes de segurança de aplicações web e mobile (DAST e SAST) e se integra a diversos sistemas para integração e varredura contínuas.

![](../images/dynamic_scan_linux.png)

<a id="versions"></a>

### Edições Windows e Linux/macOS

| | **Hybrid para Windows** | **Hybrid para Linux/macOS** |
|---|---|---|
| Servidor da interface web | OpenResty para HTTPS e HTTP | NGINX para HTTPS, OpenResty como back-end |
| Rastreador AJAX avançado | ✅ Motor Chromium | ✅ Motor Firefox |
| Análise dinâmica aumentada (DAST + OAST) | ✅ | ✅ |
| Análise de APIs (AAST + OAST) | ✅ | ✅ |
| Análise de código-fonte de aplicações web (SAST) | ✅ | ✅ |
| Análise de código-fonte de aplicações mobile (MAST) | ✅ | ✅ |
| Análise forense (FAST) | ✅ (somente CLI) | ✅ (somente CLI) |
| Recursos com IA | ✅ Exemplos de código corrigido<br>✅ Pontuação de confiança por IA | ✅ Exemplos de código corrigido<br>✅ Pontuação de confiança por IA |
| Autenticação avançada | ✅ Recorder, Selenium | ✅ Recorder, Selenium |
| Integrações | ✅ Shell ([PowerShell](../integrations/powershell.md))<br>✅ Rastreadores de issues (GitHub, GitLab, Jira…)<br>✅ Ferramentas de CI/CD (GitLab, GitHub, Bitbucket, Jenkins)<br>✅ WAFs para virtual patching<br>✅ URLs de projetos Azure DevOps / TFS (não Git) | ✅ Shell (Bash)<br>✅ Rastreadores de issues (GitHub, GitLab, Jira…)<br>✅ Ferramentas de CI/CD (GitLab, GitHub, Bitbucket, Jenkins)<br>✅ WAFs para virtual patching<br>✅ URLs de projetos Azure DevOps / TFS (não Git) |
| Agendador de varreduras | ✅ | ✅ |
| Sistemas operacionais suportados | **Oficialmente:**<br>Windows 11<br>Windows 10<br>Windows Server 2016 a 2025 | **Oficialmente:**<br>macOS Sequoia 15.4.1 ou posterior (Apple Silicon)<br>Ubuntu Server/Desktop 18.10 e posteriores<br>Debian 9 e posteriores<br>Fedora 32 e posteriores<br>**Não oficialmente (testados com sucesso):**<br>[Outras distribuições Linux](../reference/technical-specifications.md#linuxcompat_begin)<br>macOS Monterey |
| Disponibilidade | [Disponível](#windows) (binários nativos Win64) | [Disponível](#linux) (instalação baseada no Wine)<br>[Consulte sobre binários nativos](https://www.syhunt.com/en/?n=Syhunt.ContactUs) para sua distribuição |

<a id="windows"></a>

## Instalação no Windows

**Clientes registrados:** sigam os passos iniciais do [Guia de Boas-Vindas](../getting-started/welcome-guide.md) para baixar, instalar e começar a usar a versão completa do Syhunt Hybrid. Usuários não registrados podem usar o Syhunt Community.

1. *(Opcional)* Se pretende fazer varreduras de repositórios Git, instale o [Git for Windows](https://gitforwindows.org/).
2. Baixe o instalador do Syhunt Hybrid, `syhunt-hybrid-<versão>.exe`.
3. Clique duas vezes no arquivo baixado para executá-lo.
4. Leia atentamente o EULA antes de aceitá-lo.
5. Conclua o instalador (*Next → Next → Finish*). Ao clicar em **Finish**, o Syhunt é aberto e a tela do Launcher aparece.
6. Se necessário, [habilite a interface web do Syhunt](web-ui.md#firststeps).

**E agora?** Leia o [Início Rápido](../getting-started/quick-start.md) e os [guias de integração](../README.md#integrações).

<a id="mac"></a>

## Instalação no macOS

Consulte o [guia de instalação para macOS](install-macos.md).

<a id="linux"></a>

## Instalação no Linux

O Syhunt Hybrid para Linux é a edição *Carbon*: uma instalação baseada no Wine, compatível com a maioria dos desktops e servidores Linux de 64 bits. Consulte o [guia de instalação para Linux](install-linux.md) para os passos específicos de cada distribuição.

<a id="sandcat"></a>

## Instalação da extensão Syhunt Sandcat para navegador

Desde a versão 7.2, o Syhunt Hybrid inclui uma extensão para o Edge, o Chrome, o Brave e outros navegadores baseados no Chromium. Ela permite o [login manual](../scanning/authenticated-scanning.md#auth_manual) e testes assistidos pelo navegador. O nome homenageia o Sandcat Browser, o navegador integrado do Syhunt 7.1 e versões anteriores, que oferecia login manual de forma semelhante.

1. No navegador, abra **Menu → Extensões → Gerenciar extensões**.
2. Ative o **Modo do desenvolvedor** (canto superior direito).
3. Clique em **Carregar sem compactação** e selecione a pasta da extensão Sandcat:
   - Windows: `C:\Program Files\Syhunt Hybrid\Extensions\SandcatExtension`
   - Linux: `/home/<usuário>/syhunt-hybrid/carbon/sandcat`
   - macOS: `/Applications/Syhunt Hybrid/carbon/sandcat`
4. O Syhunt Sandcat passa a aparecer na lista de extensões.
5. Abra novamente a página inicial da interface web. A mensagem **Extension detected and ready** confirma que tudo funciona.

Se você acessa a interface web por um endereço IP, domínio ou subdomínio diferente de `localhost`, configure esse endereço na extensão:

1. Clique em **Detalhes** na extensão e depois em **Opções da extensão**.
2. Selecione **Use custom Syhunt UI origin**.
3. Escolha o protocolo (`http` ou `https`).
4. Informe o host, *sem* o prefixo do protocolo (`http://` ou `https://`).
5. Informe a porta usada pela interface web.
6. Clique em **Save**.
7. Abra novamente a página inicial da interface web e verifique a mensagem **Extension detected and ready**.

<a id="sysreq"></a>

## Requisitos de sistema

Consulte as [Especificações Técnicas](../reference/technical-specifications.md#specsbegin).

<a id="sysreq_net"></a>

### Requisitos de conexão com a Internet

A máquina em que o Syhunt é executado deve conseguir fazer requisições HTTP(S) aos seguintes endereços:

| Domínio | Portas | Finalidade |
|---|---|---|
| Seu(s) domínio(s) alvo | 80, 443\* | O domínio que hospeda a aplicação web ou o código que você quer verificar. |
| Quaisquer domínios de recursos, ou domínios específicos | 80, 443 | Opcional, mas recomendado: permite que o Syhunt analise arquivos JavaScript e outros recursos hospedados externamente durante o DAST ou o SAST. |
| `syhunt.fra1.cdn.digitaloceanspaces.com` | 443 | Obrigatório: recursos de instalação e atualização automática. |
| `www.syhunt.net` | 80, 443 | Obrigatório: recursos para relatórios HTML/PDF, notificações de atualização, atualização automática e mais. |
| `signal.syhunt.net` | 80, 443 | Obrigatório durante o DAST para realizar OAST (importante). |
| `api.openai.com` | 443 | Opcional: recursos com IA. |
| `fonts.googleapis.com` | 80, 443 | Obrigatório: fontes para relatórios HTML/PDF. |
| `www.google.com` | 443 | Obrigatório: Google JSAPI para relatórios HTML/PDF. |
| `www.gstatic.com` | 443 | Obrigatório: Google JSAPI para relatórios HTML/PDF. |

\* Se o seu alvo usa uma porta não padrão (como 8080), ou se você se conecta ao Git por SSH ou outro protocolo, libere também essas portas.

> [!WARNING]
> Se você usa um firewall pessoal, permita que o Syhunt faça conexões de saída com a Internet.

<a id="finishinstall"></a>

No Linux e no macOS, o instalador é um programa Java. Consulte [Execução do instalador](install-linux.md#finishinstall).

<a id="update"></a>

## Atualização do Syhunt

As atualizações podem ser baixadas e instaladas a partir do site da Syhunt. O Syhunt Hybrid 6.8.4 e versões posteriores também anunciam novas versões no Launcher e nos relatórios.

No Linux e no macOS, execute `scanupdate` para verificar se há atualizações; se houver, o Syhunt pergunta se deve baixá-las e instalá-las. Execute `scanupdate auto` para instalar as atualizações disponíveis sem pedir confirmação.

Não é necessário desinstalar o Syhunt antes de instalar uma nova versão, exceto ao atualizar o Syhunt Community CLI no Windows.

<a id="uninstall"></a>

## Desinstalação do Syhunt

**Windows:** use o atalho de desinstalação no menu Iniciar (na pasta *Syhunt Hybrid* ou *Syhunt Community*) ou remova o Syhunt em **Painel de Controle → Programas e Recursos**.

**Linux e macOS:** vá até a pasta em que o Syhunt está instalado e execute:

```
java -jar Uninstall.jar
```
