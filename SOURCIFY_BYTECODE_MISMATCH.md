# ⚠️ Erro: Bytecode Length Mismatch no Sourcify

**Erro:** `bytecode_length_mismatch` - O bytecode recompilado não corresponde ao on-chain.

---

## 🔍 Problema:

O Sourcify está compilando o contrato com configurações diferentes das usadas no deploy, resultando em bytecode diferente.

---

## ✅ Soluções:

### **Opção 1: Ajustar EVM Version no Sourcify**

No Sourcify, quando você faz upload do arquivo, **escolha manualmente**:

1. **Compiler Version:** `0.8.30+commit.73712a01` (ou tente `0.8.18+commit.87f61d96`)
2. **EVM Version:** `default` (em vez de `paris`)
3. **Optimization:** ✅ Yes, Runs: `200`
4. **via-IR:** ❌ No (desabilitado)

### **Opção 2: Usar Polygonscan Direto (Mais Confiável)**

O Sourcify pode ter limitações. Use Polygonscan diretamente:

1. **Acesse:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
2. **Clique:** "Contract" → "Verify and Publish"
3. **Método:** "Via Standard JSON Input"
4. **Upload:** `artifacts/verification/sourcify_standard_json.json`
5. **Preencha:**
   - Compiler: `v0.8.30+commit.73712a01`
   - License: `MIT License (MIT)`
   - Optimization: ✅ Yes, Runs: `200`
   - EVM Version: `default`
   - Constructor Args: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

### **Opção 3: Usar Flattened Source Code (Mais Simples)**

1. **Acesse:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
2. **Clique:** "Contract" → "Verify and Publish"
3. **Método:** "Flattened Source Code"
4. **Arquivo:** `artifacts/flattened/NeoFlowToken_flattened_sourcify.sol`
5. **Preencha:**
   - Compiler: `v0.8.30+commit.73712a01`
   - License: `MIT License (MIT)`
   - Contract Name: `NeoFlowToken`
   - Optimization: ✅ Yes, Runs: `200`
   - EVM Version: `default`
   - Constructor Args: `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

---

## 🔧 Configurações Corretas (do Deploy):

- **Compiler:** `0.8.30+commit.73712a01`
- **Optimizer:** ✅ Enabled
- **Runs:** `200`
- **EVM Version:** `default` (não especificado no deploy, então usa default)
- **via-IR:** ❌ False (desabilitado)

---

## 💡 Por Que o Sourcify Pode Falhar:

1. **EVM Version:** Sourcify pode estar usando `paris` quando deveria ser `default`
2. **Compiler Version:** Pode não ter a versão exata `0.8.30+commit.73712a01`
3. **via-IR:** Pode estar habilitando quando não deveria

---

## ✅ Recomendação:

**Use Polygonscan diretamente com Flattened Source Code** - é mais confiável e você tem controle total sobre as configurações.

**Arquivo pronto:**
```
artifacts/flattened/NeoFlowToken_flattened_sourcify.sol
```

**Guia completo:** `docs/VERIFICACAO_COMPLETA_POLYGONSCAN.md`
