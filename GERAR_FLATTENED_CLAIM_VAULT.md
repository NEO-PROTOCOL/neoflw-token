# 🔧 Gerar Arquivos Flattened para Claim e Vault

## 📋 Status Atual

- ✅ **NeoFlowToken:** Arquivo flattened existe (`artifacts/flattened/NeoFlowToken_flattened.sol`)
- ⏳ **NeoFlowClaim:** Arquivo flattened precisa ser gerado
- ⏳ **StakingVault:** Arquivo flattened precisa ser gerado

---

## 🚀 Método 1: Via Ape Framework (Recomendado)

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token

# Compilar com formato flattened
ape compile --format flattened

# Verificar arquivos gerados
ls -la artifacts/flattened/
```

**Arquivos esperados:**
- `artifacts/flattened/NeoFlowClaim_flattened.sol`
- `artifacts/flattened/StakingVault_flattened.sol`

---

## 🔧 Método 2: Via Script Python

Se o método acima não funcionar, use os scripts de verificação:

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token

# Gerar flattened
python3 scripts/verification/create_flattened_code.py

# Ou gerar flattened específico
python3 scripts/verification/generate_flattened_token.py
```

---

## 📝 Método 3: Manual (Se necessário)

Se os métodos automáticos não funcionarem:

### Para NeoFlowClaim:

1. Abra: `contracts/NeoFlowClaim.sol`
2. Copie o código
3. Substitua os imports do OpenZeppelin pelo conteúdo completo dos contratos:
   - `@openzeppelin/contracts/token/ERC20/IERC20.sol`
   - `@openzeppelin/contracts/access/Ownable.sol`
   - `@openzeppelin/contracts/security/Pausable.sol`
4. Salve como: `artifacts/flattened/NeoFlowClaim_flattened.sol`

### Para StakingVault:

1. Abra: `contracts/StakingVault.sol`
2. Copie o código
3. Substitua os imports do OpenZeppelin pelo conteúdo completo dos contratos:
   - `@openzeppelin/contracts/token/ERC20/IERC20.sol`
   - `@openzeppelin/contracts/access/Ownable.sol`
   - `@openzeppelin/contracts/security/ReentrancyGuard.sol`
   - `@openzeppelin/contracts/security/Pausable.sol`
4. Salve como: `artifacts/flattened/StakingVault_flattened.sol`

---

## ✅ Verificar Arquivos Gerados

Após gerar, verifique se os arquivos existem:

```bash
ls -lh artifacts/flattened/NeoFlowClaim_flattened.sol
ls -lh artifacts/flattened/StakingVault_flattened.sol
```

**Tamanho esperado:** Cada arquivo deve ter pelo menos alguns KB (dependendo do tamanho dos contratos OpenZeppelin incluídos).

---

## 🎯 Próximo Passo

Após gerar os arquivos flattened, use o guia completo de verificação:

📖 **Guia:** [`docs/VERIFICACAO_COMPLETA_POLYGONSCAN.md`](./docs/VERIFICACAO_COMPLETA_POLYGONSCAN.md)

---

**Última atualização:** 2025-12-17
