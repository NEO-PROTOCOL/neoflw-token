# ✅ VERIFICAÇÃO PLUG-AND-PLAY COM APE FRAMEWORK

## 🚀 COMANDO ÚNICO (MAIS SIMPLES)

O projeto já tem o Ape Framework configurado! Use este comando:

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
ape etherscan verify NeoFlowToken --network polygon:mainnet
```

**PRONTO!** ✅ O Ape Framework faz tudo automaticamente:
- ✅ Detecta as configurações de compilação
- ✅ Envia para o Polygonscan
- ✅ Verifica automaticamente

---

## 🔧 Se Precisar de Constructor Arguments

Se o comando acima não funcionar, tente:

```bash
ape etherscan verify NeoFlowToken \
  --network polygon:mainnet \
  --constructor-args 0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

---

## 🎯 Script Automático (Tenta Tudo)

Execute este script que tenta todas as formas:

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
./VERIFICAR_AUTOMATICO.sh
```

Este script tenta:
1. ✅ Ape Framework (mais simples)
2. ✅ Hardhat + OKLink
3. ✅ Script Python automático

---

## ⚙️ Configuração Necessária

Certifique-se de ter no `.env`:

```bash
POLYGONSCAN_API_KEY=sua_chave_aqui
```

**Como obter a chave:**
1. Acesse: https://polygonscan.com/apis
2. Crie uma conta (se não tiver)
3. Gere uma API Key
4. Adicione no `.env`

---

## ✅ Vantagens do Ape Framework

- ✅ **Automático:** Detecta tudo sozinho
- ✅ **Simples:** Um comando apenas
- ✅ **Inteligente:** Usa as mesmas configurações do deploy
- ✅ **Confiável:** Framework oficial e testado

---

## 🆘 Se Não Funcionar

1. **Verifique se o Ape está instalado:**
   ```bash
   ape --version
   ```

2. **Instale o plugin etherscan (se necessário):**
   ```bash
   ape plugins install etherscan
   ```

3. **Verifique a configuração:**
   ```bash
   cat ape-config.yaml
   ```

4. **Tente o script automático:**
   ```bash
   ./VERIFICAR_AUTOMATICO.sh
   ```
