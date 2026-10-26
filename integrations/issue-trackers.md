# Rastreadores de Issues

> **Aplica-se a:** Syhunt Hybrid 7.2

**Conteúdo**

- [GitHub Issues](#tracker_github)
- [GitLab Issues](#tracker_gitlab)
- [Jira](#tracker_jira)
- [Enviando vulnerabilidades a um rastreador](#tracker_submit)
- [Nomes abreviados das preferências de rastreadores](#shortnames)

Com um rastreador de issues configurado no Syhunt, você pode enviar vulnerabilidades a um projeto com um clique. Os rastreadores são criados como *conectores* na interface web; também é possível gerenciá-los pela [linha de comando](command-line.md#cli_trackers).

<a id="tracker_github"></a>
<a id="tracker_githubbegin"></a>

## GitHub Issues

**1. Crie um token de acesso pessoal** com o escopo `repo`, se ainda não tiver um:

1. Faça login no GitHub.
2. Clique no seu avatar (canto superior direito) e escolha **Settings**.
3. No menu à esquerda, role para baixo e escolha **Developer settings**.
4. Escolha **Personal access tokens** e depois **Generate new token**.
5. Opcionalmente, informe uma descrição para o token.
6. Selecione o escopo `repo`.
7. Clique em **Generate token**.
8. Guarde o token em um local seguro. Depois de sair ou atualizar a página, não será possível vê-lo novamente.

**2. Adicione um rastreador do GitHub:**

1. Abra **Connectors** na interface web.<br>![](../images/menu_connectors.png)
2. Clique em **Add**.<br>![](../images/connector_add.png)
3. Informe um nome para o rastreador (por exemplo, `MyProjectName`).
4. Defina o tipo como **GitHub**.
5. Clique em **Create** e depois em **Close**.
6. Clique no novo rastreador na lista. A tela de preferências dele é aberta.
7. Informe o projeto do GitHub no formato `owner/repo`.
8. Informe seu token de acesso pessoal e clique em **Save**.
9. Abra o rastreador novamente e clique em **Run Test**.<br>![](../images/webui_runtest_button.png)

Se tudo estiver configurado corretamente, uma issue de teste é criada em `https://github.com/<owner>/<repo>/issues`. Caso contrário, uma mensagem de erro indica o que corrigir.

<a id="tracker_gitlab"></a>
<a id="tracker_gitlabbegin"></a>

## GitLab Issues

> [!TIP]
> Para integrar o Syhunt ao GitLab CI e ao painel de segurança do GitLab, consulte [GitLab](gitlab.md).

**1. Crie um token de acesso pessoal** com o escopo `api`, se ainda não tiver um:

1. Faça login no GitLab.
2. Clique no seu avatar (canto superior direito) e escolha **Settings**.
3. No menu User Settings, escolha **Access Tokens**.
4. Informe um nome e, opcionalmente, uma data de expiração.
5. Selecione o escopo `api`.
6. Clique em **Create personal access token**.
7. Guarde o token em um local seguro. Depois de sair ou atualizar a página, não será possível vê-lo novamente.

**2. Adicione um rastreador do GitLab:**

1. Abra **Connectors** na interface web.<br>![](../images/menu_connectors.png)
2. Clique em **Add**.<br>![](../images/connector_add.png)
3. Informe um nome para o rastreador (por exemplo, `MyProjectName`).
4. Defina o tipo como **GitLab**.
5. Clique em **Create** e depois em **Close**.
6. Clique no novo rastreador na lista. A tela de preferências dele é aberta.
7. Informe o projeto do GitLab no formato `owner/repo`.
8. Informe a URL do servidor GitLab, por exemplo `https://gitlab.com/` ou a URL do seu próprio servidor.
9. Informe seu token de acesso pessoal e clique em **Save**.
10. Abra o rastreador novamente e clique em **Run Test**.<br>![](../images/webui_runtest_button.png)

Se tudo estiver configurado corretamente, uma issue de teste é criada em `https://<servidor_gitlab>/<owner>/<repo>/issues`. Caso contrário, uma mensagem de erro indica o que corrigir.

<a id="tracker_gitlabend"></a>
<a id="tracker_jira"></a>

## Jira

1. Abra **Connectors** na interface web.<br>![](../images/menu_connectors.png)
2. Clique em **Add**.<br>![](../images/connector_add.png)
3. Informe um nome para o rastreador (por exemplo, `MyProjectName`).
4. Defina o tipo como **JIRA**.
5. Clique em **Create** e depois em **Close**.
6. Clique no novo rastreador na lista. A tela de preferências dele é aberta.
7. Informe um nome de projeto Jira válido.
8. Informe a URL do servidor Jira, por exemplo `http://<IP>:8080/`.
9. Se não quiser o tipo de issue padrão, informe um nome de tipo de issue válido.
10. Informe suas credenciais do Jira (usuário e senha) e clique em **Save**.
11. Abra o rastreador novamente e clique em **Run Test**.<br>![](../images/webui_runtest_button.png)

Se tudo estiver configurado corretamente, uma issue de teste é criada no seu projeto Jira. Caso contrário, uma mensagem de erro indica o que corrigir.

<a id="tracker_submit"></a>

## Enviando vulnerabilidades a um rastreador

1. Abra a aba **Vulnerabilities** de uma varredura em andamento, ou abra **Scans**, clique em uma varredura na lista e vá para a aba **Vulnerabilities** dela.
2. Selecione uma ou mais vulnerabilidades, clique em **Send To** e escolha o rastreador.

   ![](../images/trackers_sendto.png)

O Syhunt também pode enviar automaticamente a um rastreador um resumo das vulnerabilidades encontradas:

- a partir de uma **varredura agendada**, se configurado na tela de agendamento;
- pela **CLI**, com o parâmetro `-tk` do `scanurl` ou do `scancode` (consulte [Linha de Comando](command-line.md#cli_trackers_send));
- pelo **PowerShell** ou por um **workflow de CI**, com o parâmetro `-tracker`:

```powershell
# PowerShell, rastreador existente
Start-CodeScan -pfcond "medium" -tracker "YOURTRACKERNAME"

# PowerShell, rastreador definido na hora
Start-CodeScan -pfcond "medium" -tracker "?app=github###project=user/project###token=YOURTOKEN"

# Workflow do GitHub Actions, rastreador definido na hora
Start-CodeScan -pfcond "medium" -tracker "?app=github###project=${{ github.repository }}###token=${{ secrets.GITHUB_TOKEN }}"
```

<a id="shortnames"></a>

## Nomes abreviados das preferências de rastreadores

Ao informar [preferências de rastreadores](../reference/preferences.md#prefs_tracker) por meio de `-tk` ou `-tracker`, use os nomes abreviados abaixo. Configurações sem nome abreviado não podem ser definidas por esses parâmetros.

| Nome abreviado | ID da preferência | Tipo |
|---|---|---|
| `app` | `tracker.defaultapp` | string |
| `project` | `tracker.project.name` | string |
| `token` | `tracker.auth.token.encrypted` | string |
| `from` | `tracker.message.from` | string |
| `to` | `tracker.message.tolist` | string |
| `subject` | `tracker.message.subject` | string |
| `notifyonfailonly` | `tracker.notifyonfailonly` | boolean |
| `apiurl` | `tracker.api.url` | string |

**Específicos do DefectDojo:**

| Nome abreviado | ID da preferência | Tipo |
|---|---|---|
| `producttypename` | `tracker.scan.producttypename` | string |
| `testtitle` | `tracker.scan.testtitle` | string |
| `engagementname` | `tracker.scan.engagementname` | string |
| `productname` | `tracker.scan.productname` | string |
| `minseverity` | `tracker.scan.minseverity` | string |
| `pushtojira` | `tracker.scan.pushtojira` | boolean |
| `verified` | `tracker.scan.verified` | boolean |
| `closeoldfindings` | `tracker.scan.closeoldfindings` | boolean |
| `skipduplicates` | `tracker.scan.skipduplicates` | boolean |
| `active` | `tracker.scan.active` | boolean |
| `autocreatecontext` | `tracker.scan.autocreatecontext` | boolean |
