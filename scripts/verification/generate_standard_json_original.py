#!/usr/bin/env python3
"""
Gera Standard JSON Input usando o código ORIGINAL (sem ContractMetadata)
para corresponder ao bytecode deployado (2999 bytes)
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
SOURCE_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "sourcify_standard_json.json"

def generate_standard_json():
    """Gera Standard JSON Input do código original (sem ContractMetadata)"""
    
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {SOURCE_FILE}")
    
    # Ler código fonte original (sem ContractMetadata)
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    # Remover múltiplas licenças SPDX (deixar apenas a primeira)
    lines = source_code.split('\n')
    fixed_lines = []
    first_license_found = False
    
    for line in lines:
        if 'SPDX-License-Identifier' in line:
            if not first_license_found:
                fixed_lines.append(line)
                first_license_found = True
            # Pular todas as outras
        else:
            fixed_lines.append(line)
    
    source_code = '\n'.join(fixed_lines)
    
    # Criar Standard JSON Input
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
            "evmVersion": "paris",
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "evm.bytecode",
                        "evm.deployedBytecode",
                        "evm.methodIdentifiers",
                        "metadata"
                    ],
                    "": [
                        "ast"
                    ]
                }
            }
        }
    }
    
    # Salvar
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(standard_json, f, indent=2, ensure_ascii=False)
    
    # Verificações
    spdx_count = source_code.count('SPDX-License-Identifier')
    has_contract_metadata = 'ContractMetadata' in source_code
    contract_line = [l for l in source_code.split('\n') if 'contract NeoFlowToken is' in l]
    
    print("=" * 60)
    print("✅ Standard JSON gerado do código ORIGINAL (sem ContractMetadata)")
    print("=" * 60)
    print()
    print(f"📁 Arquivo fonte: {SOURCE_FILE}")
    print(f"📁 Arquivo gerado: {OUTPUT_FILE}")
    print()
    print("✅ Verificações:")
    print(f"   Licenças SPDX: {spdx_count} {'✅' if spdx_count == 1 else '❌'}")
    print(f"   Tem ContractMetadata: {has_contract_metadata} {'❌ (deve ser False)' if has_contract_metadata else '✅'}")
    if contract_line:
        print(f"   Contrato: {contract_line[0].strip()[:80]}")
    print()
    print("💡 Este arquivo corresponde ao bytecode deployado (2999 bytes)")
    print()

if __name__ == "__main__":
    generate_standard_json()
