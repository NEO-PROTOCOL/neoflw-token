# 🌐 Deploy em Múltiplas Redes

> **Importante:** Este projeto pode ter deploys em múltiplas redes blockchain. **NÃO misturar configurações, endereços ou informações entre redes diferentes.**

---

## 📋 Redes Suportadas

### **1. Polygon Mainnet** (Principal) ✅

- **Chain ID:** 137
- **RPC:** `https://polygon-mainnet.g.alchemy.com/v2/YOUR_KEY`
- **Explorer:** https://polygonscan.com
- **Status:** Rede principal do projeto
- **Configuração:** `APE_NETWORK=polygon:mainnet`

**Endereços (preencher após deploy):**
```env
TOKEN_ADDRESS=
VAULT_ADDRESS=
CLAIM_ADDRESS=
GOVERNOR_ADDRESS=
GAMIFICATION_ADDRESS=
```

---

### **2. BASE** (Opcional) 📋

- **Chain ID:** 8453
- **RPC:** `https://base-mainnet.g.alchemy.com/v2/YOUR_KEY`
- **Explorer:** https://basescan.org
- **Status:** Deploy opcional/separado
- **Configuração:** `APE_NETWORK=base:mainnet`

**⚠️ ATENÇÃO:**
- Deploys em BASE são **separados** dos deploys em Polygon
- Endereços de contratos são **diferentes** em cada rede
- Não misturar endereços ou configurações entre redes
- Verificação deve ser feita separadamente em cada rede

---

## 🔧 Configuração por Rede

### **Polygon Mainnet (.env)**

```env
# Network padrão
APE_NETWORK=polygon:mainnet

# Alchemy RPC (Polygon)
ALCHEMY_API_KEY=your-polygon-alchemy-key

# PolygonScan API
POLYGONSCAN_API_KEY=your-polygonscan-key

# Endereços Polygon
TOKEN_ADDRESS=0x... (Polygon)
VAULT_ADDRESS=0x... (Polygon)
```

### **BASE Mainnet (.env.base)**

```env
# Network BASE
APE_NETWORK=base:mainnet

# Alchemy RPC (BASE)
ALCHEMY_API_KEY_BASE=your-base-alchemy-key

# BaseScan API
BASESCAN_API_KEY=your-basescan-key

# Endereços BASE
TOKEN_ADDRESS_BASE=0x... (BASE)
VAULT_ADDRESS_BASE=0x... (BASE)
```

---

## ⚠️ Regras Importantes

### **1. Não Misturar Endereços**

❌ **ERRADO:**
```env
# Misturando endereços de redes diferentes
TOKEN_ADDRESS=0x... (Polygon)
VAULT_ADDRESS=0x... (BASE)  # ❌ ERRO!
```

✅ **CORRETO:**
```env
# Polygon
TOKEN_ADDRESS_POLYGON=0x... (Polygon)
VAULT_ADDRESS_POLYGON=0x... (Polygon)

# BASE
TOKEN_ADDRESS_BASE=0x... (BASE)
VAULT_ADDRESS_BASE=0x... (BASE)
```

### **2. Verificação Separada**

Cada rede precisa de verificação separada:

```bash
# Verificar em Polygon
ape etherscan verify NeoFlowToken --network polygon:mainnet

# Verificar em BASE (se deployado)
ape etherscan verify NeoFlowToken --network base:mainnet
```

### **3. Análise de Bytecode**

- Bytecode decompilado de BASE **não se aplica** a Polygon
- Cada rede tem seu próprio bytecode
- Não usar informações de uma rede na outra

---

## 📝 Documentação por Rede

### **Polygon Mainnet:**
- ✅ Documentação principal do projeto
- ✅ `docs/deploy/MIGRACAO_POLYGON.md`
- ✅ `docs/STATUS_ATUAL_DEPLOY.md`
- ✅ `docs/PROXIMOS_PASSOS_AGORA.md`

### **BASE Mainnet:**
- 📋 Documentação separada (se necessário)
- 📋 Endereços separados
- 📋 Configurações separadas

---

## 🎯 Checklist por Rede

### **Polygon Mainnet:**
- [ ] Deploy dos contratos
- [ ] Verificação no PolygonScan
- [ ] Configuração de whitelist
- [ ] Transferência de tokens
- [ ] Testes end-to-end

### **BASE Mainnet (se aplicável):**
- [ ] Deploy dos contratos
- [ ] Verificação no BaseScan
- [ ] Configuração de whitelist
- [ ] Transferência de tokens
- [ ] Testes end-to-end

---

## 💡 Boas Práticas

1. **Usar variáveis de ambiente separadas:**
   ```env
   # Prefixar com nome da rede
   POLYGON_TOKEN_ADDRESS=0x...
   BASE_TOKEN_ADDRESS=0x...
   ```

2. **Documentar endereços por rede:**
   - Criar arquivo `docs/ENDERECOS_POLYGON.md`
   - Criar arquivo `docs/ENDERECOS_BASE.md` (se necessário)

3. **Scripts separados:**
   - `scripts/deploy/deploy_polygon.py`
   - `scripts/deploy/deploy_base.py` (se necessário)

4. **Não misturar:**
   - ❌ Endereços de contratos
   - ❌ Configurações de rede
   - ❌ Bytecode ou análises
   - ❌ Documentação de verificação

---

## 📚 Referências

- **Polygon Docs:** https://docs.polygon.technology/
- **BASE Docs:** https://docs.base.org/
- **PolygonScan:** https://polygonscan.com
- **BaseScan:** https://basescan.org

---

**Última atualização:** 2025-01-XX

**Status:** 📋 Documentação de múltiplas redes

