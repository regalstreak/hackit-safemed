import web3 from "./getWeb3";
import Doctor from "./build/Doctor.json";

export default (address)=>{
    return new web3.eth.Contract(
        JSON.parse(Doctor.interface),
        address
    );
};