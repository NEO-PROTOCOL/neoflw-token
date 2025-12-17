# 📋 Status da Whitelist - NeoFlowClaim

**Última Atualização:** 2025-12-17  
**Contrato:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`  
**Rede:** Polygon Mainnet (Chain ID: 137)  
**Status:** ✅ Ativa

---

## 📊 Resumo

- **Total de Endereços na Whitelist:** 3
- **Total de Tokens Configurados:** 3,000 NEOFLW
- **Saldo Disponível no Contrato:** 100,000,000 NEOFLW
- **Saldo Restante para Novos Claims:** 99,997,000 NEOFLW

---

## 👥 Endereços Elegíveis

| # | Endereço | Quantidade | Status | Claim Realizado |
|---|----------|------------|--------|-----------------|
| 1 | `0xc8b6c6cf88ece28efdede72ed625b95b73cb649f` | 1,000 NEOFLW | ✅ Elegível | ⏳ Pendente |
| 2 | `0x025d20c85bca82a614466429a8c7806e25e99408` | 1,000 NEOFLW | ✅ Elegível | ⏳ Pendente |
| 3 | `0xece5867f7c82e34a7273c2361cdf5ffa01fdf5a3` | 1,000 NEOFLW | ✅ Elegível | ⏳ Pendente |

---

## 🔗 Links Úteis

### Contrato no Polygonscan:
- **Endereço:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`
- **Link:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- **Write Contract:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#writeContract

### Verificar Elegibilidade:

Para verificar se um endereço está elegível, use:

```python
from ape import project

claim = project.NeoFlowClaim.at("0x407C037906d6441ECD4a3F9064eab2E6CF03b36b")

# Verificar quantidade elegível
amount = claim.claimableAmount("0x...")
print(f"Elegível para: {amount / 10**18:,.0f} NEOFLW")

# Verificar se já fez claim
has_claimed = claim.hasClaimed("0x...")
print(f"Já fez claim: {has_claimed}")
```

Ou verifique diretamente no Polygonscan:
1. Acesse o contrato
2. Aba "Read Contract"
3. Função `claimableAmount(address)` - coloque o endereço
4. Função `hasClaimed(address)` - coloque o endereço

---

## 📝 Como Adicionar Mais Endereços

### Opção 1: Script Automatizado (Recomendado)

```bash
ape run setup add_whitelist --network polygon:mainnet
```

Edite o arquivo `scripts/setup/add_whitelist.py` e adicione novos endereços:

```python
users = [
    "0xnovo_endereco_1",
    "0xnovo_endereco_2",
]

amounts = [
    1000 * 10**18,  # 1000 tokens
    2000 * 10**18,  # 2000 tokens
]
```

### Opção 2: Via Console Ape

```bash
ape console --network polygon:mainnet
```

```python
>>> from ape import accounts, project
>>> acct = accounts.load("neoflow-admin")
>>> claim = project.NeoFlowClaim.at("0x407C037906d6441ECD4a3F9064eab2E6CF03b36b")
>>> 
>>> # Adicionar novo endereço
>>> claim.updateClaimableAmount("0xnovo_endereco", 1000 * 10**18, sender=acct)
```

---

## 🎯 Como Fazer Claim

### Para Usuários Elegíveis:

1. **Conectar wallet na Polygon Mainnet**
   - MetaMask: Adicionar rede Polygon se necessário
   - Chain ID: 137
   - RPC: https://polygon-rpc.com/

2. **Ter POL para gas**
   - Precisa de ~0.01-0.05 POL para a transação
   - Comprar em exchange ou usar bridge

3. **Acessar o contrato**
   - Link direto: https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#writeContract
   - Ou acessar Polygonscan e buscar o endereço

4. **Chamar função `claimTokens()`**
   - Conectar wallet
   - Clicar em "Write" na função `claimTokens`
   - Confirmar transação no MetaMask
   - Aguardar confirmação (~2-5 segundos)

5. **Receber tokens**
   - Tokens serão transferidos automaticamente para sua wallet
   - Verificar saldo na wallet ou no Polygonscan

**Guia Completo:** [`docs/deploy/COMO_FAZER_CLAIM.md`](./deploy/COMO_FAZER_CLAIM.md)

---

## 📊 Estatísticas

### Distribuição de Tokens:

- **Total Supply:** 1,000,000,000 NEOFLW
- **No Contrato Claim:** 100,000,000 NEOFLW (10%)
- **Configurado na Whitelist:** 3,000 NEOFLW (0.0003%)
- **Disponível para Novos Claims:** 99,997,000 NEOFLW

### Status dos Claims:

- **Total Elegíveis:** 3 endereços
- **Claims Realizados:** 0
- **Claims Pendentes:** 3
- **Taxa de Claim:** 0% (nenhum claim realizado ainda)

---

## 🔄 Histórico de Atualizações

### 2025-12-17 - Configuração Inicial
- ✅ 3 endereços adicionados na whitelist
- ✅ Total de 3,000 NEOFLW configurados
- ✅ Script de configuração testado e funcionando

---

## 📚 Documentação Relacionada

- **Setup do Claim:** [`docs/deploy/CLAIM_SETUP.md`](./deploy/CLAIM_SETUP.md)
- **Como Fazer Claim:** [`docs/deploy/COMO_FAZER_CLAIM.md`](./deploy/COMO_FAZER_CLAIM.md)
- **Transferências:** [`docs/TRANSFERENCIAS_CONCLUIDAS.md`](./TRANSFERENCIAS_CONCLUIDAS.md)
- **Estratégia de Distribuição:** [`docs/DISTRIBUICAO_TOKENS_ESTRATEGIA.md`](./DISTRIBUICAO_TOKENS_ESTRATEGIA.md)

---

## ⚠️ Notas Importantes

1. **Claim Único:** Cada endereço pode fazer claim apenas uma vez
2. **Gas do Usuário:** Usuários precisam ter POL para pagar o gas
3. **Rede Correta:** Deve estar na Polygon Mainnet (não testnet)
4. **Saldo do Contrato:** Sempre manter saldo suficiente para todos os claims
5. **Atualizações:** Este documento deve ser atualizado após cada adição de endereços ou claims realizados

---

**Última atualização:** 2025-12-17
