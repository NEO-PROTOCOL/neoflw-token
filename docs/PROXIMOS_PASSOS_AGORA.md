# 🚀 Próximos Passos - Ação Imediata

## ✅ Status Atual (Verificado)

- ✅ **API Alchemy:** Funcionando
- ✅ **Wallet:** `neoflow-admin` configurada (`0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`)
- ✅ **Network:** `polygon:mainnet` configurado
- ✅ **Contratos:** Todos implementados e testados
- ✅ **Frontend:** Completo e configurado

---

## 🎯 PRÓXIMOS PASSOS (Ordem de Execução)

### **1️⃣ VERIFICAR SALDO DE MATIC** ⚠️ CRÍTICO

```bash
# Verificar saldo da wallet
ape accounts show neoflow-admin --network polygon:mainnet

# OU verificar no Polygonscan:
# https://polygonscan.com/address/0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60
```

**Precisa:**

- **Mínimo:** ~50 MATIC para deploy básico
- **Recomendado:** ~100 MATIC para deploy completo + verificações
- **Custo:** ~$30-60 USD

**Se não tiver MATIC:**

1. Comprar em exchange (Binance, Coinbase, etc)
2. Fazer bridge de Ethereum → Polygon: https://portal.polygon.technology/polygon/bridge
3. Transferir para a wallet `0x460F9D0cf3e6E84faC1A7Abc524ddfa66fb64f60`

---

### **2️⃣ COMPILAR CONTRATOS**

```bash
cd /Users/nettomello/CODIGOS/TOKENS/neoflw-token
npm run compile
```

**Verificar:**

- ✅ Sem erros de compilação
- ✅ Todos os contratos compilados

---

### **3️⃣ DEPLOY TOKEN (Primeiro Contrato)**

```bash
ape run scripts/deploy_token.py --network polygon:mainnet
```

**Após deploy:**

1. **Anotar endereço do Token** (será exibido no terminal)
2. **Atualizar `frontend/.env`:**
   ```env
   NEXT_PUBLIC_TOKEN_ADDRESS=0x... (endereço do token)
   ```

**Verificar no Polygonscan:**

- Acessar: `https://polygonscan.com/address/[ENDERECO_TOKEN]`
- Confirmar que o contrato foi deployado

---

### **4️⃣ DEPLOY STAKING VAULT**

```bash
ape run scripts/deploy_vault.py --network polygon:mainnet
```

**Após deploy:**

1. **Anotar endereço do Vault**
2. **Atualizar `frontend/.env`:**
   ```env
   NEXT_PUBLIC_VAULT_ADDRESS=0x... (endereço do vault)
   ```

---

### **5️⃣ DEPLOY CLAIM**

```bash
ape run scripts/deploy_claim.py --network polygon:mainnet
```

**Após deploy:**

1. **Anotar endereço do Claim**
2. **Atualizar `frontend/.env`:**
   ```env
   NEXT_PUBLIC_CLAIM_ADDRESS=0x... (endereço do claim)
   ```

---

### **6️⃣ DEPLOY GAMIFICAÇÃO (Opcional mas Recomendado)**

```bash
ape run scripts/deploy_gamification.py --network polygon:mainnet
```

**Após deploy:**

1. **Anotar endereço do GamificationController**
2. **Atualizar `frontend/.env`:**
   ```env
   NEXT_PUBLIC_GAMIFICATION_ADDRESS=0x... (endereço da gamificação)
   ```

---

### **7️⃣ VERIFICAR CONTRATOS NO POLYGONSCAN**

Para cada contrato deployado:

1. Acessar: `https://polygonscan.com/address/[ENDERECO]`
2. Clicar em **"Contract"** → **"Verify and Publish"**
3. Escolher **"Via Standard JSON Input"**
4. Upload do arquivo: `sourcify_standard_json.json`
5. Preencher **Constructor Arguments** (se solicitado)
6. Confirmar verificação

**Contratos para verificar:**

- ✅ Token
- ✅ StakingVault
- ✅ NeoFlowClaim
- ✅ GamificationController (se deployado)

---

### **7️⃣.5️⃣ VALIDAR E ANALISAR CONTRATOS COM SMARTMUV** 🔍

**SmartMuv** é uma ferramenta de análise de storage layout e extração de dados de contratos EVM. Útil para validação pós-deploy.

#### **7.5.1. Instalar SmartMuv**

```bash
# Clonar repositório
cd /Users/nettomello/CODIGOS
git clone https://github.com/mello-labs/SmartMuv.git
cd SmartMuv

# Instalar dependências
python3 setup.py install

# Instalar compiladores Solidity
python3 install_compilers.py
```

#### **7.5.2. Configurar SmartMuv**

Editar `config.ini` com:

```ini
[RPC]
# Polygon Mainnet RPC
url = https://polygon-rpc.com
# OU usar Alchemy
# url = https://polygon-mainnet.g.alchemy.com/v2/YOUR_API_KEY

[BlockExplorer]
# PolygonScan API
api_key = YOUR_POLYGONSCAN_API_KEY
url = https://api.polygonscan.com/api

[CONTRACT_DIRECTORY]
# Caminho para contratos do projeto
path = /Users/nettomello/CODIGOS/neoflw-token/contracts
```

#### **7.5.3. Analisar Layout de Storage**

```bash
# Analisar layout de storage do Token
python3 smartmuv.py

# Selecionar contrato NeoFlowToken
# Verificar slots de variáveis de estado
```

**O que validar:**

- ✅ Slots de variáveis de estado estão corretos
- ✅ Mappings estão mapeados corretamente
- ✅ Estruturas (structs) estão alocadas corretamente
- ✅ Não há conflitos de slots

#### **7.5.4. Extrair Dados dos Contratos Deployados**

```bash
# Extrair estado completo do Token
# Listar todos os holders
# Verificar balances
# Extrair dados do Vault (stakes)
# Extrair whitelist do Claim
```

**Dados úteis para extrair:**

- 📊 **Token:** Lista de holders, balances, totalSupply
- 📊 **Vault:** Stakes ativos, rewards reservados, totalStakedAmount
- 📊 **Claim:** Whitelist, tokens disponíveis para claim

#### **7.5.5. Criar Script de Análise Automatizada**

```bash
# Criar script para análise automática de todos os contratos
# Validar integridade dos dados
# Comparar estado esperado vs. real
```

**Benefícios:**

- ✅ Validação de integridade dos dados
- ✅ Auditoria de storage layout
- ✅ Preparação para migrações futuras
- ✅ Documentação do estado dos contratos

**Nota:** SmartMuv é complementar à verificação no PolygonScan. Use para validação e análise, não substitui verificação em exploradores.

---

### **8️⃣ CONFIGURAR WHITELIST E DISTRIBUIÇÃO**

#### **8.1. Transferir Tokens para StakingVault (Rewards)**

```bash
# Via Ape console ou script
# Transferir tokens para o Vault para pagar rewards
```

#### **8.2. Configurar Whitelist no Claim**

```bash
# Usar script ou console Ape
# Configurar endereços elegíveis no NeoFlowClaim
```

#### **8.3. Transferir Tokens para GamificationController (se deployado)**

```bash
# Transferir tokens para pagar rewards de quests
```

---

### **9️⃣ BUILD E DEPLOY FRONTEND**

#### **9.1. Build do Frontend**

```bash
cd frontend
npm run build
```

**Verificar:**
- ✅ Build sem erros
- ✅ Pasta `.next/out/` criada

#### **9.2. Deploy em IPFS**

**Opção A: Pinata**
1. Criar conta: https://pinata.cloud
2. Upload da pasta `.next/out/`
3. Anotar CID/IPFS hash

**Opção B: Lighthouse Storage**
1. Criar conta: https://lighthouse.storage
2. Upload da pasta `.next/out/`
3. Anotar CID/IPFS hash

**Opção C: Fleek**
1. Criar conta: https://fleek.co
2. Conectar repositório GitHub
3. Deploy automático

---

### **🔟 CONFIGURAR ENS DOMAIN**

1. Acessar: https://app.ens.domains
2. Conectar wallet que controla `neoflowoff.eth`
3. Ir em **"My Account"** → `neoflowoff.eth`
4. Em **"Content Hash"**, adicionar:
   - Tipo: **IPFS**
   - Hash: `Qm...` (CID do IPFS do passo 9)
5. Confirmar transação

**Testar:**
- Acessar: `https://neoflowoff.eth` (deve carregar o frontend)

---

### **1️⃣1️⃣ INTEGRAR NO flowoff.xyz**

Adicionar no site da agência:

```html
<!-- Botão Launch APP -->
<a href="https://neoflowoff.eth" class="launch-app-btn">
  🚀 Launch APP
</a>

<!-- Seção Partner -->
<section class="partners">
  <div class="partner-card">
    <h3>NEOFLW Protocol</h3>
    <p>Token oficial do protocolo NEOFLW</p>
    <a href="https://neoflowoff.eth">Acessar DApp</a>
  </div>
</section>
```

---

## 📋 CHECKLIST RESUMIDO

### **Fase 1: Preparação**
- [ ] Verificar saldo POL (mínimo 50 POL)
- [ ] Obter POL se necessário (ou migrar MATIC → POL)
- [ ] Compilar contratos (`npm run compile`)

### **Fase 2: Deploy Contratos**
- [ ] Deploy Token
- [ ] Anotar endereço Token
- [ ] Deploy StakingVault
- [ ] Anotar endereço Vault
- [ ] Deploy NeoFlowClaim
- [ ] Anotar endereço Claim
- [ ] Deploy GamificationController (opcional)
- [ ] Anotar endereço Gamification

### **Fase 3: Configuração**
- [ ] Atualizar `frontend/.env` com todos os endereços
- [ ] Verificar contratos no Polygonscan
- [ ] **Instalar e configurar SmartMuv** (validação pós-deploy)
- [ ] **Analisar layout de storage dos contratos**
- [ ] **Extrair dados dos contratos deployados**
- [ ] Configurar whitelist no Claim
- [ ] Transferir tokens para Vault (rewards)
- [ ] Transferir tokens para Gamification (se deployado)

### **Fase 4: Frontend e Deploy**
- [ ] Build do frontend (`npm run build`)
- [ ] Deploy em IPFS
- [ ] Anotar CID/IPFS hash
- [ ] Configurar ENS domain
- [ ] Testar acesso via `neoflowoff.eth`

### **Fase 5: Integração**
- [ ] Adicionar botão Launch APP no flowoff.xyz
- [ ] Criar seção Partner
- [ ] Testar fluxo completo end-to-end

---

## ⏱️ Tempo Estimado

| Fase | Tempo |
|------|-------|
| **Preparação** | 15-30 min |
| **Deploy Contratos** | 1-2 horas |
| **Configuração** | 30-60 min |
| **Validação SmartMuv** | 30-45 min |
| **Frontend/IPFS** | 1-2 horas |
| **Integração** | 30 min |
| **TOTAL** | **4-6 horas** |

---

## 💰 Custos Estimados

| Item | Custo |
|------|-------|
| **POL para Deploy** | $30-60 USD |
| **IPFS Deploy** | Grátis |
| **ENS Config** | $5-10 USD |
| **TOTAL** | **$35-70 USD** |

---

## 🚨 IMPORTANTE

### **Antes de Começar:**
1. ✅ Verificar que tem MATIC suficiente
2. ✅ Backup de todas as chaves privadas
3. ✅ Anotar todos os endereços em local seguro
4. ✅ Ter acesso ao Polygonscan para verificação

### **Durante o Deploy:**
- ⚠️ **NÃO FECHE O TERMINAL** durante os deploys
- ⚠️ **ANOTE TODOS OS ENDEREÇOS** imediatamente
- ⚠️ **VERIFIQUE CADA CONTRATO** no Polygonscan antes de continuar

### **Após o Deploy:**
- ✅ Verificar todos os contratos no Polygonscan
- ✅ Testar todas as funcionalidades
- ✅ Atualizar documentação com endereços finais

---

## 🎯 COMANDOS RÁPIDOS

```bash
# 1. Verificar saldo
ape accounts show neoflow-admin --network polygon:mainnet

# 2. Compilar
npm run compile

# 3. Deploy Token
ape run scripts/deploy_token.py --network polygon:mainnet

# 4. Deploy Vault
ape run scripts/deploy_vault.py --network polygon:mainnet

# 5. Deploy Claim
ape run scripts/deploy_claim.py --network polygon:mainnet

# 6. Deploy Gamification (opcional)
ape run scripts/deploy_gamification.py --network polygon:mainnet

# 7. Build Frontend
cd frontend && npm run build
```

---

## 📚 Documentação Relacionada

- **Guia Completo:** [`CONFIGURACAO_COMPLETA_TOKEN.md`](../CONFIGURACAO_COMPLETA_TOKEN.md)
- **Resumo Rápido:** [`RESUMO_CONFIGURACAO.md`](../RESUMO_CONFIGURACAO.md)
- **Migração Polygon:** [`deploy/MIGRACAO_POLYGON.md`](../deploy/MIGRACAO_POLYGON.md)
- **SmartMuv Validação:** [`SMARTMUV_VALIDACAO.md`](../SMARTMUV_VALIDACAO.md)

---

**🚀 Comece pelo Passo 1 e siga em ordem!**

