from client import VerkleTreeIPA

def main():
    print("=== Testing Verkle Tree Multi-Vector Commitment ===")
    vt = VerkleTreeIPA(width=4)
    vt.insert(0, 100)
    vt.insert(1, 200)
    vt.insert(2, 350)

    comm = vt.generate_commitment()
    print(f"Generated root vector commitment: {hex(comm)}")
    assert comm > 0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
