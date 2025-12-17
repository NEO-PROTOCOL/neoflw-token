# ✅ Guia Completo de Verificação - Polygonscan

**Data:** 2025-12-17  
**Status:** Arquivos preparados e prontos para verificação

---

## 📋 Contratos para Verificar

| Contrato | Endereço | Status |
|----------|----------|--------|
| **NeoFlowToken** | `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` | ⏳ Pendente |
| **NeoFlowClaim** | `0x407C037906d6441ECD4a3F9064eab2E6CF03b36b` | ⏳ Pendente |
| **StakingVault** | `0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41` | ⏳ Pendente |

---

## 🎯 1. NEOFLOWTOKEN - Verificação

### 📍 Link Direto:
```
https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
```

### 📋 Passo a Passo:

1. **Acesse o link acima**
2. **Clique em:** "Contract" → "Verify and Publish"
3. **Escolha o método:** "Flattened Source Code"
4. **Preencha os campos:**

#### Configurações:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowToken` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` ou `paris` |
| **via-IR** | ❌ **No** (não habilitado) |

#### Constructor Arguments (ABI-encoded):
```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Explicação:** Este é o valor `1_000_000_000 * 10**18` (1 bilhão de tokens) em hexadecimal.

#### Flattened Source Code:

**Arquivo:** `artifacts/flattened/NeoFlowToken_flattened.sol`

1. Abra o arquivo: `/Users/nettomello/CODIGOS/TOKENS/neoflw-token/artifacts/flattened/NeoFlowToken_flattened.sol`
2. **Copie TODO o conteúdo** (Ctrl+A, Ctrl+C)
3. **Cole no campo** "Flattened Source Code" do Polygonscan

5. **Clique em:** "Verify and Publish"
6. **Aguarde alguns segundos/minutos**
7. ✅ **Pronto!** O contrato estará verificado

---

## 🎯 2. NEOFLOWCLAIM - Verificação

### 📍 Link Direto:
```
https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b#code
```

### 📋 Passo a Passo:

1. **Acesse o link acima**
2. **Clique em:** "Contract" → "Verify and Publish"
3. **Escolha o método:** "Flattened Source Code"
4. **Preencha os campos:**

#### Configurações:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowClaim` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` ou `paris` |
| **via-IR** | ❌ **No** (não habilitado) |

#### Constructor Arguments (ABI-encoded):
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Explicação:** Este é o endereço do token `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` em formato ABI-encoded (32 bytes, zero-padded).

#### Flattened Source Code:

**⚠️ IMPORTANTE:** O arquivo flattened para Claim precisa ser gerado. Use uma das opções:

**Opção 1: Gerar via Ape (Recomendado)**
```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
ape compile --format flattened
```

Depois procure por: `artifacts/flattened/NeoFlowClaim_flattened.sol`

**Opção 2: Usar código direto**
1. Abra: `contracts/NeoFlowClaim.sol`
2. Copie TODO o conteúdo
3. Cole no Polygonscan
4. O Polygonscan tentará resolver os imports automaticamente

**Se der erro de imports**, você precisará criar o flattened manualmente incluindo os contratos do OpenZeppelin.

5. **Clique em:** "Verify and Publish"
6. **Aguarde alguns segundos/minutos**
7. ✅ **Pronto!** O contrato estará verificado

---

## 🎯 3. STAKINGVAULT - Verificação

### 📍 Link Direto:
```
https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41#code
```

### 📋 Passo a Passo:

1. **Acesse o link acima**
2. **Clique em:** "Contract" → "Verify and Publish"
3. **Escolha o método:** "Flattened Source Code"
4. **Preencha os campos:**

#### Configurações:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `StakingVault` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` ou `paris` |
| **via-IR** | ❌ **No** (não habilitado) |

#### Constructor Arguments (ABI-encoded):
```
00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2
```

**Explicação:** Este é o endereço do token `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2` em formato ABI-encoded.

#### Flattened Source Code:

**⚠️ IMPORTANTE:** O arquivo flattened para Vault precisa ser gerado. Use uma das opções:

**Opção 1: Gerar via Ape (Recomendado)**
```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
ape compile --format flattened
```

Depois procure por: `artifacts/flattened/StakingVault_flattened.sol`

**Opção 2: Usar código direto**
1. Abra: `contracts/StakingVault.sol`
2. Copie TODO o conteúdo
3. Cole no Polygonscan
4. O Polygonscan tentará resolver os imports automaticamente

**Se der erro de imports**, você precisará criar o flattened manualmente incluindo os contratos do OpenZeppelin.

5. **Clique em:** "Verify and Publish"
6. **Aguarde alguns segundos/minutos**
7. ✅ **Pronto!** O contrato estará verificado

---

## 🔧 Gerar Arquivos Flattened (Se Necessário)

Se os arquivos flattened não existirem para Claim ou Vault:

### Método 1: Via Ape Framework

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token

# Compilar com formato flattened
ape compile --format flattened

# Verificar arquivos gerados
ls -la artifacts/flattened/
```

### Método 2: Via Script Python

```bash
# Gerar flattened para Claim
python3 scripts/verification/generate_flattened_token.py

# Ou usar o script de verificação que gera automaticamente
python3 scripts/verification/create_flattened_code.py
```

### Método 3: Manual (Se necessário)

1. Abra o contrato Solidity
2. Substitua os imports por:
   ```solidity
   // Substituir: import "@openzeppelin/contracts/..."
   // Por: copiar o conteúdo completo do contrato OpenZeppelin
   ```
3. Salve como `[ContractName]_flattened.sol`

---

## ⚠️ Troubleshooting

### Erro: "Compiled bytecode does not match"

**Possíveis causas:**
1. Versão do compilador incorreta
2. Configurações de otimização diferentes
3. Constructor arguments incorretos
4. Código fonte diferente do usado no deploy

**Soluções:**
1. Tente versões diferentes do compilador:
   - `v0.8.18+commit.87f61d96` (primeira opção)
   - `v0.8.30+commit.73712a01` (segunda opção)
   - `v0.8.18` (sem commit hash)
2. Verifique se `via-IR` está desabilitado
3. Verifique se `Optimization Runs` está como `200`
4. Verifique se o EVM Version está como `default` ou `paris`

### Erro: "Constructor arguments are incorrect"

**Solução:**
- Verifique se copiou o constructor argument completo
- Para Token: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`
- Para Claim/Vault: `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2`

### Erro: "Cannot find import"

**Solução:**
- Use o arquivo flattened completo (não o código fonte direto)
- Ou gere o flattened via Ape Framework

---

## 📊 Resumo dos Parâmetros

### Configurações Comuns (Todos os Contratos):

- **Compiler Version:** `v0.8.18+commit.87f61d96`
- **License:** `MIT License (MIT)`
- **Optimization:** ✅ Yes
- **Optimization Runs:** `200`
- **EVM Version:** `default` ou `paris`
- **via-IR:** ❌ No

### Constructor Arguments:

| Contrato | Constructor Argument |
|----------|---------------------|
| **NeoFlowToken** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **NeoFlowClaim** | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |
| **StakingVault** | `00000000000000000000000059aa4eae743d608fbdd4205eba59b38dca755dd2` |

---

## ✅ Checklist de Verificação

### Antes de Começar:
- [ ] Conta no Polygonscan criada (pode ser com Gmail)
- [ ] Arquivo flattened do Token existe (`NeoFlowToken_flattened.sol`)
- [ ] Arquivos flattened de Claim e Vault gerados (se necessário)

### Para Cada Contrato:
- [ ] Acessei o link do contrato no Polygonscan
- [ ] Cliquei em "Contract" → "Verify and Publish"
- [ ] Escolhi "Flattened Source Code"
- [ ] Preenchi todos os campos corretamente
- [ ] Constructor arguments estão corretos
- [ ] Código fonte copiado completamente
- [ ] Cliquei em "Verify and Publish"
- [ ] Aguardei confirmação
- [ ] Contrato verificado com sucesso ✅

---

## 🔗 Links Úteis

### Contratos no Polygonscan:
- **Token:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
- **Claim:** https://polygonscan.com/address/0x407C037906d6441ECD4a3F9064eab2E6CF03b36b
- **Vault:** https://polygonscan.com/address/0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

### Documentação:
- **Guia Simples:** [`docs/VERIFICACAO_SIMPLES_POLYGONSCAN.md`](./VERIFICACAO_SIMPLES_POLYGONSCAN.md)
- **Troubleshooting:** [`artifacts/verification/TROUBLESHOOTING_VERIFICACAO.md`](../artifacts/verification/TROUBLESHOOTING_VERIFICACAO.md)
- **Configurações Corretas:** [`artifacts/verification/CONFIGURACOES_CORRETAS.txt`](../artifacts/verification/CONFIGURACOES_CORRETAS.txt)

---

## 💡 Dicas Finais

1. **Comece pelo Token** - É o mais simples e já tem arquivo flattened pronto
2. **Use Gmail** - Não precisa de email com domínio próprio para verificação de código
3. **Seja paciente** - A verificação pode levar alguns minutos
4. **Verifique tudo** - Confira cada campo antes de enviar
5. **Salve os links** - Anote os links dos contratos para referência futura

---

**✅ Tudo pronto para verificação! Boa sorte!** 🚀

**Última atualização:** 2025-12-17
