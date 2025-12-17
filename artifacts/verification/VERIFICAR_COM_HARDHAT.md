# ✅ Verificar Contrato usando Hardhat + Plugin OKLink

## 📋 Status Atual

✅ **Plugin instalado:** `@okxweb3/hardhat-explorer-verify@^1.6.5`  
✅ **Configuração:** `hardhat.config.js` já configurado  
✅ **Network:** Polygon Mainnet (137)  
✅ **Contrato:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`

---

## 🚀 COMANDO PARA VERIFICAR

### Comando Básico (Recomendado):

```bash
npx hardhat okverify \
  --network polygon \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

### Com Constructor Arguments:

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  --constructor-args "1000000000000000000000000000"
```

**Nota:** O valor `1000000000000000000000000000` é `1_000_000_000 * 10**18` (1 bilhão de tokens)

---

## 📝 Configuração Atual (hardhat.config.js)

A configuração já está correta:

```javascript
okxweb3explorer: {
  apiKey: process.env.OKLINK_API_KEY || "", // Opcional
  customChains: [
    {
      network: "Polygon Mainnet",
      chainId: 137,
      urls: {
        apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
        browserURL: "https://www.oklink.com",
      }
    }
  ]
}
```

---

## 🔧 Vantagens do Plugin Hardhat

✅ **Automático:** Detecta automaticamente as configurações de compilação  
✅ **Simples:** Um comando apenas  
✅ **Oficial:** Plugin mantido pelo OKLink  
✅ **Inteligente:** Tenta diferentes formatos automaticamente  

---

## ⚙️ O que o Plugin Faz Automaticamente

1. ✅ Lê as configurações do `hardhat.config.js`
2. ✅ Compila o contrato com as mesmas configurações do deploy
3. ✅ Extrai o código fonte e dependências
4. ✅ Envia para o OKLink com os parâmetros corretos
5. ✅ Verifica o status automaticamente

---

## 🎯 Comando Completo (com todas as opções):

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  --constructor-args "1000000000000000000000000000"
```

---

## 📋 Checklist Antes de Executar

- [x] Plugin instalado (`@okxweb3/hardhat-explorer-verify`)
- [x] `hardhat.config.js` configurado
- [x] Network `polygon` configurada
- [x] Contrato compilado localmente
- [ ] `OKLINK_API_KEY` no `.env` (opcional, mas recomendado)

---

## 💡 Dica

Se o comando básico não funcionar, tente especificar o contrato explicitamente:

```bash
npx hardhat okverify \
  --network polygon \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

---

## 🔗 Referência

Documentação oficial: https://github.com/okx/hardhat-explorer-verify

