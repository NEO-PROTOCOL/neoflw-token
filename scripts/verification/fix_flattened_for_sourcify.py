#!/usr/bin/env python3
"""
Corrige arquivo flattened para Sourcify:
1. Remove múltiplas declarações de licença SPDX (deixa apenas uma no topo)
2. Resolve imports não resolvidos (IContractMetadata e ContractMetadata)
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened.sol"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_sourcify.sol"

# Conteúdo de IContractMetadata
ICONTRACT_METADATA = """// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.18;

/**
 * @dev Interface mínima de metadata de contrato compatível com thirdweb.
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

# Conteúdo de ContractMetadata
CONTRACT_METADATA = """// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.18;

import "./interfaces/IContractMetadata.sol";

/**
 *  @title   Contract Metadata
 *  @notice  Thirdweb's ContractMetadata extension
 */
abstract contract ContractMetadata is IContractMetadata {
    /// @dev The sender is not authorized to perform the action
    error ContractMetadataUnauthorized();

    /// @notice Returns the contract metadata URI.
    string public override contractURI;

    /**
     *  @notice         Lets a contract admin set the URI for contract-level metadata.
     *  @dev            Caller should be authorized to setup contractURI, e.g. contract admin.
     *                  See {_canSetContractURI}.
     *                  Emits {ContractURIUpdated Event}.
     *
     *  @param _uri     keccak256 hash of the role. e.g. keccak256("TRANSFER_ROLE")
     */
    function setContractURI(string memory _uri) external override {
        if (!_canSetContractURI()) {
            revert ContractMetadataUnauthorized();
        }

        _setupContractURI(_uri);
    }

    /// @dev Lets a contract admin set the URI for contract-level metadata.
    function _setupContractURI(string memory _uri) internal {
        string memory prevURI = contractURI;
        contractURI = _uri;

        emit ContractURIUpdated(prevURI, _uri);
    }

    /// @dev Returns whether contract metadata can be set in the given execution context.
    function _canSetContractURI() internal view virtual returns (bool);
}
"""

def fix_flattened():
    """Corrige o arquivo flattened para Sourcify"""
    
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {INPUT_FILE}")
    
    # Ler arquivo original
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Remover todas as declarações de licença SPDX exceto a primeira
    lines = content.split('\n')
    fixed_lines = []
    first_license_found = False
    skip_next_spdx = False
    
    for i, line in enumerate(lines):
        # Se encontrar SPDX-License-Identifier
        if "SPDX-License-Identifier" in line:
            if not first_license_found:
                # Manter a primeira
                fixed_lines.append(line)
                first_license_found = True
                skip_next_spdx = True
            else:
                # Remover todas as outras
                continue
        else:
            fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    # 2. Substituir import de IContractMetadata pelo conteúdo inline
    if 'import "./interfaces/IContractMetadata.sol";' in content:
        # Encontrar onde está o import
        import_pos = content.find('import "./interfaces/IContractMetadata.sol";')
        if import_pos != -1:
            # Substituir pelo conteúdo
            content = content.replace(
                'import "./interfaces/IContractMetadata.sol";',
                '\n// === Imported from ./interfaces/IContractMetadata.sol ===\n' + 
                ICONTRACT_METADATA + 
                '\n// === End of ./interfaces/IContractMetadata.sol ===\n'
            )
    
    # 3. Substituir import de ContractMetadata pelo conteúdo inline
    if 'import "./ContractMetadata.sol";' in content:
        # Substituir pelo conteúdo (sem o import interno)
        contract_metadata_inline = CONTRACT_METADATA.replace(
            'import "./interfaces/IContractMetadata.sol";',
            '// IContractMetadata já incluído acima'
        )
        content = content.replace(
            'import "./ContractMetadata.sol";',
            '\n// === Imported from ./ContractMetadata.sol ===\n' + 
            contract_metadata_inline + 
            '\n// === End of ./ContractMetadata.sol ===\n'
        )
    
    # 4. Garantir que há apenas uma declaração de licença no topo
    # Se não houver nenhuma, adicionar
    if "SPDX-License-Identifier" not in content[:500]:
        content = "// SPDX-License-Identifier: MIT\n" + content
    
    # 5. Remover linhas duplicadas de licença que possam ter sobrado
    lines = content.split('\n')
    final_lines = []
    seen_spdx = False
    
    for line in lines:
        if "SPDX-License-Identifier" in line:
            if not seen_spdx:
                final_lines.append(line)
                seen_spdx = True
            # Pular linhas duplicadas
        else:
            final_lines.append(line)
    
    content = '\n'.join(final_lines)
    
    # Salvar arquivo corrigido
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("=" * 60)
    print("✅ Arquivo corrigido para Sourcify!")
    print("=" * 60)
    print()
    print(f"📁 Arquivo original: {INPUT_FILE}")
    print(f"📁 Arquivo corrigido: {OUTPUT_FILE}")
    print()
    print("📊 Estatísticas:")
    print(f"   Linhas originais: {len(INPUT_FILE.read_text().split(chr(10)))}")
    print(f"   Linhas corrigidas: {len(content.split(chr(10)))}")
    print()
    print("🔧 Correções aplicadas:")
    print("   ✅ Múltiplas licenças SPDX removidas (mantida apenas uma)")
    print("   ✅ Imports não resolvidos corrigidos")
    print()
    print("💡 Use este arquivo no Sourcify:")
    print(f"   {OUTPUT_FILE}")
    print()

if __name__ == "__main__":
    fix_flattened()
