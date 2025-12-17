# 📋 Métodos de Verificação no Polygonscan

## 🎯 Métodos Disponíveis

O Polygonscan oferece vários métodos de verificação. Dependendo da interface, você pode ver:

### **Método 1: Via Standard JSON Input** ⭐ (RECOMENDADO)
- **Nome:** "Via Standard JSON Input" ou "Standard JSON Input"
- **Quando usar:** Quando você tem um arquivo JSON com o código completo

### **Método 2: Via Single File (Solidity)**
- **Nome:** "Via Single File (Solidity)" ou "Single File"
- **Quando usar:** Quando você tem o código em um único arquivo flattened

### **Método 3: Via Multi-File**
- **Nome:** "Via Multi-File" ou "Multi-File"
- **Quando usar:** Quando você tem múltiplos arquivos Solidity

### **Método 4: Via Sourcify**
- **Nome:** "Via Sourcify"
- **Quando usar:** Para verificação automática via Sourcify

---

## ✅ SOLUÇÃO: Use "Via Standard JSON Input"

### 📋 Passo a Passo

1. **Acesse:** https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code

2. **Clique:** "Contract" → "Verify and Publish"

3. **Escolha:** **"Via Standard JSON Input"** (ou "Standard JSON Input")

4. **Preencha os campos:**

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` ⭐ **TESTE ESTA PRIMEIRO** |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowToken` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` |
| **Constructor Arguments** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **Standard JSON Input** | Faça upload do arquivo: `artifacts/verification/sourcify_standard_json.json` |

5. **Se não funcionar, teste estas versões (NESTA ORDEM):**

---

## 🎯 Versões do Compilador para Testar

### **1. v0.8.18+commit.87f61d96** ⭐ (MAIS PROVÁVEL)
```
v0.8.18+commit.87f61d96
```

### **2. v0.8.18** (sem commit hash)
```
v0.8.18
```

### **3. v0.8.17+commit.8df45f5f**
```
v0.8.17+commit.8df45f5f
```

### **4. v0.8.16+commit.07a7930e**
```
v0.8.16+commit.07a7930e
```

### **5. v0.8.15+commit.e14f2714**
```
v0.8.15+commit.e14f2714
```

### **6. v0.8.19+commit.425a24f5**
```
v0.8.19+commit.425a24f5
```

---

## 🔄 Alternativa: Se Não Tiver "Standard JSON Input"

Se não aparecer "Standard JSON Input", tente:

### **Opção A: "Via Single File (Solidity)"**

1. **Escolha:** "Via Single File (Solidity)" ou "Single File"

2. **Preencha:**
   - **Compiler Version:** `v0.8.18+commit.87f61d96`
   - **License:** `MIT License (MIT)`
   - **Contract Name:** `NeoFlowToken`
   - **Optimization:** Yes, Runs: 200
   - **EVM Version:** `default`
   - **Constructor Arguments:** `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`
   - **Source Code:** Cole o conteúdo de `artifacts/flattened/NeoFlowToken_original_flattened.sol`

---

## 📸 O Que Você Vê na Tela?

Quando você clica em "Verify and Publish", você deve ver algo como:

```
┌─────────────────────────────────────┐
│  Verify & Publish Contract Source   │
├─────────────────────────────────────┤
│                                     │
│  ○ Via Standard JSON Input          │
│  ○ Via Single File (Solidity)      │
│  ○ Via Multi-File                   │
│  ○ Via Sourcify                     │
│                                     │
└─────────────────────────────────────┘
```

**Se você não vê essas opções, me diga o que aparece na sua tela!**

---

## 💡 Dica

O nome exato pode variar dependendo da versão do Polygonscan. Procure por:
- "Standard JSON"
- "JSON Input"
- "Single File"
- "Solidity Single File"
- "Flattened" (pode estar em algum lugar)
