# 14X040 - Advanced Security - Understanding Proof-of-Stake and its Security Implications through the Example of Ethereum 2.0

## Demonstration Scripts

This repository contains the demonstration scripts used in the presentation of th project "Understanding Proof-of-Stake and its Security Implications through the Example of Ethereum 2.0" for the course 14X040 - Advanced Security 

> The scripts are written in Python 3.12.3 and require the `hashlib` library to be installed. The scripts can be run using the command `python <script_name>.py`.

### Structure

- `block.py` and `blockchain.py` contain the implementation of a simple blockchain and block structure, implementing the Proof of Stake consensus algorithm.

> Runing these scripts will not produce any output, as they are only used as a base for the other scripts.

---

*The following scripts can be run as standalone scripts to demonstrate the different aspects of the Proof of Stake consensus algorithm:*

- `sim_v1.py` contains the simulation of the blockchain with a single validator.

- `nothiing_at_stake.py` contains the simulation of the blockchain, demonstrating the Nothing-at-Stake problem.

- `long_range_attacks.py` contains the simulation of the blockchain, demonstrating the Long Range Attack problem.

- `bribe_attacks.py` contains the simulation of the blockchain, demonstrating the an example of a bribe attack

---
*Dany A. Darghouth - May 2024*
