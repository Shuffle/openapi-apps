# SoChain

SoChain is a block explorer and API for Bitcoin, Litecoin, Dogecoin and Zcash (transparent addresses), and their testnets. This app looks up addresses, transactions, blocks and network state, for example to enrich a wallet address or transaction ID found in an alert.

Networks: `BTC`, `LTC`, `DOGE`, `ZEC`, `BTCTEST` (Bitcoin testnet4), `LTCTEST`, `DOGETEST`, `ZECTEST`.

API documentation: https://sochain.com/docs

## Authentication

The API key is optional.

- Without a key, lookups are limited to 2,500 a day per IP. Leave the API key empty.
- With a key, the plan's monthly requests apply. A free account gives 75,000 requests a month; paid plans start at Hobby. Get a key at https://sochain.com/dashboard.

The key is sent in the `API-KEY` header. `Get account info` always needs a key.

```
curl -H "API-KEY: YOUR_KEY" https://sochain.com/api/v3/address_summary/BTC/bc1qxhmdufsvnuaaaer4ynz88fspdsxq2h9e9cetdj
```

## Actions

Addresses:
- Get balance (optionally at a block `height` or `time`)
- Get address summary: transaction counts, balances, total received, first and last activity
- Get transactions, and Get transactions by page (ten per page)
- Get transaction counts
- Get unspent outputs, and Get unspent outputs by page
- Is valid address
- Get balance history
- Get address rank
- Get address poisoning: look-alike addresses that sent the address dust
- Get address counterparties

Transactions and blocks:
- Get transaction
- Get transaction status: pending, mined, replaced or dropped
- Get block (by height or hash)
- Get latest blocks summary
- Get best block hash

Network:
- Get network info: newest block, mempool and fee rates
- Get price, Get price at (SoChain's price endpoint)
- Get chart
- Get rich list

Account:
- Get account info (needs a key)

## Responses

Answers are JSON: `{"status": "success", "data": {...}}`, or `{"status": "fail", "data": {"error_message": "..."}}` on an error. Amounts are exact decimal strings with 8 decimals, such as `"0.00012345"`.

| HTTP code | Meaning |
|---|---|
| 200 | Success |
| 400 | A bad parameter; the message says which |
| 401 | An invalid key, no key for Get account info, or the month's requests and the keyless rate both used up |
| 404 | An unknown network, address, transaction or block |
| 429 | Too many requests; wait the `Retry-After` seconds |
