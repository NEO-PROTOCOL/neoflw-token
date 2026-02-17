# 🔍 SmartMuv - Validação e Análise de Contratos

**SmartMuv** é uma ferramenta de análise de storage layout e extração de dados de contratos inteligentes EVM-compatíveis.

> **Repositório:** https://github.com/mello-labs/SmartMuv.git

---

## 📋 O que o SmartMuv faz

### ✅ Funcionalidades Principais

1. **Análise de Storage Layout (Slots)**
   - Mapeia todas as variáveis de estado e seus slots
   - Identifica mappings, arrays e estruturas complexas
   - Valida alocação de memória

2. **Extração de Estado Completo**
   - Extrai dados de contratos já deployados
   - Lista holders, balances, mappings
   - Recupera dados de estruturas complexas

3. **Migração de Dados**
   - Prepara dados para migração entre contratos
   - Útil para upgrades ou migrações L1→L2

4. **Análise Estática**
   - Aproximação de chaves em mappings
   - Análise de código-fonte Solidity

---

## 🚀 Instalação

### **1. Clonar Repositório**

```bash
cd /Users/nettomello/CODIGOS
git clone https://github.com/mello-labs/SmartMuv.git
cd SmartMuv
```

### **2. Instalar Dependências**

```bash
# Instalar pacotes Python necessários
python3 setup.py install
```

### **3. Instalar Compiladores Solidity**

```bash
# Instalar versões do compilador Solidity necessárias
python3 install_compilers.py
```

---

## ⚙️ Configuração

### **Editar `config.ini`**

```ini
[RPC]
# Polygon Mainnet RPC
# Opção 1: RPC público
url = https://polygon-rpc.com

# Opção 2: Alchemy (recomendado - mais confiável)
# url = https://polygon-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_API_KEY

# Opção 3: Infura
# url = https://polygon-mainnet.infura.io/v3/YOUR_INFURA_API_KEY

[BlockExplorer]
# PolygonScan API
api_key = YOUR_POLYGONSCAN_API_KEY
url = https://api.polygonscan.com/api

[CONTRACT_DIRECTORY]
# Caminho para os contratos do projeto neoflw-token
path = /Users/nettomello/CODIGOS/neoflw-token/contracts
```

**Obter API Keys:**

- **PolygonScan API:** https://polygonscan.com/myapikey
- **Alchemy API:** https://dashboard.alchemy.com/ (já configurado no projeto)

---

## 📊 Como Usar

### **1. Análise de Storage Layout**

```bash
cd SmartMuv
python3 -m smartmuv
```

**Selecionar contrato:**
- Adicionar endereço do contrato deployado
- Ou usar código-fonte local

**Resultado esperado:**

```
slot 0 - mapping balances[address] = uint256;
slot 1 - mapping allowed[address][address] = uint256;
slot 2 - uint256 totalSupply;
slot 3 - string name;
slot 4 - uint8 decimals;
slot 5 - string symbol;
```

### **2. Extrair Estado Completo**

**Para Token (NeoFlowToken):**

```bash
# Extrair lista de holders
# Verificar balances
# Validar totalSupply
```

**Resultado esperado:**

```
['totalSupply', 'uint256', 1000000000000000000000000000, 32, '0x2']
['decimals', 'uint8', 18, 1, '0x4']
['name', 'string', 'NEOFlowOFF', 32, '0x3']
['symbol', 'string', 'NEOFLW', 32, '0x5']
['balances:key:0x...', 'uint256', 1000000000000000000, 32, '0x...']
```

**Para Vault (StakingVault):**

```bash
# Extrair stakes ativos
# Verificar totalStakedAmount
# Validar totalRewardsReserved
```

**Para Claim (NeoFlowClaim):**

```bash
# Extrair whitelist
# Verificar tokens disponíveis
# Validar configurações
```

---

## 🎯 Casos de Uso no Projeto NEOFLW

### **1. Validação Pós-Deploy**

Após deploy e verificação no PolygonScan:

```bash
# Validar que o layout de storage está correto
# Verificar que não há conflitos de slots
# Confirmar que mappings estão mapeados corretamente
```

### **2. Auditoria de Dados**

```bash
# Extrair lista completa de holders
# Verificar integridade dos balances
# Validar que totalSupply está correto
```

### **3. Análise de Stakes**

```bash
# Listar todos os stakes ativos no Vault
# Verificar que totalStakedAmount está correto
# Validar que rewards estão calculados corretamente
```

### **4. Preparação para Migrações**

Se precisar migrar contratos no futuro:

```bash
# Extrair todos os dados necessários
# Preparar dados para novo contrato
# Validar que migração será possível
```

---

## 📝 Exemplo de Uso Completo

### **Analisar NeoFlowToken**

```bash
cd /Users/nettomello/CODIGOS/SmartMuv

# Editar smartmuv.py ou usar interface interativa
python3 -m smartmuv

# Selecionar contrato:
# 1. Adicionar endereço: 0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2
# 2. Ou usar código-fonte: /Users/nettomello/CODIGOS/neoflw-token/contracts/NeoFlowToken.sol

# Resultado:
# - Layout de storage
# - Lista de holders
# - Balances
# - Total supply
```

### **Analisar StakingVault**

```bash
# Endereço do Vault: 0x07E39107d4B35b64f9f2310B9A2B8e5262A4ee41

# Extrair:
# - Stakes ativos
# - totalStakedAmount
# - totalRewardsReserved
# - Mapeamento de stakes por endereço
```

### **Analisar NeoFlowClaim**

```bash
# Endereço do Claim: 0x407C037906d6441ECD4a3F9064eab2E6CF03b36b

# Extrair:
# - Whitelist completa
# - Tokens disponíveis para claim
# - Status de claims realizados
```

---

## ⚠️ Limitações e Observações

### **O que SmartMuv NÃO faz:**

- ❌ **Não verifica contratos** no PolygonScan/Etherscan
- ❌ **Não compara bytecode** compilado vs. deployado
- ❌ **Não valida código-fonte** automaticamente

### **O que SmartMuv FAZ:**

- ✅ **Analisa storage layout** (slots)
- ✅ **Extrai dados** de contratos deployados
- ✅ **Valida estrutura** de storage
- ✅ **Prepara migrações** de dados

### **Recomendação:**

Use SmartMuv **complementarmente** à verificação no PolygonScan:

1. **Verificar no PolygonScan** (validação de código-fonte)
2. **Analisar com SmartMuv** (validação de dados e storage)

---

## 🔧 Troubleshooting

### **Erro: "RPC connection failed"**

**Solução:**
- Verificar URL do RPC no `config.ini`
- Testar conexão: `curl https://polygon-rpc.com`
- Usar Alchemy ou Infura se RPC público falhar

### **Erro: "Contract not found"**

**Solução:**
- Verificar que o contrato está deployado
- Confirmar endereço no Polygonscan
- Verificar que está na rede correta (Polygon Mainnet)

### **Erro: "Solidity compiler not found"**

**Solução:**
```bash
# Reinstalar compiladores
python3 install_compilers.py
```

---

## 📚 Recursos Adicionais

- **Repositório:** https://github.com/mello-labs/SmartMuv
- **Documentação:** Ver README.md no repositório
- **Publicação:** Storage State Analysis and Extraction of Ethereum Blockchain Smart Contracts (TOSEM '23)

---

## ✅ Checklist de Validação

Após instalar e configurar SmartMuv:

- [ ] SmartMuv instalado e configurado
- [ ] RPC Polygon configurado no `config.ini`
- [ ] API PolygonScan configurada
- [ ] Layout de storage do Token analisado
- [ ] Layout de storage do Vault analisado
- [ ] Layout de storage do Claim analisado
- [ ] Dados extraídos e validados
- [ ] Documentação atualizada com resultados

---

**Última atualização:** 2025-01-XX

**Status:** ✅ Pronto para uso após deploy dos contratos

