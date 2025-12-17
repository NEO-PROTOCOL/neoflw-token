#!/usr/bin/env python3
"""
Verifica contrato no Sourcify via API
"""

import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Configurações
CONTRACT_ADDRESS = os.getenv("NEXT_PUBLIC_TOKEN_ADDRESS", "0x59aa4EaE743d608FBDd4205ebA59b38DCA755Dd2")
CHAIN_ID = 137  # Polygon Mainnet
PROJECT_ROOT = Path(__file__).parent.parent.parent
STANDARD_JSON_FILE = PROJECT_ROOT / "artifacts" / "verification" / "sourcify_standard_json.json"

SOURCIFY_API_URL = "https://sourcify.dev/server/verify"

def verify_contract():
    """Verifica contrato no Sourcify via API"""
    
    if not STANDARD_JSON_FILE.exists():
        print(f"❌ Arquivo não encontrado: {STANDARD_JSON_FILE}")
        print("   Execute primeiro: python3 scripts/verification/fix_standard_json_final.py")
        return False
    
    print("=" * 60)
    print("🚀 VERIFICAÇÃO SOURCIFY VIA API")
    print("=" * 60)
    print()
    print(f"📍 Contrato: {CONTRACT_ADDRESS}")
    print(f"🌐 Chain ID: {CHAIN_ID} (Polygon Mainnet)")
    print(f"📁 Arquivo: {STANDARD_JSON_FILE}")
    print()
    
    # Ler Standard JSON
    with open(STANDARD_JSON_FILE, "r", encoding="utf-8") as f:
        standard_json = json.load(f)
    
    # Preparar payload para Sourcify
    # Sourcify espera files como multipart/form-data
    files = {
        'files': (
            'standard_json.json',
            json.dumps(standard_json),
            'application/json'
        )
    }
    
    data = {
        'address': CONTRACT_ADDRESS,
        'chain': str(CHAIN_ID)
    }
    
    print("📤 Enviando para Sourcify...")
    print()
    
    try:
        response = requests.post(
            SOURCIFY_API_URL,
            files=files,
            data=data,
            timeout=60
        )
        
        print(f"📊 Status Code: {response.status_code}")
        print()
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Verificação enviada com sucesso!")
            print()
            print("📋 Resultado:")
            print(json.dumps(result, indent=2))
            print()
            print("🔗 Verificar status em:")
            print(f"   https://sourcify.dev/#/lookup/{CONTRACT_ADDRESS}")
            print()
            print("🔗 Polygonscan:")
            print(f"   https://polygonscan.com/address/{CONTRACT_ADDRESS}")
            return True
        else:
            print(f"❌ Erro na verificação:")
            print(f"   Status: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao enviar verificação:")
        print(f"   {str(e)}")
        return False

if __name__ == "__main__":
    verify_contract()
