#!/usr/bin/env python3
"""
Corrige Standard JSON para Sourcify:
1. Remove múltiplas licenças SPDX
2. Resolve imports não resolvidos (IContractMetadata)
3. Garante ordem correta (IContractMetadata antes de ContractMetadata)
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "oklink_standard_json.json"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "verification" / "sourcify_standard_json.json"

# Conteúdo de IContractMetadata (sem licença duplicada)
ICONTRACT_METADATA_CONTENT = """/**
 * @dev Interface mínima de metadata de contrato compatível com thirdweb.
 * Mantém a mesma assinatura usada em `ContractMetadata.sol`.
 */
interface IContractMetadata {
    /// @notice Retorna a URI de metadata do contrato.
    function contractURI() external view returns (string memory);

    /**
     * @notice Define a URI de metadata do contrato.
     * @param _uri Nova URI.
     */
    function setContractURI(string memory _uri) external;

    /// @dev Emitido quando a URI de metadata do contrato é atualizada.
    event ContractURIUpdated(string prevURI, string newURI);
}
"""

def fix_standard_json():
    """Corrige o Standard JSON para Sourcify"""
    
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {INPUT_FILE}")
    
    # Ler JSON original
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Obter conteúdo do contrato
    contract_content = data["sources"]["contracts/NeoFlowToken.sol"]["content"]
    
    # 1. Remover todas as declarações de licença SPDX exceto a primeira
    lines = contract_content.split('\n')
    fixed_lines = []
    first_license_found = False
    
    for line in lines:
        if "SPDX-License-Identifier" in line:
            if not first_license_found:
                fixed_lines.append(line)
                first_license_found = True
            # Remover todas as outras
        else:
            fixed_lines.append(line)
    
    contract_content = '\n'.join(fixed_lines)
    
    # 2. Resolver import de IContractMetadata
    # Encontrar onde está o ContractMetadata
    contract_metadata_start = contract_content.find("// === Imported from ./ContractMetadata.sol ===")
    
    if contract_metadata_start != -1:
        # Encontrar onde está o import problemático
        contract_metadata_section = contract_content[contract_metadata_start:]
        contract_metadata_end = contract_metadata_section.find("// === End of ./ContractMetadata.sol ===")
        
        if contract_metadata_end != -1:
            contract_metadata_full = contract_metadata_section[:contract_metadata_end]
            
            # Substituir o import pelo conteúdo inline
            if 'import "./interfaces/IContractMetadata.sol";' in contract_metadata_full:
                # Remover o import
                contract_metadata_fixed = contract_metadata_full.replace(
                    'import "./interfaces/IContractMetadata.sol";',
                    ''
                )
                
                # Adicionar IContractMetadata antes do ContractMetadata
                # Encontrar onde inserir
                before_contract_metadata = contract_content[:contract_metadata_start]
                after_contract_metadata = contract_content[contract_metadata_start + len(contract_metadata_full):]
                
                # Inserir IContractMetadata antes
                icontract_metadata_section = f"""// === Imported from ./interfaces/IContractMetadata.sol ===

pragma solidity ^0.8.18;

{ICONTRACT_METADATA_CONTENT}

// === End of ./interfaces/IContractMetadata.sol ===


"""
                
                # Reconstruir conteúdo
                contract_content = (
                    before_contract_metadata +
                    icontract_metadata_section +
                    "// === Imported from ./ContractMetadata.sol ===\n\n" +
                    contract_metadata_fixed +
                    after_contract_metadata
                )
    
    # 3. Garantir que há apenas uma licença no topo
    if not contract_content.strip().startswith("// SPDX-License-Identifier"):
        contract_content = "// SPDX-License-Identifier: MIT\n" + contract_content
    
    # 4. Remover todas as outras declarações de licença
    lines = contract_content.split('\n')
    final_lines = []
    seen_spdx = False
    
    for line in lines:
        if "SPDX-License-Identifier" in line:
            if not seen_spdx:
                final_lines.append(line)
                seen_spdx = True
        else:
            final_lines.append(line)
    
    contract_content = '\n'.join(final_lines)
    
    # 5. Atualizar JSON
    data["sources"]["contracts/NeoFlowToken.sol"]["content"] = contract_content
    
    # 6. Salvar arquivo corrigido
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("=" * 60)
    print("✅ Standard JSON corrigido para Sourcify!")
    print("=" * 60)
    print()
    print(f"📁 Arquivo original: {INPUT_FILE}")
    print(f"📁 Arquivo corrigido: {OUTPUT_FILE}")
    print()
    print("🔧 Correções aplicadas:")
    print("   ✅ Múltiplas licenças SPDX removidas (mantida apenas uma)")
    print("   ✅ Import de IContractMetadata resolvido")
    print("   ✅ Ordem correta: IContractMetadata antes de ContractMetadata")
    print()
    print("💡 Use este arquivo no Sourcify:")
    print(f"   {OUTPUT_FILE}")
    print()

if __name__ == "__main__":
    fix_standard_json()
