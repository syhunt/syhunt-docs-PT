# Faraday

> **Aplica-se a:** Syhunt Hybrid 7.2

![](../images/faraday_screenshot.png)

O [Faraday](https://faradaysec.com/) permite que as equipes gerenciem sua superfície de ataque em um único lugar, automatizando e acelerando etapas importantes da gestão de vulnerabilidades. Ele reúne uma quantidade de ferramentas e procedimentos de segurança que, de outra forma, seria difícil de administrar, em um processo único e simples.

O Syhunt pode se conectar à API de um servidor Faraday e enviar automaticamente resultados de SAST ou DAST. O Faraday também inclui um plugin do Syhunt, de modo que os resultados do Syhunt podem ser enviados pela interface web, pela CLI e pela API REST do Faraday.

## Envio automático de resultados

**1. Crie um conector do Faraday**

1. Clique em **Connectors** no menu superior da interface web.<br>![](../images/menu_connectors.png)
2. Clique em **Add**. A tela **New Connector** é aberta.
3. Informe um nome para o conector (por exemplo, `MyFaraday`).
4. Defina **Type** como **Faraday**.
5. Clique em **Create** e, após a mensagem de sucesso, em **Close**.

**2. Configure-o**

1. Clique no conector na lista. A tela de preferências dele é aberta.
2. Informe a URL do servidor Faraday, por exemplo `https://yourdashboard.apps.faradaysec.com/`.
3. Informe o nome do seu workspace. Se deixar em branco, será usado `my_workspace`.
4. Informe seu usuário e senha.
5. Clique em **Save**.

**3. Teste-o**

Clique no conector na lista e escolha **Run Test**. Se tudo estiver configurado corretamente, uma varredura de teste aparece no seu painel do Faraday. Caso contrário, uma mensagem de erro indica o que corrigir.

**4. Associe-o às suas varreduras**

- **CLI:** informe `-tk:<nomedoconector>`.
- **Varreduras agendadas:** nas preferências da varredura agendada, na aba **Notifications**, selecione o conector em **Issue Tracker #1** ou **#2**.

### Criando o conector pela CLI

```lua
-- Adicionar um rastreador do Faraday
scancore -tracker:add
-- Informe o tipo (Faraday) e um nome para o rastreador e pressione Enter.

-- Configurá-lo
scancore -tracker:set to:mytrackername -key:api.url -v:"https://yourdashboard.apps.faradaysec.com/"
scancore -tracker:set to:mytrackername -key:auth.username.encrypted -v:yourusername
scancore -tracker:set to:mytrackername -key:auth.password.encrypted -vsecret

-- Testá-lo
scancore -tracker:send -tid:TEST -to:mytrackername
```
