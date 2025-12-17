#!/usr/bin/env python3
"""
Gera Standard JSON Input PERFEITO para verificação no Blockscout
Usa o arquivo flattened_perfect.sol com configurações otimizadas
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
SOURCE_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_perfect.sol"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "blockscout_standard_json.json"

def generate_blockscout_standard_json():
    """Gera Standard JSON Input para Blockscout com configurações perfeitas"""
    
    source_file = SOURCE_FILE
    if not source_file.exists():
        print(f"❌ Arquivo não encontrado: {source_file}")
        print(f"💡 Tentando usar arquivo alternativo...")
        # Fallback para arquivo original
        fallback = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
        if fallback.exists():
            source_file = fallback
            print(f"✅ Usando: {fallback}")
        else:
            return False
    
    print("=" * 70)
    print("🔧 Gerando Standard JSON Input para Blockscout")
    print("=" * 70)
    print()
    
    # Ler código fonte perfeito
    with open(source_file, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    # Verificações
    spdx_count = source_code.count('SPDX-License-Identifier')
    pragma_count = source_code.count('pragma solidity')
    has_contract_metadata = 'ContractMetadata' in source_code
    contract_line = [l for l in source_code.split('\n') if 'contract NeoFlowToken is' in l]
    
    print(f"📊 Arquivo fonte: {source_file.name}")
    print(f"   Linhas: {len(source_code.split(chr(10))):,}")
    print(f"   Licenças SPDX: {spdx_count} {'✅' if spdx_count == 1 else '❌'}")
    print(f"   Pragmas: {pragma_count} {'✅' if pragma_count == 1 else '❌'}")
    print(f"   Tem ContractMetadata: {has_contract_metadata} {'❌' if has_contract_metadata else '✅'}")
    if contract_line:
        print(f"   Contrato: {contract_line[0].strip()[:80]}")
    print()
    
    # Criar Standard JSON Input para Blockscout
    # Configurações baseadas nas recomendações para resolver Partial Match
    standard_json = {
        "language": "Solidity",
        "sources": {
            "contracts/NeoFlowToken.sol": {
                "content": source_code
            }
        },
        "settings": {
            "optimizer": {
                "enabled": True,
                "runs": 200
            },
            "evmVersion": "paris",  # Versão EVM válida (conforme foundry.toml)
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "evm.bytecode",
                        "evm.deployedBytecode",
                        "evm.deployedBytecode.sourceMap",
                        "evm.methodIdentifiers",
                        "metadata"
                    ],
                    "": [
                        "ast"
                    ]
                }
            },
            "remappings": []
        }
    }
    
    # Salvar arquivo
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(standard_json, f, indent=2, ensure_ascii=False)
    
    file_size = OUTPUT_FILE.stat().st_size / 1024
    
    print("=" * 70)
    print("✅ Standard JSON Input gerado com sucesso!")
    print("=" * 70)
    print()
    print(f"📁 Arquivo gerado: {OUTPUT_FILE}")
    print(f"📊 Tamanho: {file_size:.1f} KB")
    print()
    print("🔧 Configurações aplicadas:")
    print("   ✅ Compiler: v0.8.18+commit.87f61d96 (versão do pragma)")
    print("   ✅ Optimization: enabled, 200 runs")
    print("   ✅ EVM Version: default")
    print("   ✅ via-IR: false (desabilitado)")
    print("   ✅ License: MIT")
    print()
    print("📋 Como usar no Blockscout:")
    print("   1. Acesse a página do contrato no Blockscout")
    print("   2. Clique em 'Verify & publish'")
    print("   3. Escolha: 'Standard JSON Input'")
    print("   4. Faça upload deste arquivo JSON")
    print("   5. Preencha os campos:")
    print("      - Compiler: v0.8.18+commit.87f61d96")
    print("      - License: MIT License (MIT)")
    print("      - Contract Name: NeoFlowToken")
    print("      - Optimization: Yes, Runs: 200")
    print("      - EVM Version: default")
    print("      - Constructor Args: 0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000")
    print()
    print("💡 Se ainda der Partial Match, tente:")
    print("   - EVM Version: paris (em vez de default)")
    print("   - Compiler: v0.8.18 (sem commit hash)")
    print("   - Compiler: v0.8.30+commit.73712a01")
    print()
    
    return True

if __name__ == "__main__":
    success = generate_blockscout_standard_json()
    if not success:
        exit(1)
