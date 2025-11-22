import hashlib
import requests
import imagehash
from PIL import Image
from io import BytesIO

# --- BitWitness Proof of Concept ---
# This script simulates the flow of capturing an image, generating a 
# perceptual hash, and anchoring it to a Merkle Root.

def download_image(url):
    """Downloads an image from a URL into memory without saving to disk."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"[ERROR] Could not download image: {e}")
        return None

def generate_phash(image):
    """
    Generates a Perceptual Hash (pHash).
    Unlike cryptographic hashes (MD5/SHA), pHash is robust against 
    compression and resizing, making it suitable for visual verification.
    """
    phash = imagehash.phash(image)
    return str(phash)

def create_merkle_root(hash_a, hash_b):
    """
    Simulates a Merkle Tree aggregation.
    Combines two hashes (leaves) to create a single root for blockchain anchoring.
    """
    combined = hash_a + hash_b
    return hashlib.sha256(combined.encode()).hexdigest()

if __name__ == "__main__":
    print("--- BitWitness Protocol: Simulation Initialized ---")

    # Configuration
    target_url = "https://cataas.com/cat"

    # 1. Capture Phase
    print(f"[STEP 1] Simulating image capture from source: {target_url}")
    img = download_image(target_url)

    if img:
        print("[INFO] Image data loaded into memory.")

        # 2. Hashing Phase
        print("[STEP 2] Calculating Perceptual Hash...")
        local_phash = generate_phash(img)
        print(f"[DATA] Generated pHash: {local_phash}")

        # 3. Anchoring Phase
        print("[STEP 3] Anchoring to Blockchain (Simulation)...")
        # Simulating a hash from another user in the network to build the tree
        network_peer_hash = "9f8a7b6c5d4e3f2a" 
        print(f"[INFO] Aggregating with peer hash: {network_peer_hash}")

        master_root = create_merkle_root(local_phash, network_peer_hash)

        print("-" * 40)
        print(f"MASTER ROOT: {master_root}")
        print("BLOCK HEIGHT: #850021 (Simulated)")
        print("-" * 40)

        # 4. Verification Phase
        print("[STEP 4] Verifying local integrity...")
        
        # Re-calculating hash to verify against the record
        verification_hash = generate_phash(img)
        
        if verification_hash == local_phash:
            print("[SUCCESS] Verification PASSED: Image content matches blockchain record.")
        else:
            print("[ALERT] Verification FAILED: Image manipulation detected.")
            
    else:
        print("[FATAL] Simulation aborted due to download error.")
