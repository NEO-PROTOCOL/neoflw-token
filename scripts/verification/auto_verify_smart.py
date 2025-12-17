#!/usr/bin/env python3
"""
Script inteligente para verificação automática
Testa primeiro as configurações mais prováveis
"""

import os
import json
import requests
import time
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis do .env (se existir)
load_dotenv()

# Configurações - URLs da API (fixas, não precisam estar no .env)
OKLINK_API_URL = os.getenv("OKLINK_API_URL", "https://www.oklink.com/api/v5/explorer/contract/verify-source-code")
CHECK_STATUS_URL = os.getenv("OKLINK_CHECK_STATUS_URL", "https://www.oklink.com/api/v5/explorer/contract/check-verify-result")

# Configurações - podem ser definidas no .env ou usar valores padrão
CHAIN_SHORT_NAME = os.getenv("OKLINK_CHAIN_SHORT_NAME", "POLYGON")
CONTRACT_ADDRESS = os.getenv("NEXT_PUBLIC_TOKEN_ADDRESS", "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
CONTRACT_NAME = os.getenv("OKLINK_CONTRACT_NAME", "NeoFlowToken")

# Caminhos
PROJECT_ROOT = Path(__file__).parent.parent.parent
SOURCE_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
CONSTRUCTOR_ARGS = "0000000000000000000000000000000000000000033b2e3c9fd0803ce8000000"

# Configurações ordenadas por probabilidade (mais prováveis primeiro)
# ⚠️ IMPORTANTE: Bytecode on-chain indica versão 0.8.18 ou anterior
CONFIGURATIONS = [
    # ⭐ MAIS PROVÁVEIS (bytecode mostra características de 0.8.18)
    {"compiler": "v0.8.18+commit.87f61d96", "evm": "default", "via_ir": False},
    {"compiler": "v0.8.18+commit.87f61d96", "evm": "paris", "via_ir": False},
    {"compiler": "v0.8.18", "evm": "default", "via_ir": False},
    {"compiler": "v0.8.17+commit.8df45f5f", "evm": "default", "via_ir": False},
    {"compiler": "v0.8.16+commit.07a7930e", "evm": "default", "via_ir": False},
    {"compiler": "v0.8.19+commit.425a24f5", "evm": "default", "via_ir": False},
    
    # Versões mais novas (menos prováveis)
    {"compiler": "v0.8.30+commit.73712a01", "evm": "paris", "via_ir": False},
    {"compiler": "v0.8.30", "evm": "paris", "via_ir": False},
    {"compiler": "v0.8.30+commit.73712a01", "evm": "default", "via_ir": False},
    {"compiler": "v0.8.29+commit.736ccbcf", "evm": "paris", "via_ir": False},
]

def read_source_code():
    """Lê o código fonte do contrato"""
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {SOURCE_FILE}")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def send_verification(config):
    """Envia verificação para OKLink"""
    source_code = read_source_code()
    
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "contractAddress": CONTRACT_ADDRESS,
        "contractName": CONTRACT_NAME,
        "sourceCode": source_code,
        "codeFormat": "solidity-single-file",
        "compilerVersion": config["compiler"],
        "optimization": "1",
        "optimizationRuns": "200",
        "evmVersion": config["evm"],
        "viaIr": "true" if config["via_ir"] else "false",
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
            print(f"      ❌ Erro: {result.get('msg', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"      ❌ Erro de conexão: {str(e)[:50]}")
        return None

def check_verification_status(guid, max_attempts=3):
    """Verifica o status da verificação (com retry)"""
    payload = {
        "chainShortName": CHAIN_SHORT_NAME,
        "guid": guid
    }
    headers = {"Content-Type": "application/json"}
    oklink_api_key = os.getenv("OKLINK_API_KEY")
    if oklink_api_key:
        headers["Ok-Access-Key"] = oklink_api_key
    
    for attempt in range(max_attempts):
        try:
            response = requests.post(CHECK_STATUS_URL, json=payload, headers=headers, timeout=30)
            response.raise_for_status()
            result = response.json()
            
            if result.get("code") == "0" and result.get("data"):
                return result["data"][0]  # Retorna status
            
            time.sleep(20)  # Aguardar antes de tentar novamente
        except Exception:
            time.sleep(20)
    
    return None

def auto_verify_smart():
    """Tenta verificar automaticamente testando configurações mais prováveis primeiro"""
    print("=" * 60)
    print("🤖 VERIFICAÇÃO AUTOMÁTICA INTELIGENTE")
    print("=" * 60)
    print()
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Chain: {CHAIN_SHORT_NAME}")
    print(f"📁 Arquivo: {SOURCE_FILE.name}")
    print()
    print(f"🔍 Testando {len(CONFIGURATIONS)} configurações (mais prováveis primeiro)...")
    print()
    
    for i, config in enumerate(CONFIGURATIONS, 1):
        print(f"[{i}/{len(CONFIGURATIONS)}] Testando:")
        print(f"   Compiler: {config['compiler']}")
        print(f"   EVM: {config['evm']}")
        print(f"   via-IR: {config['via_ir']}")
        
        guid = send_verification(config)
        
        if guid:
            print(f"   ✅ Enviado! GUID: {guid}")
            print(f"   ⏳ Aguardando resultado...")
            
            # Aguardar e verificar status
            time.sleep(60)
            
            status = check_verification_status(guid)
            
            if status == "Success":
                print()
                print("=" * 60)
                print("🎉 SUCESSO! CONTRATO VERIFICADO!")
                print("=" * 60)
                print()
                print("✅ Configuração que funcionou:")
                print(f"   Compiler: {config['compiler']}")
                print(f"   EVM Version: {config['evm']}")
                print(f"   via-IR: {config['via_ir']}")
                print(f"   Optimization: Yes (200 runs)")
                print()
                print(f"🔗 Ver contrato verificado:")
                print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
                print()
                
                # Salvar configuração que funcionou
                success_config = {
                    "compiler": config['compiler'],
                    "evm": config['evm'],
                    "via_ir": config['via_ir'],
                    "optimization": True,
                    "optimization_runs": 200,
                    "contract_address": CONTRACT_ADDRESS,
                }
                
                config_file = PROJECT_ROOT / "artifacts" / "verification" / "successful_config.json"
                config_file.parent.mkdir(parents=True, exist_ok=True)
                with open(config_file, "w") as f:
                    json.dump(success_config, f, indent=2)
                
                print(f"💾 Configuração salva em: {config_file}")
                return True
            elif status == "Fail":
                print(f"   ❌ Falhou")
            else:
                print(f"   ⏳ Status: {status}")
        else:
            print(f"   ❌ Falha ao enviar")
        
        print()
    
    print("=" * 60)
    print("❌ NENHUMA CONFIGURAÇÃO FUNCIONOU")
    print("=" * 60)
    print()
    print("💡 Possíveis causas:")
    print("   1. Código fonte não corresponde exatamente ao deploy")
    print("   2. Contrato pode ter sido deployado com configurações muito diferentes")
    print("   3. Pode ser necessário verificar manualmente")
    print()
    print("🔗 Verificar manualmente:")
    print(f"   https://www.oklink.com/polygon/address/{CONTRACT_ADDRESS}")
    import sys
    sys.exit(1)  # Retorna exit code 1 para indicar falha

if __name__ == "__main__":
    import sys
    try:
        success = auto_verify_smart()
        if not success:
            sys.exit(1)  # Retorna exit code 1 se falhou
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrompido pelo usuário")
        sys.exit(130)  # Exit code padrão para Ctrl+C
    except Exception as e:
        print(f"\n\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

