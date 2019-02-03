<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column>
        <v-list light>
          <v-list-tile
            v-for="(item, index) in 4 "
            :key="index"
            avatar
            @click="navigate(item)"
          >
            <v-list-tile-avatar>
              <v-icon class="blue white--text">folder</v-icon>
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title>{{ item }}</v-list-tile-title>
              <v-list-tile-sub-title>Folder</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import patient from "/home/regalstreak/development/web/safemed/safemed/src/util/patient.js";
import web3 from "/home/regalstreak/development/web/safemed/safemed/src/util/getWeb3";
import factory from "/home/regalstreak/development/web/safemed/safemed/src/util/factory"
export default {
  async mounted() {
    console.log("232332434");
    console.log(this.contractAddress);
    let add=await factory.methods._patientsMapping[this.contractAddress].call();
    console.log(add);
    let patientIn = patient(this.contractAddress);
        console.log("232332434");

    let _totalhashes = await patientIn.methods._totalHashes();
        console.log("232332434");

    console.log(_totalhashes);    console.log("232332434");

    let returned;
    for (let i = _totalhashes - 1; i >= 0; i--) {
      console.log("someshloli");
      returned = await patientIn.methods.getHash(i).send({
        from: this.contractAddress,gasLimit:'4700000'
      });

      this.images.push(returned);
    }
    console.log(this.images);
    console.log(_totalhashes);

    // doctorsName: "",
    // hospital: "",
    // diagnose: "",
    // time: "",
    // dateIn: "",
    // dateOut: ""
    this.fetchData();
  },
  data() {
    return {
      images: [],
      buffermera: null
    };
  },
  computed: {
    contractAddress: {
      get() {
        return this.$store.getters.contractAddressState;
      },

      set() {}
    }
  },
  methods: {
    fetchData(data) {
      fetch(`https://ipfs.io/ipfs/${data}`).then(res => {
        res.arrayBuffer().then(buffer => {
          buffer = new Uint8Array(buffer);
          this.buffermera =
            "data:image/jpeg;base64," + buffer.toString("base64");
          console.log("sp,esjlp;o");
          return this.buffermera;
        });
      });
    }
  }
};
</script>

<style>
</style>
