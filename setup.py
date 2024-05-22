from setuptools import setup, find_packages

setup(
    name="WarpPlusTool",
    version="1.0",
    author="Ali Ayoubi",
    author_email="aliayoubiiii7@gmail.com",
    description="A tool for generating Warp+ licenses and Wireguard configurations.",
    url="https://github.com/Error772/Cloudflare-Warp-Tools.git",
    packages=find_packages(),
    install_requires=[
        "qrcode>=7.3",
        "httpx>=0.22.0",
        "asyncio>=3.4.3",
        "colorama>=0.4.4",
        "Pillow>=9.0.0",
        "pynacl>=1.5.0",
    ],
    entry_points={
        "console_scripts": [
            "warp-plus-tool=WarpPlusTool.main:main",
        ],
    },
)
