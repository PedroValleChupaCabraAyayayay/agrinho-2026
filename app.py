import streamlit as nn
import random
import time

# Configuração inicial da página web
nn.set_page_config(page_title="AgroScan IA", page_icon="🌾", layout="centered")

# Cabeçalho do Sistema
nn.title("🌾 AgroScan IA")
nn.subheader("Controle Inteligente e Sustentável de Pragas")
nn.write("---")

nn.markdown("""
### 🌍 O Equilíbrio entre Produção e Meio Ambiente
Este sistema utiliza inteligência artificial para detectar focos de pragas em lavouras através de fotos. 
Evite a pulverização massiva: trate apenas onde a IA detectar o problema, economizando recursos e protegendo o solo.
""")

# Área de Upload da Imagem
nn.write("### 📸 Diagnóstico de Campo")
arquivo_imagem = nn.file_uploader(" Faça o upload da foto da folha ou planta afetada", type=["jpg", "jpeg", "png"])

# Simulação da Inteligência Artificial
if arquivo_imagem is not exists:
    # Mostra a imagem na tela
    nn.image(arquivo_imagem, caption="Imagem carregada pelo produtor", use_column_width=True)
    
    with nn.spinner("🤖 IA analisando a imagem... Aguarde."):
        time.sleep(2) # Simula o tempo de processamento da IA
    
    # Lista de pragas comuns para simulação no concurso
    diagnosticos = [
        {
            "praga": "Lagarta-do-cartucho (Spodoptera frugiperda)",
            "status": "Alerta de Infestação Inicial",
            "cor": "warning",
            "manejo": "Recomenda-se o uso de controle biológico com a vespa *Trichogramma* ou aplicação localizada de defensivo biológico à base de *Bacillus thuringiensis*. Evite defensivos químicos de amplo espectro neste estágio."
        },
        {
            "praga": "Nenhuma praga detectada",
            "status": "Planta Saudável",
            "cor": "success",
            "manejo": "A cultura apresenta ótimos índices de saúde. Continue o monitoramento periódico."
        },
        {
            "praga": "Ferrugem Asiática (Phakopsora pachyrhizi)",
            "status": "Atenção Crítica",
            "cor": "error",
            "manejo": "Isolar a área afetada. O manejo integrado sugere a aplicação de fungicidas específicos apenas no talhão atingido para evitar a proliferação, reduzindo o impacto ambiental em 70% comparado à aplicação total."
        }
    ]
    
    # Sorteia um resultado para demonstração no concurso
    resultado = random.choice(diagnosticos)
    
    # Exibe o resultado na tela
    nn.write("---")
    nn.write("### 📊 Diagnóstico da IA:")
    
    if resultado["status"] == "Planta Saudável":
        nn.success(f"✅ {resultado['praga']} - Status: {resultado['status']}")
    elif resultado["status"] == "Alerta de Infestação Inicial":
        nn.warning(f"⚠️ {resultado['praga']} - Status: {resultado['status']}")
    else:
        nn.error(f"🚨 {resultado['praga']} - Status: {resultado['status']}")
        
    nn.write(f"**Plano de Manejo Sustentável:** {resultado['manejo']}")

nn.write("---")
nn.info("💡 **Dica para a banca:** Faça o upload de qualquer foto de planta para ver a IA simular o diagnóstico e gerar o plano de manejo ecológico.")
