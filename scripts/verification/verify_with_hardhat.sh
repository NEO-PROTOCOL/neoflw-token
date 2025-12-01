#!/bin/bash
# Script para verificar contrato usando Hardhat + Plugin OKLink
# Baseado na documentação oficial: https://github.com/okx/hardhat-explorer-verify

set -e

CONTRACT_ADDRESS="0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
CONTRACT_NAME="NeoFlowToken"
CONTRACT_FILE="contracts/NeoFlowToken.sol"
CONSTRUCTOR_ARGS="1000000000000000000000000000"  # 1 bilhão * 10^18

echo "============================================================"
echo "🔍 VERIFICAÇÃO DE CONTRATO COM HARDHAT + OKLINK PLUGIN"
echo "============================================================"
echo ""
echo "📍 Contrato: $CONTRACT_ADDRESS"
echo "📁 Arquivo: $CONTRACT_FILE"
echo "🏷️  Nome: $CONTRACT_NAME"
echo "🌐 Network: polygon"
echo ""

# Verificar se o plugin está instalado
if ! npm list @okxweb3/hardhat-explorer-verify > /dev/null 2>&1; then
    echo "❌ Plugin não encontrado. Instalando..."
    npm install @okxweb3/hardhat-explorer-verify --save-dev
fi

echo "✅ Plugin verificado"
echo ""

# Compilar primeiro (para garantir que está atualizado)
echo "🔨 Compilando contrato..."
npx hardhat compile
echo ""

# Tentar verificação básica primeiro
echo "🚀 Tentando verificação básica..."
echo ""

if npx hardhat okverify \
    --network polygon \
    "$CONTRACT_ADDRESS"; then
    echo ""
    echo "✅ Verificação bem-sucedida!"
    exit 0
fi

echo ""
echo "⚠️  Verificação básica falhou. Tentando com contrato especificado..."
echo ""

# Tentar com contrato especificado
if npx hardhat okverify \
    --network polygon \
    --contract "$CONTRACT_FILE:$CONTRACT_NAME" \
    "$CONTRACT_ADDRESS"; then
    echo ""
    echo "✅ Verificação bem-sucedida!"
    exit 0
fi

echo ""
echo "⚠️  Tentando com constructor arguments..."
echo ""

# Tentar com constructor arguments
if npx hardhat okverify \
    --network polygon \
    --contract "$CONTRACT_FILE:$CONTRACT_NAME" \
    "$CONTRACT_ADDRESS" \
    --constructor-args "$CONSTRUCTOR_ARGS"; then
    echo ""
    echo "✅ Verificação bem-sucedida!"
    exit 0
fi

echo ""
echo "❌ Todas as tentativas falharam."
echo ""
echo "💡 Verifique:"
echo "   1. Se o contrato foi compilado com as mesmas configurações"
echo "   2. Se o código fonte corresponde exatamente ao deploy"
echo "   3. Se a network está configurada corretamente"
echo ""
echo "🔗 Verificar manualmente:"
echo "   https://www.oklink.com/polygon/address/$CONTRACT_ADDRESS"
echo ""

exit 1

