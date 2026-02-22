# NEOFLW — Token Listing Submissions
## Dados prontos para submissão em todos os portais

---

## Dados do Token

```
Nome:        NEOFlowOFF
Símbolo:     NEOFLW
Endereço:    0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B
Chain:       Base (Chain ID: 8453)
Decimals:    18
MAX_SUPPLY:  1.000.000.000 NEOFLW
Website:     https://flowoff.xyz
Email:       flowoff.mkt@gmail.com
GitHub:      https://github.com/NEO-FlowOFF
Miniapp:     https://agenteflow.vercel.app
Logo local:  public/images/avatar_neoflow.png (256x256 PNG)
Logo IPFS:   ipfs://QmVMuP3WLuKkWjrPFT4WnQSfkRQfbNppAVkgi9aSQvtrBo
Basescan:    https://basescan.org/token/0x41f4ff3d45ded9c1332e4908f637b75fe83f5d6b
```

**Descrição curta (EN):**
> NEOFlowOFF (NEOFLW) is the native token of the NEO Protocol ecosystem on Base. ERC20 with gasless transactions (ERC20Permit), burn mechanism, and public mint. Powered by NEO Smart Factory.

**Descrição curta (PT):**
> NEOFlowOFF (NEOFLW) é o token nativo do ecossistema NEO Protocol na Base. ERC20 com transações gasless (ERC20Permit), mecanismo de queima e mint público. Powered by NEO Smart Factory.

---

## 1. Basescan Token Info Update

**URL:** https://basescan.org/token/0x41f4ff3d45ded9c1332e4908f637b75fe83f5d6b#comments

Ou direto: https://etherscan.io/tokenupdate?t=0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B&c=8453

**Campos:**
- Project Name: NEOFlowOFF
- Logo: upload `avatar_neoflow.png` (256x256)
- Website: https://flowoff.xyz
- Email: flowoff.mkt@gmail.com
- Description: NEOFlowOFF (NEOFLW) is the native token of the NEO Protocol ecosystem...
- GitHub: https://github.com/NEO-FlowOFF

---

## 2. DexScreener

**URL:** https://dexscreener.com/update-token-info

**Chain:** Base
**Contract:** 0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B

**Campos:**
- Logo: upload `avatar_neoflow.png`
- Header Image: (opcional — criar banner 1200x400)
- Description: NEOFlowOFF (NEOFLW) is the native token of the NEO Protocol ecosystem on Base.
- Website: https://flowoff.xyz
- GitHub: https://github.com/NEO-FlowOFF
- Miniapp: https://agenteflow.vercel.app

**Nota:** DexScreener exige pelo menos alguma liquidez na pool antes de aceitar a submissão. ⚠️ Adicionar liquidez primeiro.

---

## 3. GeckoTerminal / CoinGecko

**URL:** https://www.geckoterminal.com/
Pool estará visível automaticamente após liquidez ser adicionada.

Para info adicional: https://www.coingecko.com/en/coins/new

---

## 4. Uniswap Token List

**Entry JSON** (para adicionar ao token list):

```json
{
  "chainId": 8453,
  "address": "0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B",
  "name": "NEOFlowOFF",
  "symbol": "NEOFLW",
  "decimals": 18,
  "logoURI": "ipfs://QmVMuP3WLuKkWjrPFT4WnQSfkRQfbNppAVkgi9aSQvtrBo"
}
```

**PR Target:** https://github.com/Uniswap/default-token-list
Ou token list própria hosteada em: https://flowoff.xyz/neoflw-token-list.json

---

## 5. Ordem de Execução Recomendada

1. ✅ Verificação no Basescan — já está (NeoTokenV2 Exact Match)
2. ⬜ **Adicionar liquidez** na pool Uniswap V4 (wallet nsfactory.eth)
3. ⬜ Submeter info na **Basescan** (logo + website)
4. ⬜ Submeter no **DexScreener** (após liquidez)
5. ⬜ **GeckoTerminal** — aparece automático após liquidez; submeter info
6. ⬜ **Uniswap token list** — PR ou lista própria
