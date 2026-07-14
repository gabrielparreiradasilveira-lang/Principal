#!/usr/bin/env python3
"""
Script de Autorização - Executa uma única vez
Abre o navegador e você autoriza. Token fica salvo automaticamente.
"""

import os
import pickle
import webbrowser

try:
    from google.auth.oauthlib.flow import InstalledAppFlow
except ImportError:
    print("Instalando dependências...")
    os.system("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client PyPDF2")
    from google.auth.oauthlib.flow import InstalledAppFlow


def autorizar():
    """
    Cria autorização do Google
    Abre navegador para você clicar em "Autorizar"
    Salva token automaticamente
    """

    print("""
╔════════════════════════════════════════════════════════════╗
║           AUTORIZAÇÃO GOOGLE SLIDES                       ║
║      (Isso só precisa ser feito UMA VEZ!)                ║
╚════════════════════════════════════════════════════════════╝
    """)

    # Verifica se credentials_oauth.json existe
    if not os.path.exists('credentials_oauth.json'):
        print("""
❌ Arquivo 'credentials_oauth.json' não encontrado!

Para criar:
1. Vá para: https://console.cloud.google.com/apis/credentials
2. Clique em "+ Criar Credenciais"
3. Escolha "OAuth 2.0 - ID do cliente"
4. Tipo: "Aplicativo para desktop"
5. Clique em "Criar"
6. Download o arquivo JSON
7. Renomeie para: credentials_oauth.json
8. Coloque nesta pasta
9. Volte a rodar este script!

Guia completo: AUTORIZACAO_RAPIDA.md
        """)
        return False

    print("✅ Arquivo credentials_oauth.json encontrado\n")

    SCOPES = [
        'https://www.googleapis.com/auth/presentations',
        'https://www.googleapis.com/auth/drive'
    ]

    try:
        print("🔐 Criando fluxo de autorização...\n")

        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials_oauth.json',
            SCOPES
        )

        print("📱 Abrindo navegador em 3 segundos...\n")
        print("   → Clique em 'Autorizar' quando o navegador abrir")
        print("   → Selecione sua conta Google")
        print("   → Clique em 'Permitir'\n")

        # Run local server
        creds = flow.run_local_server(port=0)

        # Salva token
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

        print("\n" + "=" * 60)
        print("✅ AUTORIZAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print("\n✨ Seu token foi salvo automaticamente!")
        print("   Próximas conversões serão automáticas!\n")

        return True

    except Exception as e:
        print(f"\n❌ Erro na autorização: {e}")
        print("\nTente novamente ou verifique:")
        print("  - credentials_oauth.json está correto?")
        print("  - APIs estão ativadas?")
        print("  - Seu template foi compartilhado com você?")
        return False


if __name__ == "__main__":
    sucesso = autorizar()

    if sucesso:
        print("\n🚀 Agora você pode usar:")
        print("   python converter_simples.py seu_pdf.pdf")
    else:
        print("\n📖 Leia: AUTORIZACAO_RAPIDA.md")
