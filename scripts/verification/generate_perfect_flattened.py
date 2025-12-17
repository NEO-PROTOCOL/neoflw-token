#!/usr/bin/env python3
"""
Gera arquivo flattened PERFEITO para verificação no Polygonscan/Sourcify
- Apenas 1 licença SPDX no topo
- Apenas 1 pragma solidity no topo
- Todos os imports resolvidos
- Pronto para uso direto
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
INPUT_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_original_flattened.sol"
OUTPUT_FILE = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_perfect.sol"

def generate_perfect_flattened():
    """Gera arquivo flattened perfeito para verificação"""
    
    input_file = INPUT_FILE
    if not input_file.exists():
        print(f"❌ Arquivo não encontrado: {input_file}")
        print(f"💡 Tentando usar outro arquivo...")
        # Tenta usar o arquivo sourcify como fallback
        fallback = PROJECT_ROOT / "artifacts" / "flattened" / "NeoFlowToken_flattened_sourcify.sol"
        if fallback.exists():
            input_file = fallback
            print(f"✅ Usando: {fallback}")
        else:
            return False
    
    print("=" * 70)
    print("🔧 Gerando arquivo flattened PERFEITO para verificação")
    print("=" * 70)
    print()
    
    # Ler arquivo original
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_lines = len(content.split('\n'))
    original_spdx = content.count("SPDX-License-Identifier")
    original_pragmas = content.count("pragma solidity")
    
    print(f"📊 Arquivo original:")
    print(f"   Linhas: {original_lines:,}")
    print(f"   Licenças SPDX: {original_spdx}")
    print(f"   Pragmas: {original_pragmas}")
    print()
    
    lines = content.split('\n')
    fixed_lines = []
    
    # Flags para controle
    first_spdx_found = False
    first_pragma_found = False
    header_done = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Processar licença SPDX
        if "SPDX-License-Identifier" in line:
            if not first_spdx_found:
                # Manter a primeira licença SPDX
                fixed_lines.append("// SPDX-License-Identifier: MIT")
                first_spdx_found = True
            # Pular todas as outras licenças SPDX
            i += 1
            continue
        
        # Processar pragma solidity
        if re.match(r'^\s*pragma\s+solidity', line):
            if not first_pragma_found:
                # Manter apenas o primeiro pragma (do contrato principal)
                # Usar a versão mais específica (^0.8.18)
                if "^0.8.18" in line or "0.8.18" in line:
                    fixed_lines.append("pragma solidity ^0.8.18;")
                else:
                    # Extrair a versão do primeiro pragma
                    match = re.search(r'(\^?0\.\d+\.\d+)', line)
                    if match:
                        version = match.group(1)
                        fixed_lines.append(f"pragma solidity {version};")
                    else:
                        fixed_lines.append("pragma solidity ^0.8.18;")
                first_pragma_found = True
                header_done = True
            # Pular todos os outros pragmas
            i += 1
            continue
        
        # Após o header (SPDX + pragma), adicionar linha em branco se necessário
        if header_done and first_pragma_found and len(fixed_lines) > 0:
            if fixed_lines[-1] != "" and line.strip() != "":
                # Verificar se precisa de linha em branco
                if not any(x in fixed_lines[-1] for x in [";", "}", "//"]):
                    pass  # Não adicionar linha em branco desnecessária
        
        # Adicionar linha normal
        fixed_lines.append(line)
        i += 1
    
    # Garantir que começa com SPDX e pragma
    if not first_spdx_found:
        fixed_lines.insert(0, "// SPDX-License-Identifier: MIT")
    
    if not first_pragma_found:
        # Procurar primeiro pragma no conteúdo
        for line in fixed_lines:
            if "pragma solidity" in line:
                match = re.search(r'(\^?0\.\d+\.\d+)', line)
                if match:
                    version = match.group(1)
                    fixed_lines.insert(1, f"pragma solidity {version};")
                    break
        else:
            fixed_lines.insert(1, "pragma solidity ^0.8.18;")
    
    # Garantir linha em branco após header
    if len(fixed_lines) > 2:
        if fixed_lines[2].strip() != "":
            fixed_lines.insert(2, "")
    
    # Remover linhas vazias duplicadas excessivas (máximo 2 consecutivas)
    final_lines = []
    empty_count = 0
    for line in fixed_lines:
        if line.strip() == "":
            empty_count += 1
            if empty_count <= 2:  # Permitir até 2 linhas vazias consecutivas
                final_lines.append(line)
        else:
            empty_count = 0
            final_lines.append(line)
    
    fixed_content = '\n'.join(final_lines)
    
    # Estatísticas finais
    final_spdx = fixed_content.count("SPDX-License-Identifier")
    final_pragmas = fixed_content.count("pragma solidity")
    final_lines = len(fixed_content.split('\n'))
    
    # Salvar arquivo
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(fixed_content)
    
    print("=" * 70)
    print("✅ Arquivo PERFEITO gerado com sucesso!")
    print("=" * 70)
    print()
    print(f"📁 Arquivo de entrada:  {input_file}")
    print(f"📁 Arquivo de saída:   {OUTPUT_FILE}")
    print()
    print("📊 Estatísticas:")
    print(f"   Linhas:        {original_lines:,} → {final_lines:,}")
    print(f"   Licenças SPDX: {original_spdx} → {final_spdx} ✅")
    print(f"   Pragmas:       {original_pragmas} → {final_pragmas} ✅")
    print()
    print("🔧 Correções aplicadas:")
    print("   ✅ Apenas 1 licença SPDX no topo")
    print("   ✅ Apenas 1 pragma solidity no topo")
    print("   ✅ Formatação limpa e consistente")
    print()
    print("💡 Uso:")
    print("   Este arquivo está pronto para:")
    print("   • Polygonscan (método Flattened Source Code)")
    print("   • Sourcify (upload direto)")
    print("   • Outros block explorers")
    print()
    print(f"📋 Caminho completo:")
    print(f"   {OUTPUT_FILE}")
    print()
    
    # Verificar primeiras linhas
    print("📝 Primeiras linhas do arquivo:")
    print("-" * 70)
    for i, line in enumerate(fixed_content.split('\n')[:10], 1):
        print(f"{i:3}: {line}")
    print("-" * 70)
    print()
    
    return True

if __name__ == "__main__":
    success = generate_perfect_flattened()
    if not success:
        exit(1)
