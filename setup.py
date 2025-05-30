import os
import platform
import subprocess
import setuptools
import sys

"""
Ensures the "dist" directory exists to store the built package.
"""
os.makedirs("dist", exist_ok=True)

def get_linux_distro():
    """
    Detects the Linux distribution and version.
    Returns a tuple of (distro_name, version).
    """
    try:
        # Try using /etc/os-release first (most modern distributions)
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                lines = f.readlines()
                
            distro_info = {}
            for line in lines:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    distro_info[key] = value.strip('"\'')
            
            distro_name = distro_info.get('ID', '').lower()
            version = distro_info.get('VERSION_ID', '').lower()
            
            return distro_name, version
        
        # Fallback method 1: lsb_release command
        try:
            distro = subprocess.check_output(['lsb_release', '-is'], universal_newlines=True).strip().lower()
            version = subprocess.check_output(['lsb_release', '-rs'], universal_newlines=True).strip()
            return distro, version
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
            
        # Fallback method 2: Check specific distribution files
        if os.path.exists('/etc/amazon-linux-release'):
            return 'amzn', ''
        elif os.path.exists('/etc/system-release'):
            with open('/etc/system-release', 'r') as f:
                content = f.read().lower()
                if 'amazon linux' in content:
                    # Extract version if possible
                    if 'amazon linux 2' in content:
                        return 'amzn', '2'
                    elif 'amazon linux 2023' in content:
                        return 'amzn', '2023'
                    else:
                        return 'amzn', ''
        elif os.path.exists('/etc/debian_version'):
            return 'debian', open('/etc/debian_version', 'r').read().strip()
        elif os.path.exists('/etc/redhat-release'):
            return 'rhel', ''
        elif os.path.exists('/etc/centos-release'):
            return 'centos', ''
        elif os.path.exists('/etc/fedora-release'):
            return 'fedora', ''
        elif os.path.exists('/etc/SuSE-release'):
            return 'suse', ''
            
    except Exception as e:
        print(f"Warning: Could not determine Linux distribution: {e}")
    
    # Default fallback
    return 'unknown', ''

def get_glibc_version():
    """
    Attempts to determine the glibc version on the system.
    Returns the version as a string (e.g., "2.17", "2.34").
    """
    try:
        # Try to get glibc version from ldd
        ldd_output = subprocess.check_output(['ldd', '--version'], universal_newlines=True, stderr=subprocess.STDOUT)
        # Example output: "ldd (GNU libc) 2.34"
        for line in ldd_output.splitlines():
            if 'GNU libc' in line or 'glibc' in line:
                parts = line.split()
                for i, part in enumerate(parts):
                    if part in ('GNU libc)', 'glibc)'):
                        if i + 1 < len(parts):
                            return parts[i + 1]
                    elif part.startswith('2.'):
                        return part
    except Exception as e:
        print(f"Warning: Could not determine glibc version: {e}")
    
    # Default fallback - assume older glibc
    return "2.17"

def get_python_version_for_wheel():
    """
    Returns the Python version suitable for wheel selection.
    Returns string like "cp310", "cp311", "cp312"
    """
    python_version = sys.version_info
    return f"cp{python_version.major}{python_version.minor}"

# Determine appropriate wheel based on platform, architecture, and distro
def get_appropriate_wheels():
    """
    Get a list of appropriate wheels for different Python versions
    Returns a dictionary with Python version as key and wheel URL as value
    """
    sys_platform = platform.system().lower()
    machine = platform.machine().lower()
    current_py_version = get_python_version_for_wheel()
    
    # Base URL for all wheels
    base_url = "https://github.com/GCH-SC/regorus-wrapper/releases/download/0.4.0/"
    
    # Python versions to support
    python_versions = ["cp310", "cp311", "cp312"]
    
    # Store wheels for each Python version
    wheels = {}
    
    # Windows wheels
    if sys_platform == 'windows' or sys_platform.startswith('win'):
        for py_ver in python_versions:
            wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-win32.whl"
    
    # macOS wheels
    elif sys_platform == 'darwin':
        if machine == 'x86_64':
            for py_ver in python_versions:
                wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-macosx_10_12_x86_64.whl"
        elif machine == 'arm64':
            for py_ver in python_versions:
                wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-macosx_11_0_arm64.whl"
    
    # Linux wheels
    elif sys_platform == 'linux':
        # Get Linux distro info
        distro, version = get_linux_distro()
        glibc_version = get_glibc_version()
        
        print(f"Detected Linux distribution: {distro} {version}")
        print(f"Detected glibc version: {glibc_version}")
        print(f"Current Python version: {current_py_version}")
        
        # Special case for Amazon Linux
        if distro == 'amzn':
            # Amazon Linux 2 should use manylinux2014 (glibc 2.17) compatible wheels
            if version == '2':
                if machine == 'x86_64':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
                elif machine == 'aarch64':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl"
                elif machine == 'armv7l':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl"
            # Amazon Linux 2023 uses glibc 2.34, so can use the newer wheels
            elif version == '2023':
                if machine == 'x86_64':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_x86_64.whl"
                elif machine == 'aarch64':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_aarch64.whl"
                elif machine == 'armv7l':
                    for py_ver in python_versions:
                        wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_armv7l.whl"
        
        # Compare glibc versions to determine which manylinux to use
        use_newer_manylinux = False
        
        if glibc_version:
            major, minor = map(int, glibc_version.split('.', 1))
            if major > 2 or (major == 2 and minor >= 34):
                use_newer_manylinux = True
        
        # Modern distros likely using newer glibc (2.34+)
        if use_newer_manylinux or distro in ['ubuntu', 'debian', 'fedora', 'arch']:
            if machine == 'x86_64':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_x86_64.whl"
            elif machine == 'aarch64':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_aarch64.whl"
            elif machine == 'armv7l':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_34_armv7l.whl"
        else:
            # Older distros - use manylinux2014 (glibc 2.17)
            if machine == 'x86_64':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
            elif machine == 'aarch64':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl"
            elif machine == 'armv7l':
                for py_ver in python_versions:
                    wheels[py_ver] = f"{base_url}regorus-0.4.0-{py_ver}-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl"
    
    return wheels

# Create version-specific install dependencies
def generate_python_specific_dependencies():
    """
    Generates the dependencies list with version-specific constraints
    """
    wheels = get_appropriate_wheels()
    current_py_version = get_python_version_for_wheel()
    
    dependencies = ["wheel"]
    
    if not wheels:
        print("Warning: Could not determine appropriate wheels for this platform.")
        return dependencies
    
    # For each Python version, add a conditional dependency
    for py_ver, wheel in wheels.items():
        # Convert cp310 to 3.10, cp311 to 3.11, etc.
        py_ver_str = f"{py_ver[2]}.{py_ver[3:]}"
        
        # Add conditional dependency
        dependencies.append(
            f"regorus @ {wheel} ; python_version == '{py_ver_str}'"
        )
    
    return dependencies

# Get the dependencies with specific Python version constraints
dependencies = generate_python_specific_dependencies()

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
    install_requires=dependencies,
)