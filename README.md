# BitWitness Protocol
**Open Source Standard for Decentralized Reality Verification**

> "In a world of infinite generative AI, the only scarcity is truth."

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Proof%20of%20Concept-orange.svg)
![Platform](https://img.shields.io/badge/platform-Mobile%20%7C%20Web-lightgrey)

## Abstract
The digital ecosystem is entering a crisis of provenance. High-fidelity generative AI models (such as Gemini 3, Nano Banana, and Sora) have democratized the creation of hyper-realistic synthetic media. Consequently, traditional detection methods are failing, creating an environment where users cannot distinguish between authentic capture and fabrication.

**BitWitness** proposes a shift in paradigm: rather than detecting the fake, the protocol cryptographically verifies the real. By establishing a chain of custody from the hardware sensor to the blockchain, BitWitness creates an immutable proof of existence for digital media.

## Architecture
The protocol creates a "Chain of Trust" comprising three distinct layers of verification.

### Layer 1: Hardware Attestation (The Physical Root)
Verification begins at the device level to prevent software emulation and injection attacks.
* **Secure Enclave Signing:** Utilizes the Trusted Execution Environment (TEE) found in modern smartphones to sign image data locally. This cryptographic signature confirms the data originated from a physical camera sensor.
* **PRNU Fingerprinting:** For standalone cameras, the protocol analyzes Photo Response Non-Uniformity (PRNU)—unique noise patterns inherent to specific silicon sensors—to distinguish optical capture from synthetic generation.

### Layer 2: Context & Sensor Fusion (The Environmental Check)
To mitigate "re-photography" attacks (capturing an image of a screen or print), BitWitness correlates visual data with environmental telemetry.
* **3D Depth Verification:** Utilizes LiDAR or Depth APIs to validate spatial depth, rejecting 2D planar subjects.
* **Audio Ambiance Analysis:** Corroborates the visual scene with a simplified hash of the ambient audio environment.
* **Signal Fingerprinting:** Analyzes local light frequency (50Hz/60Hz detection) to identify artificial lighting inconsistent with outdoor scenes.

### Layer 3: The Immutable Anchor (Settlement Layer)
* **Perceptual Hashing (pHash):** Generates a robust visual fingerprint based on frequency and structure, allowing verification to survive platform-specific compression algorithms (e.g., X, Instagram).
* **Merkle Tree Batching:** Aggregates user proofs into a Merkle Tree structure to ensure scalability.
* **Bitcoin Anchoring:** The Merkle Root is committed to the Bitcoin Blockchain via OP_RETURN transactions, providing a censorship-resistant and immutable timestamp.

---

## Strategic Roadmap: From App to Standard

BitWitness is architected not merely as an application, but as an interoperable protocol. The goal is integration into the native camera stack of operating systems.

### Phase 1: Reference Implementation (Current)
Development of a standalone mobile application.
* **Objective:** Validate the efficacy of hardware attestation and blockchain anchoring in a production environment.
* **Use Case:** Enabling journalists and high-risk users to capture verifiable media immediately.

### Phase 2: The SDK (Middleware)
Packaging the protocol into a lightweight Software Development Kit.
* **Objective:** Enable third-party applications (messaging platforms, social networks) to integrate "Verified Capture" without proprietary development.
* **Integration:** Developers import the BitWitness library to sign and verify media within their existing infrastructure.

### Phase 3: Native OS Integration (The Standard)
Integration at the Operating System (Android/iOS) and Image Signal Processor (ISP) level.
* **Objective:** "Verified Mode" becomes a native feature of the default camera application.
* **Vision:** Verification runs silently in the hardware background, making provenance the default standard for digital photography.

---

## Quick Start (Proof of Concept)
A Python simulation of the hashing and anchoring logic is available in this repository.

### Prerequisites
```bash
pip install ImageHash requests Pillow
