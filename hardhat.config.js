// hardhat.config.js
// Configuração mínima do Hardhat APENAS para verificação no OKLink
// NOTA: Este projeto usa Ape Framework para deploy. Hardhat é usado apenas para verificação.

require("@nomicfoundation/hardhat-toolbox");
require("@okxweb3/hardhat-explorer-verify");
require("dotenv").config();
const SOLC_VERSION = process.env.SOLC_VERSION || "0.8.33";

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    // Para verificação legada de contratos já deployados, use:
    // SOLC_VERSION=0.8.30 npx hardhat verify ...
    version: SOLC_VERSION,
    settings: {
      optimizer: {
        enabled: true,
        runs: 200 // Mesma configuração do deploy
      }
    }
  },
  
  networks: {
    polygon: {
      url: process.env.ALCHEMY_API_KEY 
        ? `https://polygon-mainnet.g.alchemy.com/v2/${process.env.ALCHEMY_API_KEY}`
        : "https://polygon-rpc.com",
      chainId: 137,
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
  },
  
  // Configuração do OKLink Explorer (Method 1 - Recomendado)
  // API Key é opcional - verificação funciona sem ela
  okxweb3explorer: {
    apiKey: process.env.OKLINK_API_KEY || "", // Opcional - obter em https://www.oklink.com/docs/en/
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
  // O plugin pode usar etherscan como fallback, então configuramos aqui também
  etherscan: {
    apiKey: {
      polygon: process.env.OKLINK_API_KEY || process.env.ETHERSCAN_API_KEY || "",
    },
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
