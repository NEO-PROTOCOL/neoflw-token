# ✅ EVM Version Corrigido no Standard JSON

**Erro:** `Invalid EVM version requested` - "default" não é válido no Sourcify.

---

## 🔧 Correção Aplicada:

**Antes:**
```json
"evmVersion": "default"  ❌ (inválido)
```

**Agora:**
```json
"evmVersion": "paris"  ✅ (válido - padrão do Solidity 0.8.30)
```

---

## 📝 Explicação:

Quando você não especifica `evmVersion` no deploy, o Solidity 0.8.30 usa **"paris"** como padrão.

No Standard JSON, você **deve** especificar um valor válido:
- ✅ `paris` (padrão para 0.8.30)
- ✅ `shanghai`
- ✅ `london`
- ✅ `cancun`
- ❌ `default` (não é válido)

---

## ✅ Arquivo Corrigido:

```
artifacts/verification/sourcify_standard_json.json
```

**Configurações finais:**
- ✅ Optimizer: Enabled, Runs: 200
- ✅ EVM Version: `paris` (corrigido)
- ✅ via-IR: False (não especificado = false)
- ✅ 1 licença SPDX
- ✅ Sem imports não resolvidos

---

## 🚀 Próximo Passo:

**Tente novamente no Sourcify:**

1. Acesse: https://sourcify.dev/verifier
2. Upload: `artifacts/verification/sourcify_standard_json.json` (corrigido)
3. Selecione: `contracts/NeoFlowToken.sol: NeoFlowToken`
4. Compiler: `0.8.30+commit.73712a01`
5. Clique em "Verify"

**Agora deve funcionar!** ✅
