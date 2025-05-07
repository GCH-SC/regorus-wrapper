import os
import setuptools

"""
Ensures the "dist" directory exists to store the built package.
"""
os.makedirs("dist", exist_ok=True)


setuptools.setup(
    name="regorus-wrapper",
    version="0.4.0",
    author="Haim Shulner",
    author_email="haim.shulner@gmail.com",
    include_package_data=True,
    description="Wrapper for platform-specific regorus wheels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8,<3.13",
    install_requires=[
    # Linux (manylinux_2_34)
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_34_aarch64.whl ; sys_platform == 'linux' and platform_machine == 'aarch64' and python_version == '3.11'",
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_34_armv7l.whl ; sys_platform == 'linux' and platform_machine == 'armv7l' and python_version == '3.11'",
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_34_x86_64.whl ; sys_platform == 'linux' and platform_machine == 'x86_64' and python_version == '3.11'",

    # Linux (manylinux_2_17 / manylinux2014)
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl ; sys_platform == 'linux' and platform_machine == 'aarch64' and python_version == '3.11'",
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl ; sys_platform == 'linux' and platform_machine == 'armv7l' and python_version == '3.11'",
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and platform_machine == 'x86_64' and python_version == '3.11'",

    # Windows (win32)
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-win32.whl ; sys_platform == 'win32' and python_version == '3.11'",

    # macOS (split targets)
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-macosx_10_12_x86_64.whl ; sys_platform == 'darwin' and platform_machine == 'x86_64' and python_version == '3.11'",
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-macosx_11_0_arm64.whl ; sys_platform == 'darwin' and platform_machine == 'arm64' and python_version == '3.11'",

    # Optional: universal2 fallback (works for both arm64 and x86_64)
    "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/regorus-0.4.0-cp310-abi3-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl ; sys_platform == 'darwin' and python_version == '3.11'",
    ],
    )