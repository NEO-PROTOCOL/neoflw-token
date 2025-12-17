# ⚠️ OKLink Hardhat - API Será Suspensa em 20/05/2025

> **ATENÇÃO:** OKLink anunciou suspensão da API em 20 de maio de 2025.  
> **Recomendação:** Use Sourcify (veja `VERIFICACAO_FINAL_SOURCIFY.md`)  
> Veja detalhes: `OKLINK_API_SUSPENSA.md`

---

# ✅ Comando OKLink Hardhat - CORRIGIDO

## ❌ Erro Anterior:

```bash
npx hardhat okverify --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  --constructor-args 0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

**Erro:** `--constructor-args` espera um arquivo JavaScript, não um valor hexadecimal.

---

## ✅ Comandos Corretos:

### Opção 1: Sem Constructor Args (Recomendado - Tenta Detectar Automaticamente)

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

### Opção 2: Com Constructor Args como Argumentos Posicionais

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  "1000000000000000000000000000"
```

**Nota:** Use o valor decimal (`1000000000000000000000000000`), não o hexadecimal.

### Opção 3: Com Constructor Args em Arquivo JavaScript

Crie um arquivo `constructor-args.js`:

```javascript
module.exports = ["1000000000000000000000000000"];
```

Depois execute:

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  --constructor-args constructor-args.js
```

---

## 🚀 Execute Agora:

**Tente primeiro sem constructor args (mais simples):**

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

Se não funcionar, tente com o valor decimal:

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  "1000000000000000000000000000"
```

---

## 📋 Informações do Contrato:

- **Endereço:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Constructor Arg (decimal):** `1000000000000000000000000000` (1 bilhão * 10^18)
- **Constructor Arg (hex):** `0x33b2e3c9fd0803ce8000000`
- **Constructor Arg (ABI-encoded):** `0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000`

---

## 💡 Dica:

O plugin OKLink Hardhat é inteligente e pode detectar automaticamente os constructor args na maioria dos casos. Tente primeiro sem especificar!
