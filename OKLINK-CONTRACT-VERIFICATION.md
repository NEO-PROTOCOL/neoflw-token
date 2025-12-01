# 🔧 Configurar Hardhat + OKLink Plugin para Verificação

**Data**: 29 de Novembro de 2025

---

## ⚠️ IMPORTANTE - REDE DO PROJETO

**Este projeto é deployado na POLYGON MAINNET, não em X Layer ou outras chains da OKX.**

- ✅ **Rede**: Polygon Mainnet (Chain ID: 137)
- ✅ **Chain Short Name**: `POLYGON`
- ❌ **NÃO é**: X Layer, X Layer Testnet, ou outras chains da OKX
- 🔗 **Explorer**: https://polygonscan.com (PolygonScan) ou https://www.oklink.com/polygon (OKLink)

---

## 📋 Pré-requisitos

- **Repositório do contrato**: `github.com/kauntdewn1/neoflw-token`
- **Contrato**: `0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2`
- **Chain**: **Polygon Mainnet (137)** - ⚠️ NÃO confundir com X Layer
- **Chain Short Name**: `POLYGON`

---

## 🚀 Passo a Passo

### **1. Clonar o Repositório do Contrato**

```bash
# Se ainda não tiver clonado
git clone https://github.com/kauntdewn1/neoflw-token.git
cd neoflw-token
```

### **2. Instalar Dependências**

```bash
npm install
```

### **3. Instalar Plugin do OKLink**

```bash
npm install @okxweb3/hardhat-explorer-verify --save-dev
```

### **4. Configurar hardhat.config.js**

Edite o arquivo `hardhat.config.js` (ou `hardhat.config.ts`) e adicione:

```javascript
import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import '@okxweb3/hardhat-explorer-verify';  // Importar o plugin

const config: HardhatUserConfig = {
  solidity: {
    version: "0.8.20", // Ajustar para versão usada no deploy
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  
  networks: {
    polygon: {
      url: process.env.POLYGON_RPC_URL || "https://polygon-mainnet.infura.io/v3/9afb8749df8f4370aded1dce851d13f4",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 137,
    },
  },
  
  // Configuração do OKLink Explorer
  okxweb3explorer: {
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
  },
  
  // Configuração alternativa usando etherscan (Method 2)
  etherscan: {
    customChains: [
      {
        network: "polygon",
        chainId: 137,
        urls: {
          apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/POLYGON",
          browserURL: "https://www.oklink.com",
        }
      }
    ]
  }
};

export default config;
```

### **5. Configurar Variáveis de Ambiente**

Crie ou edite o arquivo `.env` no repositório do contrato:

```bash
# Polygon RPC
POLYGON_RPC_URL=https://polygon-mainnet.infura.io/v3/9afb8749df8f4370aded1dce851d13f4

# Private Key (opcional, apenas se precisar fazer deploy)
PRIVATE_KEY=sua_private_key_aqui
```

### **6. Verificar o Contrato**

Execute o comando de verificação:

```bash
npx hardhat okverify --network polygon 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Com nome do contrato específico** (se houver múltiplos contratos):

```bash
npx hardhat okverify --network polygon --contract contracts/NEOFLWToken.sol:NEOFLWToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

### **7. Verificar Contrato Proxy (se aplicável)**

Se o contrato for um proxy:

```bash
npx hardhat okverify --network polygon --contract contracts/NEOFLWToken.sol:NEOFLWToken --proxy 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

**Nota**: Se usar contrato 897, não adicione `--proxy`, use diretamente:

```bash
npx hardhat okverify --network polygon --contract contracts/NEOFLWToken.sol:NEOFLWToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

---

## 📝 Exemplo Completo de hardhat.config.js

```javascript
require("@nomicfoundation/hardhat-toolbox");
require("@okxweb3/hardhat-explorer-verify");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.20",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    polygon: {
      url: process.env.POLYGON_RPC_URL || "https://polygon-mainnet.infura.io/v3/9afb8749df8f4370aded1dce851d13f4",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 137,
    },
  },
  okxweb3explorer: {
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
};
```

---

## 🔍 Verificar Resultado

Após a verificação bem-sucedida, você pode ver o contrato verificado em:

```
https://www.oklink.com/polygon/address/0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

---

## ⚠️ Troubleshooting

### **Erro: "Contract not found"**

- Verifique se o endereço do contrato está correto
- Confirme que está na rede correta (Polygon Mainnet)

### **Erro: "Compiler version mismatch"**

- Use exatamente a mesma versão do compilador usada no deploy
- Verifique em `hardhat.config.js` ou nos artifacts

### **Erro: "Optimization settings mismatch"**

- Use as mesmas configurações de otimização do deploy
- Verifique `optimizer.enabled` e `optimizer.runs`

### **Erro: "Source code not found"**

- Certifique-se de que os arquivos de contrato estão no caminho correto
- Se usar imports, pode precisar fazer flatten do código

---

## 📚 Recursos

- **Plugin GitHub**: https://github.com/okx/hardhat-explorer-verify
- **OKLink Explorer**: https://www.oklink.com/
- **Documentação API**: https://www.oklink.com/docs/en/
- **Lista de Chains Suportadas**: https://www.oklink.com/docs/zh/#quickstart-guide-list-of-supported-chains

---

## 🎯 Comandos Rápidos

```bash
# 1. Instalar plugin
npm install @okxweb3/hardhat-explorer-verify --save-dev

# 2. Verificar contrato
npx hardhat okverify --network polygon 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2

# 3. Verificar com nome específico
npx hardhat okverify --network polygon --contract contracts/NEOFLWToken.sol:NEOFLWToken 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2

# 4. Verificar proxy
npx hardhat okverify --network polygon --contract contracts/NEOFLWToken.sol:NEOFLWToken --proxy 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
```

---

**Última atualização**: 29 de Novembro de 2025

