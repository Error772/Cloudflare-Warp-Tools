# 🌐 Warp+ Tool 1.0

Warp+ Tool 1.0 is a utility for generating and managing Warp+ licenses and Wireguard configurations. It includes features for creating Wireguard configuration QR codes and managing Warp+ accounts, particularly for use with Cloudflare's Warp+ service.

## ✨ Features

-   🔑 Generate Warp+ licenses
-   ⚙️ Create and manage Wireguard configurations
-   📷 Generate QR codes for Wireguard configurations
-   🖥️ User-friendly console interface
-   ℹ️ Includes important usage information and warnings

## 📋 Requirements

-   Python 3.x
-   Required Python packages:
    -   `qrcode`
    -   `httpx`
    -   `nacl`
    -   `asyncio`
    -   `colorama`
    -   `Pillow`

You can install these dependencies using pip:

```sh
pip install qrcode httpx pynacl asyncio colorama Pillow
```

🛠️ Installation
Clone the repository:

```sh
git clone https://github.com/Error772/warp-plus-tool.git
```

Install the required Python packages:

```sh
pip install -r requirements.txt
```

Run the script:

```sh
python warp_tool.py
```

## 🚀 Usage

When you run the script, you will see a menu with several options. Follow the on-screen instructions to use the tool.

## 📜 Main Menu Options

-   ### Generate a Single Warp+ License:
    -   This option generates a single Warp+ license.
    -   Enter the required details as prompted.
-   ### Generate a Single Wireguard Configuration:
    -   This option generates a Wireguard configuration with a QR code.
    -   Enter the required details such as address and endpoint.
-   ### Generate a Wireguard QR Code:
    -   This option generates a QR code for an existing Wireguard configuration.
    -   Enter the required private key, public key, address, and endpoint.
-   ### About:
    -   Displays information about the tool and the developer.
-   ### Exit:
    -   Exits the tool.

## 🔧 Generating Wireguard Configuration

When generating a Wireguard configuration, the tool will:

-   Generate Wireguard private and public keys.
-   Create a Wireguard configuration file.
-   Generate a QR code for the configuration and save it as an image file.

## ⚠️ Warnings and Important Information

Before using the tool, it is important to read and understand the warnings provided in the tool. These warnings include:

-   The need for a VPN for certain users (e.g., Iranian users).
-   Potential issues and errors you may encounter and how to resolve them.
-   Legal and ethical considerations for using this tool.

## 🖼️ Generating QR Codes

The tool can generate QR codes for Wireguard configurations, which can be scanned to quickly configure devices. The QR code generation includes:

-   Fetching a Wireguard logo to embed in the QR code.
-   Creating a QR code with the Wireguard configuration details.
-   Saving the QR code as an image file.

## 🤝 Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## 👤 Authors

Ali Ayoubi - [Telegram : Error772](https://t.me/Error772)

## 📧 Contact

For questions or feedback, contact aliayoubiiii7@gmail.com.

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

> [!IMPORTANT]
> This tool is provided for educational purposes only. Using this tool may violate Cloudflare's terms of service. The developer is not responsible for any misuse or damage caused by this tool.