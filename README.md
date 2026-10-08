# oobinary: Sovereign BIT PACKER

<div align="center">

```
================================================================================
                                oobinary
               Sovereign openOODA BIT PACKER
================================================================================
```

**Sovereign BIT PACKER**  
*Bit-level endianness converter, bitmask applicator, and stream aligner.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oobinary/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oobinary-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oobinary/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oobinary/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oobinary-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oobinary/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oobinary [options] [INPUT_OR_FILE]

Capability-bounded endianness converter, bitmask applicator, and stream aligner.

Options:
  -h, --help               display this help and exit
  -v, --version            output version information and exit
  -b, --bits               display 8-bit binary representation (default)
      --swap16             invert 16-bit word byte pairs
      --swap32             invert 32-bit word byte order
      --swap64             invert 64-bit word byte order
  -e, --endian <16|32|64>  invert word byte order for specified width
  -m, --mask <VAL>         apply bitwise mask value (0-255)
      --op <and|or|xor|not> bitwise mask operator [default: xor]
  -a, --align <N>          pad byte stream to N-byte boundary [default: 1]
  -p, --pad <BYTE>         fill byte value for alignment padding [default: 0]
  -r, --reverse            reverse bit order within each byte
  -n, --length <N>         maximum bytes to inspect in bit view [default: 32]
  -f, --file <PATH>        read payload from file
      --json               output telemetry as formatted JSON
      --mcp                run as Model Context Protocol stdio server
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oobinary` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `binary_endian`: Invert word endianness across 16-bit, 32-bit, or 64-bit word boundaries.
* `binary_mask`: Apply bitwise AND, OR, XOR, or NOT masks across byte streams.
* `binary_align`: Pad byte streams to arbitrary power-of-two boundaries with custom fill values.
* `binary_bits`: Format raw bytes into structured 8-bit binary string representations.
* `binary_stats`: Query oobinary bit-packing engine specifications and available operations.

```bash
oobinary --mcp
```

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and bounded word widths.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
