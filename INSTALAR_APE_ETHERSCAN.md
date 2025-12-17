# 🔧 Instalar Plugin Etherscan no Ape Framework

## ⚠️ Problema Encontrado

O comando `ape etherscan verify` não funciona porque o plugin não está instalado.

## ✅ Solução Rápida

Execute este comando:

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
ape plugins install etherscan
```

Depois disso, você pode usar:

```bash
ape etherscan verify NeoFlowToken --network polygon:mainnet
```

---

## 🚀 Depois de Instalar

O script automático funcionará:

```bash
./VERIFICAR_AUTOMATICO.sh
```

---

## 📋 O Que o Plugin Faz

- ✅ Conecta com Polygonscan automaticamente
- ✅ Usa as mesmas configurações do deploy
- ✅ Envia código fonte e metadados
- ✅ Verifica automaticamente

---

## ⚙️ Configuração Necessária

Certifique-se de ter no `.env`:

```bash
POLYGONSCAN_API_KEY=sua_chave_aqui
```

**Como obter:** https://polygonscan.com/apis
