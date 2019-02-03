// import Web3 from "web3";

// const getWeb3 = () =>
//   new Promise((resolve, reject) => {
//     // Wait for loading completion to avoid race conditions with web3 injection timing.
//     window.addEventListener("load", async () => {
//       // Modern dapp browsers...
//       if (window.ethereum) {
//         const web3 = new Web3(window.ethereum);
//         try {
//           // Request account access if needed
//           await window.ethereum.enable();
//           // Acccounts now exposed
//           resolve(web3);
//         } catch (error) {
//           reject(error);
//         }
//       }
//       // Legacy dapp browsers...
//       else if (window.web3) {
//         // Use Mist/MetaMask's provider.
//         const web3 = window.web3;
//         console.log("Injected web3 detected.");
//         resolve(web3);
//       }
//       // Fallback to localhost; use dev console port by default...
//       else {
//         const provider = new Web3.providers.HttpProvider(
//           "http://192.168.6.138:22001"
//         );
//         const web3 = new Web3(provider);
//         console.log("No web3 instance injected, using Local web3.");
//         resolve(web3);
//       }
//     });
//   });

// export default getWeb3;

import Web3 from 'web3';

let web3;

if (typeof window !== 'undefined' && typeof window.web3 !== 'undefined') {
  // We are in the browser and metamask is running.
  web3 = new Web3(window.web3.currentProvider);
} else {
  // We are on the server *OR* the user is not running metamask
  const provider = new Web3.providers.HttpProvider(
    'http://192.168.6.138:22001'
  );
  web3 = new Web3(provider);
}

export default web3;