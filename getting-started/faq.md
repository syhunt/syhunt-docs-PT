# Perguntas Frequentes

> **Aplica-se a:** Syhunt Hybrid 7.2

<a id="dynamic_begin"></a>

## Syhunt Dynamic

**Quanto tempo o Syhunt Dynamic leva para executar todos os testes?**

Depende de quantas páginas e aplicações o site contém e do método de varredura escolhido. Após o rastreamento (crawling), as verificações das aplicações web costumam ser a etapa mais longa, e sua duração aumenta conforme o tamanho do site.

**Posso reabrir uma varredura anterior e gerar seus relatórios novamente?**

Sim. Abra **Scans** no menu, clique na varredura na lista e depois em **View Report**, ou em **Export** para salvar os dados em um formato específico.

**Existe uma lista dos testes realizados pela versão atual?**

Sim. Abra **Help → Vulnerability Checks** ou consulte [Verificações de Vulnerabilidades](../reference/vulnerability-checks.md).

**Algum dos testes pode derrubar o host alvo?**

Algumas verificações de negação de serviço (DoS) podem derrubar o alvo. Você pode desativá-las escolhendo um método de varredura sem testes de DoS, como **Complete Scan, No DoS** (consulte [Métodos de Varredura](../scanning/hunt-methods.md)).

**O Syhunt Dynamic tem problemas com firewalls pessoais?**

Você precisará permitir que o Syhunt faça conexões de saída. Alguns firewalls de software também lidam mal com tráfego intenso, por isso não recomendamos executar um firewall pessoal na mesma máquina que o Syhunt.

Se a máquina que executa a varredura tiver um firewall com filtragem de saída, tente desativá-lo. Ocasionalmente, vimos firewalls bloquearem silenciosamente as conexões de um programa sem consultar o usuário.

**O Syhunt pode fazer varredura das portas 21 (FTP) ou 23 (Telnet)?**

Não. O Syhunt Dynamic não é um scanner de rede de uso geral; ele é especializado em aplicações web e APIs web.

<a id="dynamic_end"></a>

## Nomes de produtos

**O que aconteceu com o Sandcat Platinum, o TrustSight e o Collapse?**

O Sandcat Platinum foi renomeado para Sandcat Pro e, mais tarde, tornou-se o Syhunt Dynamic. As tecnologias TrustSight e Collapse foram incorporadas ao Syhunt Dynamic.
