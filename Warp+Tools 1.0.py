import qrcode
import os
import httpx
import warnings
import ctypes
import random
import time
import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from nacl.bindings import crypto_scalarmult_base
from io import BytesIO
import asyncio
from colorama import Fore, init
from PIL import Image
from base64 import b64encode

""" Dev >>> T.me/Error772 """

ctypes.windll.kernel32.SetConsoleTitleW("Warp+ Tool 1.0 | Error772")
os.system("mode 110,27")
init(convert=True)
warnings.filterwarnings("ignore")

# ==============================[Values]============================== #

Timeout = 30.0
C_White = Fore.LIGHTWHITE_EX
C_Cyan = Fore.CYAN
C_Blue = Fore.BLUE
C_LCyan = Fore.LIGHTCYAN_EX
C_Yellow = Fore.YELLOW
C_Red = Fore.RED
C_Green = Fore.GREEN

LOGO = f"""
        {C_Blue}
                                     
                                            __        __                     
                                            \ \      / /_ _ _ __ _ __    _   
                                             \ \ /\ / / _` | '__| '_ \ _| |_ 
                                              \ V  V / (_| | |  | |_) |_   _|
                                               \_/\_/ \__-_|_|  | .__/  |_|  
                                                                |_|          
                                                                  {C_Yellow}By Error772{C_White}"""

TIMEOUT = 30.0

KEY_SAMPLES = [
    "G1U50X9Q-EeD956U2-Y10L6wE5",
    "4K07b9PI-5C6Z1E2b-ZD49mO10",
    "WT01vN43-8Th6b20i-2RW7n54a",
    "Fhl38Q51-93cxYP72-Q56HB37d",
    "960XeUb3-nJ3bW654-K3U560Aa",
    "C0358LIg-NJr472O6-47a9reF2",
    "3Hx07rq1-5oQ32i4g-025cVkY4",
    "2Z5T1w6H-t4b53O6p-2Q1Hd78L",
    "S5ep609T-15se7HE2-ZgQ5763J",
    "fxQ639i7-3s042wor-98f3LP6G",
    "19Pvfr24-7I5E82zM-7g2r94pj",
    "1kN6Ut53-fL6s9P27-574OP0IT",
    "5R6gAl30-2cs803Ad-t7WS9Z52",
    "Ka59yv30-2DHng563-4Y0y52iw",
    "D54ZmP82-05iZ8vr4-y5Tu306K",
    "4NbW5x30-0dO72rB4-5TLJx208",
    "39Df7L6q-OL910b2X-LG1H7y24",
    "7s9q2Xo6-5BbY1S70-G875WQ0k",
    "75IVkU04-75GMm2f0-37hrL1D5",
    "P23J49IS-Bm1752tI-94l7VQC2",
    "1Y6g3w2e-X2wb8A46-6sF834Ar",
]

HEADERS = {
    "CF-Client-Version": "a-6.11-2223",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
}

BASE_URL = "https://api.cloudflareclient.com/v0a2223/reg"

# ==============================[Functions]============================== #


def clear():
    print("\033c", end="")


def KeyGen_Wireguard():
    private_key = os.urandom(32)
    public_key = crypto_scalarmult_base(private_key)
    return b64encode(private_key).decode("utf-8"), b64encode(public_key).decode("utf-8")


def about():
    clear()
    print(f"""{LOGO}\n\n
    [{C_Yellow}>{C_White}] {C_White}Application {C_LCyan}>>> {C_White}Warp+ Tool {C_Yellow}1.0{C_White}
    [{C_Yellow}>{C_White}] {C_White}Developed by: {C_Cyan}T.me/Error772{C_White}

    [{C_Yellow}>{C_White}] {C_White}GitHub {C_LCyan}>>> {C_Cyan}https://github.com/Error772
    {C_White}[{C_Yellow}>{C_White}] {C_White}Telegram {C_LCyan}>>> {C_Cyan}https://t.me/Error772\n\n""")
    input(f"{C_Yellow}#> {C_White}Done! {C_Green}Press Enter to continue . . . ")


def warns():
    clear()
    print(LOGO)
    print(f" {C_White}[{C_Green}*{C_White}] Important things before you start")
    print()
    print(f" {C_White}[{C_Yellow}+{C_White}] For Iranian users")
    print()
    print(
        f" {C_White}[{C_Red}-{C_White}] 1. This tool requires a VPN to function properly."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] 2. Default WireGuard settings won't work for Iranian users."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}]    You need to replace the Endpoint and Port with a clear Cloudflare IP address."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] 3. Licenses and Warp software are compatible with MIC, Mokhaberat, and Irancell."
    )
    print()
    print(f" {C_White}[{C_Yellow}+{C_White}] For All Users")
    print()
    print(f" {C_White}[{C_Red}-{C_White}] If you encounter the following errors:")
    print(f" {C_White}[{C_Red}-{C_White}] 1. Error 0")
    print(f" {C_White}[{C_Red}-{C_White}] 2. Server Disconnected Without response")
    print(
        f" {C_White}[{C_Red}-{C_White}]    It means your IP has been banned. Retry after 30 minutes or use a VPN and change locations."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] If you encounter 'Failed to Generate Unlimited Data License':"
    )
    print(
        f" {C_White}[{C_Red}-{C_White}]    It indicates your IP isn't clear. Use a VPN."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] If you encounter an SSL error, switch to another VPN. (You won't get SSL errors with a VPN)"
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] If you get '[Expecting value: line 1 column 1]', close the program and retry after 30 minutes."
    )
    print(
        f" {C_White}[{C_Red}-{C_White}] This program deletes client configs and Token IDs. Other data is useless except the license."
    )
    print()
    print(f"{C_Red}[-] Warning: {C_White}This tool is for educational purposes only.")
    print(
        f"{C_Red}[-] Warning: {C_White}Using this tool may violate Cloudflare's terms of service."
    )
    print(
        f"{C_Red}[-] Warning: {C_White}The developer is not responsible for any misuse or damage caused by this tool.\n"
    )
    input(f"{C_Yellow}#> {C_White}Understood! {C_Green}Press Enter to continue . . . ")


def message_box(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 1)


async def generate_qr(prk, puk, address, endpoint, path=""):
    if not path:
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        path = f"Warp+ (Wireguard Qr) {time_str}.png"

    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        response = await client.get(
            "https://static-00.iconduck.com/assets.00/wireguard-icon-512x512-7suxjlbo.png"
        )
        logo = Image.open(BytesIO(response.content))

    width = 150
    percent = width / float(logo.size[0])
    size = int(float(logo.size[1]) * percent)
    logo = logo.resize((width, size), Image.LANCZOS)

    qr_code = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H, version=2
    )

    config = f"""[Interface]
PrivateKey = {prk}
Address = {address}
DNS = 1.1.1.1
[Peer]
PublicKey = {puk}
Endpoint = {endpoint}
AllowedIPs = 0.0.0.0/0"""

    qr_code.add_data(config)
    qr_code.make()

    img = qr_code.make_image(
        image_factory=StyledPilImage,
        color_mask=RadialGradiantColorMask(),
        module_drawer=RoundedModuleDrawer(),
    )
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    img.save(path)


async def single_wg():
    Prk = input(f"{C_Yellow}#> {C_White}Public Key: ")
    Puk = input(f"{C_Yellow}#> {C_White}Priavte Key: ")
    Address = input(f"{C_Yellow}#> {C_White}Address: ")
    Endpoint = input(f"{C_Yellow}#> {C_White}Endpoint: ")
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    name = f"Warp+ (Wireguard) {time_str}"
    os.mkdir(name)

    generate_qr(Prk, Puk, Address, Endpoint, path=os.path.join(name, "Wireguard.png"))
    print("\n")
    print(f"[{C_Cyan}+{C_White}] Successfuly Saved.")
    print()


async def wg_mode(res):
    print(f" [{Fore.GREEN}*{Fore.WHITE}] Successfully Generated.")
    lic, dat, did, tkk, prk, puk, add, end = map(str, res)
    dat += " GB"
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    name = f"Warp+ (Wireguard) {time_str}"
    os.mkdir(name)

    lic_format = f"""Warp+ {time_str}

License : {lic} 

Data Remaining : {dat}

Device ID : {did}

Token : {tkk}

Credit : Error772"""

    wg_format = f"""[Interface]
PrivateKey = {prk}
Address = {add}

[Peer]
PublicKey = {puk}
AllowedIPs = 0.0.0.0/1
Endpoint = {end}"""

    print(f" [{Fore.GREEN}*{Fore.WHITE}] Creating License...")
    time.sleep(1)
    with open(os.path.join(name, "License.txt"), "w") as file:
        file.write(lic_format)

    print(f" [{Fore.GREEN}*{Fore.WHITE}] Creating Wireguard Config...")
    time.sleep(1)
    with open(os.path.join(name, "Wireguard.conf"), "w") as file:
        file.write(wg_format)

    print(f" [{Fore.GREEN}*{Fore.WHITE}] Creating Wireguard QR Code...")
    time.sleep(1)
    await generate_qr(prk, puk, add, end, os.path.join(name, "Wireguard.png"))

    print(f" [{Fore.CYAN}>{Fore.WHITE}] License : {lic}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Data Remaining : {dat}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Device ID : {did}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Token : {tkk}")
    print()
    print(f" [{Fore.YELLOW}+{Fore.WHITE}] Wireguard Config Details")
    print()
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Private Key : {prk}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Public Key : {puk}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Address : {add}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Endpoint : {end}")
    print()
    print(f" [{Fore.GREEN}*{Fore.WHITE}] Done.")
    print()
    input(f"{C_Yellow}#> {C_White}Done! {C_Green}Press Enter to continue . . . ")


async def single_mode(res):
    print(f" [{Fore.GREEN}*{Fore.WHITE}] Successfully Generated.")
    time.sleep(1)
    lic, dat, did, tkk = map(str, res[:4])
    dat += " GB"
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    name = f"Warp+ License {time_str}.txt"

    lic_format = f"""Warp+ {time_str}

License : {lic} 
input(f" [{Fore.CYAN}>{Fore.WHITE}] Press A
Data Remaining : {dat}

Device ID : {did}

Token : {tkk}

Credit : Error772"""

    print(f" [{Fore.GREEN}*{Fore.WHITE}] Saving Txt File...")
    time.sleep(1)
    with open(name, "w") as file:
        file.write(lic_format)

    print(f" [{Fore.YELLOW}+{Fore.WHITE}] Details")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] License : {lic}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Data Remaining : {dat}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Device ID : {did}")
    print(f" [{Fore.CYAN}>{Fore.WHITE}] Token : {tkk}")
    print()
    print(f" [{Fore.GREEN}*{Fore.WHITE}] Done.")
    print()
    input(f"{C_Yellow}#> {C_White}Done! {C_Green}Press Enter to continue . . . ")


async def gen_wireguard():
    try:
        base_url = "https://api.cloudflareclient.com/v0a884/reg"
        fheaders = {
            "User-Agent": "okhttp/3.12.1",
            "Content-Type": "application/json; charset=UTF-8",
        }

        keys = KeyGen_Wireguard()

        content = {
            "key": keys[1],
            "install_id": "",
            "fcm_token": "",
            "referrer": "bcf5ab07-0d3c-466d-9da8-b9cf8d3eec42",
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-7] + "Z",
            "model": "",
            "type": "Android",
            "locale": "en_US",
        }

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            req = await client.post(url=base_url, headers=fheaders, json=content)
            req_json = req.json()

            id1 = req_json["id"]
            token1 = req_json["token"]
            license = req_json["account"]["license"]
            private_key = keys[0]
            public_key = req_json["config"]["peers"][0]["public_key"]
            address = req_json["config"]["interface"]["addresses"]["v4"]
            endpoint = req_json["config"]["peers"][0]["endpoint"]["host"]

            sheaders = {
                "CF-Client-Version": "a-6.11-2223",
                "Host": "api.cloudflareclient.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.12.1",
            }

            base_url_v2 = "https://api.cloudflareclient.com/v0a2223/reg"
            req = await client.post(base_url_v2, headers=sheaders)
            req_json = req.json()

            id2 = req_json["id"]
            token2 = req_json["token"]

            headers_auth1 = {"Authorization": f"Bearer {token1}"}
            headers_auth2 = {"Authorization": f"Bearer {token2}"}
            headers_patch = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token1}",
            }

            patch_content = {"referrer": f"{id2}"}
            await client.patch(
                f"{base_url_v2}/{id1}", headers=headers_patch, json=patch_content
            )

            await client.delete(f"{base_url_v2}/{id2}", headers=headers_auth2)

            key = random.choice(KEY_SAMPLES)

            put_content = {"license": f"{key}"}
            await client.put(
                f"{base_url_v2}/{id1}/account", headers=headers_patch, json=put_content
            )

            put_content = {"license": f"{license}"}
            await client.put(
                f"{base_url_v2}/{id1}/account", headers=headers_patch, json=put_content
            )

            req = await client.get(
                f"{base_url_v2}/{id1}/account", headers=headers_auth1
            )
            referral_count = req.json().get("referral_count", 0)

            await client.delete(f"{base_url_v2}/{id1}", headers=headers_auth1)

            return (
                license,
                referral_count,
                id1,
                token1,
                private_key,
                public_key,
                address,
                endpoint,
            )

    except Exception as error:
        return False, str(error)


async def single_license():
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            request = await client.post(BASE_URL, headers=HEADERS)
            id1 = request.json()["id"]
            license = request.json()["account"]["license"]
            token1 = request.json()["token"]

            request = await client.post(BASE_URL, headers=HEADERS)
            id2 = request.json()["id"]
            token2 = request.json()["token"]

            headers_auth1 = {"Authorization": f"Bearer {token1}"}
            headers_auth2 = {"Authorization": f"Bearer {token2}"}
            headers_patch = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Bearer {token1}",
            }

            content = {"referrer": f"{id2}"}
            await client.patch(f"{BASE_URL}/{id1}", headers=headers_patch, json=content)

            await client.delete(f"{BASE_URL}/{id2}", headers=headers_auth2)

            key = random.choice(KEY_SAMPLES)

            content = {"license": f"{key}"}
            await client.put(
                f"{BASE_URL}/{id1}/account", headers=headers_patch, json=content
            )

            content = {"license": f"{license}"}
            await client.put(
                f"{BASE_URL}/{id1}/account", headers=headers_patch, json=content
            )

            request = await client.get(
                f"{BASE_URL}/{id1}/account", headers=headers_auth1
            )
            referral_count = request.json().get("referral_count", 0)

            await client.delete(f"{BASE_URL}/{id1}", headers=headers_auth1)

            return license, referral_count, id1, token1

        except Exception as error:
            return False, str(error)


# ==============================[Main]============================== #


async def main():
    while True:
        clear()
        print(f"""{LOGO}\n\n\n
    {C_LCyan}[{C_Red}0{C_LCyan}] {C_White}Things You Should Know Before Use!
    {C_LCyan}[1] {C_White}Generate Single Warp+ License
    {C_LCyan}[2] {C_White}Generate Warp+ License (Wireguard)
    {C_LCyan}[3] {C_White}Create WireGuard QR Code
    {C_LCyan}[4] {C_White}About
    {C_LCyan}[5] {C_White}Exit\n\n""")

        Read = int(input(f"{C_Yellow}#> {C_White}Choice: "))

        if Read == 0 or Read == 1 or Read == 2 or Read == 3 or Read == 4 or Read == 5:
            if not (Read == 1):
                if not (Read == 2):
                    if not (Read == 3):
                        if not (Read == 4):
                            if not (Read == 5):
                                if Read == 0:
                                    clear()
                                    warns()
                            else:
                                exit()
                        else:
                            clear()
                            about()
                    else:
                        await single_wg()
                        input(
                            f"{C_Yellow}#> {C_White}Done! {C_Green}Press Enter to continue . . . "
                        )
                else:
                    clear()
                    print(LOGO)
                    print(
                        f" {C_White}[{C_Yellow}+{C_White}] Wait a while, Generating..."
                    )
                    print()
                    res1 = await gen_wireguard()
                    if res1[0] is False:
                        print(
                            f" {C_White}[{C_Red}-{C_White}] First Attemp Faild! Wait..."
                        )
                        if str(res1[1]) != "":
                            print(f" {C_White}[{C_Red}-{C_White}] Reason : " + str(res1[1]))
                        res2 = await gen_wireguard()
                        if res2[0] is False:
                            print(
                                f" {C_White}[{C_Red}-{C_White}] Faild To Generate! Please Try Again Later."
                            )
                            if str(res2[1]) != "":
                                print(
                                f" {C_White}[{C_Red}-{C_White}] Reason : "
                                + str(res2[1])
                                )
                                print()
                            input(
                                f"{C_Yellow}#> {C_Green}Press Enter to continue . . . "
                            )
                        else:
                            if int(res2[1]) < 1200:
                                print(
                                    f" {C_White}[{C_Red}-{C_White}] Faild To Gen Unlimited Data License! second Try..."
                                )
                                sec1 = gen_wireguard()
                                if int(sec1[1]) < 1200:
                                    print(
                                        f" {C_White}[{C_Red}-{C_White}] Faild To Generate Unlimited Data License! Please Try Again Later."
                                    )
                                    input(
                                        f"{C_Yellow}#> {C_Green}Press Enter to continue . . . "
                                    )
                                else:
                                    await wg_mode(res=sec1)
                            else:
                                await wg_mode(res=res2)
                    else:
                        if int(res1[1]) < 1200:
                            print(
                                f" {C_White}[{C_Red}-{C_White}] Faild To Gen Unlimited Data License! second Try..."
                            )
                            sec = await gen_wireguard()
                            if int(sec[1]) < 1200:
                                print(
                                    f" {C_White}[{C_Red}-{C_White}] Faild To Generate Unlimited Data License! Please Try Again Later."
                                )
                                print()
                                input(
                                    f"{C_Yellow}#> {C_Green}Press Enter to continue . . . "
                                )
                            else:
                                await wg_mode(res=sec)
                        else:
                            await wg_mode(res=res1)
            else:
                clear()
                print(LOGO)
                print()
                print(f" {C_White}[{C_Yellow}+{C_White}] Wait, Generating...")
                print()
                res1 = await single_license()
                if res1[0] is False:
                    print(f" {C_White}[{C_Red}-{C_White}] First Attemp Faild! Wait...")
                    if str(res1[1]) != "":
                        print(f" {C_White}[{C_Red}-{C_White}] Reason : " + str(res1[1]))
                    res2 = await single_license()
                    if int(res2[0]) is False:
                        print(
                            f" {C_White}[{C_Red}-{C_White}] Faild To Generate! Please Try Again Later."
                        )
                        if str(res2[1]) != "":
                            print(f" {C_White}[{C_Red}-{C_White}] Reason : " + str(res2[1]))
                            print()
                        input(f"{C_Yellow}#> {C_Green}Press Enter to continue . . . ")
                    else:
                        if int(res2[1]) < 1200:
                            print(
                                f" {C_White}[{C_Red}-{C_White}] Faild To Gen Unlimited Data License! second Try..."
                            )
                            sec1 = await single_license()
                            if int(sec1[1]) < 1200:
                                print(
                                    f" {C_White}[{C_Red}-{C_White}] Faild To Generate Unlimited Data License! Please Try Again Later."
                                )
                                print()
                                input(
                                    f"{C_Yellow}#> {C_Green}Press Enter to continue . . . "
                                )
                            else:
                                await single_mode(res=res2)
                else:
                    if int(res1[1]) < 1200:
                        print(
                            f" {C_White}[{C_Red}-{C_White}] Faild To Gen Unlimited Data License! second Try..."
                        )
                        sec2 = await single_license()
                        if int(sec2[1]) < 1200:
                            print(
                                f" {C_White}[{C_Red}-{C_White}] Faild To Generate Unlimited Data License! Please Try Again Later."
                            )
                            print()
                            input(
                                f"{C_Yellow}#> {C_Green}Press Enter to continue . . . "
                            )
                        else:
                            await single_mode(res=sec2)
                    else:
                        await single_mode(res=res1)
        else:
            message_box("Warp+ Tool", "      Please choose a number between 0-7!")


if __name__ == "__main__":
    asyncio.run(main())
