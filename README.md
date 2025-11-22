# BitWitness 
**The Open Source Protocol for Decentralized Reality Verification.**

> *"In a world of infinite generative AI, the only scarcity is truth."*

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Proof%20of%20Concept-orange.svg)
![Platform](https://img.shields.io/badge/platform-Mobile%20%7C%20Web-lightgrey)

## The Problem
We are entering the "Dead Internet" era.
* **Slop & Deepfakes:** Hyper-realistic AI models (Gemini 3, Nano Banana, Sora) are flooding social media.
* **Erosion of Trust:** Users can no longer distinguish between a real photo of a war zone and a generated fabrication.
* **The Detection Trap:** Traditional AI detectors are failing. They are an arms race we cannot win.

## The Solution: BitWitness
BitWitness flips the script. Instead of detecting the *fake*, we cryptographically verify the *real*.

We are building a **Chain of Trust** from the physical camera sensor to the user's screen. By combining **Hardware Attestation**, **Sensor Fusion**, and **Bitcoin Anchoring**, BitWitness creates an immutable proof that a specific image was captured by a real device, at a real location, at a specific time.

### How It Works (The 3 Layers)

#### 1. Hardware & Sensor Attestation (The Physical Root)
We verify the hardware, not just the file.
* **Secure Enclave Signing:** Uses the TEE (Trusted Execution Environment) in modern smartphones to sign image data. This proves the image originated from a physical camera sensor, not a software emulator.
* **PRNU Fingerprinting:** For standalone cameras, we analyze the unique sensor noise patterns to detect AI generation (which lacks natural sensor noise).

#### 2. Context & Sensor Fusion (The Reality Check)
We prevent "Re-photography" attacks (taking a photo of a screen).
* **3D Depth Verification:** Uses LiDAR/Depth API to reject flat 2D scenes (screens/prints).
* **Audio Ambiance:** Corroborates the visual scene with ambient audio analysis (e.g., a beach photo must sound like a beach).
* **Light Frequency:** Detects 50Hz/60Hz flicker from artificial light sources.

#### 3. The Immutable Anchor (Bitcoin)
* **Perceptual Hashing (pHash):** Creates a visual fingerprint that survives social media compression (Twitter/X, Instagram).
* **Merkle Tree Batching:** Aggregates thousands of proofs into a single hash.
* **Bitcoin OP_RETURN:** Anchors the root hash into the Bitcoin Blockchain. This makes the timestamp impossible to fake.

---

## Quick Start (Proof of Concept)
Want to see the math in action? We have a Python simulation of the hashing and anchoring logic.

### Prerequisites
```bash
pip install ImageHash requests Pillow
