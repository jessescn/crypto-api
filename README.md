# Crypto API

An API using Flask + Scrapy to provide data about cryto coins from [coinmarketcap](https://coinmarketcap.com/all/views/all/).

## Endpoints

### /crypto

Returns a JSON with  all crytocoins listed inside a coinmarketcap site.
```
 [{
    name: "Bitcoin",
    symbol: "BTC",
    market_cap: "$180,060,754,801",
    price: "10031.5125448",
    circulation_supply: "17949512.0",
    volume: "13615452153.7"
  },
  {
    name: "Ethereum",
    symbol: "ETH",
    market_cap: "$23,355,904,569",
    price: "216.585492684",
    circulation_supply: "107836883.624",
    volume: "7734900542.1"
  },
  ...
 ]
```


### /crypto/:symbol

Return a JSON with informations about a specific cryptocoin.
```
{
    name: "Bitcoin",
    symbol: "BTC",
    market_cap: "$180,060,754,801",
    price: "10031.5125448",
    circulation_supply: "17949512.0",
    volume: "13615452153.7"
}
```

## Configurations

This project is using pipenv for dependencies management.  

```bash
# Installing the dependencies management
$ pip install --user pipenv

# Installing all project dependencies
$ pipenv install

# Running the API
$ pipenv run start 
```

After that, you just need to access your [localhost:3000]('https://localhost:3000) and check if a message "API is on and running" has appeared. 


