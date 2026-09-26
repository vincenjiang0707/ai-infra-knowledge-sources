source: https://docs.nvidia.com/attestation/index.html

The NVIDIA Attestation Suite enhances Confidential Computing by providing robust mechanisms to ensure the integrity and security of devices and platforms. The suite includes NVIDIA Remote Attestation Service (NRAS), the Reference Integrity Manifest (RIM) Service, and the NVIDIA OCSP Service.

**NVIDIA Attestation Suite: Establish Absolute Trust in Your GPU Infrastructure**

Cryptographically verify the authenticity and integrity of your NVIDIA hardware and software — from a single GPU to a global fleet.

**What is Attestation?**

Attestation is the process of cryptographically verifying claims about hardware and software to establish trust between parties. It provides independent confirmation that systems are authentic, unmodified, and operating as intended—essential for security critical environments.

**Why GPU Attestation?**

**- Establishes Trust Foundation:**Cryptographically proves GPU hardware is genuine and running authentic NVIDIA firmware, creating the foundation of trust needed for secure computing

**- Critical for Confidential Computing:**Verifies hardware is operating in a secure, isolated environment before processing sensitive data and code

**- Enables Secure Execution:**Acts as the gatekeeper that verifies hardware integrity before allowing confidential computing modes

**Confidential Computing Integration**

Once attestation verifies the hardware, confidential computing protects sensitive data and code in use:

**Secure AI Training:**Train models with PII and sensitive data**Protected Inference:**Run inference with enterprise secrets safely**IP Protection:**Safeguard valuable AI model intellectual property

For detailed information, visit [https://docs.nvidia.com/nvtrust/index.html](https://docs.nvidia.com/nvtrust/index.html)

New to attestation? Get started here for immediate hands-on experience.

New to attestation? Get started here for immediate hands-on experience.

Learn how to transition from proof-of-concept to production deployment, including NGC onboarding and integration options

NVIDIA NGC Onboarding Guide for Attestation Services

NVIDIA RIM, NRAS and OCSP user manuals, guides, and releases.

CPP Attestation SDK user manuals, guides and releases

Attestation SDK Rust Bindings user manuals, guides and releases

PPCIE - CPP SDK user manuals, guides and releases

Python Attestation SDK user manuals, guides and releases

PPCIE - Python SDK user manuals, guides and releases

Claims guide and SDK troubleshooting documentation


NVIDIA has implemented an HBM3 memory channel repair mechanism on certain Hopper GPUs to improve reliability and reduce unnecessary RMAs (Return Merchandise Authorizations).