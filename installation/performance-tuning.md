# Ajuste de Desempenho

## Como lidar com varreduras DAST longas

A varredura de um site que gera muito conteúdo dinâmico pode levar bastante tempo com o Syhunt Dynamic. Isso não é um bug nem uma limitação, mas consequência de uma decisão de projeto: o Syhunt Dynamic **não** limita a profundidade com que mapeia a estrutura e os pontos de entrada de um site, pois o objetivo é sempre testar o alvo por completo. Alguns sites, porém, são extremamente grandes ou geram uma quantidade praticamente infinita de links, o que se torna um problema quando a varredura precisa terminar dentro de um prazo.

Consideramos que uma varredura DAST de um site com conteúdo muito dinâmico não deve levar mais de **três horas**. Para isso, o Syhunt Dynamic oferece:

- **Varredura incremental**, que reduz o tempo de novas varreduras do mesmo alvo.
- **Um conjunto grande e crescente de regras integradas** que aceleram varreduras desse tipo de site. Novas regras são incluídas nas atualizações do Syhunt toda semana.

### Otimização de DAST

Quando as regras integradas não bastam para um site específico, um especialista da Syhunt pode analisá-lo, mediante solicitação, e adicionar regras personalizadas. Chamamos esse processo de *otimização de DAST*; normalmente ele leva apenas algumas horas.

As novas regras aceleram o mapeamento e direcionam o scanner às áreas e pontos de entrada relevantes do site, ignorando conteúdo dinâmico redundante. Nenhum ataque é realizado contra o site durante a otimização, portanto não há risco para sua integridade ou disponibilidade. Ao final do trabalho, uma nova versão do Syhunt com as novas regras é disponibilizada.

**Para solicitá-la, [abra um ticket de suporte](../support/reporting-bugs.md#supportticketcreation) listando as URLs alvo que precisam de otimização de DAST.**

## Complementando o DAST com SAST

Para sites com conteúdo muito dinâmico, a Syhunt recomenda também fazer a varredura do código-fonte com o [Syhunt Code](../scanning/code-scanning.md). A análise estática cobre trechos de código difíceis de alcançar pelo rastreamento.

## Acelerando varreduras de código

A proteção antivírus em tempo real pode deixar as varreduras de código-fonte bem mais lentas. Consulte [Como evitar a interferência do antivírus em pipelines](../scanning/code-scanning.md#advanced_pipeline).
