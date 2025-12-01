#!/usr/bin/env python3
"""
Verificação direta via API OKLink usando código original
Baseado na documentação: https://www.oklink.com/docs/en/
Usa ETHERSCAN_API_KEY do .env (conforme dica-verify.md)
"""

import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
OKLINK_API_URL = "https://www.oklink.com/api/v5/explorer/contract/verify-source-code"
CHECK_STATUS_URL = "https://www.oklink.com/api/v5/explorer/contract/check-verify-result"
CHAIN_SHORT_NAME = "POLYGON"
CONTRACT_ADDRESS = "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2"
CONTRACT_NAME = "NeoFlowToken"

# Caminhos
PROJECT_ROOT = Path(__file__).parent.parent.parent
SOURCE_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
CONSTRUCTOR_ARGS = "0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"

# Versões do compilador para testar (em ordem de probabilidade)
COMPILER_VERSIONS = [
    "v0.8.30+commit.73712a01",
    "v0.8.30+commit.8c9944cf",
    "v0.8.30",
    "v0.8.18+commit.87f61d96",
]

def read_source_code():
    """Lê o código fonte original (sem ContractMetadata)"""
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {SOURCE_FILE}")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def send_verification(compiler_version):
    """Envia verificação para OKLink via API"""
    source_code = read_source_code()
    
    # Usar ETHERSCAN_API_KEY conforme dica-verify.md
    api_key = os.getenv("ETHERSCAN_API_KEY") or os.getenv("OKLINK_API_KEY") or ""
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "contractAddress": CONTRACT_ADDRESS,
        "contractName": CONTRACT_NAME,
        "sourceCode": source_code,
        "codeFormat": "solidity-single-file",
        "compilerVersion": compiler_version,
        "optimization": "1",
        "optimizationRuns": "200",
        "evmVersion": "paris",
        "viaIr": "false",
        "licenseType": "MIT License (MIT)",
        "constructorArguments": CONSTRUCTOR_ARGS,
    }
    
    headers = {
        "Content-Type": "application/json",
    }
    
    # Adicionar API key se disponível (conforme dica-verify.md)
    if api_key:
        headers["Ok-Access-Key"] = api_key
    
    print(f"🚀 Enviando verificação...")
    print(f"   Compiler: {compiler_version}")
    print(f"   API Key: {'✅ Configurada' if api_key else '⚠️  Não configurada (opcional)'}")
    print()
    
    try:
        response = requests.post(OKLINK_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == "0":
            guid = result.get("data", [""])[0]
            print(f"✅ Verificação enviada! GUID: {guid}")
            return guid
        else:
            print(f"❌ Erro: {result.get('msg', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"❌ Erro ao enviar: {str(e)[:100]}")
        return None

def check_status(guid):
    """Verifica status da verificação"""
    api_key = os.getenv("ETHERSCAN_API_KEY") or os.getenv("OKLINK_API_KEY") or ""
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "guid": guid
    }
    
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Ok-Access-Key"] = api_key
    
    try:
        response = requests.post(CHECK_STATUS_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == "0" and result.get("data"):
            return result["data"][0]
        return None
    except Exception:
        return None

def main():
    print("=" * 60)
    print("🔍 VERIFICAÇÃO DIRETA VIA API OKLINK")
    print("=" * 60)
    print()
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"📁 Arquivo: {SOURCE_FILE.name}")
    print(f"🌐 Chain: {CHAIN_SHORT_NAME}")
    print()
    
    # Verificar se ETHERSCAN_API_KEY está configurado
    api_key = os.getenv("ETHERSCAN_API_KEY") or os.getenv("OKLINK_API_KEY")
    if not api_key:
        print("⚠️  ETHERSCAN_API_KEY não encontrado no .env")
        print("   A verificação pode funcionar sem API key, mas é recomendado ter uma")
        print()
    
    # Tentar cada versão do compilador
    for compiler in COMPILER_VERSIONS:
        print(f"🔧 Tentando com: {compiler}")
        print()
        
        guid = send_verification(compiler)
        
        if guid:
            print()
            print("⏳ Aguardando resultado (30-60 segundos)...")
            import time
            time.sleep(60)
            
            status = check_status(guid)
            
            if status == "Success":
                print()
                print("=" * 60)
                print("🎉 SUCESSO! CONTRATO VERIFICADO!")
                print("=" * 60)
                print()
                print(f"✅ Configuração que funcionou:")
                print(f"   Compiler: {compiler}")
                print(f"   Optimization: Yes (200 runs)")
                print(f"   EVM Version: paris")
                print(f"   via-IR: false")
                print()
                print(f"🔗 Ver contrato:")
                print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
                return True
            elif status == "Fail":
                print(f"   ❌ Falhou com esta versão")
            else:
                print(f"   ⏳ Status: {status}")
        
        print()
    
    print("=" * 60)
    print("❌ NENHUMA VERSÃO FUNCIONOU")
    print("=" * 60)
    print()
    print("💡 Tente verificar manualmente no OKLink usando:")
    print(f"   Arquivo: {SOURCE_FILE}")
    print()
    return False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrompido pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()

