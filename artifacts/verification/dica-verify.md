Developer tools
Retrieve detailed information on address and token authorizations. Utilize API tools for domain risk detection, on-chain transaction broadcasting, and contract verification for both proxy and standard contracts.

Contract verification
Source code verification provides a way for projects to open source their smart contract code for end users to inspect and verify that it does what it claims to do and improve the transparency.

Endpoints of the "Contract verification" module support submitting contract source code for contract verification, verifying proxy contracts, and querying the contract ABI and source code of already verified contracts.

Verify contract source code
By uploading the contract source code, OKLink explorer will match the compiled contract bytecode with the bytecode on the blockchain and display it on the contract page of the explorer.

You can use this endpoint to quickly verify contracts and improve verification efficiency. The average processing time for contract verification is between 30-60 seconds.

Consumption per query 0
HTTP Request
POST /api/v5/explorer/contract/verify-source-code
lembrando que usamos ETHERSCAN_API_KEY e está em .env


requeest example
POST /api/v5/explorer/contract/verify-source-code
body
{
    "chainShortName":"ETH",
    "contractAddress":"0x9Dca580D2c8B8e19e9d77345a5b4C2820B25b386",
    "contractName":"HelloWorld",
    "sourceCode":"pragma solidity ^0.7.6;↵contract HelloWorl {↵ string public greet = 'Hello Worl!';↵}",
    "codeFormat":"solidity-single-file",
    "compilerVersion":"v0.7.6+commit.7338295f",
    "optimization":"1",
    "optimizationRuns":"200",
    "contractAbi":"0xfce353f66162630000000000000000000000000",
    "evmVersion":"tangerineWhistle",
    "viaIr":false,
    "libraryInfo":[
        {
        "libraryName":"libraryName1",
        "libraryAddress":"0xCfE28868F6E0A24b7333D22D8943279e76aC2cdc"
        },
        {
        "libraryName":"libraryName2",
        "libraryAddress":"0xCfE28868F6E0A24b7333D22D8943279e76aC2cdc"
        },
        {
        "libraryName":"libraryName3",
        "libraryAddress":"0xCfE28868F6E0A24b7333D22D8943279e76aC2cdc"
        }
    ]
}


Get contract source code verification results
After submitting the source code verification, you can query the result with the GUID returned.

Consumption per query 0
HTTP Request
POST /api/v5/explorer/contract/check-verify-result

Request Example

POST /api/v5/explorer/contract/check-verify-result
body
{
    "chainShortName":"ETH",
    "guid":"eb5c06099d3841359d398541166343fe"
}
Request Parameters
Parameter	Type	Required	Description
chainShortName	String	Yes	The abbreviated name of the blockchain network
guid	String	Yes	Query the source code verification result with the GUID returned
Response Example

{
    "code": "0",
    "msg": "",
    "data": [
        "Success"
    ]
}
Response Parameters
Parameter	Type	Description
result	String	Contract source code verification result
Success,Fail,Pending

Verify proxy contract
Verify whether a proxy contract implements the contract as expected.

Consumption per query 0
HTTP Request
POST /api/v5/explorer/contract/verify-proxy-contract

Request Parameters
Parameter	Type	Required	Description
chainShortName	String	Yes	The abbreviated name of the blockchain network
proxyContractAddress	String	Yes	Proxy contract address
expectedImplementation	String	No	Verify whether the implementation contract for the proxy contract is this address
Response Example

{
    "code": "0",
    "msg": "",
    "data": [
        "4f2e75682f75410f958c0a3bbf754358"
    ]
}
Response Parameters
Parameter	Type	Description
guid	String	A GUID is returned upon successful submission, which can be used to query the verification result


Get proxy contract verification results
After submitting the proxy contract verification, you can query the result with the GUID returned.

Consumption per query 0
HTTP Request
POST /api/v5/explorer/contract/check-proxy-verify-result


Request Parameters
Parameter	Type	Required	Description
chainShortName	String	Yes	The abbreviated name of the blockchain network
guid	String	Yes	Query the proxy contract verification result with the GUID returned
Response Example

{
    "code": "0",
    "msg": "The proxy's (0x826427966fb2e7edee940c5d99b7d66062faef2e) implementation contract is found at 0xd4a2dca4e03713d5bf7d2173237058466a9c1be4 and is successfully updated.",
    "data": []
}
Response Parameters
Parameter	Type	Description
result	String	Proxy contract verification result.
If the verification is successful, return the address of the implementation contract.
If the verification fails, return "A corresponding implementation contract was unfortunately not detected for the proxy address."


Get verified contract's ABI and source code
Query the contract ABI, source code and other basic information of the verified contract, or query the implementation contract address information of the verified proxy contract.

Consumption per query 0
HTTP Request
GET /api/v5/explorer/contract/verify-contract-info

Request Example

/api/v5/explorer/contract/verify-contract-info?chainShortName=ETH&contractAddress=0xcF80631b469A54dcba8c8ee1aF84505f496ed248
Request Parameters
Parameter	Type	Required	Description
chainShortName	String	Yes	The abbreviated name of the blockchain network
contractAddress	String	Yes	Contract address



Response Parameters
Parameter	Type	Description
sourceCode	String	Source code of the contract
contractName	String	Contract name
compilerVersion	String	Compiler version used
optimization	String	Whether optimization was used when compiling the contract, 0 for no optimization, 1 if optimization was used
optimizationRuns	String	The number of runs if optimization was used
contractAbi	String	Contract ABI
evmVersion	String	EVM version of contract compilation
licenseType	String	Open source license type
libraryInfo	Array	Library info used in contract
> libraryName	String	Library name
> libraryAddress	String	Library address, e.g., 0xCfE28868F6E0A24b7333D22D8943279e76aC2cdc
proxy	String	Whether it is a proxy contract, 0 means it is not a proxy contract, 1 means it is a proxy contract
implementation	String	The implementation contract address of the proxy contract
swarmSource	String	Swarm hash of contract source code
