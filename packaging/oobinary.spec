Name:           oobinary
Version:        0.2.0
Release:        1%{?dist}
Summary:        Bit-level endianness converter, bitmask applicator, and stream aligner.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobinary
Source0:        oobinary-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobinary is a sovereign, capability-bounded BIT PACKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobinary
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobinary-uninstall

%files
/usr/bin/oobinary
/usr/bin/oobinary-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA bit packer with dual CLI/MCP interface
