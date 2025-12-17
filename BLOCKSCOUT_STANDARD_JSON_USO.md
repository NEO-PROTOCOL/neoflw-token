# 📋 Como Usar o Standard JSON Input no Blockscout

## ✅ Arquivo Gerado

O Standard JSON Input perfeito foi gerado com sucesso:
```
artifacts/verification/blockscout_standard_json.json
```

**Estatísticas:**
- ✅ 22.0 KB
- ✅ Usa `NeoFlowToken_flattened_perfect.sol`
- ✅ 1 licença SPDX
- ✅ 1 pragma solidity
- ✅ Sem ContractMetadata (correto)

---

## 📝 Passo a Passo no Blockscout

### 1. Acesse o Contrato

```
https://polygon.blockscout.com/token/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

### 2. Clique em "Verify & publish"

Botão azul na página do contrato.

### 3. Escolha o Método

Selecione: **"Standard JSON Input"** ou **"Solidity (Standard JSON input)"**

### 4. Faça Upload do Arquivo

- Clique em **"Choose File"** ou **"Browse"**
- Navegue até: `artifacts/verification/blockscout_standard_json.json`
- Selecione e faça upload

### 5. Preencha os Campos Obrigatórios

⚠️ **IMPORTANTE:** Mesmo com Standard JSON, você precisa preencher estes campos:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` ⭐ **TESTE ESTA PRIMEIRO** |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowToken` |
| **Contract File Path** | `contracts/NeoFlowToken.sol` |
| **Optimization** | ✅ **Yes** (habilitado) |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` (ou `paris` se default não funcionar) |
| **via-IR** | ❌ **No** / **false** (desabilitado) |
| **Constructor Arguments** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |

### 6. Clique em "Verify"

---

## 🔧 Se Ainda Der Partial Match

Teste estas alternativas na ordem:

### Opção 1: Mudar Compiler Version

**Tentar primeiro:**
```
v0.8.18+commit.87f61d96
```

**Se não funcionar, tentar:**
```
v0.8.18
```
(sem commit hash)

**Ou:**
```
v0.8.30+commit.73712a01
```
(versão que deu Partial Match antes)

### Opção 2: Mudar EVM Version

- Se estava `default`, tente `paris`
- Se estava `paris`, tente `default`

### Opção 3: Verificar via-IR

Certifique-se que está **DESABILITADO**:
- ❌ No
- ❌ false
- ❌ unchecked

---

## ✅ Checklist Antes de Enviar

- [ ] Arquivo JSON carregado: `blockscout_standard_json.json`
- [ ] Compiler: `v0.8.18+commit.87f61d96` (ou alternativa)
- [ ] License: `MIT License (MIT)`
- [ ] Contract Name: `NeoFlowToken`
- [ ] Contract File Path: `contracts/NeoFlowToken.sol`
- [ ] Optimization: **Yes**, Runs: **200**
- [ ] EVM Version: `default` ou `paris`
- [ ] via-IR: **No** / **false**
- [ ] Constructor Args: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

---

## 💡 Dica

O Standard JSON Input é mais preciso que Flattened Source Code porque:
- ✅ Inclui metadados do compilador
- ✅ Preserva estrutura do código
- ✅ Melhor para correspondência de bytecode

---

## 📁 Arquivos Relacionados

- **Standard JSON:** `artifacts/verification/blockscout_standard_json.json`
- **Flattened Perfect:** `artifacts/flattened/NeoFlowToken_flattened_perfect.sol`
- **Script gerador:** `scripts/verification/generate_blockscout_standard_json.py`

---

**Última atualização:** Arquivo gerado com configurações otimizadas para resolver Partial Match
