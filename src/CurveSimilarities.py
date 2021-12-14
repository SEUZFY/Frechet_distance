import Frechet

if __name__ == "__main__":
    P = [(1,1),(2,2)]
    Q = [(1,1),(2,2),(4,4)]
    print(Frechet.frechet_distance(P,Q)) 