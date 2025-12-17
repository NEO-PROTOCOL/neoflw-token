#!/bin/bash
# 🚀 VERIFICAÇÃO AUTOMÁTICA - PLUG AND PLAY
# Este script tenta todas as formas possíveis de verificar o contrato

set -e

CONTRACT_ADDRESS="0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
CONTRACT_NAME="NeoFlowToken"
CONSTRUCTOR_ARGS="0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"

echo "🚀 VERIFICAÇÃO AUTOMÁTICA DO NEOFLOWTOKEN"
echo "=========================================="
echo ""
echo "Endereço: $CONTRACT_ADDRESS"
echo ""

# Método 1: Ape Framework (MAIS SIMPLES - RECOMENDADO)
echo "📋 Tentativa 1: Ape Framework (automático)"
echo "-------------------------------------------"
if command -v ape &> /dev/null; then
    echo "✅ Ape Framework encontrado"
    echo "⚠️  Nota: Precisa instalar plugin: ape plugins install etherscan"
    echo "Executando: ape etherscan verify $CONTRACT_NAME --network polygon:mainnet"
    if ape etherscan verify $CONTRACT_NAME --network polygon:mainnet 2>/dev/null; then
        echo ""
        echo "✅✅✅ SUCESSO! Contrato verificado via Ape Framework!"
        exit 0
    else
        echo "❌ Ape Framework não conseguiu verificar"
        echo ""
    fi
else
    echo "❌ Ape Framework não instalado"
    echo ""
fi

# Método 2: Hardhat com OKLink
echo "📋 Tentativa 2: Hardhat + OKLink Plugin"
echo "----------------------------------------"
if [ -f "hardhat.config.js" ]; then
    echo "✅ Hardhat config encontrado"
    echo "Executando: npx hardhat okverify --network polygon $CONTRACT_ADDRESS"
    if npx hardhat okverify --network polygon --contract contracts/NeoFlowToken.sol:NeoFlowToken $CONTRACT_ADDRESS --constructor-args $CONSTRUCTOR_ARGS 2>/dev/null; then
        echo ""
        echo "✅✅✅ SUCESSO! Contrato verificado via Hardhat!"
        exit 0
    else
        echo "❌ Hardhat não conseguiu verificar"
        echo ""
    fi
else
    echo "❌ Hardhat config não encontrado"
    echo ""
fi

# Método 3: Script Python Automático
echo "📋 Tentativa 3: Script Python Automático"
echo "-----------------------------------------"
if [ -f "scripts/verification/auto_verify_smart.py" ]; then
    echo "✅ Script Python encontrado"
    echo "Executando: python3 scripts/verification/auto_verify_smart.py"
    # Python retorna exit code baseado no resultado
    python3 scripts/verification/auto_verify_smart.py
    PYTHON_EXIT=$?
    if [ $PYTHON_EXIT -eq 0 ]; then
        echo ""
        echo "✅✅✅ SUCESSO! Contrato verificado via script Python!"
        exit 0
    else
        echo "❌ Script Python não conseguiu verificar (exit code: $PYTHON_EXIT)"
        echo ""
    fi
else
    echo "❌ Script Python não encontrado"
    echo ""
fi

echo ""
echo "❌❌❌ NENHUMA VERIFICAÇÃO AUTOMÁTICA FUNCIONOU"
echo ""
echo "💡 PRÓXIMOS PASSOS:"
echo "   1. Verifique se o contrato foi deployado corretamente"
echo "   2. Tente verificação manual no Polygonscan"
echo "   3. Verifique as configurações do Ape Framework"
echo ""
