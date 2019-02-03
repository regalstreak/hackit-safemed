<template>
  <v-container>
    <v-timeline dense class="pb-4">
      <v-timeline-item
        v-for="(y, index2) in records"
        :key="index2"
        color="teal lighten--1"
        fill-dot
        right
      >
        <v-card>
          <v-card-title class="teal lighten--1">
            <v-layout column>
              <v-flex xs6 justify-end align-end>
                <h2 class="display-1 white--text">{{ y[0] }}</h2>
              </v-flex>
            </v-layout>
          </v-card-title>
          <v-container>
            <v-layout column>
              <v-flex v-for="(n, index) in y[index2]" :key="index" xs4>
                <div v-if="index == 3">{{ Date(y[index]) }}</div>
                <div v-else>{{ y[index] }}</div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-timeline-item>
    </v-timeline>

    <v-bottom-nav :active.sync="bottomNav" :value="true" fixed>
      <v-btn color="teal" @click="homeClicked" flat value="home">
        <span>Home</span>
        <v-icon>home</v-icon>
      </v-btn>

      <v-btn color="teal" @click="qrClicked" flat value="QR">
        <span>QR</span>
        <v-icon>texture</v-icon>
      </v-btn>

      <v-btn color="teal" @click="historyClicked" flat value="history">
        <span>History</span>
        <v-icon>history</v-icon>
      </v-btn>

      <v-btn color="teal" @click="accountClicked" flat value="account">
        <span>Account</span>
        <v-icon>person</v-icon>
      </v-btn>
    </v-bottom-nav>
  </v-container>
</template>

<script>
import doctor from "/home/regalstreak/development/web/safemed/safemed/src/util/doctor.js";
import web3 from "/home/regalstreak/development/web/safemed/safemed/src/util/getWeb3";
import patient from "../../../util/patient";
import factory from "/home/regalstreak/development/web/safemed/safemed/src/util/factory.js";
export default {
  async mounted() {
    console.log(this.contractAddress);
    let accounts = await web3.eth.getAccounts();
    let doctorin = doctor(this.contractAddress);
    this.patients = await doctorin.methods
      .retpatients()
      .call({ from: accounts[0] });
    // let nopatient=this.patients.length;
    this.patients.forEach(async ele => {
      let naddress = await factory.methods._patientsMapping[ele].call();
      let patientinstance = patient(naddress);
      this.records.push(
        patientinstance.methods.getBasicInfo().call({ from: accounts[0] })
      );
    });

    // doctorsName: "",
    // hospital: "",
    // diagnose: "",
    // time: "",
    // dateIn: "",
    // dateOut: ""
  },
  data() {
    return {
      records: [],
      patients: []
    };
  },
  computed: {
    contractAddress: {
      get() {
        return this.$store.getters.contractAddressState;
      },

      set() {}
    },
    bottomNav: {
      get() {
        return this.$store.getters.bottomNavState;
      },
      set() {}
    }
  },
  methods: {
    homeClicked() {
      this.$store.commit("changeBottomNavState", "home");
      this.$router.push("/doctor");
    },
    qrClicked() {
      this.$store.commit("changeBottomNavState", "QR");
      this.$router.push("/doctor/qr");
    },
    historyClicked() {
      this.$store.commit("changeBottomNavState", "history");
      this.$router.push("/doctor/history");
    },
    accountClicked() {
      this.$store.commit("changeBottomNavState", "account");
      this.$router.push("/doctor/account");
    }
  }
};
</script>

<style>
</style>