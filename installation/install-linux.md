# Instalação no Linux

> **Aplica-se a:** Syhunt Hybrid 7.2

O Syhunt Hybrid roda no Ubuntu (Server ou Desktop) e na maioria das distribuições Linux de 64 bits praticamente sem esforço de configuração, e quase sem nenhum ajuste no Kali Linux. A edição para Linux (*Carbon*) é uma instalação baseada no Wine. Para comparar os recursos com a edição para Windows, consulte a [Visão Geral da Instalação](install-windows.md#versions).

<a id="dists_begin"></a>

## Visão geral

A instalação do Syhunt no Linux segue sempre o mesmo padrão:

1. Leia e aceite o [EULA do Syhunt](https://www.syhunt.com/en/?n=Legal.EULA) antes de executar qualquer um dos comandos abaixo.
2. Instale o **Java** (necessário para o instalador), se ainda não estiver instalado.
3. *(Opcional)* Instale o **Git** se pretende fazer varreduras de repositórios Git.
4. Instale o **Wine64**, seguindo o [guia do Wine](wine.md) para sua distribuição.
5. [Execute o instalador do Syhunt](#finishinstall).

As seções abaixo trazem os comandos exatos para cada distribuição.

<a id="dists_end"></a>

**Distribuições:** [Kali](#kali) · [Parrot OS](#parrot) · [Ubuntu](#ubuntu) · [Debian](#debian) · [Fedora](#fedora) · [CentOS / RHEL](#centos) · [AlmaLinux](#almalinux) · [Rocky Linux](#rockylinux) · [Oracle Linux](#oraclelinux) · [Amazon Linux 2](#amazonlinux2) · [Amazon Linux 2023](#amazonlinux2023) · [Arch / Manjaro](#archlinux) · [Linux Mint](#mint) · [MX Linux](#mxlinux) · [openSUSE](#opensuse) · [elementary OS](#elementaryos) · [Deepin](#deepin) · [Solus](#solus)

<a id="kali"></a>

## Kali Linux

> **Aplica-se a:** Kali Linux 2024.3 ou posterior

O Kali já inclui a maior parte das dependências do Syhunt, então você só precisa do Wine64 e do próprio Syhunt.

1. Instale o Wine64 seguindo o [guia do Wine para Debian/Kali](wine.md#debian).
2. [Execute o instalador do Syhunt](#finishinstall).

<a id="parrot"></a>

## Parrot OS

> **Aplica-se a:** Parrot OS 6.1 ou posterior

Assim como o Kali, o Parrot OS já inclui a maior parte das dependências do Syhunt.

1. Instale o Wine64 seguindo o [guia do Wine para Debian](wine.md#debian).
2. [Execute o instalador do Syhunt](#finishinstall).

<a id="ubuntu"></a>

## Ubuntu

> **Aplica-se a:** Ubuntu Desktop/Server 18.10 a 24.04 e posteriores; KDE neon 2020.03 ou posterior

1. Instale o Java:
   ```bash
   sudo apt install openjdk-17-jre
   ```
2. *(Opcional)* Instale o Git:
   ```bash
   sudo apt install git
   ```
3. Instale o Wine64 seguindo o [guia do Wine para Ubuntu](wine.md#ubuntu).
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="debian"></a>

## Debian

> **Aplica-se a:** Debian 9, 10 ou 12 (com interface gráfica ou mínima)

1. Instale o Wine64 seguindo o [guia do Wine para Debian](wine.md#debian).
2. Instale o Java (no Debian 9, provavelmente já está instalado):
   ```bash
   sudo apt install default-jre
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo apt install git
   ```
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="fedora"></a>

## Fedora

> **Aplica-se a:** Fedora 32, 39, 40 e 41

1. Aplique todas as atualizações pendentes e reinicie.
2. Instale o Java:
   ```bash
   sudo yum install java
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo yum install git
   ```
4. Instale o Wine64 seguindo o [guia do Wine para Fedora](wine.md#fedora).
5. [Execute o instalador do Syhunt](#finishinstall).

> [!TIP]
> Se o OpenJDK 17 estiver instalado e o instalador falhar com um erro como
> `Exception in thread "main" java.lang.UnsatisfiedLinkError: Can't load library: /usr/lib/jvm/java-17-openjdk-…/lib/libawt_xawt.so`,
> instale os pacotes do OpenJDK que faltam e execute o instalador novamente:
> ```bash
> sudo dnf install java-17-openjdk java-17-openjdk-devel java-17-openjdk-headless
> ```

<a id="centos"></a>
<a id="redhat"></a>

## CentOS e Red Hat Enterprise Linux

> **Aplica-se a:** CentOS 7 ou 8 (Everything ou Minimal); Red Hat Enterprise Linux

1. Instale o Wine64 seguindo o [guia do Wine para CentOS](wine.md#centos).
2. Instale o Java:
   ```bash
   sudo yum -y update
   sudo yum install java    # ou: sudo yum install java-1.8.0-openjdk
   ```
3. *(Opcional; no Minimal, necessário para varreduras de repositórios Git)* Instale o Git:
   ```bash
   sudo yum install git
   ```
4. *(Instalações Minimal)* Instale o wget:
   ```bash
   sudo yum install wget
   ```
5. [Execute o instalador do Syhunt](#finishinstall).

<a id="almalinux"></a>
<a id="rockylinux"></a>
<a id="oraclelinux"></a>

## AlmaLinux, Rocky Linux e Oracle Linux

> **Aplica-se a:** AlmaLinux 9, Rocky Linux 9, Oracle Linux 9

1. Instale o Wine64 seguindo o guia do Wine para sua distribuição: [AlmaLinux](wine.md#almalinux), [Rocky Linux](wine.md#rockylinux) ou [Oracle Linux](wine.md#oraclelinux).
2. Instale o Java:
   ```bash
   sudo yum -y update
   sudo yum install java    # ou: sudo yum install java-1.8.0-openjdk
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo yum install git
   ```
4. *(AlmaLinux e Rocky Linux)* Instale o wget:
   ```bash
   sudo yum install wget
   ```
5. Permita que processos não confinados executem arquivos que exigem a permissão `execmod` do SELinux. Isso resolve um conflito com o Wine; enfraquece levemente o SELinux, mas não o desativa.
   ```bash
   sudo setsebool -P selinuxuser_execmod on
   ```
6. [Execute o instalador do Syhunt](#finishinstall).

<a id="amazonlinux2"></a>

## Amazon Linux 2

1. Instale o Wine64 seguindo o [guia do Wine para Amazon Linux 2](wine.md#amazonlinux2).
2. Instale o Java:
   ```bash
   sudo yum -y update
   sudo yum install java
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo yum install git
   ```
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="amazonlinux2023"></a>

## Amazon Linux 2023

1. Instale o Wine64 seguindo o [guia do Wine para Amazon Linux 2023](wine.md#amazonlinux2023).
2. Instale o Java:
   ```bash
   sudo yum -y update
   sudo yum install java
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo yum install git
   ```
4. Permita a permissão `execmod` do SELinux, como explicado na [seção do AlmaLinux](#almalinux):
   ```bash
   sudo setsebool -P selinuxuser_execmod on
   ```
5. [Execute o instalador do Syhunt](#finishinstall).

<a id="archlinux"></a>
<a id="manjaro"></a>

## Arch Linux e Manjaro

> **Aplica-se a:** Arch Linux 2019 ou posterior, Manjaro 19

1. Atualize o banco de dados do pacman:
   ```bash
   sudo pacman -Syy
   ```
2. Instale o Java 8:
   ```bash
   sudo pacman -S jre8-openjdk
   ```
3. *(Opcional)* Instale o Git:
   ```bash
   sudo pacman -S git
   ```
4. Instale o Wine64:
   - **Arch Linux:** siga o [guia do Wine para Arch Linux](wine.md#archlinux).
   - **Manjaro:** execute `sudo pacman -S wine` e depois `wine64 ipconfig`. O Wine é iniciado e se configura sozinho; pressione **I** se ele pedir para instalar componentes ausentes.
5. [Execute o instalador do Syhunt](#finishinstall).

<a id="mint"></a>

## Linux Mint

> **Aplica-se a:** Linux Mint 18, 19 e 20

1. O Java já vem instalado no Linux Mint.
2. *(Opcional)* Instale o Git:
   ```bash
   sudo apt install git
   ```
3. Instale o Wine64 seguindo o [guia do Wine para Linux Mint](wine.md#mint).
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="mxlinux"></a>

## MX Linux

> **Aplica-se a:** MX Linux 19.1 ou posterior

1. O Java e o Git já vêm instalados no MX Linux 19.
2. Instale o Wine64 e execute-o uma vez para que ele se configure:
   ```bash
   sudo apt install wine
   wine64 ipconfig
   ```
3. [Execute o instalador do Syhunt](#finishinstall).

<a id="opensuse"></a>

## openSUSE

> **Aplica-se a:** openSUSE Leap 15, Leap 42 ou posterior, Tumbleweed

1. *(Opcional)* Instale o Git:
   ```bash
   zypper in git        # ou, se não for encontrado: zypper in git-core
   ```
2. Instale o Wine64 seguindo o [guia do Wine para openSUSE](wine.md#opensuse).
3. [Execute o instalador do Syhunt](#finishinstall).

<a id="elementaryos"></a>

## elementary OS

> **Aplica-se a:** elementary OS 5.0 e 5.1

- **elementary OS 5.1:** siga os [passos do Ubuntu](#ubuntu). Pode ser necessário reiniciar após instalar o Wine64.
- **elementary OS 5.0:** leia primeiro [este aviso](wine.md#elementaryos). Se ainda quiser prosseguir, faça isso por sua conta e risco.

<a id="deepin"></a>

## Deepin

> **Aplica-se a:** Deepin 15.9

1. Instale o Java:
   ```bash
   sudo apt install default-jre
   ```
2. *(Opcional)* Instale o Git:
   ```bash
   sudo apt install git
   ```
3. Instale o Wine64 e execute-o uma vez para que ele se configure:
   ```bash
   sudo apt install wine
   wine64 ipconfig
   ```
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="solus"></a>

## Solus

> **Aplica-se a:** Solus 4.1

1. Instale o Java (o comando `java` ficará em `/usr/lib64/openjdk-8/bin/java` ou `/usr/lib64/openjdk-11/bin/java`):
   ```bash
   sudo eopkg install openjdk-8    # ou: sudo eopkg install openjdk-11
   ```
2. *(Opcional)* Instale o Git:
   ```bash
   sudo eopkg install git
   ```
3. Instale o Wine64 seguindo o [guia do Wine para Solus](wine.md#solus).
4. [Execute o instalador do Syhunt](#finishinstall).

<a id="finishinstall"></a>

## Execução do instalador (Linux e macOS)

1. Baixe o instalador do Syhunt Hybrid com um navegador, `wget` ou `curl`.
2. Execute o instalador:

   | Edição | Comando |
   |---|---|
   | Hybrid | `java -jar syhunt-hybrid-<versão>.jar` |
   | Hybrid em servidor sem interface gráfica | `java -jar syhunt-hybrid-<versão>.jar -console` |
   | Community | `java -jar <arquivo>` |

   No Linux, se o `binfmt-support` estiver instalado (`sudo apt install binfmt-support`), você pode tornar o arquivo executável (`chmod a+rx <arquivo>.jar`) e executá-lo diretamente, por exemplo `./syhunt-hybrid-<versão>.jar` (acrescente `-console` em servidores sem interface gráfica).
3. Leia atentamente o EULA antes de aceitá-lo e conclua o instalador (*Next → Next → Finish*). Por padrão, o Syhunt é instalado em:
   - Linux: `/home/<usuário>/syhunt-hybrid` ou `/home/<usuário>/syhunt-community`
   - macOS: `/Applications/Syhunt Hybrid/` ou `/Applications/Syhunt Community/`
4. [Habilite a interface web do Syhunt](web-ui.md#firststeps).

<a id="finishconsole"></a>

### Modo console

Se o instalador for executado em modo console:

1. Leia o EULA e digite **1** para aceitá-lo (ou **2** para recusá-lo; o Syhunt não pode ser instalado sem aceitá-lo).
2. Pressione **Enter** para usar o caminho de instalação padrão.
3. Digite **1** para continuar.
4. Digite **Y** para instalar o Syhunt Core.
5. Digite **1** para continuar. A mensagem **Console installation done** confirma a instalação.

**E agora?** Leia o [Início Rápido](../getting-started/quick-start.md) e os [guias de integração](../README.md#integrações).
