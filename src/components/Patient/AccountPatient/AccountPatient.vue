<template>
  <v-card height="200px" flat>
    <div class="headline text-xs-center pa-5">
      
    </div>
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
  </v-card>
</template>

<script>
import store from "../../../store.js";
export default {
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
      set() {
        
      }
    }
  }
};
</script>

<style>
</style>
