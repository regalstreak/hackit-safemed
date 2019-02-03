import web3 from "./getWeb3";
import Patient from "./build/Patient.json";

export default (address)=>{
    return new web3.eth.Contract(
        JSON.parse(Patient.interface),
        address
    );
};