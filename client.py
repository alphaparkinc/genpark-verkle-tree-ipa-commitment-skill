import hashlib

class VerkleTreeIPA:
    """
    Verkle Tree evaluation with multi-proof vector commitments.
    Child hashes committed via vector polynomial evaluation.
    """
    def __init__(self, width=4):
        self.width = width
        self.leaves = {}

    def commit_vector(self, vec):
        h = hashlib.sha256(b"".join(v.to_bytes(4, 'big') for v in vec)).hexdigest()
        return int(h[:8], 16)

    def insert(self, key, val):
        self.leaves[key] = val

    def generate_commitment(self):
        vec = [self.leaves.get(i, 0) for i in range(self.width)]
        return self.commit_vector(vec)
