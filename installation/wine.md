# Instalando o Wine

O Syhunt Hybrid para Linux e macOS (a edição *Carbon*) roda sobre o Wine64. Esta página explica como instalar o Wine64 em cada sistema suportado. Depois de instalar o Wine, volte ao guia de [Linux](install-linux.md) ou de [macOS](install-macos.md) para instalar o Syhunt.

> [!IMPORTANT]
> Leia e aceite o [EULA do Syhunt](https://www.syhunt.com/en/?n=Legal.EULA) antes de executar qualquer um dos comandos abaixo.

**Sistemas:** [macOS (Apple Silicon)](#macos) · [macOS (Intel)](#macos_intel) · [Ubuntu](#ubuntu) · [Debian / Kali](#debian) · [Fedora](#fedora) · [CentOS](#centos) · [AlmaLinux](#almalinux) · [Rocky Linux](#rockylinux) · [Oracle Linux](#oraclelinux) · [Amazon Linux 2](#amazonlinux2) · [Amazon Linux 2023](#amazonlinux2023) · [Arch Linux](#archlinux) · [Linux Mint](#mint) · [openSUSE](#opensuse) · [elementary OS](#elementaryos) · [Solus](#solus)

> [!TIP]
> Em todos os sistemas, o último passo é executar `wine64 ipconfig` uma vez. O Wine é iniciado pela primeira vez e se configura sozinho; se ele pedir para instalar componentes ausentes (como o Wine Mono ou o Wine Gecko), pressione **I** para instalá-los. Ao final, aparece uma mensagem como `wine: configuration in '/home/<usuário>/.wine' has been updated`.

<a id="macos"></a>

## macOS (Apple Silicon)

> **Aplica-se a:** macOS Sequoia em Apple Silicon (M1, M2, M3, M4)

1. Instale o [Homebrew](https://brew.sh), caso ainda não o tenha. Abra o **Terminal** (em `/Applications/Utilities/`) e execute:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
   ```
   Informe sua senha de administrador quando solicitado. Ao final, o Homebrew exibe instruções para configurar o `~/.zprofile`; siga-as.
2. Instale o XQuartz (talvez seja preciso informar a senha de administrador novamente):
   ```bash
   brew install --cask xquartz
   ```
3. Instale o Rosetta:
   ```bash
   softwareupdate --install-rosetta --agree-to-license
   ```
4. Instale o Wine:
   ```bash
   brew install --cask --no-quarantine wine-stable
   ```
   Se o seu Homebrew não aceitar `--no-quarantine`, execute estes comandos:
   ```bash
   brew install --cask wine-stable
   xattr -dr com.apple.quarantine /Applications/Wine\ Stable.app
   ```
5. Após a mensagem `wine-stable was successfully installed!`, execute `wine64 ipconfig`.

<a id="macos_intel"></a>

## macOS (Intel)

> **Aplica-se a:** macOS Big Sur e Monterey em Intel

1. Instale o [Homebrew](https://brew.sh), caso ainda não o tenha. Abra o **Terminal** e execute:
   - macOS Catalina e posteriores:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
     ```
   - macOS High Sierra, Sierra, El Capitan e anteriores:
     ```bash
     /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
     ```

   Informe sua senha de administrador quando solicitado e siga as instruções do Homebrew para configurar o `~/.zprofile`.
2. Instale o XQuartz:
   ```bash
   brew install --cask xquartz
   ```
3. Instale o Wine (consulte a seção do Apple Silicon para a alternativa caso `--no-quarantine` não seja aceito):
   ```bash
   brew install --cask --no-quarantine wine-stable
   ```
4. Execute `wine64 ipconfig`.

<a id="ubuntu"></a>

## Ubuntu

> **Aplica-se a:** Ubuntu 18.10 a 24.04 e posteriores

```bash
sudo apt install wine-stable
wine ipconfig
```

O Syhunt é de 64 bits e não precisa do Wine de 32 bits. Se quiser instalá-lo mesmo assim:

```bash
sudo dpkg --add-architecture i386 && sudo apt-get update
sudo apt-get install wine32
```

<a id="debian"></a>

## Debian e Kali Linux

> **Aplica-se a:** Debian 9, 10 ou 12 (com interface gráfica ou mínima); Kali Linux 2024.3

```bash
sudo apt-get update
sudo apt install wine
wine64 ipconfig
```

<a id="fedora"></a>

## Fedora

> **Aplica-se a:** Fedora 32, 39 e 40

1. Verifique se há atualizações:
   ```bash
   sudo dnf check-update
   ```
2. Execute `wine64`. Quando for perguntado se deseja instalar o `wine-core`, digite **yes** e depois **Y** para confirmar as alterações.

   Se o download dos pacotes do Wine falhar, aplique todas as atualizações, reinicie e tente novamente:
   ```bash
   sudo dnf update
   sudo reboot
   sudo dnf install wine
   ```
3. Execute `wine64 ipconfig` e pressione **I** para instalar o Wine Mono e o Wine Gecko quando solicitado. O Wine pode exibir mensagens de depuração em segundo plano; elas podem ser ignoradas.

<a id="centos"></a>

## CentOS

> **Aplica-se a:** CentOS 7.7, 7.8, 8.0 e 8.2 (Everything ou Minimal)

1. Atualize o sistema:
   ```bash
   sudo yum -y update
   ```
   Se isso falhar com **No URLs in mirrorlist** (o CentOS 8 chegou ao fim de vida), aponte os repositórios para o vault do CentOS. O DNF voltará a funcionar, mas você não receberá mais atualizações ([detalhes](https://stackoverflow.com/questions/70926799/centos-through-a-vm-no-urls-in-mirrorlist)):
   ```bash
   sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*
   sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Linux-*
   sudo yum -y update
   ```
2. Instale o EPEL e o Wine:
   ```bash
   sudo yum install epel-release
   sudo yum install wine
   ```
   Se o Wine64 não puder ser instalado porque falta o SDL2, instale primeiro o SDL2 e depois execute `sudo yum install wine` novamente:
   - Habilite o repositório que fornece o SDL2:
     ```bash
     sudo dnf config-manager --set-enabled PowerTools
     ```
   - CentOS 8.2.3 e posteriores:
     ```bash
     sudo dnf --enablerepo=PowerTools install SDL2
     ```
   - CentOS 8.4 e posteriores:
     ```bash
     sudo dnf -y update
     sudo dnf groupinstall 'Development Tools' -y
     sudo dnf config-manager --set-enabled powertools
     sudo dnf -y install SDL2-devel
     ```
3. Execute `wine64 ipconfig`.

<a id="almalinux"></a>
<a id="rockylinux"></a>

## AlmaLinux e Rocky Linux

> **Aplica-se a:** AlmaLinux 9, Rocky Linux 9

```bash
sudo yum -y update
sudo dnf install yum-utils
sudo yum install epel-release
sudo dnf config-manager --set-enabled crb
sudo dnf install mingw64-zlib
sudo yum install wine
wine64 ipconfig
```

<a id="oraclelinux"></a>

## Oracle Linux

> **Aplica-se a:** Oracle Linux 9

```bash
sudo yum -y update
sudo yum install epel-release
sudo yum install SDL2-devel
sudo yum install wine
```

Se o Wine64 não puder ser instalado porque nenhum pacote fornece `mingw64-zlib` e `mesa-libOSMesa`, habilite o repositório CodeReady Builder, instale o `mingw64-zlib` e instale o Wine novamente:

```bash
sudo dnf config-manager --set-enabled ol9_codeready_builder
sudo dnf install mingw64-zlib
sudo yum install wine
```

Por fim, execute `wine64 ipconfig`.

<a id="amazonlinux2"></a>

## Amazon Linux 2

```bash
sudo yum update -y
sudo yum groupinstall "Development Tools" -y
sudo amazon-linux-extras install epel -y
```

Instale duas dependências importantes do Wine a partir de pacotes compatíveis do Oracle Linux e, em seguida, o próprio Wine:

```bash
sudo yum install -y https://yum.oracle.com/repo/OracleLinux/OL8/appstream/x86_64/getPackage/spirv-tools-libs-2023.1-2.el8.x86_64.rpm
sudo yum install -y https://yum.oracle.com/repo/OracleLinux/OL7/9/base/x86_64/getPackage/isdn4k-utils-3.2-99.el7.x86_64.rpm
sudo yum install -y wine
wine64 ipconfig
```

<a id="amazonlinux2023"></a>

## Amazon Linux 2023

1. Adicione os repositórios de que o Wine precisa, usando o script auxiliar da Syhunt:
   ```bash
   sudo yum groupinstall "Development Tools" -y
   wget https://syhunt.fra1.cdn.digitaloceanspaces.com/tools/linux/al2023-createrepos.sh
   chmod +x al2023-createrepos.sh
   ./al2023-createrepos.sh
   ```
2. Instale o Wine e execute-o uma vez:
   ```bash
   sudo yum update -y
   sudo yum install wine -y
   wine64 ipconfig
   ```
3. Para evitar conflitos, remova os repositórios do Oracle Linux 9 adicionados pelo script, que não são mais necessários:
   ```bash
   sudo rm /etc/yum.repos.d/epel.repo
   sudo rm /etc/yum.repos.d/appstream.repo
   sudo rm /etc/yum.repos.d/crb.repo
   ```

<a id="archlinux"></a>

## Arch Linux

> **Aplica-se a:** Arch Linux 2019

1. Habilite o suporte a multilib no pacman: edite `/etc/pacman.conf` (por exemplo, `sudo vi /etc/pacman.conf`), remova o comentário destas linhas e salve o arquivo:
   ```ini
   [multilib]
   Include = /etc/pacman.d/mirrorlist
   ```
2. *(Opcional)* Atualize as chaves do pacman:
   ```bash
   sudo pacman-key --init
   sudo pacman-key --populate archlinux
   sudo pacman-key --keyserver keyserver.ubuntu.com --refresh-keys
   sudo pacman -S archlinux-keyring
   ```
3. Atualize o banco de dados de pacotes e instale o Wine:
   ```bash
   sudo pacman -Syy
   sudo pacman -S wine
   ```
4. Execute `wine64 ipconfig` e pressione **I** para instalar o Wine Mono e o Wine Gecko quando solicitado.

<a id="mint"></a>

## Linux Mint

> **Aplica-se a:** Linux Mint 18, 19 e 20

### Linux Mint 20

```bash
sudo apt-get update
sudo apt install wine-stable
wine64 ipconfig
```

### Linux Mint 18 e 19

1. Habilite a arquitetura de 32 bits (exigida pelos pacotes, embora o próprio Syhunt seja de 64 bits) e instale o Wine:
   ```bash
   sudo dpkg --add-architecture i386
   sudo apt install wine-stable
   ```
2. Se a instalação falhar por problemas de dependências (como aconteceu em nossos testes), instale o Wine a partir do repositório do WineHQ:
   ```bash
   wget -nc https://dl.winehq.org/wine-builds/winehq.key; sudo apt-key add winehq.key
   sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
   sudo add-apt-repository ppa:cybermax-dexter/sdl2-backport
   sudo apt update && sudo apt install --install-recommends winehq-stable
   ```
   Use `bionic` para o Linux Mint 19.x ou `xenial` para o Linux Mint 18.x. O PPA fornece a biblioteca `libfaudio0`, que é necessária.
3. Execute `wine64 ipconfig`.

<a id="opensuse"></a>

## openSUSE

> **Aplica-se a:** openSUSE Leap 15, Leap 42 ou posterior, Tumbleweed

1. Adicione o repositório do Wine para a sua versão do openSUSE. O padrão da URL é `https://download.opensuse.org/repositories/Emulators:/Wine/openSUSE_<nome>_<versão>/Emulators:Wine.repo`. Por exemplo:
   ```bash
   # Leap 15.1
   sudo zypper ar -r https://download.opensuse.org/repositories/Emulators:/Wine/openSUSE_Leap_15.1/Emulators:Wine.repo
   # Tumbleweed
   sudo zypper ar -r https://download.opensuse.org/repositories/Emulators:/Wine/openSUSE_Tumbleweed/Emulators:Wine.repo
   ```
2. Atualize o cache do zypper. Quando for perguntado se deseja confiar na chave do novo repositório, digite **a**:
   ```bash
   sudo zypper ref
   ```
3. Instale o Wine (digite **y** para iniciar a instalação) e execute-o uma vez:
   ```bash
   sudo zypper in wine
   wine64 ipconfig
   ```

<a id="elementaryos"></a>

## elementary OS

> **Aplica-se a:** elementary OS 5.0 e 5.1

- **elementary OS 5.1:** siga as instruções do [Ubuntu](#ubuntu).
- **elementary OS 5.0:** não suportado. Em nossos testes, a instalação do Wine deixou o sistema sem conseguir inicializar, por isso não fornecemos instruções para ele.

<a id="solus"></a>

## Solus

> **Aplica-se a:** Solus 4.1

> [!WARNING]
> O Solus não é suportado. O Wine64 se mostrou instável no Solus 4.1 em nossos testes (erros como `wine client error:6c: write: Bad file descriptor`), tanto com o pacote `wine-stable` quanto com o `wine-devel`.

Se ainda assim quiser tentar:

```bash
sudo eopkg upgrade openssl
sudo eopkg install wine-devel
wine64 ipconfig
```
