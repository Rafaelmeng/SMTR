
import requests, os
from dotenv import load_dotenv


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as variáveis de ambiente
prtg_url = os.getenv("PRTG_BASE_URL")
prtg_username = os.getenv("PRTG_USERNAME")
prtg_passhash = os.getenv("PRTG_PASSHASH")



class Request:
    def __init__(self):
        
        self.base = prtg_url
        self.auth = f"&username={prtg_username}&passhash={prtg_passhash}"
        self.endpoint = "/api/table.json?content=sensors&output=json&columns=sensor,message,lastup,device"
        self.filter_backbone = "&filter_name=@sub(BB, Traffic)&filter_status=5"
        self.filter_ops = "&filter_name=@sub(OPS)&filter_status=5&id=38147"
        self.filter_anel = "&filter_name=@sub(AN-, Traffic)&filter_status=5"
        self.filter_pps = "&filter_name=@sub(PPS-, )&filter_status=5"

    def get_sensors(self, filter):
        response = requests.get(
            f"{self.base}{self.endpoint}{filter}{self.auth}", verify=False
        ).json()
        sensors = response.get("sensors", [])
        return [sensor for sensor in sensors if "INFO" not in sensor["sensor"]]

    def get_backbone(self):
        return self.get_sensors(self.filter_backbone)

    def get_ops(self):
        return self.get_sensors(self.filter_ops)

    def get_anel(self):
        return self.get_sensors(self.filter_anel)

    def get_pps(self):
        return self.get_sensors(self.filter_pps)