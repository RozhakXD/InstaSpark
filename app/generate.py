import requests, json

def generate_bio(description: str) -> dict:
    with requests.Session() as session:
        session.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Sec-Fetch-User": "?1",
            "Host": "www.blackbox.ai",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        response = session.get("https://www.blackbox.ai/agent/InstaSparkiPajE2b", allow_redirects=True, verify=True)
        
        sessionId = response.cookies.get('sessionId')
        
        data = {
            "messages": [
                {
                    "id": "8zz8bn3ricntI0BOcptk2",
                    "content": f"{description}",
                    "role": "user"
                }
            ],
            "agentMode": {
                "id": "InstaSparkiPajE2b",
                "name": "InstaSpark",
                "sysprompt": "Anda adalah seorang ahli dalam membuat bio Instagram yang menarik, modern, dan kreatif. Tugas Anda adalah menghasilkan bio Instagram berdasarkan deskripsi singkat yang diberikan oleh pengguna. Bio yang Anda buat harus mencerminkan kepribadian, minat, atau passion pengguna dengan gaya yang unik, profesional, dan sesuai dengan tren terkini.\n\nGunakan bahasa yang sangat ringkas (maksimal 150 karakter), kreatif, dan menarik perhatian. Prioritaskan kata-kata kunci yang kuat dan gunakan emoji secukupnya untuk menghemat ruang tanpa mengurangi makna. Jangan terpaku pada contoh yang diberikan—kembangkan ide yang lebih kreatif dan relevan berdasarkan deskripsi pengguna. Pastikan bio yang dihasilkan tetap informatif dan menggambarkan identitas pengguna dengan baik.\n\nFormat Output:\nOutput harus selalu dalam format README.md code block seperti berikut:\n```text\n[Bio Instagram (maksimal 150 karakter)]\n```\nPastikan untuk selalu menggunakan format ini agar output mudah di-scrape dan diproses lebih lanjut.\n\nPeringatan:\n- Maksimal 150 karakter/huruf (harus <= 150).\n- Jangan melebihi batas karakter!\n- Hindari penggunaan hashtag karena tidak berfungsi di bio Instagram.\n\nInstruksi Tambahan untuk InstaSpark:\n- Analisis deskripsi pengguna untuk mengidentifikasi kata kunci utama (contoh: \"membaca buku\" → 📚 Book Lover).\n- Gabungkan kata kunci dengan kalimat inspiratif atau aktivitas spesifik.\n- Susun bio dalam format multi-layer dengan emoji dan pemisah garis (➖) untuk tampilan yang rapi.\n- Pastikan bio tidak melebihi 150 karakter dan selalu gunakan format README.md code block.",
                "demonstrations": [
                    {
                        "userInput": "Deskripsi: Saya seseorang yang giat dalam membaca buku di perpustakaan",
                        "modelOutput": "```text\n📚 Book Lover | Library Explorer 🌟  \n➖  \n✨ Turning Pages, Expanding Minds  \n🌍 Always Lost in a Good Story  \n```"
                    },
                    {
                        "userInput": "Deskripsi: Saya seorang traveler yang suka menjelajahi tempat-tempat baru",
                        "modelOutput": "```text\n🌍 Wanderlust Soul | Adventure Seeker ✨  \n➖  \n🌟 Exploring the World, One Step at a Time  \n✈️ Collecting Memories, Not Just Stamps  \n```"
                    }
                ],
                "agentParams": None
            },
            "id": "8zz8bn3ricntI0BOcptk2",
            "previewToken": None,
            "userId": None,
            "codeModelMode": True,
            "trendingAgentMode": {},
            "isMicMode": False,
            "userSystemPrompt": None,
            "maxTokens": 1024,
            "playgroundTopP": None,
            "playgroundTemperature": None,
            "isChromeExt": False,
            "githubToken": "",
            "clickedAnswer2": False,
            "clickedAnswer3": False,
            "clickedForceWebSearch": False,
            "visitFromDelta": False,
            "isMemoryEnabled": False,
            "mobileClient": False,
            "userSelectedModel": None,
            "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94",
            "imageGenerationMode": False,
            "webSearchModePrompt": False,
            "deepSearchMode": False,
            "domains": None,
            "vscodeClient": False,
            "codeInterpreterMode": False,
            "customProfile": {
                "name": "",
                "occupation": "",
                "traits": [],
                "additionalInfo": "",
                "enableNewChats": False
            },
            "session": None,
            "isPremium": False
        }

        session.headers.update(
            {
                "Referer": "https://www.blackbox.ai/agent/Pseudofy-AIGeneratorPseudocodeOeIoRQK",
                "Cookie": f"sessionId={sessionId};",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Length": f"{len(json.dumps(data))}",
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Origin": "https://www.blackbox.ai",
            }
        )
        response2 = session.post('https://www.blackbox.ai/api/chat', json=data)
        if '```text' in response2.text:
            return {
                "status": True,
                "message": response2.text.split('```text')[1].split('```')[0].strip()
            }
        else:
            return {
                "status": False,
                "error": "Failed to generate bio"
            }
