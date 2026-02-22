# NEOFLW — Deployment Record
## Base Mainnet · Chain ID 8453

---

## Token

| Campo | Valor |
|-------|-------|
| Nome | NEOFlowOFF |
| Símbolo | NEOFLW |
| Endereço | `0x41F4ff3d45DED9C1332e4908F637B75fe83F5d6B` |
| Basescan | https://basescan.org/token/0x41f4ff3d45ded9c1332e4908f637b75fe83f5d6b |
| Owner | `0x470a8c640fFC2C16aEB6bE803a948420e2aE8456` (nsfactory.eth) |
| Total Supply (genesis) | 1.000 NEOFLW |
| MAX_SUPPLY | 1.000.000.000 NEOFLW (1 bilhão) |
| Decimals | 18 |

---

## Contrato

| Campo | Valor |
|-------|-------|
| Classe Solidity | `NeoTokenV2` |
| Template | NEO Smart Factory v0.5.3 — PROTOCOL \| TOKENIZE-SE |
| Compiler | v0.8.20+commit.a1b79de6 |
| Optimizer | 200 runs (?) / 1 run (verificado) |
| EVM Version | paris |
| OZ Version | v5.0.0 |
| Verificação | ✅ Exact Match — Basescan |

### Arquitetura
- `ERC20` — token padrão
- `ERC20Burnable` — burn público
- `ERC20Permit` — assinaturas gasless (EIP-2612), Account Abstraction ready
- `Ownable2Step` — transferência de ownership em dois passos (seguro)
- `publicMint` — 1 mint por wallet (anti-bot)
- `bridgeMinter` — role para multichain bridges
- `MAX_SUPPLY` — hard cap de 1B imutável

---

## Investigação 2026-02-22

**Contexto:** Verificação no Basescan mostrava "NeoTokenV2" — suspeitou-se de erro.

**Conclusão:** A verificação está CORRETA. O contrato deployado É o NeoTokenV2.

**Prova:**
- CBOR metadata do bytecode → Solidity 0.8.20 (confirma NeoTokenV2, não NeoFlowToken)
- `pendingOwner()` retorna → Ownable2Step presente ✅
- `permit()` reverts (exists, wrong args) → ERC20Permit presente ✅
- `owner()` → `0x470a8c640fFC2C16aEB6bE803a948420e2aE8456` (nsfactory.eth) ✅
- `totalSupply()` → 1.000 NEOFLW ✅

**O que é `NeoFlowToken.sol` local?**
O arquivo `contracts/NeoFlowToken.sol` neste repo é uma versão simplificada (ERC20 + Ownable v4 + ContractMetadata thirdweb) que **nunca foi deployada** neste endereço. O contrato real é o template NeoTokenV2 do NEO Smart Factory.

---

## Pool Uniswap V4

| Campo | Valor |
|-------|-------|
| Tx criação | `0xeb700565f74b510e5b713c7066b646033132c9552c8722130c14556b7e4b3d23` |
| Basescan | https://basescan.org/tx/0xeb700565f74b510e5b713c7066b646033132c9552c8722130c14556b7e4b3d23 |
| Liquidez atual | ~$0.79 (0.402 NEOFLW + ETH) |
| Status | ⚠️ Subcapitalizada — precisa de liquidez |

---

## Holders Notáveis

| Endereço | Participação | Nota |
|----------|-------------|------|
| nsfactory.eth | ~75% | Founder / NEO Protocol |
| inkpink.eth | ~25% | Co-holder |

---

## Próximos Passos

- [ ] Adicionar liquidez à pool Uniswap V4
- [ ] Definir estratégia de publicMint (MINT_PRICE / MINT_AMOUNT)
- [ ] Configurar bridgeMinter para expansão multichain
- [ ] Integração ceo-escalavel-miniapp ✅ (concluído 2026-02-22)
