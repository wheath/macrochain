// Add your code here
alert("setting up Thor");

const thor = new Connex.Thor({
    node: 'https://mainnet.veblocks.net/', // veblocks public node, use your own if needed
    network: 'main' // defaults to mainnet, so it can be omitted here
})


const 
const response = await fetch("https://api.vorj.app/main/v1/blockchain/nft/0x2a9f8d68d910e3ea7958b19b9f7e11ef61a14915?limit=10&contractAddress=0xe412dfcc5089feaa96e93878462c11754de0405b",
{
method:"GET",
headers: {
    "x-api-key":"d48528da3bb96395f232838949f6ef1b02c48ec79ce25346e9dea53cfe300327"
},
}
)

const best = await connex.thor.block().get();

console.log(JSON.stringify(response))
