#!/usr/bin/env python3
"""
Correção FINAL do Standard JSON para Sourcify:
1. Remove múltiplas licenças SPDX (deixa apenas uma)
2. Remove imports não resolvidos
3. Remove duplicações de IContractMetadata
4. Garante ordem correta
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "oklink_standard_json.json"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "sourcify_standard_json.json"

def fix_standard_json():
    """Correção final do Standard JSON"""
    
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {INPUT_FILE}")
    
    # Ler JSON original
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    content = data["sources"]["contracts/NeoFlowToken.sol"]["content"]
    
    # 1. Remover TODAS as declarações de licença SPDX exceto a primeira
    lines = content.split('\n')
    fixed_lines = []
    first_license_found = False
    
    for i, line in enumerate(lines):
        if "SPDX-License-Identifier" in line:
            if not first_license_found:
                fixed_lines.append(line)
                first_license_found = True
            # Remover todas as outras (incluindo duplicatas consecutivas)
        else:
            fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # Remover duplicatas consecutivas de licença (caso ainda existam)
    content = re.sub(r'(// SPDX-License-Identifier: MIT\n)+', r'// SPDX-License-Identifier: MIT\n', content)
    
    # 2. Remover import não resolvido de IContractMetadata
    content = content.replace('import "./interfaces/IContractMetadata.sol";', '')
    
    # 3. Remover duplicação de IContractMetadata
    # Encontrar todas as ocorrências de IContractMetadata
    icontract_pattern = r'// === Imported from \./interfaces/IContractMetadata\.sol ===.*?// === End of \./interfaces/IContractMetadata\.sol ==='
    
    matches = list(re.finditer(icontract_pattern, content, re.DOTALL))
    if len(matches) > 1:
        # Manter apenas a primeira ocorrência
        first_match = matches[0]
        for match in reversed(matches[1:]):  # Remover do final para o início
            content = content[:match.start()] + content[match.end():]
    
    # 4. Garantir que IContractMetadata está ANTES de ContractMetadata
    icontract_section = None
    contract_metadata_section = None
    
    # Encontrar IContractMetadata
    icontract_match = re.search(r'// === Imported from \./interfaces/IContractMetadata\.sol ===.*?// === End of \./interfaces/IContractMetadata\.sol ===', content, re.DOTALL)
    if icontract_match:
        icontract_section = icontract_match.group(0)
        content = content[:icontract_match.start()] + content[icontract_match.end():]
    
    # Encontrar ContractMetadata
    contract_metadata_match = re.search(r'// === Imported from \./ContractMetadata\.sol ===.*?// === End of \./ContractMetadata\.sol ===', content, re.DOTALL)
    if contract_metadata_match:
        contract_metadata_section = contract_metadata_match.group(0)
        content = content[:contract_metadata_match.start()] + content[contract_metadata_match.end():]
    
    # Reinserir na ordem correta (IContractMetadata antes de ContractMetadata)
    if icontract_section and contract_metadata_section:
        # Encontrar onde inserir (antes do Ownable terminar)
        ownable_end = content.find("// === End of @openzeppelin/contracts/access/Ownable.sol ===")
        if ownable_end != -1:
            insert_pos = ownable_end + len("// === End of @openzeppelin/contracts/access/Ownable.sol ===")
            content = (
                content[:insert_pos] + 
                "\n\n" + 
                icontract_section + 
                "\n\n" + 
                contract_metadata_section + 
                "\n\n" + 
                content[insert_pos:]
            )
    
    # 5. Garantir que há apenas uma licença no topo
    if not content.strip().startswith("// SPDX-License-Identifier"):
        content = "// SPDX-License-Identifier: MIT\n" + content
    
    # 6. Remover linhas vazias excessivas
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 7. Atualizar JSON
    data["sources"]["contracts/NeoFlowToken.sol"]["content"] = content
    
    # 8. Salvar
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Verificações finais
    spdx_count = content.count("SPDX-License-Identifier")
    import_count = content.count('import "./interfaces/IContractMetadata.sol";')
    icontract_count = content.count("// === Imported from ./interfaces/IContractMetadata.sol ===")
    
    print("=" * 60)
    print("✅ Standard JSON CORRIGIDO para Sourcify!")
    print("=" * 60)
    print()
    print(f"📁 Arquivo: {OUTPUT_FILE}")
    print()
    print("✅ Verificações:")
    print(f"   Licenças SPDX: {spdx_count} (deve ser 1)")
    print(f"   Imports não resolvidos: {import_count} (deve ser 0)")
    print(f"   IContractMetadata: {icontract_count} (deve ser 1)")
    print()
    print("💡 Use este arquivo no Sourcify:")
    print(f"   {OUTPUT_FILE}")
    print()

if __name__ == "__main__":
    fix_standard_json()
