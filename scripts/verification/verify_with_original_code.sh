#!/bin/bash
# Script para verificar contrato usando Hardhat com código ORIGINAL (sem ContractMetadata)
# O problema: Hardhat compila o contrato atual (com ContractMetadata) mas o deploy foi feito sem ele

set -e

CONTRACT_ADDRESS="0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
ORIGINAL_FILE="artifacts/flattened/NeoFlowToken_original_flattened.sol"
BACKUP_DIR=".backup_contracts"

echo "============================================================"
echo "🔧 VERIFICAÇÃO COM CÓDIGO ORIGINAL (sem ContractMetadata)"
echo "============================================================"
echo ""

# Criar backup do contrato atual
echo "📦 Criando backup do contrato atual..."
mkdir -p "$BACKUP_DIR"
cp contracts/NeoFlowToken.sol "$BACKUP_DIR/NeoFlowToken_with_metadata.sol"
echo "✅ Backup criado"
echo ""

# Criar versão temporária do contrato original (sem ContractMetadata)
echo "📝 Criando versão temporária do contrato original..."
cat > contracts/NeoFlowToken.sol << 'EOF'
// contracts/NeoFlowToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NeoFlowToken is ERC20, Ownable {
    event Burned(address indexed account, uint256 amount);

    constructor(uint256 initialSupply) ERC20("NEOFlowOFF", "NEOFLW") {
        _mint(msg.sender, initialSupply);
    }

    function burn(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }
}
EOF
echo "✅ Contrato original criado temporariamente"
echo ""

# Compilar com Hardhat
echo "🔨 Compilando contrato original..."
npx hardhat clean
npx hardhat compile
echo ""

# Verificar
echo "🚀 Verificando contrato..."
if npx hardhat okverify \
    --network polygon \
    "$CONTRACT_ADDRESS"; then
    echo ""
    echo "✅ Verificação bem-sucedida!"
    SUCCESS=true
else
    echo ""
    echo "⚠️  Verificação falhou. Tentando com contrato especificado..."
    if npx hardhat okverify \
        --network polygon \
        --contract contracts/NeoFlowToken.sol:NeoFlowToken \
        "$CONTRACT_ADDRESS"; then
        echo ""
        echo "✅ Verificação bem-sucedida!"
        SUCCESS=true
    else
        echo ""
        echo "❌ Verificação falhou"
        SUCCESS=false
    fi
fi

# Restaurar contrato original
echo ""
echo "🔄 Restaurando contrato original..."
cp "$BACKUP_DIR/NeoFlowToken_with_metadata.sol" contracts/NeoFlowToken.sol
echo "✅ Contrato restaurado"
echo ""

if [ "$SUCCESS" = true ]; then
    echo "🎉 Processo concluído com sucesso!"
    exit 0
else
    echo "❌ Verificação não foi bem-sucedida"
    echo ""
    echo "💡 Tente usar o método manual com o arquivo flattened:"
    echo "   artifacts/flattened/NeoFlowToken_original_flattened.sol"
    exit 1
fi

