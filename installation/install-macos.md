# Instalação no macOS

> **Aplica-se a:** Syhunt Hybrid 7.2 no macOS Sequoia e versões anteriores

**Conteúdo**

- [Introdução](#intro)
- [Instalação no macOS (Apple Silicon ou Intel)](#installing)
- [Parallels Desktop: Debian ARM64](#debianarm64)
- [Parallels Desktop: Ubuntu ou Kali Linux ARM64](#ubuntuarm64)
- [Parallels Desktop: habilitando o Rosetta](#rosetta)
- [Parallels Desktop: instalando o Wine 8.0](#wine8)

<a id="intro"></a>

## Introdução

O Syhunt Hybrid 7.2 é compatível com o macOS Sequoia e versões anteriores. A edição para macOS é a edição *Carbon*: ela é instalada sobre o Wine e funciona tanto em Macs com Apple Silicon (por meio do Rosetta) quanto em Macs com Intel.

Se preferir virtualização, o Syhunt Hybrid 7.1.6 também roda em Linux ARM64 (Ubuntu, Debian ou Kali Linux) dentro do [Parallels Desktop](https://www.parallels.com/products/desktop) no macOS. Isso exige uma licença **Pro** do Parallels; a licença Standard não é compatível.

<a id="introend"></a>
<a id="installing"></a>

## Instalação no macOS (Apple Silicon ou Intel)

1. Leia e aceite o [EULA do Syhunt](https://www.syhunt.com/en/?n=Legal.EULA) antes de executar qualquer um dos comandos abaixo.
2. [Baixe o Java](https://java.com/en/download/) para macOS (`jre-<versão>-macosx-x64.dmg`) e instale-o, caso ainda não o tenha.
3. Instale o Wine64, caso ainda não o tenha:
   - [Apple Silicon (M1, M2, M3 ou M4)](wine.md#macos)
   - [Intel](wine.md#macos_intel)
4. Instale o wget:
   ```bash
   brew install wget
   ```
5. Baixe o instalador do Syhunt (arquivo `.jar`), clique no ícone com a tecla Control pressionada e escolha **Abrir**. Leia atentamente o EULA antes de aceitá-lo e conclua o instalador (*Next → Next → Finish*). As [ferramentas de linha de comando](../integrations/command-line.md) do Syhunt ficam então prontas para uso. Para mais opções, consulte [Execução do instalador](install-linux.md#finishinstall).
6. [Habilite a interface web do Syhunt](web-ui.md#firststeps).

> [!NOTE]
> Se, após uma atualização do macOS, a varredura de um repositório Git falhar com **invalid active developer path**, execute `xcode-select --install` para reparar o comando `git`.

<a id="debianarm64"></a>

## Parallels Desktop: Debian ARM64

> **Aplica-se a:** Debian 12.6 ARM64 em Macs com Apple Silicon usando o Parallels Desktop

1. Instale o Java:
   ```bash
   sudo apt install default-jre
   ```
2. *(Opcional)* Instale o Git, se pretende fazer varreduras de repositórios Git:
   ```bash
   sudo apt install git
   ```
3. Habilite e instale o Rosetta (consulte [Habilitando o Rosetta](#rosetta)).
4. Instale a versão AMD64 do Wine64. O Debian 12.6 ARM64 instala a versão 8.0 por padrão:
   ```bash
   sudo apt install wine64:amd64
   ```
5. Execute `wine ipconfig` uma vez para que o Wine se configure.
6. Instale o Syhunt: baixe o instalador `.jar` e siga [Execução do instalador](install-linux.md#finishinstall).
7. [Habilite a interface web do Syhunt](web-ui.md#firststeps).

<a id="ubuntuarm64"></a>

## Parallels Desktop: Ubuntu ou Kali Linux ARM64

> **Aplica-se a:** Ubuntu 24.04 ARM64 ou Kali Linux 2024.2 ARM64 em Macs com Apple Silicon usando o Parallels Desktop

1. Leia e aceite o [EULA do Syhunt](https://www.syhunt.com/en/?n=Legal.EULA).
2. Crie uma máquina virtual dedicada ao Syhunt.
3. Atualize as listas de pacotes:
   ```bash
   sudo apt-get update
   ```
4. Instale o Java com o SVE desativado:
   ```bash
   # Adicione uma vez ao perfil do shell
   echo 'export JAVA_TOOL_OPTIONS="$JAVA_TOOL_OPTIONS -XX:UseSVE=0"' | sudo tee /etc/profile.d/java-nosve.sh
   # Recarregue o ambiente de login (ou abra um novo terminal)
   source /etc/profile.d/java-nosve.sh
   # Instale o OpenJDK 17 e confirme a versão
   sudo apt install openjdk-17-jre
   java --version
   ```
5. Habilite e instale o Rosetta (consulte [Habilitando o Rosetta](#rosetta)). Pule este passo se estiver usando a imagem gratuita **Ubuntu with Rosetta** do Parallels.
6. O pacote padrão do Wine é a versão 9, que não funciona bem com o Rosetta. Primeiro habilite o Wine 8.0 (consulte [Instalando o Wine 8.0](#wine8)) e depois instale-o:
   ```bash
   sudo apt install libwine:amd64=8.0~repack-4 wine64:amd64=8.0~repack-4
   ```
   Se o comando `wine` não estiver disponível depois disso, execute `sudo apt install wine`. Confirme a versão com `wine --version`.
7. Execute `wine ipconfig` uma vez para que o Wine se configure.
8. Instale o Syhunt: baixe o instalador `.jar` e siga [Execução do instalador](install-linux.md#finishinstall).
9. [Habilite a interface web do Syhunt](web-ui.md#firststeps).

<a id="rosetta"></a>

## Parallels Desktop: habilitando o Rosetta

> **Aplica-se a:** Ubuntu 24.04 ARM64 ou Kali Linux 2024.2 ARM64 em Macs com Apple Silicon usando o Parallels Desktop

1. Quando a instalação da máquina virtual terminar, desligue-a. Nas configurações da VM, vá em **Hardware → CPU & Memory**, ative **Use Rosetta to run x86_64 binaries** e ligue a VM novamente.
2. Instale o suporte ao Rosetta:
   ```bash
   wget https://kb.parallels.com/Attachments/kcs-193687/rosetta_x86_sources.sh
   chmod +x rosetta_x86_sources.sh
   sudo ./rosetta_x86_sources.sh enable    # exibe "AMD64 architecture enabled"
   sudo apt update
   ```

<a id="wine8"></a>

## Parallels Desktop: instalando o Wine 8.0

> **Aplica-se a:** Ubuntu 24.04 ARM64 ou Kali Linux 2024.2 ARM64 em Macs com Apple Silicon usando o Parallels Desktop

> [!WARNING]
> Use este procedimento apenas em ambientes de teste. Ele instala pacotes do Debian 12 (*Bookworm*) no Ubuntu 24.04 ou no Kali Linux 2024.2. Atualmente funciona, mas misturar pacotes de distribuições diferentes não é uma solução estável a longo prazo. Estamos trabalhando em um método mais limpo e atualizaremos este guia quando ele estiver disponível.

1. Adicione o repositório do Debian 12, fixado para ser usado apenas pelo Wine:
   ```bash
   echo 'deb http://deb.debian.org/debian bookworm main contrib non-free non-free-firmware' |
     sudo tee /etc/apt/sources.list.d/debian-bookworm.list

   sudo tee /etc/apt/preferences.d/99-wine8 <<'EOF'
   Package: wine* libwine* fonts-wine*
   Pin: release n=bookworm
   Pin-Priority: 990

   Package: *
   Pin: release n=bookworm
   Pin-Priority: 100
   EOF
   ```
2. Adicione a chave de assinatura do repositório Bookworm:
   ```bash
   sudo mkdir -p /etc/apt/keyrings &&
   curl -fsSL https://ftp-master.debian.org/keys/archive-key-12.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/debian-bookworm.gpg > /dev/null &&
   echo "deb [signed-by=/etc/apt/keyrings/debian-bookworm.gpg] http://deb.debian.org/debian bookworm main" | sudo tee /etc/apt/sources.list.d/debian-bookworm.list &&
   sudo apt update
   ```
3. Adicione os repositórios do Ubuntu para pacotes AMD64:
   ```bash
   sudo tee /etc/apt/sources.list.d/ubuntu-amd64.list > /dev/null <<EOF
   deb [arch=amd64] http://archive.ubuntu.com/ubuntu noble main restricted universe multiverse
   deb [arch=amd64] http://archive.ubuntu.com/ubuntu noble-updates main restricted universe multiverse
   deb [arch=amd64] http://archive.ubuntu.com/ubuntu noble-security main restricted universe multiverse
   deb [arch=amd64] http://archive.ubuntu.com/ubuntu noble-backports main restricted universe multiverse
   EOF
   ```
4. Atualize o APT e confirme que o Wine 8.0 está disponível. A saída deve incluir `8.0~repack-4`:
   ```bash
   sudo apt update
   apt-cache madison wine | grep 8.0
   ```
5. Continue a partir do [passo 6 das instruções para Ubuntu/Kali](#ubuntuarm64).
