import web3 from "./getWeb3";
import Factory from "./build/Factory.json";

const instance = new web3.eth.Contract(
    // JSON.parse(Factory.interface), "0xab2557e6d39e00b2716665996ec211d45174f0c0"
    JSON.parse(Factory.interface), "0xa4d9a054e23d9d1e6bb7804cb8ff733410cbb647"
);

export default instance;
