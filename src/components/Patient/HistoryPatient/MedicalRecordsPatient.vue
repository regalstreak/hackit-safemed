<template>
  <v-container>
    <div v-for="(y, index2) in records" :key="index2" class="py-2">
      <v-card>
        <v-card-title class="teal lighten--1">
          <v-layout column>
            <v-flex xs6 justify-end align-end>
              <h3 class="display-1 white--text">Dr. {{ y[0] }}</h3>
            </v-flex>
          </v-layout>
        </v-card-title>
        <v-container>
          <v-layout column>
            <v-flex v-for="(n, index) in y[index2]" :key="index" xs4>
              <div v-if="index == 3">{{ formatDate(y[index]) }}</div>
              <div v-else>{{ y[index] }}</div>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </div>
  </v-container>
</template>

<script>
import patient from "/home/regalstreak/development/web/safemed/safemed/src/util/patient.js";
import web3 from "/home/regalstreak/development/web/safemed/safemed/src/util/getWeb3";
var moment = require("moment");

export default {
  async mounted() {
    const vm = this;
    console.log(this.contractAddress);
    let patientIn = patient(this.contractAddress);
    let accounts = await web3.eth.getAccounts();
    let numberofRec = await patientIn.methods._totalRecords().call();
    let returned;

    for (let i = numberofRec - 1; i >= 0; i--) {
      if (this.$store.getters.changePatient) {
        returned = await patientIn.methods
          .get_record(i)
          .call({ from: this.patientAddress });
      } else {
        returned = await patientIn.methods
          .get_record(i)
          .call({ from: accounts[0] });
      }
      this.records.push(returned);
    }
    console.log("sadasdasdsaad");
    console.log(this.records);

    // doctorsName: "",
    // hospital: "",
    // diagnose: "",
    // time: "",
    // dateIn: "",
    // dateOut: ""
  },
  data() {
    return {
      records: []
    };
  },
  computed: {
    contractAddress: {
      get() {
        return this.$store.getters.contractAddressState;
      },

      set() {}
    },
    patientAddress: {
      get() {
        return this.$store.getters.patientAddressState;
      },

      set() {}
    }
  },
  methods: {
    formatDate(unixtime) {
      return moment.unix(unixtime).format("YYYY-MM-DD hh:mm a");
    }
  }
};
</script>

<style>
</style>
