# 📋 Variáveis .env para Verificação - O Que Precisa?

## ✅ Resumo Rápido:

**NÃO precisa adicionar nada no `.env`!** O script `auto_verify_smart.py` funciona com valores padrão.

---

## 🔍 O Que Cada Variável Faz:

### ❌ **NÃO Precisa no .env:**

1. **`OKLINK_API_URL`** 
   - ❌ Não precisa - é URL fixa da API
   - Valor padrão: `https://www.oklink.com/api/v5/explorer/contract/verify-source-code`

2. **`CHAIN_SHORT_NAME`**
   - ❌ Não precisa - script usa `"POLYGON"` por padrão
   - Se quiser mudar: `OKLINK_CHAIN_SHORT_NAME=POLYGON`

3. **`CONTRACT_ADDRESS`**
   - ❌ Não precisa - script usa `NEXT_PUBLIC_TOKEN_ADDRESS` do `.env` (já existe!)
   - Ou valor padrão: `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`

4. **`CONTRACT_NAME`**
   - ❌ Não precisa - script usa `"NeoFlowToken"` por padrão
   - Se quiser mudar: `OKLINK_CONTRACT_NAME=NeoFlowToken`

### ✅ **Opcional (mas recomendado):**

1. **`OKLINK_API_KEY`**
   - ✅ Opcional, mas recomendado
   - Melhora rate limits da API
   - Obter em: https://www.oklink.com/docs/en/#quickstart-guide-getting-started
   - Adicionar no `.env`:
     ```bash
     OKLINK_API_KEY=sua_oklink_api_key_aqui
     ```

---

## 📝 Como o Script Funciona:

O script `auto_verify_smart.py` agora suporta `.env` opcionalmente:

1. **Tenta ler do `.env`** (se existir)
2. **Se não existir, usa valor padrão** (hardcoded)

### Exemplo:

```python
# No script:
CONTRACT_ADDRESS = os.getenv("NEXT_PUBLIC_TOKEN_ADDRESS", "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
```

**Comportamento:**
- Se `NEXT_PUBLIC_TOKEN_ADDRESS` existir no `.env` → usa esse valor ✅
- Se não existir → usa `"0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"` ✅

---

## 🎯 Recomendação Final:

**Para uso normal:** Não precisa adicionar nada! O script já funciona.

**Para melhor performance:** Adicione apenas:
```bash
OKLINK_API_KEY=sua_oklink_api_key_aqui
```

**Para mudar configurações:** Adicione (opcional):
```bash
OKLINK_CHAIN_SHORT_NAME=POLYGON
OKLINK_CONTRACT_NAME=NeoFlowToken
# CONTRACT_ADDRESS já existe como NEXT_PUBLIC_TOKEN_ADDRESS
```

---

## ✅ Variáveis que JÁ Existem no .env e São Usadas:

- ✅ `NEXT_PUBLIC_TOKEN_ADDRESS` - Usado automaticamente pelo script
- ✅ `ALCHEMY_API_KEY` - Usado para RPC (se necessário)
- ✅ `ETHERSCAN_API_KEY` - Para outras verificações

---

**Resumo:** O script funciona sem adicionar nada no `.env`! 🚀
