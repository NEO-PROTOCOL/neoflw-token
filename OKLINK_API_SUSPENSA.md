# ⚠️ IMPORTANTE: OKLink API Será Suspensa em Maio 2025

**Data do Anúncio:** 10 de Abril de 2025  
**Data de Suspensão:** 20 de Maio de 2025

---

## 📢 O Que Aconteceu:

O OKLink anunciou que **suspenderá o serviço de API do Explorer** em **20 de maio de 2025**.

**Anúncio oficial:**
- Link: https://oklinksupport.zendesk.com/hc/zh-hk/articles/36655836705172
- Data efetiva: 20 de maio de 2025
- Reembolsos: até 30 de maio de 2025

---

## ⚠️ Impacto no Projeto:

### ❌ **O Que Para de Funcionar:**

1. **Script `auto_verify_smart.py`**
   - Usa API do OKLink para verificação
   - **Não funcionará após 20/05/2025**

2. **Hardhat Plugin `@okxweb3/hardhat-explorer-verify`**
   - Depende da API do OKLink
   - **Não funcionará após 20/05/2025**

3. **Verificação via API direta do OKLink**
   - Todos os scripts que usam `https://www.oklink.com/api/v5/explorer/contract/verify-source-code`
   - **Não funcionarão após 20/05/2025**

### ✅ **O Que Ainda Funciona:**

1. **Sourcify** ✅
   - **RECOMENDADO** - Funciona independente do OKLink
   - Arquivo já corrigido: `artifacts/verification/sourcify_standard_json.json`
   - Guia: `VERIFICACAO_FINAL_SOURCIFY.md`

2. **Polygonscan Manual** ✅
   - Verificação direta no site
   - Guia: `docs/VERIFICACAO_COMPLETA_POLYGONSCAN.md`

3. **OKLink Explorer (Interface Web)** ✅
   - Apenas a **API** será suspensa
   - O explorer web continua funcionando
   - Você ainda pode ver contratos em https://www.oklink.com/polygon

---

## 🚀 Ação Recomendada IMEDIATA:

### **Opção 1: Usar Sourcify (Mais Fácil)** ⭐

**Arquivo já está pronto e corrigido!**

1. Acesse: https://sourcify.dev/verifier
2. Upload: `artifacts/verification/sourcify_standard_json.json`
3. Selecione: `contracts/NeoFlowToken.sol: NeoFlowToken`
4. Clique em "Verify"

**Vantagens:**
- ✅ Funciona agora e continuará funcionando
- ✅ Arquivo já corrigido (sem erros de licença/import)
- ✅ Aparece automaticamente no Polygonscan
- ✅ Gratuito e confiável

**Guia completo:** `VERIFICACAO_FINAL_SOURCIFY.md`

### **Opção 2: Polygonscan Manual**

1. Acesse: https://polygonscan.com/verifyContract
2. Use o arquivo flattened: `artifacts/flattened/NeoFlowToken_flattened_sourcify.sol`
3. Preencha as configurações (ver guia)

**Guia completo:** `docs/VERIFICACAO_COMPLETA_POLYGONSCAN.md`

---

## 📋 Timeline:

- **10 de Abril de 2025:** Anúncio da suspensão
- **20 de Maio de 2025:** API desativada ⚠️
- **30 de Maio de 2025:** Última data para reembolsos

---

## 💰 Reembolso (Se Aplicável):

Se você tem API key paga do OKLink e quer reembolso:

1. **Prazo:** Enviar até 20 de maio de 2025
2. **Email:** apiservice@oklink.com
3. **Assunto:** `[API Refund Request]`
4. **Informações necessárias:**
   - Seu UID (Profile > My Profile > UID)
   - Endereço USDT na rede Tron (TRC-20)
5. **Reembolso:** Será processado até 30 de maio de 2025

---

## ✅ Recomendação Final:

**Use Sourcify AGORA!**

- ✅ Arquivo já está corrigido e pronto
- ✅ Não depende do OKLink
- ✅ Funciona permanentemente
- ✅ Mais fácil que Polygonscan manual

**Arquivo pronto:**
```
artifacts/verification/sourcify_standard_json.json
```

**Guia:**
```
VERIFICACAO_FINAL_SOURCIFY.md
```

---

## 📝 Nota:

O OKLink Explorer (interface web) **continua funcionando**. Apenas a **API** será suspensa. Você ainda poderá:
- Ver contratos em https://www.oklink.com/polygon
- Navegar pelo explorer
- Ver transações e blocos

Apenas a **verificação automática via API** será desativada.

---

**Última atualização:** 17 de Dezembro de 2024
