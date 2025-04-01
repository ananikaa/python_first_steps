```mermaid
graph TD;
    A(["Welcome user"]) --> n1(["Create a random number (1, 100)"])
    n1 --> n2(["Give choose a level"])
    n2 --> n3["Easy - 10 attempts"] & n4["Hard - 5 attempts"]
    n3 --> n5["Suggest to guess the number"]
    n4 --> n7["Suggest to guess the number"]
    n5 --> n8["If &gt; random number"] & n9["If &lt; random number"] & n16["If == random number"]
    n7 --> n10["If &gt; random number"] & n11["If &lt; random number"] & n18["If == random number"]
    n8 --> n12["Tell guessed number higher than random number"]
    n12 --> n13["Suggest to guess the number again and tell that attempts - 1. Until run out of attempts (10) then game over"]
    n9 --> n14["Tell guessed number lower than random number"]
    n14 --> n15["Suggest to guess the number again and tell that attempts - 1. Until run out of attempts (10) then game over"]
    n16 --> n17["You win"]
    n10 --> n19["Tell guessed number higher than random number"]
    n19 --> n20["Suggest to guess the number again and tell that attempts - 1. Until run out of attempts (5) then game over"]
    n11 --> n21["Tell guessed number lower than random number"]
    n21 --> n22["Suggest to guess the number again and tell that attempts - 1. Until run out of attempts (5) then game over"]
    n18 --> n23["You win"]
    n5@{ shape: rect}
