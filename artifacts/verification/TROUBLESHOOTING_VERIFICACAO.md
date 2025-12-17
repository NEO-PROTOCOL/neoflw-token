# 🔧 Troubleshooting - Erro de Verificação

## ❌ Erro: "O código-fonte compilado não corresponde ao bytecode do contrato on-chain"

### 📊 Situação Atual

- **Bytecode deployado:** 2999 bytes (sem ContractMetadata)
- **Bytecode compilado localmente:** 4105 bytes (com ContractMetadata)
- **Arquivo correto:** `NeoFlowToken_original_flattened.sol` (sem ContractMetadata)

---

## 🔍 Possíveis Causas e Soluções

### 1. Versão do Compilador Incorreta

**Problema:** O commit hash do compilador pode estar errado.

**Solução:** Tente estas versões na ordem:

```
1. v0.8.30+commit.73712a01  (versão no cache)
2. v0.8.30+commit.8c9944cf  (versão mencionada anteriormente)
3. v0.8.30                   (sem commit hash)
4. v0.8.18+commit.87f61d96  (versão do pragma)
5. v0.8.29+commit.736ccbcf   (versão anterior)
6. v0.8.28+commit.736ccbcf   (versão anterior)
```

**Como verificar:** No Tenderly/OKLink, teste cada versão até encontrar a que funciona.

---

### 2. Configurações de Compilação

**Verifique se TODAS estas configurações estão corretas:**

- ✅ **Compiler Version:** Tente as versões acima
- ✅ **Optimization:** `Yes` (habilitado)
- ✅ **Optimization Runs:** `200`
- ✅ **EVM Version:** `paris` (ou `default`)
- ✅ **via-IR:** `false` (não habilitado)
- ✅ **License:** `MIT License (MIT)`

---

### 3. Código Fonte

**Certifique-se de usar o arquivo correto:**

- ✅ **Arquivo:** `artifacts/flattened/NeoFlowToken_original_flattened.sol`
- ✅ **NÃO use:** `NeoFlowToken_flattened_clean.sol` (tem ContractMetadata)
- ✅ **Copie TODO o conteúdo** (Ctrl+A, Ctrl+C)

---

### 4. Constructor Arguments

**Verifique se está correto:**

```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

Isso representa: `1_000_000_000 * 10**18` (1 bilhão de tokens)

---

### 5. Standard JSON Input

**Se usando Standard JSON Input:**

- ✅ Use: `artifacts/verification/oklink_standard_json_original.json`
- ✅ Verifique se o `compilerVersion` no JSON está correto
- ✅ Verifique se `optimizer.enabled` está como `true`
- ✅ Verifique se `optimizer.runs` está como `200`
- ✅ Verifique se `evmVersion` está como `"paris"`

---

## 🎯 Passo a Passo para Resolver

### Opção 1: Flattened Source Code (Recomendado)

1. Abra: `artifacts/flattened/NeoFlowToken_original_flattened.sol`
2. Copie TODO o conteúdo
3. No Tenderly/OKLink:
   - Método: **Flattened Source Code**
   - Compiler: Tente `v0.8.30` primeiro, depois as outras versões
   - Optimization: `Yes`, Runs: `200`
   - EVM Version: `paris` ou `default`
   - Constructor Args: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`
4. Tente cada versão do compilador até funcionar

### Opção 2: Standard JSON Input

1. Abra: `artifacts/verification/oklink_standard_json_original.json`
2. Edite o campo `compilerVersion` no JSON (se necessário)
3. Copie TODO o JSON
4. No Tenderly/OKLink:
   - Método: **Standard JSON Input**
   - Cole o JSON completo
   - Constructor Args: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

---

## 🔍 Verificar Bytecode On-Chain

Para verificar o bytecode deployado:

```bash
python3 scripts/verification/check_bytecode_match.py
```

Isso mostrará:
- Tamanho do bytecode deployado
- Tamanho do bytecode compilado
- Primeira diferença encontrada

---

## 💡 Dicas Finais

1. **Tente versões diferentes do compilador** - O commit hash pode variar
2. **Use o arquivo original** - Sem ContractMetadata
3. **Verifique todas as configurações** - Optimization, EVM Version, etc.
4. **Se nada funcionar** - Pode ser necessário verificar qual versão exata foi usada no deploy original

---

## 📝 Checklist de Verificação

- [ ] Usando arquivo `NeoFlowToken_original_flattened.sol`
- [ ] Constructor args correto
- [ ] Optimization: Yes, Runs: 200
- [ ] EVM Version: paris ou default
- [ ] via-IR: false (não habilitado)
- [ ] Tentou múltiplas versões do compilador
- [ ] Código fonte copiado completamente

