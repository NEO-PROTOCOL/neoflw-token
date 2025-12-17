# ✅ Polygonscan - Passo a Passo Atualizado

## 🎯 Método Recomendado: Standard JSON Input

### 📋 Passo a Passo Completo

1. **Acesse o contrato:**
   ```
   https://polygonscan.com/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2#code
   ```

2. **Clique em:**
   - Aba **"Contract"** (no topo da página)
   - Botão **"Verify and Publish"** (dentro da aba Contract)

3. **Escolha o método:**
   - **"Via Standard JSON Input"** ⭐ (RECOMENDADO)
   - OU **"Via Single File (Solidity)"** (se não tiver Standard JSON)

---

## 🔧 Opção 1: Via Standard JSON Input (RECOMENDADO)

### Preencha os Campos:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` ⭐ **TESTE ESTA PRIMEIRO** |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowToken` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` |
| **Constructor Arguments** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **Standard JSON Input** | **Upload do arquivo:** `artifacts/verification/sourcify_standard_json.json` |

### Como Fazer Upload:
- Clique no botão "Choose File" ou "Browse"
- Navegue até: `/Users/nettomello/CODIGOS/TOKENS/neoflw-token/artifacts/verification/sourcify_standard_json.json`
- Selecione o arquivo e faça upload

---

## 🔧 Opção 2: Via Single File (Solidity) (ALTERNATIVA)

Se não tiver "Standard JSON Input", use esta opção:

### Preencha os Campos:

| Campo | Valor |
|-------|-------|
| **Compiler Version** | `v0.8.18+commit.87f61d96` ⭐ **TESTE ESTA PRIMEIRO** |
| **License** | `MIT License (MIT)` |
| **Contract Name** | `NeoFlowToken` |
| **Optimization** | ✅ **Yes** |
| **Optimization Runs** | `200` |
| **EVM Version** | `default` |
| **Constructor Arguments** | `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000` |
| **Source Code** | **Cole o conteúdo completo** de `artifacts/flattened/NeoFlowToken_original_flattened.sol` |

### Como Copiar o Código:
1. Abra o arquivo: `artifacts/flattened/NeoFlowToken_original_flattened.sol`
2. Selecione tudo (Ctrl+A ou Cmd+A)
3. Copie (Ctrl+C ou Cmd+C)
4. Cole no campo "Source Code" do Polygonscan

---

## 🎯 Versões do Compilador para Testar (NESTA ORDEM)

Se `v0.8.18+commit.87f61d96` não funcionar, teste estas versões:

1. **v0.8.18+commit.87f61d96** ⭐ (MAIS PROVÁVEL)
2. **v0.8.18** (sem commit hash)
3. **v0.8.17+commit.8df45f5f**
4. **v0.8.16+commit.07a7930e**
5. **v0.8.15+commit.e14f2714**
6. **v0.8.19+commit.425a24f5**

---

## ⚠️ Importante

- **NÃO mude os outros campos** entre tentativas
- Apenas altere a **versão do compilador**
- Mantenha sempre: Optimization Yes (200 runs), EVM Version default

---

## ✅ Como Saber se Funcionou

✅ **Sucesso:** Você verá uma mensagem de confirmação e o contrato ficará verificado.

❌ **Erro:** Você verá uma mensagem de erro. Tente a próxima versão da lista.

---

## 🆘 Se Não Encontrar as Opções

Se você não vê "Standard JSON Input" nem "Single File", me diga:
- O que aparece na tela quando você clica em "Verify and Publish"?
- Quais opções/métodos estão disponíveis?

Isso me ajudará a criar um guia mais específico para sua situação.
