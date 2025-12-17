# 🔧 Comandos de Verificação - Adaptados para NeoFlowToken

## 📋 Informações do Contrato

- **Endereço:** `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Arquivo:** `contracts/NeoFlowToken.sol`
- **Nome do Contrato:** `NeoFlowToken`
- **Chain:** Polygon Mainnet (Chain ID: 137)
- **Chain Short Name:** `POLYGON`

---

## 1️⃣ Foundry (Forge) - Se você instalar Foundry

### Comando Adaptado:

```bash
forge verify-contract \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  contracts/NeoFlowToken.sol:NeoFlowToken \
  --verifier oklink \
  --verifier-url "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON" \
  --chain-id 137 \
  --etherscan-api-key $OKLINK_API_KEY \
  --watch
```

### Com Constructor Arguments:

```bash
forge verify-contract \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  contracts/NeoFlowToken.sol:NeoFlowToken \
  --verifier oklink \
  --verifier-url "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON" \
  --chain-id 137 \
  --etherscan-api-key $OKLINK_API_KEY \
  --constructor-args $(cast abi-encode "constructor(uint256)" 1000000000000000000000000000) \
  --watch
```

### Verificar Status (sem --watch):

```bash
forge verify-check \
  --chain-id 137 \
  --verifier oklink \
  --verifier-url "https://www.oklink.com/api/v5/explorer/contract/check-verify-result" \
  <GUID>
```

---

## 2️⃣ Hardhat (Já Configurado no Projeto)

### Comando:

```bash
npx hardhat okverify \
  --network polygon \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  --contract contracts/NeoFlowToken.sol:NeoFlowToken \
  --constructor-args 0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

### Ou usando etherscan (configurado para OKLink):

```bash
npx hardhat verify \
  --network polygon \
  0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2 \
  "1000000000000000000000000000"
```

---

## 3️⃣ Script Python Automático (RECOMENDADO)

### Versão Inteligente:

```bash
python3 scripts/verification/auto_verify_smart.py
```

### Versão Completa:

```bash
python3 scripts/verification/auto_verify.py
```

---

## 4️⃣ API Direta (OKLink)

### Usando curl:

```bash
curl -X POST "https://www.oklink.com/api/v5/explorer/contract/verify-source-code" \
  -H "Content-Type: application/json" \
  -H "Ok-Access-Key: $OKLINK_API_KEY" \
  -d '{
    "chainShortName": "POLYGON",
    "contractAddress": "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2",
    "contractName": "NeoFlowToken",
    "sourceCode": "...",
    "codeFormat": "solidity-single-file",
    "compilerVersion": "v0.8.30+commit.73712a01",
    "optimization": "1",
    "optimizationRuns": "200",
    "evmVersion": "paris",
    "viaIr": "false",
    "licenseType": "MIT License (MIT)",
    "constructorArguments": "0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"
  }'
```

---

## 📝 Constructor Arguments (ABI-encoded)

```
0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000
```

Isso representa: `1_000_000_000 * 10**18` (1 bilhão de tokens)

---

## ⚙️ Configurações de Compilação

- **Compiler:** `v0.8.30+commit.73712a01` (ou `v0.8.18+commit.87f61d96`)
- **Optimization:** `Yes` (200 runs)
- **EVM Version:** `paris` (ou `default`)
- **via-IR:** `false` (não habilitado)
- **License:** `MIT License (MIT)`

---

## 💡 Recomendação

**Use o script Python automático** (`auto_verify_smart.py`) - ele testa automaticamente diferentes configurações até encontrar a que funciona!

