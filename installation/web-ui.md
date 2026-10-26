# Interface Web

> **Aplica-se a:** Syhunt Hybrid 7.2

**Conteúdo**

- [Introdução](#intro)
- [Habilitando a interface web](#firststeps)
- [Criando contas de usuário adicionais](#addusers)
- [Alterando o idioma padrão da interface](#changelang)
- [Política de senhas](#passwords)
- [Perfis de usuário](#roles)
- [Dicas](#tips)

<a id="intro"></a>

## Introdução

Desde a versão 7.1.6, o Syhunt Hybrid inclui uma interface web que pode ser habilitada no Windows, no Linux e no macOS. Por ela, você pode iniciar varreduras DAST, SAST e MAST; ver os resultados de todas as varreduras, iniciadas pela interface, pela CLI, pela API REST ou pelo agendador; gerar relatórios e exportações; gerenciar usuários, permissões e sessões ativas; executar comandos de console; e muito mais. A interface web e os relatórios estão disponíveis em oito idiomas: inglês, alemão, espanhol, francês, italiano, japonês, coreano e português.

A interface web roda sobre o OpenResty (NGINX + Lua). Ela armazena as senhas com hash bcrypt de alto custo, gera IDs de sessão de forma segura e protege o login contra ataques de força bruta.

![](../images/webui_chrome.png)

<a id="firststeps"></a>

## Habilitando a interface web

1. Abra um terminal ou Prompt de Comando na pasta da CLI do Syhunt (o [local padrão depende do sistema operacional](../integrations/command-line.md#intro)):
   - **Linux:** `cd ${HOME}/syhunt-hybrid/carbon/`
   - **macOS:** `cd "/Applications/Syhunt Hybrid/carbon"`
   - **Windows:** abra o menu Iniciar e digite `command`. Clique com o botão direito em **Prompt de Comando** e escolha **Executar como administrador**,<br>![](../images/prompt_runasadmin.png)<br>depois execute `cd /d "%ProgramFiles%\Syhunt Hybrid\"`.
2. Configure a conta de administrador. Execute o comando a seguir, que gera e define a senha do administrador, e guarde a senha exibida; você precisará dela para fazer login:
   ```
   scancore -pwdgen:admin
   ```
   ![](../images/prompt_pwdgen.png)
3. Inicie o servidor:
   - **Linux ou macOS:** execute `syservicereg` e depois `webui_utils --sslenable`. O serviço da interface web é instalado e iniciado.
   - **Windows:** reinicie o Windows (a interface web é iniciada junto com o sistema) ou, para evitar a reinicialização, execute `scansched -restart` como administrador.<br>![](../images/prompt_schedrestart.png)
4. Abra a interface web:
   1. No navegador, acesse `https://127.0.0.1:8018/syhunt/`.
   2. Informe o usuário `admin` e a senha gerada.<br>![](../images/prompt_login.png)
   3. Clique em **Sign In**.

### Observações

- No **Windows**, depois que a senha do administrador é definida, a interface web é iniciada sempre que o serviço Hybrid Scheduler é iniciado, de modo que continua em execução mesmo quando o usuário atual faz logoff. No Linux, o serviço Syhunt Web UI faz o mesmo.
- No **AlmaLinux**, se o serviço da interface web não iniciar, talvez seja necessário desativar o SELinux permanentemente. Após reiniciar, o serviço deve funcionar normalmente:
  ```bash
  sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config && sudo reboot
  ```

<a id="addusers"></a>

## Criando contas de usuário adicionais

Para criar outra conta, execute:

```
scancore -pwdgen:nomedousuario
```

<a id="changelang"></a>

## Alterando o idioma padrão da interface

Para alterar o idioma da interface web, execute o comando a seguir com um dos [códigos de idioma disponíveis](../integrations/command-line.md#replanguages):

```
scancore -langset:CODIGO
```

Por exemplo, `scancore -langset:PT` para português.

<a id="passwords"></a>

## Política de senhas

Para reforçar a segurança e apoiar a conformidade, o Syhunt 7.1 introduziu uma política de senhas rigorosa para a interface web:

| Requisito | Contas de administrador | Demais contas |
|---|---|---|
| Comprimento mínimo | 26 caracteres | 16 caracteres |
| Reutilização de senhas | Não é possível reutilizar as últimas 24 senhas | Não é possível reutilizar as últimas 10 senhas |

Além disso, toda senha deve:

- **não** incluir o nome de usuário nem qualquer parte do nome completo do usuário;
- conter pelo menos uma letra maiúscula (A–Z), uma letra minúscula (a–z), um dígito (0–9) e um caractere não alfanumérico (como `@`, `#`, `$`, `%`);
- **não** conter três ou mais caracteres idênticos consecutivos (como `AAA`) nem três caracteres consecutivos em ordem crescente ou decrescente (como `123`, `321`, `ABC`, `CBA`).

Essas regras são verificadas sempre que uma senha é definida. Após uma atualização, se uma senha existente violar alguma delas, você precisará redefini-la no próximo login.

A forma mais fácil de criar uma senha válida é `scancore -pwdgen:<usuário>`, que gera uma senha com segurança, define-a e a exibe. Para digitar a senha você mesmo, use `-pwdset`.

<a id="roles"></a>

## Perfis de usuário

Conectado como administrador, você pode atribuir a qualquer usuário o perfil Operator, Restricted Operator ou Viewer:

| Perfil | Pode |
|---|---|
| **Administrator** | Iniciar varreduras e ver todos os resultados, editar permissões e preferências de usuários e executar comandos de console. Atualmente, só é permitida uma conta de administrador. |
| **Operator** | Iniciar varreduras e ver os resultados de todas as varreduras. |
| **Restricted Operator** | Iniciar varreduras, mas ver apenas os resultados das suas próprias varreduras. |
| **Viewer** | Ver os resultados de todas as varreduras, mas não iniciar varreduras. |

### Permissões por perfil

| Permissão | Admin | Operator | Restricted Operator | Viewer |
|---|---|---|---|---|
| Alertas administrativos na tela inicial | ✅ | | | |
| Excluir varreduras, alvos, usuários e conectores | ✅ | | | |
| **Controle de acesso de usuários** | | | | |
| Acessar a tela Users | ✅ | | | |
| Criar usuários | ✅ | | | |
| Alterar o perfil de um usuário | ✅ | | | |
| Acessar perfis de usuário | ✅ | Apenas o próprio | Apenas o próprio | Apenas o próprio |
| Invalidar sessões de usuário | ✅ | Apenas as próprias | Apenas as próprias | Apenas as próprias |
| Alterar a senha de um usuário | ✅ | Apenas a própria | Apenas a própria | Apenas a própria |
| **Varreduras e alvos** | | | | |
| Iniciar varreduras | ✅ | ✅ | ✅ | |
| Acessar a tela Targets e as preferências | ✅ | ✅ | ✅ | ✅ (somente leitura) |
| Acessar informações das varreduras (logs, comparação, achados, resumo, mapa, relatórios, exportações, depuração, lista) | ✅ | ✅ | Apenas das próprias varreduras | ✅ |
| Acessar informações de ações (incluindo pré-visualização) | ✅ | ✅ | Apenas das próprias varreduras | ✅ |
| **Telas administrativas** | | | | |
| Acessar a lista de varreduras agendadas | ✅ | ✅ | ✅ | ✅ |
| Acessar os detalhes de cada varredura agendada | ✅ | | | |
| Acessar a tela Connectors | ✅ | | | |
| Acessar o console de comandos | ✅ | | | |
| Acessar as preferências e listas globais (incluindo exportação) | ✅ | | | |
| Acessar o log do agendador (se habilitado) | ✅ | ✅ | | |
| **Importação** | | | | |
| Importar especificações de API | ✅ | ✅ | | |
| Inserir ou atualizar a licença do produto | ✅ | | | |

<a id="tips"></a>

## Dicas

### Horário do agendador incorreto

Se o horário exibido na tela Scan Scheduler não corresponder ao horário do sistema, defina o fuso horário do sistema (substitua `America/Sao_Paulo` pelo seu):

- **macOS:** `sudo /usr/sbin/systemsetup -settimezone "America/Sao_Paulo"`
- **Linux:** `sudo timedatectl set-timezone America/Sao_Paulo`

### Varredura de repositórios privados

Antes de fazer a varredura de um repositório Git privado pela interface web, configure as credenciais do repositório ou as chaves SSH e teste a varredura com o [comando `scancode`](../integrations/command-line.md#cli_code_begin).

### Limitações

Conexões diretas a repositórios Azure DevOps (TFS) que não sejam Git não são suportadas no Linux nem no macOS.
