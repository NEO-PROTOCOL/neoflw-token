#!/usr/bin/env python3
"""
Script automático para verificação de contrato
Testa diferentes configurações até encontrar a que funciona
"""

import os
import json
import requests
import time
from pathlib import Path

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

# Configurações para testar (em ordem de probabilidade)
COMPILER_VERSIONS = [
    "v0.8.30+commit.73712a01",  # Versão no cache
    "v0.8.30+commit.8c9944cf",  # Versão mencionada anteriormente
    "v0.8.30",                  # Sem commit hash
    "v0.8.18+commit.87f61d96",  # Versão do pragma
    "v0.8.29+commit.736ccbcf",  # Versão anterior
    "v0.8.28+commit.736ccbcf",  # Versão anterior
]

EVM_VERSIONS = [
    "paris",    # Conforme cache
    "default",  # Fallback
    "london",   # Alternativa
]

def read_source_code():
    """Lê o código fonte do contrato"""
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {SOURCE_FILE}")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def send_verification(compiler_version, evm_version, via_ir=False):
    """Envia verificação para OKLink"""
    source_code = read_source_code()
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "contractAddress": CONTRACT_ADDRESS,
        "contractName": CONTRACT_NAME,
        "sourceCode": source_code,
        "codeFormat": "solidity-single-file",
        "compilerVersion": compiler_version,
        "optimization": "1",
        "optimizationRuns": "200",
        "evmVersion": evm_version,
        "viaIr": "true" if via_ir else "false",
        "licenseType": "MIT License (MIT)",
        "constructorArguments": CONSTRUCTOR_ARGS,
    }
    
    headers = {"Content-Type": "application/json"}
    oklink_api_key = os.getenv("OKLINK_API_KEY")
    if oklink_api_key:
        headers["Ok-Access-Key"] = oklink_api_key
    
    try:
        response = requests.post(OKLINK_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == "0":
            return result.get("data", [""])[0]  # Retorna GUID
        else:
            return None
    except Exception as e:
        return None

def check_verification_status(guid):
    """Verifica o status da verificação"""
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "guid": guid
    }
    headers = {"Content-Type": "application/json"}
    oklink_api_key = os.getenv("OKLINK_API_KEY")
    if oklink_api_key:
        headers["Ok-Access-Key"] = oklink_api_key
    
    try:
        response = requests.post(CHECK_STATUS_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if result.get("code") == "0" and result.get("data"):
            return result["data"][0]  # Retorna status
        return None
    except Exception:
        return None

def auto_verify():
    """Tenta verificar automaticamente testando diferentes configurações"""
    print("=" * 60)
    print("🤖 VERIFICAÇÃO AUTOMÁTICA DO CONTRATO")
    print("=" * 60)
    print()
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Chain: {CHAIN_SHORT_NAME}")
    print()
    
    total_attempts = len(COMPILER_VERSIONS) * len(EVM_VERSIONS) * 2  # via-IR true/false
    attempt = 0
    
    # Testar todas as combinações
    for compiler in COMPILER_VERSIONS:
        for evm in EVM_VERSIONS:
            for via_ir in [False, True]:  # Testar com e sem via-IR
                attempt += 1
                
                print(f"[{attempt}/{total_attempts}] Testando:")
                print(f"   Compiler: {compiler}")
                print(f"   EVM: {evm}")
                print(f"   via-IR: {via_ir}")
                print()
                
                guid = send_verification(compiler, evm, via_ir)
                
                if guid:
                    print(f"   ✅ Verificação enviada! GUID: {guid}")
                    print(f"   ⏳ Aguardando resultado (30-60 segundos)...")
                    print()
                    
                    # Aguardar e verificar status
                    time.sleep(60)
                    
                    status = check_verification_status(guid)
                    
                    if status == "Success":
                        print("=" * 60)
                        print("🎉 SUCESSO! CONTRATO VERIFICADO!")
                        print("=" * 60)
                        print()
                        print("✅ Configuração que funcionou:")
                        print(f"   Compiler: {compiler}")
                        print(f"   EVM Version: {evm}")
                        print(f"   via-IR: {via_ir}")
                        print(f"   Optimization: Yes (200 runs)")
                        print()
                        print(f"🔗 Ver contrato:")
                        print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
                        return True
                    elif status == "Fail":
                        print(f"   ❌ Falhou com esta configuração")
                        print()
                    else:
                        print(f"   ⏳ Status: {status} (aguardando mais tempo...)")
                        time.sleep(30)
                        status = check_verification_status(guid)
                        if status == "Success":
                            print("=" * 60)
                            print("🎉 SUCESSO! CONTRATO VERIFICADO!")
                            print("=" * 60)
                            return True
                else:
                    print(f"   ❌ Erro ao enviar verificação")
                    print()
    
    print("=" * 60)
    print("❌ NENHUMA CONFIGURAÇÃO FUNCIONOU")
    print("=" * 60)
    print()
    print("💡 Possíveis causas:")
    print("   1. Código fonte não corresponde exatamente ao deploy")
    print("   2. Contrato pode ter sido deployado com configurações diferentes")
    print("   3. Pode ser necessário verificar manualmente no explorer")
    print()
    print("🔗 Verificar manualmente:")
    print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
    return False

if __name__ == "__main__":
    try:
        auto_verify()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrompido pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()

