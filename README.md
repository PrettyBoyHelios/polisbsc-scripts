# Polis on BSC Scripts and API

## Running
Download the token holders list from [BSCScan](https://bscscan.com/token/0xb5bea8a26d587cf665f2d78f077cca3c7f6341bd#balances), rename it to holders.csv and put it into the data folder.  
Until this is automated, this is required anytime you want to get up to date information.

```bash
pip install -r requirements.txt
python main.py
```

## Scope
This project will be updated to include multiple scripts that can be used as a reference to implement information services and applications for the [Polis Protocol](https://farms.polispay.org).  

Soon I'll start implementing an API using this scripts so information can be queried from the service, also with a frontend to interactively display the protocol's information.

## Donations
POLIS, BNB, ETH: 0xF8F14be2A3D129F21fAA53e208cF903043D267e0