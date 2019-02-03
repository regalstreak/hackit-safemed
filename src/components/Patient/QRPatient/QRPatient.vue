<template>
  <v-container fill-height>
    <v-layout row wrap align-center>
      <v-flex class="text-xs-center">
        <qrcode-vue :value="returnQRdata" :size="300" level="H"></qrcode-vue>
      </v-flex>
    </v-layout>
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
import store from "../../../store.js";
import web3 from "../../../util/getWeb3.js";
import QrcodeVue from "qrcode.vue";
export default {
  data() {
    return {
      account: "",
      patientAccount: ""
    };
  },
  components: {
    QrcodeVue
  },
  methods: {
    homeClicked() {
      this.$store.commit("changeBottomNavState", "home");
      this.$router.push("/patient");
    },
    qrClicked() {
      this.$store.commit("changeBottomNavState", "QR");
      this.$router.push("/patient/qr");
    },
    historyClicked() {
      this.$store.commit("changeBottomNavState", "history");
      this.$router.push("/patient/history");
    },
    accountClicked() {
      this.$store.commit("changeBottomNavState", "account");
      this.$router.push("/patient/account");
    }
  },
  computed: {
    bottomNav: {
      get() {
        return store.getters.bottomNavState;
      },
      set() {}
    },
    contractAddress: {
      get() {
        return store.getters.contractAddressState;
      },
      set() {}
    },
    returnQRdata() {
      return JSON.stringify({
        patient: this.patientAccount,
        contract: this.contractAddress
      });
    }
  },

  async created() {
    console.log("CONTRACT ADDRESS OF PATIENT: " + this.contractAddress);
    let accounts = await web3.eth.getAccounts();
    this.patientAccount = accounts[0];
  }
};
</script>

<style>
</style>
