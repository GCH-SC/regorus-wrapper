import os
import setuptools

"""
Ensures the "dist" directory exists to store the built package.
"""
os.makedirs("dist", exist_ok=True)


setuptools.setup(
    name="regorus-wrapper",
    version="0.2.2",
    author="Haim Shulner",
    author_email="haim.shulner@gmail.com",
    include_package_data=True,
    description="Wrapper for platform-specific regorus wheels",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8,<3.13",
    install_requires=[
        # Linux (manylinux_x86_64)
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.8'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.9'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.10'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.11'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl ; sys_platform == 'linux' and python_version == '3.12'",

        # Windows (64-bit only)
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp38-none-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.8'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp39-none-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.9'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp310-none-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.10'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp311-none-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.11'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp312-none-win_amd64.whl ; sys_platform == 'win32' and python_version == '3.12'",

        # macOS (universal2: x86_64 and arm64)
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp39-cp39-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl ; sys_platform == 'darwin' and python_version == '3.9'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp310-cp310-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl ; sys_platform == 'darwin' and python_version == '3.10'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp311-cp311-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl ; sys_platform == 'darwin' and python_version == '3.11'",
        "regorus @ https://github.com/GCH-SC/regorus-wrapper/releases/download/0.2.2/regorus-0.2.2-cp312-cp312-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl ; sys_platform == 'darwin' and python_version == '3.12'",
    ],
)