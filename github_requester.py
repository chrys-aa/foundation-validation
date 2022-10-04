import requests

# token_github = os.getenv("GITHUB_PAS")
token_github = "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"

project_url = {
    "android": "https://api.github.com/repos/chrys-aa/foundation-validation/pulls/",
    "ios": "https://api.github.com/repos/chrys-aa/foundation-validation/pulls/"
}

headers = { 
    "Authorization": f"Bearer {token_github}",
    "Accept": "application/vnd.github+json"
}

def getPRInfo(platform, pr_number):
    try:
        #TODO Implement project get by platform variable
        print(f'Plataforma: {platform}, Número da entrega: {pr_number}')
        response = requests.get(f"{project_url[platform]}{pr_number}",headers=headers, timeout=5)

        if response.status_code == 200:
            response_json = response.json()
            pr_body = response_json["body"]
            pr_body.replace("\r\n","")
            return pr_body
    except Exception as e:
        print("Erro na requisição")
        raise Exception("Falha ao obter dados do repositório.")

