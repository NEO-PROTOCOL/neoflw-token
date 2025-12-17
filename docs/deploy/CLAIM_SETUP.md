# 🎁 NeoFlowClaim - Sistema de Claim de Tokens

Sistema de claim onde **usuários pagam o próprio gas** para reivindicar tokens elegíveis via whitelist.

## 📋 Visão Geral

O contrato `NeoFlowClaim` permite distribuição eficiente de tokens para múltiplos endereços elegíveis. Diferente de airdrops tradicionais onde o owner paga todo o gas, neste sistema cada usuário paga seu próprio gas ao fazer claim.

### 🔑 Características Principais

- ✅ **Usuário paga o gas**: Distribuição eficiente sem custos excessivos para o owner
- ✅ **Whitelist configurável**: Owner define endereços elegíveis e quantidades
- ✅ **Claim único**: Cada endereço pode fazer claim apenas uma vez
- ✅ **Proteção CEI**: Implementação segura seguindo Checks-Effects-Interactions
- ✅ **Função de emergência**: Owner pode retirar tokens em caso de necessidade

---

## 🚀 Deploy do Contrato

### Pré-requisitos

1. Token `NeoFlowToken` já deployado
2. Conta `neoflow-admin` configurada e com saldo de Sepolia ETH
3. Endereço do token salvo em `.token_address.txt` ou disponível

### Opção 1: Usando npm

```bash
npm run deploy:claim
```

### Opção 2: Usando Ape diretamente

```bash
# Com endereço do token em arquivo
ape run deploy_claim --network ethereum:sepolia

# Ou passando endereço como argumento
ape run deploy_claim -- <token_address> --network ethereum:sepolia
```

### Opção 3: Usando Makefile

```bash
make deploy-claim
```

### Output Esperado

```
🔗 Token address: 0x...
📦 Deploying NeoFlowClaim...

============================================================
✅ NeoFlowClaim deployed at: 0x...
🔗 Token address: 0x...
============================================================

🔗 Ver no Etherscan:
   https://sepolia.etherscan.io/address/0x...

⚠️  IMPORTANTE: Lembre-se de transferir tokens para o contrato!
   Transferir tokens via: token.transfer(0x..., amount)
```

O endereço do contrato será salvo automaticamente em `.claim_address.txt`.

---

## 💰 Financiamento do Contrato

**CRÍTICO**: Após o deploy, você **DEVE** transferir tokens para o contrato, caso contrário os claims falharão.

### Transferir Tokens via Script Python

```python
from ape import accounts, project

acct = accounts.load("neoflow-admin")

# Ler endereços
with open(".token_address.txt", "r") as f:
    token_address = f.read().strip()
    
with open(".claim_address.txt", "r") as f:
    claim_address = f.read().strip()

# Obter instâncias
token = project.NeoFlowToken.at(token_address)
claim = project.NeoFlowClaim.at(claim_address)

# Transferir tokens (exemplo: 50M tokens)
amount = 50_000_000 * 10**18
token.transfer(claim_address, amount, sender=acct)

print(f"✅ Transferidos {amount / 10**18:,.0f} tokens para o contrato")
```

### Verificar Saldo do Contrato

```python
balance = claim.contractBalance()
print(f"Saldo do contrato: {balance / 10**18:,.2f} NEOFLW")
```

---

## 📝 Configuração da Whitelist

### ✅ Whitelist Atual Configurada (Polygon Mainnet)

**Data de Configuração:** 2025-12-17  
**Contrato:** `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b`  
**Status:** ✅ Configurada e Ativa

#### Endereços na Whitelist:

| # | Endereço | Quantidade | Status |
|---|----------|------------|--------|
| 1 | `0xc8b6c6cf88ece28efdede72ed625b95b73cb649f` | 1,000 NEOFLW | ✅ Elegível |
| 2 | `0x025d20c85bca82a614466429a8c7806e25e99408` | 1,000 NEOFLW | ✅ Elegível |
| 3 | `0xece5867f7c82e34a7273c2361cdf5ffa01fdf5a3` | 1,000 NEOFLW | ✅ Elegível |

**Total Configurado:** 3,000 NEOFLW  
**Saldo Disponível no Contrato:** 100,000,000 NEOFLW  
**Saldo Restante para Novos Claims:** 99,997,000 NEOFLW

#### Como Adicionar Mais Endereços:

Use o script automatizado:

```bash
ape run setup add_whitelist --network polygon:mainnet
```

Ou edite o arquivo `scripts/setup/add_whitelist.py` e adicione novos endereços na lista `users` e `amounts`.

---

### Opção 1: Configurar múltiplos usuários de uma vez

```python
from ape import accounts, project

acct = accounts.load("neoflow-admin")

# Ler endereço do claim
with open(".claim_address.txt", "r") as f:
    claim_address = f.read().strip()

claim = project.NeoFlowClaim.at(claim_address)

# Lista de usuários e quantidades
users = [
    "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
    "0x8ba1f109551bD432803012645Hac136c22C2bF5c",
    "0x1234567890123456789012345678901234567890"
]

amounts = [
    1000 * 10**18,  # 1000 tokens
    2000 * 10**18,  # 2000 tokens
    5000 * 10**18   # 5000 tokens
]

# Configurar whitelist
claim.setWhitelist(users, amounts, sender=acct)

print("✅ Whitelist configurada com sucesso!")
```

### Opção 2: Atualizar usuário individual

```python
claim.updateClaimableAmount(
    "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
    3000 * 10**18,  # 3000 tokens
    sender=acct
)
```

**Nota**: Não é possível atualizar o amount de um usuário que já fez claim.

---

## 🎯 Como Usuários Fazem Claim

### Via Frontend (Recomendado)

Usuários conectam carteira e chamam a função `claimTokens()`:

```typescript
// hooks/useNeoFlowClaim.ts
import { useContractWrite } from 'wagmi'
import { NEOFLOW_CLAIM_ABI } from '@/lib/abi/neoflowClaim'

const CLAIM_ADDRESS = '0x...' // Endereço do contrato de claim

export function useNeoFlowClaim() {
  const { write: claimTokens, isLoading } = useContractWrite({
    address: CLAIM_ADDRESS,
    abi: NEOFLOW_CLAIM_ABI,
    functionName: 'claimTokens',
  })

  return { claimTokens, isLoading }
}
```

### Via Etherscan

1. Acesse o contrato no Etherscan: `https://sepolia.etherscan.io/address/<claim_address>`
2. Vá na aba "Contract" → "Write Contract"
3. Conecte sua carteira
4. Chame a função `claimTokens()`
5. Confirme a transação (você pagará o gas)

### Via Console Ape

```bash
ape console --network ethereum:sepolia
```

```python
>>> claim = project.NeoFlowClaim.at("0x...")
>>> claim.claimTokens(sender=accounts[1])  # accounts[1] é o usuário
```

---

## 🔍 Verificações e Consultas

### Verificar se endereço é elegível

```python
amount = claim.claimableAmount("0x...")
if amount > 0:
    print(f"Elegível para {amount / 10**18:.2f} tokens")
else:
    print("Não elegível")
```

### Verificar se já fez claim

```python
has_claimed = claim.hasClaimed("0x...")
if has_claimed:
    print("Usuário já fez claim")
else:
    print("Usuário ainda não fez claim")
```

### Verificar saldo do contrato

```python
balance = claim.contractBalance()
print(f"Saldo disponível: {balance / 10**18:,.2f} NEOFLW")
```

---

## 🛡️ Funções de Segurança

### Emergency Withdraw (Apenas Owner)

Em caso de emergência, o owner pode retirar tokens do contrato:

```python
amount_to_withdraw = 10_000 * 10**18
claim.emergencyWithdraw(amount_to_withdraw, sender=acct)
```

**Use com cuidado**: Certifique-se de que não há claims pendentes antes de retirar tokens.

---

## 📊 Eventos do Contrato

O contrato emite os seguintes eventos para auditoria:

- `TokensClaimed(address indexed user, uint256 amount)` - Quando um usuário faz claim
- `WhitelistUpdated(uint256 userCount)` - Quando whitelist é atualizada
- `ClaimableAmountUpdated(address indexed user, uint256 amount)` - Quando amount de um usuário é atualizado
- `EmergencyWithdraw(address indexed to, uint256 amount)` - Quando owner retira tokens

### Monitorar Eventos

```python
# Buscar todos os claims realizados
from ape import chain

claims = []
for event in chain.contracts.get_events(claim, "TokensClaimed"):
    claims.append({
        "user": event["user"],
        "amount": event["amount"]
    })
```

---

## 🧪 Testes

Execute os testes do contrato:

```bash
# Via npm
npm run test

# Via Ape
ape test tests/test_claim.py

# Via Makefile
make test-claim
```

### Testes Disponíveis

- ✅ Deploy do contrato
- ✅ Configuração de whitelist
- ✅ Claim de tokens
- ✅ Proteção contra claim duplicado
- ✅ Validação de endereços não elegíveis
- ✅ Validação de saldo insuficiente
- ✅ Função de emergência

---

## 📋 Checklist de Deploy Completo

- [ ] Token `NeoFlowToken` deployado
- [ ] Contrato `NeoFlowClaim` deployado
- [ ] Tokens transferidos para o contrato de claim
- [ ] Whitelist configurada com endereços elegíveis
- [ ] Contrato verificado no Etherscan (opcional)
- [ ] Documentação de endereços salva
- [ ] Testes executados e passando

---

## 🔗 Arquivos Relacionados

- **Contrato**: `contracts/NeoFlowClaim.sol`
- **Deploy Script**: `scripts/deploy_claim.py`
- **Setup Script**: `scripts/setup_claim.py`
- **Testes**: `tests/test_claim.py`

---

## ⚠️ Considerações Importantes

1. **Saldo do Contrato**: Sempre mantenha saldo suficiente no contrato para cobrir todos os claims da whitelist
2. **Gas do Usuário**: Usuários precisam ter ETH (ou Sepolia ETH) para pagar o gas do claim
3. **Claim Único**: Uma vez feito o claim, o usuário não pode fazer novamente
4. **Whitelist Prévia**: Configure a whitelist antes de anunciar o claim para usuários
5. **Emergency Withdraw**: Use apenas em emergências e certifique-se de comunicar aos usuários

---

## 📚 Exemplo Completo de Setup

```python
# scripts/complete_claim_setup.py
from ape import accounts, project

def main():
    acct = accounts.load("neoflow-admin")
    
    # 1. Ler endereços
    with open(".token_address.txt", "r") as f:
        token_address = f.read().strip()
    
    token = project.NeoFlowToken.at(token_address)
    
    # 2. Deploy do claim (se ainda não feito)
    # claim = project.NeoFlowClaim.deploy(token, sender=acct)
    
    # Ou usar endereço existente
    with open(".claim_address.txt", "r") as f:
        claim_address = f.read().strip()
    
    claim = project.NeoFlowClaim.at(claim_address)
    
    # 3. Transferir tokens para o contrato
    total_tokens = 50_000_000 * 10**18  # 50M tokens
    token.transfer(claim_address, total_tokens, sender=acct)
    print(f"✅ Transferidos {total_tokens / 10**18:,.0f} tokens")
    
    # 4. Configurar whitelist
    users = [
        "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
        "0x8ba1f109551bD432803012645Hac136c22C2bF5c",
    ]
    amounts = [
        1000 * 10**18,
        2000 * 10**18,
    ]
    
    claim.setWhitelist(users, amounts, sender=acct)
    print("✅ Whitelist configurada")
    
    # 5. Verificar setup
    balance = claim.contractBalance()
    print(f"💰 Saldo do contrato: {balance / 10**18:,.2f} NEOFLW")
    
    print("\n✅ Setup completo! Usuários podem fazer claim agora.")
```

---

## 🆘 Troubleshooting

### Erro: "Claim: Endereco nao elegivel"
- Verifique se o endereço está na whitelist usando `claimableAmount(address)`

### Erro: "Claim: Tokens ja reivindicados"
- O endereço já fez claim anteriormente. Cada endereço pode fazer claim apenas uma vez.

### Erro: "Claim: Falha na transferencia"
- O contrato não tem saldo suficiente. Transfira mais tokens para o contrato.

### Erro ao fazer deploy
- Verifique se o token está deployado e o endereço está correto
- Certifique-se de ter Sepolia ETH para gas

---

## 📞 Suporte

Para dúvidas ou problemas, consulte:
- `README.md` - Documentação geral do projeto
- `DEPLOY_INSTRUCTIONS.md` - Instruções de deploy
- Testes em `tests/test_claim.py` - Exemplos de uso

